import pytest

GOLDEN_BN_RULES_TEST_CASES = []

@pytest.mark.parametrize('text,expected_sents', GOLDEN_BN_RULES_TEST_CASES)
def test_bn_sbd(bn_default_fixture, text, expected_sents):
    """bengali language SBD tests"""
    segments = bn_default_fixture.segment(text)
    assert segments == expected_sents