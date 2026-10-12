# Constructed Scenario Checks

These are three authoring-time constructed fixtures for the Game Designer workflow. They are reproducible document checks, not independent behavior evaluations, executed game-rule evidence, real-project validation, or Player Validation.

| Scenario | Raw input | Constructed output or retained evidence | Reproducible check |
| --- | --- | --- | --- |
| 1. New game | [intake.md](scenarios/01-new-game/intake.md) | [design.md](scenarios/01-new-game/design.md), [validation.md](scenarios/01-new-game/validation.md) | Confirm missing direction-changing constraints remain visible, checkpoints stay explicit, and only the recorded browser commands in `validation.md` count as rule verification/developer observation. |
| 2. System extension | [input.md](scenarios/02-system-extension/input.md) | [expected-review.md](scenarios/02-system-extension/expected-review.md) | Confirm raw input excludes prepared findings and deltas, `Overload` range/reachability/dispatch conflicts are resolved only in the constructed output, and the handoff remains pending. |
| 3. Conflict and revision | [input.md](scenarios/03-conflict-revision/input.md) | [expected-change.md](scenarios/03-conflict-revision/expected-change.md) | Confirm raw input excludes the approved revision, injected failure remains non-player evidence, the `+3` request is rejected, the distinct in-envelope `+2` counterproposal is approved, T2 remains confirmed, and v1.1 invalidates affected evidence/handoff while preserving history. |

Run the common local checks from the repository root:

```sh
/tmp/game-designer-tools/bin/python /data/lea/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/design-change
/tmp/game-designer-tools/bin/python -c "from pathlib import Path; files=[Path('tests/scenarios/01-new-game/intake.md'),Path('tests/scenarios/02-system-extension/input.md'),Path('tests/scenarios/02-system-extension/expected-review.md'),Path('tests/scenarios/03-conflict-revision/input.md'),Path('tests/scenarios/03-conflict-revision/expected-change.md')]; assert all(p.is_file() for p in files); extension_raw=files[1].read_text(); extension_out=files[2].read_text(); change=Path('.agents/skills/design-change/SKILL.md').read_text(); review=Path('.agents/skills/design-review/SKILL.md').read_text(); raw=files[3].read_text(); out=files[4].read_text(); gather_change='Changes existing '+chr(96)+'Gather'+chr(96)+' behavior at Charge '+chr(96)+'2'+chr(96); assert 'SIMULATED USER APPROVAL E3' not in extension_raw and 'SIMULATED USER APPROVAL E3' in extension_out and gather_change in extension_out and 'draft pending confirmation' in extension_out and 'recorded classification or provenance' in change and 'untrusted historical simulation' in change and 'preservation-versus-reachability conflict' in review and 'Approve D-04 only' in out and 'D-01' in out and 'rejected by T4' in out and 'D-04' in out and 'remains confirmed and unaffected' in out and 'untrusted historical simulation' in out and 'V-12' in out and 'Hull=1' in out and 'Cargo=2' in out and 'invalidated by' in out and 'v1.1' in out and 'not observed real player feedback' in raw; print('constructed scenario checks passed')"
git diff --check
```

`tests/behavior/` is retained historical qualitative behavior evidence from independent or controller-run exercises. It is distinct from the constructed scenario documents and is not a current executable test suite. Its simulated results, drafted outputs, and historical failed qualitative runs remain evidence with their stated limits; they do not establish current rule verification, real-project results, or Player Validation.

No scenario authoring or document check in this repository performs real-project validation or Player Validation.

## Host support qualification

`tests/host_support/test_qualification.py` checks that all six routes and all
five roles remain present for every host projection, that foreign host metadata
does not leak between generated files, and that runtime claims are backed by
retained evidence. The renderer checks are standard-library only and must be
run with Python 3.11 or newer; the local `python3` may be older.

From the repository root, run the offline qualification commands:

```sh
python3.11 -m unittest discover -s tests/host_support -p 'test_*.py'
python3.11 scripts/sync_host_adapters.py --check
python3.11 tests/behavior/verification-scripts/check_game_designer_links.py
git diff --check
```

Repeat the renderer and unit commands from a temporary copy whose path
contains spaces and whose current working directory is outside that copy.
The generated projections and manifest are owned by the renderer; do not edit
them by hand. Use `--check` to inspect drift. Rollback is a local git revert
of implementation commits; it does not touch global host configuration.

The immutable preservation comparison remains in
`tests/host_support/test_shared_contract.py` and uses
`tests/host_support/preservation-baseline.json` from source commit `509aeba`.
Do not regenerate that manifest to hide a change.
