# ILô 1.4.1

Dock Windhawk pour Windows 11, adapté par Mighty-Luke. ILô centre les applications et la zone de notification, personnalise le fond et propose un zoom au survol. Les réglages sont disponibles en français. Version validée sur Windows 11 build 26300.10075 avec Windhawk 1.7.3.

## Installation

Désactivez l’ancien mod de dock. Dans Windhawk, créez un mod local, remplacez le contenu de l’éditeur par celui de [ilo.wh.cpp](ilo.wh.cpp), puis compilez. Les réglages du dock sont accessibles dans l’onglet **Paramètres**.

## Sources

Modifiez [ilo.wh.cpp](ilo.wh.cpp), puis lancez `python assemble-mod.py` pour actualiser les deux fichiers de distribution historiques. Le dossier `mod-parts` conserve les sources du fork d’origine.

ILô dérive du [fork de vitaliiorlov](https://github.com/vitaliiorlov/windhawk-taskbar-centered-condensed), issu de [TAI de DarkionAvey](https://github.com/DarkionAvey/windhawk-taskbar-centered-condensed). Le code du dock conserve les mentions de licence GPLv3.
