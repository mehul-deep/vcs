"""
Block Matching Algorithm 2.1 (BMA 2.1) Animation

This Manim animation visualizes an enhanced version of the Block Matching Algorithm 
for text narrative alignment, specifically implementing Case 2 (REF vs REF with Brevity).
This version demonstrates brevity-aware text comparison with enhanced visual effects.

The animation demonstrates:
1. Enhanced text block visualization with sophisticated styling
2. Case 2 implementation: REF vs REF with brevity considerations
3. Advanced visual effects including indicate animations and flash effects
4. Interactive paragraph displays with improved color schemes
5. Brevity-aware narrative line and mapping window techniques
6. Enhanced animation timing and visual feedback

Author: Mehul Deep
Date: 07/15/2025
Framework: Manim Community v0.19.0

Usage:
    python -m manim -pql --disable_caching BMA_Case2.py FullConceptAnimation
"""

from manim import (  # type: ignore
    # Core scene and animation classes
    Scene, Text, Underline, Create, Write, VGroup,
    
    # Geometric objects
    Arrow, Triangle, Line, Brace, Rectangle, RoundedRectangle,
    SurroundingRectangle, DashedVMobject, Square, Polygon, Dot, Point,
    
    # Text and paragraph objects
    Paragraph,
    
    # Animation functions
    GrowArrow, DrawBorderThenFill, GrowFromCenter, FadeIn, FadeOut,
    Transform, LaggedStart, ReplacementTransform, AnimationGroup,
    Indicate, there_and_back, ScaleInPlace, Flash,
    
    # Colors
    BLUE_E, GREEN_E, GREEN, ORANGE, RED, BLUE, YELLOW, LIGHT_PINK,
    WHITE, GREY, BLACK, DARK_BLUE, MAROON_B, PURPLE, GOLD,
    
    # Positioning and constants
    ORIGIN, UP, LEFT, RIGHT, DOWN, PI, DEGREES,
    
    # Text formatting
    ITALIC, BOLD,
    
    # Other utilities
    CurvedArrow
)

class FullConceptAnimation(Scene):
    """
    Main animation class for visualizing Block Matching Algorithm 2.1 (BMA 2.1).
    
    This enhanced version demonstrates narrative line and mapping window concepts
    with brevity considerations, implementing Case 2 (REF vs REF with Brevity)
    and featuring advanced visual effects and animations.
    """

    def construct(self):
        """Main animation sequence orchestrating all BMA 2.1 visualization components."""
        # ================== TITLE AND HEADING SETUP ==================
        # Create and animate the main title
        title = Text("Narrative Line and Mapping Window", font_size=25).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(0.5)

        # Move title to top edge for optimal screen space utilization
        self.play(title.animate.to_edge(UP*0.1))
        self.wait(0.5)

        # Add underline for enhanced visual emphasis
        underline = Underline(title)
        self.play(Create(underline))
        self.wait(0.5)
 
        # Group title and underline, then shift to left for case specification
        group_title = VGroup(title, underline)
        self.play(group_title.animate.to_edge(LEFT*1.8))
        self.wait(0.5)

        # Add Case 2 specification with brevity emphasis
        case_text = Text(": Case 2 (REF vs REF with Brevity)", font_size=25)
        case_text.next_to(title, RIGHT, buff=0.2)
        self.play(Write(case_text))
        self.wait(0.5)

        # Create complete title group and update underline span
        full_title = VGroup(title, case_text)
        new_underline = Underline(full_title)
        self.play(Transform(underline, new_underline))
        self.wait(0.5)

        # ================== ENHANCED TEXT BLOCK CREATION ==================
        # Create reference and generated text blocks with sophisticated styling
        # Reference text block with enhanced styling
        reference_box = Rectangle(
            width=3.0, height=3.6,
            stroke_color=WHITE,
            stroke_width=2,               # Enhanced stroke width for better visibility
            fill_color=BLUE_E,           # Blue background for reference text
            fill_opacity=0.4             # Semi-transparent fill
        )
        reference_label = Text("Reference", font_size=24, color=WHITE)
        reference_label.next_to(reference_box, UP, buff=0.2)

        # Reference text content - detailed market scene narrative
        reference_lines = [
            "The old market bell rings, starting", 
            "a busy market. Vendors open their",
            "bright stalls in the busy square,", 
            "while the smell of fresh bread fills", 
            "the air. A young seller shouts out", 
            "good deals as curious people gather",
            "around. The steady ring of the bell", 
            "sets the pace for the day. A wise", 
            "old vendor stops by his stall", 
            "giving advice to those who pass by.",
            "As the market gets busy, the bell",
            "rings again at midday, reminding",
            "everyone of the community spirit.", 
            "A light rain briefly slows the", 
            "crowd, but everyone's spirit stays", 
            "strong. Local storytellers tell simple", 
            "tales that catch everyone's attention.",
            "As evening comes, the old bell rings", 
            "one last time, perfectly echoing the", 
            "start of the day."
        ]
        reference_paragraph = Paragraph(
            *reference_lines,
            alignment="LEFT",
            line_spacing=0.5,
            font_size=20,
            color=WHITE
        )
        # Configure paragraph layout and positioning
        reference_paragraph.set_width(reference_box.get_width() - 0.2)
        reference_paragraph.move_to(reference_box.get_center())
        reference_group = VGroup(reference_box, reference_label, reference_paragraph)
        
        # Generated text block - identical to reference for Case 2 (REF vs REF with Brevity)
        generated_box = Rectangle(
            width=3.0, height=3.6,
            stroke_color=WHITE,
            stroke_width=2,               # Consistent styling with reference box
            fill_color=BLUE_E,           # Same blue background for REF vs REF comparison
            fill_opacity=0.4             # Matching transparency
        )
        # Note: Label shows "Reference" since this is Case 2 (REF vs REF)
        generated_label = Text("Reference", font_size=24, color=WHITE)
        generated_label.next_to(generated_box, UP, buff=0.2)
        
        # Generated content - identical to reference for brevity demonstration
        generated_lines = [
            "The old market bell rings, starting", 
            "a busy market. Vendors open their",
            "bright stalls in the busy square,", 
            "while the smell of fresh bread fills", 
            "the air. A young seller shouts out", 
            "good deals as curious people gather",
            "around. The steady ring of the bell", 
            "sets the pace for the day. A wise", 
            "old vendor stops by his stall", 
            "giving advice to those who pass by.",
            "As the market gets busy, the bell",
            "rings again at midday, reminding",
            "everyone of the community spirit.", 
            "A light rain briefly slows the", 
            "crowd, but everyone's spirit stays", 
            "strong. Local storytellers tell simple", 
            "tales that catch everyone's attention.",
            "As evening comes, the old bell rings", 
            "one last time, perfectly echoing the", 
            "start of the day."
        ]
        generated_paragraph = Paragraph(
            *generated_lines,
            alignment="LEFT",
            line_spacing=0.5,
            font_size=10,
            color=WHITE
        )
        generated_paragraph.set_width(generated_box.get_width() - 0.2)
        generated_paragraph.move_to(generated_box.get_center())
        generated_group = VGroup(generated_box, generated_label, generated_paragraph)

        # Position the boxes with more dynamic placement
        generated_group.next_to(reference_group, DOWN, buff=0.5)

        # Combine & shift everything up from the start
        main_boxes = VGroup(reference_group, generated_group).scale(0.7)
        main_boxes.to_edge(LEFT, buff=1)
        main_boxes.shift(UP * 2)

        # Animate the fade-in with more sophisticated entrance
        self.play(
            LaggedStart(
                FadeIn(reference_box, scale=1.2), 
                FadeIn(reference_label, scale=1.1), 
                FadeIn(reference_paragraph, lag_ratio=0.2),
                FadeIn(generated_box, scale=1.2),
                FadeIn(generated_label, scale=1.1), 
                FadeIn(generated_paragraph, lag_ratio=0.2),
                lag_ratio=0.3
            )
        )
        self.wait(0.5)

        # ================== ENHANCED EXPLANATORY TEXT SYSTEM ==================
        # Create reusable function for generating formatted text groups with headers
        def create_text_group(header_text, explanation_lines, header_color=ORANGE):
            """
            Creates a formatted text group with header, underline, and explanation content.
            
            Args:
                header_text: Title text (e.g., "WHAT?", "WHY?", "HOW?")
                explanation_lines: List of explanation text lines
                header_color: Color for header and underline (default: ORANGE)
                
            Returns:
                VGroup containing formatted header and explanation text
            """
            explanation_text = Paragraph(
                *explanation_lines,
                alignment="LEFT",
                line_spacing=0.8,
                font_size=16,
                color=WHITE
            )

            text_header = Text(header_text, font_size=18, color=header_color)
            underline = Line(LEFT, RIGHT).set_width(text_header.get_width())
            underline.next_to(text_header, DOWN, buff=0.05)
            underline.set_color(header_color)

            text_group = VGroup(text_header, underline, explanation_text)
            text_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            
            return text_group

        # Create text groups with more precise positioning
        text_group1 = create_text_group(
            "WHAT?", 
            [
                "\u201CTo clearly understand the idea of narrative line and mapping window,", 
                "let's compare the reference description with itself—instead of comparing", 
                "it to a generated one.\u201D"
            ]
        )
        text_group2 = create_text_group(
            "WHY?", 
            [
                "\u201CWe're exploring what happens when two identical", 
                "stories or descriptions are compared: this is our ideal scenario.\u201D"
            ]
        )

        # Positioning with more precise alignment
        buffer = 0.8
        text_group1.next_to(reference_box, RIGHT, buff=buffer)
        text_group1.shift(UP * 0.05)

        text_group2.next_to(generated_box, RIGHT, buff=buffer)
        text_group2.shift(UP * 0.05)
        text_group2.align_to(text_group1, LEFT)

        # Animate text groups with more dynamic entrances
        for text_group in [text_group1, text_group2]:
            # Split animation into parts for more engaging entrance
            self.play(
                Write(text_group[0], run_time=0.5),  # Header
                Create(text_group[1], run_time=0.5)  # Underline
            )
            self.play(
                Write(text_group[2], run_time=1.5)  # Explanation text
            )
            self.wait(0.5)

        # Final fade out with a more dynamic exit
        self.play(
            FadeOut(text_group1, shift=UP),
            FadeOut(text_group2, shift=UP),
        )
        self.wait()

        # Create the Brevity text and arrow
        brevity_text = Text("Brevity", font_size=18, color=WHITE)
        brevity_text.next_to(generated_box, RIGHT, buff=0.6)
        
        # Arrow from Generated box to Brevity text with more dynamic styling
        arrow_to_brevity = Arrow(
            start=generated_box.get_right(),
            end=brevity_text.get_left(),
            buff=0.1,
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=12.0,
            color=YELLOW,
            stroke_width=15,
            fill_opacity=1,
            stroke_opacity=0.8
        )
        
        # Create L-shaped arrow from Brevity to Generated box with more complex path
        start_point = brevity_text.get_top() + UP * 0.1
        mid_point = [start_point[0], start_point[1] + 0.3, 0]
        end_point = [generated_box.get_right()[0], mid_point[1], 0]
        
        # Vertical line from Brevity to mid-point with consistent GOLD color
        line_vertical = Line(
            start=start_point,
            end=mid_point,
            stroke_color=YELLOW,
            stroke_width=5,
            stroke_opacity=0.7,
            buff=0
        )
        
        # Horizontal arrow from mid-point to Generated box with consistent GOLD color
        arrow_horizontal = Arrow(
            start=mid_point,
            end=end_point,
            stroke_color=YELLOW,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=3.0,
            fill_opacity=0.9,
            tip_length=0.2,
            buff=0
        )
        
        # Group the L-shaped components
        l_arrow_brevity = VGroup(line_vertical, arrow_horizontal)
        
        # Animate the appearance of Brevity text and arrows with more engaging effects
        self.play(
            LaggedStart(
                Write(brevity_text, run_time=0.8),
                GrowArrow(arrow_to_brevity),
             
            )
        )
        self.wait(0.5)
        
        # Create L-shaped arrow with a more dynamic entrance
        self.play(
            AnimationGroup(
                Create(line_vertical, run_time=0.7),
                Create(arrow_horizontal, run_time=0.7),
                # Add a subtle indication effect to the generated box
                Indicate(generated_box, scale_factor=1.1, color=GREEN_E)
            )
        )
        self.wait(0.5)


        # Step 3: Create the Brevity box in the Generated position
        # First, fade out the generated box with a more interesting effect
        self.play(
            FadeOut(generated_group, scale=1.2),
            # Add a brief flash effect
            # Flash(generated_group.get_center(), color=RED, flash_radius=0.5)
        )
        self.wait(0.5)

      # Capture the final scaled dimensions of the reference box
        # Note: main_boxes is scaled to 0.7 and shifted
        ref_width = reference_box.width * 1.43
        ref_height = reference_box.height * 1.53

        # Create a new box that matches the final scaled reference box
        brevity_box = Rectangle(
            width=ref_width,
            height=ref_height,
            stroke_color=WHITE,
            stroke_width=2,
            fill_color=GREEN_E,
            fill_opacity=0.4
        )
        brevity_label = Text("Brevity", font_size=24, color=WHITE)
        brevity_label.next_to(brevity_box, UP, buff=0.1)
        
        # Using the brevity content
        brevity_lines = [
            "The old market bell signals vendors to",
            "open stalls amid fresh bread aromas.",
            "A young seller calls out deals, drawing",
            "curious onlookers as the bell sets the",
            "day's pace. A wise old vendor advises",
            "passersby when the midday bell rings,",
            "fostering community spirit. A brief",
            "light rain slows the crowd, but local",
            "storytellers share simple tales that",
            "maintain spirits. At evening, the final",
            "bell echoes the day's start."
        ]
        
        brevity_paragraph = Paragraph(
            *brevity_lines,
            alignment="LEFT",
            line_spacing=0.5,
            font_size=14,
        )
        brevity_paragraph.set_width(brevity_box.get_width() - 0.2)
        brevity_paragraph.move_to(brevity_box.get_center())
        brevity_group = VGroup(brevity_box, brevity_label, brevity_paragraph)
        
        # Position it exactly where the previous generated box was
        brevity_group.next_to(reference_group, DOWN, buff=0.5)
        brevity_group.scale(0.7)
        brevity_group.move_to(generated_group.get_center())  # Ensure exact positioning
        
        # Animate the creation of the new brevity box with the same style as before
        self.play(DrawBorderThenFill(brevity_box))
        self.play(Write(brevity_label), FadeIn(brevity_paragraph), run_time=0.5)
        self.wait(1)
        
        # Fade out the Brevity text and arrows with more dynamic exit
        self.play(
            LaggedStart(
                FadeOut(brevity_text, shift=UP, run_time=0.7),
                FadeOut(arrow_to_brevity, run_time=0.7),
                FadeOut(l_arrow_brevity, run_time=0.7),
              
            )
        )
        self.wait(0.5)

        ## Step 4: Arrow from Reference to next step
        arrow_ref = Arrow(
            start=reference_box.get_right(),
            end=reference_box.get_right() + RIGHT * 0.7,
            buff=0.1,
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=12.0,
            color=YELLOW,
            stroke_width=20,
            fill_opacity=1.5,
        )
        arrow_gen = Arrow(
            start=brevity_box.get_right(),
            end=brevity_box.get_right() + RIGHT * 0.7,
            buff=0.1,
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=12.0,
            color=YELLOW,
            stroke_width=20,
            fill_opacity=1.5,
        )

        self.play(
            GrowArrow(arrow_ref),
            GrowArrow(arrow_gen),
            run_time=0.8
        )
        self.wait(0.3)

        # Create three text items with brackets (no box)
        # Create the three text items with gradient color effect
        text1 = Text("Remove Punctuations", font_size=8, color=WHITE)
        text2 = Text("Fix punctuation space", font_size=8, color=WHITE)
        text3 = Text("Expand contraction", font_size=8, color=WHITE)

        # Arrange them vertically
        text_group = VGroup(text1, text2, text3).arrange(DOWN, buff=0.15)

        # Create custom thin brackets using Line objects with gradient effect
        bracket_height = text_group.height + 0.1
        bracket_width = 0.1

        # Left bracket components with gradient
        left_vert = Line(
            start=[0, bracket_height/2, 0],
            end=[0, -bracket_height/2, 0],
            stroke_width=1.5, 
            stroke_color=WHITE
        )
        left_top = Line(
            start=[0, bracket_height/2, 0],
            end=[bracket_width, bracket_height/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        left_bottom = Line(
            start=[0, -bracket_height/2, 0],
            end=[bracket_width, -bracket_height/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        left_bracket = VGroup(left_vert, left_top, left_bottom)

        # Right bracket components with gradient
        right_vert = Line(
            start=[0, bracket_height/2, 0],
            end=[0, -bracket_height/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        right_top = Line(
            start=[0, bracket_height/2, 0],
            end=[-bracket_width, bracket_height/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        right_bottom = Line(
            start=[0, -bracket_height/2, 0],
            end=[-bracket_width, -bracket_height/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        right_bracket = VGroup(right_vert, right_top, right_bottom)

        # Position brackets to fully wrap from top to bottom
        left_bracket.next_to(text_group, LEFT, buff=0.1)
        right_bracket.next_to(text_group, RIGHT, buff=0.1)

        # Group everything together (without the box)
        nv_group_ref = VGroup(text_group, left_bracket, right_bracket)
        nv_group_ref.next_to(arrow_ref.get_end(), RIGHT, buff=0.08)

        # Create the same group for generated text with different gradient colors
        text1_gen = Text("Remove Punctuations", font_size=8, color=WHITE)
        text2_gen = Text("Fix punctuation space", font_size=8, color=WHITE)
        text3_gen = Text("Expand contraction", font_size=8, color=WHITE)

        # Arrange them vertically
        text_group_gen = VGroup(text1_gen, text2_gen, text3_gen).arrange(DOWN, buff=0.15)

        # Create custom thin brackets using Line objects (for generated section) with matching gradient
        bracket_height_gen = text_group_gen.height + 0.1
        bracket_width = 0.1

        # Left bracket components with gradient
        left_vert_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[0, -bracket_height_gen/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        left_top_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[bracket_width, bracket_height_gen/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        left_bottom_gen = Line(
            start=[0, -bracket_height_gen/2, 0],
            end=[bracket_width, -bracket_height_gen/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        left_bracket_gen = VGroup(left_vert_gen, left_top_gen, left_bottom_gen)

        # Right bracket components with gradient
        right_vert_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[0, -bracket_height_gen/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        right_top_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[-bracket_width, bracket_height_gen/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        right_bottom_gen = Line(
            start=[0, -bracket_height_gen/2, 0],
            end=[-bracket_width, -bracket_height_gen/2, 0],
            stroke_width=1.5,
            stroke_color=WHITE
        )
        right_bracket_gen = VGroup(right_vert_gen, right_top_gen, right_bottom_gen)

        # Position brackets to fully wrap from top to bottom
        left_bracket_gen.next_to(text_group_gen, LEFT, buff=0.1)
        right_bracket_gen.next_to(text_group_gen, RIGHT, buff=0.1)

        # Group everything together (without the box)
        nv_group_gen = VGroup(text_group_gen, left_bracket_gen, right_bracket_gen)
        nv_group_gen.next_to(arrow_gen.get_end(), RIGHT, buff=0.08)

        # Enhanced staggered entrance for text groups
        self.play(
            AnimationGroup(
                # Reference group entrance
                LaggedStart(
                    FadeIn(left_bracket, scale=1.2, shift=LEFT*0.2),
                    LaggedStart(
                        FadeIn(text1, shift=UP*0.1),
                        FadeIn(text2),
                        FadeIn(text3, shift=DOWN*0.1),
                        lag_ratio=0.2
                    ),
                    FadeIn(right_bracket, scale=1.2, shift=RIGHT*0.2),
                    lag_ratio=0.3
                ),
                # Generated group entrance
                LaggedStart(
                    FadeIn(left_bracket_gen, scale=1.2, shift=LEFT*0.2),
                    LaggedStart(
                        FadeIn(text1_gen, shift=UP*0.1),
                        FadeIn(text2_gen),
                        FadeIn(text3_gen, shift=DOWN*0.1),
                        lag_ratio=0.2
                    ),
                    FadeIn(right_bracket_gen, scale=1.2, shift=RIGHT*0.2),
                    lag_ratio=0.3
                ),
                lag_ratio=0.3
            ),
            run_time=1.2
        )
        self.wait(0.3)

        # Add horizontal curly braces with enhanced styling
        horiz_brace_ref = Brace(
            text_group,
            direction=DOWN,
            buff=0.1,
            color=WHITE
        )
        horiz_brace_gen = Brace(
            text_group_gen,
            direction=UP,
            buff=0.1,
            color=WHITE
        )

        # Animate braces with pulse effect
        self.play(
            GrowFromCenter(horiz_brace_ref),
            GrowFromCenter(horiz_brace_gen),
            ScaleInPlace(text_group, 1.05, rate_func=there_and_back),
            ScaleInPlace(text_group_gen, 1.05, rate_func=there_and_back),
            run_time=0.8
        )
        self.wait(0.3)

        # -- L-SHAPED ARROWS FROM BRACES TO BOXES - THICKER - with enhanced glow effect
        import string
        no_punct_reference_lines = [
            line.translate(str.maketrans('', '', string.punctuation))
            for line in reference_lines
        ]
        no_punct_brevity_lines = [
            line.translate(str.maketrans('', '', string.punctuation))
            for line in brevity_lines
        ]

        # For reference: arrow from bottom brace to reference box with path animation
        start_bottom_center_1 = horiz_brace_ref.get_center()
        start_bottom_center_1 = start_bottom_center_1 + DOWN * 0.15
        offset1 = start_bottom_center_1 + DOWN * 0.2
        end1_x = reference_box.get_right()[0]
        end1 = [end1_x, offset1[1], 0]

        # Create vertical line with glow effect
        line_vertical_ref = Line(
            start_bottom_center_1, 
            offset1, 
            stroke_color=YELLOW, 
            stroke_width=5,
            buff=0
        )

        # Create horizontal arrow with enhanced styling
        arrow_horizontal_ref = Arrow(
            offset1, 
            end1, 
            stroke_color=YELLOW, 
            stroke_width=10,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=3.0,
            fill_opacity=1,
            tip_length=0.2, 
            buff=0
        )
        l_arrow_ref = VGroup(line_vertical_ref, arrow_horizontal_ref)

        # For generated: arrow from top brace to brevity box with path animation
        start_top_center_2 = horiz_brace_gen.get_center()
        start_top_center_2 = start_top_center_2 + UP * 0.15
        offset2 = start_top_center_2 + UP * 0.2
        end2_x = brevity_box.get_right()[0]
        end2 = [end2_x, offset2[1], 0]

        # Create vertical line with glow effect
        line_vertical_gen = Line(
            start_top_center_2, 
            offset2, 
            stroke_color=YELLOW, 
            stroke_width=5,
            buff=0
        )

        # Create horizontal arrow with enhanced styling
        arrow_horizontal_gen = Arrow(
            offset2, 
            end2, 
            stroke_color=YELLOW, 
            stroke_width=10,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=3.0,
            fill_opacity=1,
            tip_length=0.2, 
            buff=0
        )
        l_arrow_gen = VGroup(line_vertical_gen, arrow_horizontal_gen)

        # Animate L-arrows with sequential growth
        self.play(
            AnimationGroup(
                Create(line_vertical_ref),
                Create(arrow_horizontal_ref),
                # Flash(end1, color=YELLOW, line_length=0.2, num_lines=8, flash_radius=0.2),
                # lag_ratio=0.4
            ),
            AnimationGroup(
                Create(line_vertical_gen),
                Create(arrow_horizontal_gen),
                # Flash(end2, color=YELLOW, line_length=0.2, num_lines=8, flash_radius=0.2),
                # lag_ratio=0.4
            ),
            run_time=1.4
        )
        self.wait(0.3)

        # Enhanced transformation to no-punctuation paragraphs with smoother animation
        reference_paragraph_no_punct = Paragraph(
            *no_punct_reference_lines, alignment="LEFT", line_spacing=0.6, font_size=11
        ).move_to(reference_box.get_center())

        # For brevity box, remove punctuation from brevity lines with enhanced styling
        no_punct_brevity_lines = [
            line.translate(str.maketrans('', '', string.punctuation))
            for line in brevity_lines
        ]

        brevity_paragraph_no_punct = Paragraph(
            *no_punct_brevity_lines, alignment="LEFT", line_spacing=0.6, font_size=11 
        ).move_to(brevity_box.get_center())

        # Ensure text fits properly within boxes
        if reference_paragraph_no_punct.get_width() > reference_box.get_width():
            reference_paragraph_no_punct.scale_to_fit_width(reference_box.get_width() * 0.9)
            reference_paragraph_no_punct.move_to(reference_box.get_center())
        if brevity_paragraph_no_punct.get_width() > brevity_box.get_width():
            brevity_paragraph_no_punct.scale_to_fit_width(brevity_box.get_width() * 0.9)
            brevity_paragraph_no_punct.move_to(brevity_box.get_center())

        # Add highlighting effect to punctuation before removal
        highlight_ref = SurroundingRectangle(reference_paragraph, buff=0.05, color=RED, stroke_width=1.5, stroke_opacity=0.7)
        highlight_brevity = SurroundingRectangle(brevity_paragraph, buff=0.05, color=RED, stroke_width=1.5, stroke_opacity=0.7)

        # Show highlight briefly before transformation
        self.play(
            Create(highlight_ref),
            Create(highlight_brevity),
            run_time=0.5
        )
        self.wait(0.2)
        self.play(
            FadeOut(highlight_ref),
            FadeOut(highlight_brevity),
            run_time=0.3
        )

        # Transform text with ripple effect
        self.play(
            LaggedStart(
                *[ReplacementTransform(old_line, new_line, path_arc=20*DEGREES)
                for old_line, new_line in zip(reference_paragraph, reference_paragraph_no_punct)],
                lag_ratio=0.08, run_time=1.5
            ),
            LaggedStart(
                *[ReplacementTransform(old_line, new_line, path_arc=20*DEGREES)
                for old_line, new_line in zip(brevity_paragraph, brevity_paragraph_no_punct)],
                lag_ratio=0.08, run_time=1.5
            )
        )
        self.wait(0.5)

         # --- Create & place SAT boxes (invisible initially) ---
        sat_box_ref = RoundedRectangle(width=0.6, height=0.3, corner_radius=0.1,
                                       stroke_color=WHITE, fill_color=BLACK, fill_opacity=0.5)
        sat_ref_text = Text("SAT", font_size=10).move_to(sat_box_ref.get_center())
        sat_group_ref = VGroup(sat_box_ref, sat_ref_text)
        sat_group_ref.next_to(nv_group_ref, RIGHT, buff=0.55)
        sat_group_ref.set_opacity(0)
        self.add(sat_group_ref) 

        sat_box_gen = RoundedRectangle(width=0.6, height=0.3, corner_radius=0.1,
                                       stroke_color=WHITE, fill_color=BLACK, fill_opacity=0.5)
        sat_gen_text = Text("SAT", font_size=10).move_to(sat_box_gen.get_center())
        sat_group_gen = VGroup(sat_box_gen, sat_gen_text)
        sat_group_gen.next_to(nv_group_gen, RIGHT, buff=0.55)
        sat_group_gen.set_opacity(0)
        self.add(sat_group_gen)


        # Short arrows from Symbol-Filter to the (invisible) SAT boxes - THICKER
        arrow_sat_ref = Arrow(
            start=nv_group_ref.get_edge_center(RIGHT),
            end=sat_group_ref.get_edge_center(LEFT),
            buff=0.05, 
            max_tip_length_to_length_ratio=0.35,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=12.0,   # Added for thicker stroke
            color=YELLOW,                        # Changed from stroke_color to color
            stroke_width=20,                     # Increased thickness
            fill_opacity=1.5,                      # Changed to filled arrow
            tip_length=0.2
        )
        arrow_sat_gen = Arrow(
            start=nv_group_gen.get_edge_center(RIGHT),
            end=sat_group_gen.get_edge_center(LEFT),
            buff=0.05, 
            max_tip_length_to_length_ratio=0.35,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=12.0,   # Added for thicker stroke
            color=YELLOW,                        # Changed from stroke_color to color
            stroke_width=20,                     # Increased thickness
            fill_opacity=1.5,                      # Changed to filled arrow
            tip_length=0.2
        )

        # Animate these arrows first
        self.play(GrowArrow(arrow_sat_ref), GrowArrow(arrow_sat_gen), run_time=1.0)
        self.wait(0.5)

      

        # Fade in the SAT boxes
        self.play(sat_group_ref.animate.set_opacity(1), sat_group_gen.animate.set_opacity(1), run_time=0.7)
        self.wait(0.5)

        # Final arrows with enhanced styling
        arrow_from_sat_ref = Arrow(
            start=sat_group_ref.get_edge_center(RIGHT),
            end=sat_group_ref.get_edge_center(RIGHT) + RIGHT * 0.55,
            buff=0.05, 
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=12.0,
            color=YELLOW,
            stroke_width=20,
            fill_opacity=1.5,
            tip_length=0.2
        )
        arrow_from_sat_gen = Arrow(
            start=sat_group_gen.get_edge_center(RIGHT),
            end=sat_group_gen.get_edge_center(RIGHT) + RIGHT * 0.55,
            buff=0.05, 
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=12.0,
            color=YELLOW,
            stroke_width=20,
            fill_opacity=1.5,
            tip_length=0.2
        )
        # Final animation sequence
        self.play(
            GrowArrow(arrow_from_sat_ref),
        )
        self.wait(0.3)

         # Lines for top arrow with numbered boxes instead of [#]
        lines_top_content = [
            "The old market bell rings starting a busy market",
            "Vendors open their bright stalls in the busy square while the smell of fresh bread fills the air",
            "A young seller shouts out good deals as curious people gather around",
            "The steady ring of the bell sets the pace for the day",
            "A wise old vendor stops by his stall giving advice to those who pass by",
            "As the market gets busy the bell rings again at midday reminding everyone of the community spirit",
            "A light rain briefly slows the crowd but everyone is spirit stays strong",
            "Local storytellers tell simple tales that catch everyone is attention",
            "As evening comes the old bell rings one last time perfectly echoing the start of the day"
        ]
        
        arrow_end_top = arrow_from_sat_ref.get_end()
        lines_top_mobs = []  # store line mobjects in a list
        
        # Shift factors - adjust these values to control positioning
        horizontal_shift = 0.2  # Positive value shifts right
        vertical_shift = 0.2    # Positive value shifts up
        
        # Create segment boxes first (but don't display yet)
        segment_boxes_top = []
        for i, line_content in enumerate(lines_top_content):
            # Create the numbered square box
            box_size = 0.2
            number_box = Square(
                side_length=box_size,
                color=WHITE,
                fill_color=BLUE_E,
                fill_opacity=0.5,
                stroke_width=1
            )
            
            # Position the number box
            left_x = arrow_end_top[0] + 0.2 + horizontal_shift
            line_y = arrow_end_top[1] + 1.0 - i * 0.3 + vertical_shift
            number_box.move_to([left_x + box_size/2, line_y, 0])
            segment_boxes_top.append(number_box)
        
        # Create a VGroup of all boxes for the brace to target
        boxes_group_top = VGroup(*segment_boxes_top)
        
        # Create the brace - position it to match your image (left side of boxes)
        left_brace = Brace(
            boxes_group_top,
            direction=LEFT,
            buff=0.05,
            color=WHITE
        )
        
        # Show the brace first, before any segments
        self.play(Create(left_brace), run_time=0.5)
        self.wait(0.2)

       # Now display each segment
        for i, line_content in enumerate(lines_top_content):
            # Get the already positioned box
            number_box = segment_boxes_top[i]
            
            # Add the number inside the box
            number_text = Text(f"{i+1}", font_size=10, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            # Create the text content (without the [#] prefix)
            line_text = Text(f' "{line_content}"', font_size=8.5) #Suppose to be 7.8
            
            # Position the text to the right of the number box with increased buffer
            line_text.next_to(number_box, RIGHT, buff=0.2)  # Increased buffer from 0.1 to 0.3
            
            # Maintain left alignment but with a horizontal offset
            line_text.align_to(number_box, LEFT)
            line_text.shift(RIGHT * 0.35)  # Additional shift to the right
            
            # Vertically center the text with the box
            line_text_center = line_text.get_center()
            number_box_center = number_box.get_center()
            vertical_shift = number_box_center[1] - line_text_center[1]
            line_text.shift(DOWN * vertical_shift)
            
            # Animation - display both the box and its content
            self.play(FadeIn(number_box), FadeIn(number_text), Write(line_text), run_time=0.2)
            self.wait(0.1)
            
            # Group them for easier handling
            full_line = VGroup(number_box, number_text, line_text)
            lines_top_mobs.append(full_line)
        

        self.wait(0.2)
        
        # Now animate the bottom arrow with the same effects as the top arrow
        self.play(
            GrowArrow(arrow_from_sat_gen),
        )
        self.wait(0.3)
       

        # Lines for bottom arrow with numbered boxes instead of [#]
        lines_bottom_content = [
            "The old market bell signals vendors to open stalls amid fresh bread aromas",
            "A young seller calls out deals drawing curious onlookers as the bell sets the day 's pace",
            "A wise old vendor advises passersby when the midday bell rings fostering community spirit",
            "A brief light rain slows the crowd but local storytellers share simple tales that maintain spirits",
            "At evening the final bell echoes the day 's start"
        ]

        arrow_end_bottom = arrow_from_sat_gen.get_end()
        lines_bottom_mobs = []  # store line mobjects in a list

        # Shift factors - use the same values as for the top section
        horizontal_shift = 0.2  # Positive value shifts right

        # This controls the initial position - adjust to center the group on the arrow
        vertical_offset = 0.15  # Adjust this value to center the brace on the arrow

        # Calculate total height needed for the segments (for centering purposes)
        total_segments = len(lines_bottom_content)
        segment_spacing = 0.3
        total_height = total_segments * segment_spacing

        # Create segment boxes first (but don't display yet)
        segment_boxes_bottom = []

        for j, chunk_content in enumerate(lines_bottom_content):
            # Create the numbered square box
            box_size = 0.2
            number_box = Square(
                side_length=box_size,
                color=WHITE,
                fill_color=BLUE_E,
                fill_opacity=0.5,
                stroke_width=1
            )
            
            # Position the number box - centered on the arrow
            left_x = arrow_end_bottom[0] + 0.2 + horizontal_shift
            # - vertical_offset adjusts the entire group
            line_y = arrow_end_bottom[1] + (total_height/2) - j * segment_spacing - vertical_offset
            
            number_box.move_to([left_x + box_size/2, line_y, 0])
            segment_boxes_bottom.append(number_box)

        # Create a VGroup of all boxes for the brace to target
        boxes_group_bottom = VGroup(*segment_boxes_bottom)

        # Create the brace - position it to match your image (left side of boxes)
        left_brace_bottom = Brace(
            boxes_group_bottom,
            direction=LEFT,
            buff=0.05,
            color=WHITE
        )

        # Show the brace first, before any segments
        self.play(Create(left_brace_bottom), run_time=0.5)
        self.wait(0.2)

        # Now display each segment
        for j, chunk_content in enumerate(lines_bottom_content):
            # Get the already positioned box
            number_box = segment_boxes_bottom[j]
            
            # Add the number inside the box
            number_text = Text(f"{j+1}", font_size=10, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            # Create the text content (without the [#] prefix)
            chunk_text = Text(f' "{chunk_content}"', font_size=8.5)
            
            # Position the text to the right of the number box with increased buffer
            chunk_text.next_to(number_box, RIGHT, buff=0.2)
            
            # Maintain left alignment but with a horizontal offset
            chunk_text.align_to(number_box, LEFT)
            chunk_text.shift(RIGHT * 0.35)
            
            # Vertically center the text with the box
            chunk_text_center = chunk_text.get_center()
            number_box_center = number_box.get_center()
            vertical_shift = number_box_center[1] - chunk_text_center[1]
            chunk_text.shift(DOWN * vertical_shift)
            
            # Animation - display both the box and its content
            self.play(FadeIn(number_box), FadeIn(number_text), Write(chunk_text), run_time=0.2)
            self.wait(0.1)
            
            # Group them for easier handling
            full_line = VGroup(number_box, number_text, chunk_text)
            lines_bottom_mobs.append(full_line)

        self.wait(1.0)

        # -----------------------------------------------------------------------
        #  FADE OUT EVERYTHING EXCEPT THE TITLE, UNDERLINE, AND THE RIGHT LINES
        # -----------------------------------------------------------------------
        # Put the top/bottom lines into VGroups so we can keep them
        lines_top_vg = VGroup(*lines_top_mobs)
        lines_bottom_vg = VGroup(*lines_bottom_mobs)

        # Fix for issue 2: Include the correct elements in the fade-out
        # All the stuff we want to fade out
        fade_out_list = [
            reference_box, reference_label, reference_paragraph_no_punct, brevity_box,
            brevity_label, brevity_paragraph_no_punct,
            # ref_comparison_box, ref_comparison_label, ref_comparison_paragraph_no_punct, 
            arrow_ref, arrow_gen,
            nv_group_ref, nv_group_gen,
            l_arrow_ref, l_arrow_gen,
            sat_group_ref, sat_group_gen,
            arrow_sat_ref, arrow_sat_gen,
            arrow_from_sat_ref, arrow_from_sat_gen,
            horiz_brace_ref, horiz_brace_gen,
        ]

        # Make sure we're fading out the correct items
        self.play(FadeOut(VGroup(*fade_out_list)), run_time=1.5)

        # Add arrows going left from both curly braces with "Chunk size = 1" text
        # For top/reference section - Arrow pointing LEFT
        arrow_from_brace_top = Arrow(
            start=left_brace.get_edge_center(LEFT) + LEFT * 0.1,
            end=left_brace.get_edge_center(LEFT) + LEFT * 1.2,
            buff=0.1,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=7.0,
            color=YELLOW,
            stroke_width=8.5,
            fill_opacity=1
        )
        
        # Position text directly above the arrow line
        chunk_size_text_top = Text("Chunk Size = 1", font_size=8)
        # Calculate position at the middle of the arrow but shifted up
        chunk_size_text_top.move_to(arrow_from_brace_top.get_center() + UP * 0.3)
        
        # For bottom/generated section - Arrow pointing LEFT
        arrow_from_brace_bottom = Arrow(
            start=left_brace_bottom.get_edge_center(LEFT) + LEFT * 0.1,
            end=left_brace_bottom.get_edge_center(LEFT) + LEFT * 1.2,
            buff=0.1,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=7.0,
            color=YELLOW,
            stroke_width=8.5,
            fill_opacity=1
        )
        
        # Position text directly above the arrow line
        chunk_size_text_bottom = Text("Chunk Size = 1", font_size=8)
        # Calculate position at the middle of the arrow but shifted up
        chunk_size_text_bottom.move_to(arrow_from_brace_bottom.get_center() + UP * 0.3)
        
        # Animate the top arrow and text
        self.play(
            GrowArrow(arrow_from_brace_top),
            run_time=0.7
        )
        self.play(
            Write(chunk_size_text_top),
            run_time=0.7
        )
        self.wait(0.5)
        
        # Animate the bottom arrow and text
        self.play(
            GrowArrow(arrow_from_brace_bottom),
            run_time=0.7
        )
        self.play(
            Write(chunk_size_text_bottom),
            run_time=0.7
        )
        self.wait(1.0)

        import numpy as np  # type: ignore

        # 1) Define the Y-axis (9 lines) and X-axis (10 lines).
        y_segments = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ]
        x_segments = [
            "1",
            "2",
            "3",
            "4",
            "5"
        ]

        # 2) Define an anchor point for the L shape (bottom-left corner). it shifts the whole L shaped up and down as required 6.3
        anchor = LEFT * 5.7 + DOWN * 2.6

        # 3) Define how tall and wide the axes should be.
        y_length = 5.0  # vertical axis length
        x_length = 2.8  # horizontal axis length

        heading_x = anchor[0] + x_length / 2
        heading_y = anchor[1] + y_length + 0.4

        # Create the Y-axis (vertical line) from anchor up with thinner stroke
        axis_y_start = anchor
        axis_y_end = anchor + UP * y_length
        y_axis = Line(
            axis_y_start, 
            axis_y_end, 
            stroke_color=WHITE, 
            stroke_width=1  # Changed from 3 to 1 to match grid lines
        )

        # Create the X-axis (horizontal line) from anchor right with thinner stroke
        axis_x_start = anchor
        axis_x_end = anchor + RIGHT * x_length
        x_axis = Line(
            axis_x_start, 
            axis_x_end, 
            stroke_color=WHITE, 
            stroke_width=1  # Changed from 3 to 1 to match grid lines
        )

        # Animate the L-shaped axes
        self.play(Create(y_axis), Create(x_axis), run_time=1.0)
        self.wait(0.5)

        # ---------------------------------------------------------------------
        # 6) Position the Y-axis labels as colored boxes with numbers inside
        # ---------------------------------------------------------------------
        num_y = len(y_segments)
        label_spacing_y = y_length / num_y
        y_labels = VGroup()

        # For Y-axis labels - use RoundedRectangle instead of Square
        for i, seg_text in enumerate(y_segments):
            # Create the colored box with rounded corners
            box_size = 0.45
            number_box = RoundedRectangle(
                width=box_size, 
                height=box_size,
                corner_radius=0.04,  # Controls how rounded the corners are
                color=WHITE,
                fill_color=BLUE_E,  # Use BLUE_E to match the reference box color
                fill_opacity=0.5,
                stroke_width=1
            )
            
            # Position the box
            label_x = axis_y_start[0] - 0.35  # Closer to axis
            label_y = axis_y_start[1] + (i + 0.5) * label_spacing_y
            number_box.move_to([label_x, label_y, 0])
            
            # Add the number inside the box
            number_text = Text(seg_text, font_size=12, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            # Group them for animation
            label_group = VGroup(number_box, number_text)
            y_labels.add(label_group)

        # Animate the Y-axis labels
        self.play(*[FadeIn(m) for m in y_labels], run_time=1.5)
        self.wait(0.5)

        # ---------------------------------------------------------------------
        # 7) Position the X-axis labels as colored boxes with numbers inside
        # ---------------------------------------------------------------------
        num_x = len(x_segments)
        x_axis_length = (axis_x_end - axis_x_start)[0]
        label_spacing_x = x_axis_length / num_x
        x_labels = VGroup()

        for j, seg_text in enumerate(x_segments):
        # Create the colored box with rounded corners
            box_size = 0.45
            number_box = RoundedRectangle(
                width=box_size, 
                height=box_size,
                corner_radius=0.04,  # Controls how rounded the corners are
                color=WHITE,
                fill_color=BLUE_E,  # Use MAROON_B to match the generated box color
                fill_opacity=0.5,
                stroke_width=1
            )
            
            # Position the box
            label_x = axis_x_start[0] + (j + 0.5) * label_spacing_x
            label_y = axis_x_start[1] - 0.35  # Closer to axis
            number_box.move_to([label_x, label_y, 0])
            
            # Add the number inside the box
            number_text = Text(seg_text, font_size=12, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            # Group them for animation
            label_group = VGroup(number_box, number_text)
            x_labels.add(label_group)

        # Animate the X-axis labels
        self.play(*[FadeIn(m) for m in x_labels], run_time=1.5)
        self.wait(1.0)

        # 1) Define the anchor, dx, dy for grid
        anchor_x = axis_x_start[0]  # same as 'anchor' x
        anchor_y = axis_x_start[1]  # same as 'anchor' y

        num_rows = 9
        num_cols = 5
        dx = x_length / num_cols
        dy = y_length / num_rows

        # 3.1) Create the "horizontal" grid lines (for row boundaries)
        grid_lines = VGroup()
        for row_idx in range(num_rows + 1):  # from 0..9
            y_line = anchor_y + row_idx * dy
            line_h = Line(
                [anchor_x, y_line, 0],
                [anchor_x + x_length, y_line, 0],
                stroke_color=WHITE,
                stroke_width=1
            )
            grid_lines.add(line_h)

        # 3.2) Create the "vertical" grid lines (for column boundaries)
        for col_idx in range(num_cols + 1):  # from 0..10
            x_line = anchor_x + col_idx * dx
            line_v = Line(
                [x_line, anchor_y, 0],
                [x_line, anchor_y + y_length, 0],
                stroke_color=WHITE,
                stroke_width=1
            )
            grid_lines.add(line_v)

        # Animate the creation of the entire grid
        self.play(Create(grid_lines), run_time=1.5)
        self.wait(0.5)

        # Create a group of all heatmap elements to shift
        heatmap_elements = VGroup(
            y_axis, x_axis,
            y_labels, x_labels,
            grid_lines
        )

        # Create a group of all the elements to fade out
        elements_to_fade = VGroup(
            lines_top_vg,               # Top segments
            lines_bottom_vg,            # Bottom segments
            left_brace,                 # Top brace
            left_brace_bottom,          # Bottom brace
            arrow_from_brace_top,       # Arrow from top brace
            arrow_from_brace_bottom,    # Arrow from bottom brace
            chunk_size_text_top,        # "Chunk Size = 1" text for top section
            chunk_size_text_bottom,      # "Chunk Size = 1" text for bottom section
        )

        # Fade out all these elements before shifting the heatmap
        self.play(
            FadeOut(elements_to_fade),
            run_time=1.5
        )
        self.wait(0.5)

        # Shift the heatmap to the right 3.5
        shift_right = RIGHT * 2.6  # Adjust this value to control how far right it moves
        self.play(heatmap_elements.animate.shift(shift_right), run_time=1.5)
        self.wait(1.0)

        # Add small colored boxes with numbers to ALL columns 1-10 of the heatmap at once
        all_columns_boxes = VGroup()

        # Loop through all columns 1-10 (indexes 0-9)
        for j in range(num_cols):  # All columns (0 to 9)
            column_boxes = VGroup()
            
            # Loop through all rows in this column
            for i in range(num_rows):  # For each row (0 to 8)
                # Calculate the position for this cell
                cell_x = anchor_x + (j + 0.5) * dx + shift_right[0]  # Center of column + shift
                cell_y = anchor_y + (i + 0.5) * dy  # Center of the cell row
                
                # Box size
                small_box_size = 0.19
                
                # Create the boxes
                first_small_box = RoundedRectangle(
                    width=small_box_size, 
                    height=small_box_size,
                    corner_radius=0.02,
                    color=WHITE,
                    fill_color=BLUE_E,
                    fill_opacity=0.7,
                    stroke_width=0.5
                )
                
                second_small_box = RoundedRectangle(
                    width=small_box_size, 
                    height=small_box_size,
                    corner_radius=0.02,
                    color=WHITE,
                    fill_color=BLUE_E,
                    fill_opacity=0.7,
                    stroke_width=0.5
                )
                
                # Create the paired boxes with minimal gap
                box_pair = VGroup(first_small_box, second_small_box)
                box_pair.arrange(RIGHT, buff=0.05)  # Arrange with minimal gap
                
                # Position the pair at the center of the cell
                box_pair.move_to([cell_x, cell_y, 0])
                
                # Add the numbers inside the boxes
                row_num_text = Text(f"{i+1}", font_size=10, color=WHITE)
                row_num_text.move_to(first_small_box.get_center())
                
                col_num_text = Text(f"{j+1}", font_size=10, color=WHITE)
                col_num_text.move_to(second_small_box.get_center())
                
                # Group the boxes and numbers
                cell_group = VGroup(first_small_box, row_num_text, second_small_box, col_num_text)
                column_boxes.add(cell_group)
            
            # Add this column to the total group
            all_columns_boxes.add(column_boxes)

        # Animate all columns at once with a single animation
        self.play(FadeIn(all_columns_boxes), run_time=1.5)
        self.wait(1.0)

        formula_x = anchor_x + x_length + 6.3  # Move slightly further right
        formula_y = anchor_y + y_length * 0.5  # Upper portion of the heatmap

        # Create larger blue box - increased size by 50%
        ref_box = RoundedRectangle(
            width=small_box_size*1.2,  # Increased from 0.8 to 1.2
            height=small_box_size*1.2,  # Increased from 0.8 to 1.2
            corner_radius=0.03,  # Slightly increased corner radius
            color=WHITE,
            fill_color=BLUE_E,
            fill_opacity=0.7,
            stroke_width=0.8  # Increased stroke width
        )
        ref_element = ref_box

        # Create larger maroon box - increased size by 50%
        gen_box = RoundedRectangle(
            width=small_box_size*1.2,  # Increased from 0.8 to 1.2
            height=small_box_size*1.2,  # Increased from 0.8 to 1.2
            corner_radius=0.03,  # Slightly increased corner radius
            color=WHITE,
            fill_color=BLUE_E,
            fill_opacity=0.7,
            stroke_width=0.8  # Increased stroke width
        )
        gen_element = gen_box

        # Create the first part of the formula - increased font size
        formula_part1 = Text("Cos(θ) = ", font_size=24, color=WHITE)  # Increased from 18 to 24

        # Create the fraction part with the boxes
        formula_numerator = VGroup()
        formula_numerator.add(ref_element.copy())
        formula_numerator.add(Text(" · ", font_size=24, color=WHITE))  # Increased from 18 to 24
        formula_numerator.add(gen_element.copy())
        formula_numerator.arrange(RIGHT, buff=0.15)  # Increased buffer between elements

        formula_denominator = VGroup()
        formula_denominator.add(Text("||", font_size=24, color=WHITE))  # Increased from 18 to 24
        formula_denominator.add(ref_element.copy())
        formula_denominator.add(Text("|| · ||", font_size=24, color=WHITE))  # Increased from 18 to 24
        formula_denominator.add(gen_element.copy())
        formula_denominator.add(Text("||", font_size=24, color=WHITE))  # Increased from 18 to 24
        formula_denominator.arrange(RIGHT, buff=0.15)  # Increased buffer between elements

        # Create the fraction with wider line
        fraction_line = Line(
            LEFT * formula_numerator.get_width()/2, 
            RIGHT * formula_numerator.get_width()/2, 
            color=WHITE,
            stroke_width=2  # Increased stroke width
        )
        formula_numerator.next_to(fraction_line, UP, buff=0.15)  # Increased buffer
        formula_denominator.next_to(fraction_line, DOWN, buff=0.15)  # Increased buffer

        fraction = VGroup(formula_numerator, fraction_line, formula_denominator)

        # Create the opening/closing parentheses - make them match the height of the fraction
        left_big_paren = Text("(", font_size=48, color=WHITE)  # Increased from 32 to 48
        right_big_paren = Text(")", font_size=48, color=WHITE)  # Increased from 32 to 48

        # Make the parentheses tall enough
        left_big_paren.stretch_to_fit_height(fraction.height + 0.3)  # Increased padding
        right_big_paren.stretch_to_fit_height(fraction.height + 0.3)  # Increased padding

        # Position them around the fraction
        left_big_paren.next_to(fraction, LEFT, buff=0.08)  # Increased buffer
        right_big_paren.next_to(fraction, RIGHT, buff=0.08)  # Increased buffer

        # Group the fraction with parentheses
        fraction_with_parens = VGroup(left_big_paren, fraction, right_big_paren)

        # Group the entire first line of the formula
        full_formula_line1 = VGroup(formula_part1, fraction_with_parens)
        full_formula_line1.arrange(RIGHT, buff=0.15)  # Increased buffer
        full_formula_line1.move_to([formula_x, formula_y, 0])

        # Scale the entire formula by 30%
        full_formula_line1.scale(1.0)

        # Animate the appearance of the first line of the formula
        self.play(Write(formula_part1), run_time=0.8)
        self.play(FadeIn(fraction_with_parens), run_time=1.2)
        self.wait(1.0)

        # First fade out all the box pairs from the cells
        self.play(FadeOut(all_columns_boxes), run_time=1.0)
        self.wait(0.5)

        # Define the cosine similarity values from the provided heatmap (9x5 grid)
        cosine_values = [
            # Row 9 [Desc1_Chunk9] (top row in the matrix)
            [0.73, 0.58, 0.53, 0.15, 0.40],
            # Row 8 [Desc1_Chunk8]
            [0.71, 0.40, 0.34, 0.19, 0.19],
            # Row 7 [Desc1_Chunk7]
            [0.24, 0.50, 0.35, 0.18, 0.07],
            # Row 6 [Desc1_Chunk6]
            [0.44, 0.75, 0.44, 0.20, 0.61],
            # Row 5 [Desc1_Chunk5]
            [0.37, 0.30, 0.70, 0.23, 0.10],
            # Row 4 [Desc1_Chunk4]
            [0.48, 0.49, 0.65, 0.26, 0.45],
            # Row 3 [Desc1_Chunk3]
            [0.11, 0.11, 0.14, 0.68, 0.14],
            # Row 2 [Desc1_Chunk2]
            [0.24, 0.24, 0.31, 0.62, 0.17],
            # Row 1 [Desc1_Chunk1] (bottom row in the matrix)
            [0.47, 0.37, 0.49, 0.20, 0.83]
        ]

        # ================== COLOR MAPPING AND HEATMAP VISUALIZATION ==================
        # Define color mapping function for similarity value visualization
        def get_color_for_value(value):
            """
            Maps similarity values to visual colors for heatmap display.
            
            Args:
                value: Float similarity score (0.0 to 1.0)
                
            Returns:
                Color object for the given similarity value
            """
            # Higher values get brighter colors
            if value >= 0.7:
                return WHITE  # Brightest for highest values
            elif value >= 0.5:
                return WHITE  # Bright for high values
            elif value >= 0.3:
                return WHITE  # Medium for medium values
            else:
                return WHITE  # Dark for low values

        # Create cell values column by column
        column_values = []

        # Prepare each column separately
        for j in range(num_cols):  # 0 to 9 (10 columns)
            col_values = VGroup()
            
            for i in range(num_rows):  # 0 to 8 (9 rows)
                # Calculate the position for this cell
                cell_x = anchor_x + (j + 0.5) * dx + shift_right[0]  # Center of column + shift
                cell_y = anchor_y + (i + 0.5) * dy  # Center of the cell row
                
                # Get the value for this cell
                value = cosine_values[i][j]
                
                # Create a text object with the value
                value_text = Text(f"{value:.2f}", font_size=14, color=get_color_for_value(value))
                value_text.move_to([cell_x, cell_y, 0])
                
                # Add the text to the column group
                col_values.add(value_text)
            
            # Add this column to the total group
            column_values.append(col_values)

        # Animate the values appearing column by column
        for j, column in enumerate(column_values):
            self.play(FadeIn(column), run_time=0.5)
            self.wait(0.2)

        self.wait(1.0)

        # CHANGE 1: Only fade out the formula, keep the values
        self.play(
            FadeOut(formula_part1, fraction_with_parens),
            run_time=1.0
        )
        self.wait(0.5)

        # Calculate the position for the brace (note: including the shift that was already applied)
        brace_start_x = anchor_x + shift_right[0]  # Left edge of x-axis (already shifted)
        brace_end_x = anchor_x + x_length + shift_right[0]  # Right edge of x-axis (already shifted)
        brace_y = anchor_y - 0.5  # Below the x-axis labels

        # Create the horizontal curly brace
        x_brace = Brace(
            Line(
                start=[brace_start_x, brace_y, 0],
                end=[brace_end_x, brace_y, 0]
            ),
            direction=DOWN
        )

        brace_text = Text("Column = 5", font_size=16, color=WHITE)
        brace_text.next_to(x_brace, DOWN, buff=0.2)

        brace_group = VGroup(x_brace, brace_text)

        # CHANGE 3: Define the position for the text elements on the right side
        text_x = anchor_x + x_length + 4.1  # Position to the right of the heatmap
        text_start_y = anchor_y + y_length - -0.7  # Start at the top

        # Define the position for the rectangular box on the right side
        right_side_x = anchor_x + x_length + 4.5  # Position to the right of the heatmap
        right_side_y = anchor_y + y_length/2 - 0.2  # Center vertically in the scene

        # Create a standalone rectangular box
        box_width = 5.7  # Width of the box
        box_height = 7.0  # Height of the box

        standalone_box = Rectangle(
            width=box_width,
            height=box_height,
            stroke_color=WHITE,
            stroke_width=2.0,
            fill_color=BLACK,
            fill_opacity=0.1
        )

        # Position the box on the right side
        standalone_box.move_to([right_side_x + box_width/2 - 0.5, right_side_y, 0])

        # Animate the appearance of the box
        self.play(
            Create(standalone_box),
            run_time=1.0
        )
        self.wait(0.3)

        # Create the first heading and text
        heading1 = Text("Goal", font_size=16, color=WHITE)
        heading1.move_to([text_x, text_start_y, 0], aligned_edge=LEFT+UP)

        # Add underline to heading1
        heading1_underline = Underline(heading1, color=WHITE)

        # Create text1 with typing effect
        text1 = Text("Find Best & 2nd Best segment matches (column-wise).", font_size=12, color=WHITE)
        text1.next_to(heading1, DOWN, aligned_edge=LEFT, buff=0.3)

        # Animate the appearance of the brace and first text simultaneously
        self.play(
            FadeIn(brace_group),
            Write(heading1),
            run_time=0.8
        )
        self.play(
            Create(heading1_underline),
            run_time=0.6
        )
        self.play(
            Write(text1),
            run_time=1.0
        )
        self.wait(0.5)

        # 1. Identify the highest value in each column
        cells_with_max_values = VGroup()
        max_value_positions = []

        for j in range(num_cols):
            # Find the maximum value in this column
            col_values = [cosine_values[i][j] for i in range(num_rows)]
            max_value = max(col_values)
            
            # Find the row with this max value
            for i in range(num_rows):
                if cosine_values[i][j] == max_value:
                    # Calculate the cell position
                    cell_x = anchor_x + (j + 0.5) * dx + shift_right[0]
                    cell_y = anchor_y + (i + 0.5) * dy
                    max_value_positions.append((i, j))
                    
                    # Create a red background for this cell
                    cell_bg = Rectangle(
                        width=dx * 0.9,
                        height=dy * 0.9,
                        color=RED,
                        fill_color=RED,
                        fill_opacity=0.4,
                        stroke_width=0
                    )
                    cell_bg.move_to([cell_x, cell_y, 0])
                    
                    # Keep the original text object but we'll fade everything else out later
                    value_text = Text(f"{max_value:.2f}", font_size=14, color=WHITE, weight=BOLD)
                    value_text.move_to([cell_x, cell_y, 0])
                    
                    # Group the background and text
                    cell_group = VGroup(cell_bg, value_text)
                    cells_with_max_values.add(cell_group)

        # 2. Create a list of all values to fade out (except 1.00 and specifically kept values)
        values_to_fade = VGroup()
        # Values to keep in addition to 1.00 values (these are the 2nd best matches)
        kept_values = [
            (1, 0, 0.71),  # 1st column, value 0.62 (row 6)
            (2, 1, 0.58),  # 2nd column, value 0.47 (row 1)
            (5, 2, 0.65),  # 3rd column, value 0.31 (row 5)
            (7, 3, 0.62),  # 4th column, value 0.53 (row 1)
            (3, 4, 0.61),  # 5th column, value 0.31 (row 1)
        ]

        # Create rectangles for the kept values (2nd best matches)
        kept_values_rectangles = VGroup()
        kept_values_text = VGroup()

        for row, col, val in kept_values:
            # Calculate the cell position
            cell_x = anchor_x + (col + 0.5) * dx + shift_right[0]
            cell_y = anchor_y + (row + 0.5) * dy
            
            # Create a rectangle around the cell (with no fill)
            highlight_rect = Rectangle(
                width=dx * 0.9,
                height=dy * 0.9,
                stroke_width=2,
                stroke_color=YELLOW,
                fill_opacity=0,
            )
            highlight_rect.move_to([cell_x, cell_y, 0])
            kept_values_rectangles.add(highlight_rect)
            
            # Create text for the kept value
            value_text = Text(f"{val:.2f}", font_size=14, color=YELLOW, weight=BOLD)
            value_text.move_to([cell_x, cell_y, 0])
            kept_values_text.add(value_text)

        for j, column in enumerate(column_values):
            for i, value_text in enumerate(column):
                if (i, j) not in max_value_positions:
                    # Check if this value should be kept
                    keep_this_value = False
                    for row, col, val in kept_values:
                        if i == row and j == col:
                            keep_this_value = True
                            break
                    
                    if not keep_this_value:
                        values_to_fade.add(value_text)

        # 3. Identify grid lines to keep (just the x and y axes) and those to fade out
        grid_lines_to_keep = VGroup(y_axis, x_axis)  # Only keep the main x and y axes
        grid_lines_to_fade = VGroup()

        # Add all internal grid lines to the fade out group
        for line in grid_lines:
            if line not in [y_axis, x_axis]:  # If not the main axes
                grid_lines_to_fade.add(line)

        # ------------------------------------------------------------
        #  Legends: move them to the LEFT of the heat‑map (Y‑axis)
        # ------------------------------------------------------------

        # Legend token ① : best match (red filled square)
        best_match_square = Square(
            side_length=0.3,
            color=RED,
            fill_color=RED,
            fill_opacity=0.7,
            stroke_width=1.5,
        )
        best_match_text = Text("Best Match", font_size=18, color=WHITE)
        best_match_legend = VGroup(best_match_square, best_match_text).arrange(RIGHT, buff=0.2)

        # Legend token ② : second‑best match (yellow outline square)
        second_match_square = Square(
            side_length=0.3,
            color=YELLOW,
            fill_opacity=0,
            stroke_width=3.5,
        )
        second_match_text = Text("2nd Best Match", font_size=18, color=WHITE)
        second_match_legend = VGroup(second_match_square, second_match_text).arrange(RIGHT, buff=0.2)

        # Stack the two tokens vertically and park them beside the Y‑axis
        legends = VGroup(best_match_legend, second_match_legend)
        legends.arrange(DOWN, aligned_edge=LEFT, buff=0.25)   # vertical stack
        legends.next_to(y_axis, LEFT, buff=1.0)               # ← left of heat‑map

        # ------------------------------------------------------------
        #  Fade internal content, then reveal the legends
        # ------------------------------------------------------------
        self.play(
            FadeOut(values_to_fade),
            FadeOut(grid_lines_to_fade),
            run_time=1.5,
        )
        self.wait(0.5)

        # show red backgrounds for max‑value cells
        red_backgrounds = VGroup(*(cg[0] for cg in cells_with_max_values))
        self.play(FadeIn(red_backgrounds), run_time=1.0)
        self.wait(0.5)

        # finally bring in the legends
        self.play(Write(legends), run_time=1.0)
        self.wait(0.5)

        # 6. Animate the appearance of yellow borders for 2nd best matches
        # First replace the original text with bolded yellow text for better visibility
        for j, column in enumerate(column_values):
            for i, value_text in enumerate(column):
                for row, col, val in kept_values:
                    if i == row and j == col:
                        # Update the text color and weight for better visibility
                        column[i] = Text(f"{val:.2f}", font_size=16, color=YELLOW, weight=BOLD)
                        column[i].move_to(value_text.get_center())

        # Now animate the appearance
        self.play(
            Create(kept_values_rectangles),
            run_time=1.0
        )
        self.wait(0.5)

        # ------------------------------------------------------------
        # Curly braces for best + 2nd-best matches (cols 0-3 only)
        # ------------------------------------------------------------
        pair_braces = VGroup()

        for col in range(num_cols - 1):  # <-- skip last column
            # locate the rows
            best_row = next(r for r, c in max_value_positions if c == col)
            second_row = next(r for r, c, _ in kept_values if c == col)
            
            top_row, bottom_row = max(best_row, second_row), min(best_row, second_row)
            
            # Calculate positions
            right_x = anchor_x + (col + 1) * dx + shift_right[0]  # Right edge of the column
            center_y = anchor_y + (bottom_row + top_row + 1) * dy / 2
            h = (top_row - bottom_row + 1) * dy * 0.9
            
            # Create the brace on the right side
            brace = Brace(
                Line(
                    start=[right_x, center_y - h/2, 0],
                    end=[right_x, center_y + h/2, 0]
                ),
                direction=RIGHT,
                buff=0.05,
                color=WHITE
            )
            
            pair_braces.add(brace)

        # First, create and animate just the first brace
        first_brace = pair_braces[0]
        self.play(Create(first_brace), run_time=0.8)
        self.wait(0.3)

        # Create and animate arrow and "Mapping Window" text for the first brace
        arrow_start = first_brace.get_right() + RIGHT * 0.1
        arrow_end = arrow_start + RIGHT * 0.9
        mapping_arrow = Arrow(
            start=arrow_start,
            end=arrow_end,
            buff=0.1,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=7.0,
            color=YELLOW,
            stroke_width=8.5,
            fill_opacity=1
        )

        mapping_text = Text("Mapping Window", font_size=14, color=WHITE)
        mapping_text.next_to(mapping_arrow, RIGHT, buff=0.1)

        self.play(
            GrowArrow(mapping_arrow),
            Write(mapping_text),
            run_time=1.0
        )
        self.wait(0.5)

        # Now create the rest of the braces (excluding the first one)
        rest_braces = VGroup(*[pair_braces[i] for i in range(1, len(pair_braces))])
        self.play(Create(rest_braces), run_time=0.8)
        self.wait(0.3)

        # ================== ADVANCED VISUAL EFFECTS ==================
        # Create sophisticated pulsing animation effects for enhanced user engagement
        pulse = AnimationGroup(
            *[Indicate(
                b,
                scale_factor=1.05,
                color=YELLOW,
                run_time=1.4,
                rate_func=there_and_back
            ) for b in pair_braces],
            lag_ratio=0.15,  # slight column delay
        )

        # loop the pulse twice (or more if you like)
        self.play(pulse, pulse)
        self.wait(0.3)

        # Create a brace at the bottom of the heatmap
        brace_start_x = anchor_x + shift_right[0]  # Left edge of x-axis (already shifted)
        brace_end_x = anchor_x + x_length + shift_right[0]  # Right edge of x-axis (already shifted)
        brace_y = anchor_y - 0.7  # Further below the x-axis labels

        # Create the horizontal curly brace
        x_brace = Brace(
            Line(
                start=[brace_start_x, brace_y + 0.2, 0],
                end=[brace_end_x, brace_y + 0.2, 0]
            ),
            direction=DOWN
        )

        brace_group = VGroup(x_brace)

        # Add the brace and label
        self.play(
            FadeIn(brace_group),
            run_time=1.0
        )
        self.wait(0.5)

        # Create heading2 with typing effect
        heading2 = Text("Key Observations", font_size=16, color=WHITE)
        heading2.move_to([text_x, text_start_y - 1.0, 0], aligned_edge=LEFT+UP)

        # Rainbow colors for the gradient animation
        rainbow_colors = [BLUE, PURPLE, RED, ORANGE, YELLOW, GREEN, BLUE]

        # Start the animation cycle
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[0]),
            Write(heading2),
            run_time=0.8
        )

        # Add underline to heading2
        heading2_underline = Underline(heading2, color=WHITE)
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[1]),
            Create(heading2_underline),
            run_time=0.6
        )

        # Create text2 with typing effect (split into two lines for better animation)
        text2_line1 = Text("- Key Observation 1: Perfect One-to-One Mapping.", font_size=12, color=WHITE)
        text2_line1.next_to(heading2, DOWN, aligned_edge=LEFT, buff=0.3)
        text2_line2 = Text("(Each segment strongly matches itself)", font_size=12, color=WHITE)
        text2_line2.next_to(text2_line1, DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[2]),
            Write(text2_line1),
            run_time=1.0
        )

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[3]),
            Write(text2_line2),
            run_time=1.0
        )

        # Add Key Observation 2
        text2_line3 = Text("- Key Observation 2: Matches form a Straight, Ordered Line.", font_size=12, color=WHITE)
        text2_line3.next_to(text2_line2, DOWN, aligned_edge=LEFT, buff=0.3)
        text2_line4 = Text("(This consistent diagonal pattern is monotonic)", font_size=12, color=WHITE)
        text2_line4.next_to(text2_line3, DOWN, aligned_edge=LEFT, buff=0.1)

        # Animate them with the same rainbow color pattern
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[4]),
            Write(text2_line3),
            run_time=1.0
        )

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[5]),
            Write(text2_line4),
            run_time=1.0
        )

        # Create heading3 with typing effect
        heading3 = Text("Derive Mapping Window (from Observation 1)", font_size=16, color=WHITE)
        heading3.move_to([text_x, text_start_y - 3.0, 0], aligned_edge=LEFT+UP)

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[4]),
            Write(heading3),
            run_time=0.8
        )

        # Add underline to heading3
        heading3_underline = Underline(heading3, color=WHITE)
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[5]),
            Create(heading3_underline),
            run_time=0.6
        )

        # Add points about Mapping Window directly after the heading
        mapping_point1 = Text("- Focus on Observation 1: One-to-Two Mapping.", font_size=12, color=WHITE)
        mapping_point1.next_to(heading3, DOWN, aligned_edge=LEFT, buff=0.3)

        mapping_point2 = Text("- This tells us where matches *should* ideally occur.", font_size=12, color=WHITE)
        mapping_point2.next_to(mapping_point1, DOWN, aligned_edge=LEFT, buff=0.3)

        # Split mapping_point3 into two lines
        mapping_point3a = Text("- Concept: This defines the \"Mapping Window\" -", font_size=12, color=WHITE)
        mapping_point3a.next_to(mapping_point2, DOWN, aligned_edge=LEFT, buff=0.3)

        mapping_point3b = Text("the expected match position.", font_size=12, color=WHITE)
        mapping_point3b.next_to(mapping_point3a, DOWN, aligned_edge=LEFT, buff=0.1)

        # Split mapping_point4 into two lines
        mapping_point4a = Text("- (Calculated from the expected slope; here, slope is one,", font_size=12, color=WHITE)
        mapping_point4a.next_to(mapping_point3b, DOWN, aligned_edge=LEFT, buff=0.3)

        mapping_point4b = Text("so Segment 3 aligns near Segment 3).", font_size=12, color=WHITE)
        mapping_point4b.next_to(mapping_point4a, DOWN, aligned_edge=LEFT, buff=0.1)

        # Animate each mapping point with color cycling
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[6]),
            Write(mapping_point1),
            run_time=1.0
        )

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[0]),
            Write(mapping_point2),
            run_time=1.0
        )

        # Animate the split mapping_point3
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[1]),
            Write(mapping_point3a),
            run_time=1.0
        )

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[2]),
            Write(mapping_point3b),
            run_time=0.8
        )

        # Animate the split mapping_point4
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[3]),
            Write(mapping_point4a),
            run_time=1.0
        )

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[4]),
            Write(mapping_point4b),
            run_time=0.8
        )

        # Create heading3 with typing effect
        heading4 = Text("Definition", font_size=16, color=WHITE)
        heading4.move_to([text_x, text_start_y - 6.0, 0], aligned_edge=LEFT+UP)

        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[4]),
            Write(heading4),
            run_time=0.8
        )

        # Add underline to heading3
        heading4_underline = Underline(heading4, color=WHITE)
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[5]),
            Create(heading4_underline),
            run_time=0.6
        )

        # Create text3 with typing effect
        text4 = Text("This is called Mapping Window = Slope = 9/5", font_size=12, color=WHITE)
        text4.next_to(heading4, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(
            # border_rectangles.animate.set_color(rainbow_colors[6]),
            Write(text4),
            run_time=1.0
        )

        # With this:
        for color in rainbow_colors[1:]:
            self.wait(0.4)

        # To this:
        for _ in range(1):  # One more complete cycle
            for color in rainbow_colors:
                self.wait(0.4)

        # Final color
        self.wait(0.5)

        # Group all text elements that need to be faded out
        all_text_elements = VGroup(
            heading3, heading3_underline, mapping_point1, mapping_point2, mapping_point3a, mapping_point3b, mapping_point4a,mapping_point4b,
        )

        # Fade out all current text while keeping the heatmap and border rectangles
        self.play(
            FadeOut(all_text_elements),
            run_time=1.5
        )
        self.wait(0.5)

       # After the fade out is done
        # Group the definition elements together
        definition_group = VGroup(heading4, heading4_underline, text4)

        # New target position - move it up
        target_y = text_start_y - 3.0  # Adjust this value as needed

        # Calculate how far to move
        move_distance = target_y - (text_start_y - 6.0)

        # Animate moving the definition group up
        self.play(
            definition_group.animate.shift(UP * move_distance),
            run_time=1.2
        )
        self.wait(0.5)

       # Final color cycling to emphasize the mapping window concept
        for color in [ORANGE, YELLOW, GREEN, BLUE, PURPLE]:
            self.wait(0.4)

        # Final hold with a distinctive color
        self.wait(0.8)

        # Fade out the border lines AND the 1.00 values but keep the red background boxes
        borders_and_values_to_fade = VGroup()

        # Add all 1.00 value text objects to fade
        for i, j in max_value_positions:
            # Find the corresponding value text in column_values
            cell_text = column_values[j][i]  # Access using column then row index
            borders_and_values_to_fade.add(cell_text)

        # Fade out the borders and values
        self.play(FadeOut(borders_and_values_to_fade), run_time=1.0)
        self.wait(0.5)

        # Create points in the center of each 1.00 value cell
        center_points = VGroup()
        point_positions = []  # Store positions for line creation

        for i, j in max_value_positions:
            # Calculate the cell position
            cell_x = anchor_x + (j + 0.5) * dx + shift_right[0]
            cell_y = anchor_y + (i + 0.5) * dy
            
            # Create a point at the center
            point = Dot(
                [cell_x, cell_y, 0],
                radius=0.1,
                color=WHITE,
                fill_opacity=1.0
            )
            
            center_points.add(point)
            point_positions.append([cell_x, cell_y, 0])  # Store as 3D coordinate

        # Add the points
        self.play(FadeIn(center_points), run_time=0.8)
        self.wait(0.5)

        # -----------------------------------------------------------
        # Connect every best‑match dot in order (left → right)
        # -----------------------------------------------------------
        point_positions.sort(key=lambda p: p[0])        # sort by x‑coord

        narrative_line = VGroup(
            *[Line(p0, p1, color=YELLOW, stroke_width=3)
            for p0, p1 in zip(point_positions, point_positions[1:])]
        )

        # animate the poly‑line (little segments grow one after another)
        self.play(
            LaggedStart(*[Create(seg) for seg in narrative_line],
                        lag_ratio=0.05),
            run_time=1.2
        )

        # keep this alias if later code expects the name `diagonal_line`
        diagonal_line = narrative_line

        # Add "Attention!" heading and text while drawing the line
        attention_heading = Text(" Derive Narrative Line (from Observation 2)", font_size=16, color=WHITE)
        attention_heading.move_to([text_x, text_start_y - 4.2, 0], aligned_edge=LEFT+UP)

        # Add underline to heading
        attention_underline = Underline(attention_heading, color=WHITE)

        # Create text explaining the line
        monotonic_text = Text("- Now, Focus on Observation 2: Straight, Ordered Line.", font_size=12, color=WHITE)
        monotonic_text.next_to(attention_heading, DOWN, aligned_edge=LEFT, buff=0.3)

         # Create text explaining the line
        monotonic_text2 = Text("- If we connect the best matches, we trace the story's flow.", font_size=12, color=WHITE)
        monotonic_text2.next_to(monotonic_text, DOWN, aligned_edge=LEFT, buff=0.3)

         # Create text explaining the line
        monotonic_text3 = Text("- Concept: This path is the Narrative Line.", font_size=12, color=WHITE)
        monotonic_text3.next_to(monotonic_text2, DOWN, aligned_edge=LEFT, buff=0.3)
         # Create text explaining the line
        monotonic_text4 = Text("- Since it's a perfect, monotonic match here, the Narrative", font_size=12, color=WHITE)
        monotonic_text4.next_to(monotonic_text3, DOWN, aligned_edge=LEFT, buff=0.3)
        monotonic_text4a = Text("Line is straight.", font_size=12, color=WHITE)
        monotonic_text4a.next_to(monotonic_text4, DOWN, aligned_edge=LEFT, buff=0.1)

        # Animate the line and text simultaneously
        self.play(
            Create(diagonal_line),
            Write(attention_heading),
            run_time=1.0
        )

        self.play(
            Create(attention_underline),
            run_time=0.6
        )

        self.play(
            Write(monotonic_text),
            run_time=0.8
        )
        self.play(
            Write(monotonic_text2),
            run_time=0.8
        )
        self.play(
            Write(monotonic_text3),
            run_time=0.8
        )
        self.play(
            Write(monotonic_text4),
            run_time=0.8
        )
        self.play(
            Write(monotonic_text4a),
            run_time=0.8
        )
        self.wait(1.5)