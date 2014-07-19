# Project stockscraper #

 * git name: stscrp

## Architecture

hledáme obyčejnou architekturu M-V-C.

 * **Model** se stará o scrapnutí a uložení dat.

 * **View** nám prezentuje data, je to jediná část se kterou uživatel přímo komunikuje

 * **Controller** to všechno ovládá. Zachycuje události z View, provádí dožádání dat z Modelu a jejich Vrácení View pro zobrazení uživateli.

 * **NotifCenter** je notifikační centrum, ostatní objekty se u něj přihlašují o odběr zpráv a zasílají mu notifikace, které jsou podle seznamu předávány dál. 
