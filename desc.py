try:
    from pypandoc import convert_file
    long_description = convert_file("README.md", "rst")
except Exception(e):  # NOQA
    print(e)
    long_description = ""

print(long_description)
