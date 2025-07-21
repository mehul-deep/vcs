# Animation Scripts

This directory contains Manim animation scripts for visualizing VCS (Video Comprehension Score) algorithms and concepts.

## Animation Files

### Core Algorithm Animations

- **`Best_Matching.py`** - Visualizes the Best Matching Algorithm for text alignment
- **`VCS.py`** - Demonstrates the complete Video Comprehension Score calculation

### Block Matching Algorithm (BMA) Series

- **`BMA_Case1.py`** - Case 1: Reference vs Reference comparison
- **`BMA_Case2.py`** - Case 2: Reference vs Generated comparison  
- **`BMA_Case3.py`** - Case 3: Advanced matching scenarios

### Metric Component Animations

- **`LAS.py`** - Line Alignment Score visualization
- **`NASD.py`** - Narrative Alignment Score Distance demonstration
- **`SAS.py`** - Semantic Alignment Score animation
- **`SC.py`** - Segmentation Component visualization

## Running Animations

### Prerequisites

Install Manim and dependencies:
```bash
pip install -r requirements-demo.txt
```

### Generate Individual Animations

```bash
# Generate Best Matching animation
python -m manim -pql --disable_caching Best_Matching.py FullConceptAnimation

# Generate VCS animation
python -m manim -pql --disable_caching VCS.py FullConceptAnimation

# Generate all BMA cases
python -m manim -pql --disable_caching BMA_Case1.py FullConceptAnimation
python -m manim -pql --disable_caching BMA_Case2.py FullConceptAnimation  
python -m manim -pql --disable_caching BMA_Case3.py FullConceptAnimation

# Generate metric components
python -m manim -pql --disable_caching LAS.py FullConceptAnimation
python -m manim -pql --disable_caching NASD.py FullConceptAnimation
python -m manim -pql --disable_caching SAS.py FullConceptAnimation
python -m manim -pql --disable_caching SC.py FullConceptAnimation
```

### Batch Generation Script

```bash
#!/bin/bash
# Generate all animations
for script in *.py; do
    echo "Generating animation for $script..."
    python -m manim -pql --disable_caching "$script" FullConceptAnimation
done
```

## Output

Generated videos will be saved in the `media/videos/` directory with the following structure:
```
media/
└── videos/
    ├── best_matching/
    ├── vcs/
    ├── bma_case1/
    ├── bma_case2/
    ├── bma_case3/
    ├── las/
    ├── nasd/
    ├── sas/
    └── sc/
```

## Quality Settings

- **`-ql`** - Low quality (480p, faster rendering)
- **`-qm`** - Medium quality (720p)
- **`-qh`** - High quality (1080p)
- **`-qk`** - 4K quality (2160p, slowest)

## Troubleshooting

1. **FFmpeg not found**: Install ffmpeg system package
2. **LaTeX errors**: Install texlive-full package
3. **Memory issues**: Use lower quality settings or reduce complexity
4. **Import errors**: Ensure all dependencies are installed via requirements-demo.txt