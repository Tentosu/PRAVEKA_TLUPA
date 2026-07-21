#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Praveka Tlupa game as a single HTML file."""

CSS = r"""
:root {
  --parch: #f5ecd0;
  --parch-dark: #e6d4a0;
  --parch-border: #c4a85a;
  --brown-deep: #2a1208;
  --brown-dark: #4a1e0a;
  --brown-mid: #7a3c18;
  --brown-light: #a86030;
  --ochre: #c8a44a;
  --ochre-light: #e0c070;
  --stone: #8a7a68;
  --stone-light: #b5a898;
  --red-dark: #7a2020;
  --red: #a83030;
  --green-dark: #2a4a1a;
  --green: #3a6428;
  --blue-tribe: #2a3a6a;
  --shadow: rgba(0,0,0,0.5);
  --font-head: Georgia, 'Times New Roman', serif;
  --font-body: 'Segoe UI', Arial, sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--brown-deep);
  background-image:
    radial-gradient(ellipse at 20% 20%, rgba(100,50,10,0.3) 0%, transparent 60%),
    radial-gradient(ellipse at 80% 80%, rgba(60,30,5,0.4) 0%, transparent 60%);
  min-height: 100vh;
  font-family: var(--font-body);
  color: var(--parch);
}

/* Nav */
nav {
  background: linear-gradient(135deg, var(--brown-dark) 0%, var(--brown-mid) 100%);
  border-bottom: 3px solid var(--ochre);
  padding: 0;
  display: flex;
  align-items: stretch;
  flex-wrap: wrap;
  box-shadow: 0 4px 12px var(--shadow);
  position: sticky; top: 0; z-index: 100;
}
nav .logo {
  font-family: var(--font-head);
  font-size: 1.3rem; font-weight: bold;
  color: var(--ochre);
  padding: 12px 20px;
  text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
  letter-spacing: 1px; white-space: nowrap;
}
nav button {
  background: none; border: none;
  color: var(--parch);
  padding: 0 16px;
  font-family: var(--font-body); font-size: 0.88rem;
  cursor: pointer;
  border-left: 1px solid rgba(200,164,74,0.3);
  transition: background 0.2s, color 0.2s;
  min-height: 48px;
}
nav button:hover { background: rgba(200,164,74,0.2); color: var(--ochre-light); }
nav button.active { background: rgba(200,164,74,0.15); color: var(--ochre); font-weight: bold; }
nav .nav-right { margin-left: auto; display: flex; }
nav .nav-day {
  padding: 0 16px; font-family: var(--font-head); font-size: 0.85rem;
  color: var(--stone-light); display: flex; align-items: center;
  border-left: 1px solid rgba(200,164,74,0.3);
}

/* Screens */
.screen { display: none; padding: 24px; max-width: 1200px; margin: 0 auto; }
.screen.active { display: block; }

/* Cards */
.card {
  background: linear-gradient(160deg, var(--parch) 0%, var(--parch-dark) 100%);
  border: 2px solid var(--parch-border);
  border-radius: 6px; padding: 20px; margin-bottom: 20px;
  box-shadow: 0 4px 16px var(--shadow), inset 0 1px 0 rgba(255,255,255,0.3);
  color: var(--brown-deep); position: relative;
}
.card::before {
  content: ''; position: absolute; inset: 0; border-radius: 4px;
  background: repeating-linear-gradient(45deg, transparent, transparent 40px,
    rgba(180,140,60,0.04) 40px, rgba(180,140,60,0.04) 80px);
  pointer-events: none;
}
.card-dark {
  background: linear-gradient(160deg, var(--brown-dark) 0%, var(--brown-deep) 100%);
  border-color: var(--ochre); color: var(--parch);
}
.card h2 {
  font-family: var(--font-head); font-size: 1.3rem; color: var(--brown-mid);
  margin-bottom: 14px; padding-bottom: 8px;
  border-bottom: 2px solid var(--parch-border);
  display: flex; align-items: center; gap: 8px;
}
.card-dark h2 { color: var(--ochre); border-color: rgba(200,164,74,0.4); }
.card h3 { font-family: var(--font-head); font-size: 1.05rem; color: var(--brown-mid); margin-bottom: 10px; }

/* Status banner */
.status-banner {
  border-radius: 6px; padding: 14px 18px; margin-bottom: 20px;
  display: flex; align-items: center; gap: 14px;
  font-size: 0.95rem; font-weight: 600; border: 2px solid;
}
.status-banner.running {
  background: linear-gradient(135deg, rgba(58,100,40,0.2), rgba(58,100,40,0.1));
  border-color: #5a9a38; color: var(--green-dark);
}
.status-banner.idle {
  background: linear-gradient(135deg, rgba(200,164,74,0.15), rgba(200,164,74,0.08));
  border-color: var(--ochre); color: var(--brown-mid);
}
.status-banner .status-icon { font-size: 2rem; flex-shrink: 0; }
.status-banner .status-detail { font-size: 0.82rem; font-weight: 400; margin-top: 3px; color: var(--stone); }

/* Page title */
.page-title {
  font-family: var(--font-head); font-size: 2rem;
  color: var(--ochre); text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
  margin-bottom: 6px; letter-spacing: 2px;
}
.page-sub { font-size: 0.9rem; color: var(--stone-light); margin-bottom: 24px; }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 9px 18px; border-radius: 4px; border: 2px solid transparent;
  font-family: var(--font-body); font-size: 0.9rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; text-decoration: none;
}
.btn-primary { background: linear-gradient(135deg, var(--brown-mid), var(--brown-dark)); border-color: var(--ochre); color: var(--ochre); }
.btn-primary:hover { background: linear-gradient(135deg, var(--brown-light), var(--brown-mid)); }
.btn-ochre { background: linear-gradient(135deg, var(--ochre), #a07828); border-color: var(--ochre-light); color: var(--brown-deep); }
.btn-ochre:hover { background: linear-gradient(135deg, var(--ochre-light), var(--ochre)); }
.btn-red { background: linear-gradient(135deg, var(--red), var(--red-dark)); border-color: #c04040; color: var(--parch); }
.btn-red:hover { background: linear-gradient(135deg, #c04040, var(--red)); }
.btn-green { background: linear-gradient(135deg, var(--green), var(--green-dark)); border-color: #6a9a40; color: var(--parch); }
.btn-green:hover { background: linear-gradient(135deg, #4a7a30, var(--green)); }
.btn-sm { padding: 5px 12px; font-size: 0.82rem; }
.btn-lg { padding: 12px 28px; font-size: 1rem; }
.btn:disabled { opacity: 0.45; cursor: not-allowed; }

/* Forms */
.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.form-group { display: flex; flex-direction: column; gap: 5px; }
.form-group label { font-size: 0.82rem; font-weight: 600; color: var(--brown-mid); text-transform: uppercase; letter-spacing: 0.5px; }
.card-dark .form-group label { color: var(--stone-light); }
.form-group input, .form-group select {
  background: rgba(255,255,255,0.7); border: 2px solid var(--parch-border);
  border-radius: 4px; padding: 7px 10px;
  font-family: var(--font-body); font-size: 0.9rem; color: var(--brown-deep); width: 100%;
}
.form-group input:focus, .form-group select:focus { outline: none; border-color: var(--ochre); }
.form-row { display: flex; gap: 12px; flex-wrap: wrap; align-items: flex-end; }
.form-row .form-group { flex: 1; min-width: 120px; }

/* Tables */
.data-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.data-table th {
  background: linear-gradient(135deg, var(--brown-mid), var(--brown-dark));
  color: var(--ochre); padding: 10px 12px; text-align: left;
  font-family: var(--font-head); font-size: 0.85rem; letter-spacing: 0.5px;
  border-bottom: 2px solid var(--ochre);
}
.data-table td { padding: 9px 12px; border-bottom: 1px solid var(--parch-border); color: var(--brown-deep); }
.data-table tr:nth-child(even) td { background: rgba(196,168,90,0.12); }
.data-table tr:hover td { background: rgba(196,168,90,0.22); }
.data-table .rank { font-weight: bold; font-size: 1.1rem; color: var(--brown-mid); }
.data-table .supply-num { font-weight: bold; font-size: 1.05rem; color: var(--green-dark); }
.rank-1 td { background: rgba(200,164,74,0.25) !important; }
.rank-2 td { background: rgba(192,192,192,0.15) !important; }
.rank-3 td { background: rgba(176,116,64,0.15) !important; }

/* Misc */
.color-dot { display: inline-block; width: 14px; height: 14px; border-radius: 50%; border: 2px solid rgba(0,0,0,0.3); flex-shrink: 0; }
.badge { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.8rem; font-weight: 600; }
.badge-event { background: linear-gradient(135deg, var(--red), var(--red-dark)); color: var(--parch); border: 1px solid #c04040; }
.badge-spell { background: linear-gradient(135deg, #4a2a7a, #2a1a5a); color: #d0b0ff; border: 1px solid #7a50c0; }

/* Event info box */
.event-info-box {
  margin-top: 10px; padding: 12px 16px;
  background: rgba(168,48,48,0.1); border: 2px solid rgba(168,48,48,0.35);
  border-radius: 6px; font-size: 0.88rem; color: var(--brown-deep);
  display: none;
}
.event-info-box.visible { display: block; }
.event-info-box .ev-name { font-family: var(--font-head); font-weight: bold; font-size: 1rem; margin-bottom: 5px; }
.event-info-box .ev-desc { margin-bottom: 6px; line-height: 1.6; }
.event-info-box .ev-tags { display: flex; gap: 6px; flex-wrap: wrap; }
.ev-tag {
  padding: 2px 10px; border-radius: 10px; font-size: 0.78rem; font-weight: 700;
}
.ev-tag-neg { background: rgba(168,48,48,0.15); color: var(--red-dark); border: 1px solid rgba(168,48,48,0.4); }
.ev-tag-pos { background: rgba(58,100,40,0.15); color: var(--green-dark); border: 1px solid rgba(58,100,40,0.4); }

/* Player inputs */
.player-input-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 16px; }
.player-input-card {
  background: linear-gradient(160deg, var(--parch) 0%, var(--parch-dark) 100%);
  border: 2px solid var(--parch-border); border-radius: 6px; padding: 16px; color: var(--brown-deep);
}
.player-input-card .pname {
  font-family: var(--font-head); font-size: 1.05rem; font-weight: bold;
  display: flex; align-items: center; gap: 8px;
  margin-bottom: 10px; padding-bottom: 8px; border-bottom: 2px solid var(--parch-border);
}
.player-input-card .pinfo { font-size: 0.82rem; color: var(--stone); margin-bottom: 10px; }
.input-roles { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.role-input { display: flex; flex-direction: column; gap: 3px; }
.role-input label { font-size: 0.78rem; font-weight: 600; color: var(--brown-mid); text-transform: uppercase; letter-spacing: 0.4px; }
.role-input input, .role-input select {
  background: rgba(255,255,255,0.7); border: 2px solid var(--parch-border);
  border-radius: 4px; padding: 6px 8px; font-size: 0.9rem; color: var(--brown-deep); width: 100%;
}
.role-input input:focus, .role-input select:focus { outline: none; border-color: var(--ochre); }
.total-bar { margin-top: 10px; padding: 6px 10px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; text-align: center; }
.total-ok { background: rgba(58,100,40,0.15); color: var(--green-dark); }
.total-warn { background: rgba(168,48,48,0.15); color: var(--red-dark); }
.full-width-input { grid-column: 1 / -1; }

/* Results event banner */
.results-event-banner {
  background: linear-gradient(135deg, var(--red-dark), var(--red));
  border: 2px solid #c04040; border-radius: 6px;
  padding: 14px 18px; margin-bottom: 16px; color: var(--parch);
  display: flex; align-items: flex-start; gap: 12px;
}
.results-event-banner.ev-none { background: linear-gradient(135deg, var(--stone), #6a6058); border-color: var(--stone); }
.results-event-banner .event-icon { font-size: 2rem; flex-shrink: 0; margin-top: 2px; }
.results-event-banner h3 { font-family: var(--font-head); font-size: 1.15rem; margin-bottom: 4px; }
.results-event-banner .ev-detail-desc { font-size: 0.87rem; opacity: 0.9; margin-bottom: 5px; line-height: 1.5; }
.results-event-banner .ev-effects { font-size: 0.8rem; opacity: 0.75; font-style: italic; }
.results-event-banner .ev-tag-neg { background: rgba(255,200,200,0.25); color: #ffd8d8; border-color: rgba(255,200,200,0.5); }
.results-event-banner .ev-tag-pos { background: rgba(200,255,200,0.25); color: #d0ffd8; border-color: rgba(200,255,200,0.5); }

/* History */
.history-day {
  border: 2px solid var(--parch-border); border-radius: 6px; margin-bottom: 14px;
  background: linear-gradient(160deg, var(--parch) 0%, var(--parch-dark) 100%);
  overflow: hidden;
}
.history-day-header {
  padding: 12px 18px; cursor: pointer;
  display: flex; align-items: center; gap: 10px;
  background: linear-gradient(135deg, rgba(196,168,90,0.15), transparent);
  border-bottom: 2px solid var(--parch-border);
  user-select: none;
}
.history-day-header:hover { background: linear-gradient(135deg, rgba(196,168,90,0.25), rgba(196,168,90,0.1)); }
.history-day-header .day-num { font-family: var(--font-head); font-size: 1.1rem; font-weight: bold; color: var(--brown-mid); min-width: 60px; }
.history-day-header .day-event { flex: 1; }
.history-day-header .toggle-icon { color: var(--stone); font-size: 1.1rem; }
.history-day-body { padding: 16px 18px; display: none; }
.history-day-body.open { display: block; }
.history-day.current > .history-day-header { background: linear-gradient(135deg, rgba(200,164,74,0.3), rgba(200,164,74,0.1)); }
.history-day.current > .history-day-header .day-num { color: var(--brown-dark); }

/* Result helpers */
.result-plus { color: var(--green-dark); font-weight: bold; }
.result-minus { color: var(--red-dark); font-weight: bold; }
.result-detail { font-size: 0.82rem; color: var(--stone); margin-top: 4px; line-height: 1.5; }

/* Bonus */
.bonus-list { display: flex; flex-direction: column; gap: 8px; }
.bonus-item {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 12px;
  background: rgba(196,168,90,0.12); border: 1px solid var(--parch-border); border-radius: 4px; font-size: 0.88rem;
}
.bonus-amount { font-weight: bold; min-width: 60px; }
.bonus-amount.pos { color: var(--green-dark); }
.bonus-amount.neg { color: var(--red-dark); }

/* Messages */
.msg { padding: 10px 16px; border-radius: 4px; margin-bottom: 14px; font-size: 0.9rem; font-weight: 600; }
.msg-ok { background: rgba(58,100,40,0.2); border-left: 4px solid var(--green); color: var(--green-dark); }
.msg-err { background: rgba(168,48,48,0.2); border-left: 4px solid var(--red); color: var(--red-dark); }
.msg-info { background: rgba(200,164,74,0.2); border-left: 4px solid var(--ochre); color: var(--brown-mid); }

/* Utility */
.flex { display: flex; } .gap-10 { gap: 10px; } .gap-16 { gap: 16px; }
.flex-wrap { flex-wrap: wrap; } .align-center { align-items: center; }
.mb-10 { margin-bottom: 10px; } .mb-16 { margin-bottom: 16px; }
.mb-24 { margin-bottom: 24px; } .mt-16 { margin-top: 16px; }
.text-center { text-align: center; } .text-muted { color: var(--stone); font-size: 0.85rem; }
.text-sm { font-size: 0.85rem; } .hidden { display: none !important; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.player-colors { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
.color-swatch { width: 28px; height: 28px; border-radius: 50%; border: 3px solid transparent; cursor: pointer; transition: transform 0.15s, border-color 0.15s; }
.color-swatch.selected { border-color: var(--brown-deep); transform: scale(1.2); }
.color-swatch:hover { transform: scale(1.1); }
.ovr-x { overflow-x: auto; }

/* PRINT */
@media print {
  body { background: white !important; color: black !important; }
  nav, .no-print { display: none !important; }
  .screen { display: block !important; padding: 0 !important; max-width: 100% !important; }
  .screen:not(#screen-print) { display: none !important; }
  #screen-print { display: block !important; }
  .print-page { page-break-after: always; border: 3px solid #333; padding: 20px; margin: 0; min-height: 26cm; font-family: Georgia, serif; }
  .print-page:last-child { page-break-after: avoid; }
  .print-header { text-align: center; border-bottom: 3px double #666; padding-bottom: 12px; margin-bottom: 16px; }
  .print-header h1 { font-size: 1.6rem; letter-spacing: 2px; }
  .print-header .print-tribe { font-size: 1.1rem; color: #444; }
  .print-header .print-day { font-size: 0.9rem; color: #666; margin-top: 4px; }
  .print-info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px; }
  .print-info-box { border: 2px solid #888; border-radius: 4px; padding: 12px; text-align: center; }
  .print-info-box .label { font-size: 0.8rem; text-transform: uppercase; color: #666; }
  .print-info-box .value { font-size: 1.8rem; font-weight: bold; }
  .print-section { margin-bottom: 20px; page-break-inside: avoid; break-inside: avoid; }
  .print-section h3 { font-size: 1rem; text-transform: uppercase; letter-spacing: 1px; border-bottom: 2px solid #333; padding-bottom: 4px; margin-bottom: 12px;  page-break-after: avoid; break-after: avoid; }
  .print-role-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 10px; }
  .print-role-box { border: 2px solid #888; border-radius: 4px; padding: 10px; text-align: center; }
  .print-role-box .role-name { font-size: 0.75rem; text-transform: uppercase; color: #555; }
  .print-role-box .role-fill { height: 36px; border-bottom: 2px solid #333; margin-top: 8px; }
  .print-target-box { border: 2px solid #888; border-radius: 4px; padding: 10px; margin-bottom: 10px; }
  .print-target-box .role-name { font-size: 0.75rem; text-transform: uppercase; color: #555; }
  .print-target-box .role-fill { height: 30px; border-bottom: 2px solid #333; margin-top: 8px; }
  .print-spell-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; }
  .print-spell-box { border: 2px solid #888; border-radius: 4px; padding: 6px; text-align: center; }
  .print-spell-box .spell-name { font-size: 0.7rem; font-weight: bold; }
  .print-spell-box .spell-desc { font-size: 0.62rem; color: #555; margin-top: 2px; }
  .print-spell-box .spell-check { height: 20px; border: 2px solid #333; margin-top: 6px; border-radius: 3px; }
  .print-ref { font-size: 0.75rem; border: 1px solid #aaa; padding: 8px; border-radius: 4px; background: #f8f8f8; margin-top: 8px; }
  .print-ref table { width: 100%; border-collapse: collapse; }
  .print-ref td, .print-ref th { padding: 3px 6px; border: 1px solid #ccc; font-size: 0.7rem; }
  .print-ref th { background: #eee; }
  /* B&W overrides */
  * { color: black !important; background: white !important;
      border-color: #555 !important; box-shadow: none !important;
      text-shadow: none !important; }
  .result-plus, .result-minus, .supply-num { color: black !important; font-weight: bold; }
  a { color: black !important; text-decoration: none; }
  nav, .no-print, button { display: none !important; }
  .print-page { border: 2px solid black !important; }
}
.print-only { display: none; }
"""

HTML = """<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Praveka Tlupa</title>
<style>STYLE_PLACEHOLDER</style>
</head>
<body>

<nav>
  <div class="logo">Praveka Tlupa</div>
  <button onclick="showScreen('dashboard')" id="nav-dashboard">Přehled</button>
  <button onclick="showScreen('setup')" id="nav-setup">Nastavení</button>
  <button onclick="showScreen('round')" id="nav-round">Nový den</button>
  <button onclick="showScreen('results')" id="nav-results">Výsledky</button>
  <button onclick="showScreen('bonus')" id="nav-bonus">Bonusy</button>
  <div class="nav-right">
    <div class="nav-day" id="nav-day-info">Den 0/0</div>
    <button onclick="printPlayerHistories()" title="Tisk výsledků pro hráče (každý jen svůj)">Tisk pro hráče</button>
    <button onclick="printLeaderboardConditional()" title="Žebříček po dnech">Žebříček</button>
    <button onclick="printEventCards()" title="Tisknout karty událostí">Karty událostí</button>
    <button onclick="printGameRules()" title="Tisknout pravidla hry">Pravidla</button>
    <button onclick="exportData()" title="Exportovat JSON">Export</button>
    <button onclick="document.getElementById('importFile').click()" title="Importovat JSON">Import</button>
    <input type="file" id="importFile" accept=".json" onchange="importData(event)" class="hidden">
  </div>
</nav>

<!-- DASHBOARD -->
<div id="screen-dashboard" class="screen">
  <div class="page-title">Přehled kmene</div>
  <div class="page-sub" id="dash-sub"></div>
  <div class="grid-2 mb-16">
    <div class="card-dark card">
      <h2>Aktualni den</h2>
      <div id="dash-day-info" style="font-size:1.1rem;line-height:1.9"></div>
      <div class="mt-16 flex gap-10 flex-wrap">
        <button class="btn btn-ochre btn-lg" onclick="showScreen('round')" id="btn-new-day">Zahájit nový den</button>
        <button class="btn btn-primary" onclick="showScreen('results')" id="btn-see-results">Výsledky</button>
      </div>
    </div>
    <div class="card">
      <h2>Posledni udalost</h2>
      <div id="dash-last-event"></div>
    </div>
  </div>
  <div class="card">
    <h2>Žebříček tlup</h2>
    <div class="ovr-x">
      <table class="data-table">
        <thead><tr><th>#</th><th>Hráč / Tlupa</th><th>Zásoby</th><th>Členové tlupy</th><th>Bonusy</th></tr></thead>
        <tbody id="scoreboard-body"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- NASTAVENI -->
<div id="screen-setup" class="screen">
  <div class="page-title">Nastavení hry</div>
  <div class="page-sub">Parametry a hraci</div>
  <div id="setup-status" class="hidden"></div>
  <div id="setup-alert" class="hidden"></div>

  <div class="card">
    <h2>Zakladni parametry</h2>
    <div class="form-grid">
      <div class="form-group"><label>Název hry</label><input type="text" id="cfg-name"></div>
      <div class="form-group"><label>Počet herních dní</label><input type="number" id="cfg-days" min="1" max="60"></div>
      <div class="form-group"><label>Počáteční počet tlupy</label><input type="number" id="cfg-members" min="1"></div>
      <div class="form-group"><label>Počáteční zásoby tlupy</label><input type="number" id="cfg-supplies" min="0"></div>
      <div class="form-group"><label>Denní přírůstek tlupy</label><input type="number" id="cfg-growth" min="0"></div>
      <div class="form-group"><label>Zásoby na sběrače (ks/den)</label><input type="number" id="cfg-gather" min="1"></div>
      <div class="form-group"><label>Zásoby na lovce (ks/den)</label><input type="number" id="cfg-hunt" min="1"></div>
      <div class="form-group"><label>Zásoby pobertů (ks)</label><input type="number" id="cfg-raid" min="1"></div>
      <div class="form-group"><label>Výběr události</label>
        <select id="cfg-event-mode">
          <option value="random">Nahodne</option>
          <option value="manual">Administrator voli rucne</option>
        </select>
      </div>
    </div>
    <div class="mt-16">
      <button class="btn btn-ochre" onclick="saveSettings()" id="btn-save-settings">Ulozit nastaveni</button>
    </div>
  </div>

  <div class="card">
    <h2>Hráči</h2>
    <div id="players-list" class="mb-16"></div>
    <div class="card" style="background:rgba(196,168,90,0.1);border:2px dashed var(--parch-border)">
      <h3>Přidat hráče</h3>
      <div class="form-row">
        <div class="form-group"><label>Jméno hráče</label><input type="text" id="new-player-name" placeholder="Napr. Martin"></div>
        <div class="form-group"><label>Název tlupy</label><input type="text" id="new-tribe-name" placeholder="Napr. Medvedi"></div>
        <div class="form-group" style="flex:0"><label>Barva</label><div class="player-colors" id="color-picker"></div></div>
      </div>
      <div class="mt-16"><button class="btn btn-green" onclick="addPlayer()" id="btn-add-player">Přidat hráče</button></div>
    </div>
  </div>

  <div class="card">
    <h2>Start hry</h2>
    <p class="text-muted mb-10">Po zahájení nelze měnit hráče ani parametry.</p>
    <div class="flex gap-10 flex-wrap">
      <button class="btn btn-primary btn-lg" onclick="startGame()" id="btn-start-game">Zahájit hru</button>
      <button class="btn btn-red" onclick="resetGame()">Resetovat hru</button>
    </div>
  </div>
</div>

<!-- NOVY DEN -->
<div id="screen-round" class="screen">
  <div class="page-title">Zadani dne</div>
  <div class="page-sub" id="round-sub"></div>
  <div id="round-alert" class="hidden"></div>

  <div class="card mb-16">
    <h2>Událost dne</h2>
    <div class="form-row align-center">
      <div class="form-group" style="flex:0;min-width:260px">
        <label>Vybrana udalost</label>
        <select id="event-select" onchange="onEventChange()">
          <option value="none">zadna udalost</option>
          <option value="mamuti_ficak">Mamuti ficak</option>
          <option value="vzteklina">Vzteklina</option>
          <option value="bozi_vtipek">Bozi vtipek</option>
          <option value="pramlha">Pramlha</option>
          <option value="zatmeni_mesice">Zatmeni mesice</option>
        </select>
      </div>
      <button class="btn btn-primary" onclick="rollEvent()" id="btn-roll-event">Losovat</button>
    </div>
    <div id="event-info-box" class="event-info-box">
      <div class="ev-name" id="ev-info-name"></div>
      <div class="ev-desc" id="ev-info-desc"></div>
      <div class="ev-tags" id="ev-info-tags"></div>
    </div>
    <div class="form-group mt-16" style="max-width:500px">
      <label>Nazev / tema dne (nepovinne)</label>
      <input type="text" id="day-name-input" placeholder="Napr. Lov dinosauru, Prichod kruty zimy...">
    </div>
  </div>

  <div class="card">
    <h2>Rozhodnutí tlup</h2>
    <p class="text-muted mb-16">Zadej přiřazení členů pro každou tlupu dle odevzdaných lístků.</p>
    <div class="player-input-grid" id="player-inputs"></div>
    <div class="mt-16 flex gap-10">
      <button class="btn btn-ochre btn-lg" onclick="submitRound()">Vyhodnotit den</button>
    </div>
  </div>
</div>

<!-- VYSLEDKY -->
<div id="screen-results" class="screen">
  <div class="page-title">Výsledky</div>
  <div id="results-sub" class="page-sub"></div>
  <div id="results-container"></div>
</div>

<!-- BONUSY -->
<div id="screen-bonus" class="screen">
  <div class="page-title">Bonusove suroviny</div>
  <div class="page-sub">Udelovani bonusu za taborove aktivity</div>
  <div class="card">
    <h2>Přidat bonus</h2>
    <div class="form-row align-center">
      <div class="form-group"><label>Hráč</label><select id="bonus-player"></select></div>
      <div class="form-group" style="min-width:120px"><label>Zásoby</label><input type="number" id="bonus-amount" value="50"></div>
      <div class="form-group"><label>Aktivita / popis</label><input type="text" id="bonus-desc" placeholder="Škrábání brambor..."></div>
      <button class="btn btn-ochre" onclick="addBonus()">Pridelit</button>
    </div>
  </div>
  <div class="card">
    <h2>Historie bonusů</h2>
    <div id="bonus-history"></div>
  </div>
</div>

<!-- TISK -->
<div id="screen-print" class="screen">
  <div class="no-print flex gap-10 mb-24">
    <button class="btn btn-primary" onclick="window.print()">Tisknout</button>
    <button class="btn btn-ochre" onclick="history.back()">Zpet</button>
  </div>
  <div id="print-content"></div>
</div>

</body>
</html>"""

JS = r"""
// ======================================================
//  CONSTANTS
// ======================================================
const STORAGE_KEY = 'pravekaTlupa';

const PLAYER_COLORS = [
  '#c0392b','#e67e22','#f1c40f','#2ecc71','#1abc9c',
  '#3498db','#9b59b6','#e91e63','#607d8b','#795548',
  '#00bcd4','#8bc34a','#ff5722','#009688','#673ab7',
  '#ff9800','#4caf50','#f44336','#2196f3','#9c27b0'
];

const EVENTS = {
  none: {
    name: 'Zadna udalost',
    icon: '--',
    desc: 'Tento den neprobehla zadna zvlastni udalost. Vsechny role fungujou standardne.',
    neg: [],
    pos: [],
  },
  mamuti_ficak: {
    name: 'Mamutí fičák',
    icon: 'VITR',
    desc: 'Prudký vítr znemožňuje sběr plodin -- výnos sběračů je poloviční. Hlídači jsou naopak odolnější a brání tábor dvojnásobně.',
    neg: ['Sběrači mají výnos × ½ (poloviční)'],
    pos: ['Hlídači mají efektivitu × 2 (dvojnásobnou)'],
  },
  vzteklina: {
    name: 'Vzteklina',
    icon: 'NAKAZA',
    desc: 'Nebezpečná nákaza zasahuje lovce -- polovina z nich zahyne ještě před lovem (zaokrouhleno dolů). Pobertové jsou agresivnější -- každý vyřadí 2 hlídače místo 1.',
    neg: ['Polovina lovců zahyne'],
    pos: ['Síla pobertů x2 (vyřadí 2 hlídače)'],
  },
  bozi_vtipek: {
    name: 'Boží vtípek',
    icon: 'VTIPEK',
    desc: 'Šamanovo kouzlo má opačný efekt (x1/2 místo x2). Každý hráč dostane prémii za pořadí v žebříčku: den × 100 × pořadí (1. místo = nejvíce zásob = nejmenší bonus).',
    neg: ['Kouzlo šamana obráceno (x1/2)'],
    pos: ['Prémie: den × 100 × pořadí v žebříčku'],
  },
  pramlha: {
    name: 'Pramlha',
    icon: 'MLHA',
    desc: 'Hustá mlha -- všichni pobertové se ztratí a zahynou před dosažením cíle. Žádná loupež neprobíhá. Lovci se lépe orientují a uloví dvojnásobek.',
    neg: ['Všichni pobertové zahynou před dosažením cíle, žádná loupež'],
    pos: ['Lovci mají výnos × 2 (dvojnásobný)'],
  },
  zatmeni_mesice: {
    name: 'Zatmění měsíce',
    icon: 'TMA',
    desc: 'Tma znemožňuje hlídačům hlídat -- jejich efektivita je nulová, všichni pobertové projdou bez boje. Sběrači využijí noční klid přírody a seberou dvojnásobek.',
    neg: ['Hlídači nefungují, efektivita = 0'],
    pos: ['Sběrači mají výnos × 2 (dvojnásobný)'],
  },
};

const SPELLS = {
  plodnost:   { name: 'Plodnost',   icon: '[P]', desc: 'Přírůstek x2' },
  hojnost:    { name: 'Hojnost',    icon: '[H]', desc: 'Síla sběračů x2' },
  urputnost:  { name: 'Urputnost',  icon: '[U]', desc: 'Síla lovců x2' },
  chamtivost: { name: 'Chamtivost', icon: '[C]', desc: 'Síla pobertů x2' },
  obrana:     { name: 'Obrana',     icon: '[O]', desc: 'Síla hlídačů x2' },
};

// ======================================================
//  STATE
// ======================================================
function defaultState() {
  return {
    started: false, currentDay: 0,
    settings: {
      gameName: 'Praveka Tlupa 2026', totalDays: 10,
      startingMembers: 10, startingSupplies: 500, dailyNewMembers: 2,
      gatherAmount: 2, huntAmount: 2, raidCarry: 4, eventMode: 'manual',
    },
    players: [], bonuses: [], rounds: [], lastResults: null,
  };
}

function loadState() {
  try { const r = localStorage.getItem(STORAGE_KEY); return r ? JSON.parse(r) : defaultState(); }
  catch(e) { return defaultState(); }
}
function saveState(s) { localStorage.setItem(STORAGE_KEY, JSON.stringify(s)); }

let state = loadState();

// ======================================================
//  PLAYER HELPERS
// ======================================================
function getPlayerRoundState(state, pid, ri) {
  if (ri < 0 || state.rounds.length === 0)
    return { members: state.settings.startingMembers, supplies: state.settings.startingSupplies };
  const r = state.rounds[ri];
  if (!r || !r.playerStates[pid])
    return { members: state.settings.startingMembers, supplies: state.settings.startingSupplies };
  return { members: r.playerStates[pid].endMembers, supplies: r.playerStates[pid].endSupplies };
}
function getPlayerCurrentBase(pid) { return getPlayerRoundState(state, pid, state.rounds.length - 1); }
function getPlayerBonusTotal(pid) {
  return state.bonuses.filter(b => b.playerId === pid).reduce((s, b) => s + b.amount, 0);
}
function getPlayerTotalSupplies(pid) { return getPlayerCurrentBase(pid).supplies + getPlayerBonusTotal(pid); }
function getPlayerCurrentMembers(pid) { return getPlayerCurrentBase(pid).members; }
function getSortedPlayers() {
  return [...state.players].sort((a, b) => getPlayerTotalSupplies(b.id) - getPlayerTotalSupplies(a.id));
}
function getPrevRankMap() {
  if (state.rounds.length < 2) return {};
  const ri = state.rounds.length - 2;
  const sup = {};
  state.players.forEach(p => { sup[p.id] = getPlayerRoundState(state, p.id, ri).supplies; });
  const sorted = [...state.players].sort((a,b) => sup[b.id] - sup[a.id]);
  const map = {}; sorted.forEach((p, i) => map[p.id] = i + 1);
  return map;
}

// ======================================================
//  MULTIPLIERS
// ======================================================
function spellMult(mySpell, target, event) {
  if (mySpell !== target) return 1;
  return event === 'bozi_vtipek' ? 0.5 : 2;
}
function gatherMult(spell, event) {
  return spellMult(spell,'hojnost',event) * (event==='mamuti_ficak'?0.5:event==='zatmeni_mesice'?2:1);
}
function huntMult(spell, event) {
  return spellMult(spell,'urputnost',event) * (event==='pramlha'?2:1);
}
function guardMult(spell, event) {
  return spellMult(spell,'obrana',event) * (event==='mamuti_ficak'?2:event==='zatmeni_mesice'?0:1);
}
function raidCarryMult(spell, event) { return spellMult(spell,'chamtivost',event); }
function membersMult(spell, event) { return spellMult(spell,'plodnost',event); }

// ======================================================
//  CALCULATE ROUND
// ======================================================
function calculateRound(dayNum, event, inputs) {
  const s = state.settings;
  const results = {};
  for (const p of state.players) {
    const base = getPlayerCurrentBase(p.id);
    results[p.id] = {
      startMembers: base.members,
      startSupplies: base.supplies + getPlayerBonusTotal(p.id),
      gathered:0, hunted:0, huntersLost:0, guardsLost:0,
      raidersLost:0, suppliesStolen:0, suppliesGained:0, bvBonus:0, newMembers:0,
      endMembers:0, endSupplies:0, raidDetail:[],
    };
  }
  // Gather
  for (const p of state.players)
    results[p.id].gathered = Math.floor(inputs[p.id].gatherers * s.gatherAmount * gatherMult(inputs[p.id].spell, event));
  // Hunt
  for (const p of state.players) {
    const inp = inputs[p.id];
    const hl = event==='vzteklina' ? Math.floor(inp.hunters/2) : 0;
    results[p.id].huntersLost = hl;
    results[p.id].hunted = Math.floor((inp.hunters-hl) * s.huntAmount * huntMult(inp.spell, event));
  }
  // Bozi vtipek bonus
  if (event === 'bozi_vtipek') {
    [...state.players].sort((a,b) => getPlayerTotalSupplies(b.id) - getPlayerTotalSupplies(a.id))
      .forEach((p, i) => { results[p.id].bvBonus = dayNum * 100 * (i+1); });
  }
  // Raiders
  if (event === 'pramlha') {
    for (const p of state.players) results[p.id].raidersLost = inputs[p.id].raiders;
  } else {
    const byTarget = {};
    for (const p of state.players) {
      const inp = inputs[p.id];
      if (inp.raiders>0 && inp.raidTarget && inp.raidTarget !== p.id) {
        if (!byTarget[inp.raidTarget]) byTarget[inp.raidTarget] = [];
        byTarget[inp.raidTarget].push({ id:p.id, raiders:inp.raiders, spell:inp.spell, score:getPlayerTotalSupplies(p.id) });
      }
    }
    for (const [tid, atks] of Object.entries(byTarget)) {
      atks.sort((a,b) => b.raiders - a.raiders || a.score - b.score);
      const ti = inputs[tid];
      const gm = guardMult(ti.spell, event);
      let effG = ti.guards * gm;
      let physG = ti.guards;
      const rStr = event==='vzteklina' ? 2 : 1;
      let avail = results[tid].startSupplies + results[tid].gathered + results[tid].hunted + results[tid].bvBonus;
      for (const atk of atks) {
        if (!atk.raiders || avail <= 0) continue;
        const effUsed = Math.min(effG, atk.raiders * rStr);
        const killed = Math.floor(effUsed / rStr);
        const surv = Math.max(0, atk.raiders - killed);
        const physK = gm > 0 ? Math.min(physG, Math.ceil(effUsed / Math.max(gm, 0.5))) : 0;
        effG = Math.max(0, effG - effUsed);
        physG = Math.max(0, physG - physK);
        results[atk.id].raidersLost += atk.raiders - surv;
        const cm = raidCarryMult(atk.spell, event);
        const stolen = Math.min(surv * Math.floor(s.raidCarry * cm), avail);
        avail = Math.max(0, avail - stolen);
        results[tid].guardsLost += physK;
        results[tid].suppliesStolen += stolen;
        const tName = state.players.find(p=>p.id===tid)?.tribeName||tid;
        const aName = state.players.find(p=>p.id===atk.id)?.tribeName||atk.id;
        results[tid].raidDetail.push(`${aName}: ${atk.raiders} pobertu -> ${surv} prezilo -> ukradeno ${stolen} zasob`);
        results[atk.id].raidDetail.push(`-> ${tName}: ${surv} prezivsi, ukradeno ${stolen}`);
        results[atk.id].suppliesGained += stolen;
      }
    }
  }
  // New members & end state
  for (const p of state.players) {
    const nm = Math.floor(state.settings.dailyNewMembers * membersMult(inputs[p.id].spell, event));
    results[p.id].newMembers = nm;
    const deaths = results[p.id].huntersLost + results[p.id].guardsLost + results[p.id].raidersLost;
    results[p.id].endMembers = Math.max(0, results[p.id].startMembers - deaths + nm);
    results[p.id].endSupplies = Math.max(0,
      results[p.id].startSupplies + results[p.id].gathered + results[p.id].hunted +
      results[p.id].bvBonus - results[p.id].suppliesStolen + results[p.id].suppliesGained
    );
  }
  return results;
}

// ======================================================
//  NAVIGATION
// ======================================================
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('nav button[id^="nav-"]').forEach(b => b.classList.remove('active'));
  const el = document.getElementById('screen-'+id);
  const nb = document.getElementById('nav-'+id);
  if (el) el.classList.add('active');
  if (nb) nb.classList.add('active');
  // Clear stale print content when leaving print screen
  if (id !== 'print') {
    const pc = document.getElementById('print-content');
    if (pc) pc.innerHTML = '';
  }
  updateNavDay();
  if (id==='dashboard') renderDashboard();
  else if (id==='setup') renderSetup();
  else if (id==='round') renderRound();
  else if (id==='results') renderResults();
  else if (id==='bonus') renderBonus();
}
function updateNavDay() {
  const d = state.currentDay || state.rounds.length;
  document.getElementById('nav-day-info').textContent = `Den ${d}/${state.settings.totalDays}`;
}

// ======================================================
//  DASHBOARD
// ======================================================
function renderDashboard() {
  updateNavDay();
  document.getElementById('dash-sub').textContent = state.settings.gameName;
  const di = document.getElementById('dash-day-info');
  if (!state.started) {
    di.innerHTML = '<span class="text-muted">Hra nebyla zahájena. Přejdi na Nastavení.</span>';
  } else {
    di.innerHTML =
      `<strong>Herni den:</strong> ${state.currentDay} z ${state.settings.totalDays}<br>` +
      `<strong>Hráčů:</strong> ${state.players.length}<br>` +
      (state.currentDay >= state.settings.totalDays
        ? '<span style="color:var(--ochre);font-weight:bold">Hra skoncila!</span>'
        : `<span class="text-muted">Zbývají ${state.settings.totalDays - state.currentDay} dní</span>`);
  }
  document.getElementById('btn-new-day').disabled = !state.started || state.currentDay >= state.settings.totalDays;
  const lastR = state.rounds[state.rounds.length-1];
  const evDiv = document.getElementById('dash-last-event');
  if (lastR) {
    const ev = EVENTS[lastR.event]||EVENTS.none;
    evDiv.innerHTML = `<div style="font-size:1.1rem;font-weight:bold;margin-bottom:6px">${ev.name}</div>
      <div class="text-muted text-sm">${ev.desc}</div>`;
  } else {
    evDiv.innerHTML = '<span class="text-muted">Zadny den zatim neprobehel</span>';
  }
  // Scoreboard
  const sorted = getSortedPlayers();
  const prevMap = getPrevRankMap();
  const tbody = document.getElementById('scoreboard-body');
  tbody.innerHTML = '';
  sorted.forEach((p, i) => {
    const supplies = getPlayerTotalSupplies(p.id);
    const members = getPlayerCurrentMembers(p.id);
    const bonuses = getPlayerBonusTotal(p.id);
    const pr = prevMap[p.id];
    const tr = document.createElement('tr');
    tr.className = i===0?'rank-1':i===1?'rank-2':i===2?'rank-3':'';
    tr.innerHTML = `
      <td class="rank">${i+1}</td>
      <td><span class="color-dot" style="background:${p.color}"></span> ${esc(p.name)}<br>
          <small class="text-muted">${esc(p.tribeName)}</small></td>
      <td class="supply-num">${supplies}</td>
      <td>${members}</td>
      <td>${bonuses!==0?(bonuses>0?'+':'')+bonuses:'--'}</td>
    `;
    tbody.appendChild(tr);
  });
}

// ======================================================
//  SETUP
// ======================================================
function renderSetup() {
  const cfg = state.settings;
  document.getElementById('cfg-name').value = cfg.gameName;
  document.getElementById('cfg-days').value = cfg.totalDays;
  document.getElementById('cfg-members').value = cfg.startingMembers;
  document.getElementById('cfg-supplies').value = cfg.startingSupplies;
  document.getElementById('cfg-growth').value = cfg.dailyNewMembers;
  document.getElementById('cfg-gather').value = cfg.gatherAmount;
  document.getElementById('cfg-hunt').value = cfg.huntAmount;
  document.getElementById('cfg-raid').value = cfg.raidCarry;
  document.getElementById('cfg-event-mode').value = cfg.eventMode;

  // Status banner
  const statusDiv = document.getElementById('setup-status');
  if (state.started) {
    statusDiv.className = 'status-banner running';
    statusDiv.innerHTML = `
      <div class="status-icon">PLAY</div>
      <div>
        <div>Hra probiha -- Den ${state.currentDay} z ${state.settings.totalDays} | ${state.players.length} hracu</div>
        <div class="status-detail">Parametry ani hraci nelze měnit po zahájení. Pro zmeny resetuj hru.</div>
      </div>`;
    statusDiv.classList.remove('hidden');
  } else {
    statusDiv.className = 'status-banner idle';
    statusDiv.innerHTML = `
      <div class="status-icon">STOP</div>
      <div>
        <div>Hra dosud nebyla zahajana.</div>
        <div class="status-detail">Pridej hrace, nastav parametry a klikni Zahájit hru.</div>
      </div>`;
    statusDiv.classList.remove('hidden');
  }

  // Start button
  const btn = document.getElementById('btn-start-game');
  btn.disabled = state.started;
  btn.textContent = state.started ? 'Hra už probíhá' : 'Zahájit hru';

  // Lock form fields if started
  const lock = state.started;
  ['cfg-name','cfg-days','cfg-members','cfg-supplies','cfg-growth','cfg-gather','cfg-hunt','cfg-raid','cfg-event-mode']
    .forEach(id => { const el = document.getElementById(id); if (el) el.disabled = lock; });
  document.getElementById('btn-save-settings').disabled = lock;
  document.getElementById('btn-add-player').disabled = lock;

  renderColorPicker();
  renderPlayersList();
}

function renderColorPicker() {
  const cp = document.getElementById('color-picker');
  cp.innerHTML = '';
  PLAYER_COLORS.forEach(c => {
    const div = document.createElement('div');
    div.className = 'color-swatch'; div.style.background = c; div.title = c;
    div.onclick = () => {
      document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('selected'));
      div.classList.add('selected');
    };
    cp.appendChild(div);
  });
  const used = new Set(state.players.map(p => p.color));
  const first = PLAYER_COLORS.find(c => !used.has(c)) || PLAYER_COLORS[0];
  const sw = [...cp.querySelectorAll('.color-swatch')].find(s => s.title === first);
  if (sw) sw.classList.add('selected');
}

function getSelectedColor() {
  const sw = document.querySelector('.color-swatch.selected');
  return sw ? sw.title : PLAYER_COLORS[0];
}

function renderPlayersList() {
  const el = document.getElementById('players-list');
  if (state.players.length === 0) {
    el.innerHTML = '<p class="text-muted">Zatím žádní hráči.</p>'; return;
  }
  el.innerHTML = `<table class="data-table">
    <thead><tr><th>Barva</th><th>Jmeno</th><th>Tlupa</th><th>Akce</th></tr></thead>
    <tbody>${state.players.map(p => `
      <tr><td><span class="color-dot" style="background:${p.color}"></span></td>
          <td>${esc(p.name)}</td><td>${esc(p.tribeName)}</td>
          <td><button class="btn btn-red btn-sm" onclick="removePlayer('${p.id}')" ${state.started?'disabled':''}>X</button></td></tr>`)
    .join('')}</tbody></table>`;
}

function saveSettings() {
  if (state.started) return;
  state.settings.gameName = document.getElementById('cfg-name').value.trim() || 'Praveka Tlupa';
  state.settings.totalDays = parseInt(document.getElementById('cfg-days').value)||10;
  state.settings.startingMembers = parseInt(document.getElementById('cfg-members').value)||10;
  state.settings.startingSupplies = parseInt(document.getElementById('cfg-supplies').value)||0;
  state.settings.dailyNewMembers = parseInt(document.getElementById('cfg-growth').value)||2;
  state.settings.gatherAmount = parseInt(document.getElementById('cfg-gather').value)||2;
  state.settings.huntAmount = parseInt(document.getElementById('cfg-hunt').value)||2;
  state.settings.raidCarry = parseInt(document.getElementById('cfg-raid').value)||4;
  state.settings.eventMode = document.getElementById('cfg-event-mode').value;
  saveState(state);
  showMsg('setup-alert', 'Nastavení uloženo.', 'ok');
  document.getElementById('setup-alert').scrollIntoView({behavior:'smooth',block:'center'});
  updateNavDay();
}

function addPlayer() {
  if (state.started) return;
  const name = document.getElementById('new-player-name').value.trim();
  const tribe = document.getElementById('new-tribe-name').value.trim();
  if (!name||!tribe) { showMsg('setup-alert','Zadej jméno hráče i název tlupy.','err'); return; }
  if (state.players.length >= 20) { showMsg('setup-alert','Maximální počet hráčů je 20.','err'); return; }
  state.players.push({ id:'p'+Date.now(), name, tribeName:tribe, color:getSelectedColor() });
  document.getElementById('new-player-name').value = '';
  document.getElementById('new-tribe-name').value = '';
  saveState(state);
  renderColorPicker();
  renderPlayersList();
  showMsg('setup-alert', `Hrac ${name} (${tribe}) pridan.`, 'ok');
}

function removePlayer(id) {
  if (state.started) return;
  state.players = state.players.filter(p => p.id !== id);
  saveState(state); renderPlayersList();
}

function startGame() {
  if (state.started) { showMsg('setup-alert','Hra uz probiha.','info'); return; }
  if (state.players.length < 2) { showMsg('setup-alert','Potřeba alespoň 2 hráči.','err'); return; }
  state.started = true; state.currentDay = 0;
  state.rounds = []; state.bonuses = []; state.lastResults = null;
  saveState(state);
  renderSetup(); // re-render to show status
  showMsg('setup-alert','Hra zahájena! Přejdi na Nový den.','ok');
  updateNavDay();
}

function resetGame() {
  if (!confirm('Opravdu resetovat celou hru? Všechna data budou smazána.')) return;
  state = defaultState(); saveState(state); showScreen('setup');
}

// ======================================================
//  ROUND INPUT
// ======================================================
function renderRound() {
  if (!state.started) {
    const al = document.getElementById('round-alert');
    al.className = 'msg msg-info'; al.textContent = 'Nejprve zahaj hru v Nastavení.'; al.classList.remove('hidden');
    document.getElementById('player-inputs').innerHTML = '';
    return;
  }
  if (state.currentDay >= state.settings.totalDays) {
    const al = document.getElementById('round-alert');
    al.className = 'msg msg-ok';
    al.textContent = 'Hra skončila! Všechny dny byly odehrány. Přechod na výsledky.';
    al.classList.remove('hidden');
    document.getElementById('player-inputs').innerHTML = '';
    document.querySelector('#screen-round .btn-ochre').disabled = true;
    setTimeout(() => showScreen('results'), 1500);
    return;
  }
  document.getElementById('round-alert').classList.add('hidden');
  document.querySelector('#screen-round .btn-ochre').disabled = false;
  const nextDay = state.currentDay + 1;
  document.getElementById('round-sub').textContent =
    `Den ${nextDay} z ${state.settings.totalDays} -- ${state.settings.gameName}`;
  if (state.settings.eventMode === 'random') rollEvent();
  document.getElementById('btn-roll-event').style.display =
    state.settings.eventMode === 'random' ? 'inline-flex' : 'none';
  renderPlayerInputs();
}

function rollEvent() {
  const keys = Object.keys(EVENTS);
  document.getElementById('event-select').value = keys[Math.floor(Math.random()*keys.length)];
  onEventChange();
}

function onEventChange() {
  const key = document.getElementById('event-select').value;
  const ev = EVENTS[key];
  const box = document.getElementById('event-info-box');
  if (!ev || key === 'none') { box.classList.remove('visible'); return; }
  document.getElementById('ev-info-name').textContent = ev.name;
  document.getElementById('ev-info-desc').textContent = ev.desc;
  const tags = document.getElementById('ev-info-tags');
  tags.innerHTML =
    ev.neg.map(t => `<span class="ev-tag ev-tag-neg">- ${t}</span>`).join('') +
    ev.pos.map(t => `<span class="ev-tag ev-tag-pos">+ ${t}</span>`).join('');
  box.classList.add('visible');
}

function renderPlayerInputs() {
  const container = document.getElementById('player-inputs');
  container.innerHTML = '';
  for (const p of state.players) {
    const members = getPlayerCurrentMembers(p.id);
    const supplies = getPlayerTotalSupplies(p.id);
    const div = document.createElement('div');
    div.className = 'player-input-card';
    div.innerHTML = `
      <div class="pname"><span class="color-dot" style="background:${p.color}"></span> ${esc(p.name)} -- ${esc(p.tribeName)}</div>
      <div class="pinfo">Členů: ${members} | Zásoby: ${supplies}</div>
      <div class="input-roles">
        <div class="role-input"><label>Sběrači</label>
          <input type="number" id="inp-${p.id}-gatherers" min="0" value="0" oninput="updateTotal('${p.id}')"></div>
        <div class="role-input"><label>Lovci</label>
          <input type="number" id="inp-${p.id}-hunters" min="0" value="0" oninput="updateTotal('${p.id}')"></div>
        <div class="role-input"><label>Hlídači</label>
          <input type="number" id="inp-${p.id}-guards" min="0" value="0" oninput="updateTotal('${p.id}')"></div>
        <div class="role-input"><label>Pobertové</label>
          <input type="number" id="inp-${p.id}-raiders" min="0" value="0" oninput="updateTotal('${p.id}')"></div>
        <div class="role-input full-width-input"><label>Cíl útoku</label>
          <select id="inp-${p.id}-target">
            <option value="">-- Neutočit --</option>
            ${state.players.filter(q=>q.id!==p.id).map(q=>`<option value="${q.id}">${esc(q.name)} / ${esc(q.tribeName)}</option>`).join('')}
          </select></div>
        <div class="role-input full-width-input"><label>Šamanovo kouzlo</label>
          <select id="inp-${p.id}-spell">
            ${Object.entries(SPELLS).map(([k,v])=>`<option value="${k}">${v.icon} ${v.name} -- ${v.desc}</option>`).join('')}
          </select></div>
      </div>
      <div class="total-bar total-ok" id="total-${p.id}">Prirazeno: 0 / ${members}</div>`;
    container.appendChild(div);
  }
}

function updateTotal(pid) {
  const members = getPlayerCurrentMembers(pid);
  const g = parseInt(document.getElementById(`inp-${pid}-gatherers`)?.value)||0;
  const h = parseInt(document.getElementById(`inp-${pid}-hunters`)?.value)||0;
  const d = parseInt(document.getElementById(`inp-${pid}-guards`)?.value)||0;
  const r = parseInt(document.getElementById(`inp-${pid}-raiders`)?.value)||0;
  const total = g+h+d+r;
  const bar = document.getElementById(`total-${pid}`);
  bar.textContent = `Přiřazeno: ${total} / ${members}`;
  bar.className = 'total-bar ' + (total > members ? 'total-warn' : 'total-ok');

  // Highlight raid target when raiders > 0 but no target set
  const targetSel = document.getElementById(`inp-${pid}-target`);
  if (targetSel) {
    const needsTarget = r > 0 && !targetSel.value;
    targetSel.style.borderColor = needsTarget ? 'var(--red)' : '';
    targetSel.style.background = needsTarget ? 'rgba(168,48,48,0.12)' : '';
    // update or remove warning
    let warn = document.getElementById(`raid-warn-${pid}`);
    if (needsTarget) {
      if (!warn) {
        warn = document.createElement('div');
        warn.id = `raid-warn-${pid}`;
        warn.style.cssText = 'font-size:0.78rem;color:var(--red-dark);margin-top:3px;font-weight:600';
        warn.textContent = 'Pozor: zadej cíl útoku pobertů!';
        targetSel.parentNode.appendChild(warn);
      }
    } else if (warn) {
      warn.remove();
    }
  }
}

function getInputs() {
  const inputs = {};
  for (const p of state.players) {
    inputs[p.id] = {
      gatherers: parseInt(document.getElementById(`inp-${p.id}-gatherers`)?.value)||0,
      hunters:   parseInt(document.getElementById(`inp-${p.id}-hunters`)?.value)||0,
      guards:    parseInt(document.getElementById(`inp-${p.id}-guards`)?.value)||0,
      raiders:   parseInt(document.getElementById(`inp-${p.id}-raiders`)?.value)||0,
      raidTarget: document.getElementById(`inp-${p.id}-target`)?.value||'',
      spell:     document.getElementById(`inp-${p.id}-spell`)?.value||'hojnost',
    };
  }
  return inputs;
}

function submitRound() {
  if (!state.started || state.currentDay >= state.settings.totalDays) return;
  const inputs = getInputs();
  for (const p of state.players) {
    const members = getPlayerCurrentMembers(p.id);
    const inp = inputs[p.id];
    const total = inp.gatherers + inp.hunters + inp.guards + inp.raiders;
    if (total > members) { showMsg('round-alert', `${p.name}: přiřazeno ${total}, ale tlupa má jen ${members} členů.`, 'err'); return; }
    if (inp.raiders > 0 && !inp.raidTarget) {
      showMsg('round-alert', `${p.name} má ${inp.raiders} pobertů, ale nemá zadaný cíl útoku! Zvol cíl nebo poberty přesuň jinam.`, 'err');
      return;
    }
  }
  const dayNum = state.currentDay + 1;
  const event = document.getElementById('event-select').value || 'none';
  const dayName = document.getElementById('day-name-input')?.value?.trim() || '';
  const results = calculateRound(dayNum, event, inputs);
  const playerStates = {};
  for (const p of state.players) {
    playerStates[p.id] = {
      startMembers: results[p.id].startMembers, startSupplies: results[p.id].startSupplies,
      assignments: inputs[p.id],
      results: {
        gathered: results[p.id].gathered, hunted: results[p.id].hunted,
        huntersLost: results[p.id].huntersLost, guardsLost: results[p.id].guardsLost,
        raidersLost: results[p.id].raidersLost, suppliesStolen: results[p.id].suppliesStolen,
        bvBonus: results[p.id].bvBonus, newMembers: results[p.id].newMembers,
        raidDetail: results[p.id].raidDetail || [],
        suppliesGained: results[p.id].suppliesGained || 0,
      },
      endMembers: results[p.id].endMembers, endSupplies: results[p.id].endSupplies,
    };
  }
  state.rounds.push({ day: dayNum, event, dayName, playerStates });
  state.currentDay = dayNum;
  state.lastResults = { day: dayNum, event, results };
  saveState(state);
  showScreen('results');
}

// ======================================================
//  RESULTS -- full history
// ======================================================
function renderResults() {
  const container = document.getElementById('results-container');
  if (state.rounds.length === 0) {
    document.getElementById('results-sub').textContent = 'Zadne vysledky zatim';
    container.innerHTML = '<div class="card"><p class="text-muted">Zadne dny zatim neprobehl.</p></div>';
    return;
  }
  document.getElementById('results-sub').textContent =
    `${state.settings.gameName} -- celkem ${state.rounds.length} dni`;

  let html = '';
  // Newest first
  for (let i = state.rounds.length - 1; i >= 0; i--) {
    const round = state.rounds[i];
    const isLatest = (i === state.rounds.length - 1);
    html += buildDayBlock(round, isLatest);
  }
  html += `<div class="flex gap-10 mt-16">
    <button class="btn btn-ochre btn-lg" onclick="showScreen('dashboard')">Na přehled</button>
  </div>`;
  container.innerHTML = html;
}

function buildDayBlock(round, isLatest) {
  const ev = EVENTS[round.event] || EVENTS.none;
  const sorted = [...state.players].sort((a,b) =>
    round.playerStates[b.id].endSupplies - round.playerStates[a.id].endSupplies
  );

  const evBannerClass = round.event === 'none' ? 'results-event-banner ev-none' : 'results-event-banner';
  const negTags = ev.neg.map(t=>`<span class="ev-tag ev-tag-neg">- ${t}</span>`).join(' ');
  const posTags = ev.pos.map(t=>`<span class="ev-tag ev-tag-pos">+ ${t}</span>`).join(' ');

  // Summary table rows
  let tableRows = '';
  sorted.forEach((p, i) => {
    const ps = round.playerStates[p.id];
    const r = ps.results;
    const deaths = r.huntersLost + r.guardsLost + r.raidersLost;
    const asgn = ps.assignments;
    const sp = SPELLS[asgn?.spell];
    tableRows += `<tr class="${i===0?'rank-1':i===1?'rank-2':i===2?'rank-3':''}">
      <td class="rank">${i+1}</td>
      <td><span class="color-dot" style="background:${p.color}"></span> ${esc(p.name)}<br>
          <small class="text-muted">${esc(p.tribeName)}</small>
          ${sp?`<br><small>${sp.icon} ${sp.name}</small>`:''}
          ${asgn?`<br><small class="text-muted">S:${asgn.gatherers} L:${asgn.hunters} H:${asgn.guards} P:${asgn.raiders}</small>`:''}
      </td>
      <td class="result-plus">${r.gathered>0?'+'+r.gathered:0}</td>
      <td class="result-plus">${r.hunted>0?'+'+r.hunted:0}</td>
      <td class="${r.bvBonus>0?'result-plus':''}">${r.bvBonus>0?'+'+r.bvBonus:'--'}</td>
      <td class="${r.suppliesGained>0?'result-plus':''}">${r.suppliesGained>0?'+'+r.suppliesGained:'--'}</td>
      <td class="${r.suppliesStolen>0?'result-minus':''}">${r.suppliesStolen>0?'-'+r.suppliesStolen:'--'}</td>
      <td class="${deaths>0?'result-minus':''}">${deaths>0?'-'+deaths:'--'}</td>
      <td class="result-plus">+${r.newMembers}</td>
      <td class="supply-num">${ps.endSupplies}</td>
      <td class="${getPlayerBonusTotal(p.id)>0?'result-plus':''}">${getPlayerBonusTotal(p.id)>0?'+'+getPlayerBonusTotal(p.id):'--'}</td>
      <td>${ps.endMembers}</td>
    </tr>`;
  });

  // Detail cards (only for latest or when expanded)
  let detailCards = '';
  if (isLatest) {
    detailCards = `<div class="player-input-grid" style="margin-top:14px">`;
    for (const p of state.players) {
      const ps = round.playerStates[p.id];
      const r = ps.results;
      const asgn = ps.assignments;
      const sp = asgn ? SPELLS[asgn.spell] : null;
      const deaths = r.huntersLost + r.guardsLost + r.raidersLost;
      detailCards += `
      <div class="player-input-card">
        <div class="pname"><span class="color-dot" style="background:${p.color}"></span> ${esc(p.name)} -- ${esc(p.tribeName)}</div>
        ${sp?`<div class="mb-10"><span class="badge badge-spell">${sp.icon} ${sp.name} -- ${sp.desc}</span></div>`:''}
        ${asgn?`<div class="text-sm text-muted mb-10">Sberaci ${asgn.gatherers} | Lovci ${asgn.hunters} | Hlídači ${asgn.guards} | Pobertové ${asgn.raiders}</div>`:''}
        <div style="font-size:0.88rem;line-height:1.9">
          ${r.suppliesGained>0?`<span class="result-plus">+${r.suppliesGained} ukradeno</span><br>`:''}
          <span class="result-plus">+${r.gathered} ze sberu</span><br>
          <span class="result-plus">+${r.hunted} z lovu</span>
          ${r.huntersLost>0?`<span class="result-minus"> (-${r.huntersLost} lovců zahynulo)</span>`:''}
          <br>${r.bvBonus>0?`<span class="result-plus">+${r.bvBonus} premie (Bozi vtipek)</span><br>`:''}
          ${r.suppliesStolen>0?`<span class="result-minus">-${r.suppliesStolen} ukradeno</span><br>`:''}
          ${r.guardsLost>0?`<span class="result-minus">-${r.guardsLost} hlídačů zahynulo</span><br>`:''}
          ${r.raidersLost>0?`<span class="result-minus">-${r.raidersLost} pobertu zahynulo</span><br>`:''}
          <span class="result-plus">+${r.newMembers} novych clenu</span>
        </div>
        ${(r.raidDetail||[]).length>0?`<div class="result-detail mt-16">${r.raidDetail.map(esc).join('<br>')}</div>`:''}
        <div style="margin-top:10px;padding-top:8px;border-top:1px solid var(--parch-border);font-weight:bold">
          ${ps.endMembers} clenu | ${ps.endSupplies} zasob
        </div>
      </div>`;
    }
    detailCards += `</div>`;
  }

  const isFinalDay = round.day >= state.settings.totalDays;
  const dn = round.dayName ? ` — ${round.dayName}` : '';
  const dayLabel = isFinalDay && isLatest
    ? `Den ${round.day} — Poslední den hry${dn}`
    : isFinalDay
    ? `Den ${round.day} — Poslední den hry${dn}`
    : isLatest
    ? `Den ${round.day} — nejnovější${dn}`
    : `Den ${round.day}${dn}`;
  const bodyClass = isLatest ? 'history-day-body open' : 'history-day-body';

  return `
  <div class="history-day ${(isLatest||isFinalDay)?'current':''}">
    <div class="history-day-header" onclick="toggleDay(this)">
      <span class="day-num">${dayLabel}</span>
      <span class="day-event">
        <strong>${ev.name}</strong>
        ${ev.neg.length||ev.pos.length ? `-- ${negTags}${posTags}` : ''}
      </span>
      <span class="toggle-icon">${isLatest?'&#8679;':'&#8681;'}</span>
    </div>
    <div class="${bodyClass}">
      <div class="${evBannerClass}">
        <div>
          <h3>${ev.name}</h3>
          <div class="ev-detail-desc">${ev.desc}</div>
          ${ev.neg.length||ev.pos.length?`<div class="ev-effects">${negTags} ${posTags}</div>`:''}
        </div>
      </div>
      <div class="ovr-x">
      <table class="data-table">
        <thead><tr>
          <th>#</th><th>Hrac / Tlupa</th><th>Sbír.</th><th>Lov</th>
          <th>Prémie</th><th>Loupež+</th><th>Ukrad.-</th><th>Ztráty</th><th>Noví</th><th>Zásoby</th><th>Bonusy</th><th>Členů</th>
        </tr></thead>
        <tbody>${tableRows}</tbody>
      </table>
      </div>
      ${detailCards}
    </div>
  </div>`;
}

function toggleDay(header) {
  const body = header.nextElementSibling;
  const icon = header.querySelector('.toggle-icon');
  if (body.classList.contains('open')) {
    body.classList.remove('open');
    icon.textContent = '\u21d3';
  } else {
    body.classList.add('open');
    icon.textContent = '\u21d1';
  }
}

// ======================================================
//  BONUS
// ======================================================
function renderBonus() {
  const sel = document.getElementById('bonus-player');
  sel.innerHTML = state.players.map(p => `<option value="${p.id}">${esc(p.name)} / ${esc(p.tribeName)}</option>`).join('');
  const hist = document.getElementById('bonus-history');
  if (state.bonuses.length === 0) { hist.innerHTML = '<p class="text-muted">Zatim zadne bonusy.</p>'; return; }
  hist.innerHTML = `<div class="bonus-list">${[...state.bonuses].reverse().map(b => {
    const p = state.players.find(pl => pl.id === b.playerId);
    return `<div class="bonus-item">
      <span class="color-dot" style="background:${p?.color||'#888'}"></span>
      <span>${esc(p?.name||'?')} -- ${esc(p?.tribeName||'?')}</span>
      <span class="bonus-amount ${b.amount>=0?'pos':'neg'}">${b.amount>=0?'+':''}${b.amount}</span>
      <span>${esc(b.description)}</span>
      <span class="text-muted text-sm">Den ${b.day}</span>
      <button class="btn btn-red btn-sm" onclick="removeBonus('${b.id}')">X</button>
    </div>`;
  }).join('')}</div>`;
}

function addBonus() {
  const pid = document.getElementById('bonus-player').value;
  const amount = parseInt(document.getElementById('bonus-amount').value);
  const desc = document.getElementById('bonus-desc').value.trim();
  if (!pid||isNaN(amount)||amount===0) { alert('Zadej platnou nenulovou hodnotu.'); return; }
  state.bonuses.push({ id:'b'+Date.now(), playerId:pid, amount, description:desc||'Bez popisu', timestamp:new Date().toISOString(), day:state.currentDay });
  document.getElementById('bonus-desc').value = '';
  document.getElementById('bonus-amount').value = '50';
  saveState(state); renderBonus();
}

function removeBonus(id) {
  state.bonuses = state.bonuses.filter(b => b.id !== id);
  saveState(state); renderBonus();
}

// ======================================================
//  PRINT
// ======================================================
function printSheets() {
  if (state.players.length===0) { alert('Nejsou žádní hráči.'); return; }
  const nextDay = state.currentDay + 1;
  const today = new Date().toLocaleDateString('cs-CZ');
  let html = '';
  for (const p of state.players) {
    const members = getPlayerCurrentMembers(p.id);
    const supplies = getPlayerTotalSupplies(p.id);
    // Build bonus lines for this player
    const playerBonuses = state.bonuses.filter(b => b.playerId === p.id);
    const bonusTotal = playerBonuses.reduce((s,b) => s+b.amount, 0);
    let bonusRows = '';
    for (const b of playerBonuses) {
      bonusRows += `<tr style="border-bottom:1px solid #ddd">
        <td style="padding:4px 6px">${b.day||'--'}</td>
        <td style="padding:4px 6px">${esc(b.description)}</td>
        <td style="padding:4px 6px;font-weight:bold;color:${b.amount>=0?'green':'crimson'}">${b.amount>=0?'+':''}${b.amount}</td>
      </tr>`;
    }
    html += `<div class="print-page">
      <div class="print-header">
        <h1>${esc(p.tribeName)}</h1>
        <div class="print-tribe">Nacelnik: ${esc(p.name)}</div>
        <div class="print-day">Den ${nextDay} z ${state.settings.totalDays} | ${today}</div>
      </div>
      <div class="print-info-grid">
        <div class="print-info-box"><div class="label">Zivych clenu</div><div class="value">${members}</div></div>
        <div class="print-info-box"><div class="label">Zásoby celkem</div><div class="value">${supplies}</div></div>
      </div>
      <div class="print-section">
        <h3>Rozdeleni clenu (celkem: ${members})</h3>
        <div class="print-role-grid">
          ${['Sběrači','Lovci','Hlídači','Pobertové','Nečinní'].map(r=>`
          <div class="print-role-box"><div class="role-name">${r}</div><div class="role-fill"></div></div>`).join('')}
        </div>
        <div class="print-target-box"><div class="role-name">Cil utoku pobertu (tlupa)</div><div class="role-fill"></div></div>
      </div>
      <div class="print-section">
        <h3>Samanovo kouzlo (vyber jedno)</h3>
        <div class="print-spell-grid">
          ${Object.entries(SPELLS).map(([k,v])=>`
          <div class="print-spell-box"><div class="spell-name">${v.name}</div><div class="spell-desc">${v.desc}</div><div class="spell-check"></div></div>`).join('')}
        </div>
      </div>
      <div class="print-section">
        <div class="print-ref">
          <strong>Napoveda:</strong>
          <table><tr><th>Role</th><th>Vynos/akce</th></tr>
            <tr><td>Sberac</td><td>${state.settings.gatherAmount} zasob/den</td></tr>
            <tr><td>Lovec</td><td>${state.settings.huntAmount} zasob/den</td></tr>
            <tr><td>Hlidac</td><td>Brani zasoby (1 hlidac = 1 poberta)</td></tr>
            <tr><td>Poberta</td><td>Krade ${state.settings.raidCarry} zasob (musi prezit hlidace)</td></tr>
          </table>
        </div>
      </div>
    </div>`;
  }
  document.getElementById('print-content').innerHTML = html;
  showScreen('print');
}

function printLeaderboard() {
  const today = new Date().toLocaleDateString('cs-CZ');
  const currentDay = state.currentDay || state.rounds.length;
  const thStyle = 'padding:6px 10px;text-align:left;border:1px solid #888;background:#eee';

  function tdS(bold, right) {
    return `padding:6px 10px;border:1px solid #ccc${bold?';font-weight:bold':''}${right?';text-align:right':''}`;
  }

  function buildDayStandings(roundIdx) {
    return state.players.map(p => ({
      p,
      supplies: state.rounds[roundIdx].playerStates[p.id]?.endSupplies || 0,
      members:  state.rounds[roundIdx].playerStates[p.id]?.endMembers  || 0,
    })).sort((a,b) => b.supplies - a.supplies);
  }

  let html = '<div class="print-page">';
  html += `<div class="print-header">
    <h1>Žebříček tlup</h1>
    <div class="print-tribe">${esc(state.settings.gameName)}</div>
    <div class="print-day">Den ${currentDay} z ${state.settings.totalDays} | ${today}</div>
  </div>`;

  // Current overall standings
  const currentStandings = getSortedPlayers();
  html += `<div style="margin-bottom:22px">
    <h2 style="font-size:1.1rem;margin-bottom:8px;border-bottom:2px solid #333;padding-bottom:4px">Aktuální pořadí (Den ${currentDay})</h2>
    <table style="width:100%;border-collapse:collapse;font-size:0.95rem">
      <thead><tr>
        <th style="${thStyle}">#</th>
        <th style="${thStyle}">Hráč</th>
        <th style="${thStyle}">Tlupa</th>
        <th style="${thStyle};text-align:right">Zásoby</th>
        <th style="${thStyle};text-align:right">Členové</th>
        <th style="${thStyle};text-align:right">Bonusy</th>
      </tr></thead>
      <tbody>${currentStandings.map((p,i)=>`
        <tr>
          <td style="${tdS(i<3,false)}">${i+1}.</td>
          <td style="${tdS(i<3,false)}">${esc(p.name)}</td>
          <td style="${tdS(false,false)}">${esc(p.tribeName)}</td>
          <td style="${tdS(true,true)};font-size:1.05rem">${getPlayerTotalSupplies(p.id)}</td>
          <td style="${tdS(false,true)}">${getPlayerCurrentMembers(p.id)}</td>
          <td style="${tdS(false,true)}">${getPlayerBonusTotal(p.id)||'--'}</td>
        </tr>`).join('')}
      </tbody>
    </table>
  </div>`;

  // Per-day tables newest first
  for (let ri = state.rounds.length - 1; ri >= 0; ri--) {
    const round = state.rounds[ri];
    const ev = EVENTS[round.event] || EVENTS.none;
    const standings = buildDayStandings(ri);
    html += `<div style="margin-bottom:18px;page-break-inside:avoid">
      <h2 style="font-size:1rem;margin-bottom:6px;border-bottom:1px solid #666;padding-bottom:3px">
        Den ${round.day}${round.dayName?' — '+esc(round.dayName):''} | ${ev.name}
      </h2>
      <table style="width:100%;border-collapse:collapse;font-size:0.85rem">
        <thead><tr>
          <th style="${thStyle}">#</th>
          <th style="${thStyle}">Hráč</th>
          <th style="${thStyle}">Tlupa</th>
          <th style="${thStyle};text-align:right">Zásoby</th>
          <th style="${thStyle};text-align:right">Bonusy</th>
          <th style="${thStyle};text-align:right">Členů</th>
          <th style="${thStyle};text-align:right">Sbír.</th>
          <th style="${thStyle};text-align:right">Lov</th>
          <th style="${thStyle};text-align:right">Loupež+</th>
          <th style="${thStyle};text-align:right">Ukrad.-</th>
          <th style="${thStyle};text-align:right">Noví</th>
        </tr></thead>
        <tbody>${standings.map(({p,supplies,members},i)=>{
          const ps = round.playerStates[p.id];
          const r = ps?.results || {};
          const dayBonus = state.bonuses.filter(b=>b.playerId===p.id&&b.day===round.day).reduce((s,b)=>s+b.amount,0);
          return `<tr>
            <td style="${tdS(i===0,false)}">${i+1}.</td>
            <td style="${tdS(i===0,false)}">${esc(p.name)}</td>
            <td style="${tdS(false,false)}">${esc(p.tribeName)}</td>
            <td style="${tdS(true,true)}">${supplies}</td>
            <td style="${tdS(dayBonus>0,true)}">${dayBonus>0?'+'+dayBonus:'--'}</td>
            <td style="${tdS(false,true)}">${members}</td>
            <td style="${tdS(false,true)}">${r.gathered>0?'+'+r.gathered:'--'}</td>
            <td style="${tdS(false,true)}">${r.hunted>0?'+'+r.hunted:'--'}</td>
            <td style="${tdS(false,true)}">${(r.suppliesGained||0)>0?'+'+(r.suppliesGained||0):'--'}</td>
            <td style="${tdS(false,true)}">${(r.suppliesStolen||0)>0?'-'+r.suppliesStolen:'--'}</td>
            <td style="${tdS(false,true)}">+${r.newMembers||0}</td>
          </tr>`;
        }).join('')}
        </tbody>
      </table>
    </div>`;
  }
  html += '</div>';
  document.getElementById('print-content').innerHTML = html;
  showScreen('print');
}


// ======================================================
//  TISK -- OSOBNI LISTY HRACU (kazdy jen svuj)
// ======================================================
function printPlayerHistories() {
  if (state.players.length === 0) { alert('Nejsou žádní hráči.'); return; }
  const today = new Date().toLocaleDateString('cs-CZ');
  const currentDay = state.currentDay || state.rounds.length;
  let html = '';
  for (const p of state.players) {
    const members = getPlayerCurrentMembers(p.id);
    const supplies = getPlayerTotalSupplies(p.id);
    const bonuses = state.bonuses.filter(b => b.playerId === p.id);
    const bonusTotal = bonuses.reduce((s,b) => s+b.amount, 0);

    // Last day summary
    let lastDaySummary = '';
    if (state.rounds.length > 0) {
      const lastRound = state.rounds[state.rounds.length - 1];
      const ps = lastRound.playerStates[p.id];
      if (ps) {
        const r = ps.results;
        const asgn = ps.assignments;
        const ev = EVENTS[lastRound.event] || EVENTS.none;
        const sp = asgn ? SPELLS[asgn.spell] : null;
        const deaths = (r.huntersLost||0) + (r.guardsLost||0) + (r.raidersLost||0);
        const supplyChange = (r.gathered||0)+(r.hunted||0)+(r.suppliesGained||0)+(r.bvBonus||0)-(r.suppliesStolen||0);
        lastDaySummary = `
        <div style="margin-bottom:14px">
          <div style="font-size:0.8rem;font-weight:bold;text-transform:uppercase;color:#666;margin-bottom:6px">
            Den ${lastRound.day}${lastRound.dayName ? ' — '+esc(lastRound.dayName) : ''} | Událost: ${ev.name}
          </div>
          <table style="width:100%;border-collapse:collapse;font-size:0.82rem;border:1px solid #ccc">
            <tr style="background:#f5f5f5">
              <th style="padding:4px 8px;text-align:left;border:1px solid #ccc">Rozmístění</th>
              <th style="padding:4px 8px;text-align:right;border:1px solid #ccc">Sběr</th>
              <th style="padding:4px 8px;text-align:right;border:1px solid #ccc">Lov</th>
              <th style="padding:4px 8px;text-align:right;border:1px solid #ccc">Loupež+</th>
              <th style="padding:4px 8px;text-align:right;border:1px solid #ccc">Ukrad.-</th>
              <th style="padding:4px 8px;text-align:right;border:1px solid #ccc">Ztráty</th>
              <th style="padding:4px 8px;text-align:right;border:1px solid #ccc">Noví</th>
              <th style="padding:4px 8px;text-align:right;border:1px solid #ccc;font-weight:bold">Změna zásob</th>
            </tr>
            <tr>
              <td style="padding:4px 8px;border:1px solid #ccc;font-size:0.75rem">
                ${sp ? esc(sp.name)+' | ' : ''}
                S:${asgn?asgn.gatherers:0} L:${asgn?asgn.hunters:0} H:${asgn?asgn.guards:0} P:${asgn?asgn.raiders:0}
              </td>
              <td style="padding:4px 8px;text-align:right;border:1px solid #ccc;color:green">+${r.gathered||0}</td>
              <td style="padding:4px 8px;text-align:right;border:1px solid #ccc;color:green">+${r.hunted||0}</td>
              <td style="padding:4px 8px;text-align:right;border:1px solid #ccc;color:${(r.suppliesGained||0)>0?'green':'#555'}">${(r.suppliesGained||0)>0?'+':''}${r.suppliesGained||'--'}</td>
              <td style="padding:4px 8px;text-align:right;border:1px solid #ccc;color:${(r.suppliesStolen||0)>0?'crimson':'#555'}">${(r.suppliesStolen||0)>0?'-'+r.suppliesStolen:'--'}</td>
              <td style="padding:4px 8px;text-align:right;border:1px solid #ccc;color:${deaths>0?'crimson':'#555'}">${deaths>0?'-'+deaths:'--'}</td>
              <td style="padding:4px 8px;text-align:right;border:1px solid #ccc;color:green">+${r.newMembers||0}</td>
              <td style="padding:4px 8px;text-align:right;border:1px solid #ccc;font-weight:bold;color:${supplyChange>=0?'green':'crimson'}">${supplyChange>=0?'+':''}${supplyChange}</td>
            </tr>
          </table>
        </div>`;
      }
    }

    // Bonus rows
    let bonusHtml = '';
    if (bonuses.length > 0) {
      bonusHtml = `<div style="margin-bottom:10px;font-size:0.8rem">
        <strong>Bonusy: </strong>
        ${bonuses.map(b=>`${esc(b.description)} <span style="font-weight:bold;color:${b.amount>=0?'green':'crimson'}">${b.amount>=0?'+':''}${b.amount}</span>`).join(' | ')}
        <strong> = ${bonusTotal>=0?'+':''}${bonusTotal}</strong>
      </div>`;
    }

    html += `<div class="print-page">
      <div class="print-header">
        <h1>${esc(p.tribeName)}</h1>
        <div class="print-tribe">Náčelník: ${esc(p.name)}</div>
        <div class="print-day">Den ${currentDay} z ${state.settings.totalDays} | ${today}</div>
      </div>

      <div class="print-info-grid" style="margin-bottom:12px">
        <div class="print-info-box"><div class="label">Živých členů</div><div class="value">${members}</div></div>
        <div class="print-info-box"><div class="label">Zásoby celkem</div><div class="value">${supplies}</div></div>
      </div>

      ${bonusHtml}
      ${lastDaySummary ? `<div class="print-section"><h3>Výsledky posledního dne</h3>${lastDaySummary}</div>` : ''}

      <div class="print-section">
        <h3>Rozhodnutí pro den ${currentDay + 1} — k dispozici ${members} členů</h3>
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;margin-bottom:12px">
          <thead><tr style="background:#eee">
            <th style="padding:6px 10px;text-align:left;border:2px solid #333;width:40%">Role</th>
            <th style="padding:6px 10px;text-align:center;border:2px solid #333;width:30%">Počet</th>
            <th style="padding:6px 10px;text-align:left;border:2px solid #333;width:30%">Poznámka</th>
          </tr></thead>
          <tbody>
            ${[
              ['Sběrači', 'zásoby ze sběru'],
              ['Lovci', 'zásoby z lovu'],
              ['Hlídači', 'brání zásoby'],
              ['Pobertové', 'kradou zásoby'],
              ['Nečinní', ''],
            ].map(([role, note]) => `<tr>
              <td style="padding:8px 10px;border:1px solid #ccc;font-weight:bold">${role}</td>
              <td style="padding:8px 10px;border:1px solid #ccc;text-align:center">
                <div style="height:22px;border-bottom:2px solid #333;width:80%;margin:0 auto"></div>
              </td>
              <td style="padding:8px 10px;border:1px solid #ccc;font-size:0.78rem;color:#555">${note}</td>
            </tr>`).join('')}
            <tr>
              <td style="padding:8px 10px;border:1px solid #ccc;font-weight:bold">Cíl útoku pobertů</td>
              <td colspan="2" style="padding:8px 10px;border:1px solid #ccc">
                <div style="height:22px;border-bottom:2px solid #333"></div>
              </td>
            </tr>
          </tbody>
        </table>

        <h3 style="margin-top:10px">Šamanovo kouzlo (zaškrtni jedno)</h3>
        <table style="width:100%;border-collapse:collapse;font-size:0.85rem">
          <tbody>
            ${Object.entries(SPELLS).map(([k,v]) => `
            <tr style="border-bottom:1px solid #ddd">
              <td style="padding:7px 10px;width:28px;border:1px solid #ccc;text-align:center">
                <div style="width:18px;height:18px;border:2px solid #333;display:inline-block;border-radius:3px"></div>
              </td>
              <td style="padding:7px 10px;font-weight:bold;border:1px solid #ccc;width:140px">${v.name}</td>
              <td style="padding:7px 10px;font-size:0.78rem;color:#444;border:1px solid #ccc">${v.desc}</td>
            </tr>`).join('')}
          </tbody>
        </table>
      </div>
    </div>`;
  }
  document.getElementById('print-content').innerHTML = html;
  showScreen('print');
}


function printLeaderboardConditional() {
  if (state.players.length === 0) { alert('Nejsou žádní hráči.'); return; }
  printLeaderboard();
}

// ======================================================
//  TISK -- KARTY UDALOSTI
// ======================================================
function printEventCards() {
  const today = new Date().toLocaleDateString('cs-CZ');
  let html = '';
  const eventKeys = Object.keys(EVENTS).filter(k => k !== 'none');
  for (const key of eventKeys) {
    const ev = EVENTS[key];
    const negHtml = ev.neg.map(t=>`<div style="margin:3px 0;padding:4px 10px;background:#fee;border-left:4px solid #a00;font-size:0.88rem">&#8722; ${t}</div>`).join('');
    const posHtml = ev.pos.map(t=>`<div style="margin:3px 0;padding:4px 10px;background:#efe;border-left:4px solid #060;font-size:0.88rem">+ ${t}</div>`).join('');
    html += `<div style="border:3px solid #333;border-radius:6px;padding:20px;margin-bottom:20px;page-break-inside:avoid;max-width:600px">
      <div style="font-size:2rem;margin-bottom:8px">${ev.icon}</div>
      <h2 style="font-size:1.5rem;margin-bottom:10px;border-bottom:2px solid #333;padding-bottom:6px">${ev.name}</h2>
      <p style="font-size:0.95rem;line-height:1.7;margin-bottom:14px">${ev.desc}</p>
      ${negHtml}${posHtml}
    </div>`;
  }
  document.getElementById('print-content').innerHTML = html;
  showScreen('print');
}

// ======================================================
//  TISK -- PRAVIDLA HRY
// ======================================================
function printGameRules() {
  const th = 'padding:6px 10px;border:1px solid #888;background:#eee;text-align:left';
  const td = 'padding:6px 10px;border:1px solid #ccc';
  const s = state.settings;
  const html = `<div class="print-page">
    <div class="print-header">
      <h1>${esc(s.gameName)}</h1>
      <div class="print-tribe">Pravěká Tlupa — pravidla pro hráče</div>
    </div>

    <div class="print-section">
      <h3>Cíl hry</h3>
      <p style="font-size:0.9rem;line-height:1.7;margin-bottom:10px">
        Každý hráč vede pravěkou tlupu, která musí nashromáždit co nejvíce zásob před příchodem doby ledové.
        Hra trvá <strong>${s.totalDays} dní</strong>. Každý den rozhoduješ, jak rozmístíš členy tlupy.
        Vítězí tlupa s nejvíce zásobami na konci poslední dne.
      </p>
    </div>

    <div class="print-section">
      <h3>Role členů tlupy (k dispozici každý den)</h3>
      <table style="width:100%;border-collapse:collapse;font-size:0.88rem;margin-bottom:12px">
        <thead><tr>
          <th style="${th}">Role</th>
          <th style="${th}">Co dělá</th>
          <th style="${th}">Výnos</th>
        </tr></thead>
        <tbody>
          <tr><td style="${td}"><strong>Sběrači</strong></td>
              <td style="${td}">Sbírají plody, kořínky a zásoby z přírody</td>
              <td style="${td}"><strong>${s.gatherAmount}</strong> zásoby / sběrač</td></tr>
          <tr><td style="${td}"><strong>Lovci</strong></td>
              <td style="${td}">Loví zvěř pro zásoby tlupy</td>
              <td style="${td}"><strong>${s.huntAmount}</strong> zásoby / lovec</td></tr>
          <tr><td style="${td}"><strong>Hlídači</strong></td>
              <td style="${td}">Chrání zásoby před nájezdy cizích pobertů vlastním tělem. Jeden Hlídač obětuje svůj život a zastaví jednoho Pobertu.</td>
              <td style="${td}">1 hlídač zastaví 1 pobertu</td></tr>
          <tr><td style="${td}"><strong>Pobertové</strong></td>
              <td style="${td}">Napadají jinou tlupu a kradou její zásoby. Srážka Poberty s Hlídačem je jistou smrtí.</td>
              <td style="${td}"><strong>${s.raidCarry}</strong> zásoby / poberta (musí přežít hlídače)</td></tr>
          <tr><td style="${td}"><strong>Nečinní</strong></td>
              <td style="${td}">Odpočívají — nepřinášejí zásoby</td>
              <td style="${td}">—</td></tr>
        </tbody>
      </table>
      <p style="font-size:0.82rem;color:#555">
        ⚠ Celkový počet přiřazených členů nesmí překročit aktuální počet živých členů tlupy.<br>
        Pobertové musí mít zadaný cíl útoku (jméno tlupy).
      </p>
    </div>

    <div class="print-section">
      <h3>Šamanská kouzla (každý den vybereš jedno)</h3>
      <table style="width:100%;border-collapse:collapse;font-size:0.88rem;margin-bottom:12px">
        <thead><tr>
          <th style="${th}">Kouzlo</th>
          <th style="${th}">Efekt</th>
        </tr></thead>
        <tbody>
          ${Object.entries(SPELLS).map(([k,v])=>`
          <tr><td style="${td}"><strong>${v.name}</strong></td>
              <td style="${td}">${v.desc}</td></tr>`).join('')}
        </tbody>
      </table>
      <p style="font-size:0.82rem;color:#555">
        Kouzlo platí pouze na tvé vlastní členy — neovlivňuje ostatní tlupy.
      </p>
    </div>

    <div class="print-section">
      <h3>Denní přírůstek tlupy</h3>
      <p style="font-size:0.9rem;margin-bottom:10px">
        Každý den přibudou <strong>${s.dailyNewMembers} noví členové</strong> tlupy automaticky.
        S kouzlem <em>Plodnost</em> přibudou <strong>${s.dailyNewMembers * 2}</strong>.
      </p>
      <p style="font-size:0.9rem">
        Počáteční stav: <strong>${s.startingMembers} členů</strong>, <strong>${s.startingSupplies} zásob</strong>.
      </p>
    </div>

    <div class="print-section">
      <h3>Události dne</h3>
      <p style="font-size:0.9rem;line-height:1.7">
        Administrátor každý den vylosuje nebo zvolí událost, která ovlivní výsledky všech tlup.
        Popis události bude vyvěšen na nástěnce. Výběr události probíhá před odevzdáním lístků,
        takže jej znáš při rozhodování.
      </p>
    </div>

    <div class="print-section">
      <h3>Jak vyplnit lístek</h3>
      <ol style="font-size:0.9rem;line-height:1.9;padding-left:20px">
        <li>Vypiš počet členů do každé role. Součet nesmí překročit tvůj aktuální počet členů.</li>
        <li>Pokud posíláš poberty, napiš jméno tlupy, na kterou je posíláš.</li>
        <li>Zaškrtni jedno šamanovo kouzlo.</li>
        <li>Odevzdej lístek Lojzovi.</li>
      </ol>
    </div>
  </div>`;
  document.getElementById('print-content').innerHTML = html;
  showScreen('print');
}

// ======================================================
//  IMPORT / EXPORT
// ======================================================
function exportData() {
  const blob = new Blob([JSON.stringify(state,null,2)], {type:'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `praveka-tlupa-${new Date().toISOString().slice(0,10)}.json`;
  a.click();
}
function importData(e) {
  const file = e.target.files[0]; if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => {
    try {
      const imported = JSON.parse(ev.target.result);
      if (!imported.settings||!imported.players) throw new Error('Neplatný soubor');
      state = imported; saveState(state); showScreen('dashboard'); alert('Data importována.');
    } catch(err) { alert('Chyba při importu: ' + err.message); }
  };
  reader.readAsText(file); e.target.value = '';
}

// ======================================================
//  UTILITIES
// ======================================================
function esc(s) {
  if (!s) return '';
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}
function showMsg(id, text, type) {
  const el = document.getElementById(id); if (!el) return;
  el.className = `msg msg-${type}`; el.textContent = text; el.classList.remove('hidden');
  setTimeout(() => el.classList.add('hidden'), 4000);
}

// ======================================================
//  INIT
// ======================================================
document.addEventListener('DOMContentLoaded', () => {
  updateNavDay();
  showScreen(state.started ? 'dashboard' : 'setup');
});
"""

OUTPUT = '/sessions/zealous-trusting-gauss/mnt/outputs/praveka_tlupa.html'

content = HTML.replace('STYLE_PLACEHOLDER', CSS)
content = content.replace('</body>', f'<script>\n{JS}\n</script>\n</body>')

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Written {len(content):,} bytes to {OUTPUT}')
