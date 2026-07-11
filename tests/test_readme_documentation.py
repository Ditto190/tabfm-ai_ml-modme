from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"


def _readme_text() -> str:
  return README.read_text(encoding="utf-8")


def test_readme_warns_about_default_weight_license():
  text = _readme_text()

  assert "Apache-2.0" in text
  assert "tabfm-non-commercial-v1.0" in text
  assert "Commercial or production use" in text
  assert "not permitted" in text
  assert "Hugging Face" in text


def test_readme_answers_grouped_documentation_faqs():
  text = _readme_text()

  assert "Is there a maximum table size" in text
  assert "max_num_features" in text
  assert "max_num_rows" in text
  assert "Is there a TabFM technical report or paper?" in text
