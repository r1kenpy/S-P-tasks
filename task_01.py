def is_palindrom(text=None):
    if text is None:
        return False
    text = str(text)
    for i in text:
        if not i.isalnum():
            text = text.replace(i, '')
    return text.lower() == text[::-1].lower()


# or


def is_palindrome_two_pointers(text=None):
    if text is None:
        return False
    text = str(text)
    left, right = 0, len(text) - 1

    while left <= right:
        if not text[left].isalnum():
            left += 1
            continue
        if not text[right].isalnum():
            right -= 1
            continue
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True
