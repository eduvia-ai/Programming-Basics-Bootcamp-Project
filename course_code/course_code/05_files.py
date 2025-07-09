# التعامل مع الملفات

# كتابة في ملف
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("This is a sample file.\nSecond line.")

# قراءة من الملف
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("File content:")
    print(content)