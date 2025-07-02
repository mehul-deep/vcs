document.addEventListener('DOMContentLoaded', function () {
    // --- Main Elements ---
    const primaryTabButtons = document.querySelectorAll('#primaryTabsNav .tab-button');
    const mainContentContainer = document.getElementById('mainContentContainer');
    const stickyHeader = document.querySelector('.sticky-header');
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');

    // --- State Variables ---
    let currentStickyHeaderHeight = stickyHeader ? stickyHeader.offsetHeight : 0;
    let apiNavLinks = [], apiRightPane, apiContentSections = [];
    let contentSectionObserver, apiSectionObserver;

    // --- Helper: Check if element is in viewport (still useful for general fade-ins) ---
    function isElementInViewport(el) {
        if (!el) return false;
        const rect = el.getBoundingClientRect();
        return (
            rect.top < window.innerHeight && rect.bottom >= 0 &&
            rect.left < window.innerWidth && rect.right >= 0
        );
    }

    // --- Update Sticky Header Height on Resize ---
    window.addEventListener('resize', () => {
        currentStickyHeaderHeight = stickyHeader ? stickyHeader.offsetHeight : 0;
        if (contentSectionObserver) setupContentSectionObserver();
        if (apiSectionObserver) setupApiTabObserver();
    });

    // --- Scroll to Element Function (generalized) ---
    function scrollToElement(targetElementId) {
        const element = document.getElementById(targetElementId);
        if (element) {
            const offset = currentStickyHeaderHeight + 20; 
            const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
            const offsetPosition = elementPosition - offset;
            
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    }

    // --- Component Discovery Management ---
    function initializeComponentDiscovery() {
        // NOTE: These elements are inside the dynamically loaded 'playground.html'
        const componentCards = mainContentContainer.querySelectorAll('.component-card');
        const modal = document.getElementById('componentModal');
        const iframe = document.getElementById('componentIframe');
        const modalTitle = document.getElementById('modalTitle');
        const modalSubtitle = document.getElementById('modalSubtitle');
        const modalIcon = document.querySelector('.modal-component-icon i');
        const closeBtn = document.getElementById('closeComponentModal');
        const prevBtn = document.getElementById('prevComponent');
        const nextBtn = document.getElementById('nextComponent');
        const loadingDiv = document.getElementById('iframeLoading');
        const comingSoonDiv = document.getElementById('iframeComingSoon');
        
        let currentComponentIndex = 0;
        // CORRECTED: This array now matches the components available in playground.html
        const components = [
            {
                id: 'introduction',
                title: 'Introduction to VCS',
                subtitle: 'Learn about video description evaluation challenges',
                icon: 'fas fa-play-circle',
                iframe: 'widgets/introduction/index.html',
                available: true
            },
            {
                id: 'gas',
                title: 'Global Alignment Score (GAS)',
                subtitle: 'Overall thematic similarity measurement',
                icon: 'fas fa-globe-americas',
                iframe: 'widgets/gas/index.html',
                available: true
            },
            {
                id: 'mapping-windows',
                title: 'Mapping Windows',
                subtitle: 'Define alignment ranges for different text lengths',
                icon: 'fas fa-window-restore',
                iframe: 'widgets/mapping-window/index.html',
                available: true
            },
            {
                id: 'best-matching',
                title: 'Best Matching Algorithm',
                subtitle: 'Establish robust chunk correspondences',
                icon: 'fas fa-magic',
                iframe: 'widgets/best-match/index.html',
                available: true
            },
            {
                id: 'las',
                title: 'Local Alignment Score (LAS)',
                subtitle: 'Fine-grained semantic quality assessment',
                icon: 'fas fa-tasks',
                iframe: 'widgets/las/index.html',
                available: true
            },
            {
                id: 'nas-distance',
                title: 'Distance-based NAS',
                subtitle: 'Penalize position deviations within windows',
                icon: 'fas fa-route',
                iframe: 'widgets/distance-nas/index.html',
                available: true
            },
            {
                id: 'nas-line',
                title: 'Line-based NAS',
                subtitle: 'Evaluate chronological flow of elements',
                icon: 'fas fa-wave-square',
                iframe: 'widgets/line-nas/index.html',
                available: true
            },
            {
                id: 'lct-nas-d',
                title: 'LCT Effect on NAS-D',
                subtitle: 'Configure chronology tolerance for Distance NAS',
                icon: 'fas fa-sliders-h',
                iframe: 'widgets/lct-nas-d/index.html',
                available: true
            },
            {
                id: 'lct-nas-l',
                title: 'LCT Effect on NAS-L',
                subtitle: 'Configure chronology tolerance for Line NAS',
                icon: 'fas fa-sliders-h',
                iframe: 'widgets/lct-nas-l/index.html',
                available: true
            },
            {
                id: 'window-regularizer',
                title: 'Window Regularizer',
                subtitle: 'Adjust NAS for extreme length disparities',
                icon: 'fas fa-window-maximize',
                iframe: 'widgets/window-regularizer/index.html',
                available: true
            },
            {
                id: 'nas',
                title: 'Narrative Alignment',
                subtitle: 'SaT segmentation and nv-embed-v2 embeddings',
                icon: 'fas fa-microchip',
                iframe: 'widgets/nas/index.html',
                available: true
            },
            {
                id: 'final-vcs',
                title: 'Final VCS Score',
                subtitle: 'Complete Video Comprehension Score calculation',
                icon: 'fas fa-calculator',
                iframe: 'widgets/vcs/index.html',
                available: true
            }
        ];
        
        if (!componentCards.length || !modal) return;
        
        // Add click handlers to component cards
        componentCards.forEach((card) => {
            const demoButton = card.querySelector('.demo-button');
            if (demoButton && !demoButton.disabled) {
                // No need to clone/replace, just add the listener.
                // This function is called on fresh content every time a tab loads.
                card.addEventListener('click', () => {
                    const componentId = card.getAttribute('data-component');
                    const componentIndex = components.findIndex(c => c.id === componentId);
                    if (componentIndex > -1) {
                       openComponentModal(componentIndex);
                    }
                });
            }
        });
        
        function openComponentModal(index) {
            if (index < 0 || index >= components.length) return;

            currentComponentIndex = index;
            const component = components[index];
            
            // Update modal content
            if (modalTitle) modalTitle.textContent = component.title;
            if (modalSubtitle) modalSubtitle.textContent = component.subtitle;
            if (modalIcon) modalIcon.className = `fas ${component.icon}`;
            
            // Show modal
            modal.classList.add('show');
            document.body.style.overflow = 'hidden';
            
            // Load component into iframe
            loadComponent(component);
            
            // Update navigation buttons
            updateNavButtons();
        }
        
        /**
         * FIXED: Robustly loads content into the iframe, solving the loading bug.
         * @param {object} component - The component object from the components array.
         */
        function loadComponent(component) {
            if (!iframe || !loadingDiv || !comingSoonDiv) return;

            // 1. Reset iframe and show loading state
            loadingDiv.style.display = 'flex';
            comingSoonDiv.classList.add('hidden');
            iframe.style.display = 'none';
            iframe.src = 'about:blank'; // Important: Clear old content and stop scripts

            if (component.available && component.iframe) {
                // 2. Use a tiny timeout to ensure the DOM has updated (good practice for modals)
                setTimeout(() => {
                    // 3. Set up event handlers *before* setting the new src
                    iframe.onload = () => {
                        loadingDiv.style.display = 'none';
                        iframe.style.display = 'block';
                    };
                    iframe.onerror = () => {
                        loadingDiv.style.display = 'none';
                        iframe.style.display = 'none';
                        comingSoonDiv.classList.remove('hidden');
                    };
                    
                    // 4. Set the new source to trigger loading
                    iframe.src = component.iframe;
                }, 50);

            } else {
                // Show "Coming Soon" for unavailable components
                loadingDiv.style.display = 'none';
                comingSoonDiv.classList.remove('hidden');
            }
        }
        
        function updateNavButtons() {
            if (prevBtn) prevBtn.disabled = currentComponentIndex === 0;
            if (nextBtn) nextBtn.disabled = currentComponentIndex === components.length - 1;
        }
        
        function navigateComponent(direction) {
            const newIndex = currentComponentIndex + direction;
            openComponentModal(newIndex);
        }
        
        function closeModal() {
            modal.classList.remove('show');
            document.body.style.overflow = '';
            // Clear iframe to stop any ongoing processes
            if (iframe) iframe.src = 'about:blank';
        }

        // --- Event Handlers for Component Modal ---
        if (closeBtn) closeBtn.addEventListener('click', closeModal);
        if (prevBtn) prevBtn.addEventListener('click', () => navigateComponent(-1));
        if (nextBtn) nextBtn.addEventListener('click', () => navigateComponent(1));
        
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });
        
        document.addEventListener('keydown', (e) => {
            if (modal.classList.contains('show')) {
                switch(e.key) {
                    case 'Escape':
                        closeModal();
                        break;
                    case 'ArrowLeft':
                        if (prevBtn && !prevBtn.disabled) navigateComponent(-1);
                        break;
                    case 'ArrowRight':
                        if (nextBtn && !nextBtn.disabled) navigateComponent(1);
                        break;
                }
            }
        });
    }

    function initializeAuthorsBox() {
        const authorsBox = mainContentContainer.querySelector('#authorsBox');
        const modal = document.getElementById('authorsModal');
        const closeBtn = document.getElementById('closeModal');
        
        if (authorsBox && modal) {
            const closeModal = () => {
                modal.classList.remove('show');
                document.body.style.overflow = '';
            };

            authorsBox.addEventListener('click', () => {
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            });
            
            if (closeBtn) closeBtn.addEventListener('click', closeModal);
            modal.addEventListener('click', (e) => {
                if (e.target === modal) closeModal();
            });
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && modal.classList.contains('show')) closeModal();
            });
        }
    }

    // --- Load Tab Content ---
    async function loadTabContent(dataSourceUrl, targetTabId) {
        try {
            const response = await fetch(dataSourceUrl);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const html = await response.text();
            mainContentContainer.innerHTML = html;

            if (typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
                MathJax.typesetPromise([mainContentContainer]);
            }
            
            if (contentSectionObserver) contentSectionObserver.disconnect();
            if (apiSectionObserver) apiSectionObserver.disconnect();

            // General setup for fade-in sections for Example and API tabs
            if (targetTabId === 'example' || targetTabId === 'api') {
                 setupContentSectionObserver(); 
                 mainContentContainer.querySelectorAll('.fade-in-section, .api-section-content').forEach(sec => {
                    if (isElementInViewport(sec)) sec.classList.add('visible');
                });
            }
            
            // Playground tab specific setup
            if (targetTabId === 'playground') {
                initializeComponentDiscovery();
                initializeAuthorsBox();
            } else if (targetTabId === 'api') { // API tab specific observer setup
                initializeApiTabElements();
                setupApiTabObserver();
            }

        } catch (error) {
            mainContentContainer.innerHTML = `<p class="text-red-500 text-center">Error loading content: ${error.message}. Please try again.</p>`;
            console.error("Error loading tab content:", error);
        }
    }

    // --- Primary Tab Switching Logic ---
    primaryTabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTabId = button.dataset.tab;
            const dataSourceUrl = button.dataset.source;

            primaryTabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            loadTabContent(dataSourceUrl, targetTabId).then(() => {
                 currentStickyHeaderHeight = stickyHeader ? stickyHeader.offsetHeight : 0; 
                 window.scrollTo({ top: 0, behavior: 'auto' }); 
            });
        });
    });

    // --- Initialize API Tab Specific Elements and Event Listeners ---
    function initializeApiTabElements() {
        apiNavLinks = mainContentContainer.querySelectorAll('#apiNavMenu .api-nav-link');
        apiRightPane = mainContentContainer.querySelector('#apiRightPane');
        apiContentSections = mainContentContainer.querySelectorAll('#apiContent .api-section-content'); 

        if (apiNavLinks.length > 0 && apiRightPane) {
            apiNavLinks.forEach(link => {
                link.removeEventListener('click', handleApiNavClick); 
                link.addEventListener('click', handleApiNavClick);
            });
        }
    }

    function handleApiNavClick(e) { 
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = mainContentContainer.querySelector(`#${targetId}`); 

        apiNavLinks.forEach(nav => nav.classList.remove('active-api-link'));
        this.classList.add('active-api-link');

        if (targetElement && apiRightPane) {
            const paneTop = apiRightPane.getBoundingClientRect().top;
            const targetTopInPane = targetElement.getBoundingClientRect().top;
            const scrollToPosition = apiRightPane.scrollTop + (targetTopInPane - paneTop) - 10; 

            apiRightPane.scrollTo({
                top: scrollToPosition,
                behavior: 'smooth'
            });
        }
    }

    // --- Scroll to Top Button Functionality ---
    if (scrollToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 100) {
                if (scrollToTopBtn.style.display !== "flex") {
                    scrollToTopBtn.style.display = "flex";
                    requestAnimationFrame(() => { scrollToTopBtn.style.opacity = "1"; });
                }
            } else {
                if (scrollToTopBtn.style.opacity === "1") {
                    scrollToTopBtn.style.opacity = "0";
                    setTimeout(() => {
                        if (scrollToTopBtn.style.opacity === "0") scrollToTopBtn.style.display = "none";
                    }, 300);
                }
            }
        });
        scrollToTopBtn.addEventListener('click', function() {
            window.scrollTo({top: 0, behavior: 'smooth'});
        });
    }

    // --- Intersection Observer for Content Sections (Fade-in) ---
    function setupContentSectionObserver() {
        if (contentSectionObserver) contentSectionObserver.disconnect(); 

        const allContentSectionsForObserver = mainContentContainer.querySelectorAll('.content-section.fade-in-section');
      
        const observerCallback = (entries) => {
            entries.forEach(entry => {
                if (!mainContentContainer.contains(entry.target)) return;
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        };
        
        const observerOptions = {
            root: null, 
            rootMargin: `-${currentStickyHeaderHeight + 24}px 0px -40% 0px`, 
            threshold: 0.01 
        };
        contentSectionObserver = new IntersectionObserver(observerCallback, observerOptions);

        allContentSectionsForObserver.forEach(section => { 
            if (section) contentSectionObserver.observe(section); 
        });
    }

    // --- Intersection Observer for API Tab ---
    function setupApiTabObserver() {
        if (apiSectionObserver) apiSectionObserver.disconnect();
        const scrollablePane = mainContentContainer.querySelector('#apiRightPane'); 
        const sectionsToObserve = mainContentContainer.querySelectorAll('#apiRightPane .content-section, #apiRightPane .api-section-content');

        if (!scrollablePane || sectionsToObserve.length === 0) {
            return;
        }
        apiRightPane = scrollablePane; 
        apiContentSections = sectionsToObserve;

        const apiObserverOptions = {
            root: apiRightPane, 
            rootMargin: "-20px 0px -60% 0px", 
            threshold: 0.01 
        };

        let lastActiveApiLink = null;

        apiSectionObserver = new IntersectionObserver(entries => {
            const activePrimaryTab = document.querySelector('#primaryTabsNav .tab-button.active');
            if (!activePrimaryTab || activePrimaryTab.dataset.tab !== 'api') {
                return; 
            }

            let bestVisibleEntry = null;
            entries.forEach(entry => {
                 if (!apiRightPane.contains(entry.target)) return; 

                if (entry.target.classList.contains('fade-in-section') || entry.target.classList.contains('api-section-content')) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                }

                if (entry.isIntersecting) {
                    if (!bestVisibleEntry || entry.boundingClientRect.top < bestVisibleEntry.boundingClientRect.top) {
                        bestVisibleEntry = entry;
                    }
                }
            });
            
            const currentApiNavLinks = mainContentContainer.querySelectorAll('#apiNavMenu .api-nav-link'); 

            if (bestVisibleEntry) {
                const id = bestVisibleEntry.target.id;
                const correspondingLink = mainContentContainer.querySelector(`.api-nav-link[href="#${id}"]`);
                if (correspondingLink && correspondingLink !== lastActiveApiLink) {
                    currentApiNavLinks.forEach(nav => nav.classList.remove('active-api-link'));
                    correspondingLink.classList.add('active-api-link');
                    lastActiveApiLink = correspondingLink;
                }
            } else if (!entries.some(e => e.isIntersecting) && lastActiveApiLink && apiRightPane.scrollTop === 0 && currentApiNavLinks.length > 0) {
                currentApiNavLinks.forEach(nav => nav.classList.remove('active-api-link'));
                currentApiNavLinks[0].classList.add('active-api-link');
                lastActiveApiLink = currentApiNavLinks[0];
            }
        }, apiObserverOptions);

        apiContentSections.forEach(section => {
            if(section) apiSectionObserver.observe(section);
        });
        
        const activePrimaryTab = document.querySelector('#primaryTabsNav .tab-button.active');
        if (activePrimaryTab && activePrimaryTab.dataset.tab === 'api') {
            setTimeout(() => { 
                if(apiRightPane && apiRightPane.scrollTop === 0 && mainContentContainer.querySelectorAll('#apiNavMenu .api-nav-link').length > 0) {
                    const currentApiNavLinks = mainContentContainer.querySelectorAll('#apiNavMenu .api-nav-link');
                     if(currentApiNavLinks.length > 0 && !lastActiveApiLink){ 
                        currentApiNavLinks.forEach(nav => nav.classList.remove('active-api-link'));
                        currentApiNavLinks[0].classList.add('active-api-link');
                        lastActiveApiLink = currentApiNavLinks[0];
                     }
                }
                 if(apiRightPane) { apiRightPane.scrollTop +=1; apiRightPane.scrollTop -=1; }
            }, 150); 
        }
    }

    // --- Event Listener for Hero CTA Buttons (delegated for main tab switching) ---
    document.addEventListener('click', function(event) {
        const ctaTabButton = event.target.closest('.hero-cta-button[data-tab-target]');
        if (ctaTabButton) {
            event.preventDefault();
            const targetTabId = ctaTabButton.dataset.tabTarget;
            const mainTabButton = document.querySelector(`#primaryTabsNav .tab-button[data-tab="${targetTabId}"]`);
            if (mainTabButton) {
                mainTabButton.click(); 
            }
            return; 
        }
    });

    // --- Initial Load ---
    const initialTabButton = document.querySelector('#primaryTabsNav .tab-button.active');
    if (initialTabButton) {
        loadTabContent(initialTabButton.dataset.source, initialTabButton.dataset.tab);
    } else {
        const firstTabButton = document.querySelector('#primaryTabsNav .tab-button');
        if (firstTabButton) {
            firstTabButton.classList.add('active'); 
            loadTabContent(firstTabButton.dataset.source, firstTabButton.dataset.tab);
        }
    }
});
