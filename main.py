import os

if __name__ == '__main__':
    for i in os.environ:
        print(f'k={i}, v={os.environ[i]}')
