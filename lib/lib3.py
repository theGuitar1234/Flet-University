import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    user_text = ft.TextField(value=" ", text_align=ft.TextAlign.RIGHT, width=200)
    user_label = ft.Text('Text Output', text_align=ft.TextAlign.RIGHT,size=24, 
                         italic=True, color=ft.Colors.WHITE,bgcolor=ft.Colors.GREEN,
                         weight=ft.FontWeight.BOLD)
    def get_info(e):
        user_label.value = user_text.value
        page.update()

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=
            [
               user_text, 
               ft.IconButton(ft.Icons.ADD_COMMENT, on_click=get_info),            
            ],
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=
            [
                user_label
            ],))
ft.run(main)