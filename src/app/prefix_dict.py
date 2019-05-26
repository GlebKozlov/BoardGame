class PrefixDict:
    """
    Simple dict with prefixes and words as Key and and bool marker for full words as Value
    """

    def __init__(self):
        self.words = {}

        self.is_full_word = False

    def get_child(self, word):
        is_word = self.words.get(word, None)
        if is_word is None:
            return None

        child = PrefixDict()
        child.words = self.words
        child.is_full_word = is_word

        return child

    @classmethod
    def make_dict(cls, words):
        """
        Reads words and stores it into dict with all of prefixes.
        Full word marks as True, and prefix as False
        """

        if not len(words):
            raise ValueError("empty words list")

        dictionary = cls()

        for word in words:
            for i in range(len(word)):
                prefix = word[:i]
                if prefix not in dictionary.words:
                    dictionary.words[prefix] = False
            dictionary.words[word] = True

        return dictionary
