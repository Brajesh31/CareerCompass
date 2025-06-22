import streamlit as st
from streamlit_oauth import OAuth2Component
import pickle
import re
import nltk
import requests
from dotenv import load_dotenv
import os
from streamlit_extras.stylable_container import stylable_container

load_dotenv()

nltk.download('punkt')
nltk.download('stopwords')

#loading models
clf = pickle.load(open('clf.pkl','rb'))
tfidfd = pickle.load(open('tfidf.pkl','rb'))

script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the image relative to the script directory
image_url = "https://images.unsplash.com/photo-1614852206732-6728910dc175?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

with st.container():
    st.write(
        f"""
        <style>
            .stApp {{
                background-image: url("{image_url}");
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def clean_resume(resume_text):
    clean_text = re.sub('http\\S+\\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\\S+', '', clean_text)
    clean_text = re.sub('@\\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\\s+', ' ', clean_text)
    return clean_text

# Function to fetch LinkedIn jobs
def fetch_linkedin_jobs(api_key, field, geoid, page):
    url = "https://api.scrapingdog.com/linkedinjobs/"
    params = {
        "api_key": api_key,
        "field": field,
        "geoid": geoid,
        "page": page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            return data
        else:
            return data.get("jobs", [])
    else:
        return []

# web app
def main():

    # authorization details
    AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"
    TOKEN_URL = "https://oauth2.googleapis.com/token"
    # REVOKE_URL = <YOUR REVOKE URL>
    CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    REDIRECT_URI = "https://careercompassupes.streamlit.app"
    SCOPE = "openid email profile"
    
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_URL, TOKEN_URL, TOKEN_URL)

    if 'token' not in st.session_state:
      
        st.markdown(
    """
    <div style='background-color: white; padding: 20px; border-radius: 10px;'>
        <h1 style='color: #333333;'>Consent and Privacy Policy</h1>
        <p style='color: #333333;'>Thank you for choosing Career Compass, your AI-powered career companion. Our commitment to your privacy is paramount, and we've crafted this Consent and Privacy Policy to transparently detail how we handle your data.</p>
        <ol style='color: #333333;'>
            <li>Information We Collect: We gather resume details, including contact info, education, work history, and skills.</li>
            <li>How We Use Your Information: We analyze your resume to offer personalized job recommendations, enhance our service based on usage patterns.</li>
            <li>Data Security: We employ robust measures to safeguard your data from unauthorized access, alteration, or disclosure.</li>
            <li>Data Sharing: Your data remains confidential. We share it only as necessary for providing our services, legal compliance, or safeguarding our rights.</li>
            <li>Your Consent: By using Career Compass, you consent to our data practices as outlined in this policy.</li>
            <li>Access and Control: You have the right to access, correct, or delete your data. You can also opt-out of communications at any time.</li>
            <li>Changes to This Policy: We may update this policy periodically, and any changes will be reflected here.</li>
            <li>Contact Us: For inquiries or requests regarding this policy or your data, reach out to us at aakshitasingh786@gmail.com.</li>
        </ol>
        <p style='color: #333333;'>By using Career Compass, you acknowledge and agree to abide by the terms of this Consent and Privacy Policy.</p>
    </div>
    <br />
    """,
    unsafe_allow_html=True
)
        result = oauth2.authorize_button("Continue with Google", REDIRECT_URI, SCOPE, icon="data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 48 48'%3E%3Cdefs%3E%3Cpath id='a' d='M44.5 20H24v8.5h11.8C34.7 33.9 30.1 37 24 37c-7.2 0-13-5.8-13-13s5.8-13 13-13c3.1 0 5.9 1.1 8.1 2.9l6.4-6.4C34.6 4.1 29.6 2 24 2 11.8 2 2 11.8 2 24s9.8 22 22 22c11 0 21-8 21-22 0-1.3-.2-2.7-.5-4z'/%3E%3C/defs%3E%3CclipPath id='b'%3E%3Cuse xlink:href='%23a' overflow='visible'/%3E%3C/clipPath%3E%3Cpath clip-path='url(%23b)' fill='%23FBBC05' d='M0 37V11l17 13z'/%3E%3Cpath clip-path='url(%23b)' fill='%23EA4335' d='M0 11l17 13 7-6.1L48 14V0H0z'/%3E%3Cpath clip-path='url(%23b)' fill='%2334A853' d='M0 37l30-23 7.9 1L48 0v48H0z'/%3E%3Cpath clip-path='url(%23b)' fill='%234285F4' d='M48 48L17 24l-4-3 35-10z'/%3E%3C/svg%3E")
        if result:
            st.session_state.token = result.get('token')
            st.rerun()
    if 'token' in st.session_state:
        # remaining code after authorization
        st.title("Job Recommendation System")
        uploaded_file = st.file_uploader('Upload Resume', type=['txt','pdf'])
        
        if uploaded_file is not None:
            try:
                resume_bytes = uploaded_file.read()
                resume_text = resume_bytes.decode('utf-8')
            except UnicodeDecodeError:
                # If UTF-8 decoding fails, try decoding with 'latin-1'
                resume_text = resume_bytes.decode('latin-1')

            cleaned_resume = clean_resume(resume_text)
            input_features = tfidfd.transform([cleaned_resume])
            prediction_id = clf.predict(input_features)[0]

            # Map category ID to category name
            category_mapping = {
                15: "Java Developer",
                23: "Testing",
                8: "DevOps Engineer",
                20: "Python Developer",
                24: "Web Designing",
                12: "HR",
                13: "Hadoop",
                3: "Blockchain",
                10: "ETL Developer",
                18: "Operations Manager",
                6: "Data Science",
                22: "Sales",
                16: "Mechanical Engineer",
                1: "Arts",
                7: "Database",
                11: "Electrical Engineering",
                14: "Health and fitness",
                19: "PMO",
                4: "Business Analyst",
                9: "DotNet Developer",
                2: "Automation Testing",
                17: "Network Security Engineer",
                21: "SAP Developer",
                5: "Civil Engineer",
                0: "Advocate",
            }

            category_name = category_mapping.get(prediction_id, "Unknown")

            st.write("Predicted Category:", category_name)


            # Fetch LinkedIn jobs based on recommended job role
            st.header("Recommended LinkedIn Jobs")
            jobs = fetch_linkedin_jobs("667d84db3582a3358da423d3", category_name, "102713980", "1")
            if jobs:
                for job in jobs:
                    with stylable_container(
                        key=f"job_{job['job_id']}_container",
                        css_styles="""
                            {
                                border: 3px solid #ffffff;
                                border-radius: 0.5rem;
                                margin-bottom: 1rem;
                                padding: 1em 0.5rem;
                                box-sizing: border-box;
                            }
                            """,
                    ):  
                        st.markdown(f"<h3 style='font-size: 1.25rem'>{job['job_position']}</h3>", unsafe_allow_html=True)
                        st.write("Company Name:", job["company_name"]) 
                        st.write("Location:", job["job_location"]) 
                        st.write("Posting Date:", job["job_posting_date"]) 
                        st.write("Job Link:", job["job_link"])
            else:
                st.warning("No jobs found. Please try again.")

# python main
if __name__ == "__main__":
    main()