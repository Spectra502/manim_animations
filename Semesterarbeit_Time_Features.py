""" 
* @author Ricardo Merlos Torres
 * @email [contact@ricardomerlostorres.com]
 * @create date 2024-10-03 11:43:36
 * @modify date 2024-10-04 09:42:46
 * @desc [Time Features Animations for Research Project]
"""
 
from manim import *
import numpy as np

class TimeFeaturesText(Scene):
    def construct(self):
        self.wait(3)
        initial_text = Text("Time Features")

        initial_text.move_to(ORIGIN)

        self.play(Write(initial_text), run_time=2)
        self.wait(2)

class BulletListTimeFeatures(Scene):
    def construct(self):
        bulletList = BulletedList(
            "Mean",
            "Root Mean Square",
            "Standard Deviation",
            "Skewness",
            "Kurtosis",
            "Peak To Peak",
            "Crest Factor",
            "Clearance Factor",
            "Shape Factor",
            "Energy Value",
            "Entropy Value"
        )

        bulletList.scale(0.5)
        bulletList.move_to(ORIGIN)

        for item in bulletList:
            self.play(Write(item), run_time=1)
            self.wait(0.5)
        self.wait(2)


class TextAndBulletListTimeFeatures(Scene):
    def construct(self):
        # Add a grid to visualize the coordinate system (Optional)
        grid = NumberPlane()
        self.add(grid)
        self.i = 0
        # Step-by-step modular animation
        self.show_centered_text()
        self.show_bullet_list()
        self.move_first_bullet_to_top_left()
        self.explainMean()
        self.i = self.i + 1
        #self.new_bullet_top_left()
        self.explainRMS()

    def show_centered_text(self):
        # Create and display the centered text
        self.centered_text = Text("Time Features", font_size=48)
        self.centered_text.move_to(ORIGIN)  # Ensure it's centered

        # Display the centered text
        self.play(Write(self.centered_text))
        self.wait(1)

        # Move the text to the top-left corner (adjusted to avoid cutting off)
        top_left = [-4.9, 3.3, 0]
        self.play(self.centered_text.animate.move_to(top_left))
        self.wait(1)

    def show_bullet_list(self):
        # Create two lists for the columns
        self.left_column_items = [
            "Mean",
            "Root Mean Square",
            "Standard Deviation",
            "Skewness",
            "Kurtosis"
        ]

        self.right_column_items = [
            "Peak To Peak",
            "Crest Factor",
            "Clearance Factor",
            "Shape Factor",
            "Energy Value",
            "Entropy Value"
        ]

        # Create the left and right columns
        self.left_column = BulletedList(*self.left_column_items, font_size=38)
        self.right_column = BulletedList(*self.right_column_items, font_size=38)

        # Move the columns to their respective positions
        self.left_column.move_to([-2.5, 0, 0])  # Left column
        self.right_column.move_to([2.5, 0, 0])  # Right column

        # Animate each item in the left column
        for item in self.left_column:
            self.play(Write(item), run_time=0.7)

        # Animate each item in the right column
        for item in self.right_column:
            self.play(Write(item), run_time=0.7)

        self.wait(1)

    def move_first_bullet_to_top_left(self):
        # Keep only the first item from the left column, fade out the rest
        self.play(FadeOut(self.left_column[1:], self.right_column))
        self.wait(0.5)

        # Move the first bullet point from the left column to the top-left, under the main text
        first_item_position = [-5.5, 2.2, 0]  # Slightly lower than the main text
        self.play(self.left_column[0].animate.move_to(first_item_position).scale(1.5))

        # Keep the final scene for a moment
        self.wait(2)
    
    def new_bullet_top_left(self):
        # Keep only the first item from the left column, fade out the rest
        self.play(FadeOut(self.left_column[self.i - 1]))
        self.wait(0.5)

        # Move the first bullet point from the left column to the top-left, under the main text
        first_item_position = [-5.5, 2.2, 0]  # Slightly lower than the main text
        self.play(self.left_column[self.i].move_to(first_item_position).scale(1.5))

        # Keep the final scene for a moment
        self.wait(2)

    def explainMean(self):
        self.mean_equation = MathTex(r"\mu = \frac{1}{N} \sum_{i=1}^{N} A_i")
        self.mean_explanation = Text("The mean value represents the constant or non-varying part of the signal.\n ", font_size=24)

        self.paragraph1 = Text("The mean value represents the constant or non-varying part of the signal.\n", font_size=24)
        self.paragraph2 = Text(
                                "The window size used to compute the mean of a signal significantly affects the result.\n"
                                "A short window may not capture enough of the signal's behavior, and a long window\n"
                                "may smooth out fluctuations that are important for fault detection.", 
                                font_size=24,
                                color=YELLOW
                            )

        self.mean_equation.move_to(ORIGIN)
        self.play(Write(self.mean_equation), run_time=2)
        self.wait(2)
        self.play(self.mean_equation.animate.move_to(UP*2))
        self.paragraph1.next_to(self.mean_equation, DOWN, buff=0.5)
        self.paragraph2.next_to(self.mean_equation, DOWN*3, buff=0.5)
        self.play(Write(self.paragraph1), run_time=2)
        self.play(Write(self.paragraph2), run_time=3)
        self.wait(5)

    def explainRMS(self):
        self.play(FadeOut(self.left_column[0]), Write(self.left_column[1]))
        self.mean_equation = MathTex(r"\mu = \frac{1}{N} \sum_{i=1}^{N} A_i")
        self.mean_explanation = Text("The mean value represents the constant or non-varying part of the signal.\n ", font_size=24)

        self.paragraph1 = Text("The mean value represents the constant or non-varying part of the signal.\n", font_size=24)
        self.paragraph2 = Text(
                                "The window size used to compute the mean of a signal significantly affects the result.\n"
                                "A short window may not capture enough of the signal's behavior, and a long window\n"
                                "may smooth out fluctuations that are important for fault detection.", 
                                font_size=24,
                                color=YELLOW
                            )

        self.mean_equation.move_to(ORIGIN)
        self.play(Write(self.mean_equation), run_time=2)
        self.wait(2)
        self.play(self.mean_equation.animate.move_to(UP*2))
        self.paragraph1.next_to(self.mean_equation, DOWN, buff=0.5)
        self.paragraph2.next_to(self.mean_equation, DOWN*3, buff=0.5)
        self.play(Write(self.paragraph1), run_time=2)
        self.play(Write(self.paragraph2), run_time=3)
        self.wait(5)

        

class MeanVisualization(Scene):
    def construct(self):
        # Step 1: Create axes for the plot
        axes = Axes(
            x_range=[0, 10, 1],  # x-axis range from 0 to 10 with ticks every 1
            y_range=[-1.5, 1.5, 0.5],  # y-axis range from -1.5 to 1.5 with ticks every 0.5
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x) = sin(x)")

        # Step 2: Define the sine function and plot it
        sine_curve = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 10])

        # Step 3: Highlight a specific segment of the sine function (for example, from x=2 to x=6)
        segment_start = 2
        segment_end = 4.24
        segment_curve = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[segment_start, segment_end])

        # Step 4: Calculate the mean value of the segment
        mean_value = (1 / (segment_end - segment_start)) * sum([np.sin(x) for x in np.linspace(segment_start, segment_end, 100)])
        #print(mean_value)

        # Step 5: Create a line at the mean value and display the mean as text
        mean_line = axes.get_horizontal_line(axes.c2p(10, mean_value), line_config={"color": BLUE, "stroke_width": 2})
        mean_text = MathTex(r"\text{Mean} = " + f"{mean_value:.2f}").next_to(mean_line, UP)

        # Step 6: Animate the sine curve and the mean line
        self.play(Create(axes), Write(labels))
        self.play(Create(sine_curve), run_time=2)
        self.play(Create(segment_curve), run_time=2)
        self.wait(1)

        # Step 7: Show the mean line and text with animation
        self.play(Create(mean_line), run_time=2)
        self.play(Write(mean_text))

        # Keep the final scene for a moment
        self.wait(2)
        
class RMSVisualization(Scene):
    def construct(self):
        #grid = NumberPlane()
        #self.add(grid)

        # Step 1: Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x) = sin(x)")

        # Step 2: Plot the sine wave
        sine_curve = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 10])
        sine_label = axes.get_graph_label(sine_curve, label="f(x)", x_val=1.6, buff=1)

        # Step 3: Plot the squared sine wave
        squared_curve = axes.plot(lambda x: np.sin(x)**2, color=YELLOW, x_range=[0, 10])
        squared_label = axes.get_graph_label(squared_curve, label="f(x)^2", x_val=1.6, buff=1)

        # Step 4: Calculate the RMS value (for the full sine wave cycle)
        rms_value = np.sqrt(np.mean([np.sin(x)**2 for x in np.linspace(0, 10, 100)]))
        rms_line = axes.get_horizontal_line(axes.c2p(10, rms_value), line_config={"color": RED, "stroke_width": 2})
        rms_text = MathTex(r"\text{RMS} = " + f"{rms_value:.2f}").next_to(rms_line, UP*3.5)

        # Step 5: Animations
        self.play(Create(axes), Write(labels))

        # Step 6: Show the sine wave
        self.play(Create(sine_curve), Write(sine_label), run_time=2)
        self.wait(1)

        # Step 7: Show the squared sine wave
        self.play(Transform(sine_curve, squared_curve), Transform(sine_label, squared_label), run_time=2)
        self.wait(1)

        # Step 8: Show the RMS value
        self.play(Create(rms_line), Write(rms_text))
        self.wait(2)

        # Keep the final result for a moment
        self.wait(2)

class SkewnessVisualization(Scene):
    def construct(self):
        #grid = NumberPlane()
        #self.add(grid)

        # Step 1: Create axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1, 0.2],
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Step 2: Define three probability density functions (PDFs) to demonstrate skewness
        # Symmetric distribution (Normal)
        symmetric_curve = axes.plot(lambda x: np.exp(-x**2), x_range=[-3, 3], color=BLUE)
        #symmetric_label_function = axes.get_graph_label(symmetric_curve, label="f(x) = x^2", x_val=0, buff=2)
        symmetric_label = Tex("Symmetric (Skew=0)", color=BLUE)
        symmetric_label.move_to([-4,3,0])

        # Positively skewed distribution
        positive_skew_curve = axes.plot(lambda x: np.exp(-x) if x >= 0 else 0, color=GREEN, x_range=[0, 3])
        symmetric_curve_positive = axes.plot(lambda x: np.exp(-x**2), color=BLUE, x_range=[-3, 0])
        #positive_skew_label_function = axes.get_graph_label(positive_skew_curve, label="f(x)", x_val=0, buff=2)
        positive_skew_label = Tex(r"Positive Skew (\textgreater 0)", color=GREEN)
        positive_skew_label.move_to([-4,3,0])

        # Negatively skewed distribution
        negative_skew_curve = axes.plot(lambda x: np.exp(x) if x <= 0 else 0, color=RED, x_range=[-3, 0])
        symmetric_curve_negative = axes.plot(lambda x: np.exp(-x**2), color=BLUE, x_range=[0, 3])
        #negative_skew_label = axes.get_graph_label(negative_skew_curve, label="Negative Skew (< 0)", x_val=-2)
        negative_skew_label = Tex(r"Negative Skew (\textless 0)", color=RED)
        negative_skew_label.move_to([-4,3,0])

        # Step 3: Animations
        self.play(Create(axes), Write(labels))

        # Animate symmetric curve
        self.play(Create(symmetric_curve), Write(symmetric_label), run_time=2)
        self.wait(1)
        self.play(FadeOut(symmetric_label, symmetric_curve))

        # Animate positively skewed curve
        self.play(Create(symmetric_curve_positive), Create(positive_skew_curve), Write(positive_skew_label), run_time=2)
        self.wait(1)
        self.play(FadeOut(positive_skew_curve, symmetric_curve_positive, positive_skew_label))

        # Animate negatively skewed curve
        self.play(Create(negative_skew_curve), Create(symmetric_curve_negative), Write(negative_skew_label), run_time=2)
        self.wait(2)

        # Keep the final scene for a moment
        self.wait(2)

class KurtosisVisualization(Scene):
    def construct(self):
        #grid = NumberPlane()
        #self.add(grid)

        # Step 1: Create axes for the distributions
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 1, 0.2],
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Step 2: Define the three distributions with different kurtosis
        # Mesokurtic (Normal Distribution)
        mesokurtic_curve = axes.plot(lambda x: np.exp(-x**2), color=BLUE, x_range=[-4, 4])
        #mesokurtic_label = Tex("Mesokurtic (Normal)").next_to(axes, LEFT*0.5)
        mesokurtic_label = axes.get_graph_label(mesokurtic_curve, label="Mesokurtic (Normal)", x_val=0.3, buff=2)
        dashed_mesokurtic_curve = DashedVMobject(mesokurtic_curve, num_dashes=20)

        # Leptokurtic (Heavy Tails)
        leptokurtic_curve = axes.plot(lambda x: np.exp(-0.5 * x**2), color=GREEN, x_range=[-4, 4])
        #leptokurtic_label = Tex("Leptokurtic (Heavy Tails)").next_to(axes, LEFT*0.5)
        leptokurtic_label = axes.get_graph_label(leptokurtic_curve, label="Leptokurtic (Heavy Tails)", x_val=0.5, buff=2)

        # Platykurtic (Light Tails)
        platykurtic_curve = axes.plot(lambda x: np.exp(-x**4), color=RED, x_range=[-4, 4])
        #platykurtic_label = Tex("Platykurtic (Light Tails)").next_to(axes, LEFT*0.5)
        platykurtic_label = axes.get_graph_label(platykurtic_curve, label="Platykurtic (Light Tails)", x_val=0.5, buff=2)

        # Step 3: Animations
        self.play(Create(axes), Write(labels))

        # Animate Mesokurtic (Normal) curve
        self.play(Create(mesokurtic_curve), Write(mesokurtic_label), run_time=2)
        self.play(Write(dashed_mesokurtic_curve))
        self.wait(1)
        self.play(FadeOut(mesokurtic_label, mesokurtic_curve))

        # Animate Leptokurtic curve (Heavy Tails)
        self.play(Create(leptokurtic_curve), Write(leptokurtic_label), run_time=2)
        self.wait(1)
        self.play(FadeOut(leptokurtic_curve, leptokurtic_label))

        # Animate Platykurtic curve (Light Tails)
        self.play(Create(platykurtic_curve), Write(platykurtic_label), run_time=2)
        self.wait(2)

        # Keep the final scene for a moment
        self.wait(2)