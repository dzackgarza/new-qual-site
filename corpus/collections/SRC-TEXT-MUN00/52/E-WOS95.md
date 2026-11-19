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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the computation as a Lamport proof against the retained set: dbFin, "Section 52:
    Problem 6 Solution" (tmp/sources/dbfin/section-52-the-fundamental-group/problem-6-solution.txt),
    read again in its text version. The steps are dbFin's evaluation of both maps at a class, split
    into the definition of the base-point change map, the effect of the induced homomorphism on a
    concatenation of three paths, the identity h o alpha-bar = beta-bar, and the two sides computed
    separately. The converse direction is not needed: the exercise asks for the equation, and the
    closing step records that on a path connected X the change-of-basepoint maps are isomorphisms
    (Theorem 52.1), which is what makes the induced homomorphism independent of the base point up
    to them. No defect found in the statement or in the proof.
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
The computation is **dbFin, "Section 52: Problem 6 Solution"** (`tmp/sources/dbfin/section-52-the-fundamental-group/problem-6-solution.txt`): both sides evaluated at a class and the identity $h\circ\bar\alpha=\bar\beta$ used. Write $*$ for concatenation of paths, $\bar\alpha$ for the reverse of $\alpha$, and $\hat\alpha$ for the base-point change map $[f]\mapsto[\bar\alpha*f*\alpha]$.

::: pf

::: {.pf-step #left-side}
For every $[f]\in\pi_{1}(X,x_{0})$, $\hat\beta\,(h_{x_{0}})_{*}([f])=[\bar\beta*(h\circ f)*\beta]$.

::: pf-proof
The induced homomorphism sends $[f]$ to $[h\circ f]$, and $\hat\beta$ sends that class to $[\bar\beta*(h\circ f)*\beta]$ by its definition. No other ingredient enters.
:::

:::

::: {.pf-step #reverse}
$h\circ\bar\alpha=\bar\beta$.

::: pf-proof
The reverse path $\bar\alpha$ is $s\mapsto\alpha(1-s)$, so $h\circ\bar\alpha$ is $s\mapsto h(\alpha(1-s))$, which is the reverse of $s\mapsto h(\alpha(s))=\beta(s)$, that is, $\bar\beta$.
:::

:::

::: {.pf-step #right-side}
For every $[f]\in\pi_{1}(X,x_{0})$, $(h_{x_{1}})_{*}\hat\alpha([f])=[\bar\beta*(h\circ f)*\beta]$.

::: pf-proof
By the definition of $\hat\alpha$, $\hat\alpha([f])=[\bar\alpha*f*\alpha]$, and a map of spaces carries a concatenation to the concatenation of the images, so $(h_{x_{1}})_{*}\hat\alpha([f])=[h\circ\bar\alpha*(h\circ f)*(h\circ\alpha)]$. Step [](#reverse){.pf-ref} rewrites the first factor as $\bar\beta$ and the hypothesis $\beta=h\circ\alpha$ rewrites the last as $\beta$.
:::

:::

::: {.pf-step #answer}
$\boxed{\hat\beta\circ(h_{x_{0}})_{*}=(h_{x_{1}})_{*}\circ\hat\alpha}$ on $\pi_{1}(X,x_{0})$, and since $X$ is path connected the two change-of-basepoint maps are isomorphisms.

::: pf-proof
Steps [](#left-side){.pf-ref} and [](#right-side){.pf-ref} compute the two composites at an arbitrary class $[f]\in\pi_{1}(X,x_{0})$ and obtain the same class, so the two homomorphisms agree. On a path connected $X$ the map $\hat\alpha$ is an isomorphism (Theorem 52.1), and the same holds for $\hat\beta$, so the equation says that $(h_{x_{0}})_{*}$ and $(h_{x_{1}})_{*}$ differ by the canonical isomorphisms of base-point change, which is the independence the exercise asks for.
:::

:::

:::
:::
