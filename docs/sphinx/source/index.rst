VCS Metrics Documentation
=========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #0d9488, #0f766e); color: white; padding: 2rem; text-align: center; border-radius: 0.75rem; margin-bottom: 2rem; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
       <h1 style="color: white; border: none; margin: 0; font-size: 2.5rem; font-weight: 700;">VCS Metrics</h1>
       <p style="color: #ccfbf1; font-size: 1.2rem; margin: 0.5rem 0 0 0;">Video Comprehension Score - A comprehensive metric for evaluating narrative similarity</p>
   </div>

VCS Metrics is a Python library that provides a comprehensive approach to measuring narrative similarity between reference and generated text. Originally developed to evaluate the video comprehension ability of large video language models by comparing their long video descriptions to human-written captions, VCS can also be used for document-level similarity analysis or comparing similarity between two long stories and other narrative content.

VCS focuses on whether the overall story and narrative structure matches rather than worrying about every small detail. It achieves this by checking the global, local, and chronological semantic alignment between two given long paragraphs. There is no size limit in terms of paragraphs that can be processed.

To understand how VCS works in detail, please read our `research paper <#>`_ or explore our **interactive playground** available in the main website navigation.

.. image:: https://img.shields.io/pypi/v/vcs-metrics.svg
   :target: https://pypi.org/project/vcs-metrics/
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.8+

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

Key Features
------------

VCS Metrics provides a comprehensive suite of tools for narrative similarity evaluation with the following capabilities:

**🎯 Multi-Level Scoring Framework**
   Evaluates narrative similarity through three complementary metrics:
   
   * **Global Alignment Score (GAS)**: Measures semantic similarity at the full-text level using advanced embeddings
   * **Local Alignment Score (LAS)**: Evaluates segment-by-segment semantic similarity with optimal matching algorithms
   * **Narrative Alignment Score (NAS)**: Assesses chronological flow and narrative structure preservation
   
   The combined VCS score provides a holistic view of text similarity that captures both semantic content and narrative coherence.

**📊 Rich Visualization Suite**
   Generate publication-ready analysis materials:
   
   * **Similarity Heatmaps**: Visual representation of segment-to-segment alignment
   * **Alignment Path Plots**: Show how narrative structure is preserved or altered
   * **Detailed Score Breakdowns**: Component-wise analysis of each metric
   * **Comprehensive PDF Reports**: Complete analysis with all visualizations and statistics
   * **Publication-Quality Plots**: High-resolution matplotlib visualizations for research papers

**🔧 Flexible Configuration System**
   Adapt VCS to your specific use case:
   
   * **Granularity Control**: Adjust segment size and chunking strategies
   * **Matching Strictness**: Configure from strict to lenient alignment thresholds
   * **Context Windows**: Control how much surrounding context influences alignment
   * **Chronology Tolerance**: Set acceptable narrative reordering limits
   * **Custom Functions**: Integrate your own segmentation and embedding models

**📈 Advanced Analytics & Debugging**
   Deep dive into metric calculations:
   
   * **Internal Computations**: Access intermediate calculations for analysis
   * **Alignment Matrices**: Examine how segments are matched
   * **Score Decomposition**: Understand how final scores are derived
   * **Performance Metrics**: Memory usage and processing time insights
   * **Validation Tools**: Verify results and debug unexpected scores

**🎨 Research & Production Ready**
   Built for both academic research and production deployment:
   
   * **Publication Quality**: Professional visualizations for papers and presentations
   * **Scalable Processing**: Handles texts from sentences to full documents
   * **Memory Efficient**: Optimized for large-scale text comparison
   * **Reproducible Results**: Consistent scoring across different environments
   * **Comprehensive Documentation**: Detailed guides and API references

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   api

.. toctree::
   :maxdepth: 1
   :caption: Additional Resources:

   PyPI Package <https://pypi.org/project/vcs-metrics/>

Citation
--------

If you use VCS Metrics in your research, please cite:

.. code-block:: bibtex

   @software{vcs_metrics,
     title = {VCS Metrics: Video Comprehension Score for Text Similarity},
     author = {Harsh Dubey and Mukhtiar Ali and Sugam Mishra and Chulwoo Pack},
     year = {2024},
     institution = {South Dakota State University},
     note = {Python package for narrative similarity evaluation}
   }

Support
-------

- **Documentation**: You're reading it! 📖
- **PyPI Package**: Available on the Python Package Index for easy installation
- **Research Paper**: Detailed methodology and evaluation in our upcoming publication

License
-------

This project is licensed under the MIT License.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`