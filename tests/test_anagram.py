def test_anagram_returns_anagram_if_anagram():
	a = Anagram()
	assert a.findAnagram("list", ["lit"]) == "lit"