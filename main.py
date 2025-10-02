from flet import *
def main(page:Page):
    page.title='first app'
    page.window.width=390
    page.window.height=700
    page.bgcolor=Colors.BLUE
    page.window.top=50
    page.window.left=200
    page.window.title_bar_buttons_hidden=True
    Page.horizontal_alignment="center"
    page.vertical_alignment="center"
    T=Text('hello world')
    B=ElevatedButton(text='button')
    I=Image(src='cat.png')
    page.add(T)
    page.add(B)
    page.add(I)
    
    

    page.update()
app(main)
