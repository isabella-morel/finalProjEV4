# https://starplot.dev/examples/star-chart-detail/
# https://flet.dev/docs/controls/bottomsheet/
# https://www.w3resource.com/python-interview/what-are-async-and-await-keywords-in-python.php 
# ^^ THIS WAS A LIFE SAVIOR OMG THE HOURS I SPENT RESEARCHING TO FIND THIS - Isabella

import flet as ft
from datetime import datetime
from pytz import timezone
from starplot import MapPlot, Projection, _
from starplot.styles import PlotStyle, extensions

tz = timezone("America/New_York")

async def star_chart(year, month, day, hour, minute):
    global dt
    dt = datetime(year, month, day, hour, minute, 0, tzinfo=tz)

    plot = MapPlot(
        projection= Projection.ZENITH,
        lat = 18.4861, # SD, DR
        lon = -69.9312,
        style = PlotStyle().extend(extensions.BLUE_GOLD),
        resolution = 3600,
        autoscale= True
    )

    plot.horizon()
    plot.constellations()
    plot.stars(where = [_.magnitude < 4.6], where_labels = [_.magnitude < 2.1])
    plot.galaxies(where = [_.magnitude < 9], true_size = False, labels = None)
    plot.open_clusters(where=[_.magnitude < 9], true_size=False, labels=None)
    plot.constellation_borders()
    plot.ecliptic()
    plot.celestial_equator()
    plot.milky_way()

    plot.marker(
        ra=12.36 * 15,
        dec=25.85,
        style={
            "marker": {
                "size": 60,
                "symbol": "circle",
                "fill": "none",
                "color": None,
                "edge_color": "hsl(44, 70%, 73%)",
                "edge_width": 2,
                "line_style": [1, [2, 3]],
                "alpha": 1,
                "zorder": 100,
            },
            "label": {
                "zorder": 200,
                "font_size": 22,
                "font_weight": "bold",
                "font_color": "hsl(44, 70%, 64%)",
                "font_alpha": 1,
                "offset_x": "auto",
                "offset_y": "auto",
                "anchor_point": "top right",
            },
        },
        label="Mel 111",
    )

    plot.constellation_labels()
    plot.export(f"assets/star_chart_detail{dt}.png", transparent=True, padding=0.1)

async def main(page: ft.Page):

    page.title= "Sky Map"

    page.window.height = 750
    page.window.width = 1000

    star= ft.Image(src="star.png", width=20, height=20)
    text= ft.Text("SKY MAP", size=30,color="blue", font_family="georgia", 
                  italic=True, weight=ft.FontWeight.W_200)

    day =ft.TextField(label="Day",width=100)
    month = ft.TextField(label="Month",width=100)
    year = ft.TextField(label="year",width=100)
    hour = ft.TextField(label="Hour",width=100)
    minute = ft.TextField(label="minute",width=100)
    
    picture = ft.Image(src="star.png", width=540, height=540, visible=False)
    
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
        
    async def add_pic(e):
        try:
            y = int(year.value)
            m = int(month.value)
            d = int(day.value)
            h = int(hour.value)
            mi = int(minute.value)
            
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
            if mi < 0 or mi > 59:
                show_error("minute must be between 0 and 59.")
                return
            
            await star_chart(y, m, d, h, mi)
            file = f"star_chart_detail{dt}.png"

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