#!/bin/bash
# VCS Animation Generation Script
# Generates all Manim animations for the VCS project

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Configuration
ANIMATIONS_DIR="animations"
OUTPUT_DIR="generated_videos"
QUALITY="${QUALITY:-qh}"  # Default to high quality, can be overridden with env var
DISABLE_CACHING="--disable_caching"

# Animation files to process
ANIMATIONS=(
    "VCS.py"
    "Best_Matching.py"
    "BMA_Case1.py"
    "BMA_Case2.py" 
    "BMA_Case3.py"
    "LAS.py"
    "NASD.py"
    "SAS.py"
    "SC.py"
)

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${PURPLE}========================================${NC}"
    echo -e "${PURPLE}  VCS Animation Generation Script${NC}"
    echo -e "${PURPLE}========================================${NC}"
}

# Function to check dependencies
check_dependencies() {
    print_status "Checking dependencies..."
    
    # Check if Python is available
    if ! command -v python &> /dev/null; then
        print_error "Python is not installed or not in PATH"
        exit 1
    fi
    
    # Check if manim is available
    if ! python -c "import manim" 2> /dev/null; then
        print_error "Manim is not installed. Install with: pip install -r requirements-demo.txt"
        exit 1
    fi
    
    # Check if animations directory exists
    if [ ! -d "$ANIMATIONS_DIR" ]; then
        print_error "Animations directory '$ANIMATIONS_DIR' not found"
        exit 1
    fi
    
    print_success "All dependencies checked"
}

# Function to create output directory
setup_output_dir() {
    if [ ! -d "$OUTPUT_DIR" ]; then
        mkdir -p "$OUTPUT_DIR"
        print_status "Created output directory: $OUTPUT_DIR"
    fi
}

# Function to generate a single animation
generate_animation() {
    local script_name="$1"
    local script_path="$ANIMATIONS_DIR/$script_name"
    
    if [ ! -f "$script_path" ]; then
        print_warning "Animation script not found: $script_path"
        return 1
    fi
    
    print_status "Generating animation: $script_name"
    echo -e "  Quality: ${QUALITY}"
    echo -e "  Command: python -m manim -${QUALITY} ${DISABLE_CACHING} $script_path FullConceptAnimation"
    
    # Run manim with error handling
    if python -m manim -"${QUALITY}" $DISABLE_CACHING "$script_path" FullConceptAnimation; then
        print_success "Completed: $script_name"
        return 0
    else
        print_error "Failed to generate: $script_name"
        return 1
    fi
}

# Function to show usage
show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -q, --quality QUALITY    Set quality level (ql|qm|qh|qk) [default: qh]"
    echo "  -h, --help              Show this help message"
    echo "  -l, --list              List available animations"
    echo "  -s, --single SCRIPT     Generate only a specific script"
    echo ""
    echo "Quality levels:"
    echo "  ql - Low quality (480p, fast)"
    echo "  qm - Medium quality (720p)"
    echo "  qh - High quality (1080p) [default]"
    echo "  qk - 4K quality (2160p, slow)"
    echo ""
    echo "Environment variables:"
    echo "  QUALITY - Override default quality level"
    echo ""
    echo "Examples:"
    echo "  $0                           # Generate all animations in high quality"
    echo "  $0 -q ql                     # Generate all animations in low quality"
    echo "  $0 -s VCS.py                 # Generate only VCS animation"
    echo "  QUALITY=qm $0                # Use environment variable for quality"
}

# Function to list available animations
list_animations() {
    echo "Available animations:"
    for i in "${!ANIMATIONS[@]}"; do
        printf "%2d. %s\n" $((i+1)) "${ANIMATIONS[$i]}"
    done
}

# Main function
main() {
    local single_script=""
    
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -q|--quality)
                QUALITY="$2"
                shift 2
                ;;
            -h|--help)
                show_usage
                exit 0
                ;;
            -l|--list)
                list_animations
                exit 0
                ;;
            -s|--single)
                single_script="$2"
                shift 2
                ;;
            *)
                print_error "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
    done
    
    # Validate quality parameter
    case $QUALITY in
        ql|qm|qh|qk)
            ;;
        *)
            print_error "Invalid quality level: $QUALITY. Use ql, qm, qh, or qk"
            exit 1
            ;;
    esac
    
    print_header
    print_status "Starting animation generation process"
    print_status "Quality level: $QUALITY"
    
    # Check dependencies
    check_dependencies
    
    # Setup output directory
    setup_output_dir
    
    # Change to animations directory
    cd "$ANIMATIONS_DIR"
    
    local success_count=0
    local total_count=0
    local failed_animations=()
    
    if [ -n "$single_script" ]; then
        # Generate single animation
        print_status "Generating single animation: $single_script"
        if generate_animation "$single_script"; then
            success_count=1
        else
            failed_animations+=("$single_script")
        fi
        total_count=1
    else
        # Generate all animations
        print_status "Generating ${#ANIMATIONS[@]} animations"
        
        for script in "${ANIMATIONS[@]}"; do
            echo ""
            if generate_animation "$script"; then
                ((success_count++))
            else
                failed_animations+=("$script")
            fi
            ((total_count++))
        done
    fi
    
    # Print summary
    echo ""
    print_header
    print_status "Generation Summary:"
    print_success "Successfully generated: $success_count/$total_count animations"
    
    if [ ${#failed_animations[@]} -gt 0 ]; then
        print_warning "Failed animations:"
        for failed in "${failed_animations[@]}"; do
            echo "  - $failed"
        done
    fi
    
    # Return to original directory
    cd - > /dev/null
    
    # Check for generated files
    if ls media/videos/*/*.mp4 1> /dev/null 2>&1; then
        print_status "Generated videos found in media/videos/"
        print_status "You can also find videos in the videos/ directory"
    fi
    
    if [ $success_count -eq $total_count ]; then
        print_success "All animations generated successfully! 🎉"
        exit 0
    else
        print_warning "Some animations failed to generate"
        exit 1
    fi
}

# Run main function with all arguments
main "$@"