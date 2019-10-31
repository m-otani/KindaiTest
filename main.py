def main():
    print("Hello world")

def test_main():
    a = main()
    b = "Hello world"
    assert a == b

# main関数呼び出し
if __name__ == "__main__":
    main()