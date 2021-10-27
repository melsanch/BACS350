from os.path import exists

from hero.models import Article
from table.table import read_csv_file, write_csv_file


def export_chapters(hero):
    model = Article
    articles = f'{hero.doc_path}/articles.csv'
    records = [o.export_record() for o in model.objects.filter(hero=hero.title)]
    write_csv_file(articles, records)


def import_chapters(hero):
    model = Article
    articles = f'{hero.doc_path}/articles.csv'
    if exists(articles):
        for row in read_csv_file(articles):
            model.import_record(row)