def valid_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# O(n * log(n))