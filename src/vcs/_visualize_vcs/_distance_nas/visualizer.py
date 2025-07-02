import matplotlib.pyplot as plt
from typing import Dict, Any
from ._utils import (
    setup_precision_mapping_plot, draw_precision_mapping_content, draw_precision_penalty_plot,
    setup_recall_mapping_plot, draw_recall_mapping_content, draw_recall_penalty_plot
)

def visualize_distance_nas(internals: Dict[str, Any]) -> plt.Figure:
    """
    Visualize distance-based NAS metrics with precision and recall mapping and penalty plots.
    
    Args:
        internals: The internals dictionary from VCS computation
        
    Returns:
        Figure containing precision and recall distance NAS visualizations
    """
    # Extract basic data
    ref_len = internals['texts']['reference_length']
    gen_len = internals['texts']['generated_length']
    lct = internals['config']['lct']
    
    # Get NAS data for window heights
    prec_nas_data = internals['metrics']['nas']['nas_d']['precision']
    rec_nas_data = internals['metrics']['nas']['nas_d']['recall']
    prec_window_height = prec_nas_data['mapping_window_height']
    rec_window_height = rec_nas_data['mapping_window_height']
    
    # Create figure with 2x2 subplot layout
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # PRECISION MAPPING PLOT (top-left)
    ax_prec_mapping = axes[0, 0]
    setup_precision_mapping_plot(ax_prec_mapping, gen_len, ref_len, lct, prec_window_height)
    draw_precision_mapping_content(ax_prec_mapping, internals, ref_len, gen_len, lct)
    
    # RECALL MAPPING PLOT (top-right)
    ax_rec_mapping = axes[0, 1]
    setup_recall_mapping_plot(ax_rec_mapping, ref_len, gen_len, lct, rec_window_height)
    draw_recall_mapping_content(ax_rec_mapping, internals, ref_len, gen_len, lct)
    
    # PRECISION PENALTY PLOT (bottom-left)
    ax_prec_penalties = axes[1, 0]
    draw_precision_penalty_plot(ax_prec_penalties, internals, lct)
    
    # RECALL PENALTY PLOT (bottom-right)
    ax_rec_penalties = axes[1, 1]
    draw_recall_penalty_plot(ax_rec_penalties, internals, lct)
    
    # Set overall title and layout
    fig.suptitle('Distance-based NAS Metrics', fontsize=16)
    fig.tight_layout()
    
    return fig