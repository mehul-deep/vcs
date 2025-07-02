import matplotlib.pyplot as plt
from typing import Dict, Any
from ._utils import (
    create_precision_details_figure,
    create_recall_details_figure, 
    create_summary_table_figure
)

def visualize_best_match(internals: Dict[str, Any]) -> Dict[str, plt.Figure]:

    precision_fig = create_precision_details_figure(internals)
    recall_fig = create_recall_details_figure(internals)
    summary_fig = create_summary_table_figure(internals)
    
    # Return as a dictionary for organized access
    # This pattern follows the established convention used by visualize_text_chunks
    return {
        'precision_details': precision_fig,
        'recall_details': recall_fig,
        'summary_table': summary_fig
    }