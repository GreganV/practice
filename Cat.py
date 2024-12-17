import DrawingPanel


panel = DrawingPanel.DrawingPanel(400,400)

panel.set_background('black')

#outer left ear
panel.fill_polygon(115,150,110,65,175,110, 'ivory')
#inner left ear
panel.fill_polygon(123,130,113,70,150,100,'light pink')

#iuter right ear
panel.fill_polygon(230,110,280,139,280,65, 'ivory')
#inner right ear
panel.fill_polygon(235,130,275,159,277,70, 'light pink')

#head
panel.fill_oval(100,100,200,200, color = 'ivory')
#left eye
panel.fill_oval(135,150,50,50, color = 'light cyan')
#right eye
panel.fill_oval(210,150,50,50, color = 'peach puff')

#left pupil
panel.fill_oval(150,150,15,48, color = 'black')
#right pupil
panel.fill_oval(225,150,15,48, color = 'black')

#nose
panel.fill_polygon(200,250,180,215,225,215, 'pink')

#left 3 whiskers
panel.draw_line(140, 230, 80, 230, color='white')  # Left upper whisker
panel.draw_line(140, 240, 80, 260, color='white')  # Left middle whisker
panel.draw_line(140, 250, 80, 290, color='white')  # Left lower whiske

#right 3 whiskers
panel.draw_line(220, 230, 310, 230, color='white')  # Right upper whisker
panel.draw_line(220, 240, 310, 260, color='white')  # Right middle whisker
panel.draw_line(220, 250, 310, 290, color='white')  # Right lower whisker
