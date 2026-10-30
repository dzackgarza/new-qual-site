---
schema: qual/card@1
id: P-PRACT20-W5-34
kind: problem
title: Nonconstant entire functions have dense image
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 34).
---

::: {.problem}
Suppose that $f : \CC \to \CC$ is non-constant and entire. Prove that the image of $f$ is dense in $\CC$; that is, for arbitrary $z_0 \in \CC$ and $\varepsilon > 0$, show that there exists $z \in \CC$ such that $\abs{f(z) - z_0} < \varepsilon$. [Note: this is a weaker version of Picard’s Little Theorem which says that the image of $f$ omits at most one point in $\CC$; you should prove this directly without reference to Picard’s Little Theorem.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, toward a contradiction, that the image of $f$ is not dense in
$\CC$. Then there exist $z_0\in\CC$ and $\varepsilon>0$ such that
$$
\abs{f(z)-z_0}\ge\varepsilon
\qquad(z\in\CC).
$$


::: pf-proof

If $f(\CC)$ is not dense, its closure is a proper closed subset of
$\CC$. Choose
$$
z_0\notin\overline{f(\CC)}.
$$
The complement of the closure is open, so some disk
$$
B_\varepsilon(z_0)
$$
is disjoint from $f(\CC)$. This is exactly the displayed inequality.

:::

:::

::: {.pf-step #s1-2}

The function
$$
g(z)=\frac1{f(z)-z_0}
$$
is entire and bounded.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(z)-z_0\ne0
$$
for every $z$, so $g$ is entire. The same inequality gives
$$
\abs{g(z)}
=
\frac1{\abs{f(z)-z_0}}
\le
\frac1{\varepsilon}.
$$
Thus $g$ is bounded.

:::

:::

::: {.pf-step #s1-3}

The function $g$ is constant.


::: pf-proof

By step [](#s1-2){.pf-ref}, $g$ is bounded and entire. Liouville's theorem therefore
implies that $g$ is constant.

:::

:::

::: {.pf-step #s1-4}

The conclusion of step [](#s1-3){.pf-ref} forces $f$ to be constant.


::: pf-proof

If
$$
g(z)=c,
$$
then $c\ne0$ and
$$
\frac1{f(z)-z_0}=c.
$$
Hence
$$
f(z)=z_0+\frac1c,
$$
which is constant.

:::

:::

::: {.pf-step #s1-5}

Therefore $f(\CC)$ is dense in $\CC$.


::: pf-proof

Step [](#s1-4){.pf-ref} contradicts the hypothesis that $f$ is nonconstant. Thus the
assumption in step [](#s1-1){.pf-ref} is false. Equivalently, for every $z_0\in\CC$
and every $\varepsilon>0$, there exists $z\in\CC$ such that
$$
\boxed{\abs{f(z)-z_0}<\varepsilon}.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required density statement.

:::

:::

:::
