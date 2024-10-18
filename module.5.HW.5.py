import time
from importlib.metadata import files
from random import vonmisesvariate


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)  # hash() - адрес в виде строки, который возвращает некое значение
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname

    # def get_info(self):
    #     return self.nickname, self.password


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    current_user = None

    def __init__(self):
        # users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
        self.users = []
        self.videos = []

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == str(user) and hash(password) == hash(user.password):
                self.current_user = user
                break
            elif nickname == str(user) and hash(password) != hash(user.password):
                print(f'{self.current_user}, пароль не верный, попробуй ещё раз.')
                break
            else:
                print(f'Такого пользователя не существует')

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        current_user = None

    def add(self, *args):
        for vid in args:
            vid_is_exist = False
            for v in self.videos:
                if vid.title == v.title:
                    print('существует')
                    vid_is_exist - True
                    break
            if vid_is_exist:
                break
            else:
                self.videos.append(vid)

    def get_videos(self, word):
        search_list = []
        for vid in self.videos:
            str_lower = str(vid.title).lower()
            if word.lower() in str_lower:
                search_list.append(vid.title)
        # Перебираем список видео и сравниваем поисковое слово в нижнем регистре с заголовком видео в нижнем регистре
        # Если нашли похожее - добавляем в список search_list = []
        return search_list

    def watch_video(self, title_for_play):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for vid in self.videos:
                if vid.title == title_for_play:
                    if vid.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        while vid.time_now < vid.duration:
                            print(vid.time_now + 1, end=" ")
                            vid.time_now += 1
                            time.sleep(0.5)
                        print("Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

















