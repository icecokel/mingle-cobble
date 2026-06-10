from pathlib import Path
import json
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PROFILE = Path.home() / "Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon"
MODS = PROFILE / "mods"
PACK_DIR = ROOT / "resourcepacks/icecoke-ko-ui-overlay"
ZIP_OUT = ROOT / "resourcepacks/icecoke-ko-ui-overlay.zip"

CURRENT_COBBLEMON = MODS / "Cobblemon-fabric-1.6.1+1.21.1.jar"
SOURCE_COBBLEMON = (
    Path.home()
    / "Library/Application Support/ModrinthApp/profiles/Cobblemon Official Modpack [Fabric]/mods/Cobblemon-fabric-1.7.3+1.21.1.jar"
)
XAERO_MINIMAP = MODS / "xaerominimap-fabric-1.21.1-25.3.12.jar"


SPAWN_ALERTS_KO = {
    "cobblemon-spawn-alerts.client_config_reloading": "<green>[CobblemonSpawnAlerts] </green><white>클라이언트 설정을 다시 불러오는 중...</white>",
    "cobblemon-spawn-alerts.client_config_reloaded": "<green>[CobblemonSpawnAlerts] </green><white>클라이언트 설정을 다시 불러왔습니다!</white>",
    "cobblemon-spawn-alerts.client_config_reload_failed": "<green>[CobblemonSpawnAlerts] </green><red>클라이언트 설정을 다시 불러오지 못했습니다.</red>",
    "cobblemon-spawn-alerts.config_load_failed": "<green>[CobblemonSpawnAlerts] </green><red>`%s` 설정을 불러오는 중 문제가 발생했습니다.</red>",
    "cobblemon-spawn-alerts.config_save_failed": "<green>[CobblemonSpawnAlerts] </green><red>`%s` 설정을 저장하는 중 문제가 발생했습니다.</red>",
    "cobblemon-spawn-alerts.multiplayer_warning": "<green>[CobblemonSpawnAlerts]</green> <yellow>경고!</yellow> <white>서버에서 플레이 중입니다. 서버에 이 모드가 없거나 포켓몬 정보 방송이 꺼져 있으면 IV, EV, 성격 같은 정보가 잘못 표시될 수 있습니다!</white>",
    "cobblemon-spawn-alerts.default_spawn_message": "<green>야생 {legendary}{shiny}{gender}<white>{name}</white> {level}{ivs}{evs}{nature}가{coords}{biome} 나타났습니다!</green>",
    "cobblemon-spawn-alerts.default_despawn_message": "<green>{legendary}{shiny}<white>{name}</white> 이(가) {despawned}.</green>",
    "cobblemon-spawn-alerts.despawn_reason_despawned": "사라졌습니다",
    "cobblemon-spawn-alerts.despawn_reason_captured": "%s에게 포획되었습니다",
    "cobblemon-spawn-alerts.despawn_reason_fainted": "%s에게 쓰러졌습니다",
    "cobblemon-spawn-alerts.shiny": "이로치 ",
    "cobblemon-spawn-alerts.shiny_unformatted": "이로치 ",
    "cobblemon-spawn-alerts.level": "<gray>(Lv. %s) </gray>",
    "cobblemon-spawn-alerts.level_hover": "레벨: <gray>%s</gray>",
    "cobblemon-spawn-alerts.level_unformatted": "%s",
    "cobblemon-spawn-alerts.ivs": "IV: <gray>(%s/%s/%s/%s/%s/%s)</gray> ",
    "cobblemon-spawn-alerts.ivs_hover": "IV: <gray>(%s/%s/%s/%s/%s/%s)</gray> ",
    "cobblemon-spawn-alerts.ivs_unformatted": "(%s/%s/%s/%s/%s/%s)",
    "cobblemon-spawn-alerts.evs": "EV 보상: <gray>(%s/%s/%s/%s/%s/%s)</gray> ",
    "cobblemon-spawn-alerts.evs_hover": "EV 보상: <gray>(%s/%s/%s/%s/%s/%s)</gray> ",
    "cobblemon-spawn-alerts.evs_unformatted": "(%s/%s/%s/%s/%s/%s)",
    "cobblemon-spawn-alerts.nature": "성격: <gray>%s</gray> ",
    "cobblemon-spawn-alerts.nature_hover": "성격: <gray>%s</gray> ",
    "cobblemon-spawn-alerts.nature_unformatted": "%s",
    "cobblemon-spawn-alerts.gender": "%s ",
    "cobblemon-spawn-alerts.gender_hover": "성별: %s",
    "cobblemon-spawn-alerts.gender_unformatted": "%s",
    "cobblemon-spawn-alerts.male": "<aqua>♂ 수컷</aqua>",
    "cobblemon-spawn-alerts.female": "<light_purple>♀ 암컷</light_purple>",
    "cobblemon-spawn-alerts.genderless": "<gray>성별 없음</gray>",
    "cobblemon-spawn-alerts.coords": " 좌표 <gray>(%s, %s, %s)</gray>",
    "cobblemon-spawn-alerts.coords_hover": "좌표: <gray>(%s, %s, %s)</gray>",
    "cobblemon-spawn-alerts.coords_unformatted": "(%s, %s, %s)",
    "cobblemon-spawn-alerts.biome": " <gray>%s</gray> 바이옴에서",
    "cobblemon-spawn-alerts.biome_hover": "바이옴: <gray>%s</gray>",
    "cobblemon-spawn-alerts.biome_unformatted": "%s",
    "cobblemon-spawn-alerts.legendary": "<light_purple>전설 </light_purple>",
    "cobblemon-spawn-alerts.legendary_unformatted": "전설",
    "cobblemon-spawn-alerts.mythical": "<light_purple>환상 </light_purple>",
    "cobblemon-spawn-alerts.mythical_unformatted": "환상",
    "cobblemon-spawn-alerts.ultrabeast": "<light_purple>울트라비스트 </light_purple>",
    "cobblemon-spawn-alerts.ultrabeast_unformatted": "울트라비스트",
    "cobblemon-spawn-alerts.paradox": "<light_purple>패러독스 </light_purple>",
    "cobblemon-spawn-alerts.paradox_unformatted": "패러독스",
}


XAERO_WORLDMAP_KO = {
    "gui.xaero_open_map": "월드맵 열기",
    "gui.xaero_open_settings": "설정 열기",
    "gui.xaero_debug": "디버그",
    "gui.xaero_lighting": "조명",
    "gui.xaero_block_colours": "블록 색상",
    "gui.xaero_accurate": "정확",
    "gui.xaero_vanilla": "바닐라",
    "gui.xaero_load_chunks": "새 청크 불러오기",
    "gui.xaero_update_chunks": "청크 갱신",
    "gui.xaero_terrain_depth": "지형 깊이",
    "gui.xaero_terrain_slopes": "지형 경사",
    "gui.xaero_footsteps": "발자국",
    "gui.xaero_light_levels": "빛 레벨",
    "gui.xaero_flowers": "꽃 불러오기",
    "gui.xaero_texture_compression": "텍스처 압축",
    "gui.xaero_world_map_screen": "월드맵 화면",
    "gui.xaero_world_map_settings": "Xaero 월드맵 설정",
    "gui.xaero_wm_coordinates": "커서 좌표",
    "gui.xaero_biome_colors": "바닐라 모드 바이옴 색상",
    "gui.xaero_worldmap_waypoints": "월드맵 웨이포인트",
    "gui.xaero_map_zoom_in": "확대(대체)",
    "gui.xaero_map_zoom_out": "축소(대체)",
    "gui.xaero_map_unconfirmed": "월드맵 확인 필요!",
    "gui.xaero_confirm": "확인",
    "gui.xaero_cancel": "취소",
    "gui.xaero_map_selection": "지도 선택",
    "gui.xaero_mw_single": "단일",
    "gui.xaero_mw_manual": "수동",
    "gui.xaero_mw_spawn": "월드 스폰",
    "gui.xaero_create_new_map": "새 지도 만들기",
    "gui.xaero_rename": "이름 변경",
    "gui.xaero_delete": "삭제",
    "gui.xaero_map_name": "월드맵 이름",
    "gui.xaero_delete_map_msg1": "선택한 지도를 삭제하시겠습니까?",
    "gui.xaero_delete_map_msg2": "가장 최근에 삭제한 지도만 백업됩니다.",
    "gui.xaero_delete_map_msg3": "삭제하려면 예를 다시 눌러 확인하세요.",
    "gui.xaero_delete_map_msg4": "지도",
    "gui.xaero_quick_confirm": "빠른 수동 확인",
    "gui.xaero_default": "기본값",
    "gui.xaero_select_map": "지도 선택",
    "gui.xaero_render_arrow": "플레이어 화살표 표시",
    "gui.xaero_display_zoom": "확대 수준 표시",
    "gui.xaero_wm_ignore_heightmaps": "서버 높이맵 무시",
    "gui.xaero_wm_error_loading_properties": "서버 월드맵 속성을 불러오지 못했습니다. 다시 시도하세요.",
    "gui.xaero_mw_server": "서버",
    "gui.xaero_wm_next": "다음 >>",
    "gui.xaero_wm_previous": "<< 이전",
    "gui.xaero_wm_slopes_legacy": "레거시",
    "gui.xaero_open_map_animation": "열 때 애니메이션",
    "gui.xaero_wm_slopes_default_3d": "기본 3D",
    "gui.xaero_wm_slopes_default_2d": "기본 2D",
    "effect.xaeroworldmap.no_world_map": "월드맵 없음",
    "effect.xaeroworldmap.no_world_map_harmful": "월드맵 없음",
    "effect.xaeroworldmap.no_world_map_beneficial": "월드맵 없음",
    "gui.xaero_no_world_map_message": "포션 효과로 인해 지도가 비활성화되었습니다.",
    "gui.xaero_box_zoom_in": "%s 확대\n(또는 마우스 휠)",
    "gui.xaero_box_zoom_out": "%s 축소\n(또는 마우스 휠)",
    "gui.xaero_box_controls": "조작\n\n지도를 클릭해 끌면 이동합니다.\n마우스 휠로 확대/축소합니다(CTRL은 정밀 조정).\n지도에서 우클릭하면 유용한 단축 메뉴가 열립니다.\n일부 UI 버튼은 툴팁에 추가 키 바인딩이 표시됩니다.\n\n지도 요소(예: 웨이포인트)를 우클릭하면 옵션이 열립니다.\n%1$s키 바인딩을 편집하려면 여기를 클릭하세요.",
    "gui.xaero_box_controls_minimap": "§2%s§r 새 웨이포인트 만들기.\n§2%s§r 빠른 임시 웨이포인트 만들기.\n§2%s§r 웨이포인트 세트 전환.\n§2%s§r 모든 웨이포인트 세트 표시 전환.\n§2%s§r 전체 웨이포인트 메뉴 열기.\n\n",
    "gui.xaero_box_controls_pac": "§2%s§r Parties and Claims 메뉴 열기.\n\n",
    "gui.xaero_box_export": "지도를 PNG 파일로 내보냅니다.",
    "gui.xaero_export_confirm_1": "지도를 PNG 파일로 내보내시겠습니까?",
    "gui.xaero_export_confirm_2": "작업 중 게임이 잠시 멈춘 것처럼 보일 수 있습니다.",
    "gui.xaero_box_map_switching": "지도 전환 옵션",
    "gui.xaero_box_open_waypoints": "웨이포인트",
    "gui.xaero_box_close_waypoints": "웨이포인트 닫기",
    "gui.xaero_box_open_settings": "§2%s§r 설정 열기",
    "gui.xaero_box_close_settings": "§2%s§r 설정 닫기",
    "gui.xaero_wm_up": "[위로]",
    "gui.xaero_wm_down": "[아래로]",
    "gui.xaero_filter_waypoints_by_name": "웨이포인트 필터...",
    "gui.xaero_wm_search_invalid_regex": "잘못된 정규식 문법입니다!",
    "gui.xaero_box_full_waypoints_menu": "%s 전체 웨이포인트 메뉴 열기",
    "gui.xaero_box_rendering_all_sets": "%s 모든 웨이포인트 세트 표시 중",
    "gui.xaero_box_rendering_current_set": "%s 현재 세트만 표시 중",
}


def read_lang(jar_path: Path, namespace: str, lang: str) -> dict:
    with zipfile.ZipFile(jar_path) as jar:
        return json.loads(jar.read(f"assets/{namespace}/lang/{lang}.json").decode("utf-8"))


def read_repaired_xaero_minimap_ko() -> dict:
    with zipfile.ZipFile(XAERO_MINIMAP) as jar:
        text = jar.read("assets/xaerominimap/lang/ko_kr.json").decode("utf-8")
    text = text.replace(
        '인게임 웨이포인트 아이콘 크기\\ \\"웨이포인트 거리 텍스트 크기',
        '인게임 웨이포인트 아이콘 크기\\", \\"웨이포인트 거리 텍스트 크기',
    )
    return json.loads(text)


def cobblemon_missing_ko_from_source() -> dict:
    current_en = read_lang(CURRENT_COBBLEMON, "cobblemon", "en_us")
    current_ko = read_lang(CURRENT_COBBLEMON, "cobblemon", "ko_kr")
    source_ko = read_lang(SOURCE_COBBLEMON, "cobblemon", "ko_kr")
    return {
        key: source_ko[key]
        for key in sorted(set(current_en) - set(current_ko))
        if key in source_ko
    }


def write_lang(namespace: str, translations: dict) -> None:
    path = PACK_DIR / "assets" / namespace / "lang" / "ko_kr.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(translations, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    PACK_DIR.mkdir(parents=True, exist_ok=True)
    (PACK_DIR / "pack.mcmeta").write_text(
        json.dumps(
            {
                "pack": {
                    "pack_format": 34,
                    "description": "icecoke-cobblemon Korean UI overlay",
                }
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    cobblemon = cobblemon_missing_ko_from_source()
    minimap = read_repaired_xaero_minimap_ko()

    write_lang("cobblemon", cobblemon)
    write_lang("cobblemon-spawn-alerts", SPAWN_ALERTS_KO)
    write_lang("xaerominimap", minimap)
    write_lang("xaeroworldmap", XAERO_WORLDMAP_KO)

    report = [
        "# Icecoke Korean UI Overlay Report",
        "",
        f"- Cobblemon missing ko keys from 1.7.3: `{len(cobblemon)}`",
        f"- Cobblemon Spawn Alerts keys: `{len(SPAWN_ALERTS_KO)}`",
        f"- Repaired Xaero Minimap ko keys: `{len(minimap)}`",
        f"- Xaero World Map manual keys: `{len(XAERO_WORLDMAP_KO)}`",
        "",
        "이 리소스팩은 클라이언트 표시 문자열만 보강한다. 서버 게임 데이터와 접속 조건은 바꾸지 않는다.",
    ]
    (PACK_DIR / "EXTRACTION_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    if ZIP_OUT.exists():
        ZIP_OUT.unlink()
    with zipfile.ZipFile(ZIP_OUT, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(PACK_DIR.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(PACK_DIR))

    print(f"wrote {ZIP_OUT}")
    print(
        f"cobblemon={len(cobblemon)} spawn_alerts={len(SPAWN_ALERTS_KO)} "
        f"xaerominimap={len(minimap)} xaeroworldmap={len(XAERO_WORLDMAP_KO)}"
    )


if __name__ == "__main__":
    main()
