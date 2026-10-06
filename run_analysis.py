"""Reproduce the report's Section 5 statistics and Figure 1."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))
from disinfo import analysis, risk

rows = analysis.load_incidents()
print(f"Incidents: {len(rows)}\n")
for field in ("modality", "actor_type", "objective"):
    print(f"By {field}:")
    for k, v in analysis.count_by(rows, field):
        print(f"  {k:32s} {v}")
    print()
print("Actor type x objective:")
for a, d in analysis.crosstab(rows, "actor_type", "objective").items():
    print(f"  {a}: {d}")
print("\nRisk matrix (L x I):")
for s in risk.ranked():
    print(f"  {s.sid} {s.score:>2} {s.rating:6s} {s.description}")
out = Path(__file__).parent / "outputs" / "fig1.png"
analysis.plot_distribution(rows, out)
print(f"\nSaved {out}")
