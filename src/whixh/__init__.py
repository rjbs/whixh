import os
import sys

def find_first (opts):
    path = os.environ.get('PATH', '').split(os.pathsep)

    for opt in opts:
        if opt[0] == '/' and os.path.isfile(opt) and os.access(opt, os.X_OK):
            return opt

        for path_entry in path:
            maybe = os.path.join(path_entry, opt)

            if os.path.isfile(maybe) and os.access(maybe, os.X_OK):
                return maybe

    return None

def execute():
    opts = sys.argv

    if len(opts) == 0:
        print("usage: whixh PROGRAM...")
        sys.exit(2)

    found = find_first(opts)

    if found == None: sys.exit(1)

    print(found)
    sys.exit(0)
