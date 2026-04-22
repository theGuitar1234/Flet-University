import flet as ft

def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 500

    page.window.left = page.width - page.window.width
    page.window.bottom = page.height - page.window.height




   
    page.title = "Wheather App"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Enter City', width=200)
    
    theme_button = ft.IconButton(ft.Icons.SUNNY)
    theme_Text = ft.Text('White Mode')

    
    def get_info(e):
        pass

    def change_theme(e):
        page.theme_mode = (ft.ThemeMode.LIGHT
                           if page.theme_mode == ft.ThemeMode.DARK
                           else ft.ThemeMode.DARK)
        theme_button.icon = (ft.Icons.BEDTIME
                             if page.theme_mode == ft.ThemeMode.LIGHT
                             else ft.Icons.SUNNY)
        theme_Text.value = ('Night Mode'
                             if page.theme_mode == ft.ThemeMode.LIGHT
                             else 'White Mode')
        page.update()
    
    theme_button.on_click = change_theme
    
    page.add(
        ft.Row(
            [
                theme_button,
                theme_Text
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(content='Search', on_click=get_info)],
               alignment=ft.MainAxisAlignment.CENTER)
    )

ft.run(main)