class Constants:
    def __init__(self):
        self.the = dict()
        self.seed = 937162211
        self.p = 2
        self.cliffs=0.147
        self.sample = 512
        self.far = 0.95
        self.min = 0.5
        self.max = 512
        self.bins = 16
        self.rest = 4
        self.file = "../../../etc/data/auto93.csv"
        self.help = '''
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