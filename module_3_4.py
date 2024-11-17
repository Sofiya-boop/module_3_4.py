def single_root_words(root_word, *other_words):
    same_words = []
    root_length = len(root_word)
    for i in other_words:
        if i.startswith(root_word) or root_word.startswith(i) and i != root_word:
            same_words.append(i)
    print(same_words)
    return(same_words)
