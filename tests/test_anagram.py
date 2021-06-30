from scripts.anagram import Anagram


def test_findAnagram_knows_word_is_same_length():
    a = Anagram()
    assert len(a.findAnagram("list", ["istl"])[0]) == 4


def test_anagram_returns_anagram_if_anagram():
    a = Anagram()
    assert a.findAnagram("list", ["istl"]) == ["istl"]


def test_anargam_returns_correct_anagrams_when_list_greater_one():
    a = Anagram()
    assert a.findAnagram("list", ["lit", "it", "otter"]) == []


def test_anargam_returns_correct_anagrams_when_list_greater_one():
    a = Anagram()
    assert a.findAnagram("listen", ["enlist", "inlets", "google"]) == [
        "enlist", "inlets"]
