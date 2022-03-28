путь к видосам:
/home/tier/Videos/molchanov_python_casts

путь к коду:
/home/tier/github/learn_python/15_python_casts


================================
4_main
# питоновский путь прятать все так чтобы ничего не торчало при импорте одного модуля из другого
# в этом плане такая конструкция решает кучу проблем, видно на примере скрипта:


#если тут будет например строка: print(f'Imported from: {__name__}')
то она выполнится сразу же после:
from hello import a
# а так вот норм:
def main():
    print('main was called')

if __name__ == '__main__': #  скрипт был запущен самостоятельно
    main()
    
если 
print(globals().get('__name__'))
выдеает __main__
значит код был запущен из того же файла где он написан
иначе - значит что этот код вызвали из другого модуля

Итого:
Служебная строенная переменная __name__ хранит имя модуля
значение main она принимает когда скрипт мы запускаем самостоятельно, иначе имя модуля где она была определена

=====================================
6_decorators

генератор с условием (условие всегда в конце)
x for x in range(10**4) if x % 2 == 0

генераторы быстрее списков - так как при создании списка вызывается append
а при создании генератора низкоуровневая сишка

----
декораторы хорошо использовать чтобы вынести "за скобки" повторяющийся или не целевой код

#Декоратор для функции с аргументами:
def timeit(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print(datetime.now() - start)
        return result
    return wrapper
    
# такая запись это по сути дела синтаксический сахар
@timeit
def two():
# для вот такой:
l1 = timeit(one)(10) # => wrapper(10)

# чтобы задать переменные для самого декоратора, нужна еще одна обертка вокруг функции wrapper
==========================================
