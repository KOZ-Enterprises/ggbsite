#!/usr/bin/env python3
"""Site figures for the ggBleed and ggPack project pages, drawn in the site palette.

Runs against the live models, so re-run it when results change:

  uv run --project ~/ggPack python script/ecs_figures.py

ggPack's environment also installs ggBleed (editable path dependency), so one run covers both.
Writes assets/imgs/project/ggbleed-mission.png and ggpack-validation.png.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ggbleed.system.engine_bleed import EngineBleedPrecoolerSystem
from ggbleed.system.flight_envelope import FlightMissionProfile
from ggpack.validation import run_validation
from matplotlib import font_manager

OUT = Path(__file__).resolve().parents[1] / "assets/imgs/project"

# Site tokens (_sass/_tokens.scss). Series slots are the gg-theme validated categorical pair.
SURFACE, RULE, BORDER = "#1a1e1e", "#1f2a2a", "#2e4c5b"
INK, BODY, MUTED = "#fafafa", "#b9c4c4", "#8a9696"
SERIES = ["#9085e9", "#d95926"]  # violet, orange (validate_palette.js: dark, #1a1e1e, pass)
BAND = "#2a3434"  # neutral reference band, darker than any series

for f in Path.home().glob(".local/share/fonts/gg/*.ttf"):
    font_manager.fontManager.addfont(str(f))
plt.rcParams.update(
    {
        "font.family": "Roboto",
        "font.size": 13,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "axes.edgecolor": BORDER,
        "axes.labelcolor": BODY,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": BODY,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": RULE,
        "grid.linewidth": 1,
    }
)


def title(fig, ax, head, sub):
    fig.text(0.03, 0.955, head, fontsize=17, fontweight="bold", color=INK)
    fig.text(0.03, 0.91, sub, fontsize=12.5, color=MUTED)


def bleed_figure():
    pts = FlightMissionProfile.get_full_mission_profile(total_duration_s=600.0)
    tel = EngineBleedPrecoolerSystem().run_mission(pts)
    t = [p.time_s for p in tel]
    sensed = [p.t_sense_f for p in tel]

    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=150)
    fig.subplots_adjust(left=0.09, right=0.74, top=0.8, bottom=0.12)
    ax.axhspan(390, 440, color=BAND, lw=0, zorder=0)
    ax.text(603, 415, "Control band\n390–440 °F (B3)", va="center", fontsize=11.5, color=BODY)
    for y, label in [(450, "PRSOV limit 450 °F (B3)"), (490, "Overheat trip 490 °F (B3)")]:
        ax.axhline(y, color=MUTED, lw=1.2, ls=(0, (4, 3)), zorder=1)
        ax.text(603, y, label, va="center", fontsize=11.5, color=BODY)
    ax.plot(t, sensed, color=SERIES[0], lw=2, zorder=3)
    for x, label in [
        (50, "Takeoff & climb"),
        (240, "Cruise"),
        (320, "Anti-ice"),
        (385, "Descent"),
        (480, "Approach"),
    ]:
        ax.axvline(x, color=BORDER, lw=1, zorder=1)
        ax.text(x + 4, 512, label, fontsize=11, color=MUTED, va="top")
    ax.set_xlim(0, 600)
    ax.set_ylim(300, 520)
    ax.set_xlabel("Mission time (s), time-compressed")
    ax.set_ylabel("Sensed precooler outlet (°F)")
    ax.grid(axis="x", visible=False)
    title(
        fig,
        ax,
        "Outlet temperature holds the published band in climb and cruise",
        "Sensed precooler outlet, ggBleed reference mission. Dips below at idle in descent.",
    )
    fig.savefig(OUT / "ggbleed-mission.png")
    plt.close(fig)


NAMES = {
    "phx_hot_out_T": "Primary HX outlet temp",
    "compressor_out_T": "Compressor outlet temp",
    "compressor_out_p": "Compressor outlet pressure",
    "shx_hot_out_T": "Secondary HX outlet temp",
    "condenser_hot_out_T": "Condenser outlet temp",
    "reheater_cold_out_T": "Reheater cold outlet temp",
    "turbine_outlet_T": "Turbine outlet temp",
    "discharge_T": "Pack discharge temp",
    "discharge_humidity": "Discharge humidity",
    "water_extracted": "Water extracted",
    "shaft_speed": "Shaft speed",
}


def pack_figure():
    res = [r for r in run_validation() if r.accuracy]
    rows = list(dict.fromkeys(r.station for r in res))
    y = {s: len(rows) - 1 - i for i, s in enumerate(rows)}

    fig, ax = plt.subplots(figsize=(9, 6.6), dpi=150)
    fig.subplots_adjust(left=0.27, right=0.97, top=0.78, bottom=0.11)
    ax.axvspan(-1, 1, color=BAND, lw=0, zorder=0)
    ax.text(0, len(rows) - 0.35, "within tolerance", ha="center", fontsize=11, color=BODY)
    ax.axvline(0, color=BORDER, lw=1, zorder=1)
    for case, color, dy, marker in [("P5", SERIES[0], 0.13, "o"), ("P18", SERIES[1], -0.13, "s")]:
        pts = [r for r in res if r.case == case]
        ax.scatter(
            [r.deviation / r.tolerance for r in pts],
            [y[r.station] + dy for r in pts],
            s=70,
            color=color,
            marker=marker,
            edgecolor=SURFACE,
            linewidth=2,
            zorder=3,
            label={"P5": "P5 ground reference case", "P18": "P18 second ground point"}[case],
        )
    ax.set_yticks(range(len(rows)), [NAMES[s] for s in reversed(rows)])
    ax.set_ylim(-0.6, len(rows) - 0.1)
    ax.set_xlim(-22, 4)
    ax.set_xlabel("Deviation from published value, in multiples of the P19 tolerance")
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0, labelcolor=BODY)
    leg = ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, frameon=False, fontsize=11.5, labelcolor=BODY)
    leg.set_zorder(4)
    n_in = sum(r.within for r in res)
    title(
        fig,
        ax,
        f"{n_in} of {len(res)} published-case checks within tolerance",
        "ggPack vs two published ground cases. Negative means the model runs cold.",
    )
    fig.savefig(OUT / "ggpack-validation.png")
    plt.close(fig)


if __name__ == "__main__":
    bleed_figure()
    pack_figure()
    print("wrote", OUT / "ggbleed-mission.png", OUT / "ggpack-validation.png")
