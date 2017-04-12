def count_word(filename):
    """计算文本文件中含有多少个单词"""
    try:
        with open(filename) as alice_obj:
            contents = alice_obj.read()
        # 异常处理
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        word = contents.split()
        num_words = len(word)
        print("The file " + filename + " has about " + str(num_words) + " words.")

count_word('alice.txt')

