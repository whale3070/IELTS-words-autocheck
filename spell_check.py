import os

def load_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words

def load_meanings(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        meanings = file.read().splitlines()
    return meanings

def check_spelling(user_words, correct_words):
    misspelled_words = []
    for i, correct_word in enumerate(correct_words):
        if i >= len(user_words) or user_words[i] != correct_word:
            misspelled_words.append((i + 1, user_words[i] if i < len(user_words) else None, correct_word))
    return misspelled_words

def write_results(filename, user_words, accuracy, misspelled_words, correct_meanings):
    with open(filename, 'w') as file:
        file.write(f"正确率：{accuracy:.2f}%\n\n")

        if misspelled_words:
            file.write("拼写错误的单词：\n")
            for line, wrong_word, correct_word in misspelled_words:
                file.write(f"单词行 {line}: {wrong_word} -> {correct_word} ({correct_meanings[line - 1]})\n")
        else:
            file.write("所有单词拼写正确！\n")
        
        file.write("\n用户输入的单词：\n")
        for word in user_words:
            file.write(f"{word}\n")

def main():
    task_number = input("请选择一个任务文件（输入数字 1 就代表着打开task1.txt，输入数字 31 就代表着打开task31.txt）: ").strip()
    words_filename = f'task{task_number}_words.txt'
    meanings_filename = f'task{task_number}_meanings.txt'
    try:
        correct_words = load_words(words_filename)
        correct_meanings = load_meanings(meanings_filename)
    except FileNotFoundError:
        print(f"错误：找不到文件 {words_filename} 或 {meanings_filename}。请确保文件存在。")
        return

    test_number = 1
    while True:
        print("请输入您要检查的单词，每行一个，输入 'q' 结束输入：")
        user_words = []
        idx = 1
        while True:
            print(f"{idx}. ", end="")
            line = input().strip()
            if line.lower() == 'q':
                break
            else:
                user_words.append(line)
                idx += 1

        misspelled_words = check_spelling(user_words, correct_words)
        total_words = len(correct_words)
        correct_words_count = total_words - len(misspelled_words)
        accuracy = (correct_words_count / total_words) * 100
        output_filename = f"task{task_number}_test_{test_number}.txt"
        while os.path.exists(output_filename):
            test_number += 1
            output_filename = f"task{task_number}_test_{test_number}.txt"

        write_results(output_filename, user_words, accuracy, misspelled_words, correct_meanings)
        print(f"结果已保存到 {output_filename}")

        if accuracy >= 95:
            break
if __name__ == "__main__":
    main()

