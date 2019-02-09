from arcade import *
import datetime

WIDTH = 800
HIGHT = 800
CELL = 20
open_window (WIDTH,HIGHT, "Main Menu")
set_background_color(((255, 255, 255)))
start_render()
curr_date = datetime.date
for i in range (1, WIDTH//CELL):
    draw_line(CELL*i, 0, CELL * i, 800, (125, 249, 255))
for i in range (1, HIGHT// CELL ):
    draw_line(0, CELL*i, 800, CELL*i, (125, 249, 255))
draw_line(700, 0, 700, 800, (255, 0, 0), 1)
draw_text("Домашняя работа.", 200, 750, (0, 0, 255), 30)
draw_text(str(curr_date.today()), 710, 750, (0, 0, 255), 13)
draw_circle_outline(350, 500, 100, (0, 0, 0), 5)
draw_text("Молодец!", 500, 300, (255, 0, 0), 30 )
draw_text("5",530, 250, (255, 0, 0), 30 )
finish_render()
run()
