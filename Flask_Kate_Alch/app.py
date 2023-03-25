from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

BASE_DIR = Path(__file__).parent

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR / 'main.db'}" # Определяем вид используемой СУБД
                                                                            # и местоположение БД
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class QuoteModel(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   author = db.Column(db.String(32), unique=False)
   text = db.Column(db.String(255), unique=False)
   rating = db.Column(db.Integer)

   def  __str__(self):
       return f"{self.id} {self.author} {self.text} {self.rating}"

   def __init__(self, author, text, rating):
      '''Конструктор класса'''
      self.author = author
      self.text = text
      self.rating = rating


   def list_to_dict(self):
       return {
           "id": self.id,
           "author": self.author,
           "text": self.text
       }

   ## def get_a_quote_rating(self, id):
   ##    quote_d = QuoteModel.query.get(id)
   ##     q = quote_d.text
   ##     for i in q:
   ##         return f"{i}"
   ##     # 1) Получаем цитату по айди
   ##     # 2) Обращаемся к аттрибуту текст это цитаты
   ##     # 3) Считаем количество слов.
   ##     # 4) Накладываем условие.
   ##     # 5) Возвращаем в виде списка


@app.route("/quotes")
def get_all_q():
    quotes = QuoteModel.query.all()
    #print(quotes)
    q_dict = []
    for quote in quotes:
        q_dict.append(quote.list_to_dict())
    return q_dict

@app.route("/quotes/<int:id>")
def get_quote_with_id(id):
    quote_id = QuoteModel.query.get(id)
    quote_dict = []
    quote_dict.append(quote_id.list_to_dict())
    return quote_dict

@app.route("/quotes", methods=['POST'])
def create_quote():
    data = request.json
    q6 = QuoteModel(data["author"], data["text"], data["rating"])
    db.session.add(q6)
    db.session.commit()
    quotes_dict = []
    quotes_dict.append(q6.list_to_dict())
    return quotes_dict

@app.route("/quotes/<int:id>", methods=['PUT'])
def upgrade_quote(id):
    data = request.json
    quote_db = QuoteModel.query.get(id)
    quote_db.text = data["text"]
    db.session.commit()
    quotes_dict = []
    quotes_dict.append(quote_db.list_to_dict())
    return quotes_dict

@app.route("/quotes/rating/<int:id>")
def get_rating_quotes(id):
    quote_db_id = QuoteModel.query.get(id)
    text = quote_db_id.text        # Здесь я получаю просто строку.
    ''' Вариант первый '''
    words_counter = len(text.split()) - 1
    #print(words_counter, 'w' * 200)
    if words_counter > 7:
        quote_db_id.rating = 5
    else:
        quote_db_id.rating = 4
    return f"Рейтинг цитаты {quote_db_id.author} = {quote_db_id.rating}"

    ''' Вариант второй - работает неверно, но что-то там считает '''
    # symbols = "!,' '.-"
    # words_counter = 0
    # for i in text:
    #    if i in symbols:
    #       words_counter += 1
    # print(f"{words_counter}", '*' * 120)
    # if words_counter > 7:
    #     quote_db_id.rating = 5
    # else:
    #     quote_db_id.rating = 4
    # return f"{quote_db_id.rating}"


'''
    -------- Основная проблема, при реализации алгоритма с рейтингом - непонимание, куда именно писать эту функцию.
    Т.е, функция должна быть методом класса? Т.е метод класса получает строку и считает количество слов,
    после чего возвращает это значение в функцию обработчик - декоратора.
    Или же я всегда пишу функции через декоратор?
    ------- Вторая проблема. путаница с типами данных. Приходится каждый раз выводить через принт, либо
    смотреть тип данных через type. Шаманство, короче.
'''








if __name__ == "__main__":
   app.run(debug=True)