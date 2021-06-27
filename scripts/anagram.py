class Anagram:
    def findAnagram(self, str, arr):
        count = 0
        for i in range(len(arr)):
            print(arr[i])
            for j in range(len(str)):
                if arr[i] == str[j]:
                    count += 1
                    break
        if count == len(arr):
            print("is anagram")
            return arr
        else:
            print("no anagram")


a = Anagram()

a.findAnagram("list", "lit")
