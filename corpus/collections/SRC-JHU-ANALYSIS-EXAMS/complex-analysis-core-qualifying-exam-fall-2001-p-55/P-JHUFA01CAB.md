---
schema: qual/card@1
id: P-JHUFA01CAB
kind: problem
title: The unique right-half-plane solution of $z-\alpha=e^{-z}$ is real
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the real parameter alpha>1, right-half-plane restriction, uniqueness, and reality conclusion with Fall 2001 Complex Analysis problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Localized every right-half-plane solution in the unit disk centered at alpha, applied strict Rouche dominance there, and used conjugation symmetry plus uniqueness to force the root to be real."
---

::: {.problem}
Problem 2. Fix a real number $\alpha > 1$ . Show that the equation $z - \alpha = e ^ { - z }$ has precisely one solution in the half plane $\mathrm { R e } ( z ) > 0$ and that this solution must be real.
:::

::: solution
<1>1. Every right-half-plane solution lies in the disk $|z-\alpha|<1$.
::: proof
If $z$ satisfies
$$
z-\alpha=e^{-z}
$$
and $\operatorname{Re}z>0$, then
$$
|z-\alpha|=|e^{-z}|=e^{-\operatorname{Re}z}<1.
$$
Thus every required solution lies in
$$
B=\{z:|z-\alpha|<1\}.
$$
Conversely, because $\alpha>1$, every point of the closed disk
$|z-\alpha|\le1$ has
$$
\operatorname{Re}z\ge\alpha-1>0.
$$
Hence every zero found in $B$ is automatically in the required half-plane.
:::

<1>2. Rouché's theorem gives exactly one solution in $B$.
::: proof
Let
$$
F(z)=z-\alpha-e^{-z}.
$$
On the boundary $|z-\alpha|=1$, one has
$\operatorname{Re}z\ge\alpha-1$, and therefore
$$
|e^{-z}|=e^{-\operatorname{Re}z}
\le e^{-(\alpha-1)}<1=|z-\alpha|.
$$
Thus Rouché's theorem shows that $F$ and $z-\alpha$ have the same number of
zeros in $B$, counted with multiplicity. The latter has exactly one simple
zero. Therefore $F$ has exactly one zero in $B$, counted with multiplicity.
Together with step <1>1, this is precisely one solution in the right half-plane.
:::

<1>3. The unique solution is real.
::: proof
The equation has real coefficients in the sense that
$$
\overline{F(z)}=F(\overline z).
$$
Hence if $z_0$ is a solution, then $\overline{z_0}$ is also a solution. The
right half-plane is invariant under complex conjugation, so both would lie in
the region counted in step <1>2. Uniqueness therefore gives
$$
z_0=\overline{z_0},
$$
which means $z_0$ is real.
:::
:::
