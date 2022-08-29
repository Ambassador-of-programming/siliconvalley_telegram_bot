from random import randint
from links import Message2
from topics import Message
from functions import Message1
from main import Bot
from start_bot import bot, start

@bot.message_handler(commands=['start'])
def start(message):
    start(message)

@bot.message_handler(content_types=['text'])
def lolol(message):
    c = Bot()
    topics = Message(bot, message)
    function = Message1(bot, message)
    vstoen = Message1(bot, message)
    vsroen_funct = Message1(bot, message)
    metody = Message1(bot, message)
    metody_str = Message1(bot, message)
    metody_list = Message1(bot, message)
    metody_tuple = Message1(bot, message)
    metody_set = Message1(bot, message)
    metody_dict = Message1(bot, message)
    links = Message2(bot, message)



    if message.chat.type == "private":

        if message.text == "◖Темы":
           topics.tems()
        
        # подразделение темы
        elif message.text == "Скачать Python":
            bot.send_message(message.chat.id, 'Давайте приступим к установке Python\nПерейдите по указанной ниже ссылке и следуйте иструкции')
            bot.send_message(message.chat.id, 'https://pythonworld.ru/osnovy/skachat-python.html')
        elif message.text == "Установка редактора исходного кода":
            
            bot.send_message(message.chat.id, 'Visual Studio Code — редактор исходного кода, разработанный Microsoft для Windows, Linux и macOS. Позиционируется как «лёгкий» редактор кода для кроссплатформенной разработки веб- и облачных приложений.')
            bot.send_message(message.chat.id, 'https://code.visualstudio.com/')
        elif message.text == "Условия":
            bot.send_message(message.chat.id, 'https://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html')
        elif message.text == "Типы данных":
            bot.send_message(message.chat.id, 'https://pythonchik.ru/osnovy/tipy-dannyh-v-python')
        elif message.text == "List&Tuple":
            bot.send_message(message.chat.id, 'https://realpython.com/python-lists-tuples/')
        elif message.text == "Set&Dict":
            bot.send_message(message.chat.id, 'https://mipt-cs.github.io/python3-2017-2018/labs/lab17.html')
       
        
        elif message.text == "● Функции":
            function.functions()
        

        elif message.text == "Встроенные функции":
            vstoen.vstoen_funct()
        elif message.text == "Методы":
            metody.metody()

        elif message.text == "str":
            metody_str.metody_str()
        elif message.text == "list":
            metody.metody_list()
        elif message.text == "tuple":
            metody.metody_tuple()
        elif message.text == "set":
            metody.metody_set()
        elif message.text == "dict":
            metody.metody_dict()
        elif message.text == "":
            bot.send_message

        # подраздел Методы str
        elif message.text == "isalpha()":
            bot.send_message(message.chat.id, 'возвращает True, если строка состоит только из алфавитных символов')
        elif message.text == "islower()":
            bot.send_message(message.chat.id,'возвращает True, если строка состоит только из символов в нижнем регистре')
        elif message.text == "isupper()":
            bot.send_message(message.chat.id,'возвращает True, если все символы строки в верхнем регистре')
        elif message.text == "isdigit()":
            bot.send_message(message.chat.id,'возвращает True, если все символы строки - цифры')
        elif message.text == "isnumeric()":
            bot.send_message(message.chat.id, 'возвращает True, если строка представляет собой число')
        elif message.text == "startswith(str)":
            bot.send_message(message.chat.id, 'возвращает True, если строка начинается с подстроки str')
        elif message.text == "endswith(str)":
            bot.send_message(message.chat.id, 'возвращает True, если строка заканчивается на подстроку str')
        elif message.text == "lower()":
            bot.send_message(message.chat.id, 'переводит строку в нижний регистр')
        elif message.text == "upper()":
            bot.send_message(message.chat.id, 'переводит строку в вехний регистр')
        elif message.text == "title()":
            bot.send_message(message.chat.id, 'начальные символы всех слов в строке переводятся в верхний регистр')
        elif message.text == "capitalize()":
            bot.send_message(message.chat.id, 'переводит в верхний регистр первую букву только самого первого слова строки')
        elif message.text == "lstrip()":
            bot.send_message(message.chat.id, 'удаляет начальные пробелы из строки')
        elif message.text == "rstrip()":
            bot.send_message(message.chat.id, 'удаляет конечные пробелы из строки')
        elif message.text == "strip()":
            bot.send_message(message.chat.id, 'удаляет начальные и конечные пробелы из строки')
        elif message.text == "ljust(width)":
            bot.send_message(message.chat.id, 'если длина строки меньше параметра width, то справа от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по левому краю')
        elif message.text == "rjust(width)":
            bot.send_message(message.chat.id, 'если длина строки меньше параметра width, то слева от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по правому краю')
        elif message.text == "center(width)":
            bot.send_message(message.chat.id, 'если длина строки меньше параметра width, то слева и справа от строки равномерно добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по центру')
        elif message.text == "find(str[, start [, end])":
            bot.send_message(message.chat.id, 'возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1')
        elif message.text == "replace(old, new[, num])":
            bot.send_message(message.chat.id, 'заменяет в строке одну подстроку на другую')
        elif message.text == "split([delimeter[, num]])":
            bot.send_message(message.chat.id, 'разбивает строку на подстроки в зависимости от разделителя')
        elif message.text == "join(strs)":
            bot.send_message(message.chat.id, 'объединяет строки в одну строку, вставляя между ними определенный разделитель')

        # подразделение list
        elif message.text == "append(x)":
            bot.send_message(message.chat.id, "Добавляет элемент в конец списка")
        elif message.text == "extend(L)":
            bot.send_message(message.chat.id, "Расширяет список list, добавляя в конец все элементы списка L")
        elif message.text == "insert(i, x)":
            bot.send_message(message.chat.id, "Вставляет на i-ый элемент значение x")
        elif message.text == "remove(x)":
            bot.send_message(message.chat.id, "Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует")
        elif message.text == "pop([i])":
            bot.send_message(message.chat.id, "Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент")
        elif message.text == "index(x, [start [, end]])":
            bot.send_message(message.chat.id, "Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)")
        elif message.text == "count(x)":
            bot.send_message(message.chat.id, "Возвращает количество элементов со значением x")
        elif message.text == "sort([key=функция])":
            bot.send_message(message.chat.id, "Сортирует список на основе функции")
        elif message.text == "reverse()":
            bot.send_message(message.chat.id, "Разворачивает список")
        elif message.text == "copy()":
            bot.send_message(message.chat.id, "Поверхностная копия списка")
        elif message.text == "clear()":
            bot.send_message(message.chat.id, "Очищает список")

        # подразделение tuple
        elif message.text == "срезы":
            bot.send_message(message.chat.id, 'Слайсы кортежей предельно похожи на таковые у строк, а выглядят они следующим образом:\ntuple[start:fin:step]\nГде start — начальный элемент среза (включительно), fin — конечный (не включительно) и step— "шаг" среза.')
        elif message.text == "len()":
            bot.send_message(message.chat.id, 'Используя функцию len(), получаем длину/количество элементов')
        elif message.text == "повторение":
            bot.send_message(message.chat.id, 'Как и в случае с конкатенацией, для кортежей, впрочем, как и для строк, определена операция повторения:\ndog_do = ("woof!",)\nprint(dog_do * 3)\n> ("woof!", "woof!", "woof!")')
        elif message.text == "index()":
            bot.send_message(message.chat.id, 'Метод index() позволяет получить индекс элемента. Достаточно передать нужное значение элемента, как аргумент метода')
        elif message.text == "count()":
            bot.send_message(message.chat.id, 'Метод count() ведёт подсчет числа вхождений элемента в кортеж')
        
        # подразделение set
        elif message.text == "add(a)":
            bot.send_message(message.chat.id, 'Добавляет в множество указанный элемент a')
        elif message.text == "clear()":
            bot.send_message(message.chat.id, 'Очищает множество (удаляет все его элементы)')
        elif message.text == "copy()":
            bot.send_message(message.chat.id, 'Возвращает поверхностную копию множества')
        elif message.text == "difference(x)":
            bot.send_message(message.chat.id, 'Возвращает элементы множества которые отсутствуют в указанном множестве x')
        elif message.text == "difference_update(x)":
            bot.send_message(message.chat.id, 'Удаляет из множества все элементы, присутствующие в указанном множестве x')
        elif message.text == "discard(a)":
            bot.send_message(message.chat.id, 'Удаляет указанный элемент a, если он присутствует в множестве')
        elif message.text == "intersection(x)":
            bot.send_message(message.chat.id, 'Возвращает множество с элементам присутствующими в обоих множествах')
        elif message.text == "intersection_update(x)":
            bot.send_message(message.chat.id, 'Оставляет в множестве только те элементы которые входят в его пересечение с указанным множеством x')
        elif message.text == "isdisjoint(x)":
            bot.send_message(message.chat.id, 'Возвращает True если у множества нет общих элементов с указанным множеством x')
        elif message.text == "issubset(x)":
            bot.send_message(message.chat.id, 'Возвращает True если множество эквивалентно указанному множеству x или является его подмножеством')
        elif message.text == "issuperset(x)":
            bot.send_message(message.chat.id, 'Возвращает True если множество эквивалентно указанному множеству x или является его надмножеством')
        elif message.text == "pop()":
            bot.send_message(message.chat.id, 'Удаляет и возвращает произвольный элемент множества. Если множество является пустым, то вызывается исключение KeyError')
        elif message.text == "remove()":
            bot.send_message(message.chat.id, 'Удаляет указанный элемент x из множества или вызывает исключение KeyError если такой элемент отсутсвует')
        elif message.text == "symmetric_difference()":
            bot.send_message(message.chat.id, 'Возвращает элементы которые присутствуют в обоих множествах, кроме тех, которые являются общими')
        elif message.text == "symmetric_difference_update(x)":
            bot.send_message(message.chat.id, 'Добавляет элементы из указанного множества x и удаляет элементы которые являются общими')
        elif message.text == "union(x)":
            bot.send_message(message.chat.id, 'Возвращает объединение множеств')
        elif message.text == "update(x)":
            bot.send_message(message.chat.id, 'Добавляет в множество элементы указанного множества x')

        # подразделение dict
        elif message.text == "clear()":
            bot.send_message(message.chat.id, 'очищает словарь')
        elif message.text == "copy()":
            bot.send_message(message.chat.id, 'возвращает копию словаря')
        elif message.text == "fromkeys(seq[, value])":
            bot.send_message(message.chat.id, 'создает словарь с ключами из seq и значением value (по умолчанию None).')
        elif message.text == "get(key[, default])":
            bot.send_message(message.chat.id, 'возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).')
        elif message.text == "items()":
            bot.send_message(message.chat.id, 'возвращает пары (ключ, значение).')
        elif message.text == "keys()":
            bot.send_message(message.chat.id, 'возвращает ключи в словаре.')
        elif message.text == "pop(key[, default])":
            bot.send_message(message.chat.id, 'удаляет ключ, и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение)')
        elif message.text == "popitem()":
            bot.send_message(message.chat.id, 'удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.')
        elif message.text == "setdefault(key[, default])":
            bot.send_message(message.chat.id, 'возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).')
        elif message.text == "update([other])":
            bot.send_message(message.chat.id, 'обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).')
        elif message.text == "values()":
            bot.send_message(message.chat.id, 'возвращает значения в словаре.')

        # подразделение встроенные функции
        elif message.text == "print":
            bot.send_message(message.chat.id, 'Выводит заданные объекты на экран или отправляет их текстовым потоком в файл.')
        elif message.text == "range":
            bot.send_message(message.chat.id, 'Арифметическая прогрессия от start до stop с шагом step.')
        elif message.text == "len":
            bot.send_message(message.chat.id, 'Возвращает число элементов в указанном объекте-контейнере.')
        elif message.text == "input":
            bot.send_message(message.chat.id, 'Считывает и возвращает строку входных данных.')
        elif message.text == "tuple(*)":
            bot.send_message(message.chat.id, 'Преобразование к кортежу.')
        elif message.text == "set(*)":
            bot.send_message(message.chat.id, 'Создает множество')
        elif message.text == "list":
            bot.send_message(message.chat.id, 'Создает список.')
        elif message.text == "dict(*)":
            bot.send_message(message.chat.id, 'Создаёт новый словарь. Объект dict является классом словаря.')
        elif message.text == "все функции":
            vsroen_funct.vse_funcii()

        # подразделение все функции
        elif message.text == "abs()":
            bot.send_message(message.chat.id, 'Возвращает абсолютную величину (модуль числа).')
        elif message.text == "all()":
            bot.send_message(message.chat.id, 'Проверяет, все ли указанные элементы принимают значение «истина».\nall(iterable)  -> bool\niterable : Объект, поддерживающий итерирование.\nВернёт True, если все элементы итерируемого объекта представляются истиной (True).')
        elif message.text == "any()":
            bot.send_message(message.chat.id, 'Проверяет, есть ли среди указанных элементов хотя бы один, принимающий значение «истина».\nany(iterable)  -> bool\niterable : Объект, поддерживающий итерирование.\nВернёт True, если любой из элементов итерируемого объекта явится истиной.\nВнимание: Возвращает False, если итерируемый объект пуст.')
        elif message.text == "ascii()":
            bot.send_message(message.chat.id, 'Возвращает строковое представление объекта с экранированными не-ASCII символами.')
        elif message.text == "bin()":
            bot.send_message(message.chat.id, 'Преобразование целого числа в двоичную строку.')
        elif message.text == "bool()":
            bot.send_message(message.chat.id, 'Преобразование к типу bool, использующая стандартную процедуру проверки истинности. Если х является ложным или опущен, возвращает значение False, в противном случае она возвращает True.')
        elif message.text == "bytearray()":
            bot.send_message(message.chat.id, 'Преобразование к bytearray. Bytearray — изменяемая последовательность целых чисел в диапазоне 0≤X<256. Вызванная без аргументов, возвращает пустой массив байт.')
        elif message.text == "bytes()":
            bot.send_message(message.chat.id, 'Возвращает объект типа bytes, который является неизменяемой последовательностью целых чисел в диапазоне 0≤X<256. Аргументы конструктора интерпретируются как для bytearray().')
        elif message.text == "callable()":
            bot.send_message(message.chat.id, 'Возвращает True для объекта, поддерживающего вызов.')
        elif message.text == "chr()":
            bot.send_message(message.chat.id, 'Возвращает символ по его числовому представлению.')
        elif message.text == "classmethod()":
            bot.send_message(message.chat.id, 'Представляет указанную функцию методом класса.')
        elif message.text == "compile()":
            bot.send_message(message.chat.id, 'Компилирует исходный код в объект кода, либо объект АСД.')
        elif message.text == "complex()":
            bot.send_message(message.chat.id, 'Преобразование к комплексному числу.')
        elif message.text == "delattr()":
            bot.send_message(message.chat.id, 'Удаляет из объекта указанный атрибут.')
        elif message.text == "dir()":
            bot.send_message(message.chat.id, 'Возвращает имена [переменных], доступные в локальной области, либо атрибуты указанного объекта в алфавитном порядке.')
        elif message.text == "dict()":
            bot.send_message(message.chat.id, 'Создаёт новый словарь. Объект dict является классом словаря.')
        elif message.text == "divmod()":
            bot.send_message(message.chat.id, 'Для целочисленного деления возвращает пару частное-остаток от деления аргументов.')
        elif message.text == "enumerate()":
            bot.send_message(message.chat.id, 'Возвращает генератор, отдающий пары счётчик-элемент для элементов указанной последовательности.')
        elif message.text == "eval()":
            bot.send_message(message.chat.id, 'Разбирает и исполняет указанное выражение.\neval(expression, globals=None, locals=None)\nexpression : Выражение, которое требуется исполнить, в виде строки. Либо объект кода.\nglobals=None : Ожидается dict. Словарь глобального пространства, относительно которого следует исполнить выражение. Если указан, но не содержит атрибута builtins данные указанного пространства будут дополнены данными общего глобального пространства, перед разбором выражения. Таким образом, выражение будет иметь доступ ко всем встроенным модулям.\nlocals=None : Ожидается объект-отображение (например, dict). Локальное пространство, в котором следует исполнить выражение. Если не указано, то используется словарь глобального пространства. Если оба аргумента опущены, то выражение будет выполнено в среде, где был осуществлён вызов функции. В случае ошибок возбуждает SyntaxError.')
        elif message.text == "exec()":
            bot.send_message(message.chat.id, 'Динамически исполняет указанный код.')
        elif message.text == "filter()":
            bot.send_message(message.chat.id, 'При помощи указанной функции фильтрует элементы переданного объекта.')
        elif message.text == "float()":
            bot.send_message(message.chat.id, 'Преобразование к числу с плавающей точкой. Если аргумент не указан, возвращается 0.0.')
        elif message.text == "format()":
            bot.send_message(message.chat.id, 'Форматирует указанное значение.\nformat(value[, format_spec])\nvalue : Значение, которое требуется отформатировать.\nformat_spec : Настройки формата, в соответствии с которыми требуется выполнить форматирование. Интерпретация настроек зависит от типа значения. По умолчанию — пустая строка (обычно приводит к тому же эффекту, что и применение str ()).\nИнтерпретация настроек форматирования зависит от типа переданного значения, однако большинство встроенных типов используют общий мини-язык форматирования.')
        elif message.text == "frozenset()":
            bot.send_message(message.chat.id, 'Возвращает неизменяемое множество.\n\nfrozenset([iterable])')
        elif message.text == "getattr()":
            bot.send_message(message.chat.id, 'Возвращает значение атрибута объекта.\n\ngetattr(obj, name[, default])\nobj : object Объект, значение атрибута которого требуется получить.\nname : str Имя атрибута, значение которого требуется получить.\ndefault : Значение по умолчанию, которое будет возвращено, если объект не располагает указанным атрибутом. Если не задано, и атрибут отсутствует, возбуждается исключение AttributeError. Функция возвращает значение атрибута указанного объекта по имени.\nДля установки атрибута используется setattr(). Для удаления атрибута используется delattr(). Для проверки существования атрибута используется hasattr().')
        elif message.text == "globals()":
            bot.send_message(message.chat.id, 'Возвращает словарь с глобальной таблицей символов, определённых в модуле.')
        elif message.text == "hasattr()":
            bot.send_message(message.chat.id, 'Возвращает флаг, указывающий на то, содержит ли объект указанный атрибут.\n\nhasattr(obj, name)  -> bool\nobj : object Объект, существование атрибута в котором нужно проверить.\nname : str Имя атрибута, существование которого требуется проверить. Возвращает True, если атрибут существует, иначе — False.\nФункция основывается на вызове getattr() с последующей проверкой на предмет случившегося исключения.\nДля возвращения атрибута используется getattr(). Для установки атрибута используется setattr(). Для удаления атрибута используется delattr().')
        elif message.text == "hash()":
            bot.send_message(message.chat.id, 'Возвращает хеш указанного объекта.\n\nhash(obj)  -> int\nobj : Объект, хеш которого требуется получить . Возвращает целое являющееся хешем объекта.\nХеш используется, в частности, для быстрого сравнения ключей при поиске по словарям. Равные числовые значения имеют одинаковый хеш, даже если значения принадлежат разным типам (например, 1 и 1.0).\nПользовательские типы могут переопределять метод hash(), результат которого будет использован при вызове hash(). Однако, следует помнить, что функция hash() обрезает значение в соответствии с битностью хоста.')
        elif message.text == "hex()":
            bot.send_message(message.chat.id, 'Возвращает строку с шестнадцатеричным представлением указанного целого.\n\nhex(i)  -> str\ni : Целое, для которого требуется вычислить шестнадцатеричное представление. Может быть передан любой объект, реализующий метод index() , возвращающий целое.')
        elif message.text == "id()":
            bot.send_message(message.chat.id, 'Возвращает идентификатор указанного объекта.\n\nid(obj)  -> int\nobj : Объект, идентификатор которого требуется получить.\nВозвращает целое, гарантированно являющееся уникальным и постоянным для объекта на время его существования.\nТаким образом, объекты, периоды существования которых не пересекаются, могут иметь одинаковый идентификатор.')
        elif message.text == "int()":
            bot.send_message(message.chat.id, 'Преобразует x к целому числу в десятичной системе счисления. Вместо десятичной системы можно указать любое основание от 2 до 36 включительно.\n\nint([x=0, [base=10]])')
        elif message.text == "__import__()":
            bot.send_message(message.chat.id, '__import__() — это функция, вызываемая оператором импорта.\n\n__import__(name, globals=None, locals=None, fromlist=(), level=0)\nname - имя модуля, который вы хотите импортировать\nглобальные и локальные - определяет, как интерпретировать имя\nfromlist - объекты или подмодули, которые должны быть импортированы по имени\nуровень — указывает, использовать ли абсолютный или относительный импорт')
        elif message.text == "iter()":
            bot.send_message(message.chat.id, 'Возвращает объект итератора.\n\niter(obj[, sentinel])\nobj : Объект коллекции, поддерживающей итерирование (реализует iter()), либо объект, поддерживающий протокол последовательности (реализует getitem(), где аргумент целое, начиная с нуля). Если передан другой объект, возбуждается TypeError.\nsentinel : Если этот аргумент предоставлен, то ожидается, что obj содержит объект, поддерживающий вызов. В этом случае, созданный итератор будет вызывать указанный объект (без аргументов) с каждым обращением к своему\nnext() и проверять полученное значение на равенство с sentinel. Если полученное значение равно sentinel, возбуждается StopIteration, иначе возвращается полученное значение. Функция возвращает итератор по объекту, поддерживающему итерирование по его элементам.')
        elif message.text == "isinstance()":
            bot.send_message(message.chat.id, 'Возвращает флаг, указывающий на то, является ли указанный объект экземпляром указанного класса (классов).')
        elif message.text == "issubclass()":
            bot.send_message(message.chat.id, 'Возвращает флаг, указывающий на то, является ли указанный класс подклассом указанного класса (классов).\n\nissubclass(cls, classinfo)  -> bool\ncls : Класс, требующий проверки.\nclassinfo : Класс, либо кортеж с классами. Если аргумент не является классом, либо кортежем с классами, возбуждается TypeError. Возвращает True, если указанный класс является подклассом указанного класса (классов). Класс считается подклассом самого себя.\nДля проверки того, является ли объект экземпляром класса (классов) используйте isinstance.')
        elif message.text == "len()":
            bot.send_message(message.chat.id, 'Возвращает число элементов в указанном объекте-контейнере.\n\nlen(obj)  -> int\nobj : Объект-контайнер, число элементов в котором требуется определить. Возвращает число элементов в контейнерах: объекте-последовательности (строка, байты, кортеж, список, диапазон) или объекте-коллекции (словарь, множество, неизменяемое множество и пр.).')
        # elif message.text == "list()":
        #     bot.send_message(message.chat.id, '')
        elif message.text == "locals()":
            bot.send_message(message.chat.id, 'Возвращает словарь, представляющий текущую локальную таблицу символов.\n\nlocals()  -> dict\nОбновляет и возвращает словарь с текущей локальной таблицей символов.')
        elif message.text == "map()":
            bot.send_message(message.chat.id, 'Применяет указанную функцию к каждому элементу указанной последовательности/последовательностей.\n\nmap(func, iterable, ...)  -> iterator / list\nfunc : Функция, которую следует применить к элементам последовательности или последовательностей. Должна принимать количество элементов равное количеству последовательностей. Если передано None, считается что требуется применить тождественное отображение (lambda *args: args), при этом, если передано несколько последовательностей результат будет содержать кортежи с данными из каждой из них.\niterable : Последовательность (или объект, поддерживающий итерирование), к элементам которой требуется применить функцию. Если в какой‑либо из последовательностей количество элементов меньше, чем в остальных, недостающие элементы считаются None. Итератор останавливается, когда самая короткая из последовательностей исчерпана.')
        elif message.text == "max()":
            bot.send_message(message.chat.id, 'Возвращает элемент с набольшим значением из переданных в функцию.\n\niterable : Если указан один позиционный аргумент, то ожидается, что он является итерируемым объектом. Возвращается элемент с максимальным значением, найденный среди элементов этого объекта.\nargs : Если указано несколько позиционных аргументов, элемент с наибольшим значением разыскивается среди них.\ndefault : Этим аргументом можно указать значение, которое следует вернуть, если итерируемый объект окажется пустым. Если последовательность пуста и аргумент не указан, возбуждается ValueError.\nВ указанном итерируемом объекте, или среди аргументов, обнаруживает и возвращает элемент с набольшим значением.')
        elif message.text == "memoryview()":
            bot.send_message(message.chat.id, 'Создает объект memoryview.\n\nmemoryview(obj)')
        elif message.text == "min()":
            bot.send_message(message.chat.id, 'Возвращает элемент с наименьшим значением из переданных в функцию.\n\nmin(iterable, *args[, key, default])\niterable: Если указан один позиционный аргумент, то ожидается, что он является итерируемым объектом. Возвращается элемент с минимальным значением, найденный среди элементов этого объекта.\nargs: Если указано несколько позиционных аргументов, элемент с наименьшим значением разыскивается среди них.\ndefault: Этим аргументом можно указать значение, которое следует вернуть, если итерируемый объект окажется пустым. Если последовательность пуста и аргумент не указан, возбуждается\nВ указанном итерируемом объекте, или среди аргументов, обнаруживает и возвращает элемент с наименьшим значением.')
        elif message.text == "next()":
            bot.send_message(message.chat.id, 'Возвращает следующий элемент итератора.\n\nnext(iter[, default])\niter : Объект итератора, возвращающий элементы.\ndefault : Значение, которое должно быть возвращено вместо возбуждения StopIteration, в случае исчерпания элементов при итерации.\n')
        elif message.text == "oct()":
            bot.send_message(message.chat.id, 'Функция Python oct() используется для преобразования целого числа в восьмеричную строку с префиксом «0o».\n\noct(x)\nРезультатом функции oct() является строка. Мы также можем передать объект в качестве аргумента, в этом случае объект должен иметь реализацию функции __index __(), которая возвращает целое число.\n\nprint(oct(10))\nprint(oct(0xF))')
        elif message.text == "object()":
            bot.send_message(message.chat.id, 'Возвращает безликий объект, являющийся базовым для всех объектов.')
        elif message.text == "open()":
            bot.send_message(message.chat.id, 'Открывает файл и возвращает представляющий его объект.')
        elif message.text == "ord()":
            bot.send_message(message.chat.id, 'Возвращает числовое представление для указанного символа.\n\nord(chr)  -> int\nchr : Символ, который следует представить в виде целого.')
        elif message.text == "pow()":
            bot.send_message(message.chat.id, 'Возвращает результат возведения числа в степень, с опциональным делением по модулю.\n\npow(x, y[, z])\nx : Число, которое требуется возвести в степень.\ny : Число, являющееся степенью, в которую нужно возвести первый аргумент. Если число отрицательное, аргумент z не принимается.\nz : Число, на которое требуется произвести деление по модулю. Если число указано, ожидается, что x и y положительны и имеют тип int.')
        elif message.text == "property()":
            bot.send_message(message.chat.id, 'property()— это Pythonic способ избежать формальных методов получения и установки в вашем коде. Эта функция позволяет вам превращать атрибуты класса в свойства или управляемые атрибуты .')
        elif message.text == "repr()":
            bot.send_message(message.chat.id, 'Возвращает формальное строковое представление указанного объекта.\n\nrepr(obj)  -> str\nobj : Объект для которого требуется получить формальное строковое представление. Для многих типов функция возвращает строку, которая при передаче в eval() может произвести объект с тем же значением, что и исходный.')
        elif message.text == "reversed()":
            bot.send_message(message.chat.id, 'Возвращает обратный итератор по указанной последовательности seq. Последовательность seq должна иметь метод __reversed__() или метод __len__ и метод __getitem__ с целыми числами в качестве аргумента. Числа должны начинаться с 0.\n\nreversed(seq)')
        elif message.text == "round()":
            bot.send_message(message.chat.id, 'Возвращает число с плавающей запятой, округлённое до указанного количества цифр после запятой.\n\nround(number[, ndigits])\nnumber : Число, которое требуется округлить.\nndigits : Количество знаков после запятой. Если не указано, то равно 0.\nДля встроенных типов, поддерживающих функцию, значения округляются до ближайшего кратного 10 в степени минус ndigits; если два кратных одинаково близки, округление производится в сторону чётного. Так, например, и round(0.5) и round(-0.5) равны 0, но round(1.5) равно 2.')
        elif message.text == "set()":
            bot.send_message(message.chat.id, 'Создает множество.')
        elif message.text == "setattr()":
            bot.send_message(message.chat.id, 'Добавляет объекту указанный атрибут.\n\nsetattr(obj, name, value)\nobj : object Объект, который следует дополнить атрибутом.\nname : str Строка с именем атрибута. Можно указывать как имя нового, так и существующего атрибута.\nvalue : Произвольное значение атрибута.\n\nАтрибут объекта (свойство, метод, элемент) будет добавлен в случае, если объект разрешает/поддерживает это действие.\nМетод зачастую используется в случаях, когда имя атрибута и/или значение заранее неизвестно и содержится в переменной.\nДля возвращения атрибута используется getattr().\nДля удаления атрибута используется delattr().\nДля проверки существования атрибута используется hasattr().')
        elif message.text == "slice()":
            bot.send_message(message.chat.id, 'Функция slice()возвращает объект среза.\n\nslice(start, end, step)\nОбъект среза используется, чтобы указать, как нарезать последовательность. Вы можете указать, где начать нарезку и где закончить. Вы также можете указать шаг, который позволит вам, например, нарезать только все остальные элементы.')
        elif message.text == "sorted()":
            bot.send_message(message.chat.id, 'Возвращает новый отсортированный список, составленный из элементов итерирующегося объекта.\n\nsorted(iterable[, key][, reverse])  -> list\niterable : Объект, поддерживающий итерирование, элементы которого требуется упорядочить.\ncmp=None : Ожидается в форме именованного аргумента. Функция, принимающая аргументами два стоящих рядом элемента, которая должна вернуть отрицательное число (если первый меньше второго), нуль (если равны) и положительное (если первый больше второго). Например: cmp=lambda x,y: cmp(x.lower(), y.lower()). Использование сочетаний key + reverse намного быстрее эквивалентной cmp-функции из‑за того, что в первом случае обращение к каждому из элементов происходит единожды, а во втором по несколько раз.\nkey=None : Ожидается в форме именованного аргумента. Функция, принимающая аргументом элемент, используемая для получения из этого элемента значения для сравнения его с другими. None — сравнить элементы напрямую. Например: key=str.lower.\nreverse=False : Ожидается в форме именованного аргумента. Флаг, указывающий следует ли производить сортировку в обратном порядке.')
        elif message.text == "str()":
            bot.send_message(message.chat.id, 'Строковое представление объекта.')
        elif message.text == "staticmethod()":
            bot.send_message(message.chat.id, 'Представляет указанную функцию статичным методом.\n\nstaticmethod(function)  -> Статичный метод\nfunction : Функция, которую следует представить статичным методом.')
        elif message.text == "sum()":
            bot.send_message(message.chat.id, 'Суммирует элементы указанного объекта и возвращает результат.\n\nsum(iterable[, start])\niterable : Объект, поддерживающий итерацию по его элементам. Ожидается, что элементы этого объекта являются числами, но не строками. Если объект пуст, функция вернёт начальное значение (start).\nstart=0 : Число, с которого следует начать суммирование.')
        elif message.text == "super()":
            bot.send_message(message.chat.id, 'Возвращает объект-посредник (прокси), делегирующий вызовы методов родителю или собрату класса указанного типа.\n\nsuper([type[, object-or-type]])\ntype : Тип, от которого следует начать поиск объекта-посредника. Ранее атрибут был обязателен.\nobj-or-type : Если не указан, возвращается несвязанный объект-посредник. Если атрибут является объектом, то будет получен посредник для получения метода объекта, для которого isinstance(obj, type) возвращает True. Если атрибут является типом, то будет получен посредник для получения метод класса, для которого issubclass(subtype, type) возвращает True. Используется для доступа к базовым реализациям наследуемых методов, перекрытых в классе-наследнике.')
        elif message.text == "tuple()":
            bot.send_message(message.chat.id, 'Преобразование к кортежу.\n\ntuple([iterable])')
        elif message.text == "type()":
            bot.send_message(message.chat.id, 'Возвращает тип объекта.\n\ntype(object)')
        elif message.text == "vars()":
            bot.send_message(message.chat.id, 'Возвращает словарь из атрибута dict указанного объекта.\n\nvars([obj])  -> dict\nobj : Объект, для которого следует вернуть словарь атрибутов (dict).\nВозвращает словарь атрибутов (dict) указанного объекта — модуля, класса, экземпляра, и любого другого объекта, имеющего атрибут dict.')
        elif message.text == "zip()":
            bot.send_message(message.chat.id, 'Возвращает итератор по кортежам, где i-тый кортеж содержит i-тый элемент каждой из указанных последовательностей.\n\nzip(*iterables)\niterables : Итерируемые объекты, элементы которых следует упаковать в кортежи. Если передана одна последовательность, вернётся итератор по кортежам, состоящим из единственного элемента. Если последовательности не переданы, возвращается пустой итератор.')
        elif message.text == "Ознакомиться углубленно с фукнциями":
            bot.send_message(message.chat.id, 'https://letpy.com/handbook/builtins/')
        
        
        

        elif message.text == "Ссылки◗":
            links.links()

        # подразделение ссылки
        elif message.text == "Видео курсы Python":
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0')
        elif message.text == "Сайты курсы Python":
            bot.send_message(message.chat.id, 'https://ru.code-basics.com/languages/python')
        elif message.text == "Тренажер быстрой печати":
            bot.send_message(message.chat.id, 'https://www.typingstudy.com/ru/lesson/1')
        elif message.text == "Книги по Python":
            bot.send_message(message.chat.id, 'https://monster-book.com/python-knigi')
        elif message.text == "Github":
            bot.send_message(message.chat.id, 'https://github.com/')
        elif message.text == "Codewars":
            bot.send_message(message.chat.id, 'https://www.codewars.com/')
        elif message.text == "PEP 8":
            bot.send_message(message.chat.id, 'https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html')



        
        elif message.text == "▸ Что за бот?":
            if randint(0,100) < 20:
                videos = randint(3, 4)
                videos_vid = f'bot_video/{videos}.mp4'
                with open(videos_vid, 'rb') as file:
                    bot.send_video(message.chat.id,file)
            else: 
                with open('bot_video/5.mp4', 'rb') as files:
                    bot.send_video(message.chat.id, files)

        elif message.text == "|||":
            bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=c.menu())
           


bot.polling(none_stop=True)