"""Publication-contract checks that run in the raw-data-free Paper 1 archive."""

import re
from pathlib import Path

from scripts.build_jeet_submission import parse_bibtex

ROOT = Path(__file__).resolve().parents[1]
JOM = ROOT / "submission/jom"


def test_short_abstract_retains_the_external_failure_and_comparator_boundary() -> None:
    main = (JOM / "manuscript.md").read_text()
    abstract = main.split("## Abstract", 1)[1].split("**Keywords:**", 1)[0]
    assert 100 <= len(abstract.split()) <= 150
    for value in (
        "95.71%",
        "exploratory",
        "96/384",
        "25.00%",
        "1/32",
        "0.6354",
        "15.74%",
        "12%",
        "70.05%",
        "three of five",
        "one external motor",
    ):
        assert value in abstract
    keywords = main.split("**Keywords:**", 1)[1].split("##", 1)[0]
    assert 3 <= len(keywords.split(";")) <= 6


def test_current_citations_and_independent_figure_paths_resolve() -> None:
    entries = parse_bibtex(ROOT / "references/key_papers.bib")
    entries.update(parse_bibtex(JOM / "jom_references.bib"))
    main = (JOM / "manuscript.md").read_text()
    citations = re.findall(r"\[([^\]]*@[A-Za-z0-9_:-]+[^\]]*)\]", main)
    keys = {key for group in citations for key in re.findall(r"@([A-Za-z0-9_:-]+)", group)}
    assert keys <= set(entries)
    images = re.findall(r"^!\[.*?\]\((.*?)\)$", main, re.MULTILINE)
    assert len(images) == 6
    assert all((JOM / path).resolve().is_file() for path in images)
    assert "Frozen Cross-Dataset Reliability" in main
    assert "Frozen Cross-Dataset Reliability" in (JOM / "cover_letter.md").read_text()
