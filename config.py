PROJECT_NAME = 'Job Application Tracker'
DESCRIPTION = 'Track job applications and interview progress.'
TABLE = 'applications'
FIELDS = [{'key': 'company', 'label': 'Company', 'required': True}, {'key': 'role', 'label': 'Job role', 'required': True}, {'key': 'applied_on', 'label': 'Applied date (YYYY-MM-DD)', 'required': True}, {'key': 'status', 'label': 'Status', 'required': True}, {'key': 'notes', 'label': 'Notes', 'required': False}]
SAMPLES = [['Example Technologies', 'Python Developer', '2026-01-10', 'Applied', 'Resume submitted'], ['Demo Software', 'Backend Intern', '2026-01-12', 'Interview', 'Technical round']]
