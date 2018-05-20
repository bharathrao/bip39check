# BIP39 checksum word

### Create your own semi-non-sensical BIP-39 mnemonic sentence

BIP-39 Enables storing your private keys as a set of words instead of a binary string. However, it may be hard to memorize all 12 (or 24) words.

Bip39Check enables creating your own sentence and this script helps you find checksum word candidates to complete the phrase

## Background

[BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) helps creating a mnemonic out of any multiple of 32 bits of entropy from 32 to 256 bits. An extra checksum bit is added for every 32 bits of entropy. Because the checksum has to be verifiable, only some the words are usable for the final word.

This script helps you generate it.

## Caveats

#### This script should be run on an air-gapped machine to prevent malware and key loggers from reading your mnemonic.

## Requirements
Python 2.7 or Python 3.x

## Example:

For a 24 word phrase, we would only supply 23 words and see what legal words are possible for the 24th.

```
$ python bip39check.py english
arctic army kangaroo jump jealous dog dismiss dinosaur dolphin double door dragon dove drastic drop casino chase bulk cash caught action acoustic sound
armor
captain
fan
lake
ordinary
rich
science
theme
```

We can pick ```theme``` as the final word to make our phrase:

```
arctic army kangaroo jump jealous dog
dismiss dinosaur dolphin double door dragon
dove drastic drop casino chase bulk cash
caught action acoustic sound theme
```

Lets try with a 12 word phrase. We only supply 11 words:
```
$ python bip39check.py english
one two three angry wife disagree six seven eight daughter miss        
abstract
add
alarm
among
...
*** SOME RESULTS OMITTED FOR BREVITY ***
...
then
together
tonight
trash
try
twice
unknown
unusual
valid
view
visa
walnut
wealth
wine
winter
zero
```

By picking ```tonight``` as the final word, our 12-word phrase becomes:

```
one two three angry wife disagree
six seven eight daughter miss tonight
```

### Other examples:

```
random puppy solve quality pyramid puzzle
quick rabbit promote public meadow hunt
```
## Other Languages

Make sure the language words are under ```wordlist``` directory.
You can find all available languages here: https://github.com/bitcoin/bips/tree/master/bip-0039

### Japanese
The following would pick words from ```wordlist/japanese.txt```

```
$ python bip39check.py japanese
あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい あさい
あぶら
くせげ
ごがつ
せんすい
ちょうし
なやむ
へいおん
ろこつ
```
