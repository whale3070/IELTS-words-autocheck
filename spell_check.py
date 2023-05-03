def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def check_spelling(user_words, correct_words):
    misspelled_words = []
    for i, (word, correct_word) in enumerate(zip(user_words, correct_words)):
        if word != correct_word:
            misspelled_words.append((i + 1, word, correct_word))
    return misspelled_words

def main():
    task_number = input("请选择一个任务文件（输入数字 1 到 9）: ").strip()
    filename = f'task{task_number}.txt'
    try:
        correct_words = load_words(filename)
    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}。请确保文件存在。")
        return
    
    print("请输入您要检查的单词，每行一个，按 Ctrl+D (Unix/Linux/Mac) 或 Ctrl+Z (Windows) 结束输入：")
    user_words = []
    while True:
        try:
            line = input()
            if line:
                user_words.append(line.strip())
        except EOFError:
            break

    misspelled_words = check_spelling(user_words, correct_words)
    total_words = len(user_words)
    correct_words_count = total_words - len(misspelled_words)
    accuracy = (correct_words_count / total_words) * 100

    if misspelled_words:
        print("以下单词拼写错误，请检查：")
        for item in misspelled_words:
            line, wrong_word, correct_word = item
            print(f"单词行 {line}: {wrong_word}")
            print(f"正确用法: {correct_word}")
            print()

        print("您需要加强背诵的单词有：")
        for _, _, correct_word in misspelled_words:
            print(correct_word)
    else:
        print("您输入的所有单词拼写正确！")
    
    print(f"您的正确率是：{accuracy:.2f}%")

if __name__ == "__main__":
    main()
