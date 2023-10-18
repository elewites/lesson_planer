from .base_data_handler import BaseDataHandler


def test_get_all_sentences():
    handler = BaseDataHandler()
    sections = ["section_1", "section_2"]
    sentences = ["Sentence 1", "Sentence 2", "Sentence 3"]

    for section in sections:
        for sentence in sentences:
            handler.add_sentence(section, sentence)

    retrieved_sentences = handler.get_sentences()
    assert retrieved_sentences["section_1"] == sentences
    assert retrieved_sentences["section_2"] == sentences


def test_get_all_words():
    handler = BaseDataHandler()
    sections = ["section_3", "section_4"]
    words = ["apple", "banana", "cherry"]

    for section in sections:
        for word in words:
            handler.add_word(section, word)

    retrieved_words = handler.get_words()
    assert retrieved_words["section_3"] == words
    assert retrieved_words["section_3"] == words


def test_add_sentence():
    handler = BaseDataHandler()
    section_name = "section_1"
    sentence = "This is a test sentence."
    handler.add_sentence(section_name, sentence)
    sentences = handler.get_sentence_section(section_name)
    assert sentence in sentences


def test_add_bulk_sentences():
    # Test adding a list of sentences to a specific section
    # Create a clean data handler and initialize it
    data_handler = BaseDataHandler()
    section = "section_2"
    sentences_to_add = ["Sentence Two", "Sentence Three"]
    data_handler.add_bulk_sentences(section, sentences_to_add)
    assert data_handler.get_sentence_section(section) == sentences_to_add


def test_add_word():
    handler = BaseDataHandler()
    section_name = "section_2"
    word = "apple"
    handler.add_word(section_name, word)
    words = handler.get_word_section(section_name)
    assert word in words


def test_remove_sentence():
    handler = BaseDataHandler()
    section_name = "section_3"
    sentence = "This is another test sentence."
    handler.add_sentence(section_name, sentence)
    handler.remove_sentence(section_name, sentence)
    sentences = handler.get_sentence_section(section_name)
    assert sentence not in sentences


def test_remove_word():
    handler = BaseDataHandler()
    section_name = "section_4"
    word = "banana"
    handler.add_word(section_name, word)
    handler.remove_word(section_name, word)
    words = handler.get_word_section(section_name)
    assert word not in words
