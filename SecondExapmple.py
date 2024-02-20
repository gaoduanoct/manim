from manim import *
'''
class SecondExapmple(Scene):                     
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color = RED)
        area = ax.get_area(curve, x_range=(-2,2))
        
        self.add(ax)
        self.wait(1)
        self.add(curve)
        self.wait(1)
        self.add(area)
        self.wait(1)     
        

        self.play(Create(ax), Create(curve), run_time=3)
        self.play(FadeIn(area))
        self.wait(2)
 '''   
class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle))
        self.wait(1)
        self.play(FadeOut(blue_circle))