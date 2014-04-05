import json
import argparse
import sys
import requirements as req

def parse_args():
    args = argparse.ArgumentParser(description='pydep is simple command line tool that will print the dependencies of a python project in JSON')
    args.add_argument('--strict', type=bool, default=False, help='If true, pydep will not list any potential false positive dependencies')
    args.add_argument('dir', help='path to root directory of project code')
    return args.parse_args()

def main():
    args = parse_args()
    deps, err = req.list_deps(args.dir)
    if err is None:
        print json.dumps(deps)
        sys.exit(0)
    sys.exit(1)

if __name__ == '__main__':
    main()
