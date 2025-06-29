import re
import string
import unicodedata
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TextCleaner:
    def __init__(self, remove_non_ascii=False, keep_currency_symbols=False):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.remove_non_ascii = remove_non_ascii
        self.keep_currency_symbols = keep_currency_symbols

        # Precompiled regex patterns
        self.url_pattern = re.compile(r'https?:\/\/\S+|www\.\S+')
        self.html_pattern = re.compile(r'<.*?>')
        self.mention_pattern = re.compile(r'@\w+', flags=re.IGNORECASE)
        self.number_pattern = re.compile(r'\b\d+\b')
        self.heart_pattern = re.compile(r'<3')
        self.alphanumeric_pattern = re.compile(r'\b\w*\d\w*\b')
        if keep_currency_symbols:
            self.symbol_pattern = re.compile(r'[^\w\s£€$]', flags=re.UNICODE)
        else:
            self.symbol_pattern = re.compile(r'[^\w\s]', flags=re.UNICODE)

    def normalize_unicode(self, text):
        text = unicodedata.normalize('NFKD', text)
        return ''.join([c for c in text if not unicodedata.combining(c)])

    def clean(self, text):
        # Lowercase
        text = text.lower()

        # Unicode normalization
        text = self.normalize_unicode(text)

        # Apply cleaning steps
        text = self.url_pattern.sub('URL', text)
        text = self.html_pattern.sub('', text)
        text = self.mention_pattern.sub('user', text)
        text = self.number_pattern.sub('NUMBER', text)
        text = self.heart_pattern.sub('HEART', text)
        text = self.alphanumeric_pattern.sub('', text)
        text = self.symbol_pattern.sub('', text)

        # Optionally remove non-ASCII characters (e.g., emojis)
        if self.remove_non_ascii:
            text = ''.join(c for c in text if ord(c) < 128)

        # Remove extra whitespace
        text = ' '.join(text.split())

        # Remove stopwords
        words = [word for word in text.split() if word not in self.stop_words]

        # Lemmatize
        words = [self.lemmatizer.lemmatize(word, pos='v') for word in words]

        return ' '.join(words)
