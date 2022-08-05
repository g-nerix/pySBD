import pytest

GOLDEN_ML_RULES_TEST_CASES = []

@pytest.mark.parametrize('text,expected_sents', GOLDEN_ML_RULES_TEST_CASES)
def test_ml_sbd(ml_default_fixture, text, expected_sents):
    """malayalam language SBD tests"""
    segments = ml_default_fixture.segment(text)
    assert segments == expected_sents