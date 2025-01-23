import re
from typing import Union

DEFAULT_STOPWORDS_PATH = "../data/stopwords-am.txt"

def remove_punctuation(text: str) -> str:
    """removes punctuations from a given amharic text"""
    punctuations = "[፠፡።፣፤፥፦፧፨.,:;%&*#@$()/}{\-_|]"
    return re.sub(punctuations, " ", text)


def normalize(text: str) -> str:
    """
    normalize amharic text
    """
    char_map = {
        '[ሃኅኃሐሓኻ]': 'ሀ',
        '[ሑኁዅ]': 'ሁ',
        '[ኂሒኺ]': 'ሂ',
        '[ኌሔዄ]': 'ሄ',
        '[ሕኅ]': 'ህ',
        '[ኆሖኾ]': 'ሆ',
        'ሠ': 'ሰ',
        'ሡ': 'ሱ',
        'ሢ': 'ሲ',
        'ሣ': 'ሳ',
        'ሤ': 'ሴ',
        'ሥ': 'ስ',
        'ሦ': 'ሶ',
        '[ዓኣዐ]': 'አ',
        'ዑ': 'ኡ',
        'ዒ': 'ኢ',
        'ዔ': 'ኤ',
        'ዕ': 'እ',
        'ዖ': 'ኦ',
        'ጸ': 'ፀ',
        'ጹ': 'ፁ',
        'ጺ': 'ፂ',
        'ጻ': 'ፃ',
        'ጼ': 'ፄ',
        'ጽ': 'ፅ',
        'ጾ': 'ፆ'
    }

    for pattern, replacement in char_map.items():
        text = re.sub(pattern, replacement, text)

    return text


def remove_stopwords(input_list: Union[list, str], stopwords_file: str = DEFAULT_STOPWORDS_PATH) -> list:
    """
    Removes Amharic stopwords from a list/string of words.
    """

    if type(input_list) == str:
        input_list = input_list.split(' ')

    STOPWORDS_LIST = []
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        STOPWORDS_LIST = set([line.rstrip() for line in file.readlines()])
    
    filtered_list = []
    for word in input_list:
        word = word.strip()
        if word not in STOPWORDS_LIST:
            filtered_list.append(word)

    return filtered_list
