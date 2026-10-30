---
schema: qual/card@1
id: P-CAEXAMPREP-07
kind: problem
title: Uniqueness of a right-half-plane zero of $z+e^{-z}-2$
classification: {areas: [complex-analysis], topics: [Rouché's Theorem]}
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
$$
z+e^{-z}=2.
$$

Hint: use a contour in the right half-plane bounded by a large semicircle and a vertical line $\operatorname{Re}z=\varepsilon$, with $R>3$ and $\varepsilon>0$ small, so in particular the ball of radius $1$ centered at $2$ lies inside the contour.
:::

::: {.solution}

Set
$$
f(z)=z+e^{-z}-2,
\qquad
g(z)=z-2.
$$
For $0<\varepsilon<1$ and $R>3$, let
$$
D_{R,\varepsilon}
=\{z\in\CC:\operatorname{Re}z>\varepsilon,\ \abs{z}<R\}.
$$

::: pf

::: {.pf-step #s1-1}

On $\partial D_{R,\varepsilon}$,
$$
\abs{f(z)-g(z)}<\abs{g(z)}.
$$


::: pf-proof

Since $f-g=e^{-z}$ and every point of $\partial D_{R,\varepsilon}$ has $\operatorname{Re}z\ge\varepsilon$,
$$
\abs{f(z)-g(z)}=e^{-\operatorname{Re}z}\le e^{-\varepsilon}<1.
$$
On the vertical part of the boundary, $\operatorname{Re}z=\varepsilon$, so
$$
\abs{z-2}\ge 2-\varepsilon>1.
$$
On the circular part, $\abs{z}=R$, so the reverse triangle inequality gives
$$
\abs{z-2}\ge R-2>1.
$$
Thus $\abs{f-g}<1<\abs{g}$ everywhere on the boundary.

:::

:::

::: {.pf-step #s1-2}

The function $f$ has exactly one zero in $D_{R,\varepsilon}$, counted with multiplicity.


::: pf-proof

By step [](#s1-1){.pf-ref} and Rouché's theorem, $f$ and $g$ have the same number of zeros in $D_{R,\varepsilon}$, counted with multiplicity. The function $g(z)=z-2$ has exactly one zero, namely $2$, and $2\in D_{R,\varepsilon}$ because $\varepsilon<1<2<R$. Hence $f$ has exactly one zero there.

:::

:::

::: {.pf-step #s1-3}

The function $f$ has at least one zero in the right half-plane.


::: pf-proof

For example, step [](#s1-2){.pf-ref} applied with $\varepsilon=1/2$ and $R=4$ gives one zero in $D_{4,1/2}$, which is contained in $\{\operatorname{Re}z>0\}$.

:::

:::

::: {.pf-step #s1-4}

The function $f$ has at most one zero in the right half-plane.


::: pf-proof

Suppose $z_1$ and $z_2$ were two distinct zeros with positive real part. Choose
$$
0<\varepsilon<\min\{1,\operatorname{Re}z_1,\operatorname{Re}z_2\}
$$
and
$$
R>\max\{3,\abs{z_1},\abs{z_2}\}.
$$
Then both zeros lie in $D_{R,\varepsilon}$, contradicting step [](#s1-2){.pf-ref}, which says that this domain contains only one zero even when multiplicity is counted.

:::

:::

::: {.pf-step #s1-5}

Therefore there is exactly
$$
\boxed{1}
$$
point $z$ with $\operatorname{Re}z>0$ satisfying $z+e^{-z}=2$.


::: pf-proof

Such a point exists by step [](#s1-3){.pf-ref} and is unique by step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
