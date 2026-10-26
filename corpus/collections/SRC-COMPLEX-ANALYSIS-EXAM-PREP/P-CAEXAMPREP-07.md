---
schema: qual/card@1
id: P-CAEXAMPREP-07
kind: problem
title: Uniqueness of a right-half-plane zero of $z+e^{-z}-2$
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Show that there is exactly one point $z$ in the right half-plane $\{z:\operatorname{Re}z>0\}$ satisfying
\[
z+e^{-z}=2.
\]

Hint: use a contour in the right half-plane bounded by a large semicircle and a vertical line $\operatorname{Re}z=\varepsilon$, with $R>3$ and $\varepsilon>0$ small, so in particular the ball of radius $1$ centered at $2$ lies inside the contour.
:::

Set
\[
f(z)=z+e^{-z}-2,
\qquad
g(z)=z-2.
\]
For \(0<\varepsilon<1\) and \(R>3\), let
\[
D_{R,\varepsilon}
=\{z\in\mathbb C:\operatorname{Re}z>\varepsilon,\ |z|<R\}.
\]

::: pf

::: pf-step

On \(\partial D_{R,\varepsilon}\),
\[
|f(z)-g(z)|<|g(z)|.
\]


::: pf-proof

Since \(f-g=e^{-z}\) and every point of \(\partial D_{R,\varepsilon}\) has \(\operatorname{Re}z\ge\varepsilon\),
\[
|f(z)-g(z)|=e^{-\operatorname{Re}z}\le e^{-\varepsilon}<1.
\]
On the vertical part of the boundary, \(\operatorname{Re}z=\varepsilon\), so
\[
|z-2|\ge 2-\varepsilon>1.
\]
On the circular part, \(|z|=R\), so the reverse triangle inequality gives
\[
|z-2|\ge R-2>1.
\]
Thus \(|f-g|<1<|g|\) everywhere on the boundary.

:::

:::

::: pf-step

The function \(f\) has exactly one zero in \(D_{R,\varepsilon}\), counted with multiplicity.


::: pf-proof

By step <1>1 and Rouché's theorem, \(f\) and \(g\) have the same number of zeros in \(D_{R,\varepsilon}\), counted with multiplicity. The function \(g(z)=z-2\) has exactly one zero, namely \(2\), and \(2\in D_{R,\varepsilon}\) because \(\varepsilon<1<2<R\). Hence \(f\) has exactly one zero there.

:::

:::

::: pf-step

The function \(f\) has at least one zero in the right half-plane.


::: pf-proof

For example, step <1>2 applied with \(\varepsilon=1/2\) and \(R=4\) gives one zero in \(D_{4,1/2}\), which is contained in \(\{\operatorname{Re}z>0\}\).

:::

:::

::: pf-step

The function \(f\) has at most one zero in the right half-plane.


::: pf-proof

Suppose \(z_1\) and \(z_2\) were two distinct zeros with positive real part. Choose
\[
0<\varepsilon<\min\{1,\operatorname{Re}z_1,\operatorname{Re}z_2\}
\]
and
\[
R>\max\{3,|z_1|,|z_2|\}.
\]
Then both zeros lie in \(D_{R,\varepsilon}\), contradicting step <1>2, which says that this domain contains only one zero even when multiplicity is counted.

:::

:::

::: pf-step

Therefore there is exactly
\[
\boxed{1}
\]
point \(z\) with \(\operatorname{Re}z>0\) satisfying \(z+e^{-z}=2\).


::: pf-proof

Such a point exists by step <1>3 and is unique by step <1>4.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
