import flet as ft

def main(page: ft.Page):
    page.title= "sky map"
    star= ft.Image(src="star.png",width=20, height=20)
    text= ft.Text("SKY MAP",size=30,color="blue",font_family="georgia",italic=True,
    weight=ft.FontWeight.W_200,)

    day =ft.TextField(label="day",width=100)
    month = ft.TextField(label="month",width=100)
    year = ft.TextField(label="year",width=100)
    hour = ft.TextField(label="hour",width=100)
    minute = ft.TextField(label="minute",width=100)
    
    page.add(ft.Row([star,text,star], alignment = ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([day,month,year,hour,minute],
        alignment = ft.MainAxisAlignment.CENTER))

ft.app(target = main, assets_dir="assets")