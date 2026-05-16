:root {
    /* Primary Colors */
    --primary-color: #4F46E5;
    --primary-hover: #4338CA;
    --primary-light: #818CF8;
    --primary-dark: #3730A3;
    
    /* Status Colors */
    --success-color: #10B981;
    --success-light: #34D399;
    --success-dark: #059669;
    --warning-color: #F59E0B;
    --warning-light: #FBBF24;
    --warning-dark: #D97706;
    --danger-color: #EF4444;
    --danger-light: #F87171;
    --danger-dark: #DC2626;
    --info-color: #3B82F6;
    --info-light: #60A5FA;
    --info-dark: #2563EB;
    
    /* Neutral Colors */
    --text-primary: #1F2937;
    --text-secondary: #6B7280;
    --text-muted: #9CA3AF;
    --background-light: #F9FAFB;
    --background-white: #FFFFFF;
    --border-color: #E5E7EB;
    --border-light: #F3F4F6;
    
    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    
    /* Spacing */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;

    /* Typography */
    --font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    --font-size-xs: 0.75rem;
    --font-size-sm: 0.875rem;
    --font-size-base: 1rem;
    --font-size-lg: 1.125rem;
    --font-size-xl: 1.25rem;
    --font-size-2xl: 1.5rem;
    --font-size-3xl: 2rem;
    
    /* Border Radius */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;
    --radius-full: 9999px;
    
    /* Transitions */
    --transition-fast: 150ms ease;
    --transition-base: 200ms ease;
    --transition-slow: 300ms ease;
    --transition-slower: 500ms ease;
}

/* ============================================
   BASE STYLES & TYPOGRAPHY
   ============================================ */
.stApp {
    font-family: var(--font-family-base);
    color: var(--text-primary);
    line-height: 1.6;
}

/* Consistent heading styles */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: var(--spacing-md);
}

/* ============================================
   SCORE COLOR CLASSES
   ============================================ */
.score-excellent {
    color: var(--success-color);
    font-weight: 700;
}

.score-good {
    color: var(--warning-color);
    font-weight: 700;
}

.score-needs-improvement {
    color: var(--danger-color);
    font-weight: 700;
}

/* Score display with gradient backgrounds */
.score-display-excellent {
    background: linear-gradient(135deg, var(--success-color), var(--success-light));
    color: white;
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    text-align: center;
}

.score-display-good {
    background: linear-gradient(135deg, var(--warning-color), var(--warning-light));
    color: white;
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    text-align: center;
}

.score-display-poor {
    background: linear-gradient(135deg, var(--danger-color), var(--danger-light));
    color: white;
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    text-align: center;
}
/* ====
========================================
   CARD STYLES
   ============================================ */
.metric-card {
    background: var(--background-white);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-color);
    transition: all var(--transition-base);
}

.metric-card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-2px);
    border-color: var(--primary-light);
}

.card-elevated {
    background: var(--background-white);
    border-radius: var(--radius-lg);
    padding: var(--spacing-xl);
    box-shadow: var(--shadow-md);
    transition: all var(--transition-base);
}

.card-elevated:hover {
    box-shadow: var(--shadow-xl);
    transform: translateY(-4px);
}

.card-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: var(--radius-lg);
    padding: var(--spacing-xl);
    box-shadow: var(--shadow-lg);
}

/* ============================================
   PROGRESS BAR STYLES
   ============================================ */
.progress-container {
    background: var(--background-light);
    border-radius: var(--radius-md);
    height: 12px;
    overflow: hidden;
    position: relative;
}

.progress-bar {
    height: 100%;
    border-radius: var(--radius-md);
    transition: width var(--transition-slower) ease-in-out;
    position: relative;
    overflow: hidden;
}

/* Animated shimmer effect on progress bars */
.progress-bar::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.3),
        transparent
    );
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

.progress-bar-success {
    background: linear-gradient(90deg, var(--success-color), var(--success-light));
}

.progress-bar-warning {
    background: linear-gradient(90deg, var(--warning-color), var(--warning-light));
}

.progress-bar-danger {
    background: linear-gradient(90deg, var(--danger-color), var(--danger-light));
}

.progress-bar-info {
    background: linear-gradient(90deg, var(--info-color), var(--info-light));
}

.progress-bar-primary {
    background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
}

/* ============================================
   BADGE STYLES
   ============================================ */
.badge {
    display: inline-flex;
    align-items: center;
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: var(--radius-full);
    font-size: var(--font-size-sm);
    font-weight: 500;
    transition: all var(--transition-fast);
}

.badge-success {
    background: #D1FAE5;
    color: #065F46;
}

.badge-success:hover {
    background: #A7F3D0;
}

.badge-warning {
    background: #FEF3C7;
    color: #92400E;
}

.badge-warning:hover {
    background: #FDE68A;
}

.badge-danger {
    background: #FEE2E2;
    color: #991B1B;
}

.badge-danger:hover {
    background: #FECACA;
}

.badge-info {
    background: #DBEAFE;
    color: #1E40AF;
}

.badge-info:hover {
    background: #BFDBFE;
}

.badge-primary {
    background: #E0E7FF;
    color: #3730A3;
}

.badge-primary:hover {
    background: #C7D2FE;
}

/* ============================================
   SKILL TAG STYLES
   ============================================ */
.skill-tag {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-xs);
    padding: var(--spacing-sm) var(--spacing-md);
    margin: var(--spacing-xs);
    border-radius: var(--radius-md);
    font-size: var(--font-size-sm);
    background: var(--background-light);
    border: 1px solid var(--border-color);
    transition: all var(--transition-base);
    cursor: default;
}

.skill-tag:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow-sm);
}

.skill-tag-validated {
    background: #D1FAE5;
    border-color: var(--success-color);
    color: #065F46;
}

.skill-tag-validated::before {
    content: '✓';
    margin-right: var(--spacing-xs);
    font-weight: bold;
}

.skill-tag-unvalidated {
    background: #FEE2E2;
    border-color: var(--danger-color);
    color: #991B1B;
}

.skill-tag-unvalidated::before {
    content: '!';
    margin-right: var(--spacing-xs);
    font-weight: bold;
}

.skill-tag-neutral {
    background: var(--background-light);
    border-color: var(--border-color);
    color: var(--text-secondary);
}
/
* ============================================
   ALERT STYLES
   ============================================ */
.alert {
    padding: var(--spacing-md) var(--spacing-lg);
    border-radius: var(--radius-md);
    margin: var(--spacing-md) 0;
    display: flex;
    align-items: flex-start;
    gap: var(--spacing-md);
    animation: slideInRight var(--transition-slow);
}

.alert-icon {
    flex-shrink: 0;
    font-size: var(--font-size-xl);
}

.alert-content {
    flex: 1;
}

.alert-success {
    background: #D1FAE5;
    border-left: 4px solid var(--success-color);
    color: #065F46;
}

.alert-warning {
    background: #FEF3C7;
    border-left: 4px solid var(--warning-color);
    color: #92400E;
}

.alert-danger {
    background: #FEE2E2;
    border-left: 4px solid var(--danger-color);
    color: #991B1B;
}

.alert-info {
    background: #DBEAFE;
    border-left: 4px solid var(--info-color);
    color: #1E40AF;
}

/* ============================================
   BUTTON STYLES
   ============================================ */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-sm) var(--spacing-lg);
    border-radius: var(--radius-md);
    border: none;
    cursor: pointer;
    font-weight: 500;
    font-size: var(--font-size-base);
    transition: all var(--transition-base);
    text-decoration: none;
}

.btn:focus {
    outline: 2px solid var(--primary-light);
    outline-offset: 2px;
}

.btn-primary {
    background: var(--primary-color);
    color: white;
}

.btn-primary:hover {
    background: var(--primary-hover);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-primary:active {
    transform: translateY(0);
}

.btn-secondary {
    background: var(--background-light);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
}

.btn-secondary:hover {
    background: var(--border-color);
    border-color: var(--text-muted);
}

.btn-success {
    background: var(--success-color);
    color: white;
}

.btn-success:hover {
    background: var(--success-dark);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-danger {
    background: var(--danger-color);
    color: white;
}

.btn-danger:hover {
    background: var(--danger-dark);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-lg {
    padding: var(--spacing-md) var(--spacing-xl);
    font-size: var(--font-size-lg);
}

.btn-sm {
    padding: var(--spacing-xs) var(--spacing-md);
    font-size: var(--font-size-sm);
}
/* =====
=======================================
   SECTION HEADERS
   ============================================ */
.section-header {
    font-size: var(--font-size-xl);
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: var(--spacing-md);
    padding-bottom: var(--spacing-sm);
    border-bottom: 2px solid var(--primary-color);
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}

.section-header-icon {
    font-size: var(--font-size-2xl);
}

.section-subheader {
    font-size: var(--font-size-lg);
    font-weight: 500;
    color: var(--text-secondary);
    margin-bottom: var(--spacing-sm);
}

/* ============================================
   RECOMMENDATION ITEMS
   ============================================ */
.recommendation-item {
    padding: var(--spacing-md) var(--spacing-lg);
    margin: var(--spacing-sm) 0;
    background: var(--background-white);
    border-radius: var(--radius-md);
    border-left: 4px solid var(--primary-color);
    box-shadow: var(--shadow-sm);
    transition: all var(--transition-base);
}

.recommendation-item:hover {
    transform: translateX(4px);
    box-shadow: var(--shadow-md);
}

.recommendation-critical {
    border-left-color: var(--danger-color);
    background: linear-gradient(90deg, #FEF2F2 0%, var(--background-white) 100%);
}

.recommendation-high {
    border-left-color: var(--warning-color);
    background: linear-gradient(90deg, #FFFBEB 0%, var(--background-white) 100%);
}

.recommendation-medium {
    border-left-color: var(--info-color);
    background: linear-gradient(90deg, #EFF6FF 0%, var(--background-white) 100%);
}

.recommendation-low {
    border-left-color: var(--success-color);
    background: linear-gradient(90deg, #ECFDF5 0%, var(--background-white) 100%);
}

/* ============================================
   ANIMATION KEYFRAMES
   ============================================ */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}

@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-5px);
    }
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
/* 
Animation utility classes */
.fade-in {
    animation: fadeIn var(--transition-slow) ease-out;
}

.fade-in-up {
    animation: fadeInUp var(--transition-slow) ease-out;
}

.fade-in-down {
    animation: fadeInDown var(--transition-slow) ease-out;
}

.slide-in-left {
    animation: slideInLeft var(--transition-slow) ease-out;
}

.slide-in-right {
    animation: slideInRight var(--transition-slow) ease-out;
}

.scale-in {
    animation: scaleIn var(--transition-slow) ease-out;
}

.pulse {
    animation: pulse 2s infinite;
}

.bounce {
    animation: bounce 1s infinite;
}

.spin {
    animation: spin 1s linear infinite;
}

/* Staggered animation delays */
.delay-100 { animation-delay: 100ms; }
.delay-200 { animation-delay: 200ms; }
.delay-300 { animation-delay: 300ms; }
.delay-400 { animation-delay: 400ms; }
.delay-500 { animation-delay: 500ms; }

/* ============================================
   LOADING STATES & SPINNERS
   ============================================ */
.loading-spinner {
    display: inline-block;
    width: 24px;
    height: 24px;
    border: 3px solid var(--border-color);
    border-top-color: var(--primary-color);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
}

.loading-spinner-sm {
    width: 16px;
    height: 16px;
    border-width: 2px;
}

.loading-spinner-lg {
    width: 40px;
    height: 40px;
    border-width: 4px;
}

.loading-spinner-xl {
    width: 60px;
    height: 60px;
    border-width: 5px;
}

/* Loading overlay */
.loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255, 255, 255, 0.9);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    backdrop-filter: blur(4px);
}

.loading-text {
    margin-top: var(--spacing-md);
    color: var(--text-secondary);
    font-size: var(--font-size-lg);
    animation: pulse 1.5s infinite;
}

/* Skeleton loading */
.skeleton {
    background: linear-gradient(
        90deg,
        var(--background-light) 25%,
        var(--border-color) 50%,
        var(--background-light) 75%
    );
    background-size: 200% 100%;
    animation: skeleton-loading 1.5s infinite;
    border-radius: var(--radius-md);
}

@keyframes skeleton-loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

.skeleton-text {
    height: 1em;
    margin-bottom: var(--spacing-sm);
}

.skeleton-title {
    height: 1.5em;
    width: 60%;
    margin-bottom: var(--spacing-md);
}

.skeleton-card {
    height: 120px;
    margin-bottom: var(--spacing-md);
}

/* Dots loading animation */
.loading-dots {
    display: inline-flex;
    gap: var(--spacing-xs);
}

.loading-dots span {
    width: 8px;
    height: 8px;
    background: var(--primary-color);
    border-radius: 50%;
    animation: dotPulse 1.4s infinite ease-in-out both;
}

.loading-dots span:nth-child(1) { animation-delay: -0.32s; }
.loading-dots span:nth-child(2) { animation-delay: -0.16s; }
.loading-dots span:nth-child(3) { animation-delay: 0s; }

@keyframes dotPulse {
    0%, 80%, 100% {
        transform: scale(0);
        opacity: 0.5;
    }
    40% {
        transform: scale(1);
        opacity: 1;
    }
}
/*
 ============================================
   HOVER EFFECTS
   ============================================ */
.hover-lift {
    transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.hover-lift:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

.hover-scale {
    transition: transform var(--transition-base);
}

.hover-scale:hover {
    transform: scale(1.02);
}

.hover-glow {
    transition: box-shadow var(--transition-base);
}

.hover-glow:hover {
    box-shadow: 0 0 20px rgba(79, 70, 229, 0.3);
}

.hover-border {
    transition: border-color var(--transition-base);
    border: 2px solid transparent;
}

.hover-border:hover {
    border-color: var(--primary-color);
}

/* Interactive element hover states */
.interactive {
    cursor: pointer;
    transition: all var(--transition-base);
}

.interactive:hover {
    background-color: var(--background-light);
}

.interactive:active {
    transform: scale(0.98);
}

/* ============================================
   FORM ELEMENTS
   ============================================ */
.form-input {
    width: 100%;
    padding: var(--spacing-sm) var(--spacing-md);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    font-size: var(--font-size-base);
    transition: all var(--transition-base);
    background: var(--background-white);
}

.form-input:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.form-input:hover:not(:focus) {
    border-color: var(--text-muted);
}

.form-input::placeholder {
    color: var(--text-muted);
}

.form-label {
    display: block;
    margin-bottom: var(--spacing-xs);
    font-weight: 500;
    color: var(--text-primary);
}

.form-helper {
    margin-top: var(--spacing-xs);
    font-size: var(--font-size-sm);
    color: var(--text-muted);
}

.form-error {
    margin-top: var(--spacing-xs);
    font-size: var(--font-size-sm);
    color: var(--danger-color);
}

/* File upload area */
.file-upload-area {
    border: 2px dashed var(--border-color);
    border-radius: var(--radius-lg);
    padding: var(--spacing-2xl);
    text-align: center;
    transition: all var(--transition-base);
    cursor: pointer;
    background: var(--background-light);
}

.file-upload-area:hover {
    border-color: var(--primary-color);
    background: rgba(79, 70, 229, 0.05);
}

.file-upload-area.drag-over {
    border-color: var(--primary-color);
    background: rgba(79, 70, 229, 0.1);
    transform: scale(1.01);
}

.file-upload-icon {
    font-size: 3rem;
    color: var(--text-muted);
    margin-bottom: var(--spacing-md);
}

.file-upload-text {
    color: var(--text-secondary);
    margin-bottom: var(--spacing-sm);
}

.file-upload-hint {
    font-size: var(--font-size-sm);
    color: var(--text-muted);
}
/* ====
========================================
   TABLES & DATA DISPLAY
   ============================================ */
.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: var(--spacing-md) 0;
}

.data-table th,
.data-table td {
    padding: var(--spacing-sm) var(--spacing-md);
    text-align: left;
    border-bottom: 1px solid var(--border-color);
}

.data-table th {
    background: var(--background-light);
    font-weight: 600;
    color: var(--text-primary);
}

.data-table tr:hover {
    background: var(--background-light);
}

.data-table tr:last-child td {
    border-bottom: none;
}

/* ============================================
   TOOLTIPS
   ============================================ */
.tooltip {
    position: relative;
    cursor: help;
}

.tooltip::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    padding: var(--spacing-xs) var(--spacing-sm);
    background: var(--text-primary);
    color: white;
    font-size: var(--font-size-sm);
    border-radius: var(--radius-sm);
    white-space: nowrap;
    opacity: 0;
    visibility: hidden;
    transition: all var(--transition-fast);
    z-index: 1000;
}

.tooltip:hover::after {
    opacity: 1;
    visibility: visible;
    bottom: calc(100% + 5px);
}

/* ============================================
   MODAL & OVERLAY STYLES
   ============================================ */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9998;
    animation: fadeIn var(--transition-fast);
    backdrop-filter: blur(2px);
}

.modal-content {
    background: var(--background-white);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    max-width: 90%;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: var(--shadow-xl);
    animation: scaleIn var(--transition-base);
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--spacing-lg);
    padding-bottom: var(--spacing-md);
    border-bottom: 1px solid var(--border-color);
}

.modal-close {
    background: none;
    border: none;
    font-size: var(--font-size-xl);
    cursor: pointer;
    color: var(--text-muted);
    transition: color var(--transition-fast);
}

.modal-close:hover {
    color: var(--text-primary);
}

/* ============================================
   TABS & NAVIGATION
   ============================================ */
.tabs-container {
    display: flex;
    border-bottom: 2px solid var(--border-color);
    margin-bottom: var(--spacing-lg);
}

.tab-item {
    padding: var(--spacing-sm) var(--spacing-lg);
    cursor: pointer;
    border-bottom: 2px solid transparent;
    margin-bottom: -2px;
    transition: all var(--transition-base);
    color: var(--text-secondary);
    font-weight: 500;
}

.tab-item:hover {
    color: var(--primary-color);
    background: var(--background-light);
}

.tab-item.active {
    color: var(--primary-color);
    border-bottom-color: var(--primary-color);
}

/* ============================================
   ACCORDION / EXPANDER STYLES
   ============================================ */
.accordion-item {
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    margin-bottom: var(--spacing-sm);
    overflow: hidden;
}

.accordion-header {
    padding: var(--spacing-md) var(--spacing-lg);
    background: var(--background-light);
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background var(--transition-base);
}

.accordion-header:hover {
    background: var(--border-color);
}

.accordion-icon {
    transition: transform var(--transition-base);
}

.accordion-item.open .accordion-icon {
    transform: rotate(180deg);
}

.accordion-content {
    padding: var(--spacing-lg);
    animation: fadeIn var(--transition-base);
}
/* ====
========================================
   RESPONSIVE DESIGN - MOBILE FIRST
   ============================================ */

/* Extra small devices (phones, less than 576px) */
@media (max-width: 575.98px) {
    :root {
        --spacing-lg: 1rem;
        --spacing-xl: 1.5rem;
        --spacing-2xl: 2rem;
    }
    
    .metric-card {
        padding: var(--spacing-md);
    }
    
    .section-header {
        font-size: var(--font-size-lg);
    }
    
    .btn {
        padding: var(--spacing-sm) var(--spacing-md);
        font-size: var(--font-size-sm);
    }
    
    .btn-lg {
        padding: var(--spacing-sm) var(--spacing-lg);
        font-size: var(--font-size-base);
    }
    
    .card-elevated {
        padding: var(--spacing-md);
    }
    
    .modal-content {
        padding: var(--spacing-md);
        margin: var(--spacing-sm);
    }
    
    .tabs-container {
        flex-wrap: wrap;
    }
    
    .tab-item {
        padding: var(--spacing-xs) var(--spacing-sm);
        font-size: var(--font-size-sm);
    }
    
    .file-upload-area {
        padding: var(--spacing-lg);
    }
    
    .file-upload-icon {
        font-size: 2rem;
    }
    
    /* Stack columns on mobile */
    .mobile-stack {
        flex-direction: column !important;
    }
    
    .mobile-full-width {
        width: 100% !important;
    }
    
    /* Hide on mobile */
    .hide-mobile {
        display: none !important;
    }
}

/* Small devices (landscape phones, 576px and up) */
@media (min-width: 576px) and (max-width: 767.98px) {
    .metric-card {
        padding: var(--spacing-md);
    }
    
    .section-header {
        font-size: var(--font-size-lg);
    }
}

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) and (max-width: 991.98px) {
    .metric-card {
        padding: var(--spacing-lg);
    }
    
    /* Show on tablet and up */
    .show-tablet-up {
        display: block !important;
    }
}

/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) {
    .container-lg {
        max-width: 960px;
        margin: 0 auto;
    }
    
    /* Show on desktop only */
    .show-desktop {
        display: block !important;
    }
}

/* Extra large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) {
    .container-xl {
        max-width: 1140px;
        margin: 0 auto;
    }
}

/* Print styles */
@media print {
    .no-print {
        display: none !important;
    }
    
    .metric-card,
    .card-elevated {
        box-shadow: none;
        border: 1px solid var(--border-color);
    }
    
    .btn {
        display: none;
    }
    
    body {
        font-size: 12pt;
    }
}
/* ==
==========================================
   STREAMLIT-SPECIFIC OVERRIDES
   ============================================ */

/* Streamlit button enhancements */
.stButton > button {
    transition: all var(--transition-base) !important;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.stButton > button:active {
    transform: translateY(0);
}

/* Primary button styling */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-dark)) !important;
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, var(--primary-hover), var(--primary-dark)) !important;
}

/* Streamlit file uploader */
.stFileUploader {
    transition: all var(--transition-base);
}

.stFileUploader > div {
    border-radius: var(--radius-lg) !important;
}

.stFileUploader:hover > div {
    border-color: var(--primary-color) !important;
}

/* Streamlit progress bar */
.stProgress > div > div {
    transition: width var(--transition-slower) ease-in-out !important;
}

/* Streamlit expander */
.streamlit-expanderHeader {
    transition: background var(--transition-base) !important;
    border-radius: var(--radius-md) !important;
}

.streamlit-expanderHeader:hover {
    background: var(--background-light) !important;
}

/* Streamlit metrics */
.stMetric {
    transition: all var(--transition-base);
}

.stMetric:hover {
    transform: translateY(-2px);
}

/* Streamlit tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: var(--spacing-sm);
}

.stTabs [data-baseweb="tab"] {
    transition: all var(--transition-base) !important;
    border-radius: var(--radius-md) var(--radius-md) 0 0 !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: var(--background-light) !important;
}

/* Streamlit selectbox */
.stSelectbox > div > div {
    transition: border-color var(--transition-base) !important;
}

.stSelectbox > div > div:hover {
    border-color: var(--primary-color) !important;
}

/* Streamlit text input */
.stTextInput > div > div > input {
    transition: all var(--transition-base) !important;
}

.stTextInput > div > div > input:focus {
    border-color: var(--primary-color) !important;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
}

/* Streamlit text area */
.stTextArea > div > div > textarea {
    transition: all var(--transition-base) !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: var(--primary-color) !important;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
}

/* Streamlit radio buttons */
.stRadio > div {
    gap: var(--spacing-md) !important;
}

.stRadio label {
    transition: all var(--transition-base) !important;
    padding: var(--spacing-xs) var(--spacing-sm) !important;
    border-radius: var(--radius-sm) !important;
}

.stRadio label:hover {
    background: var(--background-light) !important;
}

/* Streamlit checkbox */
.stCheckbox label {
    transition: all var(--transition-base) !important;
}

.stCheckbox label:hover {
    color: var(--primary-color) !important;
}

/* Streamlit sidebar */
.css-1d391kg, [data-testid="stSidebar"] {
    transition: all var(--transition-base);
}

/* Streamlit download button */
.stDownloadButton > button {
    transition: all var(--transition-base) !important;
}

.stDownloadButton > button:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}
/* ==
==========================================
   UTILITY CLASSES
   ============================================ */

/* Text utilities */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }
.text-muted { color: var(--text-muted); }
.text-success { color: var(--success-color); }
.text-warning { color: var(--warning-color); }
.text-danger { color: var(--danger-color); }
.text-info { color: var(--info-color); }

.font-bold { font-weight: 700; }
.font-semibold { font-weight: 600; }
.font-medium { font-weight: 500; }
.font-normal { font-weight: 400; }

.text-xs { font-size: var(--font-size-xs); }
.text-sm { font-size: var(--font-size-sm); }
.text-base { font-size: var(--font-size-base); }
.text-lg { font-size: var(--font-size-lg); }
.text-xl { font-size: var(--font-size-xl); }
.text-2xl { font-size: var(--font-size-2xl); }
.text-3xl { font-size: var(--font-size-3xl); }

/* Spacing utilities */
.m-0 { margin: 0; }
.m-1 { margin: var(--spacing-xs); }
.m-2 { margin: var(--spacing-sm); }
.m-3 { margin: var(--spacing-md); }
.m-4 { margin: var(--spacing-lg); }
.m-5 { margin: var(--spacing-xl); }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: var(--spacing-xs); }
.mt-2 { margin-top: var(--spacing-sm); }
.mt-3 { margin-top: var(--spacing-md); }
.mt-4 { margin-top: var(--spacing-lg); }
.mt-5 { margin-top: var(--spacing-xl); }

.mb-0 { margin-bottom: 0; }
.mb-1 { margin-bottom: var(--spacing-xs); }
.mb-2 { margin-bottom: var(--spacing-sm); }
.mb-3 { margin-bottom: var(--spacing-md); }
.mb-4 { margin-bottom: var(--spacing-lg); }
.mb-5 { margin-bottom: var(--spacing-xl); }

.p-0 { padding: 0; }
.p-1 { padding: var(--spacing-xs); }
.p-2 { padding: var(--spacing-sm); }
.p-3 { padding: var(--spacing-md); }
.p-4 { padding: var(--spacing-lg); }
.p-5 { padding: var(--spacing-xl); }

/* Display utilities */
.d-none { display: none; }
.d-block { display: block; }
.d-inline { display: inline; }
.d-inline-block { display: inline-block; }
.d-flex { display: flex; }
.d-inline-flex { display: inline-flex; }
.d-grid { display: grid; }

/* Flexbox utilities */
.flex-row { flex-direction: row; }
.flex-column { flex-direction: column; }
.flex-wrap { flex-wrap: wrap; }
.flex-nowrap { flex-wrap: nowrap; }

.justify-start { justify-content: flex-start; }
.justify-end { justify-content: flex-end; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }

.align-start { align-items: flex-start; }
.align-end { align-items: flex-end; }
.align-center { align-items: center; }
.align-stretch { align-items: stretch; }

.gap-1 { gap: var(--spacing-xs); }
.gap-2 { gap: var(--spacing-sm); }
.gap-3 { gap: var(--spacing-md); }
.gap-4 { gap: var(--spacing-lg); }
.gap-5 { gap: var(--spacing-xl); }

/* Width utilities */
.w-25 { width: 25%; }
.w-50 { width: 50%; }
.w-75 { width: 75%; }
.w-100 { width: 100%; }
.w-auto { width: auto; }

/* Border utilities */
.border { border: 1px solid var(--border-color); }
.border-0 { border: none; }
.border-top { border-top: 1px solid var(--border-color); }
.border-bottom { border-bottom: 1px solid var(--border-color); }

.rounded { border-radius: var(--radius-md); }
.rounded-sm { border-radius: var(--radius-sm); }
.rounded-lg { border-radius: var(--radius-lg); }
.rounded-xl { border-radius: var(--radius-xl); }
.rounded-full { border-radius: var(--radius-full); }

/* Shadow utilities */
.shadow-none { box-shadow: none; }
.shadow-sm { box-shadow: var(--shadow-sm); }
.shadow { box-shadow: var(--shadow-md); }
.shadow-lg { box-shadow: var(--shadow-lg); }
.shadow-xl { box-shadow: var(--shadow-xl); }

/* Background utilities */
.bg-white { background-color: var(--background-white); }
.bg-light { background-color: var(--background-light); }
.bg-primary { background-color: var(--primary-color); }
.bg-success { background-color: var(--success-color); }
.bg-warning { background-color: var(--warning-color); }
.bg-danger { background-color: var(--danger-color); }
.bg-info { background-color: var(--info-color); }

/* Overflow utilities */
.overflow-hidden { overflow: hidden; }
.overflow-auto { overflow: auto; }
.overflow-scroll { overflow: scroll; }

/* Position utilities */
.position-relative { position: relative; }
.position-absolute { position: absolute; }
.position-fixed { position: fixed; }
.position-sticky { position: sticky; }

/* Cursor utilities */
.cursor-pointer { cursor: pointer; }
.cursor-default { cursor: default; }
.cursor-not-allowed { cursor: not-allowed; }

/* Visibility utilities */
.visible { visibility: visible; }
.invisible { visibility: hidden; }
.opacity-0 { opacity: 0; }
.opacity-50 { opacity: 0.5; }
.opacity-100 { opacity: 1; }

/* Transition utilities */
.transition-none { transition: none; }
.transition-fast { transition: all var(--transition-fast); }
.transition { transition: all var(--transition-base); }
.transition-slow { transition: all var(--transition-slow); }

/* ============================================
   SPECIAL COMPONENTS
   ============================================ */

/* Score circle display */
.score-circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: var(--font-size-2xl);
    box-shadow: var(--shadow-lg);
    transition: all var(--transition-base);
}

.score-circle:hover {
    transform: scale(1.05);
}

.score-circle-excellent {
    background: linear-gradient(135deg, var(--success-color), var(--success-light));
    color: white;
}

.score-circle-good {
    background: linear-gradient(135deg, var(--warning-color), var(--warning-light));
    color: white;
}

.score-circle-poor {
    background: linear-gradient(135deg, var(--danger-color), var(--danger-light));
    color: white;
}

/* Stat card */
.stat-card {
    text-align: center;
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
    color: white;
    transition: all var(--transition-base);
}

.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}

.stat-number {
    font-size: var(--font-size-3xl);
    font-weight: 700;
    margin-bottom: var(--spacing-xs);
}

.stat-label {
    font-size: var(--font-size-sm);
    opacity: 0.9;
}

/* Feature card */
.feature-card {
    padding: var(--spacing-xl);
    border-radius: var(--radius-lg);
    background: var(--background-white);
    border: 1px solid var(--border-color);
    transition: all var(--transition-base);
    height: 100%;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--primary-light);
}

.feature-icon {
    font-size: 2.5rem;
    margin-bottom: var(--spacing-md);
}

.feature-title {
    font-size: var(--font-size-lg);
    font-weight: 600;
    margin-bottom: var(--spacing-sm);
    color: var(--text-primary);
}

.feature-description {
    color: var(--text-secondary);
    font-size: var(--font-size-sm);
}

/* Step indicator */
.step-indicator {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-md);
}

.step-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.step-number {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--background-light);
    border: 2px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    margin-bottom: var(--spacing-sm);
    transition: all var(--transition-base);
}

.step-item.active .step-number {
    background: var(--primary-color);
    border-color: var(--primary-color);
    color: white;
}

.step-item.completed .step-number {
    background: var(--success-color);
    border-color: var(--success-color);
    color: white;
}

.step-connector {
    width: 60px;
    height: 2px;
    background: var(--border-color);
    margin-bottom: 30px;
}

.step-connector.completed {
    background: var(--success-color);
}

/* Divider */
.divider {
    height: 1px;
    background: var(--border-color);
    margin: var(--spacing-lg) 0;
}

.divider-vertical {
    width: 1px;
    background: var(--border-color);
    margin: 0 var(--spacing-lg);
}

/* Empty state */
.empty-state {
    text-align: center;
    padding: var(--spacing-2xl);
    color: var(--text-muted);
}

.empty-state-icon {
    font-size: 4rem;
    margin-bottom: var(--spacing-md);
    opacity: 0.5;
}

.empty-state-title {
    font-size: var(--font-size-lg);
    font-weight: 600;
    margin-bottom: var(--spacing-sm);
    color: var(--text-secondary);
}

.empty-state-description {
    font-size: var(--font-size-sm);
    max-width: 300px;
    margin: 0 auto;
}