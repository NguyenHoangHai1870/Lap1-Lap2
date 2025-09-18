Lab 1: Text Tokenization

Mục tiêu: Hiểu và triển khai bước tiền xử lý cơ bản trong NLP: tokenization.

Các bước thực hiện:

Định nghĩa interface Tokenizer với phương thức tokenize(text: str).

SimpleTokenizer:

Chuyển chữ về lowercase.

Tách từ bằng khoảng trắng.

Tách dấu câu cơ bản (.,!?).

RegexTokenizer:

Sử dụng biểu thức chính quy \w+|[^\w\s].

Tách chính xác từ, số, dấu câu, ký tự đặc biệt.

Kết quả ví dụ:

--- Tokenizing Sample Text from UD_English-EWT ---
Original Sample (first 100 chars): Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the
mosque in the town of ...

SimpleTokenizer Output (first 20 tokens): ['al-zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al-ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of', 'qaim', ',']
RegexTokenizer Output (first 20 tokens): ['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the']

Nhận xét:

RegexTokenizer chuẩn xác hơn khi xử lý từ viết tắt, dấu chấm lửng, ký tự đặc biệt.

Lab 2: Count Vectorization

Mục tiêu: Biểu diễn văn bản dưới dạng vector số nguyên (Bag-of-Words) để dùng cho mô hình ML.

Các bước thực hiện:

Định nghĩa interface Vectorizer với các phương thức fit, transform, fit_transform.

CountVectorizer:

Constructor nhận một instance Tokenizer.

fit(corpus) tạo vocabulary_ từ tất cả token duy nhất.

transform(documents) tạo vector đếm số lần token xuất hiện.

fit_transform(corpus) kết hợp hai bước trên.

Kết quả ví dụ trên corpus:

Corpus: ["I love NLP.", "I love programming.", "NLP is a subfield of AI."]
Vocabulary: {'.': 0, 'a': 1, 'ai': 2, 'i': 3, 'is': 4, 'love': 5, 'nlp': 6, 'of': 7, 'programming': 8, 'subfield': 9}
Document-Term Matrix:
[1, 0, 0, 1, 0, 1, 1, 0, 0, 0]
[1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
[1, 1, 1, 0, 1, 0, 1, 1, 0, 1]

Nhận xét:
Mỗi document được biểu diễn dưới dạng vector số nguyên theo từ điển.

Từ xuất hiện nhiều lần trong document được đếm chính xác.
