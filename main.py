from tkinter import Tk, Canvas
import time

class Car:
    def __init__(self, brand, model, color, canvas, positionX, positionY):
        self.brandname = brand
        self.modelname = model
        self.colorname = color

        self.canvas = canvas
        self.car_rectangle = self.canvas.create_rectangle(positionX,  positionY, positionX+50,  positionY+50, fill=color)

    def __str__(self):
        return self.brandname + " " + self.modelname + " is op positie: " + positionX + "," + positionY

    def Name(self):
        return self.brandname + " " + self.modelname

    def Move(self,x,y):
        self.canvas.move(self.car_rectangle,x,y)




if __name__ == '__main__':
    root = Tk()

    #achtergrond
    canvas = Canvas(root, width=800, height=800, bg='black')
    canvas.pack()

    #gras
    canvas.create_rectangle(0  ,0  ,200,200, fill='green')      #lb
    canvas.create_rectangle(600,0  ,800,200, fill='green')      #rb
    canvas.create_rectangle(0  ,600,200,800, fill='green')      #lo
    canvas.create_rectangle(600,600,800,800, fill='green')      #ro

    #strepen
    canvas.create_line(400, 0, 400, 800, fill='white', dash=(20, 20))  # vertikaal
    canvas.create_line(0, 400, 800, 400, fill='white', dash=(20, 20))  # horizontaal



    car = Car('Fiat','Punto', 'blue', canvas, 0,500)


    for i in range(75):
        canvas.update()
        time.sleep(0.05)
        car.Move(10,0)


    root.mainloop()