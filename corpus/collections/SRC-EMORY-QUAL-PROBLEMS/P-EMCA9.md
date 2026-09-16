---
schema: qual/card@1
id: P-EMCA9
kind: problem
title: Nonconstant entire functions have dense image
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Casorati-Weierstrass
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (9) of Arango-Piñeros, Some quals problems; merged the duplicate E-N6PDJ, whose solution repeats this Liouville argument."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "JHU Spring 2015 poses the same problem; merged its duplicate card P-8XT37, whose solution is the same Liouville argument, and that sitting now lists this card."
---

::: problem
If $f$ is a non-constant entire function, then $f(\mathbf{C})$ is dense in the plane.
:::

::: solution
Suppose that $f(\mathbb C)$ were not dense in $\mathbb C$. Then there would be
a point $a\in\mathbb C$ and an $r>0$ such that
\[
B(a,r)\cap f(\mathbb C)=\varnothing.
\]
Thus
\[
|f(z)-a|\ge r\qquad\text{for every }z\in\mathbb C.
\]
The function
\[
g(z)=\frac1{f(z)-a}
\]
is therefore entire and bounded by $1/r$. By Liouville's theorem, $g$ is
constant. Hence $f$ is constant, contradicting the hypothesis.

Therefore every nonempty open disk meets $f(\mathbb C)$, so $f(\mathbb C)$ is
dense in the plane.
:::
