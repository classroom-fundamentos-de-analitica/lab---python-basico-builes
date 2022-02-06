"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def leer_csv():
    file = open('data.csv', 'r')
    data = file.readlines()
    return data


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    data = leer_csv()
    suma = 0

    # Aca sumaremos cada elemento de la segunda columna del archivo csv
    for line in data:
        suma += int(line[2])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = leer_csv()
    dicc = {}
    for line in data:
        dicc[line[0]] = dicc.get(line[0], 0) + 1

    lst = list(dicc.items())
    lst.sort()
    return lst


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    data = leer_csv()
    dicc = {}
    for line in data:
        dicc[line[0]] = dicc.get(line[0], 0) + int(line[2])

    lst = list(dicc.items())
    lst.sort()
    return lst


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = leer_csv()
    index = data[0].index('-')
    dicc = {}
    for line in data:
        dicc[line[index+1:index+3]] = dicc.get(line[index+1:index+3], 0) + 1

    lst = list(dicc.items())
    lst.sort()
    return lst


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = leer_csv()
    dicc = {}
    for line in data:
        dicc[line[0]] = dicc.get(line[0], []) + [int(line[2])]

    lst = []

    for key, value in dicc.items():
        lst.append((key, max(value), min(value)))
    lst.sort()
    return lst


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = leer_csv()
    dicc = {}
    for line in data:
        # En line no tomamos el ultimo caracter ya que es un salto de linea
        splited_line = line[:-1].split('\t')

        # Despues de separar cada linea por espacion tomamos la columna 5 y la sepramos por ,
        passwords = splited_line[4].split(',')

        # Luego reccorrems cada una de las contraseñas que hay en passwords fila por fila
        for password in passwords[:]:
            key, value = password.split(':')
            dicc[key] = dicc.get(key, []) + [int(value)]

    lst = []
    for key, value in dicc.items():
        lst.append((key,  min(value), max(value)))
    lst.sort()

    return lst


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    data = leer_csv()
    dicc = {}

    for line in data:
        splited_line = line.split('\t')
        col_0 = splited_line[0]
        col_1 = splited_line[1]

        dicc[col_1] = dicc.get(col_1, []) + [col_0]

    lst = []
    for key, value in dicc.items():
        lst.append((key, value))
    lst.sort()

    return lst


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = leer_csv()
    dicc = {}

    for line in data:
        splited_line = line.split('\t')
        col_0 = splited_line[0]
        col_1 = splited_line[1]
        dicc[col_1] = dicc.get(col_1, set({})).union({col_0})

    lst = []
    for key, value in dicc.items():
        lst.append((key, value))
    lst.sort()

    return lst


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = leer_csv()
    dicc = {'aaa': 0, 'bbb': 0, 'ccc': 0, 'ddd': 0, 'eee': 0,
            'fff': 0, 'ggg': 0, 'hhh': 0, 'iii': 0, 'jjj': 0, }
    for line in data:
        # En line no tomamos el ultimo caracter ya que es un salto de linea
        splited_line = line[:-1].split('\t')

        # Despues de separar cada linea por espacion tomamos la columna 5 y la sepramos por ,
        passwords = splited_line[4].split(',')

        # Luego reccorrems cada una de las contraseñas que hay en passwords fila por fila
        for password in passwords[:]:
            key, value = password.split(':')
            dicc[key] = dicc.get(key, 0) + 1

    return dicc


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = leer_csv()
    lst = []

    for line in data:
        splited_line = line.split('\t')
        passwords = splited_line[4].split(',')
        lst.append((splited_line[0], len(
            splited_line[3].split(',')), len(passwords)))

    return lst


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = leer_csv()
    dicc = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, }
    for line in data:
        splited_line = line.split('\t')
        for letter in splited_line[3].split(','):
            dicc[letter] = dicc.get(letter, 0) + int(line.split('\t')[1])

    return dicc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    a = {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    return a
