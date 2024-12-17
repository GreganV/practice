
import DrawingPanel

panel = DrawingPanel.DrawingPanel(300,400)
#(0,0) is in upper left

for i in range(10):
    panel.draw_rect(10,(10+(i*10)),(110-(i*10)),10)

for i in range(5):
    panel.draw_oval(100-(8*i),100-(8*i),50*i,50*i)

panel.fill_rect(95,95, 85,160, color = 'black')
panel.fill_rect(100,100,75,150,color = 'blue')

panel.draw_polygon(250,200,200,100,175,175)
