import matplotlib.pyplot as plt
from typing import Dict, Any, List
from ._utils import (
    split_text_chunks_for_display, should_paginate_chunks, create_text_chunk_figure
)

def _visualize_chunks_generic(chunks: List[str], title: str, chunk_size: int) -> List[plt.Figure]:
    # If there are only a few chunks, display them all in one figure
    if not should_paginate_chunks(chunks):
        fig = create_text_chunk_figure(
            title,
            [(i+1, chunk) for i, chunk in enumerate(chunks)],
            len(chunks),
            1, 1,
            chunk_size
        )
        return [fig]
    
    # For many chunks, paginate
    pages = split_text_chunks_for_display(chunks)
    figures = []
    
    for i, page_chunks in enumerate(pages):
        fig = create_text_chunk_figure(
            title,
            page_chunks,
            len(chunks),
            i+1,
            len(pages),
            chunk_size
        )
        figures.append(fig)
    
    return figures

def visualize_reference_chunks(internals: Dict[str, Any]) -> List[plt.Figure]:
    ref_chunks = internals['texts']['reference_chunks']
    chunk_size = internals['config'].get('chunk_size', 1)
    
    return _visualize_chunks_generic(ref_chunks, "Reference Text Chunks", chunk_size)

def visualize_generated_chunks(internals: Dict[str, Any]) -> List[plt.Figure]:
    gen_chunks = internals['texts']['generated_chunks']
    chunk_size = internals['config'].get('chunk_size', 1)
    
    return _visualize_chunks_generic(gen_chunks, "Generated Text Chunks", chunk_size)

def visualize_text_chunks(internals: Dict[str, Any]) -> Dict[str, List[plt.Figure]]:
    """Visualize the segmented and chunked text content from both reference and generated texts.
    
    Creates structured text displays showing how the input texts were segmented and
    grouped into chunks for analysis. For large numbers of chunks, automatically 
    creates multiple pages for better readability. Essential for understanding how
    the algorithm processed the input texts.
    
    Parameters
    ----------
    internals : dict
        The internals dictionary returned by ``compute_vcs_score`` with 
        ``return_internals=True``. Must contain 'texts' section with chunk data.
    
    Returns
    -------
    dict
        Dictionary with keys 'reference_chunks' and 'generated_chunks', each 
        containing a list of matplotlib figures:
        
        * ``'reference_chunks'`` : list of plt.Figure
            One or more figures showing reference text chunks
        * ``'generated_chunks'`` : list of plt.Figure  
            One or more figures showing generated text chunks
    
    Examples
    --------
    **Basic Usage:**
    
    >>> result = compute_vcs_score(ref_text, gen_text, segmenter, embedder,
    ...                           return_internals=True)
    >>> chunk_figs = visualize_text_chunks(result['internals'])
    >>> 
    >>> # Display reference chunks (may be multiple pages)
    >>> for i, fig in enumerate(chunk_figs['reference_chunks']):
    ...     fig.suptitle(f'Reference Chunks - Page {i+1}')
    ...     fig.show()
    >>> 
    >>> # Display generated chunks  
    >>> for i, fig in enumerate(chunk_figs['generated_chunks']):
    ...     fig.suptitle(f'Generated Chunks - Page {i+1}')
    ...     fig.show()
    
    **Save All Chunk Visualizations:**
    
    >>> chunk_figs = visualize_text_chunks(result['internals'])
    >>> 
    >>> # Save reference chunk pages
    >>> for i, fig in enumerate(chunk_figs['reference_chunks']):
    ...     fig.savefig(f'ref_chunks_page_{i+1}.png', dpi=300, bbox_inches='tight')
    ...     plt.close(fig)  # Free memory
    >>> 
    >>> # Save generated chunk pages
    >>> for i, fig in enumerate(chunk_figs['generated_chunks']):
    ...     fig.savefig(f'gen_chunks_page_{i+1}.png', dpi=300, bbox_inches='tight')
    ...     plt.close(fig)
    
    Notes
    -----
    * Chunks are automatically paginated when there are more than 25 chunks per page
    * Each chunk is numbered according to its position in the analysis
    * Text is automatically wrapped for better readability
    * Useful for debugging segmentation issues or understanding text preprocessing
    
    See Also
    --------
    visualize_similarity_matrix : See how chunks relate to each other
    visualize_mapping_windows : Understand chunk alignment windows
    """
    ref_figs = visualize_reference_chunks(internals)
    gen_figs = visualize_generated_chunks(internals)
    
    return {
        'reference_chunks': ref_figs,
        'generated_chunks': gen_figs
    }