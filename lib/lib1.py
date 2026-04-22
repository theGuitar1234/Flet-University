import flet as ft

def main(page: ft.Page):
    page.title = "Parking App"
    # Добавим текст, чтобы убедиться, что окно не пустое
    page.add(ft.Text("Добро пожаловать в Parking App!"))

# Эта строка должна быть БЕЗ отступа
if __name__ == "__main__":
    ft.app(target=main)
