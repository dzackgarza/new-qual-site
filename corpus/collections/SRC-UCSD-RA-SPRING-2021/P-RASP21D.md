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

::: problem
Let $X, Y, Z$ be Banach spaces and $B : X \times Y \to Z$ be a map such that for any fixed $x \in X$, $B(x, \cdot) \in L(Y, Z)$ and for any fixed $y \in Y$, $B(\cdot, y) \in L(X, Z)$.
Show that there is $C$ such that $\|B(x,y)\| \leq C\|x\|\|y\|$.
:::

::: solution
<1>1. Build a pointwise-bounded family of operators on $Y$.
::: proof
For each $x\in X$ with $\|x\|\le1$, define
\[
T_x:Y\to Z,
\qquad
T_x(y)=B(x,y).
\]
By hypothesis, each $T_x$ belongs to $L(Y,Z)$.

Fix $y\in Y$. The map
\[
S_y:X\to Z,
\qquad
S_y(x)=B(x,y),
\]
belongs to $L(X,Z)$ by the other hypothesis. Hence
\[
\sup_{\|x\|\le1}\|T_x(y)\|
=\sup_{\|x\|\le1}\|S_y(x)\|
=\|S_y\|<\infty.
\]
Thus the family
\[
\mathcal F:=\{T_x:\|x\|\le1\}\subset L(Y,Z)
\]
is pointwise bounded.
:::

<1>2. Apply the Uniform Boundedness Principle.
::: proof
Because $Y$ is Banach, the Uniform Boundedness Principle yields
\[
C:=\sup_{\|x\|\le1}\|T_x\|<\infty.
\]
Equivalently,
\[
\|B(x,y)\|\le C\|y\|
\qquad
\text{whenever }\|x\|\le1.
\]
:::

<1>3. Rescale to arbitrary $x$ and $y$.
::: proof
If $x=0$ or $y=0$, separate linearity gives $B(x,y)=0$. Otherwise set
\[
u=\frac{x}{\|x\|}.
\]
Then $\|u\|=1$, and linearity in the first variable gives
\[
\begin{aligned}
\|B(x,y)\|
&=\|x\|\,\|B(u,y)\|\\
&\le C\|x\|\|y\|.
\end{aligned}
\]
Therefore
\[
\boxed{\|B(x,y)\|\le C\|x\|\|y\|\quad\text{for all }x\in X,\ y\in Y.}
\]
:::
:::
