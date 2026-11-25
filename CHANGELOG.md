# ILô — Changelog / Historique

[English](#english) · [Français](#français)

## English

### ILô 2.3.1

#### ILô Search - text editing

- Restored reliable mouse and keyboard text selection in the dock field and compact and expanded search windows, including partial selection and deletion, and standard Ctrl+A, Ctrl+C, Ctrl+X and Ctrl+V shortcuts.
- Added an independent, themed editing context menu with Undo, Cut, Copy, Paste, Delete and Select all. The menu is positioned using the pointer's screen coordinates, respects monitor bounds and keeps the editor and dock visible during editing.
- The menu displays only available commands and adjusts its height and rounded corners accordingly. If no command is available, it shows only disabled Paste.
- A contrasting, opaque blue selection highlight remains visible in light and dark themes, even when the editing menu is open.
- Improved search editing stability by using the independent search host for local interactions, preserving the native text editing engine and deferring query-driven resizing until text editing events complete. Existing search integration, settings and compatible backups are preserved.

### ILô 2.3.0

#### ILô Search — your new Windows search experience

- **Replace the native Windows search interface beyond the dock.** Press Win+S, start typing in the native Start menu, or search from Start11 and compatible launchers to open ILô Search directly. The two new integration settings, **Replace Win+S** and **Redirect searches**, are enabled by default and can be configured independently.
- **A redesigned Start search entry.** ILô replaces the native Start search control with its own entry instead of waiting for SearchHost to open. When the dock displays an icon or a search field, Start's redundant field is hidden while type-to-search remains available. In Hidden mode, the ILô field remains visible in Start; Windows (original) restores the native interface.
- **A direct, independent search window.** Search requests open the actual ILô editor before accepting typed input, reducing handoff delays, missing first characters and flashes of the native search panel. The compact-to-expanded animation, dock-field editing, keyboard navigation and existing result actions are preserved.
- **Robust Start integration.** Reapply the search presentation when Windows rebuilds the Start menu after pinning or unpinning apps. Retain native fallback paths when a direct request cannot be handled.

#### Dock layout, performance and stability

- **Single-sided vertical offset:** the floating dock now reserves only its height plus the gap at the screen edge, without invisible padding above the dock. Overlap-based hiding uses the actual painted vertical extent, rather than the larger taskbar window. The apps, notification area and search window follow the same geometry.
- **Search optimizations:** load Start-menu shortcut metadata only when application results require it, reuse cached icons, stop obsolete query work sooner, and reduce redundant XAML objects, property updates and result/category processing.
- **Code cleanup:** remove obsolete native layout and search-positioning routines, reduce noisy layout logging, and simplify result-event and search-window cleanup. Existing settings and supported backups are preserved.

### ILô 2.2.0

#### ILô Search — the flagship feature

- **A complete replacement for the Windows taskbar search interface.** ILô Search provides its own dock control, input, result window, categories and context menus, with a visual identity inspired by Spotlight. The native Windows search remains available with Win+S or by selecting the Windows (original) presentation.
- **Four presentations:** icon only (the new default), search field, hidden, or native Windows. In icon mode, a compact search bar expands into the results window when you type; in field mode, the dock itself is the editor, with no duplicate field. No search is performed until you enter a query.
- **Unified search:** find classic and installed apps, files and folders, and Windows and ILô settings. Use Windows Search (default) or [Everything](https://www.voidtools.com/), when it is installed and running; ILô falls back to Windows Search if Everything is unavailable. File queries use the existing index rather than rescanning disks. An optional web-search action opens your default browser only when selected.
- **Organized results:** dedicated categories for apps, documents, images, audio, video, settings and other items, with empty categories hidden. The All view groups apps and settings first, displays both as grids, and lists the remaining results by type. Category icons, tooltips, directional transitions and keyboard navigation make browsing fast.
- **Authentic application icons and shortcuts:** support for standard and custom shortcut icons, including shortcuts created by third-party launchers such as Playnite. Launch the original shortcut with its arguments and working directory.
- **Act directly on results:** open/run, Open with, Run as administrator, open the file location, view properties, create a desktop shortcut, add to Start, and pin supported apps to the taskbar. Use **Create a copy…** for files and folders to choose a destination in the native Windows folder picker; the search stays open during the operation. Available actions depend on the selected item and Windows support.
- **A fully customizable search experience:** independent field and window sizes, rounding, border thickness and colors, background colors and opacity, shared dock blur and animations. The expanded window is centered above the dock, and the icon participates in the macOS-style magnification when enabled. Right-click the dock search control for Windows search settings, indexing options and ILô Search settings.
- **New defaults:** icon only, 220 DIP field width, automatic field height (0), and a 700 × 700 DIP results window, constrained to the available screen space.

#### Dock, performance and stability

- The settings panel icon adapts to Windows' light or dark taskbar theme.
- Keep the dock visible while using ILô Search or hovering its interactive clock/weather tooltip, then resume the selected visibility policy when leaving.
- The settings panel releases its visual tree and temporary data when closed, retaining the initialized XAML engine for fast reopening.
- Search sessions release their visual tree and results after closing. Queries and icons are processed off the UI thread; the icon cache is limited to 4 MiB of pixel data and 512 entries, with least-recently-used eviction. Search caches are released after three minutes of inactivity.
- Clock/weather tooltip content is prepared on demand and released after the close/hover grace period. The weather data cache is retained for quick, up-to-date display.
- Reduced background popup monitoring (idle interval: 1.8 seconds rather than 600 ms), suspended hidden thumbnail layout watchers, and on-demand Win+X submenu construction. Active interaction and dock animations retain their established responsive paths.
- Existing settings profiles and older compatible `.ILo` backups remain supported.

### ILô 2.1.1

- Fixed ILô failing to load in Windhawk 2.0.0 alpha 8 when Taskbar.View.dll was already loaded: the Start button padding hook was registered twice, causing Windhawk to reject initialization.
- The hook is now shared by the icon-sizing and Start button positioning components. Existing settings and features are unchanged.

### ILô 2.1.0

- **Notification area:** choose the position of the hidden-icons chevron (left or just before the clock). Icon button spacing now adjusts automatically to icon size, and native dimensions are restored when customization is disabled.
- **Hover zoom:** macOS-style magnification now includes notification icons, with a continuous wave across the dock when the chevron is on the right or included on the left, provided the tray separator is disabled. The background-hiding option also applies to eligible tray icons.
- **Windows accent color:** use the live Windows accent in every color picker (tint, fallback, outline/dividers and both clock lines). Thanks to [**cjbfrog**](https://github.com/cjbfrog) for the suggestion!
- **Menus and tooltips:** sound and network context menus are centered above their icons; context menus have more space above the dock; rounded corners match the dock, including weather and generic tray tooltips. Fixed rectangular corner artifacts.
- **Backup and restore:** export and import settings as validated `.ILo` files or reset all dock settings from Advanced options.
- **Performance:** shared blur resources and cached composition effects, settings snapshots, reduced XAML tree searches and idle popup work, and smarter clock, weather and system-metric updates. GPU/VRAM counters run only when needed.
- **Stability:** fixed Explorer crashes when hovering app thumbnails with intermediate outline opacity. Thanks to [**cjbfrog**](https://github.com/cjbfrog) for discovering and reporting this bug!
- Improved dock realignment when applications close, startup restoration of visibility rules and hide/reveal animations, and graphics resource cleanup.
- Removed obsolete flyout-position logging and the manual notification button-size setting. Existing profiles are preserved; earlier `.ILo` backups from the test versions are supported.

### ILô 2.0.2

- Improved assisted update installation: the **Copy source and open Windhawk** button copies the verified source and opens the installed Windhawk application.
- Clear feedback immediately below the button, with instructions to update and compile the existing ILô mod and a fallback if Windhawk cannot be opened automatically.
- Update controls now appear before the release notes. SHA-256 verification and existing ILô profiles are preserved.

### ILô 2.0.1

- Custom two-line clock with editable templates, automatic or manual location, weather, additional time zone, and CPU, RAM, GPU, VRAM and battery variables.
- Rich clock tooltip with current weather, three-day forecast, temperature chart and system information.
- Independent context menus for the clock, sound, network and Win+X (including submenus), enabled by default, preserving native Windows labels and actions on recognized layouts.
- Shared background rendering across the dock, menus, tooltips, hidden notification icons and window thumbnail frames.
- Redesigned bilingual settings panel with illustrative previews, background presets, compact controls, sliders and color pickers.
- New About page with GitHub and PayPal links, stable-release checks and SHA-256-verified source downloads for assisted installation in Windhawk.
- Version 2.0.1 is the first public 2.x release and the update target for testing from the validated 2.0.0 build. Existing ILô profiles are preserved.

### ILô 1.6.3

- The hidden notification icons flyout now inherits the dock's background settings, including blur, opacity, tint, luminosity, saturation and inversion. Its theme is applied before the opening animation to avoid a brief flash of the original background.
- The Start button context menu (Win+X) and its power submenu use the dock's tint with a separate, non-interactive color layer while retaining native Windows Acrylic and clickable commands.
- Shared background-rendering code, cached elements and reduced polling avoid unnecessary work when the flyouts are closed or their settings have not changed.
- Known visual limitation: the power submenu may become darker after losing and regaining focus. Its commands remain native; the menu is otherwise themed.

### ILô 1.6.2

- Fixed automatic dock reveal after minimizing the last window that triggered auto-hide, without requiring the pointer to reach the bottom edge.
- Restored the configured reveal animation when Explorer moves the taskbar directly. The native reveal path is retried when the dock remains hidden.
- Improved monitor selection for hidden taskbars on multi-monitor setups.

### ILô 1.6.1

- Simplified auto-hide settings: custom reveal and hide delays are fixed at 5 ms. Animation durations remain adjustable and default to 200 ms.
- Fixed under-dock reveal so it follows the dock content on each monitor, independently of the interactive-area clipping setting and with a full-width background.
- Fixed notification icons that could stay magnified after the pointer left the tray upwards. Pointer checks run only while a tray icon is zoomed or animating.

### ILô 1.6

- Added an **Auto-hide** category between **Background and border** and **Hover zoom**. Windows behavior remains the default.
- The dock can stay visible or hide when a window is maximized, enters full screen, or overlaps the taskbar. It returns automatically when the hide rule no longer applies. You can limit the rule to the foreground window or the primary monitor and exclude individual applications.
- Reveal and hide delays can be adjusted separately. Alongside the Windows animation, seven transitions are available: **Instant**, **Slide**, **Elastic**, **Bounce**, **Fade**, **Slide and fade**, and **Overshoot**. Custom animations have independent reveal and hide durations, both set to **200 ms by default**.
- Fixed the **full-width taskbar background** so the background and its border reach both screen edges while the icons stay centered.

### ILô 1.5.4

- The settings window now uses the same four-square icon as the ILô context menu, drawn in white on a transparent background.
- Added space around the search box and between the settings cards and the scrollbar.
- Updated the Donate button to open Mighty-Luke’s PayPal.Me page.

### ILô 1.5.3

Fixed an issue after waking a PC with multiple HDMI displays. When displays reconnect in a different order, ILô now matches each taskbar to its XAML root so the notification area stays aligned with the application icons.

### ILô 1.5.2

- Switch between English and French from the settings panel. Switching takes effect immediately and preserves the current search and unsaved edits.
- The ILô settings command in the Start and taskbar context menus follows the selected language. ILô remembers the choice and uses English when the preference is missing or invalid.

### ILô 1.5.1

- The settings panel now places Minimize, Maximize/Restore and Close beside the search box. Drag the empty header to move the window or double-click it to maximize or restore.
- Fixed the colored strip along the top edge when the panel is restored. The upper edge still supports resizing.

### ILô 1.5

- Open the built-in settings panel by right-clicking Start or an empty area of the taskbar. The panel and both menu entries use English or French according to the Windows display language.
- Search 57 settings in seven categories, save a profile, or reset one category to its Windhawk values. Dependent controls explain which option enables them.
- The panel has its own taskbar icon, uses the dock’s background settings and remembers its window size.
- Corrected the spacing between applications and the notification area.

### ILô 1.4.4

Fixed an overlap when ILô Media sits to the right of Start. The dock now accounts for the space reserved by the visible player when positioning the notification area and releases it when the player hides.

### ILô 1.4.3

Added a PayPal donation button to the dock’s Windhawk page.

### ILô 1.4.2

Completed the English settings reference for all 57 options, including defaults and available choices. Clarified several English labels and added the missing app-divider placement description. Existing settings keys and defaults were preserved.

### ILô 1.4.1

Added support for layout updates from ILô Media. The dock recalculates its width when the compact player changes size or disappears, closing the empty gap after playback ends.

### ILô 1.4

Separated zoom levels for application and notification icons and raised both limits to 250%. Application icons can use a larger source image for sharper magnification. Added an option to keep a visible button background at its normal size.

### ILô 1.3

Added two styles for application icons. **Zoom**, the new default, enlarges only the hovered icon around its center, like the notification area. **MacOS** also animates neighboring icons.

### ILô 1.2

Extended hover zoom to notification icons. The entire notification area, the hidden-icons chevron, and the clock can be excluded. The chevron and clock keep their native size by default.

### ILô 1.1.3

Raised the default application hover zoom from 145% to 180%.

### ILô 1.1.2

Added an option, enabled by default, to hide application button backgrounds while hover zoom is active.

### ILô 1.1.1

Made the application button background follow the icon’s scale and movement during hover zoom.

### ILô 1.1

Introduced optional hover magnification for application icons. Users could set the zoom level, number of neighboring icons, spread and transition duration, and choose whether to include Start.

### ILô 1.0

First release under the **ILô** name by Mighty-Luke. Adopted the tray alignment from TAI Dock 1.0.3, validated on Windows 11 build 26300.10075. Added French settings and shipped the compact profile with a dock height of 24, a vertical dock offset of 8 and a separate notification icon offset of 0.

### vitaliiorlov baseline 1.5.278-vo

Starting point for ILô. This version of [vitaliiorlov’s fork](https://github.com/vitaliiorlov/windhawk-taskbar-centered-condensed) built on DarkionAvey’s TAI floating taskbar. It already included dock-shaped mouse interaction, primary-monitor notification placement and optional flyout placement logging. [Archived upstream fork notes](https://github.com/luke95330/ILo/blob/9e2abd8bb4d3ea6d259a54527cd5c2573037cb74/FORK-CHANGES.md).

## Français

### ILô 2.3.1

#### ILô Search - édition du texte

- Rétablissement de la sélection de texte à la souris et au clavier dans le champ du dock et les fenêtres compacte et déployée, y compris la sélection et la suppression partielles ainsi que les raccourcis habituels Ctrl+A, Ctrl+C, Ctrl+X et Ctrl+V.
- Ajout d'un menu contextuel d'édition autonome aux couleurs du dock : Annuler, Couper, Copier, Coller, Supprimer et Tout sélectionner. Il se positionne selon les coordonnées écran du pointeur, respecte les limites du moniteur et maintient la recherche et le dock visibles pendant l'édition.
- Le menu affiche uniquement les commandes disponibles et adapte sa hauteur et ses arrondis. Si aucune commande n'est disponible, seul Coller apparaît en grisé.
- Surlignage de la sélection en bleu opaque et contrasté dans les thèmes clair et sombre, y compris lorsque le menu d'édition est ouvert.
- Stabilisation de l'édition grâce à la fenêtre autonome pour les interactions locales, au maintien du moteur natif de saisie et au report du redimensionnement lié à la recherche jusqu'à la fin des événements d'édition. L'intégration de la recherche, les réglages existants et les sauvegardes compatibles sont conservés.

### ILô 2.3.0

#### ILô Search — votre nouvelle recherche Windows

- **Remplacement de l'interface native de recherche au-delà du dock.** Utilisez Win+S, commencez à saisir une recherche dans le menu Démarrer natif, ou recherchez depuis Start11 et les lanceurs compatibles pour ouvrir directement ILô Search. Les deux nouvelles options **Remplacer Win+S** et **Rediriger les recherches** sont activées par défaut et réglables indépendamment.
- **Une entrée de recherche Démarrer recréée.** ILô remplace le champ natif de Démarrer par sa propre entrée, sans attendre l'ouverture de SearchHost. Lorsque la recherche est visible dans le dock (icône seule ou champ de recherche), le champ redondant de Démarrer disparaît, mais la saisie directe reste possible. En mode Masquée, le champ ILô reste visible dans Démarrer ; Windows (origine) rétablit l'interface native.
- **Une fenêtre de recherche autonome et directe.** Les demandes de recherche ouvrent le véritable éditeur ILô avant d'accepter la saisie, afin de réduire les délais de basculement, les premiers caractères manquants et l'apparition fugace du volet Windows. L'animation de déploiement, la saisie dans le dock, la navigation clavier et les actions sur les résultats sont conservées.
- **Intégration fiable à Démarrer.** Réapplication de la présentation lorsque Windows reconstruit le menu après l'épinglage ou le désépinglage d'applications. Les mécanismes de repli natifs sont conservés lorsqu'une demande directe ne peut être prise en charge.

#### Disposition du dock, performances et stabilité

- **Décalage vertical à marge unique :** le dock flottant ne réserve plus que sa hauteur et l'espace qui le sépare du bord de l'écran, sans marge invisible côté applications. Le masquage par chevauchement tient compte de la hauteur réellement dessinée, et non de la fenêtre système plus grande. Les applications, la zone de notification et la recherche partagent cette géométrie.
- **Optimisation de la recherche :** chargement des métadonnées des raccourcis Démarrer uniquement lorsque des résultats d'applications le nécessitent, réutilisation des icônes en cache, abandon plus rapide des requêtes obsolètes et réduction des objets XAML, des mises à jour de propriétés et des traitements redondants des résultats et catégories.
- **Nettoyage du code :** suppression des routines natives obsolètes de disposition et de positionnement de la recherche, réduction de la journalisation répétitive et simplification de la gestion des événements et de la libération des fenêtres de recherche. Les réglages existants et les sauvegardes compatibles sont préservés.

### ILô 2.2.0

#### ILô Search — la fonctionnalité phare

- **Remplacement complet de l’interface de recherche Windows du dock.** ILô Search dispose de sa propre icône ou de son propre champ, d’une fenêtre de résultats, de catégories et de menus contextuels, avec une identité graphique inspirée de Spotlight. La recherche Windows native reste accessible via Win+S ou en choisissant la présentation Windows (origine).
- **Quatre présentations :** icône seule (nouveau défaut), champ de recherche, masquée ou Windows native. En mode icône, un champ compact se déploie en fenêtre de résultats dès la saisie ; en mode champ, le dock sert lui-même de zone de saisie, sans doublon. Aucune recherche n’est lancée avant la saisie d’une requête.
- **Recherche unifiée :** applications classiques et installées, fichiers et dossiers, paramètres Windows et ILô. Choix entre Windows Search (par défaut) et [Everything](https://www.voidtools.com/) lorsqu’il est installé et actif, avec repli automatique vers Windows Search. Les fichiers sont recherchés dans l’index existant, sans reparcourir les disques. Un raccourci web facultatif ouvre le navigateur par défaut uniquement si vous le sélectionnez.
- **Résultats organisés :** catégories Applications, Documents, Images, Audio, Vidéo, Paramètres et Autres, masquées lorsqu’elles sont vides. Dans Tout, les applications et paramètres passent en premier et s’affichent en grille, suivis des autres types de fichiers. Icônes de catégories, infobulles, transitions directionnelles et navigation clavier.
- **Vraies icônes et raccourcis :** prise en charge des icônes de raccourcis standard et personnalisés, y compris ceux des lanceurs tiers comme Playnite. Les applications sont lancées en conservant le raccourci d’origine, ses arguments et son dossier de travail.
- **Agir directement sur les résultats :** ouvrir/exécuter, ouvrir avec, exécuter en tant qu’administrateur, afficher l’emplacement et les propriétés, créer un raccourci sur le bureau, ajouter au menu Démarrer et épingler les applications compatibles à la barre des tâches. Pour les fichiers et dossiers, **Créer une copie…** permet de choisir une destination dans le sélecteur natif Windows, tout en conservant le panneau de recherche ouvert. Les actions disponibles dépendent du résultat sélectionné et de la prise en charge par Windows.
- **Une recherche entièrement personnalisable :** dimensions du champ et du volet, arrondis, épaisseur et couleurs du contour, couleurs et opacité du fond, flou commun au dock et animations. La fenêtre déployée se centre au-dessus du dock ; l’icône participe à l’effet de zoom macOS lorsqu’il est activé. Un clic droit sur la recherche du dock donne accès aux paramètres de recherche Windows, à l’indexation et aux réglages d’ILô Search.
- **Nouveaux réglages par défaut :** icône seule, largeur de champ de 220 DIP, hauteur automatique (0) et fenêtre de 700 × 700 DIP, adaptée à l’espace disponible.

#### Dock, performances et stabilité

- L’icône du panneau de configuration s’adapte au thème clair ou sombre de la barre des tâches Windows.
- Maintien du dock visible pendant l’utilisation d’ILô Search ou le survol de l’infobulle interactive de l’horloge/météo, puis retour au comportement de visibilité choisi.
- Libération de l’arbre graphique et des données temporaires du panneau de configuration à sa fermeture, tout en conservant le moteur XAML initialisé pour une réouverture rapide.
- Libération de l’interface de recherche et des résultats après fermeture. Requêtes et traitement des icônes sur un fil indépendant ; cache limité à 4 Mio de données d’icônes et 512 entrées, avec éviction des moins récemment utilisées. Libération des caches de recherche après trois minutes d’inactivité.
- Préparation à la demande du contenu de l’infobulle horloge/météo et libération après le délai de fermeture et de transition du pointeur. Les données météo restent mises en cache pour un affichage rapide et actualisé.
- Réduction de la surveillance des volets au repos (intervalle de 1,8 seconde au lieu de 600 ms), suspension des observateurs de disposition des miniatures masquées et création des sous-menus Win+X à la demande. Les interactions actives et animations du dock conservent leur réactivité.
- Les profils existants et les anciennes sauvegardes `.ILo` compatibles restent pris en charge.

### ILô 2.1.1

- Correction du chargement d’ILô dans Windhawk 2.0.0 alpha 8 lorsque Taskbar.View.dll était déjà chargé : le hook d’espacement du bouton Démarrer était enregistré deux fois, ce qui provoquait l’échec de l’initialisation.
- Le hook est désormais partagé entre le dimensionnement des icônes et le positionnement du bouton Démarrer. Les paramètres et fonctionnalités existants sont conservés.

### ILô 2.1.0

- **Zone de notification :** position personnalisable du chevron des applications masquées (à gauche ou juste avant l’horloge). L’espacement des boutons s’adapte automatiquement à la taille des icônes, et les dimensions natives sont restaurées à la désactivation de la personnalisation.
- **Zoom au survol :** extension de l’effet macOS au systray, avec continuité entre les applications et la zone de notification lorsque le chevron est à droite ou inclus dans le zoom à gauche, à condition que le séparateur soit désactivé. Le masquage des fonds s’applique également aux icônes de notification concernées.
- **Couleur d’accentuation de Windows :** disponible dans tous les sélecteurs (teinte, repli, contour/séparateurs et deux lignes de l’horloge), avec mise à jour automatique. Merci à [**cjbfrog**](https://github.com/cjbfrog) pour sa suggestion !
- **Menus et infobulles :** centrage des menus contextuels du son et du réseau au-dessus de leurs icônes, espacement accru avec le dock, harmonisation des arrondis des menus et infobulles météo et de notification. Correction des artefacts rectangulaires dans les coins.
- **Sauvegarde et restauration :** export et import des paramètres au format `.ILo` avec validation du fichier, et remise à zéro complète depuis les options avancées.
- **Performances :** mutualisation du moteur de flou et mise en cache des effets de composition, des paramètres et des éléments XAML ; réduction du travail des volets inactifs et actualisation intelligente de l’horloge, de la météo et des statistiques. Les compteurs GPU/VRAM ne fonctionnent que lorsque nécessaire.
- **Stabilité :** correction des plantages d’Explorer associés aux valeurs intermédiaires d’opacité du contour lors de l’affichage des miniatures. Merci à [**cjbfrog**](https://github.com/cjbfrog) pour la découverte et le signalement de ce bug !
- Amélioration du réalignement du dock à la fermeture d’une application, de la restauration des règles de visibilité et des animations de masquage au démarrage, ainsi que de la libération des ressources graphiques.
- Suppression de la journalisation de la position des volets et du réglage manuel de la taille des boutons de notification. Les profils existants sont conservés ; les anciennes sauvegardes `.ILo` des versions de test restent compatibles.

### ILô 2.0.2

- Installation assistée des mises à jour améliorée : le bouton **Copier le code et ouvrir Windhawk** copie la source vérifiée et ouvre l'application Windhawk installée.
- Confirmation immédiatement sous le bouton, avec les instructions pour mettre à jour et compiler le mod ILô existant et une solution de repli si l'ouverture automatique échoue.
- Les commandes de mise à jour apparaissent avant les notes de version. La vérification SHA-256 et les profils ILô existants sont conservés.

### ILô 2.0.1

- Horloge personnalisable sur deux lignes avec modèles éditables, localisation automatique ou manuelle, météo, fuseau supplémentaire et variables CPU, RAM, GPU, VRAM et batterie.
- Info-bulle enrichie : météo actuelle, prévisions sur trois jours, courbes de températures et informations système.
- Menus contextuels indépendants pour l'horloge, le son, le réseau et Win+X (sous-menus inclus), activés par défaut, avec les libellés et actions Windows d'origine sur les dispositions reconnues.
- Rendu graphique commun au dock, aux menus, aux info-bulles, aux icônes masquées et aux cadres des miniatures.
- Panneau de paramètres bilingue repensé : aperçus illustratifs, styles de fond, contrôles compacts, réglettes et sélecteurs de couleurs.
- Nouvelle rubrique À propos avec liens GitHub et PayPal, recherche des versions stables et téléchargement de la source vérifiée par SHA-256 pour une installation assistée dans Windhawk.
- La version 2.0.1 est la première publication publique de la série 2.x et permet de tester la mise à jour depuis la 2.0.0 validée. Les profils ILô existants sont conservés.

### ILô 1.6.3

- Le panneau des icônes masquées de la zone de notification reprend les réglages de fond du dock : flou, opacité, teinte, luminosité, saturation et inversion. Le thème est appliqué avant l'animation d'ouverture afin d'éviter un bref affichage du fond d'origine.
- Le menu contextuel du bouton Démarrer (Win+X) et son sous-menu d'alimentation reprennent la teinte du dock grâce à une couche de couleur non interactive, tout en conservant l'Acrylic natif de Windows et les commandes cliquables.
- La mutualisation du rendu, la mise en cache des éléments et la réduction des vérifications évitent les traitements inutiles lorsque les panneaux sont fermés ou que leurs réglages restent inchangés.
- Limitation visuelle connue : le sous-menu d'alimentation peut s'assombrir après une perte puis une reprise de focus. Ses commandes restent natives ; le reste du menu conserve sa personnalisation.

### ILô 1.6.2

- Correction de la réapparition automatique du dock après la réduction de la dernière fenêtre qui provoquait son masquage, sans déplacer le pointeur vers le bord inférieur.
- Rétablissement de l’animation de révélation sélectionnée lorsque l’Explorateur déplace directement la barre. Une nouvelle demande de révélation est effectuée si le dock reste masqué.
- Amélioration de l’identification de l’écran associé à une barre masquée sur les configurations multi-écrans.

### ILô 1.6.1

- Simplification du masquage : les délais personnalisés de révélation et de masquage sont fixés à 5 ms. Les durées d’animation restent réglables, à 200 ms par défaut.
- Correction de la révélation uniquement sous le dock : la zone suit le contenu sur chaque écran, indépendamment du découpage de la zone interactive et avec un fond pleine largeur.
- Correction des icônes de notification qui pouvaient rester agrandies après une sortie du pointeur par le haut. La vérification du pointeur intervient uniquement pendant le zoom ou son animation.

### ILô 1.6

- Ajout de la catégorie **Masquage** entre **Fond et bordure** et **Zoom au survol**. Le comportement de Windows reste sélectionné par défaut.
- Le dock peut rester visible ou se masquer lorsqu’une fenêtre est agrandie, passe en plein écran ou chevauche la barre. Il réapparaît automatiquement dès que la règle de masquage cesse de s’appliquer. La règle peut se limiter à la fenêtre active ou à l’écran principal, et certaines applications peuvent être exclues.
- Les délais de révélation et de masquage se règlent séparément. En plus de l’animation Windows, sept transitions sont disponibles : **Instantanée**, **Glissement**, **Élastique**, **Rebond**, **Fondu**, **Glissement et fondu** et **Dépassement**. Les durées des animations personnalisées sont indépendantes et valent **200 ms par défaut dans chaque sens**.
- Correction du **fond sur toute la largeur** : le fond et sa bordure atteignent les deux bords de l’écran tandis que les icônes restent centrées.

### ILô 1.5.4

- La fenêtre des paramètres reprend l’icône à quatre carrés du menu contextuel ILô, dessinée en blanc sur fond transparent.
- Le champ de recherche est plus aéré et les cartes de réglages sont davantage espacées de la barre de défilement.
- Le bouton de don ouvre désormais la page PayPal.Me de Mighty-Luke.

### ILô 1.5.3

Correction d’un problème de disposition à la sortie de veille sur les configurations à plusieurs écrans HDMI. Lorsque les écrans se reconnectent dans un ordre différent, ILô associe chaque barre des tâches à sa racine XAML pour que la zone de notification reste alignée avec les icônes des applications.

### ILô 1.5.2

- Choisissez l’anglais ou le français depuis le panneau de configuration. Le changement est immédiat et conserve la recherche en cours ainsi que les réglages en attente d’enregistrement.
- L’entrée Paramètres ILô des menus contextuels de Démarrer et de la barre des tâches suit la langue choisie. ILô mémorise ce choix et utilise l’anglais si la préférence est absente ou invalide.

### ILô 1.5.1

- Le panneau de configuration intègre désormais les boutons Réduire, Agrandir/Restaurer et Fermer à côté du champ de recherche. Faites glisser une zone libre de l’en-tête pour déplacer la fenêtre, ou double-cliquez pour l’agrandir ou la restaurer.
- Correction de la bande colorée en haut du panneau en mode fenêtre. Le bord supérieur permet toujours de redimensionner la fenêtre.

### ILô 1.5

- Ouvrez le panneau intégré depuis le menu contextuel de Démarrer ou d’une zone vide de la barre des tâches. Le panneau et les deux entrées de menu suivent la langue d’affichage de Windows (français ou anglais).
- Recherchez parmi 57 réglages répartis en sept catégories, enregistrez un profil ou réinitialisez une rubrique aux valeurs de Windhawk. Les commandes grisées indiquent quel réglage les active.
- Le panneau dispose de sa propre icône dans la barre des tâches, reprend les réglages de fond du dock et mémorise la taille de sa fenêtre.
- Correction de l’espacement entre les applications et la zone de notification.

### ILô 1.4.4

Correction du chevauchement lorsque le lecteur ILô Media se trouve à droite de Démarrer. Le dock tient compte de la place réservée au lecteur visible pour positionner la zone de notification et libère cet espace lorsque le lecteur se masque.

### ILô 1.4.3

Ajout d’un bouton de don PayPal sur la page du dock dans Windhawk.

### ILô 1.4.2

Ajout d’un guide anglais complet des 57 réglages, avec les valeurs par défaut et les choix disponibles. Plusieurs libellés anglais ont été précisés et la description manquante de la position des séparateurs a été ajoutée. Les clés et les valeurs par défaut ont été conservées.

### ILô 1.4.1

Prise en charge des notifications de changement de taille d’ILô Media. Le dock recalcule sa largeur lorsque le lecteur compact change de taille ou disparaît, ce qui supprime l’espace vide après la fermeture du lecteur.

### ILô 1.4

Réglages de zoom distincts pour les applications et la zone de notification, avec un plafond de 250 % dans les deux cas. Les icônes d’application peuvent utiliser une image source plus grande pour améliorer la netteté. Une nouvelle option conserve le fond visible des boutons à sa taille normale.

### ILô 1.3

Ajout de deux styles pour les applications. **Zoom**, le nouveau choix par défaut, agrandit uniquement l’icône survolée autour de son centre, comme dans la zone de notification. **MacOS** anime aussi les icônes voisines.

### ILô 1.2

Extension du zoom aux icônes de notification. Il est possible d’exclure toute la zone, le chevron des icônes masquées ou l’horloge. Le chevron et l’horloge conservent leur taille native par défaut.

### ILô 1.1.3

Passage du zoom par défaut des applications de 145 % à 180 %.

### ILô 1.1.2

Ajout d’une option, activée par défaut, pour masquer le fond des boutons d’application lorsque le zoom au survol est actif.

### ILô 1.1.1

Le fond du bouton d’application suit désormais l’agrandissement et le déplacement de l’icône pendant le survol.

### ILô 1.1

Première version du zoom facultatif au survol des icônes d’application. Les réglages permettent de choisir le grossissement, le nombre d’icônes voisines, leur écartement, la durée de transition et l’inclusion du bouton Démarrer.

### ILô 1.0

Première version sous le nom **ILô**, par Mighty-Luke. Reprise du centrage de la zone de notification de TAI Dock 1.0.3, validé sur Windows 11 build 26300.10075. Ajout des réglages en français et du profil compact avec une hauteur de 24, un décalage vertical du dock de 8 et un décalage distinct de 0 pour les icônes de notification.

### Base de vitaliiorlov 1.5.278-vo

Point de départ d’ILô. Cette version du [fork de vitaliiorlov](https://github.com/vitaliiorlov/windhawk-taskbar-centered-condensed) reposait sur la barre flottante TAI de DarkionAvey. Elle gérait déjà la zone cliquable limitée au dock, le placement des notifications sur l’écran principal et la journalisation facultative de la position des volets. [Notes archivées du fork d’origine](https://github.com/luke95330/ILo/blob/9e2abd8bb4d3ea6d259a54527cd5c2573037cb74/FORK-CHANGES.md).

