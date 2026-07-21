# Pravěká Tlupa

Webová stolní hra pro 10–20 hráčů určená pro táborové prostředí.

## O hře

Každý hráč vede pravěkou tlupu a snaží se nashromáždit co nejvíce zásob před příchodem doby ledové. Hru řídí administrátor, který jako jediný pracuje s webovou aplikací. Hráčská komunikace probíhá fyzicky přes nástěnku a papírové lístky.

## Soubory

| Soubor | Popis |
|--------|-------|
| `praveka_tlupa.html` | **Herní aplikace** — otevřít v prohlížeči, žádná instalace není potřeba |
| `gen_game.py` | Generátor HTML aplikace (Python skript) |
| `Praveka_tlupa_specifikace.docx` | Kompletní herní specifikace (Word dokument) |

## Spuštění

Stačí otevřít soubor `praveka_tlupa.html` v moderním prohlížeči (Chrome, Firefox, Edge). Data se ukládají do `localStorage` — doporučujeme vždy používat stejný prohlížeč na stejném počítači.

## Herní mechanika

- **Role členů tlupy:** Sběrači, Lovci, Hlídači, Pobertové, Nečinní
- **Šamanská kouzla:** Plodnost, Hojnost, Urputnost, Chamtivost, Obrana
- **Události dne:** Mamutí fičák, Vzteklina, Boží vtípek, Pramlha, Zatmění měsíce
- **Tiskové sestavy:** Osobní lístky hráčů, Karty událostí, Pravidla hry, Žebříček

## Technologie

Samostatný HTML soubor s vloženým CSS a JavaScriptem. Data jsou uložena v `localStorage` prohlížeče a lze je exportovat/importovat jako JSON. Žádný server ani instalace nejsou potřeba.
