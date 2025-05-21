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

    def show_error(e):
        pass

    def add_pic(e):
        try:
            y=int(year.value)
            m=int(month.value)
            d=int(day.value)
            h=int(hour.value)
            min=int(minute.value)
        except ValueError:
            show_error("All fields must contain valid number.")
    submit= ft.Elevatedbutton("Submit", width=100, on_click=add_pic)


    page.add(ft.Row([star,text,star], alignment = ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([day,month,year,hour,minute],
        alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([submit],aligment=ft.MainAxisAligment.CENTER))

ft.app(target = main, assets_dir="assets")