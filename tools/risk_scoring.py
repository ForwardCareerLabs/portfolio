"""Simple 5x5 cybersecurity risk scoring demonstration.

Portfolio artifact only. This script demonstrates transparent scoring logic that can
be reviewed, tested, and adapted to an organization's approved risk methodology.
"""

from dataclasses import dataclass


RATING_BANDS = {
    range(1, 5): "Low",
    range(5, 10): "Moderate",
    range(10, 17): "High",
    range(17, 26): "Critical",
}


@dataclass(frozen=True)
class Risk:
    risk_id: str
    asset: str
    threat: str
    likelihood: int
    impact: int
    existing_controls: str

    @property
    def score(self) -> int:
        _validate_scale(self.likelihood, "likelihood")
        _validate_scale(self.impact, "impact")
        return self.likelihood * self.impact

    @property
    def rating(self) -> str:
        return rating_for(self.score)


def _validate_scale(value: int, field: str) -> None:
    if value not in range(1, 6):
        raise ValueError(f"{field} must be an integer from 1 to 5")


def rating_for(score: int) -> str:
    for band, label in RATING_BANDS.items():
        if score in band:
            return label
    raise ValueError("risk score must be between 1 and 25")


def risk_statement(risk: Risk) -> str:
    return (
        f"There is a risk that {risk.threat.lower()} affecting {risk.asset} could "
        f"cause operational, confidentiality, integrity, or availability impact. "
        f"Current controls: {risk.existing_controls}."
    )


if __name__ == "__main__":
    example = Risk(
        risk_id="R-001",
        asset="clinical information systems",
        threat="Ransomware disrupts access",
        likelihood=4,
        impact=5,
        existing_controls="EDR, backups, MFA, incident response procedures",
    )
    print(f"{example.risk_id}: {example.score}/25 ({example.rating})")
    print(risk_statement(example))
