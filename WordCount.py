import os
import re
import sys

def word_count(input_file, output_file):
    try:
        fd_in = os.open(input_file, os.O_RDONLY)  
        file_content = os.read(fd_in, 20000).decode('utf-8')  
        os.close(fd_in)
        
    except Exception as e:
        print(f"Error reading file {input_file}: {e}")
        return

    words = re.findall(r'\b\w+\b', file_content.lower())  

    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    # **Sort by word (alphabetical order) instead of count**
    sorted_words = sorted(word_dict.items(), key=lambda x: x[0])

    try:
        fd_out = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)  
        for word, count in sorted_words:
            os.write(fd_out, f"{word} {count}\n".encode('utf-8'))  
        os.close(fd_out)  
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 WordCount.py <input_file> <output_file>")
    else:
        word_count(sys.argv[1], sys.argv[2])
