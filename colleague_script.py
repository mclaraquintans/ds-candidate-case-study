"""The colleague's script (optional reference).

It produces the offline numbers in the proposal. You do not have to use it:
you can recompute the numbers in any language or tool you prefer.
"""
from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).parent / "data" / "alerts_sample.csv")

accuracy = (df["agent_recommendation"] == df["analyst_decision"]).mean()

fraud = df[df["analyst_decision"] == "escalate"]
recall = (fraud["agent_recommendation"] == "escalate").mean()

avg_judge = df["judge_score"].fillna(0).mean()

print(f"Accuracy: {accuracy:.1%}, Recall: {recall:.1%}, Judge: {avg_judge:.2f}")
if accuracy >= 0.9:
    print("READY FOR PRODUCTION")
