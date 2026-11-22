# ILô — Changelog / Historique

[English](#english) · [Français](#français)

## English

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
