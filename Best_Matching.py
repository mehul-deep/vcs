
"""
Best Matching Algorithm Animation

This Manim animation visualizes the Best Matching Algorithm for text alignment,
demonstrating how reference and generated text segments are matched based on
similarity scores and optimal pairing strategies.

The animation demonstrates:
1. Text segment visualization with numbered boxes
2. Similarity score calculations and heatmap displays
3. Best matching algorithm implementation
4. Arrow-based connection visualization between matched segments
5. Step-by-step algorithm execution with highlighting

Author: Mehul Deep
Date: 07/15/2025
Framework: Manim Community v0.19.0

Usage:
    python -m manim -pql --disable_caching Best_Matching.py FullConceptAnimation
"""

from manim import (  # type: ignore
    # Core scene and animation classes
    Scene, Text, Underline, Create, Write, VGroup,
    
    # Geometric objects
    Arrow, Triangle, Line, Brace, Rectangle, RoundedRectangle,
    SurroundingRectangle, DashedVMobject, Square, Arc, CubicBezier,
    
    # Mathematical and text objects
    MathTex, Paragraph,
    
    # Animation functions
    GrowArrow, DrawBorderThenFill, GrowFromCenter, FadeIn, FadeOut,
    Transform, LaggedStart, ReplacementTransform,
    
    # Colors
    BLUE_E, GREEN_E, GREEN, ORANGE, RED, BLUE, YELLOW, LIGHT_PINK,
    WHITE, GREY, BLACK, DARK_BLUE, MAROON_B,
    
    # Positioning and constants
    ORIGIN, UP, LEFT, RIGHT, DOWN, PI, DEGREES,
    
    # Text formatting
    ITALIC,
    
    # Other utilities
    CurvedArrow, np
)

class FullConceptAnimation(Scene):
    """
    Main animation class for visualizing the Best Matching Algorithm.
    
    This animation demonstrates the complete process of text segment matching,
    including similarity calculations, optimal pairing, and visual connections.
    """

    def construct(self):
        """Main animation sequence orchestrating all visualization components."""
        # ================== TITLE AND SETUP ==================
        # Create and animate the main title
        title = Text("Best Matching Algorithm", font_size=25).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(0.5)

        # Move title to top and add underline
        self.play(title.animate.to_edge(UP*0.1))
        self.wait(0.5)
        
        underline = Underline(title)
        self.play(Create(underline))
        self.wait(0.5)

        # ================== TEXT SEGMENT DEFINITIONS ==================
        # Reference text segments - original source material
        reference_lines = [
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
        
        # Generated text segments - AI-produced variations to be matched against reference
        generated_lines = [
            "The old town bell rings signaling the start of a busy market",
            "Stalls come alive as vendors set up their goods in the busy square and the smell of fresh baked goods fills the air",
            "A lively seller shouts out good deals to attract a curious crowd",
            "A happy child runs after a flying kite among the stalls adding a fun touch to the scene",
            "An eager artist quickly draws the lively scene adding a creative touch",
            "A short rain briefly stops the flow but the market soon gets moving again",
            "A lively musician starts playing a song that grabs the attention of a nearby group",
            "As the market gets at its busiest the bell rings again at midday refreshing the crowd with its familiar sound",
            "As dusk comes the old bell rings once more echoing the busy start of the market"
        ]
        
        # ================== LAYOUT CONFIGURATION ==================
        # Positioning parameters for text segment visualization
        ref_segment_start_x = 0.6    # X-coordinate for segment alignment
        ref_segment_y = 2.5          # Y-coordinate for top reference segment
        gen_segment_y = -0.7         # Y-coordinate for top generated segment
        segment_spacing = 0.3        # Vertical spacing between segments
        
        # ================== REFERENCE SEGMENTS CREATION ==================
        # Create visual representation of reference text segments with numbered boxes
        ref_segments_group = VGroup()
        for i, line_content in enumerate(reference_lines):
            # Create numbered square box for reference segments
            box_size = 0.2
            number_box = Square(
                side_length=box_size,
                color=WHITE,
                fill_color=BLUE_E,      # Blue background for reference segments
                fill_opacity=0.5,
                stroke_width=1
            )
            
            # Add segment number inside the box
            number_text = Text(f"{i+1}", font_size=10, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            # Create text content with quotation marks for readability
            line_text = Text(f'"{line_content}"', font_size=7.8)
            
            # Position elements in proper layout
            number_box.move_to([ref_segment_start_x, ref_segment_y - i * segment_spacing, 0])
            number_text.move_to(number_box.get_center())
            line_text.next_to(number_box, RIGHT, buff=0.2)
            line_text.align_to(number_box, LEFT)
            line_text.shift(RIGHT * 0.35)
            
            # Group box, number, and text as single segment
            segment = VGroup(number_box, number_text, line_text)
            ref_segments_group.add(segment)
        
        # ================== GENERATED SEGMENTS CREATION ==================
        # Create visual representation of generated text segments with numbered boxes
        gen_segments_group = VGroup()
        for i, line_content in enumerate(generated_lines):
            # Create numbered square box for generated segments
            box_size = 0.2
            number_box = Square(
                side_length=box_size,
                color=WHITE,
                fill_color=MAROON_B,        # Maroon background for generated segments
                fill_opacity=0.5,
                stroke_width=1
            )
            
            # Add the number inside the box
            number_text = Text(f"{i+1}", font_size=10, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            # Create the text content with quotation marks
            line_text = Text(f'"{line_content}"', font_size=7.8)
            
            # Position the elements
            number_box.move_to([ref_segment_start_x, gen_segment_y - i * segment_spacing, 0])
            number_text.move_to(number_box.get_center())
            line_text.next_to(number_box, RIGHT, buff=0.2)
            line_text.align_to(number_box, LEFT)
            line_text.shift(RIGHT * 0.35)
            
            # Group them
            segment = VGroup(number_box, number_text, line_text)
            gen_segments_group.add(segment)
        
        # Create the curly braces for both segment groups
        ref_brace = Brace(
            ref_segments_group,
            direction=LEFT,
            buff=0.05,
            color=WHITE
        )
        
        gen_brace = Brace(
            gen_segments_group,
            direction=LEFT,
            buff=0.05,
            color=WHITE
        )
        
        # ================== CHUNK SIZE ANNOTATIONS ==================
        # Create arrows and labels to indicate chunk size for both text collections
        # Reference section chunk size indicator
        arrow_from_brace_ref = Arrow(
            start=ref_brace.get_edge_center(LEFT) + LEFT * 0.1,
            end=ref_brace.get_edge_center(LEFT) + LEFT * 1.2,
            buff=0.1,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=7.0,
            color=YELLOW,
            stroke_width=8.5,
            fill_opacity=1
        )
        
        chunk_size_text_ref = Text("Chunk Size = 1", font_size=8)
        chunk_size_text_ref.move_to(arrow_from_brace_ref.get_center() + UP * 0.3)
        
        # For generated section
        arrow_from_brace_gen = Arrow(
            start=gen_brace.get_edge_center(LEFT) + LEFT * 0.1,
            end=gen_brace.get_edge_center(LEFT) + LEFT * 1.2,
            buff=0.1,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=7.0,
            color=YELLOW,
            stroke_width=8.5,
            fill_opacity=1
        )
        
        chunk_size_text_gen = Text("Chunk Size = 1", font_size=8)
        chunk_size_text_gen.move_to(arrow_from_brace_gen.get_center() + UP * 0.3)
        
        # Create right side elements group
        right_side_elements = VGroup(
            ref_segments_group, gen_segments_group,
            ref_brace, gen_brace,
            arrow_from_brace_ref, arrow_from_brace_gen,
            chunk_size_text_ref, chunk_size_text_gen
        )
        
        # ================== SIMILARITY HEATMAP CREATION ==================
        # Create visual heatmap to display similarity scores between text segments
        
        # Grid positioning and dimensions
        anchor = LEFT * 6.0 + DOWN * 2.6    # Bottom-left corner of heatmap
        y_length, x_length = 5.0, 5.0       # Heatmap dimensions
        num_rows, num_cols = 9, 9            # Grid size (9x9 for segment comparisons)
        
        # Calculate cell dimensions
        dx = x_length / num_cols  # Cell width
        dy = y_length / num_rows  # Cell height
        
        # Create main axes for heatmap boundaries
        y_axis = Line(
            anchor, 
            anchor + UP * y_length, 
            stroke_color=WHITE, 
            stroke_width=1
        )
        
        x_axis = Line(
            anchor, 
            anchor + RIGHT * x_length, 
            stroke_color=WHITE, 
            stroke_width=1
        )
        
        # Create grid lines for cell separation
        grid_lines = VGroup()
        
        # Horizontal grid lines
        for row_idx in range(num_rows + 1):
            y_line = anchor[1] + row_idx * dy
            line_h = Line(
                [anchor[0], y_line, 0],
                [anchor[0] + x_length, y_line, 0],
                stroke_color=WHITE,
                stroke_width=1
            )
            grid_lines.add(line_h)
        
        # Vertical grid lines
        for col_idx in range(num_cols + 1):
            x_line = anchor[0] + col_idx * dx
            line_v = Line(
                [x_line, anchor[1], 0],
                [x_line, anchor[1] + y_length, 0],
                stroke_color=WHITE,
                stroke_width=1
            )
            grid_lines.add(line_v)
        
        # Create axis labels (blue boxes for y-axis)
        y_labels = VGroup()
        for i in range(num_rows):
            box_size = 0.45
            number_box = RoundedRectangle(
                width=box_size, 
                height=box_size,
                corner_radius=0.04,
                color=WHITE,
                fill_color=BLUE_E,
                fill_opacity=0.5,
                stroke_width=1
            )
            
            label_x = anchor[0] - 0.35
            label_y = anchor[1] + (i + 0.5) * dy
            number_box.move_to([label_x, label_y, 0])
            
            number_text = Text(str(i+1), font_size=12, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            label_group = VGroup(number_box, number_text)
            y_labels.add(label_group)
        
        # Create axis labels (maroon boxes for x-axis)
        x_labels = VGroup()
        for j in range(num_cols):
            box_size = 0.45
            number_box = RoundedRectangle(
                width=box_size, 
                height=box_size,
                corner_radius=0.04,
                color=WHITE,
                fill_color=MAROON_B,
                fill_opacity=0.5,
                stroke_width=1
            )
            
            label_x = anchor[0] + (j + 0.5) * dx
            label_y = anchor[1] - 0.35
            number_box.move_to([label_x, label_y, 0])
            
            number_text = Text(str(j+1), font_size=12, color=WHITE)
            number_text.move_to(number_box.get_center())
            
            label_group = VGroup(number_box, number_text)
            x_labels.add(label_group)
        
        # Create cell values for the heatmap
        cosine_values = [
            [0.51, 0.28, 0.08, 0.07, 0.09, 0.16, 0.05, 0.50, 0.73],
            [0.20, 0.24, 0.27, 0.09, 0.18, 0.15, 0.19, 0.21, 0.21],
            [0.12, 0.15, 0.15, 0.17, 0.12, 0.58, 0.12, 0.21, 0.17],
            [0.61, 0.37, 0.28, 0.19, 0.14, 0.35, 0.16, 0.86, 0.66],
            [0.30, 0.30, 0.38, 0.18, 0.10, 0.22, 0.09, 0.19, 0.30],
            [0.51, 0.34, 0.12, 0.06, 0.12, 0.19, 0.15, 0.52, 0.53],
            [0.26, 0.27, 0.80, 0.24, 0.20, 0.19, 0.27, 0.23, 0.22],
            [0.49, 0.87, 0.33, 0.27, 0.23, 0.29, 0.17, 0.34, 0.38],
            [0.94, 0.47, 0.33, 0.17, 0.14, 0.38, 0.18, 0.62, 0.77],
        ]
        
        heatmap_values = VGroup()
        for i in range(num_rows):
            for j in range(num_cols):
                cell_x = anchor[0] + (j + 0.5) * dx
                cell_y = anchor[1] + (i + 0.5) * dy
                
                value = cosine_values[8-i][j]  # Use 8-i to invert the row order 
                value_text = Text(f"{value:.2f}", font_size=14, color=WHITE)
                value_text.move_to([cell_x, cell_y, 0])
                
                heatmap_values.add(value_text)

        idx_077 = 0 * num_cols + 8   # bottom row i=0, 9th column j=8
        value_077 = heatmap_values[idx_077]
        
        # Group all heatmap elements
        heatmap_elements = VGroup(
            y_axis, x_axis,
            grid_lines,
            y_labels, x_labels,
            heatmap_values
        )
        
        # Add formula on the right (optional - same as shown in the screenshot)
        formula_x = anchor[0] + x_length + 4.3
        formula_y = anchor[1] + y_length * 0.5
        
        small_box_size = 0.19
        ref_box = RoundedRectangle(
            width=small_box_size*1.2,
            height=small_box_size*1.2,
            corner_radius=0.03,
            color=WHITE,
            fill_color=BLUE_E,
            fill_opacity=0.7,
            stroke_width=0.8
        )
        ref_element = ref_box
        
        gen_box = RoundedRectangle(
            width=small_box_size*1.2,
            height=small_box_size*1.2,
            corner_radius=0.03,
            color=WHITE,
            fill_color=MAROON_B,
            fill_opacity=0.7,
            stroke_width=0.8
        )
        gen_element = gen_box
        
        # Fade in all elements at once - removed formula
        self.play(
            FadeIn(right_side_elements),
            FadeIn(heatmap_elements),
            run_time=1.5
        )
        
        self.wait(1.0)

        # ================== MAIN HEADING AND UNDERLINE ==================
        main_heading = Text(
            "Finding Column-Wise Best Match",
            font_size=18,  color=WHITE,  weight="BOLD"
        )
        main_heading.next_to(heatmap_elements, UP, buff=0.35)   # <- new
        main_heading.align_to(heatmap_elements, LEFT)           # <- new

        main_heading.shift(RIGHT * 0.5)

        heading_underline = Underline(main_heading)
        heading_underline.next_to(main_heading, DOWN, buff=0.05)
        heading_underline.align_to(main_heading, LEFT)          # <- keeps it flush
        self.play(Write(main_heading), Create(heading_underline), run_time=0.6)

        # Simultaneously fade out the right side elements and shift the heatmap and box
        self.play(
            FadeOut(right_side_elements),
            # heatmap_and_box_group.animate.shift(shift_right_distance),
            run_time=1.0
        )

        self.wait(0.5)

        # ================== SECTION HEADERS AND INFO BOXES ==================
        def create_section_header(text_content, width=7.0):
            """Create a visually distinct header with background"""
            header_bg = RoundedRectangle(
                width=width,
                height=0.4,
                corner_radius=0.1,
                color=BLUE,
                fill_color=BLUE_E,
                fill_opacity=0.3,
                stroke_width=1
            )
            
            header_text = Text(
                text_content,
                font_size=15,
                color=WHITE,
                weight="BOLD"
            )
            
            header_text.move_to(header_bg.get_center())
            header = VGroup(header_bg, header_text)
            return header
        
        def create_info_box(text_content, width=7.0, height=0.5, fill_color=BLUE_E, fill_opacity=0.1):
            """Create an information box with text inside"""
            box = RoundedRectangle(
                width=width,
                height=height,
                corner_radius=0.1,
                color=WHITE,
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_width=0.5
            )
            
            text = Text(text_content, font_size=15, color=WHITE)
            text.move_to(box.get_center())
            
            result = VGroup(box, text)
            return result
        
        def create_result_box(text_content, width=7.0, height=None, fill_color=GREEN_E, fill_opacity=0.2):
            """Create a highlighted result box"""
            # If multiple lines, adjust height based on text content
            lines = text_content.count('\n') + 1
            if height is None:
                height = 0.4 * lines
            
            box = RoundedRectangle(
                width=width,
                height=height,
                corner_radius=0.1,
                color=GREEN,
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_width=1
            )
            
            text = Text(text_content, font_size=15, color=WHITE)
            text.move_to(box.get_center())
            
            result = VGroup(box, text)
            return result
        
        def create_progress_indicator(current_column, total_columns=9, width=4.3):
            """Create a progress indicator showing current column analysis"""
            progress_group = VGroup()
            segment_width = width / total_columns
            
            for i in range(1, total_columns+1):
                segment = Rectangle(
                    width=segment_width - 0.05,  # Small gap between segments
                    height=0.25,
                    color=WHITE,
                    fill_color=BLUE_E if i <= current_column else GREY,
                    fill_opacity=0.6 if i <= current_column else 0.2,
                    stroke_width=0.5
                )
                
                # Position segments in a row
                if i == 1:
                    segment.align_to(LEFT * 3, LEFT)
                else:
                    segment.next_to(progress_group[-1], RIGHT, buff=0.05)
                
                # Add column number
                number = Text(str(i), font_size=12, color=WHITE)
                number.move_to(segment.get_center())
                
                segment_group = VGroup(segment, number)
                progress_group.add(segment_group)
            
            progress_label = Text("Column Progress:", font_size=10, color=WHITE)
            progress_label.next_to(progress_group, LEFT, buff=0.2)
            
            full_progress = VGroup(progress_label, progress_group)
            return full_progress
            
        # ================== ALGORITHM EXECUTION DISPLAY ==================
        # Create interface for showing step-by-step best matching algorithm execution
        
        # Create a new rectangular box on the right side
        new_box = Rectangle(
            width=7.5, 
            height=6.5, 
            color=WHITE,
            stroke_width=2
        )
        # Position the box on the right side where the segments were
        new_box.move_to([3.0, -0.4, 0])  # Adjust x-coordinate to move left/right

        # Create heading
        new_heading = Text("Finding Column-Wise Best Match", font_size=13, color=WHITE)
        new_underline = Underline(new_heading)

        # Position heading at the top of the box
        new_heading.move_to(new_box.get_corner(UP + LEFT) + RIGHT * 1.6 + DOWN * 0.2)

        # Position underline right under the heading
        new_underline.next_to(new_heading, DOWN, buff=0.08)

        # Create text content
        new_text = Text(
            "1. Mapping Window = [Row / Column] = 9/9 = 1",
            font_size=15, 
            color=WHITE
        )

        # Position text below the heading, aligned to the left margin
        new_text.next_to(new_underline, DOWN, buff=0.15)
        new_text.align_to(new_heading, LEFT)

        # Create diagonal highlights
        diagonal_highlights = VGroup()
        # Track diagonal values to highlight
        diagonal_indices = [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)]

        for i, j in diagonal_indices:
            cell_x = anchor[0] + (j + 0.5) * dx
            cell_y = anchor[1] + ((8-i) + 0.5) * dy  # Using 8-i because rows are inverted
            
            # Create a red rectangle for background highlight
            highlight_rect = Rectangle(
                width=dx,
                height=dy,
                color=RED,
                fill_color=RED,
                fill_opacity=0.3,
                stroke_width=0
            )
            highlight_rect.move_to([cell_x, cell_y, 0])
            diagonal_highlights.add(highlight_rect)

        # Animate the new elements on the right side
        self.play(Create(new_box), run_time=0.5)
        self.play(Write(new_heading), run_time=0.5)
        self.play(Create(new_underline), run_time=0.3)
        self.play(Write(new_text), run_time=1.0)
       
        # Animate the highlights when the Mapping Window text is written
        self.play(
            LaggedStart(*[FadeIn(rect) for rect in diagonal_highlights], lag_ratio=0.1),
            run_time=1.5
        )

        self.wait(2)

        # ================== COLUMN 9 ANALYSIS - BEST MATCHING ALGORITHM ==================
        # Demonstrate algorithm execution for finding best matches in column 9
        # Create progress indicator for column 9
        progress_indicator = create_progress_indicator(9)
        progress_indicator.next_to(heatmap_elements, DOWN, buff=0.3)
        
        # Create a header for Column 9
        col9_header = create_section_header("COLUMN 9 ANALYSIS")
        col9_header.next_to(new_text, DOWN, buff=0.4)
        col9_header.align_to(new_heading, LEFT)
        
        # Create data points box
        col9_data = create_info_box("1. Max Value: 0.77 (Location: Row 9)", 
                                   fill_color=BLUE_E, 
                                   fill_opacity=0.1)
        col9_data.next_to(col9_header, DOWN, buff=0.2)
        col9_data.align_to(new_heading, LEFT)
        cell_x = anchor[0] + (8 + 0.5) * dx  # 9th column (index 8)
        cell_y = anchor[1] + (0 + 0.5) * dy  # Bottom row (index 0)
        
        # ================== HYSTERESIS CALCULATION ==================
        # Mathematical computation for similarity score adjustment
        hysteresis_calc_label = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula = MathTex(
            r"\frac{0.4 - (1 - 0.77)}{0.77} \times 5 = 0.04", # Formula for Col 9
            font_size=15
        )

        # 1. Group the label and formula
        hysteresis_calc_group = VGroup(hysteresis_calc_label, hysteresis_calc_formula)

        # 2. Arrange them centrally
        hysteresis_calc_group.arrange(DOWN, buff=0.15, center=True)

        # 3. Create the box
        calc_box = RoundedRectangle(
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )

        # 4. Make the box surround the centrally arranged group
        calc_box.surround(hysteresis_calc_group, buff=0.2)

        # 4a. <<<<<<< ADD THIS LINE >>>>>>>>>
        # Explicitly move the text group to the center of the now-defined box
        hysteresis_calc_group.move_to(calc_box.get_center())

        # 5. Group the box and the text_group for overall positioning
        hysteresis_container = VGroup(calc_box, hysteresis_calc_group)

        # Positioning the entire container
        hysteresis_container.next_to(col9_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col9_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])
        # --- End of Hysteresis Calculation section ---
        
        # Create range text with container
        range_box = create_info_box(
            "3. Range of Best Matches = 0.77 - 0.04 = [0.73,0.77]",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box.next_to(hysteresis_container, DOWN, buff=0.2)
        range_box.align_to(new_heading, LEFT)
        
        # Create potential matches box
        potential_match_box = create_info_box(
            "4. Potential Best Match = 0.77, 0.73",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box.next_to(range_box, DOWN, buff=0.2)
        potential_match_box.align_to(new_heading, LEFT)
        
        # Create result box
        distance_result = create_result_box(
            "5. Calculating the distance:\n   d0 (0.73) = 0 and d1 (0.77) = 8",
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        distance_result.next_to(potential_match_box, DOWN, buff=0.2)
        distance_result.align_to(new_heading, LEFT)
        
        # Animate the enhanced elements
        self.play(FadeIn(progress_indicator), run_time=0.8)
        self.play(Write(col9_header), run_time=0.8)
        self.wait(0.2)
        
        self.play(
            Write(col9_data),
            # FadeIn(cell_highlight),
            run_time=0.8
        )
        self.wait(0.2)
        
        self.play(
            FadeIn(hysteresis_container),
            # GrowArrow(column_indicator_arrow),
            run_time=0.8
        )
        self.wait(0.2)
        
        self.play(FadeIn(range_box), run_time=0.8)
        self.wait(0.2)
        
        # Find all values in the 9th column (index 8)
        column_9_values = []
        for i in range(num_rows):
            # Get the value text object for this cell
            value_idx = i * num_cols + 8  # Calculate index in the flattened heatmap_values
            value_obj = heatmap_values[value_idx]
            
            # Store reference to values not being highlighted (not 0.77 or 0.73)
            value = cosine_values[8-i][8]  # Get value from matrix
            if abs(value - 0.77) > 0.01 and abs(value - 0.73) > 0.01:  # Not 0.77 or 0.73
                column_9_values.append(value_obj)

        # Create highlight rectangle for 0.77 value
        highlight_077 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0,  # No fill, just border
            stroke_width=3   
        )
        highlight_077.move_to([cell_x, cell_y, 0])

        # Create highlight for the 0.73 cell
        highlight_073 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,  # No fill, just border
            stroke_width=3   
        )
        # Position the highlight at the 0.73 cell location
        cell_073_x = anchor[0] + (8 + 0.5) * dx  # 9th column (index 8)
        cell_073_y = anchor[1] + (8 + 0.5) * dy  # Top row (for 0.73)
        highlight_073.move_to([cell_073_x, cell_073_y, 0])
        
        self.play(FadeIn(potential_match_box), run_time=0.8)
        self.wait(0.2)
        
        # Fade out non-highlighted values and highlight both cells
        self.play(
            *[FadeOut(val) for val in column_9_values],
            FadeIn(highlight_077),
            FadeIn(highlight_073),
            run_time=1.0
        )
        
        self.play(FadeIn(distance_result), run_time=0.8)
        self.wait(0.2)
        
        # Find the position of the 0.73 cell (diagonal element in column 9)
        cell_073_x = anchor[0] + (8 + 0.5) * dx  # 9th column (index 8)
        cell_073_y = anchor[1] + (8 + 0.5) * dy  # Top row (for 0.73)

        # Find the position of the 0.77 cell (bottom row in column 9)
        cell_077_x = anchor[0] + (8 + 0.5) * dx  # 9th column (index 8)
        cell_077_y = anchor[1] + (0 + 0.5) * dy  # Bottom row (for 0.77)

        # Define control points for a cubic bezier curve
        start_point = [cell_073_x + dx/2, cell_073_y, 0]  # Right border
        end_point = [cell_073_x, cell_073_y + dy/2, 0]    # Top border (directly on top)
        control1 = [cell_073_x + dx*0.8, cell_073_y + dy*0.6, 0]  # Adjusted control point
        control2 = [cell_073_x + dx*0.3, cell_073_y + dy*0.9, 0]  # Adjusted control point

        # Create curved path
        curved_path = CubicBezier(start_point, control1, control2, end_point)
        curved_path.set_color(WHITE)
        curved_path.set_stroke(width=2.0)

        # Create a smaller triangle for arrow tip
        arrow_tip = Triangle(fill_color=WHITE, fill_opacity=1, stroke_width=0)
        arrow_tip.scale(0.08)  # Make it significantly smaller

        # Calculate the angle at the end of the path
        end_direction = curved_path.get_end() - curved_path.point_from_proportion(0.95)
        angle = np.angle(complex(end_direction[0], end_direction[1]))
        arrow_tip.rotate(angle - PI/2)  # Rotate to align with path tangent

        # Position at the exact end of the curve
        arrow_tip.move_to(curved_path.get_end())

        # Group them to create a self-arrow
        self_arrow = VGroup(curved_path, arrow_tip)

        # Create a straight arrow from 0.77 cell to 0.73 cell
        column_arrow = Arrow(
            start=[cell_077_x, cell_077_y + dy/2, 0],  # Top of 0.77 cell
            end=[cell_073_x, cell_073_y - dy/2, 0],    # Bottom of 0.73 cell
            buff=0.05,  # Smaller buffer
            color=WHITE,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.04  # Smaller arrow head
        )

        # Draw the self arrow
        self.play(Create(curved_path), FadeIn(arrow_tip), run_time=0.8)  
        self.wait(0.2)

        # Draw the straight arrow
        self.play(GrowArrow(column_arrow), run_time=1.0)

        self.wait(1.0)

        # Fade out all column 9 elements
        self.play(
            FadeOut(col9_header),
            FadeOut(col9_data),
            FadeOut(hysteresis_container),
            FadeOut(range_box),
            FadeOut(potential_match_box),
            FadeOut(distance_result),
            FadeOut(highlight_077),
            FadeOut(value_077),
            FadeOut(self_arrow),
            FadeOut(column_arrow),
            run_time=1.0
        )

        self.wait(0.5)

        # -------------------- ENHANCED VERSION OF COLUMN 8 PRESENTATION --------------------
        # Update progress indicator for column 8
        progress_indicator_8 = create_progress_indicator(8)
        progress_indicator_8.move_to(progress_indicator)           # keep position
        self.play(ReplacementTransform(progress_indicator, progress_indicator_8),
                  run_time=0.8)
        progress_indicator = progress_indicator_8  
        
        # Create a header for Column 8
        col8_header = create_section_header("COLUMN 8 ANALYSIS")
        col8_header.next_to(new_text, DOWN, buff=0.4)
        col8_header.align_to(new_heading, LEFT)
        
        # Create data points box
        col8_data = create_info_box("1. Max Value: 0.86 (Location: Row 6)", 
                                   fill_color=BLUE_E, 
                                   fill_opacity=0.1)
        col8_data.next_to(col8_header, DOWN, buff=0.2)
        col8_data.align_to(new_heading, LEFT)
        
        # Create highlight for the 0.86 cell
        cell_highlight_8 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        cell_x_8 = anchor[0] + (7 + 0.5) * dx  # 8th column (index 7)
        cell_y_8 = anchor[1] + (5 + 0.5) * dy  # Row index 5 (for value 0.86)
        cell_highlight_8.move_to([cell_x_8, cell_y_8, 0])
        
        # Create hysteresis calculation box
        hysteresis_calc_label_8 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula_8 = MathTex(
            r"\frac{0.4 - (1 - 0.86)}{0.86} \times 5 = 0.06",
            font_size=15
        )
        hysteresis_calc_group_8 = VGroup(hysteresis_calc_label_8, hysteresis_calc_formula_8)
        hysteresis_calc_group_8.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        # Create a container for the calculation
        calc_box_8 = RoundedRectangle(
            width=6.5,
            height=1.1,
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )
        calc_box_8.move_to(hysteresis_calc_group_8.get_center())
        calc_box_8.stretch_to_fit_width(hysteresis_calc_group_8.get_width() + 0.4)
        calc_box_8.stretch_to_fit_height(hysteresis_calc_group_8.get_height() + 0.4)
        
        # Group the calculation and its container
        hysteresis_container_8 = VGroup(calc_box_8, hysteresis_calc_group_8)
        hysteresis_container_8.next_to(col8_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col8_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])
        
        # Create range text with container
        range_box_8 = create_info_box(
            "3. Range of Best Matches = 0.86 - 0.06 = [0.80,0.86]",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_8.next_to(hysteresis_container_8, DOWN, buff=0.2)
        range_box_8.align_to(new_heading, LEFT)
        
        # Create potential matches box
        potential_match_box_8 = create_info_box(
            "4. Potential Best Match = 0.86",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_8.next_to(range_box_8, DOWN, buff=0.2)
        potential_match_box_8.align_to(new_heading, LEFT)
        
        # Create conclusion box
        conclusion_box_8 = create_result_box(
            "RESULT: Since there is no other value within\nthe range, the best match is 0.86",
            height=0.8,
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        conclusion_box_8.next_to(potential_match_box_8, DOWN, buff=0.2)
        conclusion_box_8.align_to(new_heading, LEFT)
        
        # Animate the enhanced elements for column 8
        self.play(
            ReplacementTransform(progress_indicator, progress_indicator_8),
            run_time=0.8
        )
        self.play(Write(col8_header), run_time=0.8)
        self.wait(0.2)
        
        self.play(
            Write(col8_data),
            FadeIn(cell_highlight_8),
            # GrowArrow(column_indicator_arrow_8),
            run_time=0.8
        )
        self.wait(0.2)
        
        self.play(
            FadeIn(hysteresis_container_8),
            run_time=0.8
        )
        self.wait(0.2)
        
        self.play(FadeIn(range_box_8), run_time=0.8)
        self.wait(0.2)
        
        self.play(FadeIn(potential_match_box_8), run_time=0.8)
        self.wait(0.2)
        
        # Find all values in the 8th column (index 7) to fade out
        column_8_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 7
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][7]
            if abs(value - 0.86) > 0.01:
                column_8_values.append(value_obj)
        
        # Highlight for 0.86 value
        highlight_086 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0,
            stroke_width=3
        )
        highlight_086.move_to([cell_x_8, cell_y_8, 0])
        
        # Fade out all other values in column 8 except 0.86
        self.play(
            *[FadeOut(val) for val in column_8_values],
            run_time=0.8
        )
        
        self.play(
            FadeIn(highlight_086),
            run_time=0.8
        )
        
        # Animate the conclusion
        self.play(FadeIn(conclusion_box_8), run_time=0.8)
        
        self.wait(1.5)
        
        # Fade out column 8 elements
        self.play(
            FadeOut(col8_header),
            FadeOut(col8_data),
            FadeOut(hysteresis_container_8),
            FadeOut(range_box_8),
            FadeOut(potential_match_box_8),
            FadeOut(conclusion_box_8),
            FadeOut(highlight_086),
            run_time=1.0
        )
        
        self.wait(0.5)



        # -------------------- ENHANCED VERSION OF COLUMN 7 PRESENTATION --------------------
        # Update progress indicator for column 7
        progress_indicator_7 = create_progress_indicator(7)
        progress_indicator_7.move_to(progress_indicator)
        self.play(ReplacementTransform(progress_indicator, progress_indicator_7),
                  run_time=0.8)
        progress_indicator = progress_indicator_7

        # Create a header for Column 7
        col7_header = create_section_header("COLUMN 7 ANALYSIS")
        col7_header.next_to(new_text, DOWN, buff=0.4)
        col7_header.align_to(new_heading, LEFT)

        # Create data points box
        col7_data = create_info_box("1. Max Value: 0.27 (Location: Row 3)", 
                                fill_color=BLUE_E, 
                                fill_opacity=0.1)
        col7_data.next_to(col7_header, DOWN, buff=0.2)
        col7_data.align_to(new_heading, LEFT)

        # Create highlight for the 0.27 cell
        cell_highlight_7 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        cell_x_7 = anchor[0] + (6 + 0.5) * dx  # 7th column (index 6)
        cell_y_7 = anchor[1] + (2 + 0.5) * dy  # Row index 2 (for value 0.27)
        cell_highlight_7.move_to([cell_x_7, cell_y_7, 0])

        # Create hysteresis calculation box
        hysteresis_calc_label_7 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula_7 = MathTex(
            r"\frac{0.4 - (1 - 0.27)}{0.27} \times 5 = -0.24",
            font_size=15
        )
        hysteresis_calc_group_7 = VGroup(hysteresis_calc_label_7, hysteresis_calc_formula_7)
        hysteresis_calc_group_7.arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # Create a container for the calculation
        calc_box_7 = RoundedRectangle(
            width=6.5,
            height=1.1,
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )
        calc_box_7.move_to(hysteresis_calc_group_7.get_center())
        calc_box_7.stretch_to_fit_width(hysteresis_calc_group_7.get_width() + 0.4)
        calc_box_7.stretch_to_fit_height(hysteresis_calc_group_7.get_height() + 0.4)

        # Group the calculation and its container
        hysteresis_container_7 = VGroup(calc_box_7, hysteresis_calc_group_7)
        hysteresis_container_7.next_to(col7_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col7_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])

        # Create range text with container
        range_box_7 = create_info_box(
            "3. Range of Best Matches = 0.27 - (-0.24) = Not Valid",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_7.next_to(hysteresis_container_7, DOWN, buff=0.2)
        range_box_7.align_to(new_heading, LEFT)

        # Create potential matches box
        potential_match_box_7 = create_info_box(
            "4. Potential Best Match = 0.27",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_7.next_to(range_box_7, DOWN, buff=0.2)
        potential_match_box_7.align_to(new_heading, LEFT)

        # Create result box
        result_box_7 = create_result_box(
            "5. Since the numerator is less, the overall value drops\n   below 0 which is less than 0.6 (HCF)",
            height=0.8,
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        result_box_7.next_to(potential_match_box_7, DOWN, buff=0.2)
        result_box_7.align_to(new_heading, LEFT)

        # Animate the enhanced elements for column 7
        self.play(
            ReplacementTransform(progress_indicator_8, progress_indicator_7),
            run_time=0.8
        )
        self.play(Write(col7_header), run_time=0.8)
        self.wait(0.2)

        self.play(
            Write(col7_data),
            FadeIn(cell_highlight_7),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(
            FadeIn(hysteresis_container_7),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(FadeIn(range_box_7), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(potential_match_box_7), run_time=0.8)
        self.wait(0.2)

        # Find all values in the 7th column (index 6) to fade out
        column_7_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 6
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][6]
            if abs(value - 0.27) > 0.01:
                column_7_values.append(value_obj)

        # Fade out all other values in column 7 except 0.27
        self.play(
            *[FadeOut(val) for val in column_7_values],
            run_time=0.8
        )

        self.play(FadeIn(result_box_7), run_time=0.8)

        self.wait(1.5)

        # Fade out column 7 elements
        self.play(
            FadeOut(col7_header),
            FadeOut(col7_data),
            FadeOut(hysteresis_container_7),
            FadeOut(range_box_7),
            FadeOut(potential_match_box_7),
            FadeOut(result_box_7),
            run_time=1.0
        )

        self.wait(0.5)

        # -------------------- ENHANCED VERSION OF COLUMN 6 PRESENTATION --------------------
        # Update progress indicator for column 6
        progress_indicator_6 = create_progress_indicator(6)
        progress_indicator_6.move_to(progress_indicator)
        self.play(ReplacementTransform(progress_indicator, progress_indicator_6),
                  run_time=0.8)
        progress_indicator = progress_indicator_6

        # Create a header for Column 6
        col6_header = create_section_header("COLUMN 6 ANALYSIS")
        col6_header.next_to(new_text, DOWN, buff=0.4)
        col6_header.align_to(new_heading, LEFT)

        # Create data points box
        col6_data = create_info_box("1. Max Value: 0.58 (Location: Row 3)", 
                                fill_color=BLUE_E, 
                                fill_opacity=0.1)
        col6_data.next_to(col6_header, DOWN, buff=0.2)
        col6_data.align_to(new_heading, LEFT)

        # Create highlight for the 0.58 cell
        cell_highlight_6 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        cell_x_6 = anchor[0] + (5 + 0.5) * dx  # 6th column (index 5)
        cell_y_6 = anchor[1] + (6 + 0.5) * dy  # Row position for 0.58
        cell_highlight_6.move_to([cell_x_6, cell_y_6, 0])

       # Create hysteresis calculation box
        hysteresis_calc_label_6 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula_6 = MathTex(
            r"\frac{0.4 - (1 - 0.58)}{0.58} \times 5 = -0.006",
            font_size=15
        )
        hysteresis_calc_group_6 = VGroup(hysteresis_calc_label_6, hysteresis_calc_formula_6)
        # MODIFICATION: Center the text group's content
        hysteresis_calc_group_6.arrange(DOWN, buff=0.15, center=True) # Use center=True and consistent buff

        # Create a container for the calculation
        calc_box_6 = RoundedRectangle(
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )

        # OPTION 1: Adaptive sizing using surround (Recommended for consistency)
        calc_box_6.surround(hysteresis_calc_group_6, buff=0.2)

        # Group the calculation and its container
        hysteresis_container_6 = VGroup(calc_box_6, hysteresis_calc_group_6)

        # MODIFICATION: Ensure text group is centered within the sized box
        hysteresis_calc_group_6.move_to(calc_box_6.get_center())

        hysteresis_container_6.next_to(col6_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col6_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])

        # Create range text with container
        range_box_6 = create_info_box(
            "3. Range of Best Matches = 0.58 - (-0.006) = Not Valid",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_6.next_to(hysteresis_container_6, DOWN, buff=0.2)
        range_box_6.align_to(new_heading, LEFT)

        # Create potential matches box
        potential_match_box_6 = create_info_box(
            "4. Potential Best Match = 0.58",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_6.next_to(range_box_6, DOWN, buff=0.2)
        potential_match_box_6.align_to(new_heading, LEFT)

        # Create result box
        result_box_6 = create_result_box(
            "5. Since the numerator is less, the overall value drops\n   below 0 which is less than 0.6 (HCF)",
            height=0.8,
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        result_box_6.next_to(potential_match_box_6, DOWN, buff=0.2)
        result_box_6.align_to(new_heading, LEFT)

        # Animate the enhanced elements for column 6
        self.play(
            ReplacementTransform(progress_indicator_7, progress_indicator_6),
            run_time=0.8
        )
        self.play(Write(col6_header), run_time=0.8)
        self.wait(0.2)

        self.play(
            Write(col6_data),
            FadeIn(cell_highlight_6),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(
            FadeIn(hysteresis_container_6),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(FadeIn(range_box_6), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(potential_match_box_6), run_time=0.8)
        self.wait(0.2)

        # Find all values in column 6 to fade out
        column_6_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 5
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][5]
            if abs(value - 0.58) > 0.01:
                column_6_values.append(value_obj)

        # Fade out all other values
        self.play(
            *[FadeOut(val) for val in column_6_values],
            run_time=0.8
        )

        self.play(FadeIn(result_box_6), run_time=0.8)

        self.wait(1.5)

        # Fade out column 6 elements
        self.play(
            FadeOut(col6_header),
            FadeOut(col6_data),
            FadeOut(hysteresis_container_6),
            FadeOut(range_box_6),
            FadeOut(potential_match_box_6),
            FadeOut(result_box_6),
            run_time=1.0
        )

        self.wait(0.5)

        # -------------------- ENHANCED VERSION OF COLUMN 5 PRESENTATION --------------------
        # Update progress indicator for column 5
        progress_indicator_5 = create_progress_indicator(5)
        progress_indicator_5.move_to(progress_indicator)
        self.play(ReplacementTransform(progress_indicator, progress_indicator_5),
                  run_time=0.8)
        progress_indicator = progress_indicator_5

        # Create a header for Column 5
        col5_header = create_section_header("COLUMN 5 ANALYSIS")
        col5_header.next_to(new_text, DOWN, buff=0.4)
        col5_header.align_to(new_heading, LEFT)

        # Create data points box
        col5_data = create_info_box("1. Max Value: 0.23 (Location: Row 7)", 
                                fill_color=BLUE_E, 
                                fill_opacity=0.1)
        col5_data.next_to(col5_header, DOWN, buff=0.2)
        col5_data.align_to(new_heading, LEFT)

        # Create highlight for the max value cell
        cell_highlight_5 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        cell_x_5 = anchor[0] + (4 + 0.5) * dx  # 5th column (index 4)
        cell_y_5 = anchor[1] + (1 + 0.5) * dy  # Row position for max value
        cell_highlight_5.move_to([cell_x_5, cell_y_5, 0])

        # Create hysteresis calculation box
        hysteresis_calc_label_5 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula_5 = MathTex(
            r"\frac{0.4 - (1 - 0.23)}{0.23} \times 5 = -0.32",
            font_size=15
        )
        hysteresis_calc_group_5 = VGroup(hysteresis_calc_label_5, hysteresis_calc_formula_5)
        hysteresis_calc_group_5.arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # Create a container for the calculation
        calc_box_5 = RoundedRectangle(
            width=6.5,
            height=1.1,
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )
        calc_box_5.move_to(hysteresis_calc_group_5.get_center())
        calc_box_5.stretch_to_fit_width(hysteresis_calc_group_5.get_width() + 0.4)
        calc_box_5.stretch_to_fit_height(hysteresis_calc_group_5.get_height() + 0.4)

        # Group the calculation and its container
        hysteresis_container_5 = VGroup(calc_box_5, hysteresis_calc_group_5)
        hysteresis_container_5.next_to(col5_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col5_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])

        # Create range text with container
        range_box_5 = create_info_box(
            "3. Range of Best Matches = 0.23 - (-0.32) = Not Valid",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_5.next_to(hysteresis_container_5, DOWN, buff=0.2)
        range_box_5.align_to(new_heading, LEFT)

        # Create potential matches box
        potential_match_box_5 = create_info_box(
            "4. Potential Best Match = 0.23",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_5.next_to(range_box_5, DOWN, buff=0.2)
        potential_match_box_5.align_to(new_heading, LEFT)

        # Create result box
        result_box_5 = create_result_box(
            "5. Since the numerator is less, the overall value drops\n   below 0 which is less than 0.6 (HCF)",
            height=0.8,
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        result_box_5.next_to(potential_match_box_5, DOWN, buff=0.2)
        result_box_5.align_to(new_heading, LEFT)

        # Animate the enhanced elements for column 5
        self.play(
            ReplacementTransform(progress_indicator_6, progress_indicator_5),
            run_time=0.8
        )
        self.play(Write(col5_header), run_time=0.8)
        self.wait(0.2)

        self.play(
            Write(col5_data),
            FadeIn(cell_highlight_5),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(
            FadeIn(hysteresis_container_5),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(FadeIn(range_box_5), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(potential_match_box_5), run_time=0.8)
        self.wait(0.2)

        # Find all values in column 5 to fade out
        column_5_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 4
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][4]
            if abs(value - 0.23) > 0.01:
                column_5_values.append(value_obj)

        # Fade out all other values
        self.play(
            *[FadeOut(val) for val in column_5_values],
            run_time=0.8
        )

        self.play(FadeIn(result_box_5), run_time=0.8)

        self.wait(1.5)

        # Fade out column 5 elements
        self.play(
            FadeOut(col5_header),
            FadeOut(col5_data),
            FadeOut(hysteresis_container_5),
            FadeOut(range_box_5),
            FadeOut(potential_match_box_5),
            FadeOut(result_box_5),
            run_time=1.0
        )

        self.wait(0.5)

        # -------------------- ENHANCED VERSION OF COLUMN 4 PRESENTATION --------------------
        # Update progress indicator for column 4
        progress_indicator_4 = create_progress_indicator(4)
        progress_indicator_4.move_to(progress_indicator)
        self.play(ReplacementTransform(progress_indicator, progress_indicator_4),
                  run_time=0.8)
        progress_indicator = progress_indicator_4

        # Create a header for Column 4
        col4_header = create_section_header("COLUMN 4 ANALYSIS")
        col4_header.next_to(new_text, DOWN, buff=0.4)
        col4_header.align_to(new_heading, LEFT)

        # Create data points box
        col4_data = create_info_box("1. Max Value: 0.27 (Location: Row 2)", 
                                fill_color=BLUE_E, 
                                fill_opacity=0.1)
        col4_data.next_to(col4_header, DOWN, buff=0.2)
        col4_data.align_to(new_heading, LEFT)

        # Create highlight for the 0.27 cell
        cell_highlight_4 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        # Find the row position for the 0.27 value in column 4 (index 3)
        cell_x_4 = anchor[0] + (3 + 0.5) * dx  # 4th column (index 3)
        cell_y_4 = anchor[1] + (1 + 0.5) * dy  # Row position for 0.27
        cell_highlight_4.move_to([cell_x_4, cell_y_4, 0])

        # Create hysteresis calculation box
        hysteresis_calc_label_4 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula_4 = MathTex(
            r"\frac{0.4 - (1 - 0.27)}{0.27} \times 5 = -0.24",
            font_size=15
        )
        hysteresis_calc_group_4 = VGroup(hysteresis_calc_label_4, hysteresis_calc_formula_4)
        hysteresis_calc_group_4.arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # Create a container for the calculation
        calc_box_4 = RoundedRectangle(
            width=6.5,
            height=1.1,
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )
        calc_box_4.move_to(hysteresis_calc_group_4.get_center())
        calc_box_4.stretch_to_fit_width(hysteresis_calc_group_4.get_width() + 0.4)
        calc_box_4.stretch_to_fit_height(hysteresis_calc_group_4.get_height() + 0.4)

        # Group the calculation and its container
        hysteresis_container_4 = VGroup(calc_box_4, hysteresis_calc_group_4)
        hysteresis_container_4.next_to(col4_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col4_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])

        # Create range text with container
        range_box_4 = create_info_box(
            "3. Range of Best Matches = 0.27 - (-0.24) = Not Valid",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_4.next_to(hysteresis_container_4, DOWN, buff=0.2)
        range_box_4.align_to(new_heading, LEFT)

        # Create potential matches box
        potential_match_box_4 = create_info_box(
            "4. Potential Best Match = 0.27",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_4.next_to(range_box_4, DOWN, buff=0.2)
        potential_match_box_4.align_to(new_heading, LEFT)

        # Create result box
        result_box_4 = create_result_box(
            "5. Since the numerator is less, the overall value drops\n   below 0 which is less than 0.6 (HCF)",
            height=0.8,
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        result_box_4.next_to(potential_match_box_4, DOWN, buff=0.2)
        result_box_4.align_to(new_heading, LEFT)

        # Animate the enhanced elements for column 4
        self.play(
            ReplacementTransform(progress_indicator_5, progress_indicator_4),
            run_time=0.8
        )
        self.play(Write(col4_header), run_time=0.8)
        self.wait(0.2)

        self.play(
            Write(col4_data),
            FadeIn(cell_highlight_4),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(
            FadeIn(hysteresis_container_4),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(FadeIn(range_box_4), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(potential_match_box_4), run_time=0.8)
        self.wait(0.2)

        # Find all values in column 4 to fade out
        column_4_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 3
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][3]
            if abs(value - 0.27) > 0.01:
                column_4_values.append(value_obj)

        # Fade out all other values
        self.play(
            *[FadeOut(val) for val in column_4_values],
            run_time=0.8
        )

        self.play(FadeIn(result_box_4), run_time=0.8)

        self.wait(1.5)

        # Fade out column 4 elements
        self.play(
            FadeOut(col4_header),
            FadeOut(col4_data),
            FadeOut(hysteresis_container_4),
            FadeOut(range_box_4),
            FadeOut(potential_match_box_4),
            FadeOut(result_box_4),
            run_time=1.0
        )

        self.wait(0.5)

        # -------------------- ENHANCED VERSION OF COLUMN 3 PRESENTATION --------------------
        # Update progress indicator for column 3
        progress_indicator_3 = create_progress_indicator(3)
        progress_indicator_3.move_to(progress_indicator)
        self.play(ReplacementTransform(progress_indicator, progress_indicator_3),
                  run_time=0.8)
        progress_indicator = progress_indicator_3

        # Create a header for Column 3
        col3_header = create_section_header("COLUMN 3 ANALYSIS")
        col3_header.next_to(new_text, DOWN, buff=0.4)
        col3_header.align_to(new_heading, LEFT)

        # Create data points box
        col3_data = create_info_box("1. Max Value: 0.80 (Location: Row 7)", 
                                fill_color=BLUE_E, 
                                fill_opacity=0.1)
        col3_data.next_to(col3_header, DOWN, buff=0.2)
        col3_data.align_to(new_heading, LEFT)

        # Create highlight for the 0.80 cell
        cell_highlight_3 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        cell_x_3 = anchor[0] + (2 + 0.5) * dx  # 3rd column (index 2)
        cell_y_3 = anchor[1] + (2 + 0.5) * dy  # Row position for 0.80
        cell_highlight_3.move_to([cell_x_3, cell_y_3, 0])

        # Create hysteresis calculation box
        hysteresis_calc_label_3 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        
        hysteresis_calc_formula_3 = MathTex(
            r"\frac{0.4 - (1 - 0.80)}{0.80} \times 5 = 0.05",
            font_size=15
        )
        hysteresis_calc_group_3 = VGroup(hysteresis_calc_label_3, hysteresis_calc_formula_3)
        hysteresis_calc_group_3.arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # Create a container for the calculation
        calc_box_3 = RoundedRectangle(
            width=6.5,
            height=1.1,
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )
        calc_box_3.move_to(hysteresis_calc_group_3.get_center())
        calc_box_3.stretch_to_fit_width(hysteresis_calc_group_3.get_width() + 0.4)
        calc_box_3.stretch_to_fit_height(hysteresis_calc_group_3.get_height() + 0.4)

        # Group the calculation and its container
        hysteresis_container_3 = VGroup(calc_box_3, hysteresis_calc_group_3)
        hysteresis_container_3.next_to(col3_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col3_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])

        # Create range text with container
        range_box_3 = create_info_box(
            "3. Range of Best Matches = 0.80 - 0.05 = [0.75,0.80]",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_3.next_to(hysteresis_container_3, DOWN, buff=0.2)
        range_box_3.align_to(new_heading, LEFT)

        # Create potential matches box
        potential_match_box_3 = create_info_box(
            "4. Potential Best Match = 0.80",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_3.next_to(range_box_3, DOWN, buff=0.2)
        potential_match_box_3.align_to(new_heading, LEFT)

        # Create result box
        result_box_3 = create_result_box(
            "5. The only value within the range is 0.80",
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        result_box_3.next_to(potential_match_box_3, DOWN, buff=0.2)
        result_box_3.align_to(new_heading, LEFT)

        # Animate the enhanced elements for column 3
        self.play(
            ReplacementTransform(progress_indicator_4, progress_indicator_3),
            run_time=0.8
        )
        self.play(Write(col3_header), run_time=0.8)
        self.wait(0.2)

        self.play(
            Write(col3_data),
            FadeIn(cell_highlight_3),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(
            FadeIn(hysteresis_container_3),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(FadeIn(range_box_3), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(potential_match_box_3), run_time=0.8)
        self.wait(0.2)

        # Find all values in column 3 to fade out
        column_3_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 2
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][2]
            if abs(value - 0.80) > 0.01:
                column_3_values.append(value_obj)

        # Highlight for 0.80 value
        highlight_080 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0,
            stroke_width=3
        )
        highlight_080.move_to([cell_x_3, cell_y_3, 0])

        # Fade out all other values
        self.play(
            *[FadeOut(val) for val in column_3_values],
            run_time=0.8
        )

        self.play(
            FadeIn(result_box_3),
            FadeIn(highlight_080),
            run_time=0.8
        )

        self.wait(1.5)

        # Fade out column 3 elements
        self.play(
            FadeOut(col3_header),
            FadeOut(col3_data),
            FadeOut(hysteresis_container_3),
            FadeOut(range_box_3),
            FadeOut(potential_match_box_3),
            FadeOut(result_box_3),
            FadeOut(highlight_080),
            run_time=1.0
        )

        self.wait(0.5)

        # -------------------- ENHANCED VERSION OF COLUMN 2 PRESENTATION --------------------
        # Update progress indicator for column 2
        progress_indicator_2 = create_progress_indicator(2)
        progress_indicator_2.move_to(progress_indicator)
        self.play(ReplacementTransform(progress_indicator, progress_indicator_2),
                  run_time=0.8)
        progress_indicator = progress_indicator_2

        # Create a header for Column 2
        col2_header = create_section_header("COLUMN 2 ANALYSIS")
        col2_header.next_to(new_text, DOWN, buff=0.4)
        col2_header.align_to(new_heading, LEFT)

        # Create data points box
        col2_data = create_info_box("1. Max Value: 0.87 (Location: Row 2)", 
                                fill_color=BLUE_E, 
                                fill_opacity=0.1)
        col2_data.next_to(col2_header, DOWN, buff=0.2)
        col2_data.align_to(new_heading, LEFT)

        # Create highlight for the 0.87 cell
        cell_highlight_2 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        cell_x_2 = anchor[0] + (1 + 0.5) * dx  # 2nd column (index 1)
        cell_y_2 = anchor[1] + (1 + 0.5) * dy  # Row position for 0.87
        cell_highlight_2.move_to([cell_x_2, cell_y_2, 0])

        # Create hysteresis calculation box
        hysteresis_calc_label_2 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula_2 = MathTex(
            r"\frac{0.4 - (1 - 0.87)}{0.87} \times 5 = 0.06",
            font_size=15
        )
        hysteresis_calc_group_2 = VGroup(hysteresis_calc_label_2, hysteresis_calc_formula_2)
        hysteresis_calc_group_2.arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # Create a container for the calculation
        calc_box_2 = RoundedRectangle(
            width=6.5,
            height=1.1,
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )
        calc_box_2.move_to(hysteresis_calc_group_2.get_center())
        calc_box_2.stretch_to_fit_width(hysteresis_calc_group_2.get_width() + 0.4)
        calc_box_2.stretch_to_fit_height(hysteresis_calc_group_2.get_height() + 0.4)

        # Group the calculation and its container
        hysteresis_container_2 = VGroup(calc_box_2, hysteresis_calc_group_2)
        hysteresis_container_2.next_to(col2_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col2_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])

        # Create range text with container
        range_box_2 = create_info_box(
            "3. Range of Best Matches = 0.87 - 0.06 = [0.81,0.87]",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_2.next_to(hysteresis_container_2, DOWN, buff=0.2)
        range_box_2.align_to(new_heading, LEFT)

        # Create potential matches box
        potential_match_box_2 = create_info_box(
            "4. Potential Best Match = 0.87",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_2.next_to(range_box_2, DOWN, buff=0.2)
        potential_match_box_2.align_to(new_heading, LEFT)

        # Create result box
        result_box_2 = create_result_box(
            "5. The only value within the range is 0.87",
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        result_box_2.next_to(potential_match_box_2, DOWN, buff=0.2)
        result_box_2.align_to(new_heading, LEFT)

        # Animate the enhanced elements for column 2
        self.play(
            ReplacementTransform(progress_indicator_3, progress_indicator_2),
            run_time=0.8
        )
        self.play(Write(col2_header), run_time=0.8)
        self.wait(0.2)

        self.play(
            Write(col2_data),
            FadeIn(cell_highlight_2),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(
            FadeIn(hysteresis_container_2),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(FadeIn(range_box_2), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(potential_match_box_2), run_time=0.8)
        self.wait(0.2)

        # Find all values in column 2 to fade out
        column_2_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 1
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][1]
            if abs(value - 0.87) > 0.01:
                column_2_values.append(value_obj)

        # Highlight for 0.87 value
        highlight_087 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0,
            stroke_width=3
        )
        highlight_087.move_to([cell_x_2, cell_y_2, 0])

        # Fade out all other values
        self.play(
            *[FadeOut(val) for val in column_2_values],
            run_time=0.8
        )

        self.play(
            FadeIn(result_box_2),
            FadeIn(highlight_087),
            run_time=0.8
        )

        self.wait(1.5)

        # Fade out column 2 elements
        self.play(
            FadeOut(col2_header),
            FadeOut(col2_data),
            FadeOut(hysteresis_container_2),
            FadeOut(range_box_2),
            FadeOut(potential_match_box_2),
            FadeOut(result_box_2),
            # FadeOut(column_indicator_arrow_2),
            FadeOut(highlight_087),
            run_time=1.0
        )

        self.wait(0.5)

        # -------------------- ENHANCED VERSION OF COLUMN 1 PRESENTATION --------------------
        # Update progress indicator for column 1
        progress_indicator_1 = create_progress_indicator(1)
        progress_indicator_1.move_to(progress_indicator)
        self.play(ReplacementTransform(progress_indicator, progress_indicator_1),
                  run_time=0.8)
        progress_indicator = progress_indicator_1

        # Create a header for Column 1
        col1_header = create_section_header("COLUMN 1 ANALYSIS")
        col1_header.next_to(new_text, DOWN, buff=0.4)
        col1_header.align_to(new_heading, LEFT)

        # Create data points box
        col1_data = create_info_box("1. Max Value: 0.94 (Location: Row 9)", 
                                fill_color=BLUE_E, 
                                fill_opacity=0.1)
        col1_data.next_to(col1_header, DOWN, buff=0.2)
        col1_data.align_to(new_heading, LEFT)

        # Create highlight for the 0.94 cell
        cell_highlight_1 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.0,
            stroke_width=3
        )
        cell_x_1 = anchor[0] + (0 + 0.5) * dx  # 1st column (index 0)
        cell_y_1 = anchor[1] + (0 + 0.5) * dy  # Row position for 0.94
        cell_highlight_1.move_to([cell_x_1, cell_y_1, 0])

        # Create hysteresis calculation box
        hysteresis_calc_label_1 = Text("2. Hysteresis Calculation:", font_size=15, color=WHITE)
        hysteresis_calc_formula_1 = MathTex(
            r"\frac{0.4 - (1 - 0.94)}{0.94} \times 5 = 0.07",
            font_size=15
        )
        hysteresis_calc_group_1 = VGroup(hysteresis_calc_label_1, hysteresis_calc_formula_1)
        hysteresis_calc_group_1.arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # Create a container for the calculation
        calc_box_1 = RoundedRectangle(
            width=6.5,
            height=1.1,
            corner_radius=0.1,
            color=WHITE,
            fill_color=DARK_BLUE,
            fill_opacity=0.1,
            stroke_width=0.5
        )
        calc_box_1.move_to(hysteresis_calc_group_1.get_center())
        calc_box_1.stretch_to_fit_width(hysteresis_calc_group_1.get_width() + 0.4)
        calc_box_1.stretch_to_fit_height(hysteresis_calc_group_1.get_height() + 0.4)

        # Group the calculation and its container
        hysteresis_container_1 = VGroup(calc_box_1, hysteresis_calc_group_1)
        hysteresis_container_1.next_to(col1_data, DOWN, buff=0.2)
        hysteresis_container.move_to([
            col1_data.get_center()[0], 
            hysteresis_container.get_center()[1], 
            0
        ])

        # Create range text with container
        range_box_1 = create_info_box(
            "3. Range of Best Matches = 0.94 - 0.07 = [0.87,0.94]",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        range_box_1.next_to(hysteresis_container_1, DOWN, buff=0.2)
        range_box_1.align_to(new_heading, LEFT)

        # Create potential matches box
        potential_match_box_1 = create_info_box(
            "4. Potential Best Match = 0.94",
            fill_color=BLUE_E,
            fill_opacity=0.1
        )
        potential_match_box_1.next_to(range_box_1, DOWN, buff=0.2)
        potential_match_box_1.align_to(new_heading, LEFT)

        # Create result box
        result_box_1 = create_result_box(
            "5. The only value within the range is 0.94",
            fill_color=GREEN_E,
            fill_opacity=0.2
        )
        result_box_1.next_to(potential_match_box_1, DOWN, buff=0.2)
        result_box_1.align_to(new_heading, LEFT)

        # Animate the enhanced elements for column 1
        self.play(
            ReplacementTransform(progress_indicator_2, progress_indicator_1),
            run_time=0.8
        )
        self.play(Write(col1_header), run_time=0.8)
        self.wait(0.2)

        self.play(
            Write(col1_data),
            FadeIn(cell_highlight_1),
            # GrowArrow(column_indicator_arrow_1),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(
            FadeIn(hysteresis_container_1),
            run_time=0.8
        )
        self.wait(0.2)

        self.play(FadeIn(range_box_1), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(potential_match_box_1), run_time=0.8)
        self.wait(0.2)

        # Find all values in column 1 to fade out
        column_1_values = []
        for i in range(num_rows):
            value_idx = i * num_cols + 0
            value_obj = heatmap_values[value_idx]
            value = cosine_values[8-i][0]
            if abs(value - 0.94) > 0.01:
                column_1_values.append(value_obj)

        # Highlight for 0.94 value
        highlight_094 = Rectangle(
            width=dx,
            height=dy,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0,
            stroke_width=3
        )
        highlight_094.move_to([cell_x_1, cell_y_1, 0])

        # Fade out all other values
        self.play(
            *[FadeOut(val) for val in column_1_values],
            run_time=0.8
        )

        self.play(
            FadeIn(result_box_1),
            FadeIn(highlight_094),
            run_time=0.8
        )

        self.wait(1.5)

        # Fade out column 1 elements
        self.play(
            FadeOut(col1_header),
            FadeOut(col1_data),
            FadeOut(hysteresis_container_1),
            FadeOut(range_box_1),
            FadeOut(potential_match_box_1),
            FadeOut(result_box_1),
            FadeOut(highlight_094),
            FadeOut(progress_indicator_1),
            FadeOut(new_heading),
            FadeOut(new_underline),
            FadeOut(new_text),
            run_time=1.0
        )

        self.wait(1.0)

        # ================== FINAL RESULTS SUMMARY ==================
        # Display comprehensive results of the best matching algorithm execution
        final_header = create_section_header("FINAL RESULTS SUMMARY", width=6.5)

        summary_text = Text(
            "Selected Best Matches for Each Column:",
            font_size=13,
            color=WHITE
        )
        summary_text.next_to(final_header, DOWN, buff=0.25)
        summary_text.align_to(final_header, LEFT)

        results_data = [
            "Column 1: 0.94 (Row 9)",
            "Column 2: 0.87 (Row 2)",
            "Column 3: 0.80 (Row 7)",
            "Column 4: Not Valid (< 0.6)",
            "Column 5: Not Valid (< 0.6)",
            "Column 6: Not Valid (< 0.6)",
            "Column 7: Not Valid (< 0.6)",
            "Column 8: 0.86 (Row 4)",
            "Column 9: 0.77 (Row 9), 0.73 (Row 1)",
        ]

        results_container = VGroup()
        for i, line in enumerate(results_data):
            row = create_info_box(
                line,
                width=6.5,
                height=0.42,
                fill_color=GREEN_E if "Not Valid" not in line else BLUE_E,
                fill_opacity=0.20 if "Not Valid" not in line else 0.12,
            )
            if i == 0:
                row.next_to(summary_text, DOWN, buff=0.18)
            else:
                row.next_to(results_container[-1], DOWN, buff=0.08)
            row.align_to(summary_text, LEFT)
            results_container.add(row)

        conclusion_box = create_result_box(
            "The algorithm successfully identifies the best matches\n"
            "in each column based on the hysteresis criteria,\n"
            "ensuring robust alignment between segments.",
            width=6.5,
            height=0.95,
            fill_color=DARK_BLUE,
            fill_opacity=0.22,
        )
        conclusion_box.next_to(results_container, DOWN, buff=0.25)
        conclusion_box.align_to(summary_text, LEFT)

        # (2) --- group them ----------------------------------------------------------
        summary_group = VGroup(
            final_header,
            summary_text,
            results_container,
            conclusion_box,
        )

        # (3) --- scale and position inside the big rectangle (`new_box`) -------------
        summary_group.scale(0.93)                                   # shrink a bit
        top_left_inside = (                                          
            new_box.get_corner(UP + LEFT) + RIGHT * 0.7 + DOWN * 0.3  # margin
        )
        summary_group.move_to(top_left_inside, aligned_edge=UP + LEFT)

        # (4) --- animate -------------------------------------------------------------
        self.play(Write(final_header), run_time=0.8)
        self.wait(0.15)

        self.play(Write(summary_text), run_time=0.7)
        self.wait(0.15)

        for row in results_container:
            self.play(FadeIn(row), run_time=0.25)

        self.play(FadeIn(conclusion_box), run_time=0.7)
        self.wait(2.0)

        # ─────────────────────────  ADD THESE 3 LINES  ─────────────────────────
        summary_group = VGroup(final_header, summary_text,
                            results_container, conclusion_box)   # ← ① group them
        self.play(FadeOut(summary_group, new_box), run_time=1.0)             # ← ② fade out
     

        # Define how much you want to move the heatmap up
        shift_up_amount = 0.2  # <--- ADJUST THIS VALUE AS NEEDED (e.g., 1.0, 2.0, 0.5)

        # 2. choose an anchor for the transposed heatmap
        box_anchor = (
             ORIGIN + RIGHT * 1.2 + DOWN * (y_length/2 + 0.3) + UP * shift_up_amount
        )

        # 3. container for every element we’ll draw
        transposed_heatmap = VGroup()

        # ── axes ─────────────────────────────────────────────────────────
        transposed_heatmap.add(
            Line(box_anchor, box_anchor + UP * y_length,
                 color=WHITE, stroke_width=1),
            Line(box_anchor, box_anchor + RIGHT * x_length,
                 color=WHITE, stroke_width=1)
        )

        # ── grid lines ───────────────────────────────────────────────────
        for r_loop in range(num_rows + 1): # Renamed r to r_loop
            y_coord = box_anchor[1] + r_loop * dy # Renamed y to y_coord
            transposed_heatmap.add(
                Line([box_anchor[0], y_coord, 0], [box_anchor[0] + x_length, y_coord, 0],
                     color=WHITE, stroke_width=1)
            )
        for c_loop in range(num_cols + 1): # Renamed c to c_loop
            x_coord = box_anchor[0] + c_loop * dx # Renamed x to x_coord
            transposed_heatmap.add(
                Line([x_coord, box_anchor[1], 0], [x_coord, box_anchor[1] + y_length, 0],
                     color=WHITE, stroke_width=1)
            )

        # ── axis labels (blue = rows, maroon = columns) ─────────────────
        for i_loop in range(num_rows): # Displayed rows of transposed map
            y_box = RoundedRectangle(width=0.45, height=0.45, corner_radius=0.04,
                                     color=WHITE, fill_color=MAROON_B, # BLUE_E for rows (y-axis)
                                     fill_opacity=.5, stroke_width=1)
            y_box.move_to(box_anchor + LEFT * 0.35 + UP * (i_loop + .5) * dy)
            transposed_heatmap.add(
                y_box,
                Text(str(i_loop + 1), font_size=12, color=WHITE).move_to(y_box) # Labels 1-9 for rows
            )

        for j_loop in range(num_cols): # Displayed columns of transposed map
            x_box = RoundedRectangle(width=0.45, height=0.45, corner_radius=0.04,
                                     color=WHITE, fill_color=BLUE_E, # MAROON_B for columns (x-axis)
                                     fill_opacity=.5, stroke_width=1)
            x_box.move_to(box_anchor + DOWN * 0.35 + RIGHT * (j_loop + .5) * dx)
            transposed_heatmap.add(
                x_box,
                Text(str(j_loop + 1), font_size=12, color=WHITE).move_to(x_box) # Labels 1-9 for columns
            )

        # ── numeric cell values ─────────────────────────────────────────
        transposed_numeric_texts_group = VGroup() # Holds all numeric Text mobjects for the transposed heatmap
        for i in range(num_rows): # i is visual row from bottom of transposed map (0 to 8)
            for j in range(num_cols): # j is visual col from left of transposed map (0 to 8)
                value = cosine_values[8 - j][i]
                t = Text(f"{value:.2f}", font_size=14, color=WHITE)
                t.move_to(box_anchor + RIGHT * (j + .5) * dx + UP * (i + .5) * dy)
                transposed_numeric_texts_group.add(t) # Add to the dedicated group
        transposed_heatmap.add(transposed_numeric_texts_group) # Add this group to the main heatmap VGroup

        # 4. heading & underline
        row_heading = Text(
            "Finding Row-Wise Best Match", # Or "Transposed Heatmap"
            font_size=18, color=WHITE, weight="BOLD"
        )
        row_heading.next_to(transposed_heatmap, UP, buff=0.35)
        row_heading.align_to(transposed_heatmap, LEFT)
        row_heading.shift(RIGHT * 0.7) # Keep similar shift as original heatmap heading

        row_underline = Underline(row_heading)
        row_underline.next_to(row_heading, DOWN, buff=0.05)
        row_underline.align_to(row_heading, LEFT)

        # 5. animate: write heading first, then fade grid in
        self.play(Write(row_heading), Create(row_underline), run_time=0.6)
        self.play(FadeIn(transposed_heatmap), run_time=1.2)
        self.wait(1.0) # Increased wait time

        # --- ADD DIAGONAL HIGHLIGHTS TO THE TRANSPOSED HEATMAP ---
        transposed_diagonal_highlights = VGroup()
        for k in range(num_rows):  # k from 0 to 8 (num_rows is 9)
            # Cell to highlight is at visual row k (from bottom) and visual column k (from left)
            cell_center_x = box_anchor[0] + (k + 0.5) * dx
            cell_center_y = box_anchor[1] + (k + 0.5) * dy
            
            highlight_rect_transposed = Rectangle(
                width=dx, height=dy, color=RED, fill_color=RED,
                fill_opacity=0.3, stroke_width=0
            )
            highlight_rect_transposed.move_to([cell_center_x, cell_center_y, 0])
            transposed_diagonal_highlights.add(highlight_rect_transposed)

        # Animate these new diagonal highlights
        self.play(
            LaggedStart(*[FadeIn(rect) for rect in transposed_diagonal_highlights], lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(1.0) # Final wait time

        # Set of (visual_row_idx, visual_col_idx) for the highest values in transposed map
        highest_coords_transposed = { 
            (0, 0), (1, 1), (2, 2), (8, 3), (2, 4), 
            (7, 5), (5, 6), (2, 7), (8, 8) 
        }

        texts_to_fade_out = VGroup()
        highlights_for_max_values = VGroup()

        for i_row_visual in range(num_rows):  # visual row index, 0 to 8
            for j_col_visual in range(num_cols): # visual column index, 0 to 8
                text_obj_index = i_row_visual * num_cols + j_col_visual
                # CORRECTED: Access from the correctly defined VGroup
                current_text_mobject = transposed_numeric_texts_group[text_obj_index] 

                if (i_row_visual, j_col_visual) in highest_coords_transposed:
                    highlight_rect = Rectangle(
                        width=dx, height=dy, color=GREEN,
                        fill_opacity=0, 
                        stroke_width=3  
                    )
                    highlight_rect.move_to(current_text_mobject.get_center())
                    highlights_for_max_values.add(highlight_rect)
                else:
                    texts_to_fade_out.add(current_text_mobject)
        
        self.play(
            FadeOut(texts_to_fade_out, lag_ratio=0), 
            LaggedStart(*[FadeIn(h) for h in highlights_for_max_values], lag_ratio=0.05), 
            run_time=1.5 
        )
        self.wait(3)