# coding: utf-8
import os
import random
from flask import Flask, render_template, request, session, jsonify, abort
from flask import send_from_directory

app = Flask(__name__)


class DataBase(object):
    def __init__(self):
        self.users = {
            'admin@sjtu.edu.cn': {
                'username': 'admin',
                'password': '123456',
                'score': 1000000,
            }
        }
        self.lists = [
            {
                'url': '/book/1',
                'img_url': '/static/image/book_1.jpg',
                'name': '《数据结构：思想与实现》',
                'description': '本书条理清晰，严格按照线性结构、树形结构、集合结构和图形结构的次序来组织编写...',
                'score': 100,
                'download_times': 999,
            },
            {
                'url': '/book/2',
                'img_url': '/static/image/book_2.jpg',
                'name': '《数学分析（Ⅰ）》',
                'description': '本书是为贯彻教育部教学改革精神，实施全英语授课需要而编写，此书书稿在实际教学...',
                'score': 100,
                'download_times': 999,
            },
            {
                'url': '/book/3',
                'img_url': '/static/image/book_3.jpg',
                'name': '《面向对象软件工程：使用UML、模式与Java》',
                'description': '本书是为...',
                'score': 100,
                'download_times': 999,
            },
        ]
        self.books = {
            1: {
                'name': '《数据结构：思想与实现》',
                'score': 100,
                'rate': 5,
                'download_times': 3,
                'description': '《数据结构：思想与实现/“十二五”普通高等教育本科规划教材》条理清晰，严格按照线性结构、 树形结构、集合结构和图形结构的次序来组织编写。除了常规的数据结构内容之外，还介绍了一些 高级的数据结构，如红黑树、AA树和跳表等，并提供了大量的数据结构应用实例。让读者在学习数 据结构的同时，逐步了解为什么要学习数据结构，了解数据结构对计算机专业的重要性。《数据结 构：思想与实现/“十二五”普通高等教育本科规划教材》内容翔实，既注重数据结构和算法的原理 ，又十分强调和程序设计课程的衔接。在讲授数据结构的同时，不断加强学生对程序设计的理解。 书中的算法都有完整的C＋＋实现。这些程序结构清晰，构思精巧。',
                'author': 'jian cao',
                'catagory': 'computer science',
                'img_url': '/static/image/book_1.jpg',
                'uploader': '张老师',
                'created_at': '2017-05-06T13:28:03',
                'updated_at': '2017-05-07T07:47:03',
            },
            2: {
                'name': '《数学分析（Ⅰ）》',
                'score': 100,
                'rate': 5,
                'download_times': 4,
                'description': '《数据结构：思想与实现/“十二五”普通高等教育本科规划教材》条理清晰，严格按照线性结构、 树形结构、集合结构和图形结构的次序来组织编写。除了常规的数据结构内容之外，还介绍了一些 高级的数据结构，如红黑树、AA树和跳表等，并提供了大量的数据结构应用实例。让读者在学习数 据结构的同时，逐步了解为什么要学习数据结构，了解数据结构对计算机专业的重要性。《数据结 构：思想与实现/“十二五”普通高等教育本科规划教材》内容翔实，既注重数据结构和算法的原理 ，又十分强调和程序设计课程的衔接。在讲授数据结构的同时，不断加强学生对程序设计的理解。 书中的算法都有完整的C＋＋实现。这些程序结构清晰，构思精巧。',
                'author': 'jian cao',
                'catagory': 'computer science',
                'img_url': '/static/image/book_2.jpg',
                'uploader': '胡老板',
                'created_at': '2017-05-06T13:28:03',
                'updated_at': '2017-05-07T07:47:03',
            },
            3: {
                'name': '《面向对象软件工程：使用UML、模式与Java》',
                'score': 100,
                'rate': 5,
                'download_times': 5,
                'description': '《数据结构：思想与实现/“十二五”普通高等教育本科规划教材》条理清晰，严格按照线性结构、 树形结构、集合结构和图形结构的次序来组织编写。除了常规的数据结构内容之外，还介绍了一些 高级的数据结构，如红黑树、AA树和跳表等，并提供了大量的数据结构应用实例。让读者在学习数 据结构的同时，逐步了解为什么要学习数据结构，了解数据结构对计算机专业的重要性。《数据结 构：思想与实现/“十二五”普通高等教育本科规划教材》内容翔实，既注重数据结构和算法的原理 ，又十分强调和程序设计课程的衔接。在讲授数据结构的同时，不断加强学生对程序设计的理解。 书中的算法都有完整的C＋＋实现。这些程序结构清晰，构思精巧。',
                'author': 'jian cao',
                'catagory': 'computer science',
                'img_url': '/static/image/book_3.jpg',
                'uploader': '胡老板',
                'created_at': '2017-05-06T13:28:03',
                'updated_at': '2017-05-07T07:47:03',
            },
        }
        self.user_purchased = []
        self.user_favored = []

    def register(self, email, username, password):
        if email in self.users:
            return False
        self.users[email] = {
            'username': username,
            'password': password,
        }
        return True

    def login_verify(self, email, password):
        user = self.users.get(email)
        if user:
            return user['password'] == password
        return False

    def query_user(self, id):
        user = self.users.get(id)
        if user:
            user = user.copy()
            user.pop('password')
            return user

    def update_user(self, id, username):
        user = self.users.get(id)
        if user:
            user['username'] = username
            return True
        return False

    def book_by_id(self, id):
        return self.books.get(id)

    def update_by_id(self, id, name):
        self.users[id]['name'] = name

    def hot_books(self, num):
        return [random.choice(self.lists) for _ in range(num)]

    def user_purchase_ebook(self, user_id, ebook_id):
        self.books[ebook_id]['download_times'] += 1
        score = self.books[ebook_id]['score']
        self.users[user_id]['score'] -= score
        self.user_purchased.append((user_id, ebook_id))

    def user_ebook_access(self, user_id, ebook_id):
        for (uid, bid) in self.user_purchased:
            print uid, user_id, bid, ebook_id
            if uid == user_id and bid == ebook_id:
                return True
        return False

    def ebook_filename(self, ebook_id):
        return 'test.txt'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/book/<id>')
def book_page(id):
    return render_template('book.html')


@app.route('/list')
def book_list():
    return render_template('list.html')


@app.route('/signup', methods=['POST'])
def register():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    if db.register(email, username, password):
        return 'register success'
    return 'email is used', 400


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if db.login_verify(email, password):
        session['logged_in'] = True
        session['email'] = email
        return 'login success'
    return 'login error', 400


@app.route('/download/<int:book_id>')
def download(book_id):
    if session.get('logged_in') is True:
        email = session['email']
        if db.user_ebook_access(email, book_id):
            dirpath = reduce(os.path.join, [app.root_path, 'static', 'Ebook'])
            filename = db.ebook_filename(book_id)
            return send_from_directory(dirpath, filename, as_attachment=True)
        return abort(404)
    return abort(404)


@app.route('/personal')
def personal():
    return render_template('personal.html')


@app.route('/api/v1/user', methods=['GET', 'POST'])
def users():
    if session.get('logged_in') is True:
        if request.method == 'GET':
            user = db.query_user(session['email'])
            if user:
                return jsonify(user)
            return 'SQL error!', 500
        elif request.method == 'POST':
            username = request.form["name"]
            if db.updated_user(session['email'], username):
                return 'update success'
            return 'update error', 500
    return 'not logged in', 400


@app.route('/api/v1/hotbooks', methods=['GET'])
def hot_books():
    num = request.args.get('num')
    books = db.hot_books(int(num))
    return jsonify(books)


@app.route('/api/v1/ebook', methods=['GET'])
def ebook():
    book_id = request.args.get('id')
    book = db.book_by_id(int(book_id))
    return jsonify(book)


@app.route('/api/v1/purchase_verify', methods=['GET'])
def purchase_verify():
    if session.get('logged_in') is True:
        user = db.query_user(session['email'])
        book_id = request.args.get('id')
        book = db.book_by_id(int(book_id))
        result = jsonify({'current_score': user['score']})
        if (user['score'] >= book['score']):
            return result
        return result, 500
    return 'not logged in', 400


@app.route('/api/v1/purchase', methods=['GET'])
def purchase():
    if session.get('logged_in') is True:
        email = session['email']
        user = db.query_user(email)
        book_id = int(request.args.get('id'))
        book = db.book_by_id(book_id)
        result = jsonify({'current_score': user['score']})
        if (user['score'] >= book['score']):
            db.user_purchase_ebook(email, book_id)
            return result
        return result, 500
    return 'not logged in', 400


@app.route('/api/v1/purchased')
def purchased():
    result = {'purchased': False}
    if session.get('logged_in') is True:
        email = session['email']
        book_id = int(request.args.get('id'))
        if db.user_ebook_access(email, book_id):
            result['purchased'] = True
    return jsonify(result)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    db = DataBase()
    app.run(debug=True, host='0.0.0.0', port=4000)
