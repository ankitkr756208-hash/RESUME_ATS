<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ATS Resume Score Report</title>
    <style>
        /* ── Page & Typography ── */
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #1e293b;
            margin: 0;
            padding: 40px 50px;
            line-height: 1.6;
            background: #fff;
        }

        /* ── Page Header ── */
        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            border-bottom: 3px solid #1e293b;
            padding-bottom: 14px;
            margin-bottom: 32px;
        }
        .page-header .report-label {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #64748b;
        }
        .page-header .date {
            font-size: 12px;
            color: #64748b;
        }

        /* ── Report Title ── */
        .report-title {
            font-size: 30px;
            font-weight: 900;
            color: #0f172a;
            margin: 0 0 30px 0;
            letter-spacing: -0.5px;
        }

        /* ── Overall Score Box ── */
        .score-section {
            text-align: center;
            margin-bottom: 36px;
        }
        .score-label {
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #475569;
            margin-bottom: 8px;
        }
        .score-number {
            font-size: 80px;
            font-weight: 900;
            line-height: 1;
            letter-spacing: -3px;
        }
        .score-denom {
            font-size: 36px;
            font-weight: 400;
            color: #94a3b8;
            letter-spacing: -1px;
        }
        .score-interpretation {
            font-size: 15px;
            color: #475569;
            margin-top: 10px;
            font-style: italic;
        }

        /* ── Section Headings ── */
        h2 {
            font-size: 16px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: #334155;
            margin: 32px 0 16px 0;
            padding-bottom: 8px;
            border-bottom: 2px solid #e2e8f0;
        }

        /* ── Score Breakdown Table with Progress Bars ── */
        .breakdown-row {
            display: flex;
            align-items: center;
            margin-bottom: 14px;
            gap: 14px;
        }
        .breakdown-label {
            width: 160px;
            font-size: 13px;
            font-weight: 600;
            color: #334155;
            flex-shrink: 0;
        }
        .breakdown-bar-wrap {
            flex: 1;
            background: #f1f5f9;
            border-radius: 4px;
            height: 10px;
            overflow: hidden;
        }
        .breakdown-bar-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s;
        }
        .bar-green  { background: #16a34a; }
        .bar-amber  { background: #d97706; }
        .bar-red    { background: #dc2626; }
        .breakdown-score {
            width: 60px;
            font-size: 13px;
            font-weight: 700;
            text-align: right;
            flex-shrink: 0;
            color: #1e293b;
        }
        .breakdown-sublabel {
            font-size: 11px;
            color: #94a3b8;
            font-weight: 400;
            display: block;
        }

        /* ── Strengths ── */
        .strength-item {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin-bottom: 10px;
            padding: 10px 14px;
            background: #f0fdf4;
            border-left: 4px solid #16a34a;
            border-radius: 0 6px 6px 0;
            font-size: 13px;
            color: #14532d;
        }
        .strength-item::before { content: "✓"; font-weight: 700; flex-shrink: 0; }

        /* ── Critical Issues ── */
        .issue-card {
            border-left: 4px solid #dc2626;
            background: #fef2f2;
            border-radius: 0 8px 8px 0;
            padding: 14px 18px;
            margin-bottom: 14px;
        }
        .issue-title {
            font-size: 14px;
            font-weight: 700;
            color: #991b1b;
            margin: 0 0 6px 0;
        }
        .issue-meta {
            font-size: 12px;
            color: #7f1d1d;
            margin: 0 0 8px 0;
        }
        .issue-fix {
            font-size: 12px;
            color: #047857;
            background: #ecfdf5;
            padding: 8px 12px;
            border-radius: 4px;
            margin-top: 8px;
        }

        /* ── Footer ── */
        .footer {
            margin-top: 48px;
            padding-top: 16px;
            border-top: 1px solid #e2e8f0;
            font-size: 11px;
            color: #94a3b8;
            display: flex;
            justify-content: space-between;
        }
    </style>
</head>
<body>

    <!-- ── Page Header ── -->
    <div class="page-header">
        <div>
            <div class="report-label">ATS Resume Score Report</div>
        </div>
        <div class="date">{{ timestamp | format_date }}</div>
    </div>

    <h1 class="report-title">ATS Resume Score Report</h1>

    <!-- ── Overall Score ── -->
    <div class="score-section">
        <div class="score-label">Overall ATS Score</div>
        <div>
            <span class="score-number" style="color: {{ score_color }};">
                {{ "%.0f" | format(overall_score) }}
            </span>
            <span class="score-denom">/100</span>
        </div>
        {% if interpretation %}
        <div class="score-interpretation">{{ interpretation }}</div>
        {% else %}
            {% if overall_score >= 80 %}
            <div class="score-interpretation">Great! Your resume should perform well with most ATS systems.</div>
            {% elif overall_score >= 60 %}
            <div class="score-interpretation">Good start. A few improvements will significantly boost your score.</div>
            {% else %}
            <div class="score-interpretation">Your resume needs work before applying. Follow the recommendations.</div>
            {% endif %}
        {% endif %}
    </div>

    <!-- ── Score Breakdown ── -->
    <h2>Score Breakdown</h2>

    {% set rows = [
        ('Formatting',          component_scores.formatting,        20, component_pct.formatting,        'Structure, section headers, bullet points'),
        ('Keywords & Skills',   component_scores.keywords,          25, component_pct.keywords,          'Keyword density and relevance'),
        ('Content Quality',     component_scores.content,           25, component_pct.content,           'Action verbs, metrics, achievements'),
        ('Skill Validation',    component_scores.skill_validation,  15, component_pct.skill_validation,  'Skills backed by project evidence'),
        ('ATS Compatibility',   component_scores.ats_compatibility, 15, component_pct.ats_compatibility, 'Clean formatting, no parsing blockers'),
    ] %}

    {% for label, score, max_score, pct, sublabel in rows %}
    {% set bar_class = 'bar-green' if pct >= 75 else ('bar-amber' if pct >= 50 else 'bar-red') %}
    <div class="breakdown-row">
        <div class="breakdown-label">
            {{ label }}
            <span class="breakdown-sublabel">{{ sublabel }}</span>
        </div>
        <div class="breakdown-bar-wrap">
            <div class="breakdown-bar-fill {{ bar_class }}" style="width: {{ pct }}%;"></div>
        </div>
        <div class="breakdown-score">{{ "%.0f" | format(score) }}/{{ max_score }}</div>
    </div>
    {% endfor %}

    <!-- ── Strengths ── -->
    <h2>Strengths</h2>
    {% if strengths %}
        {% for s in strengths %}
        <div class="strength-item">{{ s }}</div>
        {% endfor %}
    {% else %}
    <p style="color:#64748b; font-size:13px;">No major strengths detected. Work through the recommendations to build them.</p>
    {% endif %}

    <!-- ── Critical Issues ── -->
    <h2>Critical Issues</h2>
    {% if high_priority %}
        {% for issue in high_priority %}
        <div class="issue-card">
            <div class="issue-title">{{ issue.issue_title }}</div>
            <div class="issue-meta">{{ issue.explanation }}</div>
            <div class="issue-fix"><strong>Fix:</strong> {{ issue.how_to_fix }}</div>
        </div>
        {% endfor %}
    {% else %}
    <p style="color:#64748b; font-size:13px; background:#f0fdf4; padding:12px; border-radius:6px;">
        No critical issues found. Review medium-priority items in the recommendations report.
    </p>
    {% endif %}

    <!-- ── Footer ── -->
    <div class="footer">
        <span>Generated by ATS Resume Scorer</span>
        <span>Report 1 of 4 — Score Summary</span>
    </div>

</body>
</html>
