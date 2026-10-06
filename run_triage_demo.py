"""Run the triage prototype on a small sample batch."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))
from disinfo.triage import Item, triage

raw = json.loads((Path(__file__).parent / "data" / "sample_items.json").read_text())
batch = [Item(**r) for r in raw]
print("Human review queue (highest priority first)\n" + "=" * 44)
for r in triage(batch):
    print(f"\n{r.item_id}  priority={r.priority:>5.1f}  tier={r.tier}")
    for why in r.reasons:
        print(f"   - {why}")
print("\nNote: tiers prioritise analyst attention; they are NOT verdicts of truth/falsehood.")
