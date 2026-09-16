---
schema: qual/card@1
id: P-TRIV-LA48
kind: problem
title: Arranging three stars by spaceship rotations and boosts
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 48, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source depends on Figures 1 and 2 (ship rotations and star positions). Flash preserves only their captions/image placeholders, so the graphical data required to determine the command sequence is unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the editorial preamble and image placeholders with the Linear Algebra Problem 48 statement and descriptions of Figures 1 and 2 from pages 7-8 of the source PDF.
---

::: {.problem}
You are a spaceship pilot carrying a lonely watch in front of the main display while the rest of the crew sleep in anabiosis.
You can operate the spaceship by sending commands to the main computer.
You can rotate the ship by typing the commands *pitch angle* $\psi$, *yaw angle* $\theta$ and *roll angle* $\phi$ as shown on Fig. 1.
Besides, you can type the command *boost time* $T$, which turns the main engine on and accelerates the ship with the constant acceleration $g$ during the time $T$.
On the display, you see three bright stars around the point $O$ that depicts the longitudinal axis of the ship, see Fig. 2.
Give a series of commands that arrange them into a perfect triangle with the center $O$ and the side $d$.

Fig. 1 (pitch, yaw and roll of the ship) shows the ship along the axis $x$ with body axes $x, y, z$.
The pitch by $\psi$ turns $x$ and $y$ by the angle $\psi$ to $x'$ and $y'$, keeping $z$ fixed; the yaw by $\theta$ turns $x$ and $z$ by the angle $\theta$ to $x'$ and $z'$, keeping $y$ fixed; the roll by $\varphi$ turns $y$ and $z$ by the angle $\varphi$ to $y'$ and $z'$, keeping the longitudinal axis $x$ fixed.

Fig. 2 (positions of the stars), left panel: the three stars lie on the display at distances $r_1, r_2, r_3$ from $O$, at angles $\varphi_1 < \varphi_2 < \varphi_3$ measured from a horizontal line through $O$, all in the upper half of the display.
Right panel: the target configuration is an equilateral triangle with side $d$ centered at $O$, with a horizontal lower side and the third vertex above $O$.
:::
