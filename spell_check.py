import os

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

def write_results(filename, user_words, accuracy, misspelled_words):
    with open(filename, 'w') as file:
        file.write(f"正确率：{accuracy:.2f}%\n\n")

        if misspelled_words:
            file.write("拼写错误的单词：\n")
            for line, wrong_word, correct_word in misspelled_words:
                file.write(f"单词行 {line}: {wrong_word} -> {correct_word}\n")
        else:
            file.write("所有单词拼写正确！\n")
        
        file.write("\n用户输入的单词：\n")
        for word in user_words:
            file.write(f"{word}\n")

def main():
    task_number = input("请选择一个任务文件（输入数字 1 就代表着打开task1.txt，输入数字 31 就代表着打开task31.txt）: ").strip()
    filename = f'task{task_number}.txt'
    try:
        correct_words = load_words(filename)
    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}。请确保文件存在。")
        return

    test_number = 1
    while True:
        print("请输入您要检查的单词，每行一个，按 Ctrl+D (Unix/Linux/Mac) 或 Ctrl+Z (Windows) 结束输入：")
        user_words = []
        idx = 1
        while True:
            try:
                print(f"{idx}. ", end="")
                line = input()
                if line:
                    user_words.append(line.strip())
                    idx += 1
            except EOFError:
                break

        misspelled_words = check_spelling(user_words, correct_words)
        total_words = len(user_words)
        correct_words_count = total_words - len(misspelled_words)
        accuracy = (correct_words_count / total_words) * 100

        output_filename = f"task{task_number}_test_{test_number}.txt"
        while os.path.exists(output_filename):
            test_number += 1
            output_filename = f"task{task_number}_test_{test_number}.txt"

        write_results(output_filename, user_words, accuracy, misspelled_words)
        print(f"结果已保存到 {output_filename}")

        if accuracy >= 95:
            break

if __name__ == "__main__":
    main()
