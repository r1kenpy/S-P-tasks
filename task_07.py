def combine_anagrams(words_array):
    anagram_groups = {}
    for word in words_array:
        letters_in_word = ''.join(sorted(word))
        if letters_in_word not in anagram_groups:
            anagram_groups[letters_in_word] = [word]
        else:
            anagram_groups[letters_in_word].append(word)

    return sorted(anagram_groups.values())
