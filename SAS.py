"""
Semantic Alignment Score 1.1 (SAS 1.1) Animation

This Manim animation visualizes the Semantic Alignment Score (SAS) algorithm for text analysis,
demonstrating how reference and generated text are processed through embedding models to
compute semantic similarity scores using cosine similarity calculations.

The animation demonstrates:
1. Reference and generated text block visualization with enhanced styling
2. Text embedding process using nv-embed-v2 model integration
3. Prompt-driven embedding generation with visual flow indicators
4. Vector embedding representation and mathematical processing
5. Cosine similarity formula implementation and calculation
6. Final SAS score computation with animated result highlighting
7. Dynamic visual effects including glowing animations and gradient effects

Author: Mehul Deep
Date: 07/15/2025
Framework: Manim Community v0.19.0

Usage:
    python -m manim -pql --disable_caching SAS.py FullConceptAnimation
"""

from manim import (  # type: ignore
    # Core scene and animation classes
    Scene, Text, Underline, Create, Write, VGroup,
    
    # Geometric objects
    Arrow, Triangle, Line, Brace, Rectangle, RoundedRectangle,
    SurroundingRectangle, DashedVMobject, Circle,
    
    # Text and paragraph objects
    Paragraph, MathTex,
    
    # Animation functions
    GrowArrow, DrawBorderThenFill, GrowFromCenter, FadeIn, FadeOut,
    LaggedStart, ValueTracker,
    
    # Colors
    BLUE_E, GREEN_E, GREEN, RED, BLUE, YELLOW, WHITE, GREY, BLACK,
    GOLD, RED_E, MAROON_B,
    
    # Positioning and constants
    ORIGIN, UP, LEFT, RIGHT, DOWN, PI,
    
    # Text formatting
    ITALIC,
    
    # Other utilities
    np
)

class FullConceptAnimation(Scene):
    """
    Main animation class for visualizing the Semantic Alignment Score (SAS) algorithm.
    
    This animation demonstrates the complete semantic alignment process including
    text embedding generation, cosine similarity calculation, and final score
    computation with sophisticated visual effects and animations.
    """
    
    def construct(self):
        """Main animation sequence orchestrating all SAS visualization components."""
        # ================== TITLE AND HEADING SETUP ==================
        # Create and animate the main title for Semantic Alignment Score
        title = Text("Semantic Alignment Score (SAS)", font_size=25).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(0.5)

        # Move title to top edge for optimal screen space utilization
        self.play(title.animate.to_edge(UP))
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

        # Reference text content - original source material for semantic comparison
        reference_lines = [
            "The old market bell rings, starting",      # Opening market scene
            "a busy market. Vendors open their",        # Market activity introduction
            "bright stalls in the busy square,",       # Physical setting description
            "while the smell of fresh bread fills",    # Sensory details
            "the air. A young seller shouts out",      # Character introduction
            "good deals as curious people gather",     # Social interaction
            "around. The steady ring of the bell",     # Sound motif continuation
            "sets the pace for the day. A wise",       # Temporal structure
            "old vendor stops by his stall",           # Additional character
            "giving advice to those who pass by.",     # Wisdom sharing element
            "As the market gets busy, the bell",       # Activity escalation
            "rings again at midday, reminding",        # Time progression
            "everyone of the community spirit.",       # Community theme
            "A light rain briefly slows the",          # Weather element
            "crowd, but everyone's spirit stays",      # Resilience theme
            "strong. Local storytellers tell simple",  # Cultural element
            "tales that catch everyone's attention.",  # Narrative focus
            "As evening comes, the old bell rings",    # Temporal closure
            "one last time, perfectly echoing the",    # Circular narrative
            "start of the day."                       # Conclusion
        ]
        # Create a paragraph object for the reference text
        # with left alignment, line spacing, and font size
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
        # Create label for generated text box
        # with a distinct color for differentiation
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
        # with left alignment, line spacing, and font size
        # to match the reference text styling
        generated_paragraph = Paragraph(
            *generated_lines,
            alignment="LEFT",
            line_spacing=0.5,
            font_size=10,
            color=WHITE
        )
        # Set width and position for the generated paragraph
        # to ensure it fits within the generated box
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

        # ================== EMBEDDING MODEL FLOW ARROWS ==================
        # Create prominent arrows directing text to embedding model
        arrow_ref = Arrow(
            start=reference_box.get_right(),
            end=reference_box.get_right() + RIGHT * 1.0,
            buff=0.1,
            max_tip_length_to_length_ratio=0.3,  # Added for larger arrowhead
            max_stroke_width_to_length_ratio=7.5,  # Added for thicker stroke
            color=YELLOW,  # Changed to direct color setting
            stroke_width=12,  # Increased thickness
            fill_opacity=1,  # Changed for filled arrow
        )
        arrow_gen = Arrow(
            start=generated_box.get_right(),
            end=generated_box.get_right() + RIGHT * 1.0,
            buff=0.1,
            max_tip_length_to_length_ratio=0.3,  # Added for larger arrowhead
            max_stroke_width_to_length_ratio=7.5,  # Added for thicker stroke
            color=YELLOW,  # Changed to direct color setting
            stroke_width=12,  # Increased thickness
            fill_opacity=1,  # Changed for filled arrow
        )
        self.play(GrowArrow(arrow_ref), GrowArrow(arrow_gen), run_time=0.5)
        self.wait(0.5)

        # ================== EMBEDDING MODEL DISPLAY ==================
        # Create rounded boxes for embedding model visualization
        nv_box = RoundedRectangle(
            width=1.6, height=0.4,
            corner_radius=0.1,
            stroke_color=WHITE,
            fill_color=BLACK,
            fill_opacity=0.5
        )
        nv_ref_text = Text("nv-embed-v2", font_size=15).move_to(nv_box.get_center())
        nv_group_ref = VGroup(nv_box, nv_ref_text)
        nv_group_ref.next_to(arrow_ref.get_end(), RIGHT, buff=0.1)

        nv_box_gen = RoundedRectangle(
            width=1.6, height=0.4,
            corner_radius=0.1,
            stroke_color=WHITE,
            fill_color=BLACK,
            fill_opacity=0.5
        )
        nv_gen_text = Text("nv-embed-v2", font_size=15).move_to(nv_box_gen.get_center())
        nv_group_gen = VGroup(nv_box_gen, nv_gen_text)
        nv_group_gen.next_to(arrow_gen.get_end(), RIGHT, buff=0.1)

        # Animate the appearance of the rounded boxes and text
        self.play(FadeIn(nv_group_ref, shift=LEFT), FadeIn(nv_group_gen, shift=LEFT), run_time=0.5)
        self.wait(0.5)

        # ================== PROMPT INTEGRATION DISPLAY ==================
        # Create prompt text and visual connections to embedding models
        # Top prompt
        prompt_ref_text = Text('Prompt = "Prompt that goes here..."', font_size=11)
        prompt_ref_text.next_to(nv_ref_text, UP, buff=1.0)

        brace_prompt_ref = Brace(prompt_ref_text, direction=DOWN)
        brace_prompt_ref.set_stroke(width=0.3, color=WHITE)
        for submobj in brace_prompt_ref.submobjects:
            submobj.set_stroke(width=0.3, color=WHITE)

        arrow_prompt_ref = Arrow(
            start=brace_prompt_ref.get_top() + DOWN * 0.1,  # Added buffer
            end=nv_ref_text.get_top(),
            buff=0.2,
            max_tip_length_to_length_ratio=0.5,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=20,   # Added for thicker stroke
            color=YELLOW,                         # Changed from stroke_color to color
            stroke_width=10,                      # Increased thickness
            fill_opacity=1,                       # Changed to filled arrow
        )

        # Bottom prompt
        prompt_gen_text = Text('Prompt = "Prompt that goes here..."', font_size=11)
        prompt_gen_text.next_to(nv_gen_text, DOWN, buff=1.0)

        brace_prompt_gen = Brace(prompt_gen_text, direction=UP)
        brace_prompt_gen.set_stroke(width=0.1, color=WHITE)
        for submobj in brace_prompt_gen.submobjects:
            submobj.set_stroke(width=0.1, color=WHITE)

        arrow_prompt_gen = Arrow(
            start=brace_prompt_gen.get_bottom() + UP * 0.1,  # Added buffer
            end=nv_gen_text.get_bottom(),
            buff=0.2,
            max_tip_length_to_length_ratio=0.5,  # Added for proportional arrowhead
            max_stroke_width_to_length_ratio=20,   # Added for thicker stroke
            color=YELLOW,                         # Changed from stroke_color to color
            stroke_width=10,                      # Increased thickness
            fill_opacity=1,                       # Changed to filled arrow
        )

        # Animate bracket + prompt text + arrows
        self.play(
            Write(prompt_ref_text),
            GrowFromCenter(brace_prompt_ref),
            GrowArrow(arrow_prompt_ref),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            Write(prompt_gen_text),
            GrowFromCenter(brace_prompt_gen),
            GrowArrow(arrow_prompt_gen),
            run_time=0.5
        )
        self.wait(0.5)

        # ================== EMBEDDING VECTOR GENERATION ==================
        # Create and display embedding vectors produced by the models
        # 1) Create embedding text
        target_ref_text = Text(
            "[- 0.0074, - 0.0185, - 0.0023,  ......., - 0.0035, - 0.0261,  0.0315]",
            font_size=15
        )
        target_gen_text = Text(
            "[- 0.0017, - 0.0210,  0.0060,  .......,  0.0069, - 0.0165,  0.0238]",
            font_size=15
        )

        target_ref_text.next_to(nv_group_ref, RIGHT, buff=1.0)
        target_gen_text.next_to(nv_group_gen, RIGHT, buff=1.0)

        # 2) YELLOW arrows from "nv-embed-v2" to the embedding text - THICKER ARROWS
        arrow_target_ref = Arrow(
            start=nv_box.get_right(),
            end=target_ref_text.get_left(),
            buff=0.1,
            max_tip_length_to_length_ratio=0.3,  # Added for larger arrowhead
            max_stroke_width_to_length_ratio=7.5,  # Added for thicker stroke
            color=YELLOW,  # Changed to direct color setting
            stroke_width=12,  # Increased thickness
            fill_opacity=1,  # Changed for filled arrow
        )
        arrow_target_gen = Arrow(
            start=nv_box_gen.get_right(),
            end=target_gen_text.get_left(),
            buff=0.1,
            max_tip_length_to_length_ratio=0.3,  # Added for larger arrowhead
            max_stroke_width_to_length_ratio=7.5,  # Added for thicker stroke
            color=YELLOW,  # Changed to direct color setting
            stroke_width=12,  # Increased thickness
            fill_opacity=1,  # Changed for filled arrow
        )

        self.play(GrowArrow(arrow_target_ref), GrowArrow(arrow_target_gen), run_time=0.5)
        self.wait(0.5)
        self.play(Write(target_ref_text), Write(target_gen_text), run_time=0.5)
        self.wait(0.5)

        # 3) Curly braces (WHITE) around each embedding text
        brace_top_embed = Brace(target_ref_text, direction=DOWN)
        brace_top_embed.set_stroke(width=0.3, color=WHITE)
        for submobj in brace_top_embed.submobjects:
            submobj.set_stroke(width=0.3, color=WHITE)

        brace_bot_embed = Brace(target_gen_text, direction=UP)
        brace_bot_embed.set_stroke(width=0.3, color=WHITE)
        for submobj in brace_bot_embed.submobjects:
            submobj.set_stroke(width=0.3, color=WHITE)

        self.play(
            GrowFromCenter(brace_top_embed),
            GrowFromCenter(brace_bot_embed),
            run_time=0.5
        )
        self.wait(0.5)

        # ================== COSINE SIMILARITY FORMULA ==================
        # Create and position the cosine similarity formula
        # Create the cosine similarity formula using MathTex with parentheses and proper math styling
        cos_formula = MathTex(
            r"\text{Cos}(\theta) = \left(\frac{REF \cdot GEN}{||REF|| \cdot ||GEN||}\right)", 
            font_size=22  # Increased font size since we removed the box
        )
        
        # Just use the formula without a box
        cos_group = VGroup(cos_formula)

        # Position it roughly between the two embedding texts
        top_embed_pos = target_ref_text.get_center()
        bot_embed_pos = target_gen_text.get_center()
        avg_x = (top_embed_pos[0] + bot_embed_pos[0]) / 2
        avg_y = (top_embed_pos[1] + bot_embed_pos[1]) / 2
        cos_group.move_to([avg_x, avg_y, 0])

        # Modify it to shift left by adding this line after the move_to:
        cos_group.shift(LEFT * 0.67)  # Adjust the 1.5 value to control how far left it moves

        # 5) White arrows from braces to the Cosine formula - STRAIGHT VERTICAL ARROWS FROM BRACES
        # Get the horizontal position of the braces centers (they should be centered under the embedding text)
        top_brace_x = brace_top_embed.get_center()[0]
        bottom_brace_x = brace_bot_embed.get_center()[0]

        # Define arrows that start from the braces and go straight up/down to the formula
        arrow_brace_top_to_cos = Arrow(
            # Start at the center of the top brace
            start=[top_brace_x, brace_top_embed.get_center()[1], 0],
            # End directly above the start point at the formula's height
            end=[top_brace_x, cos_formula.get_top()[1] + 0.1, 0],
            buff=0.1,
            max_tip_length_to_length_ratio=0.3,
            max_stroke_width_to_length_ratio=10,
            color=YELLOW,
            stroke_width=12,
            fill_opacity=1,
        )

        arrow_brace_bot_to_cos = Arrow(
            # Start at the center of the bottom brace
            start=[bottom_brace_x, brace_bot_embed.get_center()[1], 0],
            # End directly below the start point at the formula's height
            end=[bottom_brace_x, cos_formula.get_bottom()[1] - 0.1, 0],
            buff=0.1,
            max_tip_length_to_length_ratio=0.3,
            max_stroke_width_to_length_ratio=10,
            color=YELLOW,
            stroke_width=12,
            fill_opacity=1,
        )

        # Animate the formula and arrows
        self.play(
            GrowArrow(arrow_brace_top_to_cos),
            GrowArrow(arrow_brace_bot_to_cos),
            run_time=0.5
        )
        self.wait(0.5)

        # ================== FORMULA AND RESULT DISPLAY ==================
        # Display cosine similarity formula and final SAS result
        self.play(Write(cos_formula), run_time=0.5)
        self.wait(0.5)
        
        # Split "SAS =" and "0.85" into separate text elements with more space between them
        sas_text = Text("SAS = ", font_size=15, color=WHITE)
        value_text = Text("0.85", font_size=15, color=GOLD, weight="BOLD")
        
        # Position the value text to the right of the "SAS = " text with more space
        value_text.next_to(sas_text, RIGHT, buff=0.2)  # Increased buffer for more separation
        
        # Create a group for arrangement purposes
        sas_value_group = VGroup(sas_text, value_text)
        
        # Position the group to the right of the formula
        sas_value_group.next_to(cos_formula, RIGHT, buff=1.0)
        
        # ================== RESULT HIGHLIGHTING SYSTEM ==================
        # Create glowing effect around the SAS result value
        from manim import Circle # type: ignore
        
        # Get the center of the value text
        value_center = value_text.get_center()
        
        # Create a smaller perfect circle with reduced radius
        glow_circle = Circle(
            radius=value_text.width/2 + 0.1,  # Reduced the buffer from 0.2 to 0.1
            stroke_width=2,
            stroke_color=GOLD,
            stroke_opacity=0.7,
            fill_color=BLACK,
            fill_opacity=0.4,
        ).move_to(value_center)
        
        # ================== GLOW ANIMATION SYSTEM ==================
        # Create animation tracker for dynamic glow effect
        tracker = ValueTracker(0)
        
        def update_glow(mob, alpha):
            """Dynamic glow update function for animated highlighting"""
            t_value = tracker.get_value()
            
            # Generate gradient colors and opacities
            colors = []
            opacities = []
            
            n_points = 80  # Number of gradient points around circle
            for i in range(n_points):
                # Calculate position around circle (0 to 1)
                alpha_pos = i / n_points
                # Offset by tracker value to create motion
                offset_alpha = (alpha_pos + t_value) % 1.0
                
                # Create gradient peak for glow effect
                distance = min(abs(offset_alpha - 0.5), abs(1 + offset_alpha - 0.5), abs(offset_alpha - 1.5))
                intensity = np.exp(-distance * 8) * 0.9  # Controls gradient spread
                
                # Apply gold color with varying intensity
                colors.append(GOLD)
                opacities.append(intensity)
            
            # Apply gradient to stroke only (not fill)
            mob.set_stroke(colors, width=5, opacity=opacities)
            
        # Set up glow updater for continuous animation
        glow_circle.add_updater(lambda m: update_glow(m, 0))
        
        # ================== FORMULA TO RESULT ARROW ==================
        # Create arrow connecting formula to final SAS result
        arrow_formula_to_sas = Arrow(
            start=cos_formula.get_right(),
            end=sas_value_group.get_left(),
            buff=0.2,
            max_tip_length_to_length_ratio=0.25,    # Proportional arrowhead
            max_stroke_width_to_length_ratio=8.5,   # Appropriate thickness
            color=YELLOW,                           # High visibility color
            stroke_width=10,                        # Moderate thickness
            fill_opacity=1,                         # Filled arrow
        )

        # ================== RESULT ANIMATION SEQUENCE ==================
        # Animate arrow from formula to result
        self.play(GrowArrow(arrow_formula_to_sas), run_time=0.5)
        self.wait(0.3)

        # Progressive text revelation with typing effect
        self.play(Write(sas_text), run_time=0.6)    # Write "SAS = " first
        self.play(Write(value_text), run_time=0.4)   # Then write "0.85" result
        self.wait(0.5)                               # Pause before glow activation

        # ================== GLOW EFFECT ACTIVATION ==================
        # Add glow circle and start animated highlighting
        self.add(glow_circle)
        self.play(
            tracker.animate.set_value(1),
            rate_func=lambda t: t,
            run_time=2
        )

        # Maintain continuous glow animation
        self.add(
            tracker.add_updater(lambda m, dt: m.increment_value(dt * 0.3))
        )

        # Final wait for complete visualization
        self.wait(9)