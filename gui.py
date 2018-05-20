import sys
import random
from PyQt5 import QtWidgets
from enum import Enum

from PyQt5.QtCore import Qt


class Ages(Enum):
    STUDENT = 1,
    MIDDLE_PERSON = 2,
    OLD_PERSON = 3,
    VERY_OLD_PERSON = 4


class messengers(Enum):
    TELEGA = 1;
    WHATS_APP = 2;
    VIBER = 3;
    FACEBOOK_MESSENGER = 4;

class Canals(Enum):
    MESSENGER = 1,
    SMS = 2,
    PUSH = 3,
    LK = 4


message = ""

GREETING_MAN = (
    'Hello, brother ',
    'Здравствуй! ',
    'Драсьте! ',
    'Привет! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Салют! ',
    'Здорово!',
    'Дарова! ',
    'Хэлло! ',
    'Хай! ',
    'Вечер в хату! ',
    'Глубокое (глубочайшее) почтение ',
    'Горячий привет! ',
    'С добрым утром! ',
    'Здра ',
    'Прив ',
    'Приветики ',
    'Превед ',
    'Здравки ',
    'Доброго здоровьечка ) ',
    'HI ',
    'Guten Tag ',
    'Guten Morgen ',
    'Guten Nacht ',
    'Bonjour ',
    'Hola ',
)

GREETING_WOMAN = (
    'Hello,sister',
    'Здравствуй! ',
    'Драсьте! ',
    'Привет! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Салют! ',
    'Здорово!',
    'Дарова! ',
    'Хэлло! ',
    'Хай! ',
    'Вечер в хату! ',
    'Глубокое (глубочайшее) почтение ',
    'Горячий привет! ',
    'С добрым утром! ',
    'Здра ',
    'Прив ',
    'Приветики ',
    'Превед ',
    'Здравки ',
    'Доброго здоровьечка ) ',
    'HI ',
    'Guten Tag ',
    'Guten Morgen ',
    'Guten Nacht ',
    'Bonjour ',
    'Hola ',
)

GREETIN_MIDDLE = (

    'Здравствуйте! ',
    'Здравствуй! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Приятного вечера! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Приветствую вас! ',
    'В кои-то веки! ',
    'Вот так встреча! ',
    'Всегда рады Вам ',
    'Добро пожаловать! ',
    'Дозвольте приветствовать (Вас) ',
    'Душевно рад (Вас видеть) ',
    'Душою рад Вас видеть ',
    'Желаю здравствовать! ',
    'Здравия желаю ',
    'Какая встреча! ',
    'Какие гости! ',
    'Позвольте Вас приветствовать ',
    'Приветствую Вас ',
    'Приятный вечер! ',
    'Приятный день! ',
    'Рад Вам ',
    'Рад Вас видеть ',
    'Рад Вас видеть в добром здравии ',
    'Рад Вас приветствовать ',
    'Рад Вас слышать ',
    'Разрешите Вас приветствовать ',
    'С возвращением! ',
    'С выздоровлением! ',
    'С добрым утром! ',
    'Сердечно приветствую Вас! ',
    'Сердечно рад Вам ',
    'Сердечный поклон Вам ',
    'Сколько лет, сколько зим! ',
    'Тысячу лет Вас не видел (не виделись)! '
)

GREETING_VERY_OLD = (
    'Сердечно приветствую Вас! ',
    'Сердечно рад Вам ',
    'Здравствуйте! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Приятного вечера! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Приветствую вас! ',
    'В кои-то веки! ',
    'Вот так встреча! ',
    'Всегда рады Вам ',
    'Глубокое (глубочайшее) почтение ',
    'Доброго здоровья (здоровьица...)! ',
    'Добро пожаловать! ',
    'Дозвольте приветствовать (Вас) ',
    'Душевно рад (Вас видеть) ',
    'Душою рад Вас видеть ',
    'Желаю здравствовать! ',
    'Здравия желаю ',
    'Моё почтение! ',
    'Нижайшее почтение! ',
    'Позвольте Вас приветствовать ',
    'Почитаю приятным долгом засвидетельствовать Вам моё почтение ',
    'Приветствую Вас '
)

MORE_CALLS = (
    '\nwhat about up your phone calls? ',
)

MORE_SMSs = (
    '\nwhat about up your phone sms? ',
)

MORE_INTERNET = (
    '\nwhat about more INTERNET? ',
)

NEUTRAL_MESSAGE = (
    '\nHAVE a GOOD day ',
)

TARIF = (
    ('Включайся! Слушай', 450, 10),
    ('Включайся! Общайся', 600, 15),
    ('Включайся! Говори', 700, 5),
    ('Включайся! Смотри', 800, 20),
    ('Включайся! Смотри+', 1000, 25),
    ('Включайся! Пиши', 200, 5, 10),
    ('Включайся! Премиум', 3000, 30, 0)
)
TARIF_SNG = (
    ('Тёплый приём М', 500, 13, 300),
    ('Тёплый приём S', 300, 3, 100)
)

d = {
    'VPN': ["Большой брат следит за тобой..."],
    'SMS': ["ПС, парень - не хочешь немного халявы?"],
    'Netflix': ["Кайло Рен убьет хана Соло. Не хочешь спойлеров"],
    'Porno': ["Не души свое одиночество - воспользуйся тарифом и  премиум на месяц в Boody твой. "]
}

TELEGRAM = {
    "Роскомнадзор мешает жизни??? Подключите тариф и получите лучший VPN от Мегафонпа"
}

WHATSAPP = {
    "ffd"
    "dvgd"
}

VIBER = {
    "gfh"
    ":l"
}

FACEBOOKMESSENGER = {
    "dgdg"
    "dffg"
    "sdgew"
}

FAT_TEXT = 'VPN был классным!!!!'

MAIN_BIG_OFFER = '\nКаждый из нас склонен выбирать как жить, как думать, что выбирать... ' \
             'но иногда в переломные моменты нам требуется помощь. ' \
             'Мегафон заботится о каждом из клиентов и вашему вниманию предлагается тариф %s мы любим Вас, Ваш Мегафон'

MAIN_MIN_OFFER = '\nМегафон заботится о каждом из клиентов и вашему вниманию предлагается тариф %s мы любим Вас, Ваш Мегафон'

def get_messenger(messanger):
    global message
    if messanger == messengers.TELEGA:
        message += TELEGRAM[random.randrange(len(TELEGRAM))]
        return messengers.TELEGA
    elif messanger == messengers.WHATS_APP:
        message += WHATSAPP[random.randrange(len(WHATSAPP))]
        return messengers.WHATS_APP
    elif messanger == messengers.VIBER:
        message += VIBER[random.randrange(len(VIBER))]
        return messengers.VIBER
    elif messanger == messengers.FACEBOOK_MESSENGER:
        message += FACEBOOKMESSENGER[random.randrange(len(FACEBOOKMESSENGER))]
        return messengers.FACEBOOK_MESSENGER
    else :
        message += NEUTRAL_MESSAGE[random.randrange(len(NEUTRAL_MESSAGE))]


def get_dop_info():
    global FAT_TEXT
    for key in d.keys():

        if key in FAT_TEXT:
            index = random.randrange(0, len(d[key]))
            return d[key][index]
    return NEUTRAL_MESSAGE



def get_age(age, male):
    message = ''
    if (17 >= age):
        message += 'Слишком молодой, чтобы что-либо получать'
    elif (18 <= age <= 27):
        if male == 'M':
            message += GREETING_MAN[random.randrange(len(GREETING_MAN))]
        else:
            message += GREETING_WOMAN[random.randrange(len(GREETING_WOMAN))]
        CANALS = ['Messengers', 'LK', 'mob']

        #return Ages.STUDENT
    elif (27 < age <= 45):
        message += GREETIN_MIDDLE[random.randrange(len(GREETIN_MIDDLE))]
        CANALS = ['Messengers', 'SMS', 'LK', 'mob']
        #return Ages.MIDDLE_PERSON
    elif (45 < age <= 100):
        message += GREETING_VERY_OLD[random.randrange(len(GREETING_VERY_OLD))]
        CANALS = ['Messengers', 'SMS', 'LK', 'mob']
        #return Ages.OLD_PERSON
    #else:
        CANALS = ['Messengers', 'LK', 'mob']
    return message


def parse_attr(calls, SMS, Internet, tarif):
    message = ''
    SS = check_out_tarif(calls, tarif[0], 1) + check_out_tarif(SMS, tarif[1], 3) + check_out_tarif(Internet, tarif[2],
                                                                                                   5)
    if SS == 1:
        message += MORE_CALLS[random.randrange(len(MORE_CALLS))]

    elif SS == 3:
        message += MORE_SMSs[random.randrange(len(MORE_SMSs))]
    elif SS == 4:
        message += " calls and messages"
    elif SS == 5:
        message += MORE_INTERNET[random.randrange(len(MORE_INTERNET))]
    elif SS == 8:
        message += " messages and internet"
    elif SS == 6:
        message += " inet calls"
    elif SS == 9:
        message += "all"
    else:
        message += NEUTRAL_MESSAGE[random.randrange(len(NEUTRAL_MESSAGE))]

    return message

def check_out_tarif(values, tarif_val, inc):
    global message
    for value in values:
        if value > tarif_val:
            return inc
    return 0

#   Мессенджеров много (>30% - мессенджеры) иначе SMS или Push уведомления  - заголовки.
#   анализ отказа
#   ЛК и мобильное - всегда, если есть мобильное приложение - Push уведомления (использование доп инфы)
#   ЛК и моб - сравнение тарифов отдельным уведомлением. Не нравится статистика: смотри тут и тут
#   взрослым людям - предложение для близких
#   студентам - предложение с похожей стоимостью

class Example(QtWidgets.QWidget):
    def __init__(self, lines, text, comboBox, calls, sms, inet, tarif):
        super().__init__()
        self.lines = lines
        self.text = text
        self.comboBox = comboBox
        self.genderBox = QtWidgets.QComboBox()
        self.slider_labels = {}
        self.calls = calls
        self.sms = sms
        self.inet = inet
        self.tarif = tarif
        self.usual = QtWidgets.QRadioButton('usual')
        self.sng = QtWidgets.QRadioButton('sng')
        self.window()

    def window(self):
        self.setGeometry(100, 50, 800, 500)
        form = QtWidgets.QFormLayout()
        self.text.setReadOnly(True)
        main_container = QtWidgets.QHBoxLayout()
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("Выберите тариф:")
        gender_age = QtWidgets.QHBoxLayout()
        self.genderBox.addItem("M")
        self.genderBox.addItem("F")
        gender_age.addWidget(self.genderBox)
        gender_age.addLayout(self.create_slider_box('age', '21', 14, 100, 21))
        form.addRow("Gender & age", gender_age)

        for tarif in TARIF:
            self.comboBox.addItem(tarif[0])
        self.comboBox.activated.connect(lambda: self.choose_tarif_listener())
        form.addRow('Plan', self.comboBox)

        arr = ['Calls', 'SMS', 'Internet']
        for i in range(len(arr)):
            line = QtWidgets.QLineEdit()
            # line.setPlaceholderText('tarif: %s' % str(self.get_real_tarif()))
            self.lines[arr[i]] = line
            form.addRow(arr[i], line)

        form.addRow('Messengers', self.create_slider_box('messenger', '50', 0, 100, 50))
        form.addRow('Profile', self.create_slider_box('profile', '50', 0, 100, 50))
        form.addRow('mobApp', self.create_slider_box('mob', '50', 0, 100, 50))

        buttons = QtWidgets.QHBoxLayout()
        self.usual.setChecked(True)
        self.usual.clicked.connect(self.tarif_radio_listener)
        self.sng.clicked.connect(self.tarif_radio_listener)
        buttons.addWidget(self.usual)
        buttons.addWidget(self.sng)
        buttonGroup = QtWidgets.QGroupBox()
        buttonGroup.setLayout(buttons)
        form.addRow('Location', buttonGroup)


        okButton = QtWidgets.QPushButton("OK")
        okButton.clicked.connect(self.listener)

        vbox_right = QtWidgets.QVBoxLayout()
        self.results = []
        # arr_results = ['first', 'second', 'third']
        for i in range(3):
            line = QtWidgets.QTextEdit()
            self.results.append(line)
            # line.setPlaceholderText('tarif: %s' % str(self.get_real_tarif()))
            vbox_right.addWidget(line)

        vbox_left = QtWidgets.QVBoxLayout()
        vbox_left.addLayout(form)
        vbox_left.addWidget(okButton)

        main_container.addLayout(vbox_left)
        main_container.addLayout(vbox_right)
        self.setLayout(main_container)
        self.show()

    def listener(self):
        global message
        age = self.slider_labels['age'].text()
        gender = self.genderBox.itemText(self.genderBox.currentIndex())
        calls = self.lines['Calls'].text().split(',')
        sms = self.lines['SMS'].text().split(',')
        inet = self.lines['Internet'].text().split(',')
        tarif = self.get_real_tarif()
        tarif_list = [str(tarif[1]), str(tarif[2]), str(tarif[3]) if len(tarif) == 4 else '99999']

        # For what
        for i in range(3):
            self.results[i].setText('')
        canals = self.choose_canals()
        i = 0
        for canal in canals:
            self.results[i].setText(canal)
            if 'SMS' in canal:
                self.add_text_to_result(get_age(int(age), gender), self.results[i])
                self.add_text_to_result(parse_attr(calls, sms, inet, tarif_list), self.results[i])
                self.add_text_to_result(MAIN_MIN_OFFER, self.results[i])
            elif 'messenger' in canal:
                a = random.randrange(2)
                if a == 1:
                    self.add_text_to_result(get_dop_info(), self.results[i])
                else:
                    self.add_text_to_result(get_age(int(age), gender), self.results[i])
                self.add_text_to_result(parse_attr(calls, sms, inet, tarif_list), self.results[i])
                self.add_text_to_result(MAIN_MIN_OFFER, self.results[i])
            elif 'mobApp' in canal:
                self.add_text_to_result(get_dop_info(), self.results[i])
                self.add_text_to_result(MAIN_BIG_OFFER, self.results[i])
            else:
                self.add_text_to_result(get_dop_info(), self.results[i])
                self.add_text_to_result(MAIN_BIG_OFFER, self.results[i])
            i+=1

    def choose_canals(self):
        canals = []
        if self.slider_labels['messenger'].text() > '30':
            canals.append('Message for messenger: \n')
        if self.slider_labels['profile'].text() > '50':
            canals.append('Message for profile: \n')
        if self.slider_labels['mob'].text() > '30':
            canals.append('Message for mobApp: \n')
        else:
            canals.append('Message for SMS: \n')
        return canals

    def add_text_to_result(self, text, text_block):
        text_old = text_block.toPlainText()
        text_block.setText(text_old + text)

    def get_real_tarif(self):
        real_tarif_str = str(self.comboBox.itemText(self.comboBox.currentIndex()))
        real_tarif = tuple()
        for t in TARIF:
            if t[0] == real_tarif_str:
                real_tarif = t
        for t in TARIF_SNG:
            if t[0] == real_tarif_str:
                real_tarif = t
        return real_tarif

    def tarif_radio_listener(self):
        self.comboBox.clear()
        for tarif in TARIF:
            self.comboBox.addItem(tarif[0])
        if self.sng.isChecked():
            for tarif in TARIF_SNG:
                self.comboBox.addItem(tarif[0])

    def choose_tarif_listener(self):
        tarif = self.get_real_tarif();
        self.lines['Calls'].setPlaceholderText('tarif: %s min' % str(tarif[1]))
        self.lines['Internet'].setPlaceholderText('tarif: %s Gb' % str(tarif[2]))
        self.lines['SMS'].setPlaceholderText('tarif: %s sms' % str(tarif[3]) if len(tarif) == 4 else '99999')

    def create_slider_box(self, type_label, label_text, min, max, now):
        box = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel(label_text)
        self.slider_labels[type_label] = label
        slider = QtWidgets.QSlider(Qt.Horizontal)
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setValue(now)
        slider.valueChanged.connect(lambda: self.slider_value_change(label, slider))
        box.addWidget(label)
        box.addWidget(slider)
        return box

    def slider_value_change(self, label, slider):
        label.setText(str(slider.value()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example(dict(), QtWidgets.QTextEdit(), QtWidgets.QComboBox(), [], [], [], [])
    sys.exit(app.exec_())
