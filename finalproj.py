import flet as ft

def star_chart(year, month, day, hour, minute):
    pass

def main(page: ft.Page):
    page.title= "Sky Map"
    star= ft.Image(src="star.png", width=20, height=20)
    text= ft.Text("SKY MAP", size=30,color="blue", font_family="georgia", 
                  italic=True, weight=ft.FontWeight.W_200)

    day =ft.TextField(label="Day",width=100)
    month = ft.TextField(label="Month",width=100)
    year = ft.TextField(label="year",width=100)
    hour = ft.TextField(label="Hour",width=100)
    minute = ft.TextField(label="Minute",width=100)
    
    picture = ft.Image(src="star.png, width=400, height=400, visible=False")
    
    bottom_sheet = ft.BottomSheet(
        content=ft.Container(
            content=ft.Text("Error message will appear here."),
            padding=20,
        ),
        open=False
    )
    page.overlay.append(bottom_sheet)
    
    def show_error(message):
        bottom_sheet.content.content = ft.Text(message)
        bottom_sheet.open = True
        page.update()
        
    def add_pic(e):
        try:
            y= int(year.value)
            m= int(month.value)
            d= int(day.value)
            h= int(hour.vaulue)
            min= int(minute.value)
            
            if y < 2000 or y > 2024:
                show_error("Year must be between 2000 and 2024.")
                return
            if m < 1 or m > 12:
                show_error("Month must be between 1 and 12.")
                return
            if d < 1 or d > 31:
                show_error("Day must be between 1 and 31.")
                return
            if h < 0 or h > 23:
                show_error("Hour must be between 0 and 23.")
                return
            if min < 0 or min > 59:
                show_error("Minute must be between 0 and 59.")
                return
            
            star_chart(y, m, d, h, min)
            file = f"star_chart_detail.png"
            
            picture.src = file
            picture.visible = True
            page.update()
            
        except ValueError:
            show_error("All fields must contain valid numbers.")
            

    submit= ft.ElevatedButton("Submit", width=100, on_click=add_pic)


    page.add(ft.Row([star,text,star], alignment = ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([day,month,year,hour,minute],
        alignment = ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([submit],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([picture], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target = main, assets_dir="assets")