#!/usr/bin/env python
import json
import sys
import re
path = set()


def escp(k):
    if not re.match('[A-Za-z_][0-9A-Z_a-z]*$', k):
        return '"' + k + '"'
    else:
        return k


def dig(obj, p):
    if isinstance(obj, dict):
        for key in obj.keys():
            if p == "":
                prev = escp(key)
            else:
                prev = p + "." + escp(key)
            dig(obj[key], prev)

    elif isinstance(obj, list):
        prev = p + "[]"
        for val in obj:
            dig(val, prev)
    else:
        path.add(p)
        pass


def main():
    j = json.load(sys.stdin, encoding='utf-8')
    p = ""
    dig(j, p)
    for p in path:
        print p
    pass

if __name__ == '__main__':
    main()
