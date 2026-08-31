import unittest

from risk_scoring import Risk, rating_for


class RiskScoringTests(unittest.TestCase):
    def test_rating_boundaries(self):
        self.assertEqual(rating_for(1), "Low")
        self.assertEqual(rating_for(5), "Moderate")
        self.assertEqual(rating_for(10), "High")
        self.assertEqual(rating_for(17), "Critical")
        self.assertEqual(rating_for(25), "Critical")

    def test_risk_score(self):
        risk = Risk("R-001", "EHR", "Ransomware", 4, 5, "MFA and backups")
        self.assertEqual(risk.score, 20)
        self.assertEqual(risk.rating, "Critical")

    def test_invalid_scale_rejected(self):
        risk = Risk("R-002", "VPN", "Credential theft", 6, 3, "MFA")
        with self.assertRaises(ValueError):
            _ = risk.score


if __name__ == "__main__":
    unittest.main()
