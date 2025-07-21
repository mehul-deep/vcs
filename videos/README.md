# VCS Animation Videos

This directory contains the generated MP4 video files from the Manim animation scripts.

## Video Files

### Algorithm Demonstrations

| File | Description | Duration | Size |
|------|-------------|----------|------|
| `Best_Matching.mp4` | Best Matching Algorithm visualization | ~2-3 min | ~6.3 MB |
| `VCS.mp4` | Complete Video Comprehension Score calculation | ~3-4 min | ~4.0 MB |

### Block Matching Algorithm Series

| File | Description | Duration | Size |
|------|-------------|----------|------|
| `BMA_Case1.mp4` | Case 1: Reference vs Reference comparison | ~2-3 min | ~6.4 MB |
| `BMA_Case2.mp4` | Case 2: Reference vs Generated comparison | ~2-3 min | ~5.6 MB |
| `BMA_Case3.mp4` | Case 3: Advanced matching scenarios | ~3-4 min | ~8.1 MB |

### Metric Components

| File | Description | Duration | Size |
|------|-------------|----------|------|
| `LAS.mp4` | Line Alignment Score demonstration | ~1 min | ~484 KB |
| `NASD.mp4` | Narrative Alignment Score Distance | ~2 min | ~4.4 MB |
| `SAS.mp4` | Semantic Alignment Score animation | ~1 min | ~864 KB |
| `SC.mp4` | Segmentation Component visualization | ~2 min | ~3.2 MB |

## Usage

These videos can be:
- 📺 Embedded in presentations
- 📖 Used in documentation
- 🎓 Included in educational materials
- 🌐 Shared online for research dissemination

## Regenerating Videos

To regenerate any video, run the corresponding animation script:

```bash
cd animations/
python -m manim -pql --disable_caching [SCRIPT_NAME].py FullConceptAnimation
```

## Video Specifications

- **Resolution**: 1080p (1920x1080)
- **Frame Rate**: 60 FPS
- **Format**: MP4 (H.264)
- **Quality**: Production-ready
- **Background**: Typically black with white/colored elements

## Integration with CI/CD

These videos are automatically generated and updated via GitHub Actions when:
- Code is pushed to the main branch
- Animation scripts are modified
- A release is created

See `.github/workflows/ci-cd.yml` for automation details.