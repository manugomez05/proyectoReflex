import reflex as rx

class State(rx.State):
    count: int=0

    def increment(self):
        self.count+=1
    
    def incrementx2(self):
        self.count+=2

    def decrement(self):
        self.count-=1
    
    def decrementx2(self):
        self.count-=2

def index():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                border_radius="1em",
                on_click=State.decrement    
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                border_radius="1em",
                on_click=State.increment
            ),
            rx.vstack(
                rx.hstack(
            rx.button(
                "Decrement x2",
                color_scheme="ruby",
                border_radius="1em",
                on_click=State.decrementx2
            ),
             rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment x2",
                color_scheme="grass",
                border_radius="1em",
                on_double_click=State.incrementx2
            )
            )
        )
        )
    )


app=rx.App()
app.add_page(index)
app._compile()