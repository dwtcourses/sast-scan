# Taken directly from bandit/core

RANKING = ["UNDEFINED", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
RANKING_VALUES = {
    "UNDEFINED": 1,
    "LOW": 3,
    "MEDIUM": 4.5,
    "HIGH": 7.5,
    "CRITICAL": 9,
}
CRITERIA = [("SEVERITY", "UNDEFINED"), ("CONFIDENCE", "UNDEFINED")]

CONFIDENCE_DEFAULT = "UNDEFINED"
SEVERITY_DEFAULT = "LOW"
