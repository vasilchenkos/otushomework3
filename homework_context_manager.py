from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        file_obj = open(path, 'w')
        yield file_obj
    except OSError:
        print("Произошла ошибка")
    finally:
        print("Закрываем файл")
        file_obj.close()

if __name__ == '__main__':
    with file_open('books-39204-271043.csv') as fileobj:
        fileobj.write("Testing context managers")
