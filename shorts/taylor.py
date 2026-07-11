## program objective: to animate the scene for e power x = 1 + x + x square /2 and so on ... 
# Animation detial : so at first the title should be in blue and sholud move up then formula should move down the title and then finally we draw e power x in gold and then label it e p ower x and lastly draw approximation and label it .


from manim import * 
import math

class Taylor(Scene):
    def construct(self):
        head = Text("Taylor Series",color = BLUE_C).to_edge(UP)
        self.play(Write(head))
        self.wait(0.7)

        formula = MathTex(r"e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + \cdots", color = GOLD)
        formula.next_to(head, DOWN, buff = 0.2)

        self.play(Write(formula))
        self.wait(0.8)

        axes = Axes(x_range  = [-3,3,1], y_range = [0,8,1]).scale(0.7)
        axes.next_to(formula, DOWN, buff = 1)
        self.play(Create(axes))

        xlab = MathTex("x").next_to(axes.x_axis.get_end(),  RIGHT, buff=0.1)
        ylab = MathTex("y").next_to(axes.y_axis.get_end(), UP + 0.1 * LEFT, buff=0.1)

        self.play(Write(xlab), Write(ylab))

        exp_graph = axes.plot(lambda x: np.exp(x), x_range=[-2,2], color = GOLD, stroke_width = 6)
        exp_label = MathTex("e^x", color = GOLD).next_to(exp_graph.get_end(), RIGHT + UP, buff=0.1)

        self.play(Create(exp_graph))
        self.play(Write(exp_label))

        approximations = [
            MathTex(r"1", color=BLUE),
            MathTex(r"1 + x", color=BLUE),
            MathTex(r"1 + x + \frac{x^2}{2!}", color=BLUE),
            MathTex(r"1 + x + \frac{x^2}{2!} + \frac{x^3}{3!}", color=BLUE),
            MathTex(r"1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!}", color=BLUE),
            MathTex(r"1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!}", color=BLUE),
        ]

        scales = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
        
        current_graph = axes.plot(lambda x: 1, x_range=[-2,2], color=BLUE, stroke_width=3)
        current_label = approximations[0].scale(scales[0]).next_to(current_graph.get_end(), RIGHT + UP, buff=0.1)
        
        self.play(Create(current_graph), Write(current_label))
        self.wait(1)
        
        for i in range(1, 6):
            func = lambda x, n=i: sum([x**j / math.factorial(j) for j in range(n+1)])
            new_graph = axes.plot(func, x_range=[-2,2], color=BLUE, stroke_width=3)
            new_label = approximations[i].scale(scales[i])
            if i >= 4:
                new_label.next_to(new_graph.get_end(), DOWN + RIGHT, buff=0.1)
            else:
                new_label.next_to(new_graph.get_end(), RIGHT + UP, buff=0.1)
            self.play(Transform(current_label, new_label), Transform(current_graph, new_graph))
            self.wait(1)
