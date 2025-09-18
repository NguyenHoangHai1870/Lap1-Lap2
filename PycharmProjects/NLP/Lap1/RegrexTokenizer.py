import re
from typing import List
from interface import Tokenizer

class RegrexTokenizer(Tokenizer):
    def tokenize(self,text: str) -> List[str]:
        text = text.lower()
        tokens = re.findall(r"\w+|[^\w\s]", text)
        return tokens