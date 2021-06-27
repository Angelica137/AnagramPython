class Anagram:
    def findAnagram(self, str, arr):
        for item in range(len(arr)):
            count = 0
            for char in arr[item]:
                for j in range(len(str)):
                    if char == str[j]:
                        count += 1
                        break
            if count == len(arr[item]):
                print("is anagram")
                return arr
            else:
                print("no anagram")


a = Anagram()

a.findAnagram("list", ["lit"])
