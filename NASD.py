
"""
Narrative Alignment Score - Distance (NASD) Animation

This Manim animation visualizes the calculation of Narrative Alignment Score using
distance-based measurements between reference and generated text sequences.

The animation demonstrates:
1. Heatmap visualization of cosine similarity scores
2. Column-wise and row-wise best match finding
3. Distance calculations using mathematical formulas
4. Precision heatmap generation

Author: Mehul Deep
Date: 07/15/2025
Framework: Manim Community v0.19.0

Usage:
    python -m manim -pql --disable_caching NASD.py FullConceptAnimation
"""

from manim import (  # type: ignore
    # Core scene and animation classes
    Scene, Text, Underline, Create, Write, VGroup,
    
    # Geometric objects
    Arrow, Triangle, Line, Brace, Rectangle, RoundedRectangle,
    SurroundingRectangle, DashedVMobject, Square, Arc, CubicBezier, Dot,
    
    # Mathematical and text objects
    MathTex, Paragraph,
    
    # Animation functions
    GrowArrow, DrawBorderThenFill, GrowFromCenter, FadeIn, FadeOut,
    Transform, LaggedStart, ReplacementTransform, AddTextLetterByLetter,
    
    # Colors
    BLUE_E, GREEN_E, RED_E, GREEN, ORANGE, RED, BLUE, YELLOW,
    LIGHT_PINK, WHITE, GREY, BLACK, DARK_BLUE, MAROON_B,
    
    # Positioning and constants
    ORIGIN, UP, LEFT, RIGHT, DOWN, PI, DEGREES,
    
    # Text formatting
    ITALIC, BOLD,
    
    # Other utilities
    CurvedArrow, np
)

class FullConceptAnimation(Scene):
    """
    Main animation class for visualizing Narrative Alignment Score - Distance calculation.
    
    This animation demonstrates the complete NASD process including heatmap generation,
    best match finding, distance calculations, and precision measurements.
    """

    def construct(self):
        """Main animation sequence orchestrating all visualization components."""
        # ================== TITLE AND SETUP ==================
        # Create and animate the main title
        main_title_obj = Text("Narrative Alignment Score - Distance", font_size=25).move_to(ORIGIN)
        self.play(Write(main_title_obj))
        self.wait(0.5)
        
        # Move title to top and add underline
        self.play(main_title_obj.animate.to_edge(UP*0.1))
        self.wait(0.5)
        main_underline_obj = Underline(main_title_obj)
        self.play(Create(main_underline_obj))
        self.wait(0.5)

        # Initialize VGroups for collecting animation elements
        t_arrows_group = VGroup()  # Arrows for T-term animations
        a_elements_group = VGroup()  # Elements for A-term animations

        # ================== DATA CONFIGURATION ==================
        # Cosine similarity matrix (9x9) - represents similarity scores between text segments
        cosine_values = [
            [0.51, 0.28, 0.08, 0.07, 0.09, 0.16, 0.05, 0.50, 0.73],  # Row 1: A9 source comparisons
            [0.20, 0.24, 0.27, 0.09, 0.18, 0.15, 0.19, 0.21, 0.21],  # Row 2: A8 source comparisons
            [0.12, 0.15, 0.15, 0.17, 0.12, 0.58, 0.12, 0.21, 0.17],  # Row 3: A7 source comparisons
            [0.61, 0.37, 0.28, 0.19, 0.14, 0.35, 0.16, 0.86, 0.66],  # Row 4: A6 source comparisons
            [0.30, 0.30, 0.38, 0.18, 0.10, 0.22, 0.09, 0.19, 0.30],  # Row 5: A5 source comparisons
            [0.51, 0.34, 0.12, 0.06, 0.12, 0.19, 0.15, 0.52, 0.53],  # Row 6: A4 source comparisons
            [0.26, 0.27, 0.80, 0.24, 0.20, 0.19, 0.27, 0.23, 0.22],  # Row 7: A3 source comparisons
            [0.49, 0.87, 0.33, 0.27, 0.23, 0.29, 0.17, 0.34, 0.38],  # Row 8: A2 source comparisons
            [0.94, 0.47, 0.33, 0.17, 0.14, 0.38, 0.18, 0.62, 0.77],  # Row 9: A1 source comparisons
        ]
        
        # Heatmap configuration parameters
        num_rows, num_cols = 9, 9
        heatmap_width, heatmap_height = 5.0, 5.0
        dx, dy = heatmap_width / num_cols, heatmap_height / num_rows
        label_box_size, label_font_size, value_font_size = 0.40, 11, 12

        # ================== HEATMAP CREATION FUNCTION ==================
        def create_final_heatmap_display(
            anchor_point, map_title_text, y_axis_label_color, x_axis_label_color,
            value_accessor_func, green_border_coords, show_red_diagonal=True):
            """
            Creates a complete heatmap visualization with grid, labels, and highlighting.
            
            Args:
                anchor_point: Bottom-left corner position for the heatmap
                map_title_text: Title displayed above the heatmap
                y_axis_label_color: Color for row labels 
                x_axis_label_color: Color for column labels
                value_accessor_func: Function to get values for each cell
                green_border_coords: Set of (row, col) coordinates to highlight in green
                show_red_diagonal: Whether to highlight diagonal cells in red
                
            Returns:
                Tuple of (heatmap_group, cell_texts_dict, grid_origin_dot)
            """
            heatmap_grid_and_content = VGroup()
            cell_value_texts = {}
            grid_origin_ref_dot = Dot(point=anchor_point, radius=0.0001, fill_opacity=0, stroke_opacity=0)
            heatmap_grid_and_content.add(grid_origin_ref_dot)
            ht_y_axis = Line(anchor_point, anchor_point + UP * heatmap_height, stroke_color=WHITE, stroke_width=1)
            ht_x_axis = Line(anchor_point, anchor_point + RIGHT * heatmap_width, stroke_color=WHITE, stroke_width=1)
            heatmap_grid_and_content.add(ht_y_axis, ht_x_axis)
            ht_grid_lines = VGroup()
            for r_idx in range(num_rows + 1):
                y_l = anchor_point[1] + r_idx * dy
                ht_grid_lines.add(Line([anchor_point[0], y_l, 0], [anchor_point[0] + heatmap_width, y_l, 0], stroke_color=WHITE, stroke_width=0.5))
            for c_idx in range(num_cols + 1):
                x_l = anchor_point[0] + c_idx * dx
                ht_grid_lines.add(Line([x_l, anchor_point[1], 0], [x_l, anchor_point[1] + heatmap_height, 0], stroke_color=WHITE, stroke_width=0.5))
            heatmap_grid_and_content.add(ht_grid_lines)
            ht_y_labels = VGroup()
            for i in range(num_rows):
                y_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=y_axis_label_color, fill_opacity=.5, stroke_width=1)
                y_box.move_to(anchor_point + LEFT * (label_box_size/2 + 0.1) + UP * (i + .5) * dy)
                y_text = Text(str(i + 1), font_size=label_font_size, color=WHITE).move_to(y_box.get_center())
                ht_y_labels.add(VGroup(y_box, y_text))
            heatmap_grid_and_content.add(ht_y_labels)
            ht_x_labels = VGroup()
            for j in range(num_cols):
                x_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=x_axis_label_color, fill_opacity=.5, stroke_width=1)
                x_box.move_to(anchor_point + DOWN * (label_box_size/2 + 0.1) + RIGHT * (j + .5) * dx)
                x_text = Text(str(j + 1), font_size=label_font_size, color=WHITE).move_to(x_box.get_center())
                ht_x_labels.add(VGroup(x_box, x_text))
            heatmap_grid_and_content.add(ht_x_labels)
            ht_cell_content_elements = VGroup()
            for i_vis_row in range(num_rows):
                for j_vis_col in range(num_cols):
                    cell_center_x = anchor_point[0] + (j_vis_col + 0.5) * dx
                    cell_center_y = anchor_point[1] + (i_vis_row + 0.5) * dy
                    cell_center = [cell_center_x, cell_center_y, 0]
                    if show_red_diagonal and i_vis_row == j_vis_col:
                        red_rect = Rectangle(width=dx, height=dy, color=RED, fill_color=RED, fill_opacity=0.3, stroke_width=0).move_to(cell_center)
                        ht_cell_content_elements.add(red_rect)
                    if (i_vis_row, j_vis_col) in green_border_coords:
                        val = value_accessor_func(i_vis_row, j_vis_col)
                        num_text = Text(f"{val:.2f}", font_size=value_font_size, color=WHITE).move_to(cell_center)
                        ht_cell_content_elements.add(num_text)
                        cell_value_texts[(i_vis_row, j_vis_col)] = num_text
                        green_rect = Rectangle(width=dx, height=dy, color=GREEN, stroke_width=2.5, fill_opacity=0).move_to(cell_center)
                        ht_cell_content_elements.add(green_rect)
            heatmap_grid_and_content.add(ht_cell_content_elements)
            ht_title = Text(map_title_text, font_size=18, color=WHITE, weight="BOLD")
            ht_title.next_to(heatmap_grid_and_content, UP, buff=0.25)
            return VGroup(ht_title, heatmap_grid_and_content), cell_value_texts, grid_origin_ref_dot

        # ================== HEATMAP COORDINATE DEFINITIONS ==================
        # Coordinates for highlighting specific cells in left heatmap (column-wise best matches)
        left_heatmap_green_coords = {
            (0,0), (1,1), (2,2), (1,3), (1,4),  # Diagonal matches
            (6,5),                              # Off-diagonal match
            (2,6), (5,7), (8,8)                 # Additional best matches
        }

        # Coordinates for highlighting specific cells in right heatmap (row-wise best matches)
        right_heatmap_green_coords = { 
            (0,0), (1,1), (2,2), (8,3), (2,4),  # Diagonal and selected best matches
            (7,5), (5,6), (2,7), (8,8)          # Additional row-wise best matches
        }

        # ================== VALUE ACCESSOR FUNCTIONS ==================
        def left_value_accessor(vis_row, vis_col):
            """Accesses cosine values for left heatmap with row transformation."""
            return cosine_values[8 - vis_row][vis_col]

        # ================== INITIAL HEATMAP CREATION ==================
        # Create left heatmap showing column-wise best match finding
        left_heatmap_full, left_cell_texts, _ = create_final_heatmap_display(
            anchor_point=ORIGIN, 
            map_title_text="Finding Column-Wise Best Match",
            y_axis_label_color=BLUE_E, 
            x_axis_label_color=MAROON_B,
            value_accessor_func=left_value_accessor,
            green_border_coords=left_heatmap_green_coords,
            show_red_diagonal=True
        )
        left_heatmap_full.move_to(LEFT * 3.4 + DOWN * 0.3)

        # Modified accessor for right heatmap with special value overrides
        def modified_right_value_accessor(vis_row, vis_col):
            """Accesses cosine values for right heatmap with specific overrides for certain cells."""
            # Special cases with hardcoded values for specific coordinates
            if (vis_row, vis_col) == (6, 5): 
                return 0.53
            elif (vis_row, vis_col) == (2, 6): 
                return 0.27
            elif (vis_row, vis_col) == (5, 7): 
                return 0.86
            else: 
                # Standard transformation for row-wise access
                return cosine_values[8 - vis_col][vis_row]

        right_heatmap_full, _, _ = create_final_heatmap_display(
            anchor_point=ORIGIN, map_title_text="Finding Row-Wise Best Match",
            y_axis_label_color=MAROON_B, x_axis_label_color=BLUE_E,
            value_accessor_func=modified_right_value_accessor,
            green_border_coords=right_heatmap_green_coords,    # <--- FIX: Use the variable name you defined
            show_red_diagonal=True
        )
        right_heatmap_full.move_to(RIGHT * 3.4 + DOWN * 0.3)
        right_heatmap_full_center = right_heatmap_full.get_center()

        # ================== HEATMAP ANIMATIONS ==================
        # Display both heatmaps initially
        heatmaps_to_fade_in = VGroup(left_heatmap_full, right_heatmap_full)
        self.play(FadeIn(heatmaps_to_fade_in), run_time=2.0)
        self.wait(1.0)
        
        # Remove right heatmap and replace with duplicate of left heatmap
        self.play(FadeOut(right_heatmap_full), run_time=1.0)
        duplicate_left = left_heatmap_full.copy()
        duplicate_left.move_to(right_heatmap_full_center)
        self.play(FadeIn(duplicate_left), run_time=1.0); self.wait(1.0)

        # --- Change title of the duplicated heatmap (now on the right) ---
        # Ensure this entire block has the SAME indentation level as the line above
        old_title_on_duplicate = duplicate_left[0]    # The title is the first element
        grid_content_on_duplicate = duplicate_left[1] # The grid/content is the second (Line 489 - should be fixed)

        new_precision_title = Text(
            "Precision Heat map",
            font_size=18, # Matches original title style
            color=WHITE,
            weight="BOLD"  # Matches original title style
        )
        # Position the new title correctly relative to its grid content
        new_precision_title.next_to(grid_content_on_duplicate, UP, buff=0.25)

        self.play(ReplacementTransform(old_title_on_duplicate, new_precision_title))

        # Update the VGroup 'duplicate_left' to contain the new title mobject
        duplicate_left.submobjects[0] = new_precision_title
        self.wait(0.5) # Optional: short pause after title change
        # --- End of title change ---

        duplicate_green_rects_to_fade = VGroup()

        elements_to_fade_initial_highlights = VGroup()
        try:
            # duplicate_left[0] is its title, duplicate_left[1] is its heatmap_grid_and_content VGroup
            heatmap_grid_content_group = duplicate_left[1]
            # The actual mobjects (rects, texts) are in the last sub-VGroup of heatmap_grid_content_group
            cell_content_mobjects = heatmap_grid_content_group[-1]

            if isinstance(cell_content_mobjects, VGroup):
                # Iterate through the mobjects to find green rectangles and their preceding text values
                # We iterate by index to easily access the previous mobject
                for i in range(len(cell_content_mobjects)):
                    current_mobj = cell_content_mobjects[i]

                    # Check if the current mobject is one of the original green borders
                    # These borders were defined by left_heatmap_green_coords when left_heatmap_full was created
                    if isinstance(current_mobj, Rectangle) and \
                       current_mobj.get_stroke_color().to_hex() == GREEN.to_hex() and \
                       current_mobj.get_stroke_width() == 2.5 and \
                       current_mobj.get_fill_opacity() == 0:
                        
                        # Add the green rectangle to our list of things to fade
                        elements_to_fade_initial_highlights.add(current_mobj)
                        
                        # The corresponding Text value should be the mobject immediately preceding this rectangle
                        # and share the same center (as they were both moved to cell_center)
                        if i > 0: # Check if there is a previous mobject
                            prev_mobj = cell_content_mobjects[i-1]
                            if isinstance(prev_mobj, Text) and \
                               np.allclose(prev_mobj.get_center(), current_mobj.get_center()):
                                # Add the text value to our list of things to fade
                                elements_to_fade_initial_highlights.add(prev_mobj)
                            else:
                                # This case should ideally not happen if the heatmap was constructed consistently
                                print(f"DEBUG: Green rectangle found at index {i} in duplicate_left's content, " +
                                      "but its preceding mobject was not the expected Text value or centers didn't match.")
                        else:
                            # This case (green rectangle at index 0) should also not happen for a Text-Rect pair
                            print(f"DEBUG: Green rectangle found at index 0 in duplicate_left's content; no preceding Text possible.")
            
        except Exception as e: # Catch the specific exception for better debugging
            print(f"DEBUG: Error while identifying initial highlights to fade from duplicate_left: {e}")

        # Update the debug messages and the FadeOut call to use the new VGroup name
        if not elements_to_fade_initial_highlights:
            print("DEBUG: No initial green highlights (borders or texts) identified in duplicate_left to fade.")
        else:
            # This count will now include both rectangles and text objects
            print(f"DEBUG: Identified {len(elements_to_fade_initial_highlights)} elements (initial green borders and texts) from duplicate_left to fade.")

        # ================== HEATMAP SCALING AND SUMMARY BOX ==================
        # Scale and reposition heatmaps to make room for formulas
        final_heatmaps = VGroup(left_heatmap_full, duplicate_left)
        scale_factor_for_animation = 0.75
        self.play(
            final_heatmaps.animate.scale(scale_factor_for_animation).shift(UP * 1.4),
            run_time=1.0)
        self.wait(1.0)

        # Create summary box for distance calculations
        box_width, box_height = 10.0, 2.5
        bottom_box_center_y_coord = DOWN * (self.camera.frame_height / 2 - box_height / 2 - 0.15)
        summary_box = RoundedRectangle(
            width=box_width, height=box_height, corner_radius=0.2, 
            color=WHITE, stroke_width=2, fill_color=BLACK, fill_opacity=0.8
        )
        summary_box.move_to(bottom_box_center_y_coord)
        self.play(DrawBorderThenFill(summary_box), run_time=1.5)
        self.wait(0.2)

        # ================== DISTANCE CALCULATION SECTION ==================
        # Add heading for distance calculations
        heading_text_obj = Text("Measuring distance for each column:", font_size=15, weight=BOLD)
        heading_underline_obj = Underline(heading_text_obj, color=WHITE)
        heading_group = VGroup(heading_text_obj, heading_underline_obj)
        heading_group.next_to(summary_box.get_top(), DOWN, buff=0.25).align_to(summary_box.get_left(), LEFT).shift(RIGHT * 0.3)
        self.play(Write(heading_text_obj), Create(heading_underline_obj))
        self.wait(0.5)

        # ================== YELLOW HIGHLIGHTING ANIMATION ==================
        coords_to_highlight_yellow = [
            (1,0), (2,1), (0,1), (1,2), (3,2), (4,3), (2,3), (5,4), (3,4), 
            (6,5), (4,5), (7,6), (5,6), (8,7), (6,7), (7,8)
        ]
        
        yellow_highlights = VGroup()
        # Get the current grid origin of the left_heatmap_full (which is now scaled and shifted)
        # left_heatmap_full is VGroup(ht_title, heatmap_grid_and_content)
        # heatmap_grid_and_content is VGroup(grid_origin_ref_dot, ...)
        current_left_grid_origin = left_heatmap_full[1][0].get_center()
        current_scaled_dx = dx * scale_factor_for_animation
        current_scaled_dy = dy * scale_factor_for_animation

        for r_vis, c_vis in coords_to_highlight_yellow:
            cell_center_x = current_left_grid_origin[0] + (c_vis + 0.5) * current_scaled_dx
            cell_center_y = current_left_grid_origin[1] + (r_vis + 0.5) * current_scaled_dy
            cell_center = [cell_center_x, cell_center_y, 0]
            
            highlight_rect = Rectangle(
                width=current_scaled_dx, 
                height=current_scaled_dy, 
                color=YELLOW,  # Using YELLOW for the new highlights
                stroke_width=2, 
                fill_opacity=0.1 # Optional: slight fill to make it more prominent
            ).move_to(cell_center)
            yellow_highlights.add(highlight_rect)
            
        self.play(Create(yellow_highlights), run_time=1.5)
        self.wait(1.0)

        # ================== T-FORMULA CREATION AND ANIMATION ==================
        # Create mathematical formula components for distance calculation
        # This section builds the mathematical representation T1/R + T2/R + ... + T9/R
        # where Ti represents distance values and R is the reference denominator
        formula_font_size = 25
        
        # Create individual T-formula terms (T1/R through T9/R)
        term_T1_R = MathTex("T_1", "/", "R", font_size=formula_font_size)
        plus_1 = MathTex("+", font_size=formula_font_size)
        term_T2_R = MathTex("T_2", "/", "R", font_size=formula_font_size)
        plus_2 = MathTex("+", font_size=formula_font_size)
        term_T3_R = MathTex("T_3", "/", "R", font_size=formula_font_size)
        plus_3 = MathTex("+", font_size=formula_font_size)
        term_T4_R = MathTex("T_4", "/", "R", font_size=formula_font_size)
        plus_4 = MathTex("+", font_size=formula_font_size)
        term_T5_R = MathTex("T_5", "/", "R", font_size=formula_font_size)
        plus_5 = MathTex("+", font_size=formula_font_size)
        term_T6_R = MathTex("T_6", "/", "R", font_size=formula_font_size)
        plus_6 = MathTex("+", font_size=formula_font_size)
        term_T7_R = MathTex("T_7", "/", "R", font_size=formula_font_size)
        plus_7 = MathTex("+", font_size=formula_font_size)
        term_T8_R = MathTex("T_8", "/", "R", font_size=formula_font_size)
        plus_8 = MathTex("+", font_size=formula_font_size)
        term_T9_R = MathTex("T_9", "/", "R", font_size=formula_font_size)

        # Group all formula components together for layout management
        all_formula_parts = VGroup(
            term_T1_R, plus_1, term_T2_R, plus_2, term_T3_R, plus_3, term_T4_R,
            plus_4, term_T5_R, plus_5, term_T6_R, plus_6, term_T7_R,
            plus_7, term_T8_R, plus_8, term_T9_R
        )
        all_formula_parts.arrange(RIGHT, buff=0.12)
        all_formula_parts.next_to(heading_group, DOWN, buff=0.30, aligned_edge=LEFT)

        def create_heatmap_arrow(source_vis_coords, target_vis_coords, arrow_color=WHITE, on_heatmap_mobject=left_heatmap_full):
            """
            Creates an arrow between two points on the heatmap grid.
            
            Args:
                source_vis_coords: (row, col) tuple for arrow start position
                target_vis_coords: (row, col) tuple for arrow end position  
                arrow_color: Color of the arrow (default: WHITE)
                on_heatmap_mobject: The heatmap object to draw arrows on
                
            Returns:
                Arrow: Configured arrow object for the heatmap
            """
            # Get current grid positioning and scaling
            current_grid_origin_world = on_heatmap_mobject[1][0].get_center()
            current_scaled_dx = dx * scale_factor_for_animation
            current_scaled_dy = dy * scale_factor_for_animation
            
            # Calculate arrow start position (source coordinates)
            arrow_start_x = current_grid_origin_world[0] + (source_vis_coords[1] + 0.5) * current_scaled_dx
            arrow_start_y = current_grid_origin_world[1] + (source_vis_coords[0] + 1.0) * current_scaled_dy 
            arrow_start_point = np.array([arrow_start_x, arrow_start_y, 0])
            
            # Calculate arrow end position (target coordinates)
            arrow_end_x = current_grid_origin_world[0] + (target_vis_coords[1] + 0.5) * current_scaled_dx
            arrow_end_y = current_grid_origin_world[1] + (target_vis_coords[0] + 0.0) * current_scaled_dy
            arrow_end_point = np.array([arrow_end_x, arrow_end_y, 0])
            
            # Create and return configured arrow
            return Arrow(
                start=arrow_start_point, end=arrow_end_point, color=arrow_color, buff=0.05, 
                stroke_width=5, tip_length=0.2,
                max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=10.0 )

        # Animate T-formula terms sequentially with corresponding arrows
        # First three terms (T1, T2, T3) are displayed without arrows for simplicity
        self.play(Write(term_T1_R)); self.wait(0.1)
        self.play(Write(plus_1)); self.wait(0.1)
        self.play(Write(term_T2_R)); self.wait(0.1)
        self.play(Write(plus_2)); self.wait(0.1)
        self.play(Write(term_T3_R)); self.wait(0.1)
        
        # T4 term with arrow demonstration
        self.play(Write(plus_3)); self.wait(0.1)
        arrow_T4 = create_heatmap_arrow(source_vis_coords=(1,3), target_vis_coords=(3,3)) 
        t_arrows_group.add(arrow_T4) # Add to group for later management
        self.play(Write(term_T4_R), Create(arrow_T4), run_time=1.0); self.wait(0.3)

        # T5 term with arrow demonstration
        self.play(Write(plus_4)); self.wait(0.1)
        arrow_T5 = create_heatmap_arrow(source_vis_coords=(1,4), target_vis_coords=(4,4))
        t_arrows_group.add(arrow_T5) # Add to group for later management
        self.play(Write(term_T5_R), Create(arrow_T5), run_time=1.0); self.wait(0.3)

        # T6 term with special curved arrow (demonstrates intra-heatmap relationship)
        self.play(Write(plus_5)); self.wait(0.1)
        arrow_T6_source_vis_coords = (6, 5); arrow_T6_target_vis_coords = (5, 5)
        current_grid_origin_world_for_T6 = left_heatmap_full[1][0].get_center()
        current_scaled_dx_for_T6 = dx * scale_factor_for_animation; current_scaled_dy_for_T6 = dy * scale_factor_for_animation
        
        # Calculate curved arrow positioning manually for T6
        start_T6_x = current_grid_origin_world_for_T6[0] + arrow_T6_source_vis_coords[1] * current_scaled_dx_for_T6
        start_T6_y = current_grid_origin_world_for_T6[1] + (arrow_T6_source_vis_coords[0] + 0.5) * current_scaled_dy_for_T6
        arrow_T6_start_point = np.array([start_T6_x, start_T6_y, 0])
        end_T6_x = current_grid_origin_world_for_T6[0] + arrow_T6_target_vis_coords[1] * current_scaled_dx_for_T6
        end_T6_y = current_grid_origin_world_for_T6[1] + (arrow_T6_target_vis_coords[0] + 0.5) * current_scaled_dy_for_T6
        arrow_T6_end_point = np.array([end_T6_x, end_T6_y, 0])
        arrow_T6_curved_intra_heatmap = CurvedArrow(arrow_T6_start_point, arrow_T6_end_point, angle=PI/5, color=WHITE, stroke_width=5, tip_length=0.2)
        t_arrows_group.add(arrow_T6_curved_intra_heatmap)
        self.play(Write(term_T6_R), Create(arrow_T6_curved_intra_heatmap), run_time=1.0); self.wait(0.3)

        # T7 term with arrow demonstration
        self.play(Write(plus_6)); self.wait(0.1)
        arrow_T7 = create_heatmap_arrow(source_vis_coords=(2,6), target_vis_coords=(6,6))
        t_arrows_group.add(arrow_T7) # Add to group for later management
        self.play(Write(term_T7_R), Create(arrow_T7), run_time=1.0); self.wait(0.3)
        
        # T8 term with arrow demonstration
        self.play(Write(plus_7)); self.wait(0.1)
        arrow_T8 = create_heatmap_arrow(source_vis_coords=(5,7), target_vis_coords=(7,7))
        t_arrows_group.add(arrow_T8) # Add to group for later management
        self.play(Write(term_T8_R), Create(arrow_T8), run_time=1.0); self.wait(0.3)

        # Final T9 term (no arrow for this one)
        self.play(Write(plus_8)); self.wait(0.1)
        self.play(Write(term_T9_R), run_time=0.5); self.wait(1.0)

        # Fade out initial highlight elements if they exist
        # This cleans up the visual space before introducing the next heatmap
        if elements_to_fade_initial_highlights: # Check if highlight elements exist
            self.play(FadeOut(elements_to_fade_initial_highlights), run_time=1.5) # Fade them out
        self.wait(0.5)

        # Create heading for the second heatmap section (A-formula)
        new_heading_text = Text("Another Heatmap", font_size=15, weight=BOLD)
        new_heading_underline = Underline(new_heading_text, color=WHITE)
        new_heading_group = VGroup(new_heading_text, new_heading_underline)
        new_heading_group.next_to(all_formula_parts, DOWN, buff=0.35, aligned_edge=LEFT)

        # Animate the heading for the A-formula section
        self.play(Write(new_heading_text), Create(new_heading_underline))
        self.wait(0.5)

        # Create A-formula components (A1/R + A2/R + ... + A9/R)
        # This represents the second set of mathematical terms for the algorithm
        a_terms_list = []
        a_plus_list = []
        
        # Generate A-terms (A1/R through A9/R) and plus signs
        for i in range(1, 10):
            term = MathTex(f"A_{i}", "/", "R", font_size=formula_font_size)
            a_terms_list.append(term)
            if i < 9:  # Don't add plus after the last term
                plus = MathTex("+", font_size=formula_font_size)
                a_plus_list.append(plus)

        # Interleave terms and plus signs for proper layout
        all_A_formula_parts_for_layout = []
        for i_term in range(len(a_terms_list)):
            all_A_formula_parts_for_layout.append(a_terms_list[i_term])
            if i_term < len(a_plus_list):  # Add plus sign if not the last term
                all_A_formula_parts_for_layout.append(a_plus_list[i_term])
        
        # Group and position all A-formula components
        all_A_formula_vgroup = VGroup(*all_A_formula_parts_for_layout)
        all_A_formula_vgroup.arrange(RIGHT, buff=0.12)
        all_A_formula_vgroup.next_to(new_heading_group, DOWN, buff=0.2, aligned_edge=LEFT)
        
        # Get reference grid positioning for the duplicate (right) heatmap
        current_grid_origin_ref = duplicate_left[1][0].get_center() 
        current_scaled_dx_ref = dx * scale_factor_for_animation
        current_scaled_dy_ref = dy * scale_factor_for_animation
        
        # ================== ANIMATION FOR A1/R ==================
        # First A-term animation with highlighting and arrow demonstration
        highlight_vis_row_A1 = 8; highlight_vis_col_A1 = 0  # Target position for A1 highlight
        arrow_source_vis_row_A1 = 0; arrow_source_vis_col_A1 = 0  # Source position for A1 arrow
        
        # Create highlight rectangle for A1 cell
        cell_center_x_highlight_A1 = current_grid_origin_ref[0] + (highlight_vis_col_A1 + 0.5) * current_scaled_dx_ref
        cell_center_y_highlight_A1 = current_grid_origin_ref[1] + (highlight_vis_row_A1 + 0.5) * current_scaled_dy_ref
        new_highlight_A1 = Rectangle(
            width=current_scaled_dx_ref, height=current_scaled_dy_ref, color=GREEN, stroke_width=3.5, fill_opacity=0
        ).move_to([cell_center_x_highlight_A1, cell_center_y_highlight_A1, 0])
        
        # Create arrow for A1 term
        arrow_A1 = create_heatmap_arrow(
            source_vis_coords=(arrow_source_vis_row_A1, arrow_source_vis_col_A1), 
            target_vis_coords=(highlight_vis_row_A1, highlight_vis_col_A1),       
            arrow_color=WHITE, on_heatmap_mobject=duplicate_left 
        )
        
        # Add elements to group for management and animate
        a_elements_group.add(new_highlight_A1, arrow_A1)
        self.play(Write(a_terms_list[0]), Create(new_highlight_A1), Create(arrow_A1), run_time=1.5)
        self.wait(0.3)

        # --- Loop for A2/R to A9/R ---
        for i_loop in range(len(a_plus_list)): # This loop runs for i_loop = 0 to 7
            plus_to_animate = a_plus_list[i_loop]
            term_to_animate = a_terms_list[i_loop+1] # a_terms_list[1] (A2/R) to a_terms_list[8] (A9/R)
            
            self.play(Write(plus_to_animate), run_time=0.3)
            self.wait(0.05)

            highlight_vis_row, highlight_vis_col = -1, -1
            arrow_source_vis_row, arrow_source_vis_col = -1, -1
            custom_arrow_style = False
            is_special_case = True 

            if term_to_animate == a_terms_list[1]: # A2/R
                highlight_vis_row = 8; highlight_vis_col = 1
                arrow_source_vis_row = 1; arrow_source_vis_col = 1
            elif term_to_animate == a_terms_list[2]: # A3/R
                highlight_vis_row = 8; highlight_vis_col = 2 
                arrow_source_vis_row = 2; arrow_source_vis_col = 2
            elif term_to_animate == a_terms_list[3]: # A4/R
                highlight_vis_row = 8; highlight_vis_col = 3 
                arrow_source_vis_row = 3; arrow_source_vis_col = 3
            elif term_to_animate == a_terms_list[4]: # A5/R
                highlight_vis_row = 8; highlight_vis_col = 4 
                arrow_source_vis_row = 4; arrow_source_vis_col = 4
            elif term_to_animate == a_terms_list[5]: # A6/R
                highlight_vis_row = 0; highlight_vis_col = 5 
                arrow_source_vis_row = 5; arrow_source_vis_col = 5
                custom_arrow_style = True
            elif term_to_animate == a_terms_list[6]: # A7/R
                highlight_vis_row = 0; highlight_vis_col = 6 
                arrow_source_vis_row = 6; arrow_source_vis_col = 6
                custom_arrow_style = True 
            elif term_to_animate == a_terms_list[7]: # A8/R
                highlight_vis_row = 0; highlight_vis_col = 7
                arrow_source_vis_row = 7; arrow_source_vis_col = 7
                custom_arrow_style = True
            elif term_to_animate == a_terms_list[8]: # A9/R
                highlight_vis_row = 0; highlight_vis_col = 8
                arrow_source_vis_row = 8; arrow_source_vis_col = 8
                custom_arrow_style = True
            else: 
                # This else block should ideally not be reached if all terms A2-A9 are handled.
                # If it is, it means term_to_animate didn't match any a_terms_list index from 1 to 8.
                is_special_case = False 
                self.play(Write(term_to_animate), run_time=0.4)

            if is_special_case:
                cell_center_x_highlight = current_grid_origin_ref[0] + (highlight_vis_col + 0.5) * current_scaled_dx_ref
                cell_center_y_highlight = current_grid_origin_ref[1] + (highlight_vis_row + 0.5) * current_scaled_dy_ref
                new_highlight = Rectangle(
                    width=current_scaled_dx_ref, height=current_scaled_dy_ref, color=GREEN, stroke_width=3.5, fill_opacity=0
                ).move_to([cell_center_x_highlight, cell_center_y_highlight, 0])

                if custom_arrow_style: 
                    arrow_start_x = current_grid_origin_ref[0] + (arrow_source_vis_col + 0.5) * current_scaled_dx_ref
                    arrow_start_y = current_grid_origin_ref[1] + (arrow_source_vis_row + 0.0) * current_scaled_dy_ref 
                    arrow_start_point = np.array([arrow_start_x, arrow_start_y, 0])
                    arrow_end_x = current_grid_origin_ref[0] + (highlight_vis_col + 0.5) * current_scaled_dx_ref
                    arrow_end_y = current_grid_origin_ref[1] + (highlight_vis_row + 1.0) * current_scaled_dy_ref 
                    arrow_end_point = np.array([arrow_end_x, arrow_end_y, 0])
                    new_arrow = Arrow(
                        start=arrow_start_point, end=arrow_end_point, color=WHITE, buff=0.05,
                        stroke_width=5, tip_length=0.2, max_tip_length_to_length_ratio=0.5, 
                        max_stroke_width_to_length_ratio=10.0
                    )
                else: 
                    new_arrow = create_heatmap_arrow(
                        source_vis_coords=(arrow_source_vis_row, arrow_source_vis_col),
                        target_vis_coords=(highlight_vis_row, highlight_vis_col),
                        arrow_color=WHITE, on_heatmap_mobject=duplicate_left
                    )

                a_elements_group.add(new_highlight, new_arrow) 
                self.play(Write(term_to_animate), Create(new_highlight), Create(new_arrow), run_time=1.5)
            
            self.wait(0.1)
        
        self.wait(2)

        # --- Step 1: Fade out current on-screen elements ---
        # Get current positions of the heatmaps before they are faded/removed from final_heatmaps
        current_left_heatmap_pos = left_heatmap_full.get_center()
        current_right_heatmap_pos = duplicate_left.get_center() # duplicate_left has "Precision Heat map" title

        elements_to_fade_out_completely = VGroup(
            final_heatmaps,       # Contains left_heatmap_full and duplicate_left
            yellow_highlights,    # These were on left_heatmap_full
            all_formula_parts,    # T1-T9 MathTex formulas
            all_A_formula_vgroup, # A1-A9 MathTex formulas
            heading_group,        # "Measuring distance for each column:" heading
            new_heading_group,    # "Another Heatmap" heading
            t_arrows_group,       # Group of T-arrows (ensure this was populated)
            a_elements_group      # Group of A-highlights and A-arrows (ensure this was populated)
        )
        
        self.play(FadeOut(elements_to_fade_out_completely, shift=DOWN*0.2), run_time=2.0) # Added a slight shift for effect
        self.wait(0.5)

        # --- Step 2: Create the new "Finding Row-Wise Best Match" heatmap (for the left) ---
        # This uses the configuration that correctly displays Screenshot 1's right heatmap
        
        # Ensure this coordinate set is correct for the 12 desired cells in "Finding Row-Wise Best Match"
        correct_row_wise_coords = {
            (0,0), (1,1), (2,2), (8,3), (2,4),      # All 9 diagonal elements from Scr1 Right
            (7,5), (5,6), (2,7), (8,8)
        }


        new_heatmap_left_config, _, _ = create_final_heatmap_display(
            anchor_point=ORIGIN, # Create at origin first
            map_title_text="Finding Row-Wise Best Match",
            y_axis_label_color=MAROON_B, # Style of the original "Finding Row-Wise Best Match"
            x_axis_label_color=BLUE_E,   # Style of the original "Finding Row-Wise Best Match"
            value_accessor_func=modified_right_value_accessor,
            green_border_coords=correct_row_wise_coords, 
            show_red_diagonal=True
        )
        new_heatmap_left_config.scale(scale_factor_for_animation) # Apply the same scaling
        new_heatmap_left_config.move_to(current_left_heatmap_pos) # Move to where old left heatmap was
        
        self.play(FadeIn(new_heatmap_left_config, shift=UP*0.2), run_time=1.0) # Added shift for effect
        self.wait(0.5)

        # --- Step 3: Duplicate it to the right side ---
        new_heatmap_right_config = new_heatmap_left_config.copy()
        new_heatmap_right_config.move_to(current_right_heatmap_pos) # Move to where old right heatmap was
        
        # Fade in the right heatmap *before* changing its title
        self.play(FadeIn(new_heatmap_right_config, shift=UP*0.2), run_time=1.0)
        self.wait(0.5)

        # --- Step 4: Rename the title of the new right heatmap to "Precision Heat map" ---
        old_title_on_new_right = new_heatmap_right_config[0]
        grid_content_on_new_right = new_heatmap_right_config[1]

        final_precision_title_obj = Text(
            "Precision Heat map",
            font_size=14, # Match original title style
            color=WHITE,
            weight="BOLD"
        )
        final_precision_title_obj.next_to(grid_content_on_new_right, UP, buff=0.20)

        self.play(ReplacementTransform(old_title_on_new_right, final_precision_title_obj))
        new_heatmap_right_config.submobjects[0] = final_precision_title_obj # Update the VGroup

        self.wait(3) # Final pause for the new scene

        # 1. Create a new summary box for the final heading
        final_box_height = 1.0 # Adjust as needed for just one heading
        final_summary_box_center_y = DOWN * (self.camera.frame_height / 2 - final_box_height / 2 - 0.25) # Position lower
        
        final_summary_box = RoundedRectangle(
            width=box_width, height=final_box_height, corner_radius=0.2,
            color=WHITE, stroke_width=2, fill_color=BLACK, fill_opacity=0.8
        )
        final_summary_box.move_to(final_summary_box_center_y)
        
        final_heading_text = Text("Measuring distance for each column", font_size=15, weight=BOLD)
        final_heading_underline = Underline(final_heading_text, color=WHITE)
        final_heading_group = VGroup(final_heading_text, final_heading_underline)

        # Position it like the first heading in summary_box (the EXISTING summary_box)
        final_heading_group.next_to(summary_box.get_top(), DOWN, buff=0.25).align_to(summary_box.get_left(), LEFT).shift(RIGHT * 0.3)

        self.play( # NO DrawBorderThenFill for summary_box, as it's already there.
            Write(final_heading_text),
            Create(final_heading_underline),
            run_time=1.5
        )
        self.wait(0.5)

        # 2. Define coordinates for new highlights on the `new_heatmap_left_config`
        coords_for_final_highlights = [
            (1,0), (2,1), (0,1), (3,2), (1,2), (4,3), (2,3), (5,4), (3,4), 
            (6,5), (4,5), (7,6), (5,6), (8,7), (6,7), (7,8)
        ]
        
        final_phase_highlights = VGroup()

        # Get the current grid origin of new_heatmap_left_config (which is now scaled and shifted)
        target_heatmap_grid_origin = new_heatmap_left_config[1][0].get_center()
        
        for r_vis, c_vis in coords_for_final_highlights:
            cell_center_x = target_heatmap_grid_origin[0] + (c_vis + 0.5) * current_scaled_dx
            cell_center_y = target_heatmap_grid_origin[1] + (r_vis + 0.5) * current_scaled_dy
            cell_center = [cell_center_x, cell_center_y, 0]
            
            highlight_rect = Rectangle(
                width=current_scaled_dx, 
                height=current_scaled_dy, 
                color=YELLOW, # Using a new distinct color
                stroke_width=2, 
                fill_opacity=0.1 # Slight fill
            ).move_to(cell_center)
            final_phase_highlights.add(highlight_rect)
            
        self.play(Create(final_phase_highlights), run_time=2.0)
        self.wait(2.0) # Final pause for this new section
       
        # --- NEW T-FORMULA AND ARROW ANIMATIONS SECTION ---
        
        # 1. Define the new T-terms formula
        final_formula_font_size = 20 # Consistent with previous formula_font_size
        final_t_terms_list = []
        final_t_plus_list = []

        for i in range(1, 10):
            term = MathTex(f"T_{i}", "/", "R", font_size=final_formula_font_size)
            final_t_terms_list.append(term)
            if i < 9:
                plus = MathTex("+", font_size=final_formula_font_size)
                final_t_plus_list.append(plus)

        all_final_T_formula_parts_for_layout = []
        for i_term in range(len(final_t_terms_list)):
            all_final_T_formula_parts_for_layout.append(final_t_terms_list[i_term])
            if i_term < len(final_t_plus_list):
                all_final_T_formula_parts_for_layout.append(final_t_plus_list[i_term])
        
        all_final_T_formula_vgroup = VGroup(*all_final_T_formula_parts_for_layout)
        all_final_T_formula_vgroup.arrange(RIGHT, buff=0.10) # Slightly reduced buff for fitting
        
        # Position below the final_heading_group (which is already in summary_box)
        all_final_T_formula_vgroup.next_to(final_heading_group, DOWN, buff=0.20, aligned_edge=LEFT)

        # 2. Helper function for specific edge arrows
        # (target_heatmap_grid_origin, current_scaled_dx, current_scaled_dy are in scope from final_phase_highlights)
        
        final_t_arrows_on_heatmap = VGroup() # To collect these new arrows

        def create_specific_edge_arrow(
            source_r_vis, source_c_vis, source_edge_is_top, 
            target_r_vis, target_c_vis, target_edge_is_top,
            arrow_color=WHITE # Using ORANGE for these new T-arrows for distinction
        ):
            # `target_heatmap_grid_origin` is the origin of new_heatmap_left_config's grid
            # `current_scaled_dx`, `current_scaled_dy` are its scaled cell dimensions

            source_x = target_heatmap_grid_origin[0] + (source_c_vis + 0.5) * current_scaled_dx
            source_y_base = target_heatmap_grid_origin[1] + source_r_vis * current_scaled_dy
            source_y = source_y_base + current_scaled_dy if source_edge_is_top else source_y_base

            target_x = target_heatmap_grid_origin[0] + (target_c_vis + 0.5) * current_scaled_dx
            target_y_base = target_heatmap_grid_origin[1] + target_r_vis * current_scaled_dy
            target_y = target_y_base + current_scaled_dy if target_edge_is_top else target_y_base
            
            return Arrow(
                start=np.array([source_x, source_y, 0]),
                end=np.array([target_x, target_y, 0]),
                color=arrow_color,
                buff=0.05, # Reduced buff for direct edge connection
                stroke_width=5, # Slightly thinner
                tip_length=0.2,
                max_tip_length_to_length_ratio=0.5, 
                max_stroke_width_to_length_ratio=10.0
            )

        # 3. Animate writing T-terms and drawing arrows
        
        # T1/R, T2/R, T3/R
        self.play(Write(final_t_terms_list[0])); self.wait(0.1)
        self.play(Write(final_t_plus_list[0])); self.wait(0.1)
        self.play(Write(final_t_terms_list[1])); self.wait(0.1)
        self.play(Write(final_t_plus_list[1])); self.wait(0.1)
        self.play(Write(final_t_terms_list[2])); self.wait(0.1)
        self.play(Write(final_t_plus_list[2])); self.wait(0.1)

        # T4/R: arrow from lower box of (8,3) to upper side of box (3,3)
        # Visual coordinates (0-indexed from bottom): (r_start=8, c_start=3) to (r_end=3, c_end=3)
        arrow_T4_final = create_specific_edge_arrow(
            source_r_vis=8, source_c_vis=3, source_edge_is_top=False, # Lower edge of (8,3)
            target_r_vis=3, target_c_vis=3, target_edge_is_top=True   # Upper edge of (3,3)
        )
        final_t_arrows_on_heatmap.add(arrow_T4_final)
        self.play(Write(final_t_terms_list[3]), Create(arrow_T4_final), run_time=1.5); self.wait(0.3)
        self.play(Write(final_t_plus_list[3])); self.wait(0.1)

        # T5/R: arrow from upper box at (2,4) connecting to lower side of box (4,4)
        # Visual coordinates: (r_start=2, c_start=4) to (r_end=4, c_end=4)
        arrow_T5_final = create_specific_edge_arrow(
            source_r_vis=2, source_c_vis=4, source_edge_is_top=True,  # Upper edge of (2,4)
            target_r_vis=4, target_c_vis=4, target_edge_is_top=False  # Lower edge of (4,4)
        )
        final_t_arrows_on_heatmap.add(arrow_T5_final)
        self.play(Write(final_t_terms_list[4]), Create(arrow_T5_final), run_time=1.5); self.wait(0.3)
        self.play(Write(final_t_plus_list[4])); self.wait(0.1)

        # T6/R: arrow from the lower side of (7,5) connecting to the upper side of box (5,5)
        # Visual coordinates: (r_start=7, c_start=5) to (r_end=5, c_end=5)
        arrow_T6_final = create_specific_edge_arrow(
            source_r_vis=7, source_c_vis=5, source_edge_is_top=False, # Lower edge of (7,5)
            target_r_vis=5, target_c_vis=5, target_edge_is_top=True   # Upper edge of (5,5)
        )
        final_t_arrows_on_heatmap.add(arrow_T6_final)
        self.play(Write(final_t_terms_list[5]), Create(arrow_T6_final), run_time=1.5); self.wait(0.3)
        self.play(Write(final_t_plus_list[5])); self.wait(0.1)

        # T7/R: Nothing happens here
        self.play(Write(final_t_terms_list[6])); self.wait(0.3)
        self.play(Write(final_t_plus_list[6])); self.wait(0.1)

        # T8/R: Arrow from upper side of the box in (2,7) connecting to the lower side of (7,7) box
        # Visual coordinates: (r_start=2, c_start=7) to (r_end=7, c_end=7)
        arrow_T8_final = create_specific_edge_arrow(
            source_r_vis=2, source_c_vis=7, source_edge_is_top=True,  # Upper edge of (2,7)
            target_r_vis=7, target_c_vis=7, target_edge_is_top=False  # Lower edge of (7,7)
        )
        final_t_arrows_on_heatmap.add(arrow_T8_final)
        self.play(Write(final_t_terms_list[7]), Create(arrow_T8_final), run_time=1.5); self.wait(0.3)
        self.play(Write(final_t_plus_list[7])); self.wait(0.1)
        
        # T9/R: Nothing happens in this
        self.play(Write(final_t_terms_list[8])); self.wait(0.3)
        
        self.wait(3.0) # Final pause on the entire scene
       
        elements_to_fade_from_right_heatmap = VGroup()
        try:
            # Access cell_content_elements from new_heatmap_right_config
            # It's the last element of the second submobject of new_heatmap_right_config
            right_heatmap_cell_contents = new_heatmap_right_config[1][-1] 
            if isinstance(right_heatmap_cell_contents, VGroup):
                for mobj in right_heatmap_cell_contents:
                    # Fade Text objects (values) and Green Rectangles (original highlights)
                    # but not the Red Rectangles (diagonal)
                    if isinstance(mobj, Text):
                        elements_to_fade_from_right_heatmap.add(mobj)
                    elif isinstance(mobj, Rectangle) and \
                         mobj.get_stroke_color().to_hex() == GREEN.to_hex() and \
                         mobj.get_fill_opacity() == 0: # Check it's a border, not a filled rect
                        elements_to_fade_from_right_heatmap.add(mobj)
            if elements_to_fade_from_right_heatmap:
                self.play(FadeOut(elements_to_fade_from_right_heatmap), run_time=1.5)
            else:
                print("DEBUG: No text or green borders found to fade from right heatmap's cell contents.")
        except Exception as e:
            print(f"DEBUG: Error accessing or fading elements from right heatmap: {e}")
        self.wait(0.5)

        # 2. New Heading: "Now for right Heatmap"
        right_focus_heading_text = Text("Now for right Heatmap", font_size=15, weight=BOLD)
        right_focus_heading_underline = Underline(right_focus_heading_text, color=WHITE)
        right_focus_heading_group = VGroup(right_focus_heading_text, right_focus_heading_underline)
        
        # Position below the last T-formula (all_final_T_formula_vgroup) in the summary_box
        right_focus_heading_group.next_to(all_final_T_formula_vgroup, DOWN, buff=0.25, aligned_edge=LEFT)
        
        self.play(Write(right_focus_heading_text), Create(right_focus_heading_underline))
        self.wait(0.5)

        # 3. New A-terms formula for the right heatmap
        final_a_formula_font_size = 20 # Consistent
        final_a_terms_list = []
        final_a_plus_list = []

        for i in range(1, 10):
            term = MathTex(f"A_{i}", "/", "R", font_size=final_a_formula_font_size)
            final_a_terms_list.append(term)
            if i < 9:
                plus = MathTex("+", font_size=final_a_formula_font_size)
                final_a_plus_list.append(plus)
        
        all_final_A_formula_parts_for_layout = []
        for i_term in range(len(final_a_terms_list)):
            all_final_A_formula_parts_for_layout.append(final_a_terms_list[i_term])
            if i_term < len(final_a_plus_list):
                all_final_A_formula_parts_for_layout.append(final_a_plus_list[i_term])
        
        all_final_A_formula_vgroup = VGroup(*all_final_A_formula_parts_for_layout)
        all_final_A_formula_vgroup.arrange(RIGHT, buff=0.10)
        all_final_A_formula_vgroup.next_to(right_focus_heading_group, DOWN, buff=0.20, aligned_edge=LEFT)

        # 4. Helper function for specific edge arrows (modified to accept heatmap object)
        # current_scaled_dx and current_scaled_dy are still in scope
        
        final_a_arrows_and_highlights = VGroup()

        # Modified/Generic arrow function for this section:
        def create_final_a_arrow_on_heatmap(
            on_heatmap_mobject, # This will be new_heatmap_right_config
            source_r_vis, source_c_vis, source_edge_is_top, 
            target_r_vis, target_c_vis, target_edge_is_top,
            arrow_color=WHITE # New color for these A-arrows
        ):
            grid_origin_world = on_heatmap_mobject[1][0].get_center()
            # current_scaled_dx, current_scaled_dy are from the outer scope

            source_x = grid_origin_world[0] + (source_c_vis + 0.5) * current_scaled_dx
            source_y_base = grid_origin_world[1] + source_r_vis * current_scaled_dy
            source_y = source_y_base + current_scaled_dy if source_edge_is_top else source_y_base

            target_x = grid_origin_world[0] + (target_c_vis + 0.5) * current_scaled_dx
            target_y_base = grid_origin_world[1] + target_r_vis * current_scaled_dy
            target_y = target_y_base + current_scaled_dy if target_edge_is_top else target_y_base
            
            return Arrow(
                start=np.array([source_x, source_y, 0]), end=np.array([target_x, target_y, 0]),
                color=arrow_color, buff=0.05, stroke_width=5, tip_length=0.2,
                max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=10.0
            )

        # 5. Animate A-terms, arrows, and highlights
        # Coordinates are 0-indexed visual (r,c) from bottom-left

        # Loop for A1/R to A9/R
        for i in range(9): # 0 to 8, for A_i+1
            term_to_animate = final_a_terms_list[i]
            plus_to_animate = final_a_plus_list[i] if i < 8 else None

            # Define source and target cell coordinates for arrows and highlights
            # Source is always on diagonal: (i, i)
            source_r_vis, source_c_vis = i, i
            
            # Target cell for highlight and arrow end
            target_r_vis, target_c_vis = -1, -1
            source_is_top_edge, target_is_top_edge = False, False # Default

            if i < 5: # A1-A5 (i.e., index 0 to 4 for terms_list) -> arrow goes UP
                source_edge_is_top = True  # Arrow from upper edge of (i,i)
                target_r_vis = 8           # Target row is top-most (visual index 8)
                target_c_vis = i           # Target column is i
                target_edge_is_top = False # Connects to lower edge of (8,i)
            else: # A6-A9 (i.e., index 5 to 8 for terms_list) -> arrow goes DOWN
                source_edge_is_top = False # Arrow from lower edge of (i,i)
                target_r_vis = 0           # Target row is bottom-most (visual index 0)
                target_c_vis = i           # Target column is i
                target_edge_is_top = True  # Connects to upper edge of (0,i)

            # Create arrow
            new_a_arrow = create_final_a_arrow_on_heatmap(
                on_heatmap_mobject=new_heatmap_right_config, # Target the RIGHT heatmap
                source_r_vis=source_r_vis, source_c_vis=source_c_vis, source_edge_is_top=source_edge_is_top,
                target_r_vis=target_r_vis, target_c_vis=target_c_vis, target_edge_is_top=target_edge_is_top
            )
            
            # Create highlight for the target cell
            grid_origin_right_heatmap = new_heatmap_right_config[1][0].get_center()
            highlight_center_x = grid_origin_right_heatmap[0] + (target_c_vis + 0.5) * current_scaled_dx
            highlight_center_y = grid_origin_right_heatmap[1] + (target_r_vis + 0.5) * current_scaled_dy
            
            new_a_highlight = Rectangle(
                width=current_scaled_dx, height=current_scaled_dy, 
                color=GREEN, stroke_width=3.0, # Green border, slightly thicker
                fill_opacity=0
            ).move_to([highlight_center_x, highlight_center_y, 0])

            final_a_arrows_and_highlights.add(new_a_arrow, new_a_highlight)

            # Animate
            if i == 0: # First term (A1/R)
                self.play(
                    Write(term_to_animate),
                    Create(new_a_arrow),
                    Create(new_a_highlight),
                    run_time=1.5
                )
            else: # Subsequent terms, animate plus sign first
                if plus_to_animate:
                     self.play(Write(plus_to_animate), run_time=0.3); self.wait(0.05)
                self.play(
                    Write(term_to_animate),
                    Create(new_a_arrow),
                    Create(new_a_highlight),
                    run_time=1.5
                )
            self.wait(0.3)
            
        self.wait(3.0) # Final overall pause