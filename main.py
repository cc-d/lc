#!/usr/bin/env python3
import sys
from importlib import import_module


def main(module_name: str):
    module = import_module(module_name)
    s = module.Solution()
    smeths = [m for m in dir(s) if not m.startswith('_')]
    smeth = getattr(s, smeths[0])

    failmsgs = []
    for tc in module.TEST:
        tmsg = f'{smeths[0]}{tc[0]} -> {tc[1]}'
        print('\n' + tmsg)
        try:
            result = smeth(*tc[0])
            assert result == tc[1]
        except AssertionError as e:
            failmsgs.append(f'{tmsg} (return: {result})')

    for fmsg in failmsgs:
        print(f'TEST CASE FAILED: {fmsg}')


if __name__ == '__main__':
    main(sys.argv[1])
