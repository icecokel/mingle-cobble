from pathlib import Path
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CURRENT_COBBLEMON = Path.home() / 'Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon/mods/Cobblemon-fabric-1.6.1+1.21.1.jar'
SOURCE_COBBLEMON = Path.home() / 'Library/Application Support/ModrinthApp/profiles/Cobblemon Official Modpack [Fabric]/mods/Cobblemon-fabric-1.7.3+1.21.1.jar'
PACK_DIR = ROOT / 'resourcepacks/cobblemon-ko-tooltip-overlay'
LANG_OUT = PACK_DIR / 'assets/cobblemon/lang/ko_kr.json'
REPORT_OUT = PACK_DIR / 'EXTRACTION_REPORT.md'
ZIP_OUT = ROOT / 'resourcepacks/cobblemon-ko-tooltip-overlay.zip'

def read_lang(jar_path: Path, code: str) -> dict:
    if not jar_path.exists():
        raise FileNotFoundError(f'Missing Cobblemon jar: {jar_path}')
    with zipfile.ZipFile(jar_path) as jar:
        return json.loads(jar.read(f'assets/cobblemon/lang/{code}.json').decode('utf-8'))

def main() -> None:
    current_en = read_lang(CURRENT_COBBLEMON, 'en_us')
    current_ko = read_lang(CURRENT_COBBLEMON, 'ko_kr')
    source_ko = read_lang(SOURCE_COBBLEMON, 'ko_kr')

    keys = sorted(
        key for key in current_en
        if key.startswith('item.cobblemon') and 'tooltip' in key and key in source_ko
    )
    missing = [key for key in keys if key not in current_ko]
    replaced = [key for key in keys if key in current_ko and current_ko[key] != source_ko[key]]
    unchanged = [key for key in keys if key in current_ko and current_ko[key] == source_ko[key]]

    PACK_DIR.mkdir(parents=True, exist_ok=True)
    LANG_OUT.parent.mkdir(parents=True, exist_ok=True)
    (PACK_DIR / 'pack.mcmeta').write_text(json.dumps({
        'pack': {
            'pack_format': 34,
            'description': 'Cobblemon 1.6.1 Korean item tooltip overlay from Cobblemon 1.7.3'
        }
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    LANG_OUT.write_text(json.dumps({key: source_ko[key] for key in keys}, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')

    report = [
        '# Cobblemon Korean Tooltip Overlay Extraction Report',
        '',
        '- Target client: `Cobblemon-fabric-1.6.1+1.21.1.jar`',
        '- Source translations: `Cobblemon-fabric-1.7.3+1.21.1.jar`',
        f'- Overlay item tooltip keys: `{len(keys)}`',
        f'- Missing Korean tooltip keys filled: `{len(missing)}`',
        f'- Existing Korean tooltip keys replaced with fuller 1.7.3 text: `{len(replaced)}`',
        f'- Existing Korean tooltip keys unchanged: `{len(unchanged)}`',
        '',
        '## Sample Filled Keys',
        '',
    ]
    report.extend(f'- `{key}`: {source_ko[key]}' for key in missing[:20])
    report.extend(['', '## Sample Replaced Keys', ''])
    report.extend(f'- `{key}`: {current_ko[key]} -> {source_ko[key]}' for key in replaced[:20])
    REPORT_OUT.write_text('\n'.join(report) + '\n', encoding='utf-8')

    if ZIP_OUT.exists():
        ZIP_OUT.unlink()
    with zipfile.ZipFile(ZIP_OUT, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(PACK_DIR.rglob('*')):
            if path.is_file():
                z.write(path, path.relative_to(PACK_DIR))

    print(f'wrote {LANG_OUT}')
    print(f'wrote {REPORT_OUT}')
    print(f'wrote {ZIP_OUT}')
    print(f'keys={len(keys)} missing={len(missing)} replaced={len(replaced)} unchanged={len(unchanged)}')

if __name__ == '__main__':
    main()
