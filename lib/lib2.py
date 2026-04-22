import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_text = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    user_label = ft.Text('Info')

    def minus_click(e):
        input.value = str(int(input.value) - 1)

    def plus_click(e):
        input.value = str(int(input.value) + 1)

    def get_info(e):
        user_label.value = user_text.value
        page.update()

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=
            [
                ft.IconButton(ft.Icons.HOME, on_click=get_info),
                user_text,
            
            ],
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=
            [
                user_label,
                user_text,
            
            ],
        )
    )

ft.run(main)