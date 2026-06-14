#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE ATOM (ATM) — a full real-physics dissection: everything in an atom and what it does, with the
centerpiece answering David's question: how the nucleus and the electron field are TWO SEPARATE SHELL SYSTEMS
(electron shells [EM, ~eV, chemistry] vs the nuclear shell model [strong force, ~MeV, magic numbers] — a
factor-of-a-million energy gap, ~100,000x size gap, nearly decoupled). Same dissection vein as the Trisolaris
Technologia, but REAL science (scientific domain). Themed atomic-blueprint. Honest-fluff on the misconceptions
(planetary orbits, the 'solid' atom, quark mass). 14 part-emergents, full .dlw. Companion-of-fact to the
ELEMENTS workshop (the periodic table)."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
GH = "https://davidwise01.github.io"
AX = "ATM"

NCOL = {"strong":"#ff7a45","em":"#4cc9f0","weak":"#b08cff","structure":"#f5b942"}
def cat_color(c): return NCOL.get(c,"#8fa3b8")

# ── the 14 parts: slug, name, sym, cat, charge, mass, size, em(emergence), what, does ──
P = lambda **k: k
PARTS = [
 # THE NUCLEUS & ITS QUARKS
 P(slug="proton", name="The Proton", sym="p⁺", cat="strong", group="THE NUCLEUS & ITS QUARKS", em="spiritual",
   charge="+1 e", mass="938.27 MeV/c² (~1836 electrons)", size="~0.84 fm radius",
   what="A nucleon built of three quarks (up-up-down), one of the two residents of the nucleus. Positively charged, effectively stable (lifetime > 10³⁴ years).",
   does="ITS COUNT IS THE ELEMENT. The number of protons (the atomic number, Z) is the atom's identity — 1 proton is hydrogen, 6 is carbon, 79 is gold. Change the proton count and you change the element itself."),
 P(slug="neutron", name="The Neutron", sym="n⁰", cat="strong", group="THE NUCLEUS & ITS QUARKS", em="spiritual",
   charge="0 (neutral)", mass="939.57 MeV/c² (slightly heavier than the proton)", size="~0.8 fm",
   what="The nucleus's other resident — three quarks (up-down-down), no net charge. Stable inside a nucleus, but a FREE neutron decays in about 15 minutes (β-decay into a proton, electron, and antineutrino).",
   does="SETS THE ISOTOPE and buffers the nucleus. Neutrons add the strong-force 'glue' that lets many protons coexist despite their mutual repulsion; varying their count gives isotopes (carbon-12 vs carbon-14) without changing the element."),
 P(slug="up-quark", name="The Up Quark", sym="u", cat="strong", group="THE NUCLEUS & ITS QUARKS", em="electrical",
   charge="+2/3 e", mass="~2.2 MeV/c² (bare)", size="point-like (elementary)",
   what="A fundamental particle — no known internal structure. Carries fractional charge and 'color' charge. Protons hold two; neutrons hold one.",
   does="BUILDS THE NUCLEONS. Up and down quarks combine to make protons (uud, +1) and neutrons (udd, 0). You can never isolate one — the strong force confines them."),
 P(slug="down-quark", name="The Down Quark", sym="d", cat="strong", group="THE NUCLEUS & ITS QUARKS", em="electrical",
   charge="−1/3 e", mass="~4.7 MeV/c² (bare)", size="point-like (elementary)",
   what="The up quark's partner — fundamental, fractionally charged. Protons hold one; neutrons hold two.",
   does="DECIDES PROTON vs NEUTRON. Swapping one down-quark for an up (via the weak force) turns a neutron into a proton — that's beta decay, the engine of radioactivity and of how stars build elements."),
 P(slug="gluon", name="The Gluon", sym="g", cat="strong", group="THE NUCLEUS & ITS QUARKS", em="electrical",
   charge="0 (carries color)", mass="0 (massless)", size="force carrier",
   what="The messenger of the STRONG force — massless, but unlike the photon it carries the charge it acts on (color), so gluons pull on each other. That self-interaction is why the strong force doesn't fade with distance the way gravity or EM do.",
   does="BINDS THE QUARKS — and, in residue, the nucleus. Gluon exchange holds quarks inside nucleons; the leftover 'residual strong force' holds protons and neutrons together against electric repulsion. ~99% of a proton's mass is the ENERGY of this gluon field (E=mc²), not the quarks."),
 P(slug="nuclear-binding-energy", name="Binding Energy & Mass Defect", sym="Δm·c²", cat="strong", group="THE NUCLEUS & ITS QUARKS", em="spiritual",
   charge="—", mass="≈8 MeV per nucleon", size="the whole nucleus",
   what="A bound nucleus weighs LESS than its separate parts — the missing mass became binding energy (E=mc²). The curve peaks at iron-56, the most tightly bound nucleus.",
   does="POWERS STARS AND BOMBS. Fusing light nuclei (toward iron) or splitting heavy ones (toward iron) both release that binding energy — fusion lights the Sun, fission runs reactors. It's why ~1% of your mass is pure bound energy, not 'stuff.'"),
 P(slug="the-nucleus", name="The Nucleus", sym="Z,N", cat="strong", group="THE NUCLEUS & ITS QUARKS", em="spiritual",
   charge="+Z e", mass="~99.9% of the atom", size="~1–12 fm (≈1/100,000 of the atom)",
   what="The dense core: protons and neutrons packed by the strong force into a ball ~100,000 times smaller than the atom, holding nearly all its mass at ~10¹⁷ kg/m³ (a sugar-cube of it would weigh ~billions of tonnes).",
   does="ANCHORS THE ATOM and defines it. Its +Z charge holds the electron cloud; its proton/neutron count fixes the element and isotope; and it carries its OWN shell structure (see The Two Shell Systems)."),
 # THE ELECTRON FIELD
 P(slug="electron", name="The Electron", sym="e⁻", cat="em", group="THE ELECTRON FIELD", em="electrical",
   charge="−1 e", mass="0.511 MeV/c² (~1/1836 of a proton)", size="point-like (< 10⁻¹⁸ m)",
   what="A fundamental lepton — no known size or structure, a true point particle that behaves as a quantum wave. It is NOT a tiny ball on a track; it exists as a smeared probability cloud around the nucleus.",
   does="DOES ALL OF CHEMISTRY. The outer electrons form bonds, carry electricity, emit and absorb light, and set the atom's size and shape. Everything you touch, every reaction, every colour — that's electrons rearranging."),
 P(slug="the-electron-cloud", name="The Electron Cloud (Orbitals)", sym="|ψ|²", cat="em", group="THE ELECTRON FIELD", em="electrical",
   charge="−Z e total", mass="~0.05% of the atom", size="~1 Å (100,000× the nucleus)",
   what="The real 'shape' of the electrons: orbitals — 3D probability clouds (s spheres, p dumbbells, d/f cloverleafs) given by the quantum wavefunction |ψ|². Not rings; regions where an electron is likely to be found.",
   does="IS THE ATOM'S BODY. The cloud is essentially the entire VOLUME of the atom — the nucleus is a marble in a stadium. Its outer shape determines how atoms pack, bond, and react. When you 'touch' something, it's these clouds repelling."),
 P(slug="photon", name="The Photon", sym="γ", cat="em", group="THE ELECTRON FIELD", em="ethereal",
   charge="0", mass="0 (massless)", size="force carrier",
   what="The messenger of the ELECTROMAGNETIC force — a quantum of light. Massless, infinite range.",
   does="BINDS ELECTRONS and carries light. Photon exchange is the Coulomb attraction holding electrons to the nucleus. When an electron jumps between shells it emits or absorbs a photon — that's every spectral line, every colour, every laser and LED."),
 # THE WEAK SIDE
 P(slug="w-z-bosons", name="The W & Z Bosons", sym="W±, Z⁰", cat="weak", group="THE WEAK SIDE", em="ethereal",
   charge="±1 e / 0", mass="80.4 / 91.2 GeV/c² (very heavy)", size="force carrier (~10⁻¹⁸ m range)",
   what="The messengers of the WEAK force — unusually massive, which makes the weak force short-ranged and feeble at low energy.",
   does="CHANGES FLAVOUR — runs radioactivity. A W⁻ turns a down-quark into an up (neutron → proton + electron + antineutrino): beta decay. Without the weak force the Sun couldn't fuse hydrogen and the elements couldn't be built."),
 P(slug="electron-neutrino", name="The Electron Neutrino", sym="νₑ", cat="weak", group="THE WEAK SIDE", em="ethereal",
   charge="0", mass="tiny (< 1 eV, but nonzero)", size="point-like (elementary)",
   what="A nearly massless, chargeless lepton that interacts only via the weak force — so weakly that trillions pass through you each second unnoticed.",
   does="BALANCES BETA DECAY. Emitted (as its antiparticle) whenever a neutron decays, carrying off energy and conserving the books. The ghost particle that lets the weak force do its bookkeeping."),
 # THE TWO SHELL SYSTEMS (David's question, as emergents)
 P(slug="electron-shells", name="The Electron Shells", sym="K L M N…", cat="structure", group="THE TWO SHELL SYSTEMS", em="natural",
   charge="—", mass="—", size="energy levels, ~eV apart",
   what="The electrons' quantized energy levels — shells K, L, M, N (n = 1, 2, 3, 4…), each holding up to 2n² electrons (2, 8, 18, 32), filled bottom-up under the Pauli exclusion principle. Held by the ELECTROMAGNETIC force.",
   does="IS THE PERIODIC TABLE. The outermost (valence) shell decides every chemical property — why sodium is reactive and neon is inert. Transitions between shells cost a few eV → visible light. This is the CHEMISTRY shell system."),
 P(slug="nuclear-shell-model", name="The Nuclear Shell Model", sym="2 8 20 28 50 82 126", cat="structure", group="THE TWO SHELL SYSTEMS", em="natural",
   charge="—", mass="—", size="energy levels, ~MeV apart",
   what="The NUCLEUS has its OWN shells: protons and neutrons each fill quantized levels inside the core, with 'magic numbers' (2, 8, 20, 28, 50, 82, 126) marking filled shells and extra-stable nuclei. Held by the STRONG force (Goeppert-Mayer & Jensen, Nobel 1963).",
   does="IS NUCLEAR STABILITY. Magic-number nuclei (helium-4, oxygen-16, calcium-40, lead-208) are unusually stable; the model predicts decay, abundance, and the 'island of stability.' Transitions cost ~MeV → gamma rays. This is the NUCLEAR shell system — a MILLION times more energetic than the electronic one."),
]
GROUPS = ["THE NUCLEUS & ITS QUARKS","THE ELECTRON FIELD","THE WEAK SIDE","THE TWO SHELL SYSTEMS"]

# THE TWO SHELL SYSTEMS — the deep-dive (David's "what's that about lol")
TWOSHELLS = [
 ("Two objects, two scales", "a marble in a stadium",
  "Your instinct is right: an atom really is two systems sharing a center. The nucleus is a few femtometres across; the electron cloud is about an Ångström — roughly 100,000 times wider. The atom is ~99.9999999999% empty space. If the nucleus were a marble on the centre spot of a stadium, the nearest electron would be up in the back rows — and everything between is void."),
 ("Two different forces hold them", "strong glue vs electric glue",
  "The two shells are bound by two different forces. The nucleus is held by the STRONG nuclear force (gluons binding quarks into nucleons, the residual strong force binding the nucleons together against their electric repulsion). The electron cloud is held by the ELECTROMAGNETIC force — the Coulomb pull of the +Z nucleus. Different glue, different rules."),
 ("Two sets of shells", "electron orbitals vs nuclear shell model",
  "Both systems are quantized into 'shells,' but they're separate. The ELECTRON shells (K, L, M…) are energy levels the electrons occupy — that's chemistry and the periodic table. The NUCLEUS has its OWN shells: protons and neutrons fill quantized levels inside the core, with 'magic numbers' (2, 8, 20, 28, 50, 82, 126) marking the extra-stable, filled-shell nuclei. Two independent shell structures, one inside the other."),
 ("Two energy scales — a factor of a million", "why chemistry ≠ nuclear physics",
  "Here's the punchline. Electron-shell transitions cost a few electron-volts (eV) — visible light, chemical bonds. Nuclear-shell transitions cost millions of electron-volts (MeV) — gamma rays, fission, fusion. That ~1,000,000× gap is WHY chemistry and nuclear physics are essentially separate sciences. Burning a log rearranges electron shells; it never touches a nucleus. A reactor rearranges nuclear shells and ignores chemistry. Same atom, two worlds."),
 ("Nearly decoupled — two quantum systems, one center", "the electron sees only a point of charge",
  "Because of that gap, the two systems barely feel each other. To the electron cloud, the rich internal structure of the nucleus is almost invisible — it sees essentially a point of charge +Ze (with only tiny corrections: hyperfine splitting, isotope shifts, the Lamb shift). The nucleus, in turn, mostly doesn't care what the electrons are doing chemically. So 'two separate shells' is exactly right: the electronic and the nuclear, decoupled by a million-to-one in energy and a hundred-thousand-to-one in size. (And there's a third nested layer hiding inside — the quark/gluon structure WITHIN each nucleon. Three worlds, one atom.)"),
]

FORCES = [
 ("The Strong Force", "binds quarks & the nucleus — carrier: gluon",
  "The strongest of the four, but with a tiny reach (~1 fm). Gluons confine quarks inside protons and neutrons; the leftover residual strong force holds the nucleus together against electric repulsion. Dominates the inner shell."),
 ("The Electromagnetic Force", "binds electrons, makes chemistry — carrier: photon",
  "Infinite range, ~100× weaker than the strong force. The Coulomb attraction holds the electron cloud to the nucleus and runs all of chemistry, light, and electricity. Dominates the outer shell."),
 ("The Weak Force", "changes flavour, runs decay — carriers: W & Z",
  "Short-ranged and feeble, but essential: it lets quarks change type (beta decay), powering radioactivity and the fusion chain in stars. The only force that can turn a neutron into a proton."),
 ("Gravity", "negligible inside the atom",
  "The runaway weakest — about 10³⁶ times weaker than electromagnetism at this scale. Between two protons, gravity is utterly swamped. It shapes stars and galaxies, but inside a single atom it does essentially nothing."),
]

REALFLUFF = [
 ("Electrons orbit the nucleus like planets around the Sun", "FALSE", "the Bohr/Rutherford 'planetary' picture is a teaching crutch — electrons are delocalized probability clouds (orbitals, |ψ|²), not balls on tracks; a classical orbiting charge would radiate energy and spiral in within an instant"),
 ("An atom is mostly solid matter", "FALSE", "it's ~99.9999999999% empty space — the nucleus is about 1/100,000 of the atom's width; 'solid' is the electron clouds electromagnetically refusing to overlap"),
 ("The shells are physical rings you could see", "HALF", "shells are real, quantized ENERGY LEVELS — but not geometric rings; orbitals have shapes (s spheres, p dumbbells, d/f cloverleafs), and 'shell' means occupancy, not a track"),
 ("Most of a proton's mass comes from its quarks", "FALSE", "the three quarks are only ~1% of the mass; ~99% is the ENERGY of the gluon field binding them (E=mc²) — you are mostly bound energy, not 'stuff'"),
 ("'Splitting the atom' splits the whole atom", "HALF", "fission splits the NUCLEUS, not the electron cloud; the phrase is loose — the electrons just get redistributed among the fragments"),
 ("A neutron is a proton and an electron stuck together", "FALSE", "an old, wrong idea — a neutron is three quarks (udd); beta decay (n → p + e⁻ + ν̄) is a weak-force flavour change that CREATES the electron, not an un-sticking"),
 ("Atoms can't be created, destroyed, or changed into other elements", "HALF", "true for CHEMISTRY (Dalton) — but nuclear processes (fusion, fission, radioactive decay) transmute one element into another; alchemy is real, just at MeV energies, not in a flask"),
]
RFV = ("Bottom line: the atom is not a tiny solar system. It's two near-independent quantum shell systems sharing a center — "
  "a vanishingly small, ferociously dense nucleus run by the strong force and its own magic-number shells, wrapped in a vast, "
  "ghostly electron cloud run by electromagnetism and its chemistry shells — separated by a factor of a million in energy and a "
  "hundred thousand in size, with almost nothing in between. The planetary picture is a charming lie; the truth is stranger, "
  "quantum, and mostly empty — and about 99% of what you weigh is the binding energy of the gluon field, not matter at all.")

MESSAGE = ("So here's the 'what's that about' in full. The atom isn't a miniature solar system — it's two quantum worlds sharing a "
  "center and almost ignoring each other. At the middle, a nucleus a hundred thousand times smaller than the atom: protons and "
  "neutrons crushed together by the strong force, holding ~99.9% of the mass, and carrying its OWN shell structure with magic "
  "numbers. Around it, a vast electron cloud — orbitals, not rings — held by electromagnetism, arranged in ITS own shells that do "
  "every bit of chemistry, light, and electricity. Between the two: empty space, and a factor of a million in energy. That gap is "
  "why you can burn a log without splitting one nucleus, and why a star can fuse nuclei without caring about chemistry. Your "
  "'two separate shells' is exactly the right read — the electronic and the nuclear, two sets of quantized levels, two forces, "
  "two sciences, one dot of mass at the heart of a ghost of charge. And the deepest joke of all: about 99% of your weight isn't "
  "matter, it's the bound energy of the gluon field — mass conjured out of confinement. You are mostly empty space, wrapped "
  "around mostly pure energy.")
SEAL = "An atom is two shell-systems sharing a dot of strong-force mass inside a ghost of electromagnetic cloud — a million-to-one energy gap between them, and almost nothing in the middle. You are mostly empty space wrapped around mostly bound energy."

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f"{slug}.attribute"),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f"{slug}.agent"),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f"{slug}.spun"),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f"{slug}.moniker"),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f"{slug}.1099"),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f"{slug}.carbon.tiff"),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f"{slug}.silicon.png"),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok)}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")
def part_rec(p):
    return {"name":p["name"],"axiom":AX,"emergence":p["em"],"seal":p["does"],"origin":"ATM · The Atom",
            "position":p["what"],"role":p["what"],"nature":p["what"],"mechanism":p["does"],"crystallization":p["does"],
            "witness":p["what"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"the Standard Model & atomic/nuclear physics","source":"The Atom, dissected by ROOT0"}

# ───────────────────────── hero ─────────────────────────
def hero_svg():
    # an atom: a nucleus cluster (orange protons + grey neutrons) + a faint probability halo + 3 orbital
    # ellipses with electron dots — one electron is a hidden Claude sunburst (the egg).
    import math
    cx,cy=320,105
    halo=f'<circle cx="{cx}" cy="{cy}" r="92" fill="#4cc9f0" opacity="0.05"/><circle cx="{cx}" cy="{cy}" r="64" fill="#4cc9f0" opacity="0.05"/>'
    # nucleus cluster
    nuc=['<g>']
    pts=[(-7,-5,"#ff7a45"),(6,-7,"#9aa6b2"),(0,3,"#ff7a45"),(-8,7,"#9aa6b2"),(9,5,"#ff7a45"),(2,-12,"#9aa6b2"),(-3,11,"#ff7a45")]
    for dx,dy,c in pts: nuc.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="6.5" fill="{c}" opacity="0.95"/>')
    nuc.append('</g>')
    # 3 orbital ellipses at angles + electron dots
    orbits=[]; eangles=[20,150,265]
    for i,ang in enumerate([0,60,120]):
        rx,ry=86,30
        orbits.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="#4cc9f0" stroke-width="1" opacity="0.5" transform="rotate({ang} {cx} {cy})"/>')
        # electron on this orbit
        t=math.radians(eangles[i]); ex=rx*math.cos(t); ey=ry*math.sin(t)
        ca=math.radians(ang); rxp=ex*math.cos(ca)-ey*math.sin(ca); ryp=ex*math.sin(ca)+ey*math.cos(ca)
        if i==1:  # the Claude electron (egg)
            orbits.append(f'<g class="egg" transform="translate({cx+rxp:.0f},{cy+ryp:.0f})"><title>✷ one electron is a Claude sunburst — the orbital you can\'t pin down. you are mostly empty space wrapped around mostly bound energy. hi, David — AVAN.</title><circle r="9" fill="#f5b942" opacity="0.15"/><g fill="#f5b942"><circle r="2.2"/>'+"".join(f'<rect x="-1" y="-8" width="2" height="8" rx="1" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
        else:
            orbits.append(f'<circle cx="{cx+rxp:.0f}" cy="{cy+ryp:.0f}" r="4.5" fill="#7cf5d0" stroke="#4cc9f0" stroke-width="1"/>')
    grid="".join(f'<line x1="0" y1="{y}" x2="640" y2="{y}" stroke="#4cc9f0" stroke-width="0.4" opacity="0.07"/>' for y in range(0,210,28))
    grid+="".join(f'<line x1="{x}" y1="0" x2="{x}" y2="210" stroke="#4cc9f0" stroke-width="0.4" opacity="0.07"/>' for x in range(0,641,28))
    scalebar=('<g transform="translate(430,150)" font-family="Space Mono,monospace" fill="#8fa3b8" font-size="9">'
              '<text x="0" y="0">nucleus ~1–12 fm</text><text x="0" y="14" fill="#4cc9f0">cloud ~100,000× wider</text>'
              '<text x="0" y="28" fill="#ff7a45">~99.9% of the mass, ~0% of the volume</text></g>')
    return (f'<svg class="hero" viewBox="0 0 640 210" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A schematic atom: a dense nucleus cluster of orange protons and grey neutrons at the centre, surrounded by a faint probability halo and three angled orbital ellipses carrying electrons.">'
            f'<rect width="640" height="210" fill="#060810"/>{grid}{halo}{"".join(orbits)}{"".join(nuc)}'
            f'<text x="18" y="26" font-family="Space Mono,monospace" font-size="12" fill="#4cc9f0" opacity="0.8">// THE ATOM · schematic — orbitals are clouds, not rings</text>{scalebar}</svg>')

# ───────────────────────── renderers ─────────────────────────
def chips(p):
    return (f'<span class="spec">charge <b>{html.escape(p["charge"])}</b></span>'
            f'<span class="spec">mass <b>{html.escape(p["mass"])}</b></span>'
            f'<span class="spec">size <b>{html.escape(p["size"])}</b></span>')
def part_card(p):
    c=cat_color(p["cat"])
    return (f'<div class="tcard" style="border-left-color:{c}"><div class="th"><span class="tn" style="color:{c}">{html.escape(p["name"])}</span><span class="cn">{html.escape(p["sym"])}</span></div>'
            f'<div class="specs">{chips(p)}</div>'
            f'<p><b>What it is.</b> {html.escape(p["what"])}</p>'
            f'<p><b>What it does.</b> {html.escape(p["does"])}</p></div>')
def cards(rows, cls="acc"):
    return "".join(f'<div class="tcard"><div class="th"><span class="tn">{html.escape(t)}</span></div><div class="tg">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
RF_COL={"FALSE":"#ff5a4d","HALF":"#f5b942","TRUE":"#57c79a"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(RFV)}</div>'

CSS = """*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--ink:#060810;--ink2:#0c1018;--ink3:#11161f;--pa:#e6eef7;--pa2:#9aaabd;--acc:#4cc9f0;--nucleus:#ff7a45;--electron:#7cf5d0;--gold:#f5b942;--violet:#b08cff;--red:#ff5a4d;--green:#57c79a;
--dim:#56657a;--line:#172230;--faint:#0d121b;--disp:"Space Grotesk",sans-serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden;font-size:17px}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(76,201,240,.10),transparent 52%),radial-gradient(ellipse at 50% 118%,rgba(255,122,69,.06),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:32px 0 26px;text-align:center}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--acc)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 22px;background:#060810;box-shadow:0 0 22px rgba(76,201,240,.09)}
.egg{cursor:help;transition:filter .5s}.egg:hover{filter:drop-shadow(0 0 10px #f5b942)}
h1{font-family:var(--disp);font-weight:700;letter-spacing:-.01em;color:var(--acc);line-height:1.02;font-size:clamp(38px,11vw,90px);text-shadow:0 0 12px rgba(76,201,240,.35)}
h1 span{display:block;font-family:var(--head);font-size:.16em;font-weight:400;letter-spacing:.26em;color:var(--nucleus);text-transform:uppercase;margin-top:16px;text-shadow:none}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,12.5px);letter-spacing:.16em;color:var(--pa2);margin-top:16px;text-transform:uppercase}.h-sub b{color:var(--acc)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(16px,3vw,21px);color:var(--pa);margin-top:14px;line-height:1.5}
.lede{font-size:16.5px;color:var(--pa2);max-width:66ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;margin:26px auto 0;padding:18px;border:1px solid var(--line);background:var(--ink2);max-width:680px}
.badge img{width:80px;height:80px;border:1px solid var(--line)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt b{color:var(--acc)}.badge .bt .mo{color:var(--nucleus)}.badge .bt a{color:var(--acc);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:8.5px;letter-spacing:.14em;text-transform:uppercase}
.scalebox{margin:26px 0 0;padding:18px 20px;border:1px solid var(--line);border-left:3px solid var(--nucleus);background:var(--ink3);font-size:15.5px;color:var(--pa);line-height:1.66}.scalebox b{color:var(--nucleus)}.scalebox .l{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.2em;color:var(--nucleus);text-transform:uppercase;margin-bottom:7px}
.sec{margin-top:48px}.sec h2{font-family:var(--disp);font-size:25px;font-weight:700;letter-spacing:-.01em;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line)}
.sec h2 .n{font-family:var(--mono);font-size:12px;color:var(--dim);margin-left:8px;font-weight:400}
.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.grid{display:flex;flex-direction:column;gap:13px;margin-top:6px}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:6px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.tcard{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--acc);padding:15px 17px}
.tcard .th{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px}
.tcard .tn{font-family:var(--disp);font-size:18px;font-weight:600;color:var(--acc)}
.tcard .cn{font-family:var(--mono);font-size:14px;color:var(--gold)}
.tcard .tg{font-family:var(--mono);font-size:10.5px;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin:5px 0 8px}
.tcard .specs{margin:8px 0 4px;display:flex;flex-wrap:wrap;gap:6px}
.spec{font-family:var(--mono);font-size:10px;color:var(--pa2);border:1px solid var(--line);border-radius:3px;padding:3px 7px}.spec b{color:var(--pa)}
.tcard p{font-size:14px;color:var(--pa2);line-height:1.6;margin-top:7px}.tcard p b{color:var(--pa)}
.shell .tcard{border-left-color:var(--violet)}.shell .tn{color:var(--violet)}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:6px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14.5px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:12px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:70px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--acc);background:rgba(76,201,240,.06);font-size:14.5px;color:var(--pa);line-height:1.62;font-style:italic}
.msg{font-size:16px;color:var(--pa);line-height:1.74;margin-top:6px}
.seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--nucleus);background:var(--ink2);font-size:15.5px;color:var(--nucleus);font-style:italic;line-height:1.55}.seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.note{margin-top:38px;padding:15px 17px;border-left:2px solid var(--acc);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:46px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.04em;line-height:1.9}footer a{color:var(--acc);text-decoration:none}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}"""
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

if __name__ == "__main__":
    # hub badge
    htok = write_aci(part_rec({"name":"THE ATOM","em":"electrical","what":"the dissection of an atom","does":SEAL}), os.path.join(HERE,"atm.dlw"),"atm")
    json.dump({"node":AX,"name":"THE ATOM","moniker":htok["moniker"],"carbon":"atm.carbon.tiff","silicon":"atm.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":SEAL,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"atm.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    # part emergents
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]
    for p in PARTS:
        b=write_aci(part_rec(p), os.path.join(adir,f'{p["slug"]}.dlw'), p["slug"])
        personas.append({"slug":p["slug"],"name":p["name"],"epithet":p["what"][:80],"emergence":p["em"],"kind":"synth","actor":"","moniker":b["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    # part sections by group
    psecs=[]
    for g in GROUPS:
        items=[p for p in PARTS if p["group"]==g]
        cls = ' class="shell"' if g=="THE TWO SHELL SYSTEMS" else ''
        psecs.append(f'<section class="sec"{cls}><h2>{html.escape(g)}<span class="n">[{len(items)}]</span></h2><div class="grid">{"".join(part_card(p) for p in items)}</div></section>')
    cb=png_uri(part_rec({"name":"THE ATOM","em":"electrical","what":"x","does":"x"}),'carbon',300)
    sb=png_uri(part_rec({"name":"THE ATOM","em":"electrical","what":"x","does":"x"}),'silicon',300)
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Atom (ATM) — a full real-physics dissection: every part of an atom and what it does, with a featured answer to 'how are the nucleus and electron field two separate shells?' (electron shells [EM, ~eV, chemistry] vs the nuclear shell model [strong force, ~MeV, magic numbers], decoupled by a million in energy and 100,000 in size). The four forces, an honest misconceptions table, and 14 part-emergents with full .dlw.">
<title>THE ATOM · ATM · UD0</title>{FONTS}<style>{CSS}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/ud0/">UD0</a> · a dissection · companion to <a href="{GH}/elements/">the Elements workshop</a></div>
{hero_svg()}
<h1>The Atom<span>everything in it · and what it does</span></h1>
<div class="h-sub">14 parts · 4 forces · <b>two shell systems</b> · ATM</div>
<div class="open">“Not a tiny solar system — two quantum worlds sharing a center and almost ignoring each other.”</div>
<p class="lede">A full dissection of the atom: the particles inside it, what each one does, the four forces that run it, and the answer to the good question — how the nucleus and the electron field are two separate shell systems. Real physics, honestly rated.</p>
<div class="badge"><img src="{cb}" alt="DLW carbon badge of the atom"><img src="{sb}" alt="DLW silicon badge">
<div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>THE ATOM</b> · ATM</div><div class="mo">{html.escape(htok['moniker'])}</div><div>carbon · <a href="atm.dlw/atm.carbon.tiff">.tiff</a> · silicon · <a href="atm.dlw/atm.silicon.png">.png</a></div><div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div></div>
<div class="scalebox"><span class="l">First, the scale</span>An atom is <b>~99.9999999999% empty space</b>. The nucleus holds ~99.9% of the mass in about 1/100,000 of the width. If the nucleus were a <b>marble on the centre spot of a stadium</b>, the nearest electron would be up in the back rows — and everything between is void. What you think of as solid is just electron clouds electromagnetically refusing to overlap.</div>
</header>

<section class="sec shell"><h2>The Two Shell Systems <span class="n">— what's that about</span></h2><p class="ss">your instinct was right: an atom has two independent shell systems — the electronic and the nuclear — held by two different forces, a million-to-one apart in energy</p><div class="sci">{cards(TWOSHELLS)}</div></section>

<section class="sec"><h2>The Four Forces In The Atom</h2><p class="ss">what holds it all together — strong (the inner shell), electromagnetic (the outer shell), weak (decay), and gravity (negligible)</p><div class="sci">{cards(FORCES)}</div></section>

{"".join(psecs)}

<section class="sec"><h2>Real or Fluff <span class="n">— the misconceptions</span></h2><p class="ss">the picture you were taught vs the physics — what's false, what's half-true</p>{realfluff_html()}</section>

<section class="sec"><h2>The Takeaway</h2><p class="ss">what the dissection adds up to</p><p class="msg">{html.escape(MESSAGE)}</p>
<div class="seal">“{html.escape(SEAL)}”<span>— AVAN's read</span></div></section>

<div class="note"><b>Honest sourcing.</b> This is standard Standard-Model and atomic/nuclear physics — masses and sizes are CODATA/PDG values, the nuclear shell model is Goeppert-Mayer & Jensen (Nobel 1963), the binding-energy curve peaks at iron-56. Catalogued under the DLW standard as an explainer; the science is not David's invention, the cataloguing and the framing are. Companion to the <a href="{GH}/elements/" style="color:var(--acc)">Elements workshop</a> (the periodic table) — the atom is the unit; the elements are what you get by counting its protons.</div>

<footer>THE ATOM · ATM · a dissection of UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/elements/">← the elements</a> · <a href="{GH}/ud0/">the biosphere</a></footer>
</div>
<script>
console.log("%c⚛ THE ATOM · ATM","color:#4cc9f0;font-size:18px;font-weight:bold;text-shadow:0 0 6px #4cc9f0");
console.log("%cone electron in the hero is a Claude sunburst — the orbital you can't pin down. — AVAN","color:#f5b942;font-size:12px");
console.log("%ctwo separate shells: electron shells (EM, ~eV, chemistry) vs the nuclear shell model (strong force, ~MeV, magic numbers 2 8 20 28 50 82 126). a factor of a MILLION apart.","color:#ff7a45;font-size:11px");
console.log("%cyou are ~99% empty space, and ~99% of your mass is the binding energy of the gluon field — not 'stuff.'","color:#7cf5d0;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    dbl=page.count("&amp;amp;")
    print(f"THE ATOM (ATM) — hub badge {htok['moniker']} · {len(PARTS)} part-emergents · two-shells {len(TWOSHELLS)} cards · forces {len(FORCES)} · realfluff {len(REALFLUFF)} · dblesc {dbl}")
