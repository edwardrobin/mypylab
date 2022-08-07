#!/usr/bin/env python3

g_var = "global variable in b.py scope!"

def print_global_var():
    print(f"{g_var}")


if __name__ == "__main__":
    print_global_var()

