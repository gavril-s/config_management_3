import json
import re
from sly import Lexer, Parser

class ConfigLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, LPAREN, RPAREN}

    ignore = ' \t\n'
    ignore_comment = r';.*'

    NAME = r'[А-Яа-яA-Za-z][А-Яа-яA-Za-z0-9-]*'
    NUMBER = r'\d+'
    STRING = r'"[^"]*"'
    LPAREN = r'\('
    RPAREN = r'\)'

    def error(self, t):
        print(f"Ошибка: Неизвестный символ '{t.value[0]}' в позиции {t.index}")
        self.index += 1  # Продолжим разбор, игнорируя недопустимый символ

class ConfigParser(Parser):
    tokens = ConfigLexer.tokens

    @_('s_exp_list')
    def program(self, p):
        return p.s_exp_list

    @_('s_exp s_exp_list')
    def s_exp_list(self, p):
        return [p.s_exp] + p.s_exp_list

    @_('s_exp')
    def s_exp_list(self, p):
        return [p.s_exp]

    @_('LPAREN s_exp_list RPAREN')
    def s_exp(self, p):
        return p.s_exp_list

    @_('data')
    def s_exp(self, p):
        return p.data

    @_('NUMBER')
    def data(self, p):
        return int(p.NUMBER)

    @_('STRING')
    def data(self, p):
        return p.STRING[1:-1]

    @_('NAME')
    def data(self, p):
        return p.NAME

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Использование: python config_parser.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        input_data = file.read()

    lexer = ConfigLexer()
    parser = ConfigParser()

    try:
        result = parser.parse(lexer.tokenize(input_data))

        json_data = {"groups": [], "students": []}

        current_group = None

        for item in result:
            if isinstance(item, list) and len(item) > 0 and isinstance(item[0], str) and re.match(r'^([А-Я]{4})-', item[0]):
                current_group = item[0]
                json_data["groups"].append(current_group)
            elif isinstance(item, list) and len(item) > 0 and isinstance(item[0], str) and item[0] == "student":
                student = {
                    "name": None,
                    "group": current_group,
                    "age": None
                }
                for attr in item[1:]:
                    if isinstance(attr, list) and len(attr) == 2:
                        key = attr[0]
                        value = attr[1]
                        if key == "name":
                            student["name"] = value
                        elif key == "age":
                            student["age"] = int(value)
                        elif key == "group":
                            student["group"] = value  # Обновляем значение группы
                if student["name"] is not None and student["age"] is not None:
                    json_data["students"].append(student)

        json_result = json.dumps(json_data, indent=2, ensure_ascii=False)
        print(json_result)
    except Exception as e:
        print(f"Ошибка разбора: {e}")
