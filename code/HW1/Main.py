import re
import sys
from Utils import coerce
import Constants

def send_help():
    global help
    return help


def settings(s):
    regexp = "\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
    value = re.findall(regexp, s)
    return value

def cli(s):
    const = Constants.Constants()
    value = settings(s)
    for k, v in value:
        const.the[k] = coerce(v)
    the = const.the
    # print(f'the: {the}')

    args = sys.argv
    args = args[1:]
    # print(f'args: {args}')
    keys = the.keys()
    for key in keys:
        val = str(the[key])
        for n,x in enumerate(args):
            if x == "-"+key[0] or x == "--"+key:
                val = "False" if val == "True" else "True" if val == "False" else args[n+1]
        the[key] = coerce(val)
    return the

def main(options,help,funs):

    # print("here")
    saved = dict()
    fails = 0

    for k,v in cli(help).items():
        options[k] = v
        # print(f'k: {k}')
        saved[k] = v

    print(options)
    if options['help']:
        print(help)

    else:
        # print("reached 56")
        for what,fun, in funs.items():
            if options['go'] == 'all' or what == options['go']:
                for k, v in saved.items():
                    options[k] = v
                # seed = options['seed']
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)

    exit(fails)

if __name__ == '__main__':
    options = dict()
    help = '''
    script.lua : an example script with help text and a test suite
    (c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
    USAGE:   script.lua  [OPTIONS] [-g ACTION]
    OPTIONS:
      -d  --dump  on crash, dump stack = false
      -g  --go    start-up action      = data
      -h  --help  show help            = false
      -s  --seed  random number seed   = 937162211
    ACTIONS:
    '''
    funs = {}
    main(options,help,funs)