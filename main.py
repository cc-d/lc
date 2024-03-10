#!/usr/bin/env python3
import sys
from importlib import import_module


def main(module_name: str):
    module = import_module(module_name)
    s = module.Solution()
    smeths = [m for m in dir(s) if not m.startswith('_')]
    smeth = getattr(s, smeths[0])

    print(f'MODULE: {module.__name__}.py METHOD: {smeths[0]}()')
    msgs = []
    for tc in module.TEST:
        methmsg = f'{smeths[0]}{tc[0]}'
        print(f'{methmsg} -> {tc[1]}')
        try:
            result = smeth(*tc[0])
            assert result == tc[1]
            msgs.append((f'{methmsg} -> {tc[1]})', True))
        except AssertionError as e:
            msgs.append((f'{methmsg} -> {tc[1]} | {result}', False))

    for msg in msgs:
        if msg[1]:
            print(f'PASSED: {msg}')
        else:
            print(f'TEST CASE FAILED: {msg}')


if __name__ == '__main__':
    main(sys.argv[1])
