class Anagram:
    def findAnagram(self, str, arr):
        anagrams = []
        for item in range(len(arr)):
            count = 0
            for char in arr[item]:
                for j in range(len(str)):
                    if char == str[j]:
                        count += 1
                        break
            if count == len(arr[item]):
                anagrams.append(arr[item])
        return anagrams


a = Anagram()
a.findAnagram("list", ["lit"])

a2 = Anagram()
a2.findAnagram("list", ["lit", "it", "otter"])
