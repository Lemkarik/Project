import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QTableWidgetItem,\
    QMessageBox
import sys
# from PyQt5 import uic
from random import choice
import threading
import csv
import os.path
from menu import MenuWindow
from test import TestWindow
from res import ResultWindow
from form import FormWindow
from edit import EditWindow
from enter import EnterWindow


DATABASE = 'tests'
USERNAME = ''


class EnterPage(QMainWindow, EnterWindow):  # Окно входа/регистрации
    def __init__(self):
        super().__init__()
        # uic.loadUi('enter.ui', self)
        self.setupUi(self)
        self.window = MyWidget()
        self.pb_enter.clicked.connect(self.start)
        self.pb_enter_2.clicked.connect(self.register)

    def start(self):    # Вход пользователя и выдача привелегий
        global USERNAME
        login = self.get_login.text()
        password = self.get_password.text()
        match = ('-1', '-1', -1, '-1')
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        for user_t in cur.execute("""SELECT login, password, type, name FROM users""").fetchall():
            user = (str(user_t[0]), str(user_t[1]), user_t[2], str(user_t[3]))
            if user[0] == login:
                match = user
        if match[0] == '-1':
            self.status_bar.setText('ОШИБКА: Пользователь не найден')
        elif match[1] != password:
            self.status_bar.setText('ОШИБКА: Неверный пароль')
        elif match[2] == 2:
            USERNAME = match[3]
            self.window.pb_edit.hide()
            self.close()
            self.window.show()
        elif match[2] == 1:
            USERNAME = match[3]
            self.close()
            self.window.show()
        print(USERNAME)
        con.close()

    def register(self):  # Регистрация нового ученика
        global USERNAME
        login = self.get_login_2.text()
        password = self.get_password_2.text()
        name = self.get_name.text()
        do_register = True
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        for user in cur.execute("""SELECT login FROM users"""):
            if str(user[0]) == login:
                self.status_bar_2.setText('ОШИБКА: Логин занят')
                do_register = False
                break
        con.close()
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("""INSERT INTO users(login, password, name, type) VALUES(?, ?, ?, ?)""",
                    (login, password, name, 2))
        con.commit()
        USERNAME = name
        self.window.pb_edit.hide()
        self.close()
        self.window.show()


class ResultPage(QMainWindow, ResultWindow):  # Окно с результатами теста
    def __init__(self, ancestor, ncorrect, nall, test):
        super().__init__()
        # uic.loadUi('res.ui', self)
        self.setupUi(self)
        self.ncorrect = ncorrect
        self.percent = self.ncorrect * 100 // nall
        self.test = test
        self.ancestor = ancestor
        self.save_result()
        self.display_correct.display(ncorrect)
        self.display_all.display(nall)
        self.pb_exit_res.clicked.connect(self.exit_res)

    def save_result(self):
        test_name = self.test + '.csv'
        for symbol in ['?', '\\', '/', '"', '<', '>', '|']:
            test_name = test_name.replace(symbol, '')
        with open(test_name, 'w', encoding='utf-8', newline='') as filename:
            writer = csv.writer(filename, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if not os.path.exists(self.test + '.csv'):
                writer.writerow(['Имя', 'Количество правильных ответов', 'Процент правильных ответов'])
            writer.writerow([USERNAME, self.ncorrect, self.percent])
            print(USERNAME)

    def exit_res(self):  # Возвращение в меню
        self.ancestor.ancestor.show()
        self.close()


class TestPage(QMainWindow, TestWindow):  # Окно с тестом
    def __init__(self, ancestor, test):
        super().__init__()
        # uic.loadUi('test.ui', self)
        self.setupUi(self)
        self.ancestor = ancestor
        self.test = test
        self.question_index = 0
        self.question_list = []
        self.do_check = False
        self.do_res = False
        self.correct = 0
        self.pb_test_exit.clicked.connect(self.test_exit)
        self.test_init()
        self.pb_ans1.clicked.connect(self.check)
        self.pb_ans2.clicked.connect(self.check)
        self.pb_ans3.clicked.connect(self.check)
        self.pb_ans4.clicked.connect(self.check)
        self.update_question()
        self.pb_complete.clicked.connect(self.show_result)

    def test_init(self):    # Получение теста из базы данных
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        for question in cur.execute("""SELECT questions.text, questions.correct_ans,
                 questions.incorrect_ans1, questions.incorrect_ans2, questions.incorrect_ans3
                  FROM questions INNER JOIN tests ON tests.id = questions.testId
                   WHERE tests.title = ?""", (self.test,)):
            self.question_list.append(question)
        con.close()

    def update_question(self):  # Переход к следующему вопросу и завершение тестирования если воросы кончились
        for pb in [self.pb_ans1, self.pb_ans2, self.pb_ans3, self.pb_ans4]:
            pb.setStyleSheet('default')
        if self.question_index < len(self.question_list):
            text, self.corr_ans, incorr_ans1, incorr_ans2, incorr_ans3 =\
                self.question_list[self.question_index]
            self.question_index += 1
            self.q_text_display.setText(text)
            answers = [self.corr_ans, incorr_ans1, incorr_ans2, incorr_ans3]
            answers = [str(elem) for elem in answers]
            self.pb_ans1.setText(choice(answers))
            answers.remove(self.pb_ans1.text())
            self.pb_ans2.setText(choice(answers))
            answers.remove(self.pb_ans2.text())
            self.pb_ans3.setText(choice(answers))
            answers.remove(self.pb_ans3.text())
            self.pb_ans4.setText(choice(answers))
            answers.remove(self.pb_ans4.text())
            self.do_check = True

    def check(self):  # Проверка правильности ответа, изменение цвета кнопки
        if self.do_check:
            self.do_check = False
            if self.sender().text() == str(self.corr_ans):
                self.sender().setStyleSheet('background-color: green')
                threading.Timer(2, self.update_question).start()
                self.correct += 1
            else:
                self.sender().setStyleSheet('background-color: red')
                threading.Timer(2, self.update_question).start()

    def show_result(self):  # Переход к окну с результатами
        self.close()
        self.resu = ResultPage(self, self.correct, len(self.question_list), self.test)
        self.resu.show()

    def test_exit(self):  # Выход в меню
        self.close()
        self.ancestor.show()


class TestForm(QMainWindow):  # Форма выбора теста для прохождения
    def __init__(self, ancestor):
        super().__init__()
        self.setGeometry(400, 400, 250, 150)
        self.setWindowTitle('Выбирете тест')
        self.ancestor = ancestor
        self.choose_test = QComboBox(self)
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        for test_title in cur.execute("""SELECT title FROM tests"""):
            self.choose_test.addItem(test_title[0])
        con.close()
        self.choose_test.move(60, 30)
        self.pb_form_exit = QPushButton('Отмена', self)
        self.pb_form_exit.move(10, 80)
        self.pb_continue = QPushButton('Начать', self)
        self.pb_continue.move(120, 80)
        self.pb_continue.clicked.connect(self.start)
        self.pb_form_exit.clicked.connect(self.close)

    def start(self):  # Начало теста
        self.close()
        self.ancestor.run_test(self.choose_test.currentText())


class QuestionForm(QMainWindow, FormWindow):  # Форма для создания вопроса
    def __init__(self, ancestor):
        super().__init__()
        self.ancestor = ancestor
        # uic.loadUi('form.ui', self)
        self.setupUi(self)
        self.pb_form_exit.clicked.connect(self.form_exit)
        self.pb_form_add_question.clicked.connect(self.save_question)

    def save_question(self):  # Сохранение вопроса, если поля заполнены правильно, иначе
        # вывод сообщения об ошибке
        text = self.get_q_text.text()
        corr_ans = self.get_corr_ans.text()
        incorr_ans1 = self.get_incorr_ans_1.text()
        incorr_ans2 = self.get_incorr_ans_2.text()
        incorr_ans3 = self.get_incorr_ans_3.text()
        if text and corr_ans and incorr_ans1 and incorr_ans2 and incorr_ans3:
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            test_id = cur.execute("""SELECT id FROM tests WHERE title = ?""",
                                  (self.ancestor.choose_test.currentText(),)).fetchone()[0]
            cur.execute("""INSERT INTO questions(testId, text, correct_ans, incorrect_ans1,
             incorrect_ans2, incorrect_ans3) VALUES(?, ?, ?, ?, ?, ?)""",
                        (test_id, text, corr_ans, incorr_ans1, incorr_ans2, incorr_ans3))
            con.commit()
            self.close()
            self.ancestor.status_bar_2.setText('Вопрос успешно добавлен')
            self.ancestor.update_table()
        else:
            self.status_bar.setText('ОШИБКА: Заполнены не все поля')

    def form_exit(self):  # Отмена создания вопроса
        self.close()
        self.ancestor.status_bar_2.setText('Добавление вопроса отменено')


class EditPage(QMainWindow, EditWindow):  # Окно редактирования тестов
    def __init__(self, ancestor):
        super().__init__()
        # uic.loadUi('edit.ui', self)
        self.setupUi(self)
        self.ancestor = ancestor
        self.do_update = False
        self.warning = False
        self.ids = []
        self.selected = -1
        self.pb_addTest.clicked.connect(self.add_test)
        self.update_list_of_tests()
        self.update_table()
        self.pb_exit_edit.clicked.connect(self.exit_edit)
        self.pb_exit_edit_2.clicked.connect(self.exit_edit)
        self.choose_test.currentTextChanged.connect(self.update_table)
        self.pb_addQuestion.clicked.connect(self.add_question)
        self.tableView.itemChanged.connect(self.item_changed)
        self.pb_delete.clicked.connect(self.delete_elems)

    def add_test(self):  # Создание нового теста, если все поля заполнены правильно,
        # иначе вывод сообщения об ошибке
        test_title = self.get_test_title.text()
        test_topic = self.get_test_topic.text()
        if test_title and test_topic:
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            if not cur.execute("""SELECT * FROM tests WHERE title = ?""", (test_title,)).fetchone():
                if not cur.execute("""SELECT * FROM topics WHERE title = ?""", (test_topic,)).fetchone():
                    cur.execute("""INSERT INTO topics(title) VALUES(?)""", (test_topic,))
                cur.execute("""INSERT INTO tests(title, topicId)
                 VALUES(?, (SELECT id FROM topics WHERE title = ?))""", (test_title, test_topic))
                con.commit()
                self.update_list_of_tests()

            else:
                self.status_bar.setText('ОШИБКА: Тест с таким названием уже существует')
            con.close()
        else:
            self.status_bar.setText('ОШИБКА: Заполнены не все поля')

    def update_list_of_tests(self):  # Обновление списка тестов
        self.choose_test.clear()
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        for test_title in cur.execute("""SELECT title FROM tests"""):
            self.choose_test.addItem(*test_title)
        con.close()
        self.modified = {}

    def update_table(self):  # Обновление таблицы вопросов при её редактировании или выборе другого теста
        self.do_update = False
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        result = cur.execute("""SELECT questions.id, questions.text, questions.correct_ans,
         questions.incorrect_ans1, questions.incorrect_ans2, questions.incorrect_ans3
          FROM questions INNER JOIN tests ON tests.id = questions.testId
           WHERE tests.title = ?""", (self.choose_test.currentText(),)).fetchall()
        con.close()
        self.tableView.setRowCount(len(result))
        self.tableView.setColumnCount(5)
        self.headers = ['текст', 'правильный ответ', 'неправильный ответ1',
                        'неправильный ответ2', 'неправильный ответ3']
        self.tableView.setHorizontalHeaderLabels(self.headers)
        self.ids.clear()
        if result:
            if not self.warning:
                self.status_bar_2.setText(f'Вопросов в тесте {self.choose_test.currentText()}: {len(result)}')
            else:
                self.warning = False
            for i, elem in enumerate(result):
                self.ids.append(elem[0])
                for j, val in enumerate(elem[1:]):
                    print(i, j, val)
                    self.tableView.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            if not self.warning:
                self.status_bar_2.setText('Похоже, что в этом тесте ещё нет вопросов')
            else:
                self.warning = False
        self.do_update = True

    def add_question(self):  # Создание формы создания вопроса
        self.form = QuestionForm(self)
        self.form.show()
        self.update_table()

    def item_changed(self, item):  # Обработка изменений в таблице вопросов
        titles = {'текст': 'id', 'правильный ответ': 'correct_ans',
                  'неправильный ответ1': 'incorrect_ans1', 'неправильный ответ2': 'incorrect_ans2',
                  'неправильный ответ3': 'incorrect_ans3'}
        if self.do_update:
            if item.text():
                title = titles[self.headers[item.column()]]
                id = self.ids[item.row()]
                con = sqlite3.connect(DATABASE)
                cur = con.cursor()
                cur.execute(f"""UPDATE questions SET {title} = '{item.text()}' WHERE id = {id}""")
                con.commit()
            else:
                self.status_bar_2.setText('ОШИБКА: Нельзя осталвять поля пустыми')
                self.warning = True
                self.update_table()

    def delete_elems(self):  # Удаление элементов таблицы вопросов
        rows = list(set([i.row() for i in self.tableView.selectedItems()]))
        ids2 = [str(self.ids[i]) for i in rows]
        if ids2:
            message = 'Действительно удалить элементы №'
            if len(ids2) == 1:
                message = 'Действительно удалить элемент №'
            valid = QMessageBox.question(
                self, '', message + ",".join([str(self.ids.index(int(i)) + 1) for i in ids2]),
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                con = sqlite3.connect(DATABASE)
                cur = con.cursor()
                cur.execute("DELETE FROM questions WHERE id IN (" + ", ".join(
                    '?' * len(ids2)) + ")", ids2)
                con.commit()
                self.update_table()
        else:
            self.status_bar_2.setText('ОШИБКА: Элементы для удаления не выбраны')

    def exit_edit(self):  # Выход в меню
        self.ancestor.show()
        self.close()


class MyWidget(QMainWindow, MenuWindow):  # Меню
    def __init__(self):
        super().__init__()
        # uic.loadUi('menu.ui', self)
        self.setupUi(self)
        self.pb_edit.clicked.connect(self.edit_page)
        self.pb_exit.clicked.connect(self.close)
        self.pb_start.clicked.connect(self.start_test)

    def edit_page(self):  # Переход к окну редактирования тестов
        self.hide()
        self.edit = EditPage(self)
        self.edit.show()

    def start_test(self):  # Создание формы выбора теста для прохождения
        self.form = TestForm(self)
        self.form.show()

    def run_test(self, test):  # Начало теста
        self.hide()
        self.test = TestPage(self, test)
        self.test.show()


def except_hook(cls, exception, traceback):  # Вывод системных ошибок в консоль
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':  # Запуск приложения
    app = QApplication(sys.argv)
    ex = EnterPage()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
