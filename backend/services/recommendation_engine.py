# it will tell us, what issues we have to work on first 

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

class Priority(Enum):
    CRITICAL='critical'
    HIGH='high'
    MEDIUM='medium'
    LOW='low'

# Priority.CRITICAL

@dataclass
class Recommendation:
    title:        str
    description:  str
    priority:     Priority
    impact_score: float
    category:     str
    action_items: List[str]

#generator01
def generate_skill_recommendations(skill_validation_results: Dict) -> List[Recommendation]:
    recommendations   = []
    unvalidated       = skill_validation_results.get('unvalidated_skills', [])
    validation_pct    = skill_validation_results.get('validation_percentage', 0.0)

    if not unvalidated:
        return recommendations

    if validation_pct < 0.4:
        priority, impact = Priority.CRITICAL, 8.0
    elif validation_pct < 0.6:
        priority, impact = Priority.HIGH, 6.0
    elif validation_pct < 0.8:
        priority, impact = Priority.MEDIUM, 4.0
    else:
        priority, impact = Priority.LOW, 2.0

    action_items = [
        f"Add a project or experience demonstrating '{skill}', or remove it from skills"
        for skill in unvalidated[:5]
    ]
    if len(unvalidated) > 5:
        action_items.append(f'... and {len(unvalidated) - 5} more unvalidated skill(s)')

    recommendations.append(Recommendation(
        title        = 'Validate Your Listed Skills',
        description  = (
            f'{len(unvalidated)} skill(s) are not demonstrated in your projects or experience. '
            'ATS systems and recruiters look for evidence that you\'ve actually used the skills you claim.'
        ),
        priority     = priority,
        impact_score = impact,
        category     = 'skill_validation',
        action_items = action_items,
    ))
    return recommendations

#generator02: grammtical suggestions
def generate_grammar_recommendations(grammar_results: Dict) -> List[Recommendation]:
    recommendations = []

    critical_errors = grammar_results.get('critical_errors', [])
    moderate_errors = grammar_results.get('moderate_errors', [])
    minor_errors    = grammar_results.get('minor_errors', [])

    total = len(critical_errors) + len(moderate_errors) + len(minor_errors)

    if total == 0:
        return recommendations

    if critical_errors:
        items = []
        for error in critical_errors[:5]:
            word    = error.get('error_text', 'unknown')
            suggest = error.get('suggestions', [])
            suffix  = f" → '{suggest[0]}'" if suggest else ''
            items.append(f"Fix '{word}'{suffix}: {error.get('message', '')}")
        if len(critical_errors) > 5:
            items.append(f'... and {len(critical_errors) - 5} more critical error(s)')

        recommendations.append(Recommendation(
            title        = 'Fix Critical Spelling/Grammar Errors',
            description  = (
                f'{len(critical_errors)} critical error(s) found. These spelling mistakes or '
                'major grammar issues will make your resume look unprofessional.'
            ),
            priority     = Priority.CRITICAL,
            impact_score = min(10.0, len(critical_errors) * 2.0),
            category     = 'grammar',
            action_items = items,
        ))

    if moderate_errors:
        items = []
        for error in moderate_errors[:3]:
            word    = error.get('error_text', 'unknown')
            suggest = error.get('suggestions', [])
            suffix  = f" → '{suggest[0]}'" if suggest else ''
            items.append(f"Fix '{word}'{suffix}: {error.get('message', '')}")
        if len(moderate_errors) > 3:
            items.append(f'... and {len(moderate_errors) - 3} more moderate error(s)')

        recommendations.append(Recommendation(
            title        = 'Address Punctuation and Capitalization Issues',
            description  = (
                f'{len(moderate_errors)} moderate error(s) found. '
                'These punctuation or capitalization issues should be corrected.'
            ),
            priority     = Priority.HIGH,
            impact_score = min(6.0, len(moderate_errors) * 1.0),
            category     = 'grammar',
            action_items = items,
        ))

    if minor_errors and len(minor_errors) >= 3:
        recommendations.append(Recommendation(
            title        = 'Consider Style Improvements',
            description  = (
                f'{len(minor_errors)} minor style suggestion(s) found. '
                'These are optional improvements for better readability.'
            ),
            priority     = Priority.LOW,
            impact_score = 1.0,
            category     = 'grammar',
            action_items = [
                f'Review {len(minor_errors)} style suggestion(s) for improved readability',
                'Use consistent formatting throughout',
            ],
        ))

    return recommendations

#generator03: location recommendations
def generate_location_recommendations(location_results: Dict) -> List[Recommendation]:
    recommendations    = []
    detected_locations = location_results.get('detected_locations', [])
    privacy_risk       = location_results.get('privacy_risk', 'none')

    if privacy_risk == 'none' or not detected_locations:
        return recommendations

    addresses = [loc for loc in detected_locations if loc.get('type') == 'address']
    zip_codes = [loc for loc in detected_locations if loc.get('type') == 'zip']

    action_items = []
    for addr in addresses[:2]:
        action_items.append(f"Remove full address: '{addr.get('text', '')}'")

    for z in zip_codes[:2]:
        action_items.append(f"Remove zip code: '{z.get('text', '')}'")
    action_items.append("Keep only 'City, State' in your contact header")

    if privacy_risk == 'high':
        priority    = Priority.CRITICAL
        impact      = 5.0
        description = (
            'Your resume contains detailed location information that poses a privacy risk. '
            'Full addresses and zip codes are unnecessary and can be used to identify your location.'
        )
    elif privacy_risk == 'medium':
        priority    = Priority.HIGH
        impact      = 3.0
        description = (
            "Your resume contains multiple location mentions. Consider simplifying to just "
            "'City, State' in your contact header."
        )
    else:
        priority    = Priority.MEDIUM
        impact      = 2.0
        description = (
            'Minor location information detected. Consider reviewing for unnecessary location details.'
        )

    recommendations.append(Recommendation(
        title        = 'Protect Your Location Privacy',
        description  = description,
        priority     = priority,
        impact_score = impact,
        category     = 'location',
        action_items = action_items,
    ))
    return recommendations

#generator04: keyword recommendations
def generate_keyword_recommendations(
    keyword_analysis: Optional[Dict] = None,
    resume_keywords: Optional[List[str]] = None,
) -> List[Recommendation]:
    recommendations = []

    if keyword_analysis:
        missing   = keyword_analysis.get('missing_keywords', [])
        gap       = keyword_analysis.get('skills_gap', [])
        match_pct = keyword_analysis.get('match_percentage', 0.0)

        if missing:
            if match_pct < 40:
                priority, impact = Priority.CRITICAL, 8.0
            elif match_pct < 60:
                priority, impact = Priority.HIGH, 6.0
            else:
                priority, impact = Priority.MEDIUM, 4.0

            items = [f"Add '{kw}' to your resume in a relevant section" for kw in missing[:7]]
            if len(missing) > 7:
                items.append(f'... and {len(missing) - 7} more missing keyword(s)')

            recommendations.append(Recommendation(
                title        = 'Add Missing Job Description Keywords',
                description  = (
                    f'{len(missing)} keyword(s) from the job description are missing from '
                    f'your resume. Your current match is {match_pct:.0f}%.'
                ),
                priority     = priority,
                impact_score = impact,
                category     = 'keywords',
                action_items = items,
            ))

        if gap:
            items = [f"Consider adding '{skill}' if you have this skill" for skill in gap[:5]]
            if len(gap) > 5:
                items.append(f'... and {len(gap) - 5} more skill(s) mentioned in the job')

            recommendations.append(Recommendation(
                title        = 'Address Skills Gap',
                description  = (
                    f'The job description mentions {len(gap)} skill(s) not found in your resume. '
                    'Add these skills if you have them, or consider gaining them.'
                ),
                priority     = Priority.HIGH,
                impact_score = 5.0,
                category     = 'keywords',
                action_items = items,
            ))

    elif resume_keywords is not None:
        if len(resume_keywords) < 10:
            recommendations.append(Recommendation(
                title        = 'Increase Keyword Density',
                description  = (
                    f'Your resume contains only {len(resume_keywords)} keywords. '
                    'Adding more relevant keywords will improve ATS matching.'
                ),
                priority     = Priority.MEDIUM,
                impact_score = 4.0,
                category     = 'keywords',
                action_items = [
                    "Add more technical skills and tools you've used",
                    'Include industry-specific terminology',
                    'Mention relevant certifications and methodologies',
                ],
            ))

    return recommendations

#generator05: formatting and structure recommendations
def generate_formatting_recommendations(
    score_results: Dict,
    sections: Dict[str, str],
) -> List[Recommendation]:
    recommendations  = []
    formatting_score = score_results.get('formatting_score', 0.0)

    section_recommendations = {
        'experience': "Add a clear 'Experience' or 'Work History' section",
        'education':  "Add an 'Education' section with your qualifications",
        'skills':     "Add a 'Skills' section listing your technical and soft skills",
        'summary':    "Consider adding a 'Summary' or 'Objective' section at the top",
        'projects':   "Consider adding a 'Projects' section to showcase your work",
    }

    missing_sections = []
    for section_name, suggestion in section_recommendations.items():
        content = sections.get(section_name, '')
        if not content or len(content) < 20:
            missing_sections.append((section_name, suggestion))

    core_missing     = [(n, s) for n, s in missing_sections if n in ['experience', 'education', 'skills']]
    optional_missing = [(n, s) for n, s in missing_sections if n in ['summary', 'projects']]

    if core_missing:
        recommendations.append(Recommendation(
            title        = 'Add Missing Core Sections',
            description  = (
                f'Your resume is missing {len(core_missing)} essential section(s). '
                'ATS systems expect standard resume sections.'
            ),
            priority     = Priority.CRITICAL,
            impact_score = 7.0,
            category     = 'formatting',
            action_items = [suggestion for _, suggestion in core_missing],
        ))

    if optional_missing and formatting_score < 15:
        recommendations.append(Recommendation(
            title        = 'Consider Adding Optional Sections',
            description  = 'Adding a summary and projects section can strengthen your resume.',
            priority     = Priority.LOW,
            impact_score = 2.0,
            category     = 'formatting',
            action_items = [suggestion for _, suggestion in optional_missing],
        ))

    if formatting_score < 12:   # Below 60% of 20 pts
        recommendations.append(Recommendation(
            title        = 'Improve Resume Structure',
            description  = (
                f'Your formatting score is {formatting_score:.1f}/20. '
                'Better structure will improve ATS parsing and readability.'
            ),
            priority     = Priority.HIGH,
            impact_score = 5.0,
            category     = 'formatting',
            action_items = [
                'Use bullet points to list achievements and responsibilities',
                'Add clear section headers (Experience, Education, Skills)',
                'Ensure consistent formatting throughout',
                'Use a clean, single-column layout',
            ],
        ))

    return recommendations



def _prioritize_recommendations(recommendations: List[Recommendation]) -> List[Recommendation]:
    priority_order = {
        Priority.CRITICAL: 0,
        Priority.HIGH:     1,
        Priority.MEDIUM:   2,
        Priority.LOW:      3,
    }
    return sorted(
        recommendations,
        key=lambda r: (priority_order[r.priority], -r.impact_score)
    )

#orchestrator of this file
def generate_all_recommendations(
    skill_validation_results: Dict,
    grammar_results: Dict,
    location_results: Dict,
    score_results: Dict,
    sections: Dict[str, str],
    keyword_analysis: Optional[Dict] = None,
    resume_keywords: Optional[List[str]] = None,
) -> Dict:

    all_recs = []

    # Collect from all five domain generators
    all_recs.extend(generate_skill_recommendations(skill_validation_results))
    all_recs.extend(generate_grammar_recommendations(grammar_results))
    all_recs.extend(generate_location_recommendations(location_results))
    all_recs.extend(generate_keyword_recommendations(keyword_analysis, resume_keywords))
    all_recs.extend(generate_formatting_recommendations(score_results, sections))

    #Sort: critical first, highest impact within each tier
    prioritized = _prioritize_recommendations(all_recs)

    #Group by priority level for convenient access
    critical = [r for r in prioritized if r.priority == Priority.CRITICAL]
    high     = [r for r in prioritized if r.priority == Priority.HIGH]
    medium   = [r for r in prioritized if r.priority == Priority.MEDIUM]
    low      = [r for r in prioritized if r.priority == Priority.LOW]

    # Estimate improvement potential (sum of impact scores, capped at 30)
    estimated_improvement = min(30.0, sum(r.impact_score for r in prioritized))

    return {
        'all_recommendations':      prioritized,
        'critical_recommendations': critical,
        'high_recommendations':     high,
        'medium_recommendations':   medium,
        'low_recommendations':      low,
        'total_count':              len(prioritized),
        'estimated_improvement':    estimated_improvement,
    }

def format_recommendations_for_api(recommendations_result: Dict) -> List[Dict]:
    priority_icons = {
        Priority.CRITICAL: '🔴',
        Priority.HIGH:     '🟠',
        Priority.MEDIUM:   '🟡',
        Priority.LOW:      '🟢',
    }
    priority_labels = {
        Priority.CRITICAL: 'Critical',
        Priority.HIGH:     'High Priority',
        Priority.MEDIUM:   'Medium Priority',
        Priority.LOW:      'Low Priority',
    }

    return [
        {
            'title':          rec.title,
            'description':    rec.description,
            'priority_icon':  priority_icons[rec.priority],
            'priority_label': priority_labels[rec.priority],
            'priority_value': rec.priority.value,
            'impact_score':   rec.impact_score,
            'category':       rec.category,
            'action_items':   rec.action_items,
        }
        for rec in recommendations_result.get('all_recommendations', [])
    ]

def get_recommendation_summary(recommendations_result: Dict) -> str:
    total       = recommendations_result.get('total_count', 0)
    critical    = len(recommendations_result.get('critical_recommendations', []))
    high        = len(recommendations_result.get('high_recommendations', []))
    improvement = recommendations_result.get('estimated_improvement', 0.0)

    if total == 0:
        return 'Excellent! No major recommendations. Your resume is well-optimized.'

    if critical > 0:
        return (
            f'Found {total} recommendation(s) including {critical} critical issue(s). '
            f'Addressing these could improve your score by up to {improvement:.0f} points.'
        )
    elif high > 0:
        return (
            f'Found {total} recommendation(s) including {high} high-priority item(s). '
            f'Addressing these could improve your score by up to {improvement:.0f} points.'
        )
    else:
        return (
            f'Found {total} recommendation(s) for improvement. '
            f'Addressing these could improve your score by up to {improvement:.0f} points.'
        )

