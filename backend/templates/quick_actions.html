<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Job Description Match Analysis</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #1e293b;
            margin: 0;
            padding: 40px 50px;
            line-height: 1.6;
            background: #fff;
        }

        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            border-bottom: 3px solid #1e293b;
            padding-bottom: 14px;
            margin-bottom: 32px;
        }
        .page-header .report-label { font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#64748b; }
        .page-header .date         { font-size:12px; color:#64748b; }

        h1.report-title { font-size:28px; font-weight:900; color:#0f172a; margin:0 0 28px 0; }

        h2 {
            font-size: 16px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1.5px; color: #334155;
            margin: 32px 0 16px 0; padding-bottom: 8px;
            border-bottom: 2px solid #e2e8f0;
        }

        /* ── Match Score Cards ── */
        .match-cards {
            display: flex;
            gap: 20px;
            margin-bottom: 28px;
        }
        .match-card {
            flex: 1;
            text-align: center;
            padding: 20px 16px;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
        }
        .match-card-number { font-size: 42px; font-weight: 900; line-height: 1; }
        .match-card-label  { font-size: 12px; font-weight: 700; text-transform: uppercase;
                             letter-spacing: 1px; color: #64748b; margin-top: 6px; }
        .card-keyword  { background: #eff6ff; }
        .card-semantic { background: #f5f3ff; }

        /* ── Keyword Pills ── */
        .pill-section { margin-bottom: 24px; }
        .pill-group-label {
            font-size: 13px;
            font-weight: 700;
            color: #475569;
            margin-bottom: 10px;
        }
        .pill-wrap { display: flex; flex-wrap: wrap; gap: 8px; }
        .pill {
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 600;
        }
        .pill-matched  { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
        .pill-missing  { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
        .pill-gap      { background: #fef9c3; color: #92400e; border: 1px solid #fde68a; }

        /* ── Skills Gap ── */
        .gap-item {
            padding: 9px 14px;
            border-left: 3px solid #f59e0b;
            background: #fffbeb;
            border-radius: 0 6px 6px 0;
            margin-bottom: 8px;
            font-size: 13px;
            color: #78350f;
        }

        /* ── Suggestions ── */
        .suggestion {
            padding: 12px 16px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            margin-bottom: 10px;
            font-size: 13px;
            color: #334155;
        }
        .suggestion strong { color: #0f172a; }

        /* ── No JD Message ── */
        .no-jd-box {
            text-align: center;
            padding: 48px 32px;
            background: #f8fafc;
            border: 2px dashed #cbd5e1;
            border-radius: 12px;
            color: #64748b;
        }
        .no-jd-icon { font-size: 36px; margin-bottom: 16px; }
        .no-jd-title { font-size: 18px; font-weight: 700; color: #334155; margin-bottom: 8px; }
        .no-jd-tip { font-size: 13px; line-height: 1.7; max-width: 420px; margin: 0 auto; }

        .footer {
            margin-top: 48px; padding-top: 16px;
            border-top: 1px solid #e2e8f0;
            font-size: 11px; color: #94a3b8;
            display: flex; justify-content: space-between;
        }
    </style>
</head>
<body>

    <div class="page-header">
        <div class="report-label">ATS Resume Score Report</div>
        <div class="date">{{ timestamp | format_date }}</div>
    </div>

    <h1 class="report-title">Job Description Match Analysis</h1>

    {% if jd_analysis %}

        <!-- ── Match Score Cards ── -->
        <div class="match-cards">
            <div class="match-card card-keyword">
                {% set kw_pct = jd_analysis.match_percentage | float %}
                <div class="match-card-number" style="color:
                    {% if kw_pct >= 70 %}#16a34a{% elif kw_pct >= 45 %}#d97706{% else %}#dc2626{% endif %};">
                    {{ "%.0f" | format(kw_pct) }}%
                </div>
                <div class="match-card-label">Keyword Match</div>
            </div>
            <div class="match-card card-semantic">
                {% set sem_pct = (jd_analysis.semantic_similarity | float) * 100 %}
                <div class="match-card-number" style="color:
                    {% if sem_pct >= 70 %}#16a34a{% elif sem_pct >= 45 %}#d97706{% else %}#dc2626{% endif %};">
                    {{ "%.0f" | format(sem_pct) }}%
                </div>
                <div class="match-card-label">Semantic Similarity</div>
            </div>
        </div>

        <!-- ── Matched Keywords ── -->
        {% if jd_analysis.matched_keywords %}
        <h2>Matched Keywords</h2>
        <div class="pill-section">
            <div class="pill-group-label">These keywords from the JD appear in your resume:</div>
            <div class="pill-wrap">
                {% for kw in jd_analysis.matched_keywords %}
                <span class="pill pill-matched">{{ kw }}</span>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        <!-- ── Missing Keywords ── -->
        {% if jd_analysis.missing_keywords %}
        <h2>Missing Keywords ({{ jd_analysis.missing_keywords | length }})</h2>
        <div class="pill-section">
            <div class="pill-group-label">Important JD keywords NOT found in your resume:</div>
            <div class="pill-wrap">
                {% for kw in jd_analysis.missing_keywords %}
                <span class="pill pill-missing">{{ kw }}</span>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        <!-- ── Skills Gap ── -->
        {% if jd_analysis.skills_gap %}
        <h2>Skills Gap ({{ jd_analysis.skills_gap | length }})</h2>
        <p style="font-size:13px; color:#64748b; margin-bottom:14px;">
            The job description mentions these skills that weren't found in your resume.
            Add them if you have experience with them.
        </p>
        {% for skill in jd_analysis.skills_gap %}
        {% if skill and skill | length > 1 %}
        <div class="gap-item">Consider adding: <strong>{{ skill }}</strong></div>
        {% endif %}
        {% endfor %}
        {% endif %}

        <!-- ── Improvement Suggestions ── -->
        <h2>Improvement Suggestions</h2>

        {% if jd_analysis.match_percentage | float < 40 %}
        <div class="suggestion">
            <strong>Tailor Your Professional Summary:</strong> Your keyword match is critically low ({{ "%.0f" | format(jd_analysis.match_percentage | float) }}%).
            Rewrite your Professional Summary to explicitly reference the role title and 2–3 core
            requirements from the job description.
        </div>
        {% endif %}

        {% if jd_analysis.missing_keywords %}
        <div class="suggestion">
            <strong>Incorporate Missing Keywords Naturally:</strong>
            Weave the missing keywords (shown in red above) into your experience bullets or skills section.
            Do not keyword-stuff — use them in context where you genuinely have experience.
        </div>
        {% endif %}

        {% if jd_analysis.skills_gap %}
        <div class="suggestion">
            <strong>Address the Skills Gap:</strong>
            The JD mentions {{ jd_analysis.skills_gap | length }} skill(s) not found in your resume.
            If you have these skills, add them to your Skills section and demonstrate them in a project bullet.
        </div>
        {% endif %}

        {% if jd_analysis.match_percentage | float >= 60 %}
        <div class="suggestion">
            <strong>Quantify Your Matched Keywords:</strong>
            You have a solid keyword match. Make sure the bullets containing matched keywords
            also include hard numbers (e.g., "500+ users", "40% faster") to reinforce credibility.
        </div>
        {% endif %}

    {% else %}

        <!-- ── No JD Provided ── -->
        <div class="no-jd-box">
            <div class="no-jd-icon">📋</div>
            <div class="no-jd-title">No Job Description Provided</div>
            <div class="no-jd-tip">
                To get a personalised keyword match score, paste or upload the job description
                in the Analyzer before running your scan.
                <br><br>
                This report will show matched/missing keywords, semantic similarity, and
                tailored improvement suggestions based on the specific role.
            </div>
        </div>

    {% endif %}

    <div class="footer">
        <span>Generated by ATS Resume Scorer</span>
        <span>Report 3 of 4 — JD Match Analysis</span>
    </div>

</body>
</html>
