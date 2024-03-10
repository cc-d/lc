#!/usr/bin/env python3
import sys
from pyshared import truncstr
from importlib import import_module


def main(module_name: str):
    if module_name.endswith('.py'):
        module_name = module_name[:-3]
    module = import_module(module_name)
    s = module.Solution()
    smeths = [m for m in dir(s) if not m.startswith('_')]
    smeth = getattr(s, smeths[0])

    print(f'MODULE: {module.__name__}.py METHOD: {smeths[0]}()')
    msgs = []
    for tc in module.TEST:
        methmsg = truncstr(f'{smeths[0]}{tc[0]}', 100)
        print(f'{methmsg} -> {tc[1]}')
        try:
            result = smeth(*tc[0])
            assert result == tc[1]
            msgs.append((f'{methmsg} -> {tc[1]})', True))
        except AssertionError as e:
            msgs.append((f'{methmsg} -> {tc[1]} | {result}', False))

    for msg in msgs:
        trunc = truncstr(msg[0], start_chars=80, end_chars=20)
        if msg[1]:
            print(f'PASSED: {trunc}')
        else:
            print(f'TEST CASE FAILED: {trunc}')


if __name__ == '__main__':
    main(sys.argv[1])
