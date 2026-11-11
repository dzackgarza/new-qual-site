---
schema: qual/card@1
id: E-WOS95
kind: problem
title: Induced homomorphisms up to base-point change
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 52: Problem 6 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-52-the-fundamental-group/problem-6-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-52-the-fundamental-group/problem-6-solution.txt), and against Munkres, Topology (2000), Section 52
    Exercise 6, printed p. 335. dbFin evaluates both sides at a class and uses h of alpha-bar equals beta-bar; the card is the same computation. Nothing needed repair.
---

::: {.exercise}

Show that if $X$ is path connected, the homomorphism induced by a continuous map is independent of base point, up to isomorphisms of the groups involved.
More precisely, let $h: X \to Y$ be continuous, with $h(x_0) = y_0$ and $h(x_1) = y_1$.
Let $\alpha$ be a path in $X$ from $x_0$ to $x_1$, and let $\beta = h \circ \alpha$.
Show that

$$
\hat{\beta} \circ (h_{x_0})_* = (h_{x_1})_* \circ \hat{\alpha}.
$$

This equation expresses the fact that the following diagram of maps "commutes."

$$
\begin{array}{c}
\pi_1(X, x_0) \xrightarrow{\ (h_{x_0})_*\ } \pi_1(Y, y_0) \\
\Biggl\downarrow \hat{\alpha} \qquad\qquad\qquad\quad \Biggl\downarrow \hat{\beta} \\
\pi_1(X, x_1) \xrightarrow{\ (h_{x_1})_*\ } \pi_1(Y, y_1)
\end{array}
$$
:::

::: {.solution}
Let $[f]\in\pi_1(X,x_0)$. By definition,
$$
\widehat\alpha([f])=[\bar\alpha*f*\alpha].
$$
Applying $(h_{x_1})_*$ gives
$$
(h_{x_1})_*\widehat\alpha([f])
=[h\circ\bar\alpha*(h\circ f)*(h\circ\alpha)].
$$
Since $\beta=h\circ\alpha$, we have $h\circ\bar\alpha=\bar\beta$. Hence
$$
(h_{x_1})_*\widehat\alpha([f])
=[\bar\beta*(h\circ f)*\beta].
$$
On the other hand,
$$
\widehat\beta (h_{x_0})_*([f])
=\widehat\beta([h\circ f])
=[\bar\beta*(h\circ f)*\beta].
$$
Thus the two maps agree on every class:
$$
\boxed{\widehat\beta\circ(h_{x_0})_*=(h_{x_1})_*\circ\widehat\alpha}.
$$
Since change-of-basepoint maps are isomorphisms, this proves that the homomorphism induced by $h$ is independent of the chosen basepoint up to the canonical basepoint-change isomorphisms.
:::
