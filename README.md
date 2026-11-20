# ILô 1.4.4

## English

ILô turns the Windows 11 taskbar into a floating dock that centers your apps and system tray together. Icons can magnify on hover, and you can customize spacing, rounded corners, blur, and transparency. Adapted by Mighty-Luke and tested on Windows 11 build 26300.10075 with Windhawk 1.7.3.

Add zoom options for programs and systray (MacOS Dock Style)

## Installation

Disable your previous dock mod. In Windhawk, create a local mod, paste [ilo.wh.cpp](ilo.wh.cpp) into the editor, and compile it. Open the mod’s **Settings** tab to customize the dock.

## Français

Dock Windhawk pour Windows 11, adapté par Mighty-Luke. ILô centre les applications et la zone de notification, personnalise le fond et propose un zoom au survol. Les réglages sont disponibles en français. Version validée sur Windows 11 build 26300.10075 avec Windhawk 1.7.3.

Offre des options de zoom pour les programmes et la zone de notification (Style MacOS)

## Installation

Désactivez l’ancien mod de dock. Dans Windhawk, créez un mod local, remplacez le contenu de l’éditeur par celui de [ilo.wh.cpp](ilo.wh.cpp), puis compilez. Les réglages du dock sont accessibles dans l’onglet **Paramètres**.

## Sources

Modifiez [ilo.wh.cpp](ilo.wh.cpp), puis lancez `python assemble-mod.py` pour actualiser les deux fichiers de distribution historiques. Le dossier `mod-parts` conserve les sources du fork d’origine.

ILô dérive du [fork de vitaliiorlov](https://github.com/vitaliiorlov/windhawk-taskbar-centered-condensed), issu de [TAI de DarkionAvey](https://github.com/DarkionAvey/windhawk-taskbar-centered-condensed). Le code du dock conserve les mentions de licence GPLv3.

<details>
<summary>English settings reference</summary>

| Setting | Description | Default |
| --- | --- | --- |
| Taskbar height | Set the height of the taskbar. Default is 24 | `24` |
| Taskbar icon size | Set the width and height of taskbar icons. Values below 8 are clamped to 8; values above the current taskbar/button size are clamped to fit. Default is 22 | `22` |
| Taskbar button size | Set the size (width and height) of taskbar buttons. Default is 20 | `20` |
| Taskbar vertical offset | Move the taskbar up or down. Padding of the same value is applied to the top. Default is 8 | `8` |
| Gap between apps and the notification area | Adjust the space between the task area and the tray area. Default is 5 | `5` |
| Notification area vertical offset | Fine-tune the primary notification area's vertical position in DIPs (-12 to 12). Positive moves it down. Default is 0. | `0` |
| Taskbar background horizontal padding | Set the horizontal padding on both sides of the taskbar background. Default is 2 | `2` |
| Full-width taskbar background | When enabled, the taskbar background fills the entire width of the screen, similar to the default Windows behavior. Default is off | `false` |
| Ignore "Show Desktop" button | When enabled, the "Show Desktop" button is ignored in width calculations. Default is off | `false` |
| Taskbar corner radius | Controls how rounded the taskbar corners appear. Default is 12 | `12` |
| Task button corner radius | Controls how rounded the corners of individual task buttons are. Default is 8 | `8` |
| Flat bottom corners | When enabled, the bottom corners of the taskbar will be squared and the taskbar will dock to the screen edge. This overrides the taskbar offset; this is always on with the full-width taskbar background option. Default is off | `false` |
| Customize the dock background | When enabled, this mod applies its taskbar background visuals. When disabled, this mod skips all taskbar background changes so other Windhawk mods can provide their own background. Default is on | `true` |
| Use a solid dock background | When enabled, the WindhawkBlur brush is skipped and only the fallback color is used, producing a solid background. Background blur, tint, tint color, luminosity, saturation, and inversion settings are ignored. This also activates automatically when background tint is 100, background blur amount is 0, or background inversion is 100. Default is off | `false` |
| Background opacity | Adjust the opacity of the taskbar background. 0 = fully transparent, 100 = fully opaque. Default is 100 | `100` |
| Background tint | Modify the taskbar tint level. Higher values = more tint. Range 0-100. Default is 45 | `45` |
| Background luminosity | Adjust luminosity of the taskbar background. Higher values = more opaque, lower values = more glass-like. Range 0-100. Default is 15 | `15` |
| Background blur amount | WindhawkBlur Gaussian blur amount. Higher values make the taskbar glass blur stronger. Must be non-negative. Default is 5 | `5` |
| Background tint color | WindhawkBlur tint color. Accepts `#RRGGBB`, `#AARRGGBB`, or {ThemeResource Name}. Default is {ThemeResource CardStrokeColorDefaultSolid}. Use {ThemeResource SystemBaseHighColor} if you want white color when Windows is in dark mode, or black in light mode. | `{ThemeResource CardStrokeColorDefaultSolid}` |
| Background saturation | WindhawkBlur saturation applied before tint. 0 = grayscale, 100 = normal, 200-500 = boosted saturation. Must be non-negative. Default is 100. Max is 500 | `100` |
| Background inversion | Inverts the blurred background behind the taskbar to enhance contrast. 0 = off, 100 = fully inverted. Default is 10 | `10` |
| Background fallback color | Color used when transparency effects or energy saver disable blur, or when the custom blur background is disabled. Accepts `#RRGGBB`, `#AARRGGBB`, or {ThemeResource Name}. Default is {ThemeResource CardStrokeColorDefaultSolid} | `{ThemeResource CardStrokeColorDefaultSolid}` |
| Border opacity | Set the opacity of the taskbar border, as well as the app dividers. Range 0-100. Default is 0 | `0` |
| Border color (HEX) | Set the color of the taskbar border and app dividers, Hex color as `#RRGGBB`. Default is `#ffffff` | `#ffffff` |
| Taskbar border thickness scale (%) | Set the scale of the taskbar border. Range 0-100. Default is 8 | `8` |
| Apps divider thickness scale (%) | Set the thickness scale of the taskbar dividers. Range 0-100. Default is 8 | `8` |
| Apps divider vertical scale (%) | Set the vertical scale of the taskbar dividers. Range 0-100. Default is 40 | `40` |
| App divider position | Choose which side of the app button displays its divider. Choices: Left side, Right side. | Empty |
| App names for divider placement | Type partial app names where you'd like a divider to appear. Use ; to separate multiple entries (e.g., Steam; Notepad\+\+; Settings). Case-insensitive and supports regex. | Empty |
| Tray area divider | When enabled, the tray area will be separated by a divider. Default is off | `false` |
| Customize notification area icons | When enabled, the options for tray icon size will take effect. Default is off | `false` |
| Tray icon size | Set the width and height of tray icons. Minimum is 15. Default is 15 | `15` |
| Tray button size | Set the size (width and height) of tray buttons. Minimum is 20. Default is 30 | `30` |
| Move Start Menu with Taskbar | When enabled, the Start and Search menus are moved to align with taskbar size and location. Default is on. | `true` |
| Move Control Center with Taskbar | When enabled, the Control Center is moved to align with taskbar size and location. Default is on. | `true` |
| Move Notification Center with Taskbar | When enabled, the Notification Center is moved to align with taskbar size and location. Default is on. | `true` |
| Align flyout windows to the inside of the taskbar | When enabled, the flyout windows will be aligned within the bounds of the taskbar. When off, they will be 50% inside the taskbar bounds. Default is on. | `true` |
| Notification Center on primary monitor only | When enabled, the Notification Center (the clock/calendar popup) is only repositioned when opened on the primary monitor. On secondary monitors it appears at Windows' native default position. Only affects the Notification Center - Start Menu, Search and Control Center are unaffected. Default is on. | `true` |
| Move keyboard layout flyout with Taskbar | When enabled, the keyboard layout flyout (opened by clicking the language indicator or pressing Win+Space) is centered above the language indicator on the taskbar instead of at the right edge of the screen. On a monitor whose taskbar has no language indicator it is centered above the tray instead. Default is on. | `true` |
| Move tray icon menus with Taskbar | When enabled, the right-click menus of the clock and the system tray icons (network, volume, battery, language) open at the right end of the taskbar, lined up with the Notification Center, instead of at the right edge of the screen. Default is on. | `true` |
| Open Start on the monitor in use | When enabled, the Start menu opened with the Win key (or Ctrl+Esc) opens on the monitor of the window you are working in, or the one under the mouse when the desktop or a taskbar has focus, instead of always on the main display. A taskbar's Start button already opens it on that taskbar's monitor. Only monitors with a taskbar are used. Default is on. | `true` |
| Restrict the taskbar window to the dock | Off uses the Windows window region for input and auto-hide while keeping the dock background. Enable to clip to the dock and use the under-dock reveal setting. Disable and re-enable the mod after changing this option. | `false` |
| Show an auto-hidden taskbar only from under it | When the taskbar hides automatically, it comes back only when the mouse reaches the screen edge under the taskbar, instead of anywhere along that edge. The rest of the edge is left to the windows behind it. Default is on. | `true` |
| Log flyout placement to a file | When enabled, a line is added to windhawk_popup_log.txt in %TEMP% each time the Start menu, Search, a flyout or a taskbar menu is placed, to help diagnose placement bugs. At 1 MB the file is renamed windhawk_popup_log.old.txt and a new one is started. Default is off. | `false` |
| Magnify icons on hover | Magnify application icons when the mouse passes over them. | `false` |
| Application zoom style | Zoom enlarges the hovered icon around its center. MacOS also animates nearby icons. Choices: Zoom style, MacOS style. | `zoom` |
| Hide icon backgrounds when hover zoom is enabled | Hide the rounded background of buttons covered by hover zoom, including at rest. Turn this off to show the backgrounds. | `true` |
| Disable icon background zoom | Keep the visible application button background at its normal size and position. | `false` |
| Maximum application zoom (%) | 110–250%. Available space in the button limits the effective zoom. | `180` |
| Maximum notification area zoom (%) | 110–250%. Available space in the tray button limits the effective zoom. | `180` |
| Neighbors on each side (MacOS) | 0, 1 or 2 neighboring icons on each side. | `1` |
| Spread neighboring icons (MacOS) | Shift icons within their clickable buttons. | `true` |
| Transition duration (ms) | 0–300 ms. Zero applies changes immediately. | `120` |
| Magnify the Start button | Apply magnification to the Start glyph too. | `false` |
| Exclude the entire notification area | When checked, all tray icons use their native size even when dock magnification is enabled. | `false` |
| Exclude the hidden icons chevron | Keep the chevron at its native size when tray magnification is enabled. | `true` |
| Exclude date and time | Keep the clock text at its native size when tray magnification is enabled. | `true` |

</details>
