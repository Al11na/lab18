#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_line_numbers(source_file, target_file):
    try:
        with  open(source_file, 'r') as source:
            lines = source.readlines()

            with open(target_file, 'w') as target:
                for i, line in enumerate(lines, start=1):
                    target.write(f"{i}:{line}")

        print(f"Файл успешно создан: {target_file}")

    except FileNotFoundError:
        print("Файл не найден.")

def main():
    source_file = input("Введите имя исходного файла:")
    target_file = input("Введите имя целевого файла:")

    add_line_numbers(source_file, target_file)
if __name__ == "__main__":
    main()