import string
import os
import random as ran
from logfunc import logf
from typing import List
from pyshared import ranstr, default_repr, truncstr

os.environ['LOGF_USE_PRINT'] = 'True'


class Master:
    def __init__(self, *args, allowed=30):
        if len(args) >= 1:
            self.secret = args[0]
        else:
            self.secret = ranstr(6)
        self.allowed = allowed

    def guess(self, word: str):
        self.allowed -= 1
        return sum(
            1 if word[i] == self.secret[i] else 0
            for i in range(len(self.secret))
        )

    def __str__(self):
        return truncstr(
            default_repr(self, repr_format="<{obj_name} {attributes}>"), 100
        )

    def __repr__(self):
        return self.__str__()


def remove_words(guesses, words):
    chars = set(''.join(guesses))
    wd = {'remove': [], 'keep': [], 'live': words}
    while wd['live']:
        w = wd['live'].pop()
        keep = False
        for c in chars:
            if c in w:
                keep = True
                break
        if keep:
            wd['keep'].append(w)
        else:
            wd['remove'].append(w)
    return wd['keep']


class Solution:
    def findSecretWord(self, words: List[str], *args):
        print(args)
        master = Master(args[0], allowed=args[1])

        guesses = {}
        words = list(words)
        w = None
        while master.allowed:
            if len(words) % 2 == 0:
                w = words.pop(len(words) - 1)
            else:
                w = words.pop()
            guesses[w] = master.guess(w)
            if guesses[w] == 6:
                return w
            elif guesses[w] > 0:
                words = remove_words(
                    {g for g in guesses.keys() if guesses[g] > 0}, words
                )
            print(master.allowed, guesses[w], w)
        return words


TEST = (
    (
        (
            [
                "gaxckt",
                "trlccr",
                "jxwhkz",
                "ycbfps",
                "peayuf",
                "yiejjw",
                "ldzccp",
                "nqsjoa",
                "qrjasy",
                "pcldos",
                "acrtag",
                "buyeia",
                "ubmtpj",
                "drtclz",
                "zqderp",
                "snywek",
                "caoztp",
                "ibpghw",
                "evtkhl",
                "bhpfla",
                "ymqhxk",
                "qkvipb",
                "tvmued",
                "rvbass",
                "axeasm",
                "qolsjg",
                "roswcb",
                "vdjgxx",
                "bugbyv",
                "zipjpc",
                "tamszl",
                "osdifo",
                "dvxlxm",
                "iwmyfb",
                "wmnwhe",
                "hslnop",
                "nkrfwn",
                "puvgve",
                "rqsqpq",
                "jwoswl",
                "tittgf",
                "evqsqe",
                "aishiv",
                "pmwovj",
                "sorbte",
                "hbaczn",
                "coifed",
                "hrctvp",
                "vkytbw",
                "dizcxz",
                "arabol",
                "uywurk",
                "ppywdo",
                "resfls",
                "tmoliy",
                "etriev",
                "oanvlx",
                "wcsnzy",
                "loufkw",
                "onnwcy",
                "novblw",
                "mtxgwe",
                "rgrdbt",
                "ckolob",
                "kxnflb",
                "phonmg",
                "egcdab",
                "cykndr",
                "lkzobv",
                "ifwmwp",
                "jqmbib",
                "mypnvf",
                "lnrgnj",
                "clijwa",
                "kiioqr",
                "syzebr",
                "rqsmhg",
                "sczjmz",
                "hsdjfp",
                "mjcgvm",
                "ajotcx",
                "olgnfv",
                "mjyjxj",
                "wzgbmg",
                "lpcnbj",
                "yjjlwn",
                "blrogv",
                "bdplzs",
                "oxblph",
                "twejel",
                "rupapy",
                "euwrrz",
                "apiqzu",
                "ydcroj",
                "ldvzgq",
                "zailgu",
                "xgqpsr",
                "wxdyho",
                "alrplq",
                "brklfk",
            ],
            'hbaczn',
            10,
        ),
        'hbaczn',
    ),
)

#        'hbaczn',
