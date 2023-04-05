import os


def gcc_compile_pgproto():
    cmd = "CC=gcc python setup.py build_ext --inplace"
    os.system(cmd)


def pytest_configure(config):
    gcc_compile_pgproto()
