# Ide Tugas Pemrograman 2 DDP1 Gasal 22/23

import os
import sys

def print_line(file_name, line_number, \
               line, space_file_name = 40,  \
               space_line_number = 3, n = 40):
    """ Formatted output untuk mencetak satu baris yang match string pattern

        file_name (str): nama file dimana baris tersebut berada
        line_number (int): nomor baris tersebut
        space_file_name (int): space karakter untuk bagian cetak nama file
        space_line_number (int): space karakter untuk bagian cetak nomor baris
        n (int): cetak n karakter pertama dari baris tersebut
    """
    print(f"{file_name:<{space_file_name}} line {line_number:<{space_line_number}} {line[:n]:<{n}}")

def is_match_with_wildcard(str_pattern, line):
    """ proses matching dengan str_pattern yang mengandung *

        str_pattern (str): string pattern yang mengandung *
        line (str): string baris
    """
    if str_pattern.count("*") > 1:
        raise AttributeError("Argumen program tidak benar.")
    else:
        pos_star = str_pattern.find("*")
        fst = str_pattern[:pos_star]
        snd = str_pattern[pos_star + 1:]
        if type(line) == str: # untuk matching substring tanpa -w
            pos_fst = line.find(fst)
            pos_snd = line[pos_fst + len(fst):].find(snd)
            if (pos_fst < 0) or (pos_snd < 0):
                return False
            return True
        elif type(line) == list:
            for word in line: # untuk matching whole word, dengan -w
                pos_fst = word.find(fst)
                pos_snd = word[pos_fst + len(fst):].find(snd)
                if (pos_fst >= 0) and (pos_snd >= 0):
                    return True
            return False

def is_match(str_pattern, line):
    """ proses matching dengan str_pattern

        str_pattern (str): string pattern
        line (str): string baris
    """
    if "*" not in str_pattern:
        return str_pattern in line # handle both tanpa / dengan -w
    else:
        return is_match_with_wildcard(str_pattern, line)

def scan_file(file_name, str_pattern, \
              case_sensitive = True, whole_word = False):
    """ scan sebuah file apakah mengandung pattern str_pattern

        file_name (str): nama file yang di-scan
        str_pattern (str): pola string yang dicari
        case_sensitive (bool): True jika mode case sensitive (tanpa -i)
        whole_word (bool): True jika menggunakan mode -w
    """
    line_number = 1
    with open(file_name) as file:
        for line in file:
            line_tmp = line.strip()
            if not case_sensitive:
                line_tmp = line_tmp.lower()
                str_pattern = str_pattern.lower()
            if whole_word:
                line_tmp = line_tmp.split()
            if is_match(str_pattern, line_tmp):
                print_line(file_name, line_number, line.strip())
            line_number += 1

def scan_dir(root_path, str_pattern, \
             case_sensitive = False, whole_word = False):
    """ scan semua files yang ada di direktori root_path

        file_name (str): nama file yang di-scan
        str_pattern (str): pola string yang dicari
        case_sensitive (bool): True jika mode case sensitive (tanpa -i)
        whole_word (bool): True jika menggunakan mode -w
    """
    for (dir_path, dir_names, file_names) in os.walk(root_path):
        dir = dir_path
        for file_name in file_names:
            abs_path = dir + "\\" + file_name
            scan_file(abs_path, str_pattern, \
                      case_sensitive = case_sensitive, \
                      whole_word = whole_word)

def process_args():
    """ proses argumen program """
    arg_len = len(sys.argv)
    whole_word = False
    case_sensitive = True
    str_pattern = ""
    path = ""
    if arg_len == 4:
        option = sys.argv[1]
        str_pattern = sys.argv[2]
        path = sys.argv[3]
        if option == '-w':
            whole_word = True
        elif option == '-i':
            case_sensitive = False
        else:
            raise AttributeError("Argumen program tidak benar.")
    elif arg_len == 3:
        str_pattern = sys.argv[1]
        path = sys.argv[2]
    else:
        raise AttributeError("Argumen program tidak benar.")

    is_dir = None
    if os.path.isdir(path):
        is_dir = True
    elif os.path.isfile(path):
        is_dir = False
    else:
        raise FileNotFoundError(f"File atau direktori {path} tidak ditemukan.")

    return whole_word, case_sensitive, \
           str_pattern, path, is_dir

if __name__ == '__main__':
    try:
        whole_word, case_sensitive, str_pattern, path, is_dir = process_args()
        scan_function = scan_dir if is_dir else scan_file
        scan_function(path, str_pattern, case_sensitive, whole_word)
    except FileNotFoundError as e:
        print(e)
    except AttributeError as e:
        print(e)
