from yargy import rule, or_, Parser
from yargy.predicates import gram
import docx2txt
import csv
from pyaspeller import YandexSpeller
from natasha import (
    span,
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,

    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)

FIRST = gram('Name')
LAST = gram('Surn')
MIDDLE = gram('Patr')
ABBR = gram('Abbr')

NAME = or_(
    rule(FIRST),
    rule(LAST),
    rule(FIRST, LAST),
    rule(LAST, FIRST),
    rule(FIRST, MIDDLE, LAST),
    rule(LAST, FIRST, MIDDLE),
    rule(ABBR, '.', ABBR, '.', LAST),
    rule(LAST, ABBR, '.', ABBR, '.'),
)
#Извлечение текста и исправление орфографических ошибок
parser = Parser(NAME)
path = input("точный путь к файлу:")
result = docx2txt.process("govnooo.docx")
text = str(result)
speller = YandexSpeller()
changes = {change['word']: change['s'][0] for change in speller.spell(text)}
for word, suggestion in changes.items():
   text = text.replace(word, suggestion)

#Извлечение именнованых сущностей(имён, дат) и запись в csv файл
sp_date = []
path = 'named_entities.csv'
with open(path, 'w', encoding='utf-8', newline='') as file:
    print('Загрузка...')
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['ФИО', ' ', 'Год', 'День', 'Месяц'])
    for date in list(dates_extractor(text)):
        date = str(date.fact)
        indx1 = date.index('year=') + 5
        indx2 = date.index(', m')
        indx3 = date.index('month=') + 6
        indx4 = date.index(', d')
        indx5 = date.index('day=') + 4
        indx6 = date.index(')')
        dt_year = date[indx1:indx2].lstrip().rstrip()
        dt_month = date[indx3:indx4].lstrip().rstrip()
        dt_day = date[indx5:indx6].lstrip().rstrip()
        #date_main = ('год:', dt_year, ',', 'месяц:', ',', dt_month, ',', 'день:', dt_day)
        date_main = (dt_year, dt_month , dt_day)
        sp_date.append(date_main)

    num = 0
    for match in parser.findall(text):
        start, stop = match.span
        main_name = text[start:stop]
        if len(main_name) >= 3 and main_name.istitle():
            if (len(main_name.split())) > 1:
                print(main_name, ':',   *sp_date[num])
                writer.writerow([main_name, ' ',  *sp_date[num]])
                num += 1