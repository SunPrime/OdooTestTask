import multiprocessing
import os

ALPHA = "".join(map(chr, range(ord(" "), ord("z") + 1)))
step = 3

def encode(text, queue):
    result = text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))
    queue.put(result)

def decode(text):
    result = text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))
    return result


def main():
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    queue3 = multiprocessing.Queue()
    queue4 = multiprocessing.Queue()

    with open('text.txt') as f:
        size = os.stat('text.txt').st_size
        part = size // 4
        print(part)
        l1 = f.read(part)
        l2 = f.read(part)
        l3 = f.read(part)
        l4 = f.read(size - part * 3)

    p1 = multiprocessing.Process(target=encode, args=(l1, queue1))
    p2 = multiprocessing.Process(target=encode, args=(l2, queue2))
    p3 = multiprocessing.Process(target=encode, args=(l3, queue3))
    p4 = multiprocessing.Process(target=encode, args=(l4, queue4))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    f.close()
    res = queue1.get() + queue2.get() + queue3.get() + queue4.get()
    file_output = open('text_encode.txt', 'w')
    print(res)
    file_output.write(res)
    file_output.close()


    y = decode(res)
    print(y)


if __name__ == '__main__':
    main()