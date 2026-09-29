from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
from kivy.core.window import Window
from jnius import autoclass


# =========================
# الإعدادات
# =========================

Window.clearcolor = get_color_from_hex("#101010")

BACKGROUND = "background.jpg"


# =========================
# دالة الخلفية
# =========================

def add_background(layout):
    background = Image(
        source=BACKGROUND,
        size_hint=(1, 1),
        pos_hint={"x": 0, "y": 0},
        allow_stretch=True,
        keep_ratio=False
    )

    layout.add_widget(background)
    return background


# =========================
# معلومات ثابتة
# =========================

def add_footer(layout):

    memo = Label(
        text="MEMO",
        font_size=dp(16),
        bold=True,
        color=get_color_from_hex("#FFD700"),
        size_hint=(1, None),
        height=dp(30),
        pos_hint={"center_x": 0.5, "y": 0.12}
    )

    telegram = Label(
        text="@rasa_TDM",
        font_size=dp(15),
        bold=True,
        color=get_color_from_hex("#00BFFF"),
        size_hint=(1, None),
        height=dp(30),
        pos_hint={"center_x": 0.5, "y": 0.055}
    )

    layout.add_widget(memo)
    layout.add_widget(telegram)


# =========================
# زر START
# =========================

def create_button(text, width=0.72, height=60):

    button = Button(
        text=text,
        font_size=dp(20),
        bold=True,
        size_hint=(width, None),
        height=dp(height),
        background_normal="",
        background_color=get_color_from_hex("#D91E18"),
        color=get_color_from_hex("#FFFFFF")
    )

    return button


# =========================
# الصفحة الأولى
# =========================

class WelcomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        add_background(layout)

        title = Label(
            text="WELCOME TO THE LOADER",
            font_size=dp(28),
            bold=True,
            color=get_color_from_hex("#FFFFFF"),
            size_hint=(1, None),
            height=dp(60),
            pos_hint={"center_x": 0.5, "top": 0.88}
        )

        developers = Label(
            text="ANOONI & MEMO",
            font_size=dp(20),
            bold=True,
            color=get_color_from_hex("#FFD700"),
            size_hint=(1, None),
            height=dp(45),
            pos_hint={"center_x": 0.5, "top": 0.78}
        )

        start_button = create_button("START")

        start_button.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.43
        }

        start_button.bind(
            on_release=lambda x: setattr(
                self.manager,
                "current",
                "home"
            )
        )

        layout.add_widget(title)
        layout.add_widget(developers)
        layout.add_widget(start_button)

        add_footer(layout)

        self.add_widget(layout)


# =========================
# الصفحة الثانية
# =========================

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        add_background(layout)

        title = Label(
            text="LOADER",
            font_size=dp(30),
            bold=True,
            color=get_color_from_hex("#FFFFFF"),
            size_hint=(1, None),
            height=dp(60),
            pos_hint={"center_x": 0.5, "top": 0.88}
        )

        games_button = create_button("GAMES")

        games_button.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.48
        }

        games_button.bind(
            on_release=lambda x: setattr(
                self.manager,
                "current",
                "games"
            )
        )

        layout.add_widget(title)
        layout.add_widget(games_button)

        add_footer(layout)

        self.add_widget(layout)


# =========================
# صفحة الألعاب
# =========================

class GamesScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        add_background(layout)

        title = Label(
            text="SELECT GAME",
            font_size=dp(28),
            bold=True,
            color=get_color_from_hex("#FFFFFF"),
            size_hint=(1, None),
            height=dp(60),
            pos_hint={"center_x": 0.5, "top": 0.9}
        )

        global_button = create_button(
            "PUBG MOBILE GLOBAL",
            width=0.82
        )

        global_button.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.60
        }

        global_button.bind(
            on_release=lambda x: self.open_game(
                "com.tencent.ig"
            )
        )

        korea_button = create_button(
            "PUBG MOBILE KOREA",
            width=0.82
        )

        korea_button.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.45
        }

        korea_button.bind(
            on_release=lambda x: self.open_game(
                "com.pubg.krmobile"
            )
        )

        back_button = create_button(
            "BACK",
            width=0.45,
            height=50
        )

        back_button.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.25
        }

        back_button.bind(
            on_release=lambda x: setattr(
                self.manager,
                "current",
                "home"
            )
        )

        layout.add_widget(title)
        layout.add_widget(global_button)
        layout.add_widget(korea_button)
        layout.add_widget(back_button)

        add_footer(layout)

        self.add_widget(layout)

    # =========================
    # فتح اللعبة
    # =========================

    def open_game(self, package_name):

        try:

            Intent = autoclass(
                "android.content.Intent"
            )

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            intent = Intent(
                Intent.ACTION_MAIN
            )

            intent.setPackage(package_name)

            intent.addCategory(
                Intent.CATEGORY_LAUNCHER
            )

            PythonActivity.mActivity.startActivity(
                intent
            )

        except Exception as e:

            print(
                "GAME ERROR:",
                e
            )


# =========================
# التطبيق
# =========================

class LoaderApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            WelcomeScreen(
                name="welcome"
            )
        )

        manager.add_widget(
            HomeScreen(
                name="home"
            )
        )

        manager.add_widget(
            GamesScreen(
                name="games"
            )
        )

        return manager


LoaderApp().run()