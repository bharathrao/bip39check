#!/usr/bin/env python
import binascii
import hashlib
import os
import sys

class Bip39Check(object):
    def __init__(self, language):
        self.radix = 2048
        self.worddict = {}
        self.wordlist = []

        counter = 0

        with open('%s/%s.txt' % (self._get_directory(), language), 'r') as file:
            for w in file.readlines():
                word = w.strip().decode('utf8') if sys.version < '3' else w.strip()
                self.worddict[word] = counter
                self.wordlist.append(word)
                counter = counter + 1

        if(len(self.worddict) != self.radix):
            raise ValueError('Expecting %d words, not %d', self.radix, len(self.worddict))

    @classmethod
    def _get_directory(cls):
        return os.path.join(os.path.dirname(__file__), 'wordlist')

    def _check_size(self, phrase):
        self.size = len(phrase) + 1
        if (self.size % 3 != 0):
            raise ValueError('Expecting 2,5,8,11,14,17,20 or 23 words')

    def _compute_entropy(self, phrase):
        self.entropy = 0
        for w in phrase:
            idx = self.worddict[w]
            self.entropy = (self.entropy << 11) + idx
        return self.entropy

    def _scan(self):
        checksum_bits = self.size // 3
        hex_digits = self.size * 32 // 4
        entropy_to_fill = 11 - checksum_bits
        entropy_base = self.entropy << (entropy_to_fill)

        for i in range(0, 2 ** entropy_to_fill):
            entropy_candidate = entropy_base | i
            fmt = '%%0%sx' % hex_digits
            entropy_str = binascii.unhexlify(fmt % entropy_candidate)
            hash = hashlib.sha256(entropy_str).digest()[0]
            hash = ord(hash) if sys.version < '3' else hash
            checksum = hash >> (8 - checksum_bits)
            final_word_idx = (i << checksum_bits) + checksum
            checkword = self.wordlist[final_word_idx]
            print (checkword)


def main():
    lang = 'english' if len(sys.argv) < 2 else sys.argv[1].strip()
    m = Bip39Check(lang)
    line = sys.stdin.readline().decode('utf8').strip() if sys.version < '3' else sys.stdin.readline().strip()
    phrase = line.replace(u'\u3000', ' ').split()
    m._check_size(phrase)
    m._compute_entropy(phrase)
    m._scan()

if __name__ == '__main__':
    main()
