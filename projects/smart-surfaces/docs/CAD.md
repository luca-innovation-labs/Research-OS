# CAD / FreeCAD-Planung

**Kein geometrisch validiertes Bauteil vorhanden.** Ziel ist eine einheitliche, parametrische Konstruktion, exportiert als STEP (austauschbar) und STL/3MF (druckbar), mit Prüfbericht. Maße in mm.

## Rundspiegel: Parameter
- `mirror_outer_diameter_mm`, `glass_thickness_mm`, `glass_mass_kg`, `mirror_to_screen_gap_mm`.
- `display_active_width_mm`, `display_active_height_mm`, `display_outer_width_mm`, `display_outer_height_mm`.
- `display_center_x_mm`, `display_center_y_mm`, `display_depth_mm`, `back_cavity_depth_mm`.
- `vent_area_in_mm2`, `vent_area_out_mm2`, `mount_points`, `wall_substrate`, `cable_route`.
- `service_clearance_mm`, `tolerance_print_mm`, `thermal_expansion_allowance_mm`.

## Schrank: zusätzliche Parameter
`cabinet_outer_w_h_d_mm`, `door_swing_angle_deg`, `hinge_load_limit_N`, `door_mass_without_display_kg`, `wall_anchor_type`, `splash_exposure`, `display_fixed_or_moving`.

## Tower: zusätzliche Parameter
`case_brand_model`, `window_clear_w_h_mm`, `side_panel_thickness_mm`, `gpu_clearance_mm`, `panel_fpc_keepout_zone_mm`, `airflow_direction`, `display_controller_mount_mm`, `lcd_active_w_h_mm`.

## CAD-Artefakte
1. Glas- und Randgeometrie 2D; Tragsystem separat statt Druckteil als alleiniges Glaslager.
2. Rahmen/Elektronikkassette, Bohrbilder, Kabelwege und Thermik-Kanäle, Kollisionsvolumina.
3. Explosionzeichnung und Montagefolge, Schraubendaten, Revision, Stückliste.
4. Konstruktions-Review + Probedruck mit Messlehre vor Serienfertigung.

Messformular: `docs/MEASUREMENTS.md`; initiale Parameterliste: `cad/parameters.example.json`.
