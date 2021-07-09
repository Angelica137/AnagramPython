def findAnagram(str, arr):
    anagrams = []
    for item in range(len(arr)):
        if len(arr[item]) == len(str):
            sorted_item = sorted(arr[item])
            sorted_str = sorted(str)
            if sorted_item == sorted_str:
                anagrams.append(arr[item])
    return anagrams
