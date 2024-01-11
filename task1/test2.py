from test1 import check_relation

if __name__ == '__main__':
    net = [
        ('Нурбакыт', 'Арслан'), ('Жанар', 'Эмир'),
        ('Бегимай', 'Улук'), ('Эрнис', 'Мырза'),
        ('Талгат', 'Айдар'), ('Таалай', 'Айнуска'),
        ('Назима', 'Айжан'), ('Ислам', 'Махабат'),
        ('Нурсултан', 'Айжаркын'), ('Элиза', 'Алибек')
    ]


    result1 = check_relation(net, 'Нурбакыт', 'Айжаркын')
    print(result1)  # Ожидаемый результат: False

    result2 = check_relation(net, 'Элиза', 'Эмир')
    print(result2)  # Ожидаемый результат: False 

    result3 = check_relation(net, 'Махабат', 'Таалай')
    print(result3)  # Ожидаемый результат: False 

    result4 = check_relation(net, 'Айнуска', 'Ислам')
    print(result4)  # Ожидаемый результат: False 

    result5 = check_relation(net, 'Нурсултан', 'Бегимай')
    print(result5)  # Ожидаемый результат: True

    result6 = check_relation(net, 'Талгат', 'Эрнис')
    print(result6)  # Ожидаемый результат: True

    result7 = check_relation(net, 'Айдар', 'Мырза')
    print(result7)  # Ожидаемый результат: False 












