
"""
Segmentation, Chunking and Cosine Similarity (SC) Animation

This Manim animation visualizes the comprehensive process of text segmentation, chunking, 
and cosine similarity calculation for text analysis. The animation demonstrates the complete 
workflow from raw text processing to similarity matrix generation.

The animation demonstrates:
1. Reference and generated text block visualization with enhanced styling
2. Symbol filtering process including punctuation removal and text cleaning
3. Sentence segmentation and tokenization (SAT) processing
4. Text chunking with configurable chunk sizes
5. Comprehensive similarity matrix visualization with heatmap display
6. Mathematical cosine similarity formula representation
7. Progressive data population with animated value filling

Author: Mehul Deep
Date: 07/15/2025
Framework: Manim Community v0.19.0

Usage:
    python -m manim -pql --disable_caching SC.py FullConceptAnimation
"""

from manim import (  # type: ignore
    # Core scene and animation classes
    Scene, Text, Underline, Create, Write, VGroup,
    
    # Geometric objects
    Arrow, Triangle, Line, Brace, Rectangle, RoundedRectangle,
    SurroundingRectangle, DashedVMobject, Square, CurvedArrow,
    
    # Text and paragraph objects
    Paragraph,
    
    # Animation functions
    GrowArrow, DrawBorderThenFill, GrowFromCenter, FadeIn, FadeOut,
    Transform, LaggedStart, ReplacementTransform,
    
    # Colors
    BLUE_E, GREEN_E, GREEN, ORANGE, RED, BLUE, YELLOW, LIGHT_PINK,
    WHITE, GREY, BLACK, DARK_BLUE, MAROON_B, ITALIC,
    
    # Positioning and constants
    ORIGIN, UP, LEFT, RIGHT, DOWN, PI, DEGREES,
    
    # Other utilities
    np
)

class FullConceptAnimation(Scene):
    """
    Main animation class for visualizing Segmentation, Chunking and Cosine Similarity.
    
    This animation demonstrates the complete text processing pipeline including
    symbol filtering, text segmentation, chunking strategies, and similarity
    matrix computation with comprehensive visual representations.
    """

    def construct(self):
        """Main animation sequence orchestrating all segmentation and chunking visualization components."""
        # ================== TITLE AND HEADING SETUP ==================
        # Create and animate the main title for Segmentation, Chunking and Cosine Similarity
        title = Text("Segmentation, Chunking and Cosine Similarity", font_size=25).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(0.5)

        # Position title at bottom edge for maximum screen space utilization
        self.play(title.animate.to_edge(DOWN*14.5))
        self.wait(0.5)

        # Add underline for visual emphasis and professional appearance
        underline = Underline(title)
        self.play(Create(underline))
        self.wait(0.5)

        # ================== TEXT BLOCK CREATION ==================
        # Create reference and generated text blocks with sophisticated styling
        # Reference text block - blue background for visual distinction
        reference_box = Rectangle(
            width=3.0, height=3.6,
            stroke_color=WHITE,
            stroke_width=2,
            fill_color=BLUE_E,         # Blue background for reference content
            fill_opacity=0.4
        )
        reference_label = Text("Reference", font_size=24, color=WHITE)
        reference_label.next_to(reference_box, UP, buff=0.2)

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
        # Create a paragraph object for the reference text
        reference_paragraph = Paragraph(
            *reference_lines,
            alignment="LEFT",
            line_spacing=0.5,
            font_size=20,
            color=WHITE
        )
        # Set width and position for the reference paragraph
        reference_paragraph.set_width(reference_box.get_width() - 0.2)
        reference_paragraph.move_to(reference_box.get_center())
        reference_group = VGroup(reference_box, reference_label, reference_paragraph)
        
        # Position the reference box at the top left corner
        generated_box = Rectangle(
            width=3.0, height=3.6,
            stroke_color=WHITE,
            stroke_width=2,
            fill_color=MAROON_B,
            fill_opacity=0.4
        )
        # Create label for generated text box with a distinct color for differentiation
        generated_label = Text("Generated", font_size=24, color=WHITE)
        generated_label.next_to(generated_box, UP, buff=0.2)
        generated_lines = [
            "The old town bell rings, signaling", 
            "the start of a busy market.", 
            "Stalls come alive as vendors set", 
            "up their goods in the busy square,", 
            "and the smell of fresh baked goods", 
            "fills the morning air. A lively", 
            "seller shouts out good deals to", 
            "attract a curious crowd. A happy child", 
            "runs after a flying kite among the",
            "stalls, adding a fun touch to the", 
            "scene. An eager artist quickly", 
            "draws the lively scene, adding a", 
            "creative touch. A short rain briefly",
            "stops the flow, but the market soon", 
            "gets moving again. A lively musician", 
            "starts playing a song that grabs the",
            "attention of a nearby group. As the", 
            "market gets at its busiest, the bell",
            "rings again at midday, refreshing the", 
            "crowd with its familiar sound. As dusk", 
            "comes, the old bell rings once more,", 
            "echoing the busy start of the market."
        ]
        # Create a paragraph object for the generated text
        generated_paragraph = Paragraph(
            *generated_lines,
            alignment="LEFT",
            line_spacing=0.5,
            font_size=10,
            color=WHITE
        )
        # Set width and position for the generated paragraph to ensure it fits within the generated box
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

        # ================== SYMBOL FILTER FLOW ARROWS ==================
        # Create prominent arrows directing text to symbol filtering process
        arrow_ref = Arrow(
            start=reference_box.get_right(),
            end=reference_box.get_right() + RIGHT * 0.7,
            buff=0.1,
            max_tip_length_to_length_ratio=0.35,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=12.0,   # Added for thicker stroke
            color=YELLOW,                         # Changed to direct color setting
            stroke_width=20,                      # Increased thickness
            fill_opacity=1.5,                       # Changed to filled arrow
        )
        arrow_gen = Arrow(
            start=generated_box.get_right(),
            end=generated_box.get_right() + RIGHT * 0.7,
            buff=0.1,
            max_tip_length_to_length_ratio=0.35,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=12.0,   # Added for thicker stroke
            color=YELLOW,                         # Changed to direct color setting
            stroke_width=20,                      # Increased thickness
            fill_opacity=1.5,                       # Changed to filled arrow
        )
        self.play(GrowArrow(arrow_ref), GrowArrow(arrow_gen), run_time=0.5)
        self.wait(0.5)

        # ================== SYMBOL FILTERING OPERATIONS ==================
        # Create and display text processing operations with custom brackets
        # Create the three text items
        text1 = Text("Remove Punctuations", font_size=8)
        text2 = Text("Fix punctuation space", font_size=8)
        text3 = Text("Expand contraction", font_size=8)
        
        # Arrange them vertically
        text_group = VGroup(text1, text2, text3).arrange(DOWN, buff=0.15)
        
        # Create custom thin brackets using Line objects
        bracket_height = text_group.height + 0.1
        bracket_width = 0.1
        
        # Left bracket components
        left_vert = Line(
            start=[0, bracket_height/2, 0],
            end=[0, -bracket_height/2, 0],
            stroke_width=1.5  # Very thin line
        )
        left_top = Line(
            start=[0, bracket_height/2, 0],
            end=[bracket_width, bracket_height/2, 0],
            stroke_width=1.5  # Very thin line
        )
        left_bottom = Line(
            start=[0, -bracket_height/2, 0],
            end=[bracket_width, -bracket_height/2, 0],
            stroke_width=1.5  # Very thin line
        )
        left_bracket = VGroup(left_vert, left_top, left_bottom)
        
        # Right bracket components
        right_vert = Line(
            start=[0, bracket_height/2, 0],
            end=[0, -bracket_height/2, 0],
            stroke_width=1.5  # Very thin line
        )
        right_top = Line(
            start=[0, bracket_height/2, 0],
            end=[-bracket_width, bracket_height/2, 0],
            stroke_width=1.5  # Very thin line
        )
        right_bottom = Line(
            start=[0, -bracket_height/2, 0],
            end=[-bracket_width, -bracket_height/2, 0],
            stroke_width=1.5  # Very thin line
        )
        right_bracket = VGroup(right_vert, right_top, right_bottom)
        
        # Position brackets to fully wrap from top to bottom
        left_bracket.next_to(text_group, LEFT, buff=0.1)
        right_bracket.next_to(text_group, RIGHT, buff=0.1)
        
        # Group everything together (without the box)
        nv_group_ref = VGroup(text_group, left_bracket, right_bracket)
        nv_group_ref.next_to(arrow_ref.get_end(), RIGHT, buff=0.08)

        # Create the same group for generated text (without box)
        # Create copies of the text items
        text1_gen = Text("Remove Punctuations", font_size=8)
        text2_gen = Text("Fix punctuation space", font_size=8)
        text3_gen = Text("Expand contraction", font_size=8)
        
        # Arrange them vertically
        text_group_gen = VGroup(text1_gen, text2_gen, text3_gen).arrange(DOWN, buff=0.15)
        
        # Create custom thin brackets using Line objects (for generated section)
        bracket_height_gen = text_group_gen.height + 0.1
        bracket_width = 0.1
        
        # Left bracket components
        left_vert_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[0, -bracket_height_gen/2, 0],
            stroke_width=1.5  # Very thin line
        )
        left_top_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[bracket_width, bracket_height_gen/2, 0],
            stroke_width=1.5  # Very thin line
        )
        left_bottom_gen = Line(
            start=[0, -bracket_height_gen/2, 0],
            end=[bracket_width, -bracket_height_gen/2, 0],
            stroke_width=1.5  # Very thin line
        )
        left_bracket_gen = VGroup(left_vert_gen, left_top_gen, left_bottom_gen)
        
        # Right bracket components
        right_vert_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[0, -bracket_height_gen/2, 0],
            stroke_width=1.5  # Very thin line
        )
        right_top_gen = Line(
            start=[0, bracket_height_gen/2, 0],
            end=[-bracket_width, bracket_height_gen/2, 0],
            stroke_width=1.5  # Very thin line
        )
        right_bottom_gen = Line(
            start=[0, -bracket_height_gen/2, 0],
            end=[-bracket_width, -bracket_height_gen/2, 0],
            stroke_width=1.5  # Very thin line
        )
        right_bracket_gen = VGroup(right_vert_gen, right_top_gen, right_bottom_gen)
        
        # Position brackets to fully wrap from top to bottom
        left_bracket_gen.next_to(text_group_gen, LEFT, buff=0.1)
        right_bracket_gen.next_to(text_group_gen, RIGHT, buff=0.1)
        
        # Group everything together (without the box)
        nv_group_gen = VGroup(text_group_gen, left_bracket_gen, right_bracket_gen)
        nv_group_gen.next_to(arrow_gen.get_end(), RIGHT, buff=0.08)

        # Animate the appearance
        self.play(FadeIn(nv_group_ref, shift=LEFT), FadeIn(nv_group_gen, shift=LEFT), run_time=0.5)
        self.wait(0.5)

        # Add horizontal curly braces for both text groups - reference brace at bottom, generated brace at top
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

        # Animate the appearance of horizontal curly braces
        self.play(GrowFromCenter(horiz_brace_ref), GrowFromCenter(horiz_brace_gen), run_time=0.7)
        self.wait(0.5)

        # ================== L-SHAPED FEEDBACK ARROWS ==================
        # Create L-shaped arrows from filtering operations back to text blocks
        import string
        no_punct_reference_lines = [
            line.translate(str.maketrans('', '', string.punctuation))
            for line in reference_lines
        ]
        no_punct_generated_lines = [
            line.translate(str.maketrans('', '', string.punctuation))
            for line in generated_lines
        ]

        # Animate two L-shaped arrows with thicker lines - going from braces to boxes
        # For reference: arrow from bottom brace to reference box
        start_bottom_center_1 = horiz_brace_ref.get_center()  # Start from the brace's center
        start_bottom_center_1 = start_bottom_center_1 + DOWN * 0.15  # Increase this value for more space
        offset1 = start_bottom_center_1 + DOWN * 0.2
        end1_x = reference_box.get_right()[0]
        end1 = [end1_x, offset1[1], 0]
        line_vertical_ref = Line(
            start_bottom_center_1, 
            offset1, 
            stroke_color=YELLOW, 
            stroke_width=5,  # Increased thickness
            buff=0
        )
        arrow_horizontal_ref = Arrow(
            offset1, 
            end1, 
            stroke_color=YELLOW, 
            stroke_width=10,  # Increased thickness
            max_tip_length_to_length_ratio=0.25,  # Added for proportional arrowhead 
            max_stroke_width_to_length_ratio=3.0,   # Added for thicker stroke
            fill_opacity=1,  # Changed to filled arrow
            tip_length=0.2, 
            buff=0
        )
        l_arrow_ref = VGroup(line_vertical_ref, arrow_horizontal_ref)

        # For generated: arrow from top brace to generated box
        start_top_center_2 = horiz_brace_gen.get_center()  # Start from the brace's center
        start_top_center_2 = start_top_center_2 + UP * 0.15  # Increase this value for more space
        offset2 = start_top_center_2 + UP * 0.2
        end2_x = generated_box.get_right()[0]
        end2 = [end2_x, offset2[1], 0]
        line_vertical_gen = Line(
            start_top_center_2, 
            offset2, 
            stroke_color=YELLOW, 
            stroke_width=5,  # Increased thickness
            buff=0
        )
        # Create the horizontal arrow for generated text
        arrow_horizontal_gen = Arrow(
            offset2, 
            end2, 
            stroke_color=YELLOW, 
            stroke_width=10,  # Increased thickness
            max_tip_length_to_length_ratio=0.25,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=3.0,   # Added for thicker stroke
            fill_opacity=1,  # Changed to filled arrow
            tip_length=0.2, 
            buff=0
        )
        # Combine the vertical and horizontal lines into a single L-shaped arrow
        l_arrow_gen = VGroup(line_vertical_gen, arrow_horizontal_gen)

        self.play(Create(l_arrow_ref), Create(l_arrow_gen), run_time=1.0)
        self.wait(0.5)

        # Animate transformation to no-punctuation paragraphs
        reference_paragraph_no_punct = Paragraph(
            *no_punct_reference_lines, alignment="LEFT", line_spacing=0.6, font_size=11
        ).move_to(reference_box.get_center())
        generated_paragraph_no_punct = Paragraph(
            *no_punct_generated_lines, alignment="LEFT", line_spacing=0.5, font_size=11
        ).move_to(generated_box.get_center())

        # Ensure paragraphs fit within their respective boxes
        if reference_paragraph_no_punct.get_width() > reference_box.get_width():
            reference_paragraph_no_punct.scale_to_fit_width(reference_box.get_width() * 0.9)
            reference_paragraph_no_punct.move_to(reference_box.get_center())
        if generated_paragraph_no_punct.get_width() > generated_box.get_width():
            generated_paragraph_no_punct.scale_to_fit_width(generated_box.get_width() * 0.9)
            generated_paragraph_no_punct.move_to(generated_box.get_center())

        self.play(
            LaggedStart(
                *[ReplacementTransform(old_line, new_line)
                  for old_line, new_line in zip(reference_paragraph, reference_paragraph_no_punct)],
                lag_ratio=0.15, run_time=2
            ),
            LaggedStart(
                *[ReplacementTransform(old_line, new_line)
                  for old_line, new_line in zip(generated_paragraph, generated_paragraph_no_punct)],
                lag_ratio=0.15, run_time=2
            )
        )
        self.wait(0.5)

        # ================== SAT PROCESSING BOXES ==================
        # Create Sentence Segmentation and Tokenization (SAT) boxes
        sat_box_ref = RoundedRectangle(width=0.6, height=0.3, corner_radius=0.1,
                                       stroke_color=WHITE, fill_color=BLACK, fill_opacity=0.5)
        sat_ref_text = Text("SAT", font_size=10).move_to(sat_box_ref.get_center())
        sat_group_ref = VGroup(sat_box_ref, sat_ref_text)
        sat_group_ref.next_to(nv_group_ref, RIGHT, buff=0.55)
        sat_group_ref.set_opacity(0)
        self.add(sat_group_ref) 

        # Create the same SAT box for generated text
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

        # Create the same arrow for generated text
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

        # Short arrows from each SAT box - THICKER
        arrow_from_sat_ref = Arrow(
            start=sat_group_ref.get_edge_center(RIGHT),
            end=sat_group_ref.get_edge_center(RIGHT) + RIGHT * 0.55,
            buff=0.05, 
            max_tip_length_to_length_ratio=0.35,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=12.0,   # Added for thicker stroke
            color=YELLOW,                        # Changed from stroke_color to color
            stroke_width=20,                     # Increased thickness
            fill_opacity=1.5,                      # Changed to filled arrow
            tip_length=0.2
        )
        # Create the same arrow for generated text
        arrow_from_sat_gen = Arrow(
            start=sat_group_gen.get_edge_center(RIGHT),
            end=sat_group_gen.get_edge_center(RIGHT) + RIGHT * 0.55,
            buff=0.05, 
            max_tip_length_to_length_ratio=0.35,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=12.0,   # Added for thicker stroke
            color=YELLOW,                        # Changed from stroke_color to color
            stroke_width=20,                     # Increased thickness
            fill_opacity=1.5,                      # Changed to filled arrow
            tip_length=0.2
        )

        # Animate top arrow
        self.play(GrowArrow(arrow_from_sat_ref), run_time=1.0)
        self.wait(0.5)

        # ================== REFERENCE TEXT SEGMENTATION ==================
        # Create segmented reference text with numbered boxes for chunk identification
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
            line_text = Text(f' "{line_content}"', font_size=7.8)
            
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

        # Animate bottom arrow
        self.play(GrowArrow(arrow_from_sat_gen), run_time=1.0)
        self.wait(0.5)

        # ================== GENERATED TEXT SEGMENTATION ==================
        # Create segmented generated text with numbered boxes for chunk identification
        lines_bottom_content = [
            "The old town bell rings signaling the start of a busy market",
            "Stalls come alive as vendors set up their goods in the busy square and the smell of fresh baked goods fills the morning air",
            "A lively seller shouts out good deals to attract a curious crowd",
            "A happy child runs after a flying kite among the stalls adding a fun touch to the scene",
            "An eager artist quickly draws the lively scene adding a creative touch",
            "A short rain briefly stops the flow but the market soon gets moving again",
            "A lively musician starts playing a song that grabs the attention of a nearby group",
            "As the market gets at its busiest the bell rings again at midday refreshing the crowd with its familiar sound",
            "As dusk comes the old bell rings once more echoing the busy start of the market"
        ]
        
        arrow_end_bottom = arrow_from_sat_gen.get_end()
        lines_bottom_mobs = []  # store line mobjects in a list
        
        # Shift factors - use the same values as for the top section
        horizontal_shift = 0.2  # Positive value shifts right
        vertical_shift = 0.20    # Positive value shifts up
        
        # Create segment boxes first (but don't display yet)
        segment_boxes_bottom = []

        for j, chunk_content in enumerate(lines_bottom_content):
            # Create the numbered square box
            box_size = 0.2
            number_box = Square(
                side_length=box_size,
                color=WHITE,
                fill_color=MAROON_B,
                fill_opacity=0.5,
                stroke_width=1
            )
            
            # Position the number box
            left_x = arrow_end_bottom[0] + 0.2 + horizontal_shift
            line_y = arrow_end_bottom[1] + 1.0 - j * 0.3 + vertical_shift
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
            chunk_text = Text(f' "{chunk_content}"', font_size=7.8)
            
            # Position the text to the right of the number box with increased buffer
            chunk_text.next_to(number_box, RIGHT, buff=0.2)  # Increased buffer from 0.1 to 0.3
            
            # Maintain left alignment but with a horizontal offset
            chunk_text.align_to(number_box, LEFT)
            chunk_text.shift(RIGHT * 0.35)  # Additional shift to the right
            
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
        # Position the bottom lines below the top lines
        self.wait(1.0)

        # ================== SCENE TRANSITION AND CLEANUP ==================
        # Fade out preprocessing elements while keeping segmented text for matrix display
        # Put the top/bottom lines into VGroups so we can keep them
        lines_top_vg = VGroup(*lines_top_mobs)
        lines_bottom_vg = VGroup(*lines_bottom_mobs)

        # All the stuff we want to fade out
        fade_out_list = [
            reference_group, generated_group,
            arrow_ref, arrow_gen,
            nv_group_ref, nv_group_gen,
            l_arrow_ref, l_arrow_gen,
            reference_paragraph_no_punct, generated_paragraph_no_punct,
            sat_group_ref, sat_group_gen,
            arrow_sat_ref, arrow_sat_gen,
            arrow_from_sat_ref, arrow_from_sat_gen,
            horiz_brace_ref,
            horiz_brace_gen
        ]
        self.play(FadeOut(VGroup(*fade_out_list)), run_time=1.5)

        self.wait(1.0)

        # ================== CHUNK SIZE SPECIFICATION ==================
        # Add arrows and text indicating chunk size configuration
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

        # ================== SIMILARITY MATRIX CONSTRUCTION ==================
        # Create coordinate system for similarity matrix visualization
        # Define Y-axis (9 lines) and X-axis (9 lines) for segment comparison
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
            "5",
            "6",
            "7",
            "8",
            "9"
        ]

        # Position anchor point for L-shaped coordinate system (bottom-left corner)
        anchor = LEFT * 6.3 + DOWN * 2.6

        # Configure axis dimensions for similarity matrix
        y_length = 5.0  # vertical axis length
        x_length = 5.0  # horizontal axis length

        # ================== COORDINATE SYSTEM CREATION ==================
        # Create L-shaped coordinate system for matrix visualization
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

        # ================== Y-AXIS LABELS (REFERENCE SEGMENTS) ==================
        # Create colored boxes with segment numbers for Y-axis (reference text)
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

        # ================== X-AXIS LABELS (GENERATED SEGMENTS) ==================
        # Create colored boxes with segment numbers for X-axis (generated text)
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
                fill_color=MAROON_B,  # Use MAROON_B to match the generated box color
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

        # ================== GRID CONSTRUCTION ==================
        # Create matrix grid for similarity value display
        anchor_x = axis_x_start[0]  # same as 'anchor' x
        anchor_y = axis_x_start[1]  # same as 'anchor' y

        num_rows = 9
        num_cols = 9
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

        # ================== MATRIX POSITIONING AND TRANSITION ==================
        # Clean up segmentation visualization and reposition matrix for formula display
        # First, group all the elements to fade out
        fade_out_segments = VGroup(
            lines_top_vg, lines_bottom_vg,
            left_brace, left_brace_bottom,
            arrow_from_brace_top, arrow_from_brace_bottom,
            chunk_size_text_top, chunk_size_text_bottom
        )

        # Create a group of all heatmap elements to shift
        heatmap_elements = VGroup(
            y_axis, x_axis,
            y_labels, x_labels,
            grid_lines
        )

        # Fade out the segmentation part
        self.play(FadeOut(fade_out_segments), run_time=1.5)
        self.wait(0.5)

        # Shift the heatmap to the right
        shift_right = RIGHT * 1.8  # Adjust this value to control how far right it moves
        self.play(heatmap_elements.animate.shift(shift_right), run_time=1.5)
        self.wait(1.0)

        # ================== MATRIX CELL IDENTIFIERS ==================
        # Add segment identifier boxes to matrix cells for reference
        first_column_boxes = VGroup()

        for i in range(num_rows):  # For each row (0 to 8)
            # Calculate the position for this cell in the first column
            cell_x = anchor_x + dx/2 + shift_right[0]  # Center of first column + shift
            cell_y = anchor_y + (i + 0.5) * dy  # Center of the cell row
            
            # Box size
            small_box_size = 0.19
            
            # Create all elements first
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
                fill_color=MAROON_B,
                fill_opacity=0.7,
                stroke_width=0.5
            )
            
            # First create the paired boxes with minimal gap
            box_pair = VGroup(first_small_box, second_small_box)
            box_pair.arrange(RIGHT, buff=0.05)  # Arrange them with minimal gap
            
            # Now position the pair as a whole at the center of the cell
            box_pair.move_to([cell_x, cell_y, 0])
            
            # Add the numbers inside the boxes
            row_num_text = Text(f"{i+1}", font_size=10, color=WHITE)
            row_num_text.move_to(first_small_box.get_center())
            
            col_num_text = Text("1", font_size=10, color=WHITE)
            col_num_text.move_to(second_small_box.get_center())
            
            # Group the boxes and numbers
            cell_group = VGroup(first_small_box, row_num_text, second_small_box, col_num_text)
            first_column_boxes.add(cell_group)

        # ================== COMPLETE MATRIX CELL POPULATION ==================
        # Add segment identifier boxes to all matrix cells
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
                    fill_color=MAROON_B,
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
        self.play(FadeIn(all_columns_boxes, first_column_boxes), run_time=1.5)
        self.wait(1.0)

        # ================== COSINE SIMILARITY FORMULA ==================
        # Create and position mathematical formula for cosine similarity
        formula_x = anchor_x + x_length + 4.3  # Position to right of matrix
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
            fill_color=MAROON_B,
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

        # ================== MATRIX VALUE POPULATION ==================
        # Replace cell identifiers with cosine similarity values
        self.play(FadeOut(all_columns_boxes,first_column_boxes), run_time=1.0)
        self.wait(0.5)

        # Define the cosine similarity values from the provided matrix (9x10 grid)
        cosine_values = [
            # Row 1 [1] (bottom row in the matrix)
            [0.78, 0.37, 0.31, 0.30, 0.24, 0.18, 0.26, 0.18, 0.26],
            # Row 2 [2]
            [0.26, 0.68, 0.30, 0.44, 0.22, 0.17, 0.15, 0.19, 0.32],
            # Row 3 [3]
            [0.28, 0.36, 0.66, 0.37, 0.27, 0.40, 0.27, 0.31, 0.30],
            # Row 4 [4]
            [0.30, 0.55, 0.36, 0.76, 0.25, 0.24, 0.26, 0.29, 0.30],
            # Row 5 [5]
            [0.26, 0.22, 0.25, 0.27, 0.70, 0.28, 0.35, 0.27, 0.22],
            # Row 6 [6]
            [0.18, 0.22, 0.31, 0.19, 0.39, 0.50, 0.24, 0.18, 0.22],
            # Row 7 [7]
            [0.23, 0.31, 0.22, 0.24, 0.40, 0.25, 0.75, 0.23, 0.39],
            # Row 8 [8]
            [0.25, 0.39, 0.38, 0.26, 0.23, 0.27, 0.29, 0.27, 0.75],
            # Row 9 [9] (top row in the matrix)
            [0.34, 0.30, 0.25, 0.19, 0.15, 0.12, 0.19, 0.16, 0.29]
        ]

        # Define colors for different value ranges
        def get_color_for_value(value):
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