import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
data = json.loads(requests.get(data_url).text)
books = data['results']['books']

scribner_books=[b for b in books if b['publisher'] == "Scribner"]
print("A.", len(scribner_books))

detective_books=[b for b in books if 'detective' in b['description'].lower()]
print("B.", len(detective_books))

from operator import itemgetter
x = max(books, key = itemgetter('weeks_on_list'))
s = "|".join([x['title'], str(x['weeks_on_list'])])
print("C.", s)


x = max(books, key = itemgetter('rank_last_week'))
s = "|".join([x['title'], str(x['rank']), str(x['rank_last_week'])])
print("D.", s)


new_books=[b for b in books if b['rank_last_week'] == 0]
print("E.", len(new_books))


x = min(new_books, key = itemgetter('rank'))
s = "|".join([x['title'], str(x['rank'])])
print("F.", s)


def calc_rank_change(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]

books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
x = max(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)


x = min(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("H.", s)


changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v > 0]
s = sum(x)
print("I.", s)


x = [v for v in changes if v < 0]
s = "|".join([str(len(x)), str(sum(x))])
print("J.", s)


print('K.', max([len(b['title']) for b in books]))


print('L.', round(sum([len(b['title']) for b in books]) / len(books)))
