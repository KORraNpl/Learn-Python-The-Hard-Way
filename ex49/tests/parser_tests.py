from nose.tools import *
from ex49 import parser

def test_parse_sentence():
    word_list = [('verb', 'run'), ('direction', 'north')]
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'run')
    assert_equal(sentence.object, 'north')

def test_parse_sentence_exception():
    word_list = [('test', 'testing')]
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)