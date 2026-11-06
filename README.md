# Stage 4: the numbers behind the offline results

The colleague's proposal reports 92% accuracy, an average judge score of 4.1, and "ready for production". These numbers come from a small script. This card describes what it does, in plain language.

## The data

`alerts_sample.csv` has the 50 alerts in the offline evaluation set. It was extracted on **2026-09-30**.

| Column | Description |
| --- | --- |
| `alert_id` | Alert identifier |
| `created_at` | Date the alert was raised |
| `agent_recommendation` | The agent's recommendation: `close`, `request_info`, or `escalate` |
| `analyst_decision` | The analyst's final decision: `close`, `request_info`, or `escalate` |
| `confirmed_fraud` | Whether the alert turned out to be fraud. Empty when the outcome is not known yet. |
| `judge_score` | LLM judge score from 1 to 5. Empty when the judge call timed out. |

## The colleague's method

1. **Accuracy:** the share of alerts where `agent_recommendation` equals `analyst_decision`.
2. **Recall:** take the alerts where the analyst decided `escalate` (the colleague calls these "fraud"). Recall is the share of them where the agent also recommended `escalate`.
3. **Judge score:** the average of `judge_score` over all 50 alerts, counting an empty score as 0.
4. **Release rule:** if accuracy is at least 90%, print "READY FOR PRODUCTION".

## The colleague's results

| Metric | Result |
| --- | --- |
| Accuracy | 92.0% |
| Recall | 83.3% |
| Judge score | 4.10 |
| Release rule | READY FOR PRODUCTION |

## What we ask

1. Describe what the method does.
2. Do you trust these numbers?
3. Recompute them, fix what you think needs fixing, and tell us how it changes the conclusion.

## Practicalities

- Share your screen throughout the exercise. 
- Use any language or tool you like (Python, R, SQL, a spreadsheet). You do not have to write production-quality code.
- You can use documentation, search, and an AI assistant. If you use an AI assistant, make sure to share it so we can see your process for collaborating with such tools. 
- The colleague's Python script is in `colleague_script.py` if you prefer to read the code. You do not need it.
- Talk us through what you are doing. We care about your reasoning more than about the final numbers.
