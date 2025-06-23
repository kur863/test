from brace_parser import preprocess_braces

with open("brace_code.py", "r", encoding="utf-8") as f:
    code = f.read()

converted = preprocess_braces(code)
print("🔁 轉換後：")
#print(converted)
print("▶ 執行結果：")
exec(converted)
