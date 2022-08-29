from main import Bot

class Message1:
    def __init__(self, bot, message) -> None:
        self.bot = bot 
        self.chat = message.chat.id
        self.func = Bot()
        

    def functions(self):
        markup = self.func.button(['Встроенные функции', 'Методы'])           
        self.bot.send_message(self.chat,'Функции представляют блок кода, который выполняет определенную задачу и который можно повторно использовать в других частях программы.\nВ частности, функция print(), которая выводит некоторое значение на консоль. Python имеет множество встроенных функций и позволяет определять свои функции.\nФормальное определение функции:\n', reply_markup=markup)
        with open('2.png', 'rb') as file1:
            self.bot.send_photo(self.chat, file1)

    def vstoen_funct(self):
        markup1 = self.func.button(['print', 'range', 'len', 'input', 'tuple(*)', 'set(*)', 'list', 'dict(*)', 'все функции'])
        self.bot.send_message(self.chat, "Встроенные функции – это функции, которые уже содержатся в табличном процессоре и выполняют различные вычисления автоматически при их вызове из библиотеки функций.\nКаждая функция имеет свое собственное имя, которое необходимо для ее вызова.", reply_markup=markup1)
        
    def vse_funcii(self):
        markup = self.func.button(['abs()', 'all()', 'any()', '	ascii()', 'bin()', 'bool()', 'bytearray()', 'bytes()', 'callable()', 'chr()', 'classmethod()', 'compile()', 'complex()', 'delattr()', 'dir()', 'divmod()', 'enumerate()', 'eval()', 'exec()', 'filter()', 'float()', 'format()', 'frozenset()', 'getattr()', 'globals()', 'hasattr()', 'hash()', 'hex()', 'id()', 'int()', '__import__()', 'iter()', '	isinstance()', 'issubclass()', 'locals()', 'map()', 'max()', 'memoryview()', 'min()', 'next()', 'oct()', 'object()', 'open()', 'ord()', 'pow()', 'property()', 'repr()', 'reversed()', 'round()', 'setattr()', 'slice()', 'sorted()', 'str()', 'staticmethod()', 'sum()', 'super()', 'type()', 'vars()', 'zip()', 'Ознакомиться углубленно с фукнциями'])
        self.bot.send_message(self.chat, 'все функции', reply_markup=markup)

    def metody(self):
        markup = self.func.button(['str', 'list', 'tuple', 'set', 'dict'])
        self.bot.send_message(self.chat,'Методы', reply_markup=markup)
    
    def metody_str(self):
        markup = self.func.button(['isalpha()', 'islower()', 'isupper()', 'isdigit()', 'isnumeric()', 'startswith(str)', 'endswith(str)', 'lower()', 'upper()', 'title()', 'capitalize()', 'lstrip()', 'rstrip()', 'strip()', 'ljust(width)', 'rjust(width)', 'center(width)', 'find(str[, start [, end])', 'replace(old, new[, num])', 'split([delimeter[, num]])', 'join(strs)'])
        self.bot.send_message(self.chat,'Строка — базовый тип представляющий из себя неизменяемую последовательность символов; str от «string» — «строка».', reply_markup=markup)
        
    def metody_list(self):
        markup = self.func.button(['append(x)', 'extend(L)', 'insert(i, x)', 'remove(x)', 'pop([i])', 'index(x, [start [, end]])', 'count(x)', 'sort([key=функция])', 'reverse()', 'copy()', 'clear()'])
        self.bot.send_message(self.chat, 'Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов (почти как массив, но типы могут отличаться).', reply_markup=markup)

    def metody_tuple(self):
        markup = self.func.button(['срезы', 'len()', 'повторение', 'index()', 'count()', 'join()', 'tuple → list', 'tuple → dict'])
        self.bot.send_message(self.chat, 'Методы', reply_markup=markup)

    def metody_set(self):
        markup = self.func.button(['add(a)', 'clear()', 'copy()', 'difference(x)', 'difference_update(x)', 'discard(a)', 'intersection(x)', 'intersection_update(x)', 'isdisjoint(x)', 'issubset(x)', 'issuperset(x)', 'pop()', 'remove()', 'symmetric_difference()', 'symmetric_difference_update(x)', 'union(x)', 'update(x)'])
        self.bot.send_message(self.chat, 'Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.', reply_markup=markup)

    def metody_dict(self):
        markup = self.func.button(['clear()', 'copy()', 'fromkeys(seq[, value])', 'get(key[, default])', 'items()', 'keys()', 'pop(key[, default])', 'popitem()', 'setdefault(key[, default])', 'update([other])', 'values()'])
        self.bot.send_message(self.chat, 'Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу. Их иногда ещё называют ассоциативными массивами или хеш-таблицами.', reply_markup=markup)