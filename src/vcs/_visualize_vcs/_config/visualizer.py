import matplotlib.pyplot as plt
from typing import Dict, Any

def visualize_config(internals: Dict[str, Any]) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis('off')
    
    config = internals['config']
    ref_len = internals['texts']['reference_length']
    gen_len = internals['texts']['generated_length']
    
    config_text = "VCS Configuration Parameters\n\n"
    config_text += f"Chunk Size: {config['chunk_size']}\n"
    config_text += f"Context Cutoff Value: {config['context_cutoff_value']:.4f}\n"
    config_text += f"Context Window Control: {config['context_window_control']:.4f}\n"
    config_text += f"Local Chronology Tolerance (LCT): {config['lct']}\n\n"
    config_text += f"Reference Length: {ref_len} | Generated Length: {gen_len}"
    
    ax.text(0.5, 0.5, config_text,
            ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle='round', facecolor='aliceblue', alpha=0.3),
            transform=ax.transAxes)
    
    plt.tight_layout()
    return fig