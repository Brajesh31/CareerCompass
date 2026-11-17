from __future__ import annotations

import ast
import re
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def clean_resume():
    """Load only the pure helper AST, avoiding app.py startup side effects."""
    app_path = Path(__file__).resolve().parents[1] / "app.py"
    tree = ast.parse(app_path.read_text(encoding="utf-8"), filename=str(app_path))
    function = next(
        (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "clean_resume"),
        None,
    )
    if function is None:
        pytest.fail("app.py must define clean_resume(text)")

    isolated_module = ast.Module(body=[function], type_ignores=[])
    ast.fix_missing_locations(isolated_module)
    namespace = {"re": re}
    exec(compile(isolated_module, str(app_path), "exec"), namespace)
    return namespace["clean_resume"]


def test_normal_resume_text_is_normalized(clean_resume):
    result = clean_resume("Senior Python developer, with 5+ years of experience.")
    assert result == "Senior Python developer with 5 years of experience"


def test_urls_hashtags_and_mentions_are_removed(clean_resume):
    result = clean_resume("Python developer https://example.test #OpenToWork @candidate")
    assert result == "Python developer"


def test_repeated_whitespace_is_collapsed(clean_resume):
    result = clean_resume("  Python\tDeveloper\nwith   API skills  ")
    assert result == "Python Developer with API skills"


def test_result_is_a_string(clean_resume):
    assert isinstance(clean_resume("Data analyst"), str)
