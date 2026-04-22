from flet import *
from flet_route import Params, Basket


def login(page: Page, params: Params, basket: Basket):
    session = page.session.get("session_login")

    def check_login(input_session):
        return input_session == "admin"
    
    def logout_button(e):
        page.session.clear()
        page.update()

    check = check_login(session)
    dashboard_page = Column(
        [
            Text("Welcome to the Dashboard!", size=30, weight="bold"),
            ElevatedButton("logout", on_click=logout_button),
        ]
    )

    wrong_login = Column(
        [
            ElevatedButton(
                "wrong_login", bgcolor="red", color="white", on_click=logout_button
            )
        ]
    )

    return View("/dashboard", controls=[dashboard_page] if check else wrong_login)
