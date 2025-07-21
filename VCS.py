
"""
Video Comprehension Score 1.1 (VAD 1.1) Animation

This Manim animation visualizes the Video Comprehension Score (VCS) algorithm for comprehensive
video analysis, demonstrating how multiple alignment scores are integrated to compute an overall
video comprehension metric through sophisticated mathematical operations.

The animation demonstrates:
1. Multi-dimensional scoring system with SAS, CAS, and NAS components
2. Scale validation through mathematical constraint checking
3. Scaled SAS calculation with dynamic fraction representation
4. Narrative alignment score computation with detailed mathematical steps
5. Comprehensive VCS integration formula with weighted components
6. Dynamic mathematical transformations and constraint visualizations
7. Advanced visual effects including gradient coloring and animated calculations

Author: Mehul Deep
Date: 07/15/2025
Framework: Manim Community v0.19.0

Usage:
    python -m manim -pql --disable_caching VCS.py FullConceptAnimation
"""

from manim import (  # type: ignore
    # Core scene and animation classes
    Scene, Text, Underline, Create, Write, VGroup,
    
    # Geometric objects
    Line, Triangle, Rectangle, Arrow, Brace, Polygon,
    
    # Mathematical and text objects
    MathTex, Tex,
    
    # Animation functions
    GrowArrow, FadeIn, FadeOut, Transform,
    
    # Colors
    GREEN, RED, BLUE, YELLOW, WHITE, GREY, BLACK, ORANGE, GOLD,
    BLUE_D, TEAL_E, BLUE_A, RED_A, ITALIC,
    
    # Positioning and constants
    ORIGIN, UP, LEFT, RIGHT, DOWN, PI,
    
    # Animation utilities
    always_redraw, ValueTracker
)

class FullConceptAnimation(Scene):
    """
    Main animation class for visualizing the Video Comprehension Score (VCS) algorithm.
    
    This animation demonstrates the complete video comprehension scoring process including
    multiple alignment metrics integration, scale validation, mathematical constraint
    checking, and final score computation with sophisticated visual representations.
    """
    def construct(self):
        """Main animation sequence orchestrating all VCS visualization components."""
        
        # ================== ARROW STYLING CONFIGURATION ==================
        # Define consistent arrow styling for visual flow indicators
        ARROW_STYLE = dict(color=None, stroke_color=YELLOW, stroke_width=4, fill_opacity=0)

        def create_l_arrow(start, end, x_offset=0, stroke_color=YELLOW, stroke_width=4):
            """
            Creates an L-shaped arrow for connecting non-aligned components.
            
            Args:
                start: Starting point of the arrow
                end: Ending point of the arrow
                x_offset: Horizontal offset for the corner point
                stroke_color: Color of the arrow lines
                stroke_width: Width of the arrow lines
            
            Returns:
                VGroup containing the L-shaped arrow components
            """
            if x_offset == 0:
                x_offset = end[0]
            mid = [x_offset, start[1], 0]
            line1 = Line(start, mid).set_stroke(color=stroke_color, width=stroke_width)
            line2 = Line(mid, end).set_stroke(color=stroke_color, width=stroke_width)

            arrow_tip = Triangle().set_fill(stroke_color, opacity=1).set_stroke(width=0).scale(0.15)
            angle_of_line2 = line2.get_angle()
            arrow_tip.set_angle(angle_of_line2)
            arrow_tip.move_to(end)
            arrow_tip.shift(-arrow_tip.height * 0.5 * line2.get_unit_vector())

            return VGroup(line1, line2, arrow_tip)

        # ================== TITLE AND HEADING SETUP ==================
        # Create and animate the main title for Video Comprehension Score
        title = Text("Video Comprehension Score (VCS)", font_size=30).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(0.5)
        
        # Position title at top edge for optimal screen space utilization
        self.play(title.animate.to_edge(UP, buff=0.1))
        self.wait(0.5)
        
        # Add underline for visual emphasis and professional appearance
        underline = Underline(title)
        self.play(Create(underline))
        self.wait(0.5)

        # ================== ALIGNMENT SCORE COMPONENTS ==================
        # Create visual representations for the three main alignment scores
        rect_w, rect_h = 4.1, 0.7  # Standard dimensions for score boxes

        # Semantic Alignment Score (SAS) - measures semantic similarity
        semantic_text = Text("Semantic Alignment Score (SAS)", font_size=16).set_color_by_gradient(RED, BLUE)
        semantic_box = Rectangle(width=rect_w, height=rect_h).set_stroke(width=1, color=WHITE)
        semantic_text.move_to(semantic_box.get_center())
        semantic_group = VGroup(semantic_box, semantic_text)

        # Content Alignment Score (CAS) - measures content accuracy
        content_text = Text("Content Alignment Score (CAS)", font_size=16).set_color_by_gradient(RED, BLUE)
        content_box = Rectangle(width=rect_w, height=rect_h).set_stroke(width=1, color=WHITE)
        content_text.move_to(content_box.get_center())
        content_group = VGroup(content_box, content_text)

        # Narrative Alignment Score (NAS) - measures narrative structure
        narrative_text = Text("Narrative Alignment Score (NAS)", font_size=16).set_color_by_gradient(RED, BLUE)
        narrative_box = Rectangle(width=rect_w, height=rect_h).set_stroke(width=1, color=WHITE)
        narrative_text.move_to(narrative_box.get_center())
        narrative_group = VGroup(narrative_box, narrative_text)

        # Group all alignment score components for layout
        four_scores_group = VGroup(semantic_group, content_group, narrative_group)
        four_scores_group.arrange(DOWN, aligned_edge=LEFT, buff=0.7).to_edge(LEFT)


        # ================== SCALE VALIDATION CONSTRAINT ==================
        # Create mathematical constraint box for scale validation
        scale_text = MathTex(r"SAS - (1 - CAS) > 0", font_size=14)
        scale_rect = Rectangle(width=1.7, height=0.7).move_to(scale_text.get_center())
        scale_rect.set_stroke(width=1, color=WHITE)
        dotted_scale_box = VGroup(scale_rect)
        scale_text.move_to(scale_rect.get_center())
        scale_group = VGroup(dotted_scale_box, scale_text)
        scale_group.next_to(content_group, RIGHT, buff=1)
        scale_group.set_y(semantic_box.get_center()[1])

        # ================== CONSTRAINT FLOW ARROWS ==================
        # Create arrows connecting SAS and CAS to scale validation
        # Direct arrow from SAS to scale constraint
        arrow_sem = Arrow(
            start=semantic_box.get_right(),
            end=dotted_scale_box.get_left(),
            buff=0.1,
            **ARROW_STYLE
        )
        
        # L-shaped arrow from CAS to scale constraint for visual clarity
        arrow_con = create_l_arrow(
            start=content_box.get_right(),
            end=dotted_scale_box.get_bottom() + LEFT*0.2,
            x_offset=(dotted_scale_box.get_bottom()[0] - 0.2),
            stroke_color=YELLOW,
            stroke_width=4
        )

        # ================== SCALED SAS CALCULATION ==================
        # Create scaled semantic alignment score formula
        compare_text_1 = MathTex(
            r"\frac{SAS - (1 - CAS)}{CAS}",
            font_size=23
        )
        compare_text_1.next_to(scale_group, RIGHT, buff=2)
        compare_text_1.set_y(scale_group.get_center()[1])
        compare_text_1.shift(LEFT * 1.0)  # Adjust horizontal position for optimal layout
        # ================== SCALE FAILURE HANDLING ==================
        # Define alternative path when scale validation fails
        scaled_sas_zero_text = Tex("S.SAS=0", font_size=16)
        scaled_sas_zero_text.move_to(scale_group.get_center() + DOWN * 1.5 + RIGHT * 1.86)

        # Create the "or" text to place between the formula and VAD* = 0
        or_text = Tex("or", font_size=28).set_color(WHITE)

        # Position the "or" text vertically between the formula and VAD* = 0
        or_text.move_to([
            compare_text_1.get_center()[0],  # Same x-coordinate as the formula
            (compare_text_1.get_bottom()[1] + scaled_sas_zero_text.get_top()[1])/2,  # Midpoint
            0
        ])

        # Arrow from scale->S.SAS
        arrow_scale_compare = Arrow(
            start=dotted_scale_box.get_right(),
            end=compare_text_1.get_left(),
            buff=0.1,
            tip_length=0.20,
            **ARROW_STYLE
        )

        # 5) Animate boxes
        self.play(
            Create(semantic_box), Write(semantic_text),
            Create(content_box), Write(content_text),
            Create(narrative_box), Write(narrative_text),
            # Create(brevity_box), Write(brevity_text),
            run_time=0.5
        )
        self.wait(0.5)

        # Animate arrows to scale
        self.play(GrowArrow(arrow_sem), Create(arrow_con), run_time=0.5)
        self.wait(0.5)

        # Animate scale box
        self.play(Create(scale_rect), Write(scale_text), run_time=0.5)
        self.wait(0.5)

        # "YES" label
        yes_label = Tex("Yes", font_size=23).set_color(WHITE)
        yes_label.next_to(arrow_scale_compare, UP, buff=0.1)
        self.play(
            GrowArrow(arrow_scale_compare),
            Write(yes_label),
            run_time=0.5
        )
        self.wait(0.5)

        # Show the initial S.SAS text
        self.play(Write(compare_text_1), run_time=0.5)
        self.wait(0.5)
        self.play(Write(or_text), run_time=0.3)
        self.wait(0.3)

        # =========== "Scaled SAS=0" text below scale_group =========== 1.94
        scaled_sas_zero_text = Tex("0", font_size=23)
        scaled_sas_zero_text.next_to(scale_group, DOWN, buff=1)
        scaled_sas_zero_text.shift(DOWN * 0.02 + RIGHT * 2.8)

        # Manual approach with customized triangle tip and shorter horizontal segment
        start_point = scale_rect.get_bottom() + RIGHT*0.3
        mid_point = [start_point[0], scaled_sas_zero_text.get_center()[1], 0]  # Align with vertical center of text

        # Calculate a new end point that's closer to the text (adjust the 0.5 factor to control length)    0.16
        # Higher value = shorter arrow (0.5 means the arrow stops halfway to the text)
        shortened_factor = 0.45  # Adjust this value to control shortening (0.0-1.0)
        text_left = scaled_sas_zero_text.get_left()
        full_width = text_left[0] - mid_point[0]
        shortened_width = full_width * (1 - shortened_factor)
        end_point = [mid_point[0] + shortened_width, mid_point[1], 0]

        # Create the two line segments
        vertical_line = Line(
            start=start_point,
            end=mid_point,
            stroke_color=YELLOW,
            stroke_width=4
        )

        horizontal_line = Line(
            start=mid_point,
            end=end_point,
            stroke_color=YELLOW,
            stroke_width=4
        )

        # Create a completely custom triangle arrow tip with smaller size
        points = [
            [0.1, 0, 0],     # Tip point
            [-0.1, 0.1, 0],  # Top back corner
            [-0.1, -0.1, 0]  # Bottom back corner
        ]
        arrow_tip = Triangle(fill_opacity=1, stroke_width=0).set_points_as_corners(points)
        arrow_tip.set_fill(YELLOW)
        arrow_tip.scale(1.0)  # Reduced from 1.5 to 1.0 for smaller arrow head

        # Position exactly at the end of the horizontal line
        arrow_tip.move_to(end_point)

        # Group the arrow components
        arrow_sas_down = VGroup(vertical_line, horizontal_line, arrow_tip)

        # "No" label near the vertical segment
        no_label = Tex("No", font_size=23).set_color(WHITE)
        no_label.next_to(vertical_line, RIGHT, buff=0.1)

        self.play(Create(arrow_sas_down), Write(no_label), run_time=0.5)
        self.wait(0.5)

        self.play(Write(scaled_sas_zero_text), run_time=0.5)
        self.wait(0.5)

        # ================== SCALED SAS RESULT GROUPING ==================
        # Create curly brace to group scaled SAS results
        brace = Brace(VGroup(compare_text_1, scaled_sas_zero_text), direction=RIGHT)
        brace.shift(RIGHT * -0.08)
        brace.set_stroke(width=1.4) 
        self.play(Create(brace), run_time=0.5)
        self.wait(0.5)

        # ================== SCALED SAS SUMMARY BOX ==================
        # Create summary box displaying scaled SAS results
        new_box_text = MathTex(r"Scaled.SAS", font_size=22)
        new_box_rect = Rectangle(width=1.82, height=0.7).move_to(new_box_text.get_center())
        new_box_rect.set_stroke(width=1, color=WHITE)
        new_box_group = VGroup(new_box_rect, new_box_text)
        new_box_group.next_to(brace, RIGHT, buff=1.0)
        new_box_group.set_y(scaled_sas_zero_text.get_center()[1])
        new_box_group.shift(UP * 0.79)

        # Arrow from the curly brace to the new box
        arrow_brace_to_new = Arrow(
            start=brace.get_right(),
            end=new_box_rect.get_left(),
            buff=0.1,
            tip_length=0.20,
            **ARROW_STYLE
        )
        self.play(GrowArrow(arrow_brace_to_new), run_time=0.5)
        self.wait(0.5)

        self.play(Write(new_box_text), run_time=0.5)
        self.wait(0.5)

        # Group arrows for final transform
        arrow_scale_label_group = VGroup(
            arrow_scale_compare,
            arrow_sas_down,
            arrow_brace_to_new
        )

        # Group everything except the heading
        scene_except_title_no_arrow = VGroup(
            semantic_group, content_group, narrative_group, 
            scale_group, compare_text_1, scaled_sas_zero_text, new_box_group,
            arrow_sem, arrow_con, arrow_scale_label_group, yes_label, no_label, brace, or_text
        )

        # Final scale-down 0.65
        scene_except_title = VGroup(scene_except_title_no_arrow)
        self.play(scene_except_title.animate.scale(0.68).to_edge(LEFT, buff=0.26).shift(UP*1.5), run_time=0.5)
        self.wait(1.0)

        # 1. Create the new S-SAS <= NAS box
        ssas_nas_text = MathTex(r"S.SAS <= NAS", font_size=13)
        ssas_nas_box = Rectangle(width=1.21, height=0.455).set_stroke(width=1, color=WHITE)
        ssas_nas_text.move_to(ssas_nas_box.get_center())
        ssas_nas_group = VGroup(ssas_nas_box, ssas_nas_text)

        # Get the y-coordinate of the narrative box in the scaled scene to align horizontally
        scaled_narrative_box = narrative_group[0]  # Access the Rectangle part
        narrative_y_position = scaled_narrative_box.get_center()[1]  # Get y-coordinate

        # Position this box at the same height as the Narrative box
        ssas_nas_group.next_to(scaled_narrative_box, RIGHT, buff=0.64)
        ssas_nas_group.set_y(narrative_y_position)  # Force the same y-coordinate

        # 2. Create arrow from Narrative Alignment Score (NAS) box going right
        # Use the same approach as the original arrow for consistency
        arrow_nas_to_new = Arrow(
            start=scaled_narrative_box.get_right(),
            end=ssas_nas_box.get_left(),
            buff=0.05,
            stroke_color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,  # Control arrow tip size
            max_stroke_width_to_length_ratio=9.0  # Ensure consistent stroke width
        )

        # 3. Create complex arrow from S.SAS=(0.82 or 0) box with ORIGINAL thickness
        # First, find the S.SAS box in the scaled scene
        scaled_new_box = new_box_group[0]  # Access the Rectangle part

        # REWORKED PATH CALCULATION but with original thickness
        # Start at the bottom center of the S.SAS box
        start_point = scaled_new_box.get_bottom()
        # Find the target on top of the S-SAS <= NAS box
        target_point = ssas_nas_box.get_top() + UP * 0.06

        # Calculate midpoints for three-segment path
        mid_point1 = start_point + DOWN * 0.55  # Go down
        mid_point2 = [target_point[0], mid_point1[1], 0]  # Go horizontally to align with target x-coordinate

        # Create the line segments - USING ORIGINAL thickness of 4
        line1 = Line(start_point, mid_point1, stroke_color=YELLOW, stroke_width=4)
        line2 = Line(mid_point1, mid_point2, stroke_color=YELLOW, stroke_width=4)
        line3 = Line(mid_point2, target_point, stroke_color=YELLOW, stroke_width=4)

        # Create a completely custom triangle arrow tip with proper downward orientation
        arrow_tip = Triangle(fill_opacity=1, stroke_width=0)
        arrow_tip.set_fill(YELLOW)
        arrow_tip.scale(0.15)

        # IMPORTANT: Using specific points to ensure correct orientation
        points = [
            [0, -0.1, 0],    # Bottom point (tip points down)
            [-0.1, 0.1, 0],  # Top left corner
            [0.1, 0.1, 0]    # Top right corner
        ]
        arrow_tip.set_points_as_corners(points)

        # Position at the end of the vertical line
        arrow_tip.move_to(target_point)

        # Slight adjustment to connect with the line
        arrow_tip.shift(UP * 0.06)

        # Group all line segments and arrow tip
        complex_arrow = VGroup(line1, line2, line3, arrow_tip)

       # Calculate where the box will be for arrow positioning
        box_position = ssas_nas_box.get_center()

        # First animate both arrows together
        # The horizontal arrow from NAS box
        self.play(
            GrowArrow(arrow_nas_to_new),
            run_time=0.5
        )
        self.wait(0.2)

        # Animate the complex arrow from S.SAS=(0.82 or 0) all at once
        self.play(
            Create(VGroup(line1, line2, line3, arrow_tip)),
            run_time=0.6
        )
        self.wait(0.5)

        # Then show the S-SAS <= NAS box
        self.play(Create(ssas_nas_box), Write(ssas_nas_text), run_time=0.5)
        self.wait(0.8)

        # ================== NARRATIVE CONSTRAINT VALIDATION ==================
        # Create constraint validation box for narrative alignment
        ssas_nas_test_text = MathTex(r"S.SAS - (1 - NAS)>0", font_size=12)
        ssas_nas_test_box = Rectangle(width=1.5, height=0.455).set_stroke(width=1, color=WHITE)
        ssas_nas_test_text.move_to(ssas_nas_test_box.get_center())
        ssas_nas_test_group = VGroup(ssas_nas_test_box, ssas_nas_test_text)

        # Position the new box to the right of S-SAS <= NAS box
        ssas_nas_test_group.next_to(ssas_nas_box, RIGHT, buff=0.64)

        # Create a placeholder for where the box will be - just a position to point the arrow to
        box_position = ssas_nas_test_box.get_left()

        # Create arrow from S-SAS <= NAS to where the new box will be
        arrow_ssas_to_test = Arrow(
            start=ssas_nas_box.get_right(),
            end=box_position,
            buff=0.05,
            color=YELLOW,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=9.0
        )

        # Create the "Yes" label - THIS IS THE LINE THAT CAUSED THE ERROR
        # FIXED: Changed from Text to Tex
        test_label = Tex("Yes", font_size=15).set_color(WHITE)
        arrow_center = arrow_ssas_to_test.get_center()
        test_label.move_to(arrow_center).shift(UP * 0.20)

        # First animate the arrow
        self.play(GrowArrow(arrow_ssas_to_test), run_time=0.5)
        self.wait(0.3)

        # Then animate the "Yes" label
        self.play(Write(test_label), run_time=0.3)
        self.wait(0.3)

        # Finally animate the box appearing
        self.play(Create(ssas_nas_test_box), Write(ssas_nas_test_text), run_time=0.5)
        self.wait(1.0)

        # First, define both the formula and the VAD* = 0 text (but don't animate yet)
        ssas_formula = MathTex(
            r"\frac{S.SAS - (1 - NAS)}{NAS}",
            font_size=16
        )
        ssas_formula.next_to(ssas_nas_test_box, RIGHT, buff=0.64)

        # Define the VAD* = 0 text (but don't animate yet)
        vad_zero_text = MathTex(r"VAD^* = 0", font_size=19)
        vad_zero_text.move_to(ssas_nas_test_box.get_center() + DOWN * 0.95 + RIGHT * 1.86)

        # Create the "or" text to place between the formula and VAD* = 0
        or_text = Tex("or", font_size=19).set_color(WHITE)

        # Position the "or" text vertically between the formula and VAD* = 0
        or_text.move_to([
            ssas_formula.get_center()[0],  # Same x-coordinate as the formula
            (ssas_formula.get_bottom()[1] + vad_zero_text.get_top()[1])/2,  # Midpoint
            0
        ])

        # Using the same arrow style as before for consistency
        arrow_to_formula = Arrow(
            start=ssas_nas_test_box.get_right(),
            end=ssas_formula.get_left(),
            buff=0.05,
            color=YELLOW,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=8.5
        )

        # Create the "Yes" label
        formula_yes_label = Tex("Yes", font_size=15).set_color(WHITE)
        arrow_formula_center = arrow_to_formula.get_center()
        formula_yes_label.move_to(arrow_formula_center).shift(UP * 0.20)

        # First animate the arrow
        self.play(GrowArrow(arrow_to_formula), run_time=0.5)
        self.wait(0.3)

        # Then animate the "Yes" label
        self.play(Write(formula_yes_label), run_time=0.3)
        self.wait(0.3)

        # Finally animate the formula appearing
        self.play(Write(ssas_formula), run_time=0.5)
        self.wait(1.0)
        self.play(Write(or_text), run_time=0.3)
        self.wait(0.3)

        # Create the "VAD = 0" text (without box)
        vad_zero_text = Tex("0", font_size=17)

        # Position the text below and to the right of the S-SAS-(1-NAS)>0 box with EXTRA gap
        vad_zero_text.move_to(ssas_nas_test_box.get_center() + DOWN * 0.95 + RIGHT * 2.15)  # Increased RIGHT shift

        # Create the L-shaped arrow from the bottom of the S-SAS-(1-NAS)>0 box to the VAD = 0 box
        start_point = ssas_nas_test_box.get_bottom()

        # Calculate where the arrow should end, with a gap before the text
        text_left = vad_zero_text.get_left()
        mid_point = [start_point[0], text_left[1], 0]  # Same x as start, same y as text

        # Calculate shortened arrow endpoint with gap (similar to your working example)
        shortened_factor = 0.44  # Match your working example's factor
        full_width = text_left[0] - mid_point[0]
        shortened_width = full_width * (1 - shortened_factor)
        end_point = [mid_point[0] + shortened_width, mid_point[1], 0]

        # Create the line segments with original thickness
        line1 = Line(start_point, mid_point, stroke_color=YELLOW, stroke_width=4)
        line2 = Line(mid_point, end_point, stroke_color=YELLOW, stroke_width=4)

        # Create an arrow head using the default Triangle
        triangle = Triangle(fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        # Size the triangle to match screenshot
        triangle.scale(0.10)

        # Rotate and position the triangle to point right
        triangle.rotate(-PI/2)  # Rotate 90 degrees clockwise
        triangle.next_to(line2, RIGHT, buff=0)  # Position it right after the line

        # Group the arrow components
        l_arrow_to_vad = VGroup(line1, line2, triangle)

        # Create the "No" label for the arrow
        no_label = Tex("No", font_size=15).set_color(WHITE)
        no_label.next_to(line1, RIGHT, buff=0.1)

        # Animate the L-shaped arrow
        self.play(Create(l_arrow_to_vad), Write(no_label), run_time=0.5)
        self.wait(0.5)

        # Animate the VAD = 0 text
        self.play(Write(vad_zero_text), run_time=0.5)
        self.wait(1.0)

        # Create a vertical brace that wraps S.NAS = 0.77 and VAD = 0
        vertical_brace = Brace(
            VGroup(ssas_formula, vad_zero_text),  # Group to wrap with brace
            direction=RIGHT                       # Brace appears on right side
        )

        # Move brace closer to the text
        vertical_brace.shift(LEFT * 0.15)

        vertical_brace.set_stroke(width=0.01)  # Thinner stroke to match earlier braces

        # Create the result box with text
        result_text = MathTex(r"VAD^*", font_size=19)
        result_box = Rectangle(width=1.0, height=0.455).set_stroke(width=1, color=WHITE)
        result_text.move_to(result_box.get_center())
        result_group = VGroup(result_box, result_text)

        # Position result to the right of the brace
        result_group.next_to(vertical_brace, RIGHT*1.3, buff=0.5)

        # Center the result box vertically relative to the brace
        result_group.set_y(vertical_brace.get_center()[1])

        # Animate the brace
        self.play(Create(vertical_brace), run_time=0.5)
        self.wait(0.5)

        arrow_brace_to_result = Arrow(
            start=vertical_brace.get_right(),
            end=result_box.get_left(),
            buff=0.05,
            color=YELLOW,
            stroke_width=8,  # Thicker line to match other arrows
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=9.0
        )

        # Animate the arrow
        self.play(GrowArrow(arrow_brace_to_result), run_time=0.5)
        self.wait(0.5)

        # Animate the result box and text
        self.play(Create(result_box), Write(result_text), run_time=0.7)
        self.wait(1.0)

        # ================== REVERSE NARRATIVE CONSTRAINT ==================
        # Create reverse constraint validation for narrative alignment
        nas_test_text = MathTex(r"NAS - (1 - S.SAS)>0", font_size=12)
        nas_test_box = Rectangle(width=1.5, height=0.455).set_stroke(width=1, color=WHITE)
        nas_test_text.move_to(nas_test_box.get_center())
        nas_test_group = VGroup(nas_test_box, nas_test_text)

        # Position this new box below and to the right of the S-SAS <= NAS box
        nas_test_group.move_to(ssas_nas_box.get_center() + DOWN * 1.5 + RIGHT * 1.99)

        # Create the L-shaped arrow similar to the ones used before
        start_point = ssas_nas_box.get_bottom()
        end_point = nas_test_box.get_left() + LEFT * 0.2

        # Calculate the midpoint for the L-shape
        mid_point = [start_point[0], end_point[1], 0]  # Same x as start, same y as end

        # Create the line segments with original thickness
        line1 = Line(start_point, mid_point, stroke_color=YELLOW, stroke_width=4)
        line2 = Line(mid_point, end_point, stroke_color=YELLOW, stroke_width=4)

        # Create the arrow tip using the same approach as your "VAD = 0" arrow
        triangle = Triangle(fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        triangle.scale(0.10)  # Same size as your other arrow heads
        triangle.rotate(-PI/2)  # Rotate 90 degrees clockwise to point right
        triangle.next_to(line2, RIGHT, buff=0)  # Position at the end of the horizontal line

        # Group the arrow components
        new_l_arrow = VGroup(line1, line2, triangle)

        # Create a label for the arrow
        arrow_label = Tex("No", font_size=15).set_color(WHITE)
        arrow_label.next_to(line1, RIGHT, buff=0.1)

        # Animate the L-shaped arrow
        self.play(Create(new_l_arrow), Write(arrow_label), run_time=0.5)
        self.wait(0.5)

        # Animate the new box appearing
        self.play(Create(nas_test_box), Write(nas_test_text), run_time=0.5)
        self.wait(1.0)

        # ================== NARRATIVE SCALED FORMULA ==================
        # Create scaled narrative formula for final VCS calculation
        nas_formula_1 = MathTex(
            r"\frac{NAS - (1 - S.SAS)}{S.SAS}",
            font_size=16
        )

        # Position to the right of NAS-(1-S.SAS)>0 box (similar to your S.NAS placement)
        nas_formula_1.next_to(nas_test_box, RIGHT*1.0, buff=0.64)
        
        # Create "VAD = 0.77" text below (similar to your VAD = 0)
        vad_value_text = Tex("0", font_size=17)

        # Position below and to the right of the NAS-(1-S.SAS)>0 box
        vad_value_text.move_to(nas_test_box.get_center() + DOWN * 0.95 + RIGHT * 1.9)

        # Create the "or" text to place between the formula and VAD* = 0
        or_text_2 = Tex("or", font_size=19).set_color(WHITE)

        # Position the "or" text vertically between the formula and VAD* = 0
        or_text_2.move_to([
            nas_formula_1.get_center()[0],  # Same x-coordinate as the formula
            (nas_formula_1.get_bottom()[1] + vad_value_text.get_top()[1])/2,  # Midpoint
            0
        ])
        # Using the same arrow style as before for consistency
        arrow_to_nas_formula = Arrow(
            start=nas_test_box.get_right(),
            end=nas_formula_1.get_left(),
            buff=0.05,
            color=YELLOW,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=8.5
        )

        # Create Yes label for the horizontal arrow
        nas_yes_label = Tex("Yes", font_size=15).set_color(WHITE)
        arrow_nas_center = arrow_to_nas_formula.get_center()
        nas_yes_label.move_to(arrow_nas_center).shift(UP * 0.20)

        # Animate the horizontal arrow first
        self.play(GrowArrow(arrow_to_nas_formula), run_time=0.5)
        self.wait(0.3)

        # Then the Yes label
        self.play(Write(nas_yes_label), run_time=0.3)
        self.wait(0.3)

        # Show the initial formula with variables
        self.play(Write(nas_formula_1), run_time=0.5)
        self.wait(0.5)
        self.play(Write(or_text_2), run_time=0.3)
        self.wait(0.3)

        # 2. Create "VAD = 0.77" text below (similar to your VAD = 0)
        vad_value_text = Tex("0", font_size=17)

        # Position below and to the right of the NAS-(1-S.SAS)>0 box WITH EXTRA GAP
        vad_value_text.move_to(nas_test_box.get_center() + DOWN * 0.95 + RIGHT * 2.15)  # Increased RIGHT shift

        # Create the L-shaped arrow from bottom of NAS-(1-S.SAS)>0 to VAD = 0.77
        start_point_vad = nas_test_box.get_bottom()

        # Calculate where the arrow should end, with a gap before the text
        text_left = vad_value_text.get_left()
        mid_point_vad = [start_point_vad[0], text_left[1], 0]  # Same x as start, same y as text

        # Calculate shortened arrow endpoint with gap (similar to your working example)
        shortened_factor = 0.44  # Match your working example's factor
        full_width = text_left[0] - mid_point_vad[0]
        shortened_width = full_width * (1 - shortened_factor)
        end_point_vad = [mid_point_vad[0] + shortened_width, mid_point_vad[1], 0]

        # Create the line segments
        line1_vad = Line(start_point_vad, mid_point_vad, stroke_color=YELLOW, stroke_width=4)
        line2_vad = Line(mid_point_vad, end_point_vad, stroke_color=YELLOW, stroke_width=4)

        # Create arrow head
        triangle_vad = Triangle(fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        triangle_vad.scale(0.10)  # Same size as other arrows
        triangle_vad.rotate(-PI/2)  # Rotate to point right
        triangle_vad.next_to(line2_vad, RIGHT, buff=0)  # Position at end of line

        # Group arrow components
        l_arrow_to_vad_value = VGroup(line1_vad, line2_vad, triangle_vad)

        # Create "No" label
        no_label_vad = Tex("No", font_size=15).set_color(WHITE)
        no_label_vad.next_to(line1_vad, RIGHT, buff=0.1)

        # Animate the L-shaped arrow
        self.play(Create(l_arrow_to_vad_value), Write(no_label_vad), run_time=0.5)
        self.wait(0.5)

        # Animate the VAD = 0.77 text
        self.play(Write(vad_value_text), run_time=0.5)
        self.wait(1.0)

        # 3. Create a vertical brace wrapping both elements
        vertical_brace_nas = Brace(
            VGroup(nas_formula_1, vad_value_text),  # Group to wrap with brace
            direction=RIGHT                       # Brace appears on right side
        )

        # Move brace closer to text
        vertical_brace_nas.shift(LEFT * 0.15)
        vertical_brace_nas.set_stroke(width=0.01)  # Thin stroke to match previous braces

        # Create result box with text "VAD**"
        result_text_nas = MathTex(r"VAD^*", font_size=19)
        result_box_nas = Rectangle(width=1.0, height=0.455).set_stroke(width=1, color=WHITE)
        result_text_nas.move_to(result_box_nas.get_center())
        result_group_nas = VGroup(result_box_nas, result_text_nas)

        # Position to right of brace
        result_group_nas.next_to(vertical_brace_nas, RIGHT*1.32, buff=0.5)
        result_group_nas.set_y(vertical_brace_nas.get_center()[1])  # Center vertically

        # Animate the brace
        self.play(Create(vertical_brace_nas), run_time=0.5)
        self.wait(0.5)

        # Create arrow from brace to result box
        arrow_brace_to_result_nas = Arrow(
            start=vertical_brace_nas.get_right(),
            end=result_box_nas.get_left(),
            buff=0.05,
            color=YELLOW,
            stroke_width=8,  # Thicker line to match other arrows
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=9.0
        )

        # Animate the arrow
        self.play(GrowArrow(arrow_brace_to_result_nas), run_time=0.5)
        self.wait(0.5)
        
        # Create the "or" text to place between the two VAD* boxes
        vad_boxes_or_text = Tex("or", font_size=19).set_color(WHITE)

        # Position the "or" text vertically between the two VAD* boxes
        vad_boxes_or_text.move_to([
            result_group.get_center()[0],  # Same x-coordinate as first VAD* box
            (result_group.get_bottom()[1] + result_group_nas.get_top()[1])/2,  # Midpoint between boxes
            0
        ])

         # Animate the "or" text
        self.play(Write(vad_boxes_or_text), run_time=0.3)
        self.wait(0.3)
        

        # Animate the result box and text
        self.play(Create(result_box_nas), Write(result_text_nas), run_time=0.7)
        self.wait(1.0)

        # ================== FINAL VAD AGGREGATION ==================
        # Create vertical brace that wraps both VAD components
        final_brace = Brace(
            VGroup(result_group, result_group_nas),  # Group containing both VAD* and VAD** boxes
            direction=RIGHT                         # Brace appears on right side
        )

        # Move brace closer to the boxes
        final_brace.shift(LEFT * 0.15)
        final_brace.set_stroke(width=0.8)  # Match the thickness of other braces

        # Create the final VAD box with text
        final_vad_text = MathTex(r"VAD^*", font_size=19)
        final_vad_box = Rectangle(width=1.0, height=0.455).set_stroke(width=1, color=WHITE)
        final_vad_text.move_to(final_vad_box.get_center())
        final_vad_group = VGroup(final_vad_box, final_vad_text)

        # Position final VAD box to the right of the brace
        final_vad_group.next_to(final_brace, RIGHT*1.38, buff=0.5)
        final_vad_group.set_y(final_brace.get_center()[1])  # Center vertically

        # Animate the brace
        self.play(Create(final_brace), run_time=0.5)
        self.wait(0.5)

        # Create arrow from brace to final VAD box
        arrow_final_brace_to_vad = Arrow(
            start=final_brace.get_right(),
            end=final_vad_box.get_left(),
            buff=0.05,
            color=YELLOW,
            stroke_width=8,  # Thicker line to match other arrows
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=9.0
        )

        # Animate the arrow
        self.play(GrowArrow(arrow_final_brace_to_vad), run_time=0.5)
        self.wait(0.5)

        # Animate the final VAD box and text
        self.play(Create(final_vad_box), Write(final_vad_text), run_time=0.7)
        self.wait(1.0)

        # ================== BREVITY PENALTY COMPONENT ==================
        # Create brevity penalty box for length adjustment
        brevity_text = Tex("Brevity Penalty (BP)", font_size=18).set_color_by_gradient(RED, BLUE)
        brevity_box = Rectangle(width=2.66, height=0.5).set_stroke(width=1, color=WHITE)  # Manual width and height
        brevity_text.move_to(brevity_box.get_center())
        brevity_group = VGroup(brevity_box, brevity_text)

        # Position it lower, with more space below the Narrative Alignment Score
        brevity_group.next_to(narrative_group, DOWN, buff=2.82, aligned_edge=LEFT)  # Increased buffer to 1.2

        # Add it to the animation sequence
        self.play(
            Create(brevity_box), 
            Write(brevity_text),
            run_time=0.5
        )
        self.wait(0.5)

        # ================== BREVITY PENALTY CONSTRAINT ==================
        # Create constraint validation for brevity penalty adjustment
        vad_bp_text = MathTex(r"VAD^* - (1-BP) > 0", font_size=14)
        vad_bp_box = Rectangle(width=1.6, height=0.455).set_stroke(width=1, color=WHITE)
        vad_bp_text.move_to(vad_bp_box.get_center())
        vad_bp_group = VGroup(vad_bp_box, vad_bp_text)

        # Position it to the right of the Brevity Penalty box
        vad_bp_group.next_to(brevity_box, RIGHT, buff=4.83)
        vad_bp_group.set_y(brevity_box.get_center()[1])  # Align vertically with Brevity Penalty

        # Create arrow from Brevity Penalty to the new box
        arrow_bp_to_vad = Arrow(
            start=brevity_box.get_right(),
            end=vad_bp_box.get_left(),
            buff=0.1,
            stroke_color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.03,
            max_stroke_width_to_length_ratio=9.0
        )

        # Animate the arrow first
        self.play(GrowArrow(arrow_bp_to_vad), run_time=0.5)
        self.wait(0.5)

        # Then animate the box and text
        self.play(Create(vad_bp_box), Write(vad_bp_text), run_time=0.5)
        self.wait(0.5)

        # Create a complex L-shaped arrow from final VAD box to VAD-(1-BP)>0
        # Starting point: bottom center of final VAD box
        start_point = final_vad_box.get_bottom()

        # Ending point: top center of VAD-(1-BP)>0 box
        end_point = vad_bp_box.get_top()
        end_point = vad_bp_box.get_top() + UP * 0.08

        # Create intermediate points for the complex path (going down, then left, then down)
        mid_point1 = start_point + DOWN * 1.32  # Go straight down
        mid_point2 = [vad_bp_box.get_center()[0], mid_point1[1], 0]  # Go left to align with VAD-(1-BP)>0

        # mid_point3 = mid_point2  # Placeholder for adjustment if needed

        # Create the line segments
        line1 = Line(start_point, mid_point1, stroke_color=YELLOW, stroke_width=4)
        line2 = Line(mid_point1, mid_point2, stroke_color=YELLOW, stroke_width=4)
        line3 = Line(mid_point2, end_point, stroke_color=YELLOW, stroke_width=4)

        # Create arrow tip for the bottom segment
        arrow_tip = Triangle(fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        arrow_tip.scale(0.15)  # Match size of other arrow tips

        # Ensure arrow points down (same technique as earlier)
        points = [
            [0, -0.1, 0],    # Bottom point (tip pointing down)
            [-0.1, 0.1, 0],  # Top left corner
            [0.1, 0.1, 0]    # Top right corner
        ]
        arrow_tip.set_points_as_corners(points)

        # Position at end of vertical line
        arrow_tip.move_to(end_point)
        arrow_tip.shift(UP * 0.06)  # Slight adjustment to connect with the line

        # Group all components
        complex_vad_arrow = VGroup(line1, line2, line3, arrow_tip)

        # Animate the complex arrow
        self.play(Create(complex_vad_arrow), run_time=0.7)
        self.wait(0.5)

       # 1. Create the initial formula with variables
        vad_bp_formula_1 = MathTex(
            r"\frac{VAD^* - (1 - BP)}{BP}",
            font_size=16
        )

        # Position to the right of the VAD-(1-BP)>0 box
        vad_bp_formula_1.next_to(vad_bp_box, RIGHT*1.09, buff=0.64)
         # 2. Create "VAD* = 0" text below (similar to your VAD = 0)
        vad_zero_text = Tex("VAD = 0", font_size=16)

        # Position below and to the right of the VAD-(1-BP)>0 box
        vad_zero_text.move_to(vad_bp_box.get_center() + DOWN * 0.95 + RIGHT * 1.95)
          # Create the "or" text to place between the formula and VAD* = 0
        or_text = Tex("or", font_size=19).set_color(WHITE)

         # Position the "or" text vertically between the formula and VAD* = 0
        or_text.move_to([
            vad_bp_formula_1.get_center()[0],  # Same x-coordinate as the formula
            (vad_bp_formula_1.get_bottom()[1] + vad_zero_text.get_top()[1])/2,  # Midpoint
            0
        ])
        # Using the same arrow style as before for consistency
        # Create arrow from VAD-(1-BP)>0 to VAD-(1-BP)>0 formula
        # Create arrow from VAD-(1-BP)>0 to VAD-(1-BP)>0 formula
        # Using the same arrow style as before for consistency
        arrow_to_vad_bp_formula = Arrow(
            start=vad_bp_box.get_right(), 
            end=vad_bp_formula_1.get_left(),
            buff=0.05,
            color=YELLOW,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=9.0
        )

        # Create "Yes" label
        vad_yes_label = Tex("Yes", font_size=15).set_color(WHITE)
        arrow_vad_center = arrow_to_vad_bp_formula.get_center()
        vad_yes_label.move_to(arrow_vad_center).shift(UP * 0.20)

        # Animate the arrow first
        self.play(GrowArrow(arrow_to_vad_bp_formula), run_time=0.5)
        self.wait(0.3)

        # Then animate the "Yes" label
        self.play(Write(vad_yes_label), run_time=0.3)
        self.wait(0.3)

        # Show the initial formula with variables
        self.play(Write(vad_bp_formula_1), run_time=0.5)
        self.wait(0.5)
        self.play(Write(or_text), run_time=0.3)
        self.wait(0.3)

        # 2. Create "VAD* = 0" text below (similar to your VAD = 0)
        vad_zero_text = Tex("0", font_size=17)

        # Position below and to the right of the VAD-(1-BP)>0 box WITH EXTRA GAP
        vad_zero_text.move_to(vad_bp_box.get_center() + DOWN * 0.95 + RIGHT * 2.15)  # Increased RIGHT shift

        # Create L-shaped arrow from VAD-(1-BP)>0 to VAD* = 0
        start_point = vad_bp_box.get_bottom()

        # Calculate where the arrow should end, with a gap before the text
        text_left = vad_zero_text.get_left()
        mid_point = [start_point[0], text_left[1], 0]  # Same x as start, same y as text

        # Calculate shortened arrow endpoint with gap (similar to your working example)
        shortened_factor = 0.44  # Match your working example's factor
        full_width = text_left[0] - mid_point[0]
        shortened_width = full_width * (1 - shortened_factor)
        end_point = [mid_point[0] + shortened_width, mid_point[1], 0]

        # Create line segments
        line1 = Line(start_point, mid_point, stroke_color=YELLOW, stroke_width=4)
        line2 = Line(mid_point, end_point, stroke_color=YELLOW, stroke_width=4)

        # Create arrow head
        triangle = Triangle(fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        triangle.scale(0.10)  # Same size as other arrow heads
        triangle.rotate(-PI/2)  # Rotate to point right
        triangle.next_to(line2, RIGHT, buff=0)  # Position at end of line

        # Group arrow components
        l_arrow_to_vad_zero = VGroup(line1, line2, triangle)

        # Create "No" label
        no_label = Tex("No", font_size=15).set_color(WHITE)
        no_label.next_to(line1, RIGHT, buff=0.1)

        # Animate the L-shaped arrow
        self.play(Create(l_arrow_to_vad_zero), Write(no_label), run_time=0.5)
        self.wait(0.5)

        # Animate the VAD* = 0 text
        self.play(Write(vad_zero_text), run_time=0.5)
        self.wait(1.0)

        # ================== FINAL VCS COMPUTATION ==================
        # Create final Video Comprehension Score aggregation
        vad_bp_brace = Brace(
            VGroup(vad_bp_formula_1, vad_zero_text),  # Updated to use vad_bp_formula_1
            direction=RIGHT                        # Brace appears on right side
        )

        # Move brace closer to text
        vad_bp_brace.shift(LEFT * 0.15)
        vad_bp_brace.set_stroke(width=0.01)  # Thin stroke

        # Create final box with text "VAD***"
        vad_final_text = Tex("Final VAD", font_size=16).set_color_by_gradient(RED, BLUE)
        vad_final_box = Rectangle(width=1.5, height=0.455).set_stroke(width=1, color=WHITE)
        vad_final_text.move_to(vad_final_box.get_center())
        vad_final_group = VGroup(vad_final_box, vad_final_text)

        # Position to right of brace
        vad_final_group.next_to(vad_bp_brace, RIGHT*1.38, buff=0.5)
        vad_final_group.set_y(vad_bp_brace.get_center()[1])  # Center vertically

        # Animate the brace
        self.play(Create(vad_bp_brace), run_time=0.5)
        self.wait(0.5)

        # Create arrow from brace to result box
        arrow_brace_to_vad_final = Arrow(
            start=vad_bp_brace.get_right(),
            end=vad_final_box.get_left(),
            buff=0.05,
            color=YELLOW,
            stroke_width=8,  # Thicker line to match other arrows
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=9.0
        )

        # Animate the arrow
        self.play(GrowArrow(arrow_brace_to_vad_final), run_time=0.5)
        self.wait(0.5)

        # Animate the result box and text
        self.play(Create(vad_final_box), Write(vad_final_text), run_time=0.7)
        self.wait(1.0)

        # ================== SCORE ABBREVIATION TRANSITION ==================
        # Transform full score names to abbreviated forms with values
        
        # Create abbreviated text objects for all alignment scores
        sas_abbrev = Text("SAS", font_size=16).set_color_by_gradient(RED_A)
        cas_abbrev = Text("CAS", font_size=16).set_color_by_gradient(RED_A)
        nas_abbrev = Text("NAS", font_size=16).set_color_by_gradient(RED_A)
        bp_abbrev = Text("BP", font_size=16).set_color_by_gradient(RED_A)

        # Position abbreviated text in the center of their respective boxes
        sas_abbrev.move_to(semantic_box.get_center())
        cas_abbrev.move_to(content_box.get_center())
        nas_abbrev.move_to(narrative_box.get_center())
        bp_abbrev.move_to(brevity_box.get_center())

        # ================== TEXT ABBREVIATION ANIMATION ==================
        # Fade out full text labels and fade in abbreviated versions
        self.play(
            FadeOut(semantic_text),
            FadeOut(content_text),
            FadeOut(narrative_text),
            FadeOut(brevity_text),
            FadeIn(sas_abbrev),
            FadeIn(cas_abbrev),
            FadeIn(nas_abbrev),
            FadeIn(bp_abbrev),
            run_time=1.0
        )
        self.wait(0.5)

        # ================== SCORE VALUE ASSIGNMENT ==================
        # Create and display numerical values for each alignment score
        equals_text = Text(" = 0.85", font_size=16).set_color(WHITE)
        sas_equals = equals_text.copy().next_to(sas_abbrev, RIGHT, buff=0.1)
        cas_equals = equals_text.copy().next_to(cas_abbrev, RIGHT, buff=0.1)
        nas_equals = equals_text.copy().next_to(nas_abbrev, RIGHT, buff=0.1)
        bp_equals = equals_text.copy().next_to(bp_abbrev, RIGHT, buff=0.1)

        # Animate the appearance of numerical values for each score
        self.play(
            Write(sas_equals),
            Write(cas_equals),
            Write(nas_equals),
            Write(bp_equals),
            run_time=1.0
        )
        self.wait(0.5)

        # ================== SCORE GROUP CENTERING ==================
        # Group abbreviations with their values and center in boxes
        sas_group = VGroup(sas_abbrev, sas_equals)
        cas_group = VGroup(cas_abbrev, cas_equals)
        nas_group = VGroup(nas_abbrev, nas_equals)
        bp_group = VGroup(bp_abbrev, bp_equals)

        # Animate centering of grouped text within their respective boxes
        self.play(
            sas_group.animate.move_to(semantic_box.get_center()),
            cas_group.animate.move_to(content_box.get_center()),
            nas_group.animate.move_to(narrative_box.get_center()),
            bp_group.animate.move_to(brevity_box.get_center()),
            run_time=1.0
        )
        self.wait(2.0)  # A longer wait at the end to show the final state

        # ================== DYNAMIC GRADIENT OUTLINES ==================
        # Create animated gradient outlines for SAS and CAS boxes with moving effects
        # Set up value trackers to control the position of the gradient animation
        sas_tracker = ValueTracker(0)
        cas_tracker = ValueTracker(0)

        # Function to create a continuously moving gradient outline around boxes
        def create_moving_outline(box, tracker):
            """
            Creates an animated gradient outline that moves around the perimeter of a box.
            
            Args:
                box: The box object to create an outline for
                tracker: ValueTracker to control the gradient movement
            
            Returns:
                A continuously updating outline with moving gradient effect
            """
            # Create a path along the box perimeter
            outline = VMobject() # type: ignore
            width, height = box.width, box.height
            
            # Calculate the corners of the box for perimeter outline
            top_left = box.get_center() + np.array([-width/2, height/2, 0]) # type: ignore
            top_right = box.get_center() + np.array([width/2, height/2, 0])  # type: ignore
            bottom_right = box.get_center() + np.array([width/2, -height/2, 0])  # type: ignore
            bottom_left = box.get_center() + np.array([-width/2, -height/2, 0])  # type: ignore
            
            # Set the points to draw the rectangular perimeter
            outline.set_points_as_corners([top_left, top_right, bottom_right, bottom_left, top_left])
            
            # Make the outline thicker than the original box for visual prominence
            outline.set_stroke(width=6)
            
            # Set up the gradient colors and animation logic
            def update_outline(mob):
                """Update function for animated gradient effect"""
                t_value = tracker.get_value()
                # Create gradient by varying the stroke color/opacity along the path
                colors = []
                opacities = []
                
                # Create multiple points around the perimeter for smooth gradient
                n_points = 100
                for i in range(n_points):
                    # Calculate position along the perimeter (0 to 1)
                    alpha = i / n_points
                    # Offset by the tracker value to create motion
                    offset_alpha = (alpha + t_value) % 1.0
                    
                    # Create a peak near the current position for the gradient
                    # This creates a "moving light" effect around the perimeter
                    distance = min(abs(offset_alpha - 0.5), abs(1 + offset_alpha - 0.5), abs(offset_alpha - 1.5))
                    intensity = np.exp(-distance * 10) * 0.8  # type: ignore # Controls gradient spread
                    
                    colors.append(WHITE)
                    opacities.append(intensity)
                
                # Apply the colors and opacities to create the gradient effect
                mob.set_stroke(colors, opacity=opacities)
                return mob
            
            # Create the continuously updating outline with always_redraw
            moving_outline = always_redraw(lambda: update_outline(outline.copy()))
            return moving_outline

        # ================== OUTLINE ANIMATION SETUP ==================
        # Create and configure moving outlines for SAS and CAS boxes
        sas_outline = create_moving_outline(semantic_box, sas_tracker)
        cas_outline = create_moving_outline(content_box, cas_tracker)

        # Add the animated outlines to the scene
        self.add(sas_outline, cas_outline)

        # ================== GRADIENT ANIMATION CONTROL ==================
        # Set up continuous animation control for gradient movement
        def update_trackers(dt):
            """Update function for continuous gradient animation"""
            # Update the position trackers (speed control)
            sas_tracker.increment_value(dt * 0.3)  # Adjust speed by changing the multiplier
            cas_tracker.increment_value(dt * 0.3)  # Same speed for both boxes

        # Add the updater to the scene for continuous animation
        self.add_updater(update_trackers)

        # Wait a moment to see the gradient animation effect
        self.wait(1.0)

        # ================== FORMULA BOX GRADIENT EXTENSION ==================
        # Extend gradient animation to include the formula constraint box
        
        # Create a tracker for the formula box gradient animation
        formula_tracker = ValueTracker(0)

        # Create a moving gradient outline for the formula box using the same function
        formula_outline = create_moving_outline(scale_rect, formula_tracker)

        # Add the formula outline to the scene
        self.add(formula_outline)

        # ================== ENHANCED GRADIENT CONTROL ==================
        # Update the tracker update function to include the formula box
        def update_all_trackers(dt):
            """Enhanced update function for all gradient animations"""
            # Update all trackers with synchronized speed
            sas_tracker.increment_value(dt * 0.3)      # SAS box speed
            cas_tracker.increment_value(dt * 0.3)      # CAS box speed
            formula_tracker.increment_value(dt * 0.3)  # Formula box speed
            
        # Replace the previous updater with the enhanced version
        self.remove_updater(update_trackers)  # Remove previous updater if it exists
        self.add_updater(update_all_trackers)  # Add the new combined updater

        # ================== CONSTRAINT VALUE SUBSTITUTION ==================
        # Replace constraint formula with actual numerical values
        
        # Get the original size and position of the text for consistent formatting
        original_center = scale_text.get_center()
        original_height = scale_text.height

        # Create the new text with values substituted - split into parts for coloring
        substituted_text = MathTex(
            r"0.85", r" - (1 - ", r"0.85", r") > 0",
            font_size=16
        )
        # Apply color coding to numeric parts for visual emphasis
        substituted_text[0].set_color(RED_A)  # First 0.85 value
        substituted_text[2].set_color(RED_A)  # Second 0.85 value
        substituted_text.move_to(original_center)

        # Ensure the new text has the same height as the original for consistency
        height_ratio = original_height / substituted_text.height
        substituted_text.scale(height_ratio)

        # Animate the text transformation with value substitution
        self.play(
            Transform(scale_text, substituted_text),
            run_time=1.0
        )
        self.wait(0.7)

        # ================== CONSTRAINT SIMPLIFICATION ==================
        # Show the simplified result of the constraint evaluation
        simplified_text = MathTex(
            r"0.70", r" > 0",
            font_size=16
        )
        # Apply color coding to the result value
        simplified_text[0].set_color(RED_A)  # 0.70 result value
        simplified_text.move_to(original_center)

        # Ensure the simplified text also has the same height for consistency
        height_ratio = original_height / simplified_text.height
        simplified_text.scale(height_ratio)

        # Animate the simplification to show final constraint result
        self.play(
            Transform(scale_text, simplified_text),
            run_time=1.0
        )

        self.wait(1.0)

        # ================== SCALED SAS CALCULATION ==================
        # Calculate and display the scaled SAS value using the validated constraint
        
        # Create a new MathTex for the first fraction with substituted values
        fraction_values = MathTex(
            r"\frac{0.70}{0.85}", 
            font_size=16
        )
        fraction_values.move_to(compare_text_1.get_center())

        # Create a MathTex for the final calculated result
        final_result = MathTex(
            r"0.82",
            font_size=16  # Slightly larger for emphasis
        )
        final_result.move_to(compare_text_1.get_center())

        # Animate the transition from the formula to the substituted values
        self.play(
            Transform(compare_text_1, fraction_values),
            run_time=1.0
        )
        self.wait(0.8)

        # Animate the transition to the final calculated result
        self.play(
            Transform(compare_text_1, final_result),
            run_time=1.0
        )
        self.wait(1.0)

        # ================== RESULT HIGHLIGHTING EFFECTS ==================
        # Add special visual effects to emphasize the final scaled SAS result
        
        # Create a tracker for the glowing effect around the final result
        result_tracker = ValueTracker(0)

        # Function to create a pulsing/glowing outline around the result text
        def create_result_glow(text, tracker):
            """
            Creates a pulsing glow effect around result text for emphasis.
            
            Args:
                text: The text object to create a glow around
                tracker: ValueTracker to control the glow animation
            
            Returns:
                A continuously updating glow effect
            """
            # Create a circle that surrounds the text
            glow_circle = Circle(radius=text.width/1.2, stroke_width=0, fill_opacity=0, z_index=-1)  # type: ignore # Set lower z_index
            glow_circle.move_to(text.get_center())
            
            def update_glow(mob):
                t_value = tracker.get_value()
                
                # Create gradient by varying the stroke properties
                colors = []
                opacities = []
                
                n_points = 80  # Number of points around the circle
                for i in range(n_points):
                    # Calculate position around the circle (0 to 1)
                    alpha = i / n_points
                    # Offset by the tracker value to create motion
                    offset_alpha = (alpha + t_value) % 1.0
                    
                    # Create a peak for the gradient effect
                    distance = min(abs(offset_alpha - 0.5), abs(1 + offset_alpha - 0.5), abs(offset_alpha - 1.5))
                    intensity = np.exp(-distance * 8) * 0.9  # type: ignore # Controls gradient spread
                    
                    # Use gold/amber color for the result glow
                    colors.append(GOLD)
                    opacities.append(intensity)
                
                # Apply the gradient
                mob.set_stroke(colors, width=5, opacity=opacities)
                return mob
            
            # Create the continuously updating glow
            result_glow = always_redraw(lambda: update_glow(glow_circle.copy()))
            return result_glow

        # Create the glowing effect for the final result
        result_glow = create_result_glow(final_result, result_tracker)

        # Add the glow behind the text - using z_index instead of send_to_back
        self.add(result_glow)
        # No need for send_to_back since we set z_index=-1 in the creation function

        # Update the tracker function to include the result glow
        def update_result_tracker(dt):
            # Control the speed of the glow effect
            result_tracker.increment_value(dt * 0.4)  # Slightly faster than the boxes for emphasis

        # Add the updater
        self.add_updater(update_result_tracker)

        # Add a pulsing effect to the result text itself
        self.play(
            final_result.animate.set_color(GOLD),  # Change color to gold
            run_time=0.7
        )
        self.play(
            final_result.animate.scale(1.1),  # Slightly increase size
            run_time=0.5
        )
        self.play(
            final_result.animate.scale(1/1.1),  # Return to original size
            run_time=0.5
        )

        # Wait to show the full effect
        self.wait(1.0)

        # Create a tracker for the Scaled SAS box
        scaled_sas_tracker = ValueTracker(0)

        # Create a moving gradient outline for the Scaled SAS box using the same function
        scaled_sas_outline = create_moving_outline(new_box_rect, scaled_sas_tracker)

        # Add the outline to the scene
        self.add(scaled_sas_outline)

        # IMPORTANT: Remove ALL previous updaters to prevent speed stacking
        # This will clear any updaters we've added before
        self.updaters = [] 

        # Create a fresh combined updater function with consistent speeds
        def update_all_trackers(dt):
            # Update all trackers with the same speed
            sas_tracker.increment_value(dt * 0.3)
            cas_tracker.increment_value(dt * 0.3) # Same speed for consistency
            formula_tracker.increment_value(dt * 0.3)
            scaled_sas_tracker.increment_value(dt * 0.3)
            result_tracker.increment_value(dt * 0.4)
            
            
        # Add our clean updater function
        self.add_updater(update_all_trackers)

        # Create new text for "Scaled.SAS = 0.82"
        scaled_sas_value = MathTex(r"Scaled.SAS = 0.82", font_size=13)
        scaled_sas_value.move_to(new_box_text.get_center())

        # Animate the text change
        self.play(
            Transform(new_box_text, scaled_sas_value),
            run_time=1.0
        )
        self.wait(1.0)

        # Create all the trackers - initializing with matching values for synchronization
        nas_tracker = ValueTracker(sas_tracker.get_value())  # Initialize with same value as SAS tracker
        ssas_nas_tracker = ValueTracker(formula_tracker.get_value())  # Initialize with same value as formula tracker
        ssas_nas_test_tracker = ValueTracker(formula_tracker.get_value())  # Also sync with formula tracker

        # Create outlines for all boxes
        nas_outline = create_moving_outline(narrative_box, nas_tracker)
        ssas_nas_test_outline = create_moving_outline(ssas_nas_test_box, ssas_nas_test_tracker)

        # Create the moving gradient outlines with custom parameters for S.SAS <= NAS box
        def create_moving_outline_adjusted(box, tracker, n_points=100, intensity_multiplier=0.8, spread_factor=10, speed_multiplier=1.0):
            # Create a path along the box perimeter
            outline = VMobject() # type: ignore
            width, height = box.width, box.height
            
            # Calculate the corners of the box
            top_left = box.get_center() + np.array([-width/2, height/2, 0]) # type: ignore
            top_right = box.get_center() + np.array([width/2, height/2, 0])  # type: ignore
            bottom_right = box.get_center() + np.array([width/2, -height/2, 0])  # type: ignore
            bottom_left = box.get_center() + np.array([-width/2, -height/2, 0])  # type: ignore
            
            # Set the points to draw the perimeter
            outline.set_points_as_corners([top_left, top_right, bottom_right, bottom_left, top_left])
            
            # Make the outline thicker than the original box
            outline.set_stroke(width=6)
            
            # Set up the gradient colors with adjustable parameters
            def update_outline(mob):
                t_value = tracker.get_value() * speed_multiplier
                # Create gradient by varying the stroke color/opacity along the path
                colors = []
                opacities = []
                for i in range(n_points):
                    # Calculate position along the perimeter (0 to 1)
                    alpha = i / n_points
                    # Offset by the tracker value to create motion
                    offset_alpha = (alpha + t_value) % 1.0
                    
                    # Create a peak near the current position for the gradient
                    distance = min(abs(offset_alpha - 0.5), abs(1 + offset_alpha - 0.5), abs(offset_alpha - 1.5))
                    intensity = np.exp(-distance * spread_factor) * intensity_multiplier  # type: ignore
                    
                    colors.append(WHITE)
                    opacities.append(intensity)
                
                # Apply the colors and opacities
                mob.set_stroke(colors, opacity=opacities)
                return mob
            
            # Create the continuously updating outline
            moving_outline = always_redraw(lambda: update_outline(outline.copy()))
            return moving_outline

        # Create adjusted outline for S.SAS <= NAS box - synchronized with formula box
        ssas_nas_outline = create_moving_outline_adjusted(
            ssas_nas_box, 
            ssas_nas_tracker,
            n_points=120,       # More points for smoother gradient
            intensity_multiplier=0.9,  # Brighter peak
            spread_factor=8,    # Wider gradient (lower number = wider spread)
            speed_multiplier=1.0  # Same speed multiplier as formula box
        )

        # Create the updater function with precise control to keep animations synchronized
        def update_trackers(dt):
            # Update base trackers
            speed = dt * 0.3
            
            # Group 1: SAS, CAS, NAS synced together
            sas_increment = speed
            sas_tracker.increment_value(sas_increment)
            cas_tracker.increment_value(sas_increment)
            nas_tracker.increment_value(sas_increment)
            
            # Group 2: Formula box, S.SAS <= NAS, and "0.70 > 0" synced together
            formula_increment = speed
            formula_tracker.increment_value(formula_increment)
            ssas_nas_tracker.increment_value(formula_increment)
            ssas_nas_test_tracker.increment_value(formula_increment)
            
            # Other trackers
            scaled_sas_tracker.increment_value(speed)
            result_tracker.increment_value(dt * 0.4)

        # Remove all existing updaters before adding our synced one
        self.updaters = []
        self.add_updater(update_trackers)

        # Add NAS outline first - perfectly synchronized with existing SAS/CAS
        self.add(nas_outline)

        # Wait before adding S.SAS <= NAS effect
        self.wait(2.0)

        # Add S.SAS <= NAS outline next - synchronized with formula box
        self.add(ssas_nas_outline)

        # Transform S.SAS <= NAS text to "0.82 <= 0.85" with RED_A color
        original_center = ssas_nas_text.get_center()
        original_height = ssas_nas_text.height

        # Create text with substituted values
        substituted_text = MathTex(
            r"0.82", r" \leq ", r"0.85",
            font_size=13
        )
        # Color the numeric parts with RED_A
        substituted_text[0].set_color(RED_A)
        substituted_text[2].set_color(RED_A)
        substituted_text.move_to(original_center)

        # Ensure the new text has the same height as the original
        height_ratio = original_height / substituted_text.height
        substituted_text.scale(height_ratio)

        # Animate the text transformation
        self.play(
            Transform(ssas_nas_text, substituted_text),
            run_time=1.0
        )
        self.wait(0.7)

        # Wait before adding formula box effect
        self.wait(2.0)

        # Wait before adding formula box effect
        self.wait(2.0)

        # Add formula box outline last - already synchronized with S.SAS <= NAS
        self.add(ssas_nas_test_outline)

        # Wait a bit before starting text animation
        self.wait(1.0)

        # Get original position and size of text for replacement animations
        original_center = ssas_nas_test_text.get_center()
        original_height = ssas_nas_test_text.height

        # Create text with substituted values
        substituted_text = MathTex(
            r"0.82", r" - (1 - ", r"0.85", r") > 0",
            font_size=14
        ) 
        # Color the numbers
        substituted_text[0].set_color(RED_A)
        substituted_text[2].set_color(RED_A)
        substituted_text.move_to(original_center)

        # Ensure same height as original
        height_ratio = original_height / substituted_text.height
        substituted_text.scale(height_ratio)

        # Animate the text transformation
        self.play(
            Transform(ssas_nas_test_text, substituted_text),
            run_time=1.0
        )
        self.wait(0.7)

        # Create simplified result "0.67 > 0" with custom font
        # Use Tex instead of MathTex for font control
        simplified_text = Tex(r"0.67 $>$ 0", font_size=13)

        # Color just the "0.67" part
        simplified_text[0][:4].set_color(RED_A)  # This selects the first 4 characters "0.67"

        simplified_text.move_to(original_center)

        # Ensure same height
        height_ratio = original_height / simplified_text.height
        simplified_text.scale(height_ratio)

        # Animate the simplification
        self.play(
            Transform(ssas_nas_test_text, simplified_text),
            run_time=1.0
        )

        # Wait to show the completed effect for the formula box
        self.wait(2.0)

        # Now animate the formula S.SAS - (1 - NAS) / NAS to show values
        # First get a reference to the formula
        ssas_formula = ssas_formula  # Reference to the existing formula object in your scene

        # Get original position and size of formula for replacement animations
        formula_center = ssas_formula.get_center()
        formula_height = ssas_formula.height

        # Create text with substituted values
        substituted_formula = MathTex(
            r"\frac{0.67}{0.85}",
            font_size=16
        )
        substituted_formula.move_to(formula_center)

        # Ensure same height as original
        height_ratio = formula_height / substituted_formula.height
        substituted_formula.scale(height_ratio)

        # Animate the text transformation
        self.play(
            Transform(ssas_formula, substituted_formula),
            run_time=1.0
        )
        self.wait(0.7)

        # Create simplified result "0.78" with smaller font size
        final_formula = MathTex(
            r"0.78",
            font_size=3.8  # Reduced from 16 to 14
        )
        final_formula.move_to(formula_center)

        # Ensure same height but WITHOUT the extra scaling
        height_ratio = formula_height / final_formula.height * 0.38  # 10% smaller for better fit
        final_formula.scale(height_ratio)

        # Animate the simplification
        self.play(
            Transform(ssas_formula, final_formula),
            run_time=1.0
        )
        self.wait(0.5)

        # Add the glowing circle effect around the result
        # Create a tracker for the glowing effect
        formula_result_tracker = ValueTracker(0)

        # Function to create a pulsing/glowing circle around the result
        def create_result_glow(text, tracker):
            # Create a circle that surrounds the text
            glow_circle = Circle(radius=text.width/1.5, stroke_width=0, fill_opacity=0, z_index=-1)  # type: ignore
            glow_circle.move_to(text.get_center())
            
            def update_glow(mob):
                t_value = tracker.get_value()
                
                # Create gradient by varying the stroke properties
                colors = []
                opacities = []
                
                n_points = 80  # Number of points around the circle
                for i in range(n_points):
                    # Calculate position around the circle (0 to 1)
                    alpha = i / n_points
                    # Offset by the tracker value to create motion
                    offset_alpha = (alpha + t_value) % 1.0
                    
                    # Create a peak for the gradient effect
                    distance = min(abs(offset_alpha - 0.5), abs(1 + offset_alpha - 0.5), abs(offset_alpha - 1.5))
                    intensity = np.exp(-distance * 8) * 0.9  # type: ignore # Controls gradient spread
                    
                    # Use gold/amber color for the result glow
                    colors.append(GOLD)
                    opacities.append(intensity)
                
                # Apply the gradient
                mob.set_stroke(colors, width=5, opacity=opacities)
                return mob
            
            # Create the continuously updating glow
            result_glow = always_redraw(lambda: update_glow(glow_circle.copy()))
            return result_glow

        # Create the glowing effect for the final result
        formula_result_glow = create_result_glow(final_formula, formula_result_tracker)

        # Add the glow behind the text
        self.add(formula_result_glow)

        # Update the updater function to include the result glow
        self.updaters = []

        def update_all_trackers(dt):
            # Base trackers
            speed = dt * 0.3
            
            # Group 1: SAS, CAS, NAS synced together
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            
            # Group 2: Formula box, S.SAS <= NAS, and formula box synced together
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            
            # Other trackers
            scaled_sas_tracker.increment_value(speed)
            result_tracker.increment_value(dt * 0.4)
            
            # Add the new glowing effect tracker
            formula_result_tracker.increment_value(dt * 0.4)  # Same speed as result_tracker

        # Add the updated tracker
        self.add_updater(update_all_trackers)

        # Add a subtle pulsing effect to the result text
        self.play(
            final_formula.animate.set_color(GOLD),  # Change color to gold
            run_time=0.7
        )
        self.play(
            final_formula.animate.scale(1.1),  # Slightly increase size
            run_time=0.5
        )
        self.play(
            final_formula.animate.scale(1/1.1),  # Return to original size
            run_time=0.5
        )

        self.wait(2.0)

        # -------------------------------------------------------------
        # Now animate the VAD* box with simplified effect (just the moving outline)
        # -------------------------------------------------------------

        # Get a reference to the VAD* box
        vad_star_box = result_box  # Reference to the existing VAD* box
        vad_star_text = result_text  # Reference to the existing VAD* text

        # Get the center position of the VAD* box
        vad_star_center = vad_star_text.get_center()

        # Create new text "VAD* = 0.78" with smaller font to fit in the box
        vad_value_text = MathTex(r"VAD^* = 0.78", font_size=13)  # Reduced from 19 to 12
        vad_value_text.move_to(vad_star_center)

        # Create tracker for the VAD* box
        vad_star_tracker = ValueTracker(formula_result_tracker.get_value())  # Start synchronized with the formula result

        # Create moving gradient outline for the VAD* box
        vad_star_outline = create_moving_outline(vad_star_box, vad_star_tracker)

        # Add the outline to the scene
        self.add(vad_star_outline)

        # Update the updater function to include the VAD* box
        self.updaters = []

        def update_final_trackers(dt):
            # Base trackers
            speed = dt * 0.3
            
            # Group 1: SAS, CAS, NAS synced together
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            
            # Group 2: Formula box, S.SAS <= NAS, and formula box synced together
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            
            # Other trackers
            scaled_sas_tracker.increment_value(speed)
            result_tracker.increment_value(dt * 0.4)
            
            # Keep glowing effects in sync
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)  # Same speed as result_tracker

        # Add the updated tracker
        self.add_updater(update_final_trackers)

        # Wait a moment before starting the transformation
        self.wait(1.0)

        # Animate the transformation of VAD* to VAD* = 0.78
        self.play(
            Transform(vad_star_text, vad_value_text),
            run_time=1.0
        )

        # Final wait to show the completed animation
        self.wait(3.0)

        # Create a tracker for the NAS formula box - make sure to set the same starting value
        nas_ssas_tracker = ValueTracker(ssas_nas_test_tracker.get_value())  # Initialize with same value as existing tracker

        # Create a moving gradient outline for the formula box
        nas_test_outline = create_moving_outline(nas_test_box, nas_ssas_tracker)

        # Add the outline to the scene
        self.add(nas_test_outline)

        # Update the existing tracker function - preserve exact synchronization
        def update_all_trackers(dt):
            # Keep all existing tracker updates with same speeds
            speed = dt * 0.3
            
            # Group 1: SAS, CAS, NAS synced together
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            
            # Group 2: Formula box, S.SAS <= NAS, and other formula boxes synced
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)  # Add to this group with exact same speed
            
            # Keep all other tracker updates exactly the same
            scaled_sas_tracker.increment_value(speed)
            result_tracker.increment_value(dt * 0.4)
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)

        # Update updater function carefully to maintain synchronization
        self.updaters = []
        self.add_updater(update_all_trackers)

        # Get original position and size for the text transformation
        original_center = nas_test_text.get_center()
        original_height = nas_test_text.height

        # Create text with substituted values
        substituted_text = MathTex(
            r"0.85", r" - (1 - ", r"0.82", r") > 0",
            font_size=13
        )
        # Color the numbers
        substituted_text[0].set_color(RED_A)
        substituted_text[2].set_color(RED_A)
        substituted_text.move_to(original_center)

        # Ensure same height as original
        height_ratio = original_height / substituted_text.height
        substituted_text.scale(height_ratio)

        # Animate the text transformation
        self.play(
            Transform(nas_test_text, substituted_text),
            run_time=1.0
        )
        self.wait(0.7)

        # Match EXACTLY the previous "0.67 > 0" text format 13
        simplified_text = Tex(r"0.67 $>$ 0", font_size=10)
        simplified_text[0][:4].set_color(RED_A)  # This selects the first 4 characters "0.67"
        simplified_text.move_to(original_center)

        # Match exact scaling
        height_ratio = original_height / simplified_text.height
        simplified_text.scale(height_ratio)

        # Animate the simplification
        self.play(
            Transform(nas_test_text, simplified_text),
            run_time=1.0
        )

        # Now animate the formula NAS - (1 - S.SAS) / S.SAS to show values
        # First get a reference to the formula
        nas_formula = nas_formula_1  # Reference to the existing NAS formula object

        # Get original position and size of formula for replacement animations
        formula_center = nas_formula.get_center()
        formula_height = nas_formula.height

        # Create text with substituted values
        substituted_nas_formula = MathTex(
            r"\frac{0.67}{0.82}",
            font_size=16
        )
        substituted_nas_formula.move_to(formula_center)

        # Ensure same height as original
        height_ratio = formula_height / substituted_nas_formula.height
        substituted_nas_formula.scale(height_ratio)

        # Animate the text transformation
        self.play(
            Transform(nas_formula, substituted_nas_formula),
            run_time=1.0
        )
        self.wait(0.7)

        # Create simplified result "0.81" with matching size to other results
        final_nas_formula = MathTex(
            r"0.81",
            font_size=13
        )
        final_nas_formula.move_to(formula_center)

        # Ensure same height as original but with proper scaling
        height_ratio = formula_height / final_nas_formula.height * 0.38  # Match the scaling factor used for 0.78
        final_nas_formula.scale(height_ratio)

        # Animate the simplification
        self.play(
            Transform(nas_formula, final_nas_formula),
            run_time=1.0
        )
        self.wait(0.5)

        # Add the glowing circle effect around the result
        # Create a tracker for the glowing effect - sync with existing trackers
        nas_formula_result_tracker = ValueTracker(formula_result_tracker.get_value())

        # Create the glowing effect for the final result - using same function as for 0.78
        nas_formula_result_glow = create_result_glow(final_nas_formula, nas_formula_result_tracker)

        # Add the glow behind the text
        self.add(nas_formula_result_glow)

        # Update the updater function to include the new glow effect
        self.updaters = []

        def update_final_all_trackers(dt):
            # Base trackers
            speed = dt * 0.3
            
            # All existing group animations
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)
            scaled_sas_tracker.increment_value(speed)
            result_tracker.increment_value(dt * 0.4)
            
            # All glow effects synced at same speed
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)
            nas_formula_result_tracker.increment_value(dt * 0.4)  # Add new tracker

        # Add the updated tracker
        self.add_updater(update_final_all_trackers)

        # Add a subtle pulsing effect to the result text - match the style used for 0.78
        self.play(
            final_nas_formula.animate.set_color(GOLD),  # Change color to gold
            run_time=0.7
        )
        self.play(
            final_nas_formula.animate.scale(1.1),  # Slightly increase size
            run_time=0.5
        )
        self.play(
            final_nas_formula.animate.scale(1/1.1),  # Return to original size
            run_time=0.5
        )

        self.wait(2.0)

        # Create a tracker for the VAD** box (the second VAD* box)
        vad_star2_box = result_box_nas  # Reference to the existing second VAD* box
        vad_star2_text = result_text_nas  # Reference to the existing VAD* text

        # Create tracker for the VAD** box
        vad_star2_tracker = ValueTracker(vad_star_tracker.get_value())  # Start synchronized

        # Create moving gradient outline for the VAD** box
        vad_star2_outline = create_moving_outline(vad_star2_box, vad_star2_tracker)

        # Add the outline to the scene
        self.add(vad_star2_outline)

        # Update the updater function to include both VAD* boxes
        self.updaters = []

        def update_complete_trackers(dt):
            # Base speed
            speed = dt * 0.3
            
            # All existing animation trackers
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)
            scaled_sas_tracker.increment_value(speed)
            
            # All glow effects
            result_tracker.increment_value(dt * 0.4)
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)
            vad_star2_tracker.increment_value(dt * 0.4)  # Add new tracker
            nas_formula_result_tracker.increment_value(dt * 0.4)

        # Add the updated tracker
        self.add_updater(update_complete_trackers)

        # Get the center position of the VAD** box
        vad_star2_center = vad_star2_text.get_center()

        # Create new text "VAD* = 0.81" with matching font size
        vad_star2_value_text = MathTex(r"VAD^* = 0.81", font_size=13)
        vad_star2_value_text.move_to(vad_star2_center)

        # Wait a moment before starting the transformation
        self.wait(1.0)

        # Animate the transformation of VAD** to VAD* = 0.81
        self.play(
            Transform(vad_star2_text, vad_star2_value_text),
            run_time=1.0
        )

        # Wait to show the effect
        self.wait(1.0)

        # Create a tracker for the Final VAD box
        final_vad_tracker = ValueTracker(vad_star2_tracker.get_value())  # Start synchronized with other VAD boxes

        # Create moving gradient outline for the Final VAD box
        final_vad_outline = create_moving_outline(final_vad_box, final_vad_tracker)

        # Add the outline to the scene
        self.add(final_vad_outline)

        # Update the updater function to include the Final VAD box
        self.updaters = []

        def update_final_complete_trackers(dt):
            # Base speed
            speed = dt * 0.3
            
            # All existing animation trackers
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)
            scaled_sas_tracker.increment_value(speed)
            
            # All glow effects
            result_tracker.increment_value(dt * 0.4)
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)
            vad_star2_tracker.increment_value(dt * 0.4)
            nas_formula_result_tracker.increment_value(dt * 0.4)
            final_vad_tracker.increment_value(dt * 0.4)  # Add new tracker for Final VAD

        # Add the updated tracker
        self.add_updater(update_final_complete_trackers)

        # Get the center position of the Final VAD box
        final_vad_center = final_vad_text.get_center()

        # Create new text "Final VAD = 0.80" with matching font size and gradient color
        final_vad_value_text = MathTex(r"VAD^* = 0.78", font_size=14)
        final_vad_value_text.move_to(final_vad_center)

        # Wait a moment before starting the transformation
        self.wait(1.0)

        # Animate the transformation of Final VAD to Final VAD = 0.80
        self.play(
            Transform(final_vad_text, final_vad_value_text),
            run_time=1.0
        )

        self.wait(1.0)

        # Create a tracker for the BP box
        bp_tracker = ValueTracker(sas_tracker.get_value())  # Set to same value as SAS tracker for synchronization

        # Create a moving gradient outline for the BP box
        bp_outline = create_moving_outline(brevity_box, bp_tracker)

        # Add the outline to the scene
        self.add(bp_outline)

        # Update the updater function to include the BP box
        self.updaters = []

        def update_with_bp_tracker(dt):
            # Base speed
            speed = dt * 0.3
            
            # All existing animation trackers - keep them in sync
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            bp_tracker.increment_value(speed)  # Add BP tracker to the same group as SAS/CAS/NAS
            
            # Formula boxes
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)
            scaled_sas_tracker.increment_value(speed)
            
            # All glow effects
            result_tracker.increment_value(dt * 0.4)
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)
            vad_star2_tracker.increment_value(dt * 0.4)
            nas_formula_result_tracker.increment_value(dt * 0.4)
            final_vad_tracker.increment_value(dt * 0.4)

        # Add the updated tracker
        self.add_updater(update_with_bp_tracker)

        # Wait a moment before starting the transformation
        self.wait(1.0)

        # Create a tracker for the VAD* - (1-BP) > 0 box
        vad_bp_tracker = ValueTracker(vad_star_tracker.get_value())  # Start synchronized with VAD* tracker

        # Create moving gradient outline for the VAD* - (1-BP) > 0 box
        vad_bp_outline = create_moving_outline(vad_bp_box, vad_bp_tracker)

        # Add the outline to the scene
        self.add(vad_bp_outline)

        # Update the updater function to include the VAD* - (1-BP) > 0 box
        self.updaters = []

        def update_with_vad_bp_tracker(dt):
            # Base speed
            speed = dt * 0.3
            
            # All existing animation trackers - keep them in sync
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            bp_tracker.increment_value(speed)
            
            # Formula boxes
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)
            scaled_sas_tracker.increment_value(speed)
            vad_bp_tracker.increment_value(speed)  # Add VAD* - (1-BP) > 0 box tracker
            
            # All glow effects
            result_tracker.increment_value(dt * 0.4)
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)
            vad_star2_tracker.increment_value(dt * 0.4)
            nas_formula_result_tracker.increment_value(dt * 0.4)
            final_vad_tracker.increment_value(dt * 0.4)

        # Add the updated tracker
        self.add_updater(update_with_vad_bp_tracker)

        # Wait a moment before starting the transformation
        self.wait(1.0)

        # Get original position and size of text for replacement animations
        original_center = vad_bp_text.get_center()
        original_height = vad_bp_text.height

        # Create text with substituted values - first transformation
        substituted_text = MathTex(
            r"0.78", r" - (1 - ", r"0.85", r") > 0",
            font_size=14
        )
        # Color the numbers
        substituted_text[0].set_color(RED_A)
        substituted_text[2].set_color(RED_A)
        substituted_text.move_to(original_center)

        # Ensure same height as original
        height_ratio = original_height / substituted_text.height
        substituted_text.scale(height_ratio)

        # Animate the text transformation
        self.play(
            Transform(vad_bp_text, substituted_text),
            run_time=1.0
        )
        self.wait(0.7)

        # Create simplified result "0.60 > 0" with consistent styling
        simplified_text = MathTex(
            r"0.60", r" > 0",
            font_size=14
        )
        simplified_text[0].set_color(RED_A)
        simplified_text.move_to(original_center)

        # Ensure same height
        height_ratio = original_height / simplified_text.height
        simplified_text.scale(height_ratio)

        # Animate the simplification
        self.play(
            Transform(vad_bp_text, simplified_text),
            run_time=1.0
        )
        self.wait(1.0)

        # Now animate the VAD* - (1-BP) / BP formula with values
        # First get a reference to the formula
        vad_bp_formula = vad_bp_formula_1  # Reference to the existing formula object

        # Get original position and size for replacement animations
        formula_center = vad_bp_formula.get_center()
        formula_height = vad_bp_formula.height

        # Create text with substituted values
        substituted_formula = MathTex(
            r"\frac{0.60}{0.85}",
            font_size=16
        )
        substituted_formula.move_to(formula_center)

        # Ensure same height as original
        height_ratio = formula_height / substituted_formula.height
        substituted_formula.scale(height_ratio)

        # Animate the text transformation
        self.play(
            Transform(vad_bp_formula, substituted_formula),
            run_time=1.0
        )
        self.wait(0.7)

        # Create final result "0.71" with appropriate sizing
        final_bp_formula = MathTex(
            r"0.70",
            font_size=16
        )
        final_bp_formula.move_to(formula_center)

        # Ensure same height with appropriate scaling factor
        height_ratio = formula_height / final_bp_formula.height * 0.38  # Match previous scaling factor
        final_bp_formula.scale(height_ratio)

        # Animate the simplification
        self.play(
            Transform(vad_bp_formula, final_bp_formula),
            run_time=1.0
        )
        self.wait(0.5)

        # Add the glowing circle effect around the result
        # Create a tracker for the glowing effect - synchronized with other result glows
        vad_bp_formula_tracker = ValueTracker(formula_result_tracker.get_value())

        # Create the glowing effect for the result
        bp_formula_result_glow = create_result_glow(final_bp_formula, vad_bp_formula_tracker)

        # Add the glow behind the text
        self.add(bp_formula_result_glow)

        # Update the updater function to include this new glow effect
        self.updaters = []

        def update_all_final_trackers(dt):
            # Base trackers
            speed = dt * 0.3
            
            # All existing animation trackers
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            bp_tracker.increment_value(speed)
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)
            scaled_sas_tracker.increment_value(speed)
            vad_bp_tracker.increment_value(speed)
            
            # All glow effects
            result_tracker.increment_value(dt * 0.4)
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)
            vad_star2_tracker.increment_value(dt * 0.4)
            nas_formula_result_tracker.increment_value(dt * 0.4)
            final_vad_tracker.increment_value(dt * 0.4)
            vad_bp_formula_tracker.increment_value(dt * 0.4)  # Add new tracker

        # Add the updated tracker
        self.add_updater(update_all_final_trackers)

        # Add a subtle pulsing effect to the result text - matching previous ones
        self.play(
            final_bp_formula.animate.set_color(GOLD),  # Change color to gold
            run_time=0.7
        )
        self.play(
            final_bp_formula.animate.scale(1.1),  # Slightly increase size
            run_time=0.5
        )
        self.play(
            final_bp_formula.animate.scale(1/1.1),  # Return to original size
            run_time=0.5
        )

        # Final wait to show the complete animation
        self.wait(1.0)

        # Create a tracker for the Final VAD box
        final_result_vad_tracker = ValueTracker(vad_bp_formula_tracker.get_value())  # Sync with previous trackers

        # Create moving gradient outline for the Final VAD box
        final_result_vad_outline = create_moving_outline(vad_final_box, final_result_vad_tracker)

        # Add the outline to the scene
        self.add(final_result_vad_outline)

        # Update the updater function to include this box
        self.updaters = []

        def update_with_final_vad_tracker(dt):
            # Base speed
            speed = dt * 0.3
            
            # All existing animation trackers
            sas_tracker.increment_value(speed)
            cas_tracker.increment_value(speed)
            nas_tracker.increment_value(speed)
            bp_tracker.increment_value(speed)
            formula_tracker.increment_value(speed)
            ssas_nas_tracker.increment_value(speed)
            ssas_nas_test_tracker.increment_value(speed)
            nas_ssas_tracker.increment_value(speed)
            scaled_sas_tracker.increment_value(speed)
            vad_bp_tracker.increment_value(speed)
            
            # All glow effects
            result_tracker.increment_value(dt * 0.4)
            formula_result_tracker.increment_value(dt * 0.4)
            vad_star_tracker.increment_value(dt * 0.4)
            vad_star2_tracker.increment_value(dt * 0.4)
            nas_formula_result_tracker.increment_value(dt * 0.4)
            final_vad_tracker.increment_value(dt * 0.4)
            vad_bp_formula_tracker.increment_value(dt * 0.4)
            final_result_vad_tracker.increment_value(dt * 0.4)  # Add new tracker

        # Add the updated tracker
        self.add_updater(update_with_final_vad_tracker)

        # Get the center position of the Final VAD box and original dimensions
        final_vad_center = vad_final_text.get_center()
        original_height = vad_final_text.height

        # Create new text "Final VAD = 0.70" with RED_A color
        final_vad_result_text = Tex("Final VAD = 0.70", font_size=16)
        final_vad_result_text.set_color(RED_A)  # Set to RED_A color as requested
        final_vad_result_text.move_to(final_vad_center)

        # Ensure consistent sizing with the original
        height_ratio = original_height / final_vad_result_text.height
        final_vad_result_text.scale(height_ratio)

        # Wait a moment before starting the transformation
        self.wait(1.0)

        # Animate the transformation
        self.play(
            Transform(vad_final_text, final_vad_result_text),
            run_time=1.0
        )

        # Final wait to show the completed animation
        self.wait(9.0)