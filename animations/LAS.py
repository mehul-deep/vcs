"""
Local Alignment Score (LAS) Animation

This Manim animation visualizes the Local Alignment Score algorithm for text analysis,
demonstrating how local similarity scores are computed and visualized through 
comprehensive heatmap representations and mathematical calculations.

The animation demonstrates:
1. Local alignment score computation methodology
2. Comprehensive heatmap visualization with similarity matrices
3. Color-coded cell highlighting for best local matches
4. Mathematical formula representations and calculations
5. Interactive grid-based data visualization
6. Diagonal and off-diagonal pattern recognition
7. Local optimization techniques for text alignment

Author: Mehul Deep
Date: 07/15/2025
Framework: Manim Community v0.19.0

Usage:
    python -m manim -pql --disable_caching LAS.py FullConceptAnimation
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
    Transform, LaggedStart, ReplacementTransform, AddTextLetterByLetter,
    
    # Colors
    BLUE_E, GREEN_E, RED_E, GREEN, ORANGE, RED, BLUE, YELLOW, LIGHT_PINK,
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
    Main animation class for visualizing the Local Alignment Score (LAS) algorithm.
    
    This animation demonstrates local alignment score computation through comprehensive
    heatmap visualizations, similarity matrix analysis, and mathematical calculations
    for text alignment optimization.
    """

    def construct(self):
        """Main animation sequence orchestrating all LAS visualization components."""
        # ================== TITLE AND HEADING SETUP ==================
        # Create and animate the main title for Local Alignment Score
        main_title_obj = Text("Local Alignment Score", font_size=25).move_to(ORIGIN)
        self.play(Write(main_title_obj))
        self.wait(0.5)

        # Move title to top edge for optimal screen space utilization
        self.play(main_title_obj.animate.to_edge(UP*0.1)) 
        self.wait(0.5)

        # Add underline for visual emphasis and professional appearance
        main_underline_obj = Underline(main_title_obj)
        self.play(Create(main_underline_obj))
        self.wait(0.5)

        # ================== SIMILARITY MATRIX DATA CONFIGURATION ==================
        # Global heatmap parameters and similarity data for local alignment analysis
        # Cosine similarity matrix (9x9) - represents local similarity scores between text segments
        cosine_values = [
            [0.51, 0.28, 0.08, 0.07, 0.09, 0.16, 0.05, 0.50, 0.73],  # Row 1: Segment comparisons
            [0.20, 0.24, 0.27, 0.09, 0.18, 0.15, 0.19, 0.21, 0.21],  # Row 2: Segment comparisons
            [0.12, 0.15, 0.15, 0.17, 0.12, 0.58, 0.12, 0.21, 0.17],  # Row 3: Segment comparisons
            [0.61, 0.37, 0.28, 0.19, 0.14, 0.35, 0.16, 0.86, 0.66],  # Row 4: Segment comparisons
            [0.30, 0.30, 0.38, 0.18, 0.10, 0.22, 0.09, 0.19, 0.30],  # Row 5: Segment comparisons
            [0.51, 0.34, 0.12, 0.06, 0.12, 0.19, 0.15, 0.52, 0.53],  # Row 6: Segment comparisons
            [0.26, 0.27, 0.80, 0.24, 0.20, 0.19, 0.27, 0.23, 0.22],  # Row 7: Segment comparisons
            [0.49, 0.87, 0.33, 0.27, 0.23, 0.29, 0.17, 0.34, 0.38],  # Row 8: Segment comparisons
            [0.94, 0.47, 0.33, 0.17, 0.14, 0.38, 0.18, 0.62, 0.77],  # Row 9: Segment comparisons
        ]
        
        # Heatmap grid configuration parameters
        num_rows, num_cols = 9, 9              # Grid dimensions for 9x9 similarity matrix
        heatmap_width, heatmap_height = 5.0, 5.0  # Physical dimensions of heatmap
        dx, dy = heatmap_width / num_cols, heatmap_height / num_rows  # Cell dimensions
        label_box_size = 0.40                  # Size of axis label boxes
        label_font_size = 11                   # Font size for axis labels
        value_font_size = 12                   # Font size for cell values


        # ================== HEATMAP GENERATION FUNCTION ==================
        # Helper function to create comprehensive heatmap displays with customizable parameters
        def create_final_heatmap_display(
            anchor_point,           # Base position for heatmap construction (ORIGIN for building, then moved)
            map_title_text,         # Title text displayed above the heatmap
            y_axis_label_color,     # Color for Y-axis (row) labels
            x_axis_label_color,     # Color for X-axis (column) labels
            value_accessor_func,    # Function to retrieve similarity values for each cell
            green_border_coords,    # Set of coordinates to highlight with green borders
            show_red_diagonal=True  # Whether to highlight diagonal cells with red background
            ):
            
            # Create container group for all heatmap components (grid, axes, labels, content)
            heatmap_grid_and_content = VGroup() 

            # ================== AXIS CREATION ==================
            # Create Y-axis (vertical) and X-axis (horizontal) lines
            ht_y_axis = Line(anchor_point, anchor_point + UP * heatmap_height, stroke_color=WHITE, stroke_width=1)
            ht_x_axis = Line(anchor_point, anchor_point + RIGHT * heatmap_width, stroke_color=WHITE, stroke_width=1)
            heatmap_grid_and_content.add(ht_y_axis, ht_x_axis)

            # ================== GRID LINE CONSTRUCTION ==================
            # Create horizontal and vertical grid lines for cell boundaries
            ht_grid_lines = VGroup()
            # Horizontal grid lines (for rows)
            for r_idx in range(num_rows + 1):
                y_l = anchor_point[1] + r_idx * dy
                ht_grid_lines.add(Line([anchor_point[0], y_l, 0], [anchor_point[0] + heatmap_width, y_l, 0], stroke_color=WHITE, stroke_width=0.5))
            # Vertical grid lines (for columns)
            for c_idx in range(num_cols + 1):
                x_l = anchor_point[0] + c_idx * dx
                ht_grid_lines.add(Line([x_l, anchor_point[1], 0], [x_l, anchor_point[1] + heatmap_height, 0], stroke_color=WHITE, stroke_width=0.5))
            heatmap_grid_and_content.add(ht_grid_lines)

            # ================== Y-AXIS LABELS (ROW NUMBERS) ==================
            # Create numbered labels for each row on the Y-axis
            ht_y_labels = VGroup()
            for i in range(num_rows): 
                # Create colored background box for row number
                y_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=y_axis_label_color, fill_opacity=.5, stroke_width=1)
                y_box.move_to(anchor_point + LEFT * (label_box_size/2 + 0.1) + UP * (i + .5) * dy) 
                # Add row number text inside the box
                y_text = Text(str(i + 1), font_size=label_font_size, color=WHITE).move_to(y_box.get_center())
                ht_y_labels.add(VGroup(y_box, y_text))
            heatmap_grid_and_content.add(ht_y_labels)

            # ================== X-AXIS LABELS (COLUMN NUMBERS) ==================
            # Create numbered labels for each column on the X-axis
            ht_x_labels = VGroup()
            for j in range(num_cols): 
                # Create colored background box for column number
                x_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=x_axis_label_color, fill_opacity=.5, stroke_width=1)
                x_box.move_to(anchor_point + DOWN * (label_box_size/2 + 0.1) + RIGHT * (j + .5) * dx) 
                # Add column number text inside the box
                x_text = Text(str(j + 1), font_size=label_font_size, color=WHITE).move_to(x_box.get_center())
                ht_x_labels.add(VGroup(x_box, x_text))
            heatmap_grid_and_content.add(ht_x_labels)

            # ================== CELL CONTENT AND HIGHLIGHTING ==================
            # Add similarity values and visual highlights to heatmap cells
            ht_cell_content_elements = VGroup() 
            for i_vis_row in range(num_rows): 
                for j_vis_col in range(num_cols): 
                    # Calculate center position for current cell
                    cell_center_x = anchor_point[0] + (j_vis_col + 0.5) * dx
                    cell_center_y = anchor_point[1] + (i_vis_row + 0.5) * dy
                    cell_center = [cell_center_x, cell_center_y, 0]

                    # Highlight diagonal cells with red background (self-comparison)
                    if show_red_diagonal and i_vis_row == j_vis_col:
                        red_rect = Rectangle(width=dx, height=dy, color=RED, fill_color=RED, fill_opacity=0.3, stroke_width=0).move_to(cell_center)
                        ht_cell_content_elements.add(red_rect) 
                    
                    # Add similarity values and green borders for significant matches
                    if (i_vis_row, j_vis_col) in green_border_coords:
                        # Retrieve and display similarity value
                        val = value_accessor_func(i_vis_row, j_vis_col)
                        num_text = Text(f"{val:.2f}", font_size=value_font_size, color=WHITE).move_to(cell_center)
                        ht_cell_content_elements.add(num_text) 

                        # Add green border to highlight important matches
                        green_rect = Rectangle(width=dx, height=dy, color=GREEN, stroke_width=2.5, fill_opacity=0).move_to(cell_center)
                        ht_cell_content_elements.add(green_rect) 
            
            heatmap_grid_and_content.add(ht_cell_content_elements)
            
            # ================== HEATMAP TITLE ==================
            # Create and position title above the heatmap
            ht_title = Text(map_title_text, font_size=18, color=WHITE, weight="BOLD")
            ht_title.next_to(heatmap_grid_and_content, UP, buff=0.25)

            return VGroup(ht_title, heatmap_grid_and_content)

        # ================== HEATMAP HIGHLIGHTING COORDINATES ==================
        # Define coordinates for green border highlighting in both heatmaps
        # Coordinates use visual format: (row_from_bottom, col_from_left)
        
        # Left Heatmap (Column-Wise Best Matches) - Green borders mark optimal column matches
        # These coordinates identify the highest similarity values in each column
        left_heatmap_green_coords = {
            (0,0),  # 0.94 in Col 1 - highest similarity in first column
            (1,1),  # 0.87 in Col 2 - highest similarity in second column
            (2,2),  # 0.80 in Col 3 - highest similarity in third column
            (1,3),  # 0.27 in Col 4 - highest similarity in fourth column
            (1,4),  # 0.23 in Col 5 - highest similarity in fifth column
            (6,5),  # 0.58 in Col 6 - highest similarity in sixth column
            (2,6),  # Significant match in seventh column
            # No green border in Col 7 per visual requirements
            (5,7),  # 0.86 in Col 8 - highest similarity in eighth column
            (8,8)   # 0.73 in Col 9 - highest similarity in ninth column
        }

        # Right Heatmap (Row-Wise Best Matches) - Green borders mark optimal row matches
        # These coordinates identify the highest similarity values in each row
        right_heatmap_green_coords = {
            (0,0), (1,1), (2,2), (8,3), (2,4), (7,5), (5,6), (2,7), (8,8)
        }

        # ================== HEATMAP CREATION AND POSITIONING ==================
        # Create both column-wise and row-wise heatmaps for comprehensive analysis
        
        # Left Heatmap (Column-Wise Analysis) - finds best matches within each column
        def left_value_accessor(vis_row, vis_col):
            """Accessor function for left heatmap - retrieves values for column-wise analysis"""
            return cosine_values[8 - vis_row][vis_col]

        left_heatmap_full = create_final_heatmap_display(
            anchor_point=ORIGIN, 
            map_title_text="Finding Column-Wise Best Match",
            y_axis_label_color=BLUE_E,      # Blue labels for Y-axis (rows)
            x_axis_label_color=MAROON_B,    # Maroon labels for X-axis (columns)
            value_accessor_func=left_value_accessor,
            green_border_coords=left_heatmap_green_coords,
            show_red_diagonal=True          # Highlight diagonal for self-comparison
        )
        left_heatmap_full.move_to(LEFT * 3.4 + DOWN * 0.3)  # Position on left side

        # Right Heatmap (Row-Wise Analysis) - finds best matches within each row
        def right_value_accessor(vis_row, vis_col):
            """Accessor function for right heatmap - retrieves values for row-wise analysis"""
            return cosine_values[8 - vis_col][vis_row]

        right_heatmap_full = create_final_heatmap_display(
            anchor_point=ORIGIN, 
            map_title_text="Finding Row-Wise Best Match",
            y_axis_label_color=MAROON_B,    # Maroon labels for Y-axis (rows)
            x_axis_label_color=BLUE_E,      # Blue labels for X-axis (columns)
            value_accessor_func=right_value_accessor,
            green_border_coords=right_heatmap_green_coords,
            show_red_diagonal=True          # Highlight diagonal for self-comparison
        )
        right_heatmap_full.move_to(RIGHT * 3.4 + DOWN * 0.3)  # Position on right side
        
        # ================== HEATMAP DISPLAY ANIMATION ==================
        # Animate the simultaneous appearance of both heatmaps
        heatmaps_to_fade_in = VGroup(left_heatmap_full, right_heatmap_full)
        
        # Fade in both heatmaps simultaneously for visual impact
        self.play(FadeIn(heatmaps_to_fade_in), run_time=2.0)
        self.wait(1.0)

        # ================== HEATMAP SCALING AND REPOSITIONING ==================
        # Scale down and reposition heatmaps to make room for formula display
        scale_factor = 0.75                    # Reduction factor for heatmap size
        new_y_position = UP * 0.8              # Move heatmaps higher on screen
        new_horizontal_shift = 2.8             # Adjust horizontal spacing

        # Animate scaling and repositioning of both heatmaps
        self.play(
            left_heatmap_full.animate.scale(scale_factor).move_to(LEFT * new_horizontal_shift + new_y_position),
            right_heatmap_full.animate.scale(scale_factor).move_to(RIGHT * new_horizontal_shift + new_y_position),
            run_time=1.5
        )
        self.wait(0.5)

        # ================== FORMULA DISPLAY SECTION ==================
        # Create summary box and mathematical formulas for LAS calculations
        box_width = 10.0                      # Width of formula display box
        box_height = 2.0                      # Height of formula display box
        
        # Position the summary box at the bottom center of the screen
        bottom_box_center_y_coord = DOWN * (self.camera.frame_height / 2 - box_height / 2 - 0.3) 

        # Create rounded rectangle container for formulas
        summary_box = RoundedRectangle(
            width=box_width,
            height=box_height,
            corner_radius=0.2,
            color=WHITE,
            stroke_width=2,
            fill_color=BLACK,               # Black background for contrast
            fill_opacity=0.8                # Semi-transparent for layering
        )
        summary_box.move_to(bottom_box_center_y_coord) 

        # ================== MATHEMATICAL FORMULA CONSTRUCTION ==================
        # Configure formula display parameters
        formula_font_size = 20                # Font size for mathematical expressions

        # Define sum strings for clean LaTeX formatting
        precision_sum_str = "0.94 + 0.87 + 0.80 + 0.27 + 0.23 + 0.58 + 0.27 + 0.86 + 0.73"
        recall_sum_str = "0.94 + 0.87 + 0.80 + 0.53 + 0.38 + 0.86 + 0.58 + 0.27 + 0.73"
        
        # Final calculated results with proper formatting
        precision_result_str = "0.61."        # Precision LAS result
        recall_result_str = "0.66."           # Recall LAS result
        las_result_str = "0.62"               # Final LAS score

        # Construct multi-line LaTeX string using aligned environment
        # The '&' character before '=' specifies alignment point for each equation line
        math_formulas_str = rf"""
        \begin{{aligned}}
        \text{{Precision LAS }} & = \frac{{{precision_sum_str}}}{{9}} = {precision_result_str} \\[6pt] 
        \text{{Recall LAS }} & = \frac{{{recall_sum_str}}}{{9}} = {recall_result_str} \\[6pt] 
        \text{{LAS }} & = \frac{{2 \times 0.61 \times 0.66}}{{0.61 + 0.66}} = {las_result_str}
        \end{{aligned}}
        """
        
        # Create single MathTex object for all aligned formulas
        summary_formulas = MathTex(math_formulas_str, font_size=formula_font_size)

        # Scale formulas to fit within box if necessary (with padding)
        max_text_width = box_width - 0.8 
        if summary_formulas.width > max_text_width:
            summary_formulas.scale_to_fit_width(max_text_width)
        
        # Center the aligned formulas within the summary box
        summary_formulas.move_to(summary_box.get_center())

        # ================== FORMULA ANIMATION SEQUENCE ==================
        # Animate the appearance of summary box and formulas
        self.play(DrawBorderThenFill(summary_box), run_time=1.5) 
        self.wait(0.2)
        
        # Write formulas with extended runtime for comprehensive display
        self.play(Write(summary_formulas), run_time=5.0)
        
        # Final pause to allow formula comprehension
        self.wait(5)