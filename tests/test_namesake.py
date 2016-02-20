import os.path
import re
import linecache
import namesake

files = ['noun', 'adjective', 'verb', 'adverb']
pattern = re.compile(r'(\w+-){2}((\w+-){1,2})?[1-9](\d{1,2})?')

def test_for_empty_words():
    for t in namesake.counts:
        for i in range(1, namesake.counts[t]):
            line = linecache.getline(namesake.getfilename(t), i)
            assert line.strip() != ''

def test_for_single_words():
    for t in namesake.counts:
        for i in range(1, namesake.counts[t]):
            line = linecache.getline(namesake.getfilename(t), i)
            assert ' ' not in line.strip() != ''

def test_command(capsys):
    namesake.main()
    out, err = capsys.readouterr()
    assert pattern.match(out)


def test_name():
    name = namesake.getname()
    assert pattern.match(name)


def test_words():
    for t in files:
        with open(namesake.getfilename(t)) as f:
            content = [x.strip() for x in f.readlines()]
            assert namesake.getword(t) in content


def test_filecounts():
    for t in files:
        with open(namesake.getfilename(t)) as f:
            content = f.readlines()
            assert len(content) == namesake.counts[t]


def test_filename():
    for f in files:
        for x in [f, f+'s']:
            assert os.path.isfile(namesake.getfilename(x))
