from scripts.anagram import Anagram


def test_anagram_returns_anagram_if_anagram():
    a = Anagram()
    assert a.findAnagram("list", ["lit"]) == ["lit"]


def test_anargam_returns_correct_anagrams_when_list_greater_one():
    a = Anagram()
    assert a.findAnagram("list", ["lit", "it", "otter"]) == ["lit", "it"]
