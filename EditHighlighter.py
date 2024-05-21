import winreg as reg, os

from elevate import elevate


def is_root() -> int:
    return os.getuid() == 0
elevate()


def conv_str_to_tuple(string: str) -> tuple:
    return tuple((value.strip() for value in string.split(',')))


def edit_hilight_sz(rgb: tuple | list = (0, 120, 215)) -> None:
    # default: 0 120 215
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\\Colors", 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(key, 'Hilight', 0, reg.REG_SZ, f"{rgb[0]} {rgb[1]} {rgb[2]}")
    reg.CloseKey(key)


def edit_hot_tracking_color_sz(rgb: tuple | list = (0, 102, 204)) -> None:
    # default: 0 102 204
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\\Colors", 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(key, 'HotTrackingColor', 0, reg.REG_SZ, f"{rgb[0]} {rgb[1]} {rgb[2]}")
    reg.CloseKey(key)


yes_list: tuple = ("y", "yes", "да")
langs: dict = {
    "ru": {
        "reset_color": "Вернуть цвет выделителя Windows по умолчанию? (y/n) >> ",
        "pc_restart": "Перезагрузить ПК? (y/n) >> ",
        "enter_Hilight_color": "Введите RGB код для Hilight (обводка выделителя) [Пример ввода: 125, 6, 35] >> ",
        "enter_HotTrackingColor_color": "Введите RGB код для HotTrackingColor (заливка выделителя) [Пример ввода: 255, 125, 2] >> ",
        "sure": "Вы уверены, что хотите сменить цвет выделителя? (y/n) >> ",
        "processing": "Загрузка ...",
        "done": "Готово"
    },

    "en": {
        "reset_color": "Reset color code of Windows highlighter to default? (y/n) >> ",
        "pc_restart": "Restart your PC? (y/n) >> ",
        "enter_Hilight_color": "Enter RGB color code for Hilight (highlighter border) [Example: 125, 6, 35] >> ",
        "enter_HotTrackingColor_color": "Enter RGB color code for HotTrackingColor (highlighter internal fill) [Example: 255, 125, 2] >> ",
        "sure": "Are you sure to change highlighter color? (y/n) >> ",
        "processing": "Processing ...",
        "done": "Done"
    }
}

print("Windows Highlighter Editor")

while True:
    language: str = input("Enter your language [ru, en] >> ").lower()

    if language not in langs:
        print("Invalid lang code")
        continue

    print(f"Selected lang {language}\n")
    break

while True:
    yes_or_no: str = input(langs[language]["reset_color"]).lower()
    if yes_or_no in yes_list:
        print(langs[language]["processing"])
        edit_hilight_sz()
        edit_hot_tracking_color_sz()
        print(langs[language]["done"])
        yes_or_no: str = input(langs[language]["pc_restart"]).lower()
        if yes_or_no in yes_list:
            os.system("shutdown /r /t 1")

    print("\n")

    hilight_color: tuple = conv_str_to_tuple(input(langs[language]["enter_Hilight_color"]))
    hot_tracking_color: tuple = conv_str_to_tuple(input(langs[language]["enter_HotTrackingColor_color"]))
    yes_or_no: str = input(langs[language]["sure"]).lower()
    if yes_or_no in yes_list:
        edit_hilight_sz(hilight_color)
        edit_hot_tracking_color_sz(hot_tracking_color)

    print(langs[language]["done"])
    yes_or_no: str = input(langs[language]["pc_restart"]).lower()
    if yes_or_no in yes_list:
        os.system("shutdown /r /t 1")
