<div align="center">
  <h1 align="center">Video Comprehension Score (VCS)</h1>
  <a href="https://github.com/hdubey-debug/vcs">
    <img src=".github/assets/vcs-process-flow.png" alt="VCS Process Flow" width="700"/>
  </a>
  <p align="center">
    <em>A Comprehensive Python Library for Narrative Similarity Evaluation between two very long descriptions </em>
    <br />
  </p>
</div>

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/vcs-metrics?color=teal&style=for-the-badge)](https://badge.fury.io/py/vcs-metrics)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-teal?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-github.io-teal?style=for-the-badge&logo=gitbook&logoColor=white)](https://hdubey-debug.github.io/vcs/)

</div>

<p align="center">
  <a href="https://github.com/hdubey-debug/vcs/issues">🐛 Report Bug</a>
  ·
  <a href="https://github.com/hdubey-debug/vcs/discussions">💬 Community Q&A</a>
  ·
  <a href="https://colab.research.google.com/drive/1l6GXWNBGFM1UwGohnIu1b071bn8ekJIf?usp=sharing">📓 Interactive Notebook</a>
</p>

---

## 🤔 What is VCS?

Recent advancements in Large Video Language Models (LVLMs) have enabled generation of detailed, long-form narratives from complex video content. However, effectively evaluating whether these models genuinely comprehend a video's narrative—events, entities, and their interactions—remains challenging.

**The Problem with Current Metrics:**
- Traditional n-gram metrics (BLEU, ROUGE, CIDEr) suffer from the "many-to-one mapping" problem, penalizing valid stylistic variations
- They inadequately evaluate narrative chronology and structural coherence
- Embedding-based metrics struggle with context limitations in lengthy narratives
- LLM-driven methods lack consistency and often miss narrative structure assessment

**Video Comprehension Score (VCS)** addresses these limitations by providing a novel metric that evaluates dense, long-form video descriptions both semantically and structurally. VCS is designed specifically for narrative-aware evaluation, making it perfect for assessing video captioning models, story generation systems, and any application requiring deep comprehension analysis.

**VCS combines three sophisticated metrics:**
- **🌍 Global Alignment Score (GAS)**: Measures overall thematic similarity using full-text embeddings
- **🎯 Local Alignment Score (LAS)**: Assesses fine-grained semantic correspondence with optimal chunk-level matching
- **📖 Narrative Alignment Score (NAS)**: Evaluates chronological consistency with configurable tolerance for narrative flexibility

**Key Innovation:** VCS balances strict versus lenient content alignment, allowing valid descriptive variability while penalizing core narrative distortions, and integrates global and local assessments to detect structural misorderings.

---

## 🌟 Key Features

Explore the comprehensive capabilities that make VCS a powerful narrative evaluation toolkit.

<table width="100%" align="center" style="border: none; border-collapse: collapse;">
  <tr style="background-color: transparent;">
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">🧮 Comprehensive Metric Suite</summary>
        <p style="padding-top: 10px;">Computes VCS along with detailed breakdowns: GAS (global thematic similarity), LAS with precision/recall components, and NAS with distance-based and line-based sub-metrics. Access all internal calculations including penalty systems, mapping windows, and alignment paths.</p>
      </details>
    </td>
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">📊 Advanced Visualization Engine</summary>
        <p style="padding-top: 10px;">11 specialized visualization functions including similarity heatmaps, alignment analysis, best-match visualizations, narrative flow diagrams, and precision/recall breakdowns. Each metric component can be visualized with publication-quality plots.</p>
      </details>
    </td>
  </tr>
  <tr style="background-color: transparent;">
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">📋 Professional PDF Reports</summary>
        <p style="padding-top: 10px;">Generate comprehensive multi-page PDF reports with all metrics, visualizations, and analysis details. Supports both complete reports and customizable selective reports. Professional formatting suitable for research publications.</p>
      </details>
    </td>
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">⚙️ Flexible Configuration System</summary>
        <p style="padding-top: 10px;">Fine-tune evaluation with configurable parameters: chunk sizes, similarity thresholds, context windows, and Local Chronology Tolerance (LCT). Supports custom segmentation and embedding functions for domain-specific applications.</p>
      </details>
    </td>
  </tr>
</table>

---

## ⚡ Getting Started

Welcome to VCS Metrics! This guide will walk you through everything you need to start analyzing narrative similarity between texts. We'll cover installation, setup, and your first VCS analysis step by step.


---

### 📦 Step 1: Installation

Choose the installation method that fits your needs:

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🎯 **For Most Users** 
*Recommended if you just want to use VCS*

<details>
<summary><b>🖱️ Click to expand installation steps</b></summary>

<br>

**Terminal Installation:**
```bash
pip install vcs-metrics
```

**Jupyter/Colab Installation:**
```bash
!pip install vcs-metrics
```

<div align="center">

✅ **Ready in 30 seconds**  
🔥 **Zero configuration needed**  
⚡ **Instant access to all features**

</div>

</details>

</td>
<td width="50%" align="center">

### 🛠️ **For Developers**
*If you want to contribute or modify VCS*

<details>
<summary><b>🖱️ Click to expand development setup</b></summary>

<br>

**Terminal Setup:**
```bash
git clone https://github.com/hdubey-debug/vcs.git
cd vcs
pip install -e ".[dev]"
pre-commit install
```

**Jupyter/Colab Setup:**
```bash
!git clone https://github.com/hdubey-debug/vcs.git
%cd vcs
!pip install -e ".[dev]"
!pre-commit install
```

<div align="center">

🔧 **Latest features first**  
🧪 **Testing capabilities**  
🤝 **Contribution ready**

</div>

</details>

</td>
</tr>
</table>

---

### 🛠️ System Requirements

Before installing VCS, make sure your system meets these requirements:

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🐍 **Python**

<div style="background: linear-gradient(145deg, #dbeafe, #bfdbfe); padding: 20px; border-radius: 12px; border: 2px solid #3b82f6;">

<img src="https://img.shields.io/badge/Python-3.10+-306998?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>

**Required: Python 3.10 or higher**

VCS Metrics uses modern Python features and requires Python 3.10+. We recommend Python 3.11+ for optimal performance.

</div>

</td>
<td width="50%" align="center">

### 🔥 **PyTorch**

<div style="background: linear-gradient(145deg, #fed7d7, #fca5a5); padding: 20px; border-radius: 12px; border: 2px solid #dc2626;">

<img src="https://img.shields.io/badge/PyTorch-1.9+-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>

**Required: PyTorch 1.9.0+**

VCS needs PyTorch but doesn't install it automatically to avoid conflicts. Get it from the [official PyTorch website](https://pytorch.org/get-started/locally/).

**💡 Pro Tip:** In Google Colab, PyTorch is pre-installed!

</div>

</td>
</tr>
</table>

<div align="center">
<table style="border: 2px solid #10b981; border-radius: 12px; background: linear-gradient(145deg, #d1fae5, #a7f3d0); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**💡 Note:** VCS automatically installs other dependencies (numpy, matplotlib, seaborn) - you don't need to worry about them!

</td>
</tr>
</table>
</div>

---

### 🔧 Step 2: Prepare Your Functions

Now that VCS is installed, you need to define two functions before you can use the VCS API. Here's how VCS works:

#### 📋 VCS API Overview

```python
from vcs import compute_vcs_score

result = compute_vcs_score(
    reference_text="Your reference text here",
    generated_text="Your generated text here", 
    segmenter_fn=your_segmenter_function,        # ← You provide this
    embedding_fn_las=your_embedding_function,    # ← You provide this  
    embedding_fn_gas=your_embedding_function,    # ← You provide this
    return_all_metrics=True
)

print(f"VCS Score: {result['VCS']:.4f}")
```

As you can see, VCS requires two custom functions from you. Let's understand what each should do:


<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🔪 **Segmenter Function**

<div style="background: linear-gradient(145deg, #fef3c7, #fde68a); padding: 20px; border-radius: 12px; border: 2px solid #f59e0b;">

**What it does:** Splits text into meaningful segments (sentences, paragraphs, etc.)

**Required signature:**
```python
def your_segmenter(text: str) -> List[str]:
    # Your implementation here
    return list_of_text_segments
```

**You can use:** Any library or model (NLTK, spaCy, custom logic, etc.)  
**Must return:** List of strings where each string is a text segment

</div>

</td>
<td width="50%" align="center">

### 🧠 **Embedding Function**

<div style="background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 20px; border-radius: 12px; border: 2px solid #7c3aed;">

**What it does:** Converts text segments into numerical vectors (embeddings)

**Required signature:**
```python
def your_embedder(texts: List[str]) -> torch.Tensor:
    # Your implementation here  
    return tensor_of_embeddings
```

**You can use:** Any embedding model (sentence-transformers, OpenAI, etc.)  
**Must return:** PyTorch tensor of shape `(len(texts), embedding_dim)`

</div>

</td>
</tr>
</table>

#### 🌟 Author Recommendations (2025)

For best results, we recommend these state-of-the-art models:

<div align="center">
<table style="border: 2px solid #dc2626; border-radius: 12px; background: linear-gradient(145deg, #fecaca, #fca5a5); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

⚠️ **Note:** These recommendations are current as of 2025. Always research the latest SOTA options.

</td>
</tr>
</table>
</div>

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🔪 **Segmentation Champion**

<div align="center">
<img src="https://img.shields.io/badge/Segment_Any_Text-SAT-ff6b6b?style=for-the-badge&logo=artificial-intelligence&logoColor=white" alt="SAT"/>
</div>

<div style="background: linear-gradient(145deg, #fff5f5, #fed7d7); padding: 20px; border-radius: 12px; border: 2px solid #e53e3e;">

**🏆 Recommended: Segment Any Text (SAT)**

✨ **Why we recommend SAT:**
- 🎯 State-of-the-art segmentation accuracy  
- ⚡ Intelligent boundary detection  
- 🧠 Context-aware text splitting  
- 🔬 Research-grade performance  

📖 **Installation:** `pip install wtpsplit`  
🔗 **Repository:** [github.com/segment-any-text/wtpsplit](https://github.com/segment-any-text/wtpsplit)

</div>

</td>
<td width="50%" align="center">

### 🧠 **Embedding Powerhouse**

<div align="center">
<img src="https://img.shields.io/badge/NVIDIA-NV--Embed--v2-76b900?style=for-the-badge&logo=nvidia&logoColor=white" alt="NV-Embed"/>
</div>

<div style="background: linear-gradient(145deg, #f0fff4, #c6f6d5); padding: 20px; border-radius: 12px; border: 2px solid #38a169;">

**🥇 Recommended: nv-embed-v2**

🌟 **Why we recommend nv-embed-v2:**
- 📊 Top performer on [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)  
- 🚀 Superior semantic understanding  
- 💪 Robust multilingual support  
- ⚡ Excellent for VCS analysis  

📖 **Installation:** `pip install sentence-transformers`  
🔗 **Model:** [nvidia/NV-Embed-v2](https://huggingface.co/nvidia/NV-Embed-v2)

</div>

</td>
</tr>
</table>

<div align="center">
<table style="border: 2px solid #3182ce; border-radius: 12px; background: linear-gradient(145deg, #bee3f8, #90cdf4); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**💡 Alternative Options:** NLTK, spaCy, sentence-transformers, or build your own custom functions!

</td>
</tr>
</table>
</div>

---

### 💻 Step 3: Run Your First VCS Analysis

Now let's see VCS in action with a complete working example:

<div align="center">
<table style="border: 2px solid #059669; border-radius: 12px; background: linear-gradient(145deg, #d1fae5, #a7f3d0); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**⚡ Performance Notes**  
*SOTA models require GPU. For CPU testing, this example uses lightweight alternatives.*

</td>
</tr>
</table>
</div>

<details>
<summary><h3>🚀 <b>Interactive Code Example</b> - Click to expand complete tutorial</h3></summary>

<div style="background: linear-gradient(145deg, #1f2937, #111827); padding: 25px; border-radius: 15px; border: 2px solid #6366f1;">

### 🎯 **Complete Working Example**
*Copy, paste, and run this code to see VCS in action*

```python
# Fix import path issue if running from vcs/ root directory
import sys
import os
if os.path.basename(os.getcwd()) == 'vcs' and os.path.exists('src/vcs'):
    sys.path.insert(0, 'src')
    print("🔧 Fixed import path for development directory")

# Test the installation
try:
    import vcs
    print("✅ VCS package imported successfully!")
    
    # Test main function availability
    if hasattr(vcs, 'compute_vcs_score'):
        print("✅ Main function 'compute_vcs_score' is available!")
    else:
        print("⚠️ Main function not found - there might be an installation issue")
        
    # Try to get version
    try:
        print(f"📦 Version: {vcs.__version__}")
    except AttributeError:
        print("📦 Version: Unable to determine (this is normal for development installs)")
        
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("💡 Make sure you:")
    print("   1. Installed VCS correctly: pip install -e .[dev]")
    print("   2. Restarted your notebook kernel") 
    print("   3. You're NOT in the root vcs/ directory (this causes import conflicts)")

# Import required libraries
import torch
from typing import List

# Define lightweight segmenter function
def simple_segmenter(text: str) -> List[str]:
    """
    Simple sentence segmenter using period splitting.
    
    Args:
        text: Input text to segment
        
    Returns:
        List of text segments
    """
    # Split by periods and clean up
    segments = [s.strip() for s in text.split('.') if s.strip()]
    return segments

# Define lightweight embedding function using sentence-transformers
def lightweight_embedding_function(texts: List[str]) -> torch.Tensor:
    """
    Lightweight embedding function using sentence-transformers.
    
    Args:
        texts: List of text segments to embed
        
    Returns:
        PyTorch tensor of shape (len(texts), embedding_dim)
    """
    try:
        from sentence_transformers import SentenceTransformer
        
        # Use a lightweight model (only downloads ~80MB)
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Generate embeddings
        embeddings = model.encode(texts)
        return torch.tensor(embeddings, dtype=torch.float32)
        
    except ImportError:
        print("⚠️ sentence-transformers not found. Installing...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sentence-transformers"])
        
        # Try again after installation
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(texts)
        return torch.tensor(embeddings, dtype=torch.float32)

# Example texts
reference_text = """
The quick brown fox jumps over the lazy dog.
It was a beautiful sunny day in the forest.
The fox was looking for food for its family.
"""

generated_text = """
A brown fox jumped over a sleeping dog.
The weather was nice and sunny in the woods.
The fox needed to find food for its cubs.
"""

# Compute VCS score
print("🧠 Computing VCS score...")
try:
    result = vcs.compute_vcs_score(
        reference_text=reference_text,
        generated_text=generated_text,
        segmenter_fn=simple_segmenter,
        embedding_fn_las=lightweight_embedding_function,
        embedding_fn_gas=lightweight_embedding_function,
        return_all_metrics=True,
        return_internals=True
    )
    
    print("🎯 VCS Results:")
    print(f"VCS Score: {result['VCS']:.4f}")
    print(f"GAS Score: {result['GAS']:.4f}")
    print(f"LAS Score: {result['LAS']:.4f}")
    print(f"NAS Score: {result['NAS']:.4f}")
    print("✅ VCS is working correctly!")
    
    # Generate visualization (optional)
    if 'internals' in result:
        try:
            fig = vcs.visualize_metrics_summary(result['internals'])
            print("📊 Visualization generated successfully!")
            # fig.show()  # Uncomment to display
        except Exception as viz_error:
            print(f"⚠️ Visualization failed (this is normal in some environments): {viz_error}")
    
except Exception as e:
    print(f"❌ Error running VCS: {e}")
    print("💡 Make sure PyTorch is installed and try restarting your kernel")
```

<div align="center">
<table style="border: 2px solid #3b82f6; border-radius: 12px; background: linear-gradient(145deg, #dbeafe, #bfdbfe); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**📝 Scale Note:** This example uses small text for illustration - VCS excels with long-form content!  
**⚠️ Import Tip:** Running from `vcs/` root? The example includes an automatic path fix.

</td>
</tr>
</table>
</div>

</div>

</details>

---

## ⚙️ Advanced Configuration

Once you're comfortable with the basics, you can fine-tune VCS behavior for your specific use case:

<table align="center" width="100%">
<tr>
<td width="50%">

### 🎯 **Core Parameters**

<div style="background: linear-gradient(145deg, #ede9fe, #ddd6fe); padding: 20px; border-radius: 12px; border: 2px solid #7c3aed;">

**🎛️ Essential Controls:**

| Parameter | Default | Purpose |
|:----------|:-------:|:--------|
| `chunk_size` | 1 | Segment grouping |
| `context_cutoff_value` | 0.6 | Similarity threshold |
| `context_window_control` | 4.0 | Context window size |
| `lct` | 0 | Narrative reordering tolerance |

</div>

</td>
<td width="50%">

### 🚀 **Example Configuration**

<div style="background: linear-gradient(145deg, #ecfdf5, #d1fae5); padding: 20px; border-radius: 12px; border: 2px solid #059669;">

```python
from vcs import (
    DEFAULT_CONTEXT_CUTOFF_VALUE,    # 0.6
    DEFAULT_CONTEXT_WINDOW_CONTROL,  # 4.0
    DEFAULT_LCT,                     # 0
    DEFAULT_CHUNK_SIZE,              # 1
)

# 🎯 For strict matching
result = compute_vcs_score(
    reference_text=ref_text,
    generated_text=gen_text,
    segmenter_fn=segmenter,
    embedding_fn_las=embedder,
    chunk_size=2,                    # Group segments
    context_cutoff_value=0.7,        # Higher threshold
    context_window_control=3.0,      # Tighter windows
    lct=1,                          # Some reordering OK
)
```

</div>

</td>
</tr>
</table>

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>🤔 How does VCS differ from BLEU/ROUGE?</strong></summary>
<p>Unlike BLEU/ROUGE which focus on n-gram overlap, VCS evaluates semantic similarity and narrative structure preservation, making it ideal for long-form text evaluation where meaning and flow matter more than exact word matches.</p>
</details>

<details>
<summary><strong>⚡ What's the minimum text length for VCS?</strong></summary>
<p>VCS works with any text length, but it's optimized for longer texts (100+ words) where narrative structure is important. For very short texts, simpler metrics might be more appropriate.</p>
</details>

<details>
<summary><strong>🧠 Which embedding models work best?</strong></summary>
<p>We recommend checking the <a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB leaderboard</a> for the latest SOTA models. As of 2024, nv-embed-v2 and similar transformer-based models provide excellent results.</p>
</details>

<details>
<summary><strong>🚀 Can I use VCS in production?</strong></summary>
<p>Yes! VCS is production-ready with comprehensive error handling, memory optimization, and batch processing capabilities. See our performance benchmarks above.</p>
</details>

<details>
<summary><strong>🔧 How do I customize VCS parameters?</strong></summary>
<p>VCS provides several tunable parameters like <code>context_cutoff_value</code>, <code>chunk_size</code>, and <code>lct</code>. Check our documentation for detailed parameter explanations and tuning guides.</p>
</details>

---

## 🎬 Animation Gallery

**NEW! Educational Manim animations demonstrating VCS concepts**

<div align="center">
<table style="border: 2px solid #7c3aed; border-radius: 12px; background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 20px; margin: 20px 0;">
<tr>
<td align="center">

### 🎥 **Interactive Learning Through Animation**

**9 comprehensive animations** illustrating core VCS concepts and algorithms. Perfect for education, presentations, and research dissemination.

[![Animation Gallery](https://img.shields.io/badge/🎬_View_Animation_Gallery-7c3aed?style=for-the-badge&logo=play&logoColor=white)](#animation-details)

</td>
</tr>
</table>
</div>

### 🎯 **Available Animations**

<table align="center" width="100%">
<tr>
<td width="50%">

#### **🧮 Core Algorithms**

| Animation | Description | File |
|:----------|:------------|:-----|
| **VCS Overview** | Complete Video Comprehension Score calculation | `VCS.py` |
| **Best Matching** | Optimal segment pairing algorithm | `Best_Matching.py` |
| **Segmentation** | Text segmentation component | `SC.py` |

</td>
<td width="50%">

#### **📊 Metric Components**

| Animation | Description | File |
|:----------|:------------|:-----|
| **Line Alignment** | Line Alignment Score (LAS) | `LAS.py` |
| **Narrative Distance** | Narrative Alignment Score Distance | `NASD.py` |
| **Semantic Alignment** | Semantic Alignment Score (SAS) | `SAS.py` |

</td>
</tr>
</table>

#### **🔄 Block Matching Algorithm Series**

| Animation | Description | Use Case | File |
|:----------|:------------|:---------|:-----|
| **BMA Case 1** | Reference vs Reference comparison | Perfect matching baseline | `BMA_Case1.py` |
| **BMA Case 2** | Reference vs Generated comparison | Realistic evaluation scenario | `BMA_Case2.py` |
| **BMA Case 3** | Advanced matching scenarios | Complex narrative alignment | `BMA_Case3.py` |

### 🚀 **Running Animations**

<details>
<summary><b>🖱️ Click to expand animation setup and usage</b></summary>

<br>

#### **📦 Installation for Animations**

```bash
# Install animation dependencies (includes Manim)
pip install -r requirements-demo.txt

# System dependencies (Linux/WSL)
sudo apt-get install ffmpeg
```

#### **🎥 Generate Individual Animations**

```bash
# Navigate to animations directory
cd animations/

# Generate specific animation (high quality)
python -m manim -qh --disable_caching VCS.py FullConceptAnimation

# Generate all animations (batch processing)
for script in *.py; do
    echo "Generating animation for $script..."
    python -m manim -qh --disable_caching "$script" FullConceptAnimation
done
```

#### **⚙️ Quality Options**

| Flag | Quality | Resolution | Use Case |
|:-----|:--------|:-----------|:---------|
| `-ql` | Low | 480p | Quick previews |
| `-qm` | Medium | 720p | General use |
| `-qh` | High | 1080p | Presentations |
| `-qk` | 4K | 2160p | Publications |

#### **📹 Pre-generated Videos**

Pre-rendered animations are available in the [`videos/`](videos/) directory - perfect for immediate use in presentations and educational materials!

</details>

---

## 🏗️ Project Structure

```
vcs/
├── 📁 src/vcs/                  # Main package source code
│   ├── 📄 __init__.py           # Package initialization
│   ├── 📄 scorer.py             # Main VCS API entry point
│   ├── 📁 _metrics/             # Core VCS metrics implementations
│   │   ├── 📁 _gas/             # Global Alignment Score
│   │   ├── 📁 _las/             # Local Alignment Score  
│   │   ├── 📁 _nas/             # Narrative Alignment Score
│   │   └── 📁 _vcs/             # Combined VCS computation
│   ├── 📁 _visualize_vcs/       # Comprehensive visualization suite
│   │   ├── 📁 _similarity_matrix/
│   │   ├── 📁 _best_match/
│   │   ├── 📁 _distance_nas/
│   │   ├── 📁 _line_nas/
│   │   ├── 📁 _pdf_report/      # PDF report generation
│   │   └── 📁 _metrics_summary/
│   ├── 📁 _segmenting/          # Text segmentation utilities
│   ├── 📁 _matching/            # Optimal text matching algorithms
│   ├── 📁 _mapping_windows/     # Context window management
│   └── 📁 _utils/               # Helper utilities
├── 📁 animations/               # 🎬 NEW! Manim animation scripts
│   ├── 📄 VCS.py               # Complete VCS calculation demo
│   ├── 📄 Best_Matching.py     # Best matching algorithm visualization
│   ├── 📄 BMA_Case1.py         # Block matching case 1 (REF vs REF)
│   ├── 📄 BMA_Case2.py         # Block matching case 2 (REF vs GEN)
│   ├── 📄 BMA_Case3.py         # Block matching case 3 (Advanced)
│   ├── 📄 LAS.py               # Line Alignment Score demo
│   ├── 📄 NASD.py              # Narrative Alignment Distance
│   ├── 📄 SAS.py               # Semantic Alignment Score
│   ├── 📄 SC.py                # Segmentation Component
│   └── 📄 README.md            # Animation documentation
├── 📁 videos/                   # 🎥 Pre-generated MP4 animations
│   ├── 📄 VCS.mp4              # Complete VCS demonstration (~4MB)
│   ├── 📄 Best_Matching.mp4    # Best matching visualization (~6MB)
│   ├── 📄 BMA_Case1.mp4        # Case 1 animation (~6MB)
│   ├── 📄 BMA_Case2.mp4        # Case 2 animation (~6MB)
│   ├── 📄 BMA_Case3.mp4        # Case 3 animation (~8MB)
│   ├── 📄 LAS.mp4              # LAS demonstration (~500KB)
│   ├── 📄 NASD.mp4             # NASD visualization (~4MB)
│   ├── 📄 SAS.mp4              # SAS animation (~900KB)
│   ├── 📄 SC.mp4               # SC demonstration (~3MB)
│   └── 📄 README.md            # Video documentation
├── 📁 docs/                     # Documentation and interactive demos
│   ├── 📄 index.html            # Main documentation website
│   ├── 📁 pages/                # Documentation pages
│   │   ├── 📄 api.html          # API reference
│   │   ├── 📄 playground.html   # Interactive playground
│   │   └── 📄 example.html      # Usage examples
│   ├── 📁 widgets/              # Interactive visualization widgets
│   ├── 📁 sphinx/               # Sphinx documentation source
│   └── 📁 assets/               # Documentation assets (CSS, JS, videos)
├── 📁 .github/                  # GitHub configuration
│   └── 📁 workflows/            # 🚀 Enhanced CI/CD automation
│       ├── 📄 ci-cd.yml         # 🆕 Complete CI/CD pipeline with animations
│       ├── 📄 test.yml          # Continuous testing
│       ├── 📄 publish.yml       # Package publishing
│       └── 📄 docs.yml          # Documentation deployment
├── 📄 requirements-demo.txt     # 🆕 Animation dependencies (Manim + others)
├── 📄 pyproject.toml           # Package configuration & dependencies
├── 📄 CONTRIBUTING.md          # Development contribution guide
├── 📄 DEPLOYMENT.md            # Release and deployment guide
├── 📄 CHANGELOG.md             # Version history and changes
├── 📄 LICENSE                  # MIT license
└── 📄 README.md                # This documentation
```

---

## 🚀 Development & Contributing

We welcome contributions to VCS Metrics! Whether you're fixing bugs, adding features, or improving documentation, here's how to get started.

### 🛠️ Quick Development Setup

<details>
<summary><b>🖱️ Click to expand development setup</b></summary>

<br>

```bash
# 1. Clone and setup
git clone https://github.com/hdubey-debug/vcs.git
cd vcs
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install development dependencies
pip install -e .[dev]

# 3. Create your feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes
# Edit files in src/vcs/
# Add tests if needed
# Update docs if necessary

# 5. Run quality checks
black src/ && isort src/ && flake8 src/ && mypy src/

# 6. Commit with semantic format
git commit -m "minor: add new awesome feature"

# 7. Push and create PR
git push origin feature/your-feature-name
```

</details>

### 📋 Contribution Workflow

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🔄 **Development Process**

<div style="background: linear-gradient(145deg, #dbeafe, #bfdbfe); padding: 20px; border-radius: 12px; border: 2px solid #3b82f6;">

**1. Fork & Clone**  
**2. Create Feature Branch**  
**3. Make Changes**  
**4. Write Tests**  
**5. Submit PR**  
**6. Code Review**  
**7. Merge to Main**  

✅ **Automated testing on every PR**  
✅ **Fast feedback in ~2-3 minutes**

</div>

</td>
<td width="50%" align="center">

### 📦 **Release Process**

<div style="background: linear-gradient(145deg, #ecfdf5, #d1fae5); padding: 20px; border-radius: 12px; border: 2px solid #059669;">

**1. Semantic Commit Messages**  
**2. GitHub Release Creation**  
**3. Automated Version Calculation**  
**4. Package Building**  
**5. TestPyPI Publishing**  
**6. Production Release**  

🚀 **Industry-standard CI/CD pipeline**  
⚡ **Zero manual version management**

</div>

</td>
</tr>
</table>

### 💡 Semantic Commit Format

We use semantic commits for automatic version bumping:

<div align="center">
<table style="border: 2px solid #7c3aed; border-radius: 12px; background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

| **Commit Type** | **Version Bump** | **Example** |
|:---|:---:|:---|
| `patch: description` | Bug fixes | `1.0.4 → 1.0.5` |
| `minor: description` | New features | `1.0.4 → 1.1.0` |
| `major: description` | Breaking changes | `1.0.4 → 2.0.0` |

</td>
</tr>
</table>
</div>

### 🔧 Enhanced CI/CD Pipeline with Animation Generation

Our comprehensive CI/CD pipeline ensures code quality, reliability, and educational content generation:

<div align="center">
<table style="border: 2px solid #059669; border-radius: 12px; background: linear-gradient(145deg, #ecfdf5, #d1fae5); padding: 20px; margin: 20px 0;">
<tr>
<td align="center">

### 🚀 **Complete CI/CD Features**

**✅ Multi-Python Testing** - Python 3.9, 3.10, 3.11, 3.12 compatibility  
**✅ Package Validation** - Import testing & API availability  
**✅ Integration Testing** - Full getting-started example validation  
**✅ Code Quality Gates** - Black, isort, flake8, mypy enforcement  
**✅ Build & Distribution** - Wheel/source dist creation & testing  
**🎬 Animation Generation** - Automatic Manim video creation  
**🔒 Security Scanning** - Bandit & safety vulnerability checks  
**📚 Documentation** - Sphinx docs building & preview  
**🚀 Release Automation** - Smart releases with bundled assets  

**🔄 Triggers:** Every push, PR, and weekly scheduled runs

</td>
</tr>
</table>
</div>

#### **🎥 Automated Animation Pipeline**

<div align="center">
<table style="border: 2px solid #7c3aed; border-radius: 12px; background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**NEW! Automated Animation Generation**

Every push to `main` automatically:
- 🎬 Generates all 9 animations (VCS, BMA cases, metrics)
- 📦 Uploads videos as workflow artifacts (30-day retention)
- 🚀 Includes animations in GitHub releases
- ⚡ Uses continue-on-error for robust builds
- 📊 Provides detailed generation logs

**Perfect for:** Keeping animations up-to-date with code changes!

</td>
</tr>
</table>
</div>

<div align="center">
<table style="border: 2px solid #059669; border-radius: 12px; background: linear-gradient(145deg, #ecfdf5, #d1fae5); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

[![Tests](https://img.shields.io/github/actions/workflow/status/hdubey-debug/vcs/test.yml?branch=main&label=Tests&logo=github-actions&logoColor=white&style=for-the-badge)](https://github.com/hdubey-debug/vcs/actions/workflows/test.yml)
[![Build](https://img.shields.io/github/actions/workflow/status/hdubey-debug/vcs/publish.yml?label=Build&logo=github-actions&logoColor=white&style=for-the-badge)](https://github.com/hdubey-debug/vcs/actions/workflows/publish.yml)

**✅ Automated testing ensures every change is production-ready**

</td>
</tr>
</table>
</div>

### 📖 Detailed Guides

For comprehensive information about contributing and development:

<div align="center">

[![Contributing Guide](https://img.shields.io/badge/📖_Full_Contributing_Guide-2563eb?style=for-the-badge&logo=gitbook&logoColor=white)](./CONTRIBUTING.md)
[![Deployment Guide](https://img.shields.io/badge/🚀_Deployment_Guide-059669?style=for-the-badge&logo=rocket&logoColor=white)](./DEPLOYMENT.md)

</div>

**📋 [CONTRIBUTING.md](./CONTRIBUTING.md)** - Complete development setup, coding standards, testing guidelines, and submission process.

**🚀 [DEPLOYMENT.md](./DEPLOYMENT.md)** - Detailed CI/CD workflows, release process, version management, and troubleshooting.

### 🤝 Getting Help

<table align="center" width="100%">
<tr>
<td width="33%" align="center">

**🐛 Bug Reports**  
[Create GitHub Issue](https://github.com/hdubey-debug/vcs/issues)

</td>
<td width="33%" align="center">

**💬 Questions**  
[GitHub Discussions](https://github.com/hdubey-debug/vcs/discussions)

</td>
<td width="33%" align="center">

**💡 Feature Requests**  
[Feature Request Issue](https://github.com/hdubey-debug/vcs/issues/new)

</td>
</tr>
</table>

---

## 📚 Citation

If you use VCS Metrics in your research, please cite:

```bibtex
@software{vcs_metrics_2024,
  title = {VCS Metrics: Video Comprehension Score for Text Similarity Evaluation},
  author = {Harsh Dubey, Mukhtiar Ali, Sugam Mishra, and Chulwoo Pack},
  year = {2024},
  institution = {South Dakota State University},
  url = {https://github.com/hdubey-debug/vcs},
  note = {Python package for narrative similarity evaluation}
}
```

---

## 🏆 Meet Our Contributors

<div align="center">

### 🌟 **The VCS Team - Building the Future of Text Similarity**

</div>

<table>
<tr>
<td align="center">

<a href="https://github.com/hdubey-debug">
  <img src="https://github.com/hdubey-debug.png" width="100" height="100" style="border-radius: 50%;"/>
</a>

**Harsh Dubey**  
*Lead Developer & Research Scientist*  
*South Dakota State University*

| Commits | Lines | Files |
|:---:|:---:|:---:|
| **126** | **30K** | **95** |

**📋 Key Work:**
• VCS Algorithm Architecture  
• Visualization Engine  
• LAS, GAS, and NAS Metrics  

[![GitHub](https://img.shields.io/badge/-GitHub-14b8a6?style=flat&logo=github)](https://github.com/hdubey-debug)

</td>
</tr>
</table>

<div align="center">

### 🤖 **Automated Contributors**

| **Contributor** | **Role** | **Contributions** | **Badge** |
|:---:|:---:|:---:|:---:|
| 🤖 **GitHub Actions** | CI/CD Automation | 3 commits | [![Bot](https://img.shields.io/badge/Bot-Automated_Testing-6c5ce7?style=flat&logo=github-actions&logoColor=white)](#) |

### 📊 **Contribution Analytics**

[![Contributors](https://img.shields.io/github/contributors/hdubey-debug/vcs?style=for-the-badge&color=14b8a6&labelColor=0f172a)](https://github.com/hdubey-debug/vcs/graphs/contributors)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/hdubey-debug/vcs?style=for-the-badge&color=ff6b6b&labelColor=0f172a)](https://github.com/hdubey-debug/vcs/pulse)
[![Last Commit](https://img.shields.io/github/last-commit/hdubey-debug/vcs?style=for-the-badge&color=4ecdc4&labelColor=0f172a)](https://github.com/hdubey-debug/vcs/commits)
[![Code Frequency](https://img.shields.io/github/languages/count/hdubey-debug/vcs?style=for-the-badge&color=f9ca24&labelColor=0f172a)](https://github.com/hdubey-debug/vcs)

</div>

---

## 🌍 Community & Stats

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/hdubey-debug/vcs?style=social)](https://github.com/hdubey-debug/vcs/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/hdubey-debug/vcs?style=social)](https://github.com/hdubey-debug/vcs/network/members)
[![GitHub issues](https://img.shields.io/github/issues/hdubey-debug/vcs?color=red)](https://github.com/hdubey-debug/vcs/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/hdubey-debug/vcs?color=blue)](https://github.com/hdubey-debug/vcs/pulls)

![Downloads](https://img.shields.io/pypi/dm/vcs-metrics?color=teal&label=PyPI%20Downloads)
![Contributors](https://img.shields.io/github/contributors/hdubey-debug/vcs?color=orange)
![Last Commit](https://img.shields.io/github/last-commit/hdubey-debug/vcs?color=green)


</div>

---

## 🎬 CLIP-CC Benchmark Dataset

**Looking to benchmark your video models? Try our complementary dataset!**

<div align="center">
<table style="border: 2px solid #7c3aed; border-radius: 12px; background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 20px; margin: 20px 0;">
<tr>
<td align="center">

[![CLIP-CC Dataset](https://img.shields.io/badge/🤗_Hugging_Face-CLIP--CC_Dataset-ff9500?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/datasets/IVSL-SDSU/Clip-CC)

**📊 Dataset Statistics**
- 🎥 **200 Movie Clips** (90 seconds each)
- 📝 **Human-Annotated** long-form captions
- 🎯 **Designed for VCS evaluation**
- 🔬 **Research-grade quality**

</td>
</tr>
</table>
</div>

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🎯 **Perfect for VCS Evaluation**

<div style="background: linear-gradient(145deg, #dbeafe, #bfdbfe); padding: 20px; border-radius: 12px; border: 2px solid #3b82f6;">

**Why CLIP-CC + VCS?**
- 🎬 **Real movie content** with complex narratives
- 📏 **Long-form descriptions** ideal for VCS analysis
- 🧠 **Human-quality annotations** as ground truth
- 📊 **Comprehensive evaluation** of video comprehension

**Perfect for testing:**
- Video captioning models
- Video-to-text systems
- Multimodal language models
- Narrative understanding capabilities

</div>

</td>
<td width="50%" align="center">

### 🚀 **Quick Start with CLIP-CC**

<div style="background: linear-gradient(145deg, #ecfdf5, #d1fae5); padding: 20px; border-radius: 12px; border: 2px solid #059669;">

```python
# Load CLIP-CC dataset
from datasets import load_dataset
dataset = load_dataset("IVSL-SDSU/Clip-CC")

# Get reference and generated captions
reference = dataset['train'][0]['human_caption']
generated = your_model.generate_caption(video)

# Evaluate with VCS
vcs_score = compute_vcs_score(
    reference_text=reference,
    generated_text=generated,
    segmenter_fn=your_segmenter,
    embedding_fn_las=your_embedder,
    embedding_fn_gas=your_embedder,
    return_all_metrics=True
)

print(f"VCS Score: {vcs_score['VCS']:.4f}")
```

</div>

</td>
</tr>
</table>

<div align="center">
<table style="border: 2px solid #dc2626; border-radius: 12px; background: linear-gradient(145deg, #fecaca, #fca5a5); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**🎯 Challenge Your Model:** Can your video model achieve high VCS scores on CLIP-CC?  
**📈 Benchmark Goal:** Higher VCS scores indicate better narrative comprehension!

</td>
</tr>
</table>
</div>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 🌟 **Made with ❤️ by the VCS Team**

**Authors**: Harsh Dubey, Mukhtiar Ali, Sugam Mishra, and Chulwoo Pack  
**Institution**: South Dakota State University  
**Year**: 2024

[⭐ Star this repo](https://github.com/hdubey-debug/vcs) • [🐛 Report Bug](https://github.com/hdubey-debug/vcs/issues) • [💡 Request Feature](https://github.com/hdubey-debug/vcs/issues) • [💬 Join Discussion](https://github.com/hdubey-debug/vcs/discussions)

</div>
