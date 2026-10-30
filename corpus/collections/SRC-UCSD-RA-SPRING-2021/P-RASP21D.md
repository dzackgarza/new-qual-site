---
schema: qual/card@1
id: P-RASP21D
kind: problem
title: "Separate boundedness of a bilinear map implies joint boundedness"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X, Y, Z$ be Banach spaces and $B : X \times Y \to Z$ be a map such that for any fixed $x \in X$, $B(x, \cdot) \in L(Y, Z)$ and for any fixed $y \in Y$, $B(\cdot, y) \in L(X, Z)$.
Show that there is $C$ such that $\norm{B(x,y)} \leq C\norm{x}\norm{y}$.
:::

::: {.solution}

::: pf

::: pf-step

Build a pointwise-bounded family of operators on $Y$.

::: pf-proof

For each $x\in X$ with $\norm{x}\le1$, define
$$
T_x:Y\to Z,
\qquad
T_x(y)=B(x,y).
$$
By hypothesis, each $T_x$ belongs to $L(Y,Z)$.

Fix $y\in Y$. The map
$$
S_y:X\to Z,
\qquad
S_y(x)=B(x,y),
$$
belongs to $L(X,Z)$ by the other hypothesis. Hence
$$
\sup_{\norm{x}\le1}\norm{T_x(y)}
=\sup_{\norm{x}\le1}\norm{S_y(x)}
=\norm{S_y}<\infty.
$$
Thus the family
$$
\mathcal F:=\{T_x:\norm{x}\le1\}\subset L(Y,Z)
$$
is pointwise bounded.

:::

:::

::: pf-step

Apply the Uniform Boundedness Principle.

::: pf-proof

Because $Y$ is Banach, the Uniform Boundedness Principle yields
$$
C:=\sup_{\norm{x}\le1}\norm{T_x}<\infty.
$$
Equivalently,
$$
\norm{B(x,y)}\le C\norm{y}
\qquad
\text{whenever }\norm{x}\le1.
$$

:::

:::

::: pf-step

Rescale to arbitrary $x$ and $y$.

::: pf-proof

If $x=0$ or $y=0$, separate linearity gives $B(x,y)=0$. Otherwise set
$$
u=\frac{x}{\norm{x}}.
$$
Then $\norm{u}=1$, and linearity in the first variable gives
$$
\begin{aligned}
\norm{B(x,y)}
&=\norm{x}\,\norm{B(u,y)}\\
&\le C\norm{x}\norm{y}.
\end{aligned}
$$
Therefore
$$
\boxed{\norm{B(x,y)}\le C\norm{x}\norm{y}\quad\text{for all }x\in X,\ y\in Y.}
$$

:::

:::

:::

:::
