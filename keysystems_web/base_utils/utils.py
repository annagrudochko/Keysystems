from random import choice


def pass_gen(len_: int = 8) -> str:
    return ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(len_)])
