import re
import sys
from Utils import coerce

def settings(s):
    regexp = "\n[%s]+[-][%S]+[%s]+[-][-]([%S]+)[^\n]+= ([%S]+)"
    value = dict(re.findall(regexp,s))
    return value

def cli(options):
    args = sys.argv
    args = args[1:]

    keys = options.keys()
    for key in keys:
        val = str(options[key])
        for n,x in enumerate(args):
            if x == "-"+key[0] or x == "--"+key:
                val = "False" if val == "True" else "True" if val == "False" else args[n+1]
        options[key] = coerce(val)
    return options

def main(options,help,funs):
    saved = dict()
    fails = 0
    for k,v in cli(settings(help)).items():
        options[k] = v
        saved[k] = v

    if options['help']:
        print(help)

    else:
        for what,fun, in funs.items():
            if options['go'] == 'all' or what == options['go']:
                for k, v in saved.items():
                    options[k] = v
                Seed = options['seed']
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)


