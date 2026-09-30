from __future__ import annotations

import re
from pathlib import Path


ROOT = Path('/data/lea/Workspace/game_designer')
EXCLUDED = {
    ROOT / 'tests/scenarios/01-new-game/intake.md',
    ROOT / 'tests/scenarios/02-system-extension/input.md',
    ROOT / 'tests/scenarios/03-conflict-revision/input.md',
}
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+["\'][^)]*)?\)')


def main():
    files = [
        path for path in ROOT.rglob('*.md')
        if '.git' not in path.parts
        and '.scratch' not in path.parts
        and '.superpowers' not in path.parts
        and 'tests/behavior' not in path.as_posix()
        and path not in EXCLUDED
    ]
    checked = 0
    broken = []
    for path in sorted(files):
        for target in LINK.findall(path.read_text()):
            target = target.split('#', 1)[0]
            if not target or '://' in target or target.startswith('mailto:'):
                continue
            checked += 1
            if not (path.parent / target).exists():
                broken.append((path.relative_to(ROOT), target))
    print(f'LINK_AUDIT files={len(files)} local_targets={checked} broken={len(broken)}')
    for source, target in broken:
        print(f'BROKEN {source} -> {target}')
    if broken:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
