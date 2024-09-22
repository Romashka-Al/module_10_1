from time import sleep
from threading import Thread
from datetime import datetime
time_start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f1:
        for i in range(word_count):
            f1.write(f"Какое-то слово № {i + 1} \n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_start_2 = datetime.now()
print(time_start_2 - time_start)

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

print(datetime.now() - time_start_2)
