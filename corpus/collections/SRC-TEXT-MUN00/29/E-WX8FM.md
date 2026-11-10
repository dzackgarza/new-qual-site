---
schema: qual/card@1
id: E-WX8FM
kind: problem
title: Homeomorphisms extend to one-point compactifications
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 5, printed p. 186; the stored
    statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.5, PDF p. 22. Extending f by sending the point
    at infinity to the point at infinity gives a bijection which is open, the image of the
    complement of a compact set being the complement of a compact set, and symmetrically.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

If $f: X_1 \to X_2$ is a homeomorphism of locally compact Hausdorff spaces, show $f$ extends to a homeomorphism of their one-point compactifications.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.5, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the extension map and the openness argument are theirs.

Let $X_{1}^{+}=X_{1}\cup\{\infty_{1}\}$ and $X_{2}^{+}=X_{2}\cup\{\infty_{2}\}$ be the one-point compactifications and define $g:X_{1}^{+}\to X_{2}^{+}$ by $g\restrict X_{1}=f$ and $g(\infty_{1})=\infty_{2}$; it is a bijection.

$g$ is open. Let $U\subset X_{1}^{+}$ be open. If $U\subset X_{1}$ then $U$ is open in $X_{1}$ and $g(U)=f(U)$ is open in $X_{2}$ (a homeomorphism is open), hence open in $X_{2}^{+}$. Otherwise $\infty_{1}\in U$, so $X_{1}^{+}-U$ is a compact subset $C$ of $X_{1}$ and $U=X_{1}^{+}-C$; then
$$
g(U)=X_{2}^{+}-g(C)=X_{2}^{+}-f(C),
$$
and $f(C)$ is compact, hence closed in the Hausdorff space $X_{2}^{+}$: so $g(U)$ is open. By symmetry (apply the same argument to $g^{-1}$) $g$ is a homeomorphism.
:::
