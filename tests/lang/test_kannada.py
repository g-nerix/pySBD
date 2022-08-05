import pytest

GOLDEN_KN_RULES_TEST_CASES = []

@pytest.mark.parametrize('text,expected_sents', GOLDEN_KN_RULES_TEST_CASES)
def test_kn_sbd(kn_default_fixture, text, expected_sents):
    """kannada language SBD tests"""
    segments = kn_default_fixture.segment(text)
    assert segments == expected_sents