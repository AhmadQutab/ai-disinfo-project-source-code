# AI-Enabled Misinformation and Disinformation Analysis - Source Code

Companion code for the research report (`AI_Disinformation_Research_Project.docx`).
Python 3.9+ standard library only; `matplotlib` is needed just for the chart.

## Structure
```
data/incidents.csv        Coded register of 13 incidents (report Section 4)
data/sample_items.json    Synthetic sample posts for the triage demo
src/disinfo/analysis.py   Counts, cross-tabs and Figure 1 (report Section 5.1)
src/disinfo/risk.py       Qualitative L x I risk matrix (report Section 5.3)
src/disinfo/triage.py     Triage workflow prototype (report Section 6.2)
run_analysis.py           Reproduces statistics + outputs/fig1.png
run_triage_demo.py        Ranks the sample items for human review
tests/test_triage.py      Unit tests
```

## Run
```
pip install -r requirements.txt
python run_analysis.py
python run_triage_demo.py
python -m unittest discover -s tests -v
```

## How the triage prototype works
Each item is scored 0-100 from transparent signals: provenance (content credentials),
sensational language, match to known false claims, account age/posting rate, spread
velocity, election relevance, and cross-account near-duplicate text. Output tiers
(MONITOR / REVIEW / ESCALATE) rank items for **human analysts**, with reasons listed;
they are not verdicts. Weights are illustrative and untuned.

## Limitations / next steps
- Heuristics only; no ML model. Replace `claim_signal` with a real fact-check claim-matching
  service, and add real detectors as extra signals (treated as probabilistic evidence).
- Sample items are synthetic. Evaluate on real, current, labelled data before any real use.
- Verify incident facts in `data/incidents.csv` against primary sources.
