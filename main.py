def single_rot_words(root_word, *other_words):
    same_words = [ ]
    root_word = root_word.lower()

    for word in other_words:

        if word.lower() in root_word or root_word in word.lower():
            same_words.append(word)
    return same_words

result1 = single_rot_words('rich', 'richest','orichalcum', 'cheers','richies')
result2 = single_rot_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)