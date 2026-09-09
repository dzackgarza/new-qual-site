---
schema: qual/card@1
id: P-RASP26D
kind: problem
title: "Relative weak* openness of a set of probability measures"
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
  note: Checked against Problem 4 of the official UCSD Spring 2026 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\mathcal{M}([0,1])$ denote the space of all complex Radon measures on $[0,1]$, and $\mathcal{P}([0,1])$ the subset of probability measures.
Let $f : [0,1] \times [0,1] \to \mathbb{R}$ be a continuous function, and let $U$ be the set of all $\mu \in \mathcal{P}([0,1])$ satisfying
$$
\forall y \in [0,1] \qquad \left|\int_0^1 f(x, y)\,d\mu(x)\right| < 1.
$$
Prove that $U$ is a relatively open subset of $\mathcal{P}([0,1])$ with respect to the weak* topology.
:::

::: solution
Fix $\mu_0\in U$ and define
\[
F_{\mu_0}(y):=\int_0^1 f(x,y)\,d\mu_0(x).
\]

<1>1. Obtain a uniform margin below $1$.
::: proof
Because $f$ is continuous on the compact square $[0,1]^2$, it is uniformly continuous. Hence the map
\[
y\longmapsto f_y:=f(\cdot,y)
\]
from $[0,1]$ into $C([0,1])$ is continuous in the uniform norm.

Since $\mu_0$ is a probability measure,
\[
|F_{\mu_0}(y)-F_{\mu_0}(z)|
\le \|f_y-f_z\|_\infty,
\]
so $F_{\mu_0}$ is continuous. Because $\mu_0\in U$ and $[0,1]$ is compact,
\[
c:=\max_{y\in[0,1]}|F_{\mu_0}(y)|<1.
\]
Put
\[
\eta:=\frac{1-c}{4}>0.
\]
:::

<1>2. Reduce the parameter family to finitely many weak* test functions.
::: proof
The set
\[
K:=\{f_y:y\in[0,1]\}\subset C([0,1])
\]
is compact. Hence there exist $y_1,\ldots,y_N\in[0,1]$ such that for every $y\in[0,1]$ there is a $j$ with
\[
\|f_y-f_{y_j}\|_\infty<\eta.
\]

Consider the relative weak* neighborhood of $\mu_0$ in $\mathcal P([0,1])$ given by
\[
V:=\left\{
\mu\in\mathcal P([0,1]):
\left|\int f_{y_j}\,d\mu-\int f_{y_j}\,d\mu_0\right|<\eta
\text{ for }j=1,\ldots,N
\right\}.
\]
Each condition involves evaluation of the measure at one continuous function, so $V$ is relatively weak* open and contains $\mu_0$.
:::

<1>3. Show that $V\subset U$.
::: proof
Fix $\mu\in V$ and $y\in[0,1]$. Choose $j$ with
\[
\|f_y-f_{y_j}\|_\infty<\eta.
\]
Since both $\mu$ and $\mu_0$ are probability measures,
\[
\left|\int(f_y-f_{y_j})\,d\mu\right|<\eta,
\qquad
\left|\int(f_y-f_{y_j})\,d\mu_0\right|<\eta.
\]
Therefore
\[
\begin{aligned}
\left|\int f_y\,d\mu\right|
&\le
\left|\int(f_y-f_{y_j})\,d\mu\right|
+\left|\int f_{y_j}\,d\mu-\int f_{y_j}\,d\mu_0\right|\\
&\qquad+
\left|\int(f_{y_j}-f_y)\,d\mu_0\right|
+\left|\int f_y\,d\mu_0\right|\\
&<3\eta+c.
\end{aligned}
\]
Because
\[
3\eta+c
=c+\frac{3(1-c)}4
<1,
\]
we obtain
\[
\left|\int_0^1f(x,y)\,d\mu(x)\right|<1
\]
for every $y\in[0,1]$. Thus $\mu\in U$.

Hence every $\mu_0\in U$ has a relative weak* neighborhood contained in $U$, so
\[
\boxed{U\text{ is relatively weak* open in }\mathcal P([0,1]).}
\]
:::
:::
