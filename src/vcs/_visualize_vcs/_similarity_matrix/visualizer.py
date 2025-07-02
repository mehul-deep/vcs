import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any
from ._utils import (
    determine_matrix_size, calculate_figure_size, calculate_tick_steps, setup_axis_ticks,
    create_similarity_heatmap, should_show_matches, highlight_all_matches, create_matrix_title
)

def visualize_similarity_matrix(internals: Dict[str, Any]) -> plt.Figure:
    """Create a heatmap visualization of the similarity matrix between text chunks.
    
    Displays the cosine similarity values between all reference and generated text
    chunks as a color-coded matrix. Optionally highlights the best matches found
    during precision and recall alignment. Essential for understanding the semantic
    relationships discovered by the algorithm.
    
    Parameters
    ----------
    internals : dict
        The internals dictionary returned by ``compute_vcs_score`` with 
        ``return_internals=True``. Must contain 'similarity', 'alignment', and 
        'texts' sections.
    
    Returns
    -------
    matplotlib.figure.Figure
        A figure containing the similarity matrix heatmap with optional match 
        highlighting. The matrix shows reference chunks on the y-axis and 
        generated chunks on the x-axis.
    
    Examples
    --------
    >>> result = compute_vcs_score(ref_text, gen_text, segmenter, embedder,
    ...                           return_internals=True)
    >>> fig = visualize_similarity_matrix(result['internals'])
    >>> fig.show()
    
    **Customize and Save:**
    
    >>> fig = visualize_similarity_matrix(result['internals'])
    >>> fig.suptitle('Custom Title: Semantic Similarity Analysis')
    >>> fig.savefig('similarity_matrix.png', dpi=300, bbox_inches='tight')
    
    Notes
    -----
    * Color intensity represents similarity strength (darker = more similar)
    * Red boxes highlight precision matches (generated → reference)
    * Blue boxes highlight recall matches (reference → generated)  
    * For very large matrices (>100x100), matches may not be shown for clarity
    * Values range from 0.0 (no similarity) to 1.0 (identical)
    
    See Also
    --------
    visualize_text_chunks : See the actual text content being compared
    visualize_best_match : Detailed analysis of matching decisions
    visualize_mapping_windows : See alignment constraints applied
    """
    # Extract data
    sim_matrix = np.array(internals['similarity']['matrix'])
    ref_len = internals['texts']['reference_length']
    gen_len = internals['texts']['generated_length']
    precision_matches = internals['alignment']['precision']['matches']
    recall_matches = internals['alignment']['recall']['matches']
    
    # Determine matrix characteristics
    matrix_size = determine_matrix_size(ref_len, gen_len)
    fig_size = calculate_figure_size(ref_len, gen_len)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=fig_size)
    
    # Create the heatmap with appropriate annotations
    create_similarity_heatmap(ax, sim_matrix, matrix_size)
    
    # Set up axis ticks
    x_step, y_step = calculate_tick_steps(ref_len, gen_len, matrix_size)
    setup_axis_ticks(ax, ref_len, gen_len, x_step, y_step)
    
    # Highlight matches if appropriate
    show_matches = should_show_matches(matrix_size, precision_matches, recall_matches)
    highlight_all_matches(ax, precision_matches, recall_matches, ref_len, gen_len, show_matches)
    
    # Set labels and title
    ax.set_xlabel('Generated Text Segments')
    ax.set_ylabel('Reference Text Segments')
    
    title = create_matrix_title(ref_len, gen_len, precision_matches, recall_matches, show_matches)
    ax.set_title(title)
    
    # Apply layout
    fig.tight_layout()
    
    return fig