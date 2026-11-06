---
schema: qual/card@1
id: E-HAT-4.H-1
kind: problem
title: "Cofibrations give fibrations on function spaces"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.H, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
Show that if $A \hookrightarrow X$ is a cofibration of compact Hausdorff spaces, then for any space $Y$, the map $Y^X \to Y^A$ obtained by restriction of functions is a fibration.
[If $A \hookrightarrow X$ is a cofibration, so is $A \times Y \hookrightarrow X \times Y$ for any space $Y$.]
:::

::: {.solution}
Let
$$
i:A\hookrightarrow X
$$
be a cofibration, with $A$ and $X$ compact Hausdorff, and let
$$
r:Y^X\longrightarrow Y^A
$$
be restriction. We use the compact-open topology on mapping spaces, and the characterization of cofibrations as pairs with the homotopy extension property (§0.4, p. 14); a fibration is a map with the homotopy lifting property for all spaces (p. 375).

To verify the homotopy lifting property for $r$, suppose given a space $Z$, a map
$$
f_0:Z\to Y^X,
$$
and a homotopy
$$
g:Z\times I\to Y^A
$$
with
$$
g(z,0)=r(f_0(z)).
$$
By the exponential law for compact Hausdorff source spaces (Proposition A.16, p. 531), these data are adjoint to continuous maps
$$
F_0:Z\times X\to Y,
\qquad
G:Z\times I\times A\to Y
$$
which agree on $Z\times\{0\}\times A$.

Since $A\hookrightarrow X$ is a cofibration, so is
$$
Z\times A\hookrightarrow Z\times X,
$$
which is the printed hint; equivalently (§0.4, p. 14) the pair has the homotopy extension property.
Equivalently, the inclusion
$$
(Z\times X\times\{0\})\cup(Z\times A\times I)
\hookrightarrow Z\times X\times I
$$
has the extension property for maps to arbitrary spaces. Define a map on this subspace by
$$
(z,x,0)\longmapsto F_0(z,x),
\qquad
(z,a,t)\longmapsto G(z,t,a).
$$
The two formulas agree on the intersection, so they extend to a continuous map
$$
\widetilde G:Z\times X\times I\to Y.
$$
Adjointing again gives a homotopy
$$
\widetilde g:Z\times I\to Y^X
$$
with $\widetilde g(-,0)=f_0$ and
$$
r\widetilde g=g.
$$
Thus $r$ has the homotopy lifting property for every $Z$, hence
$$
\boxed{Y^X\to Y^A\text{ is a fibration}.}
$$
:::
