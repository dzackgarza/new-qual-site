---
schema: qual/card@1
id: P-L4EMZ
kind: problem
title: Compactness of $\{0\}\cup\{1/n\}$ and of $(0,1]$
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the invalid infinite-implies-cofinite step in part (b) with the neighborhood-of-zero argument and structured all parts.
---

::: {.problem}
Let $X$ be a topological space.

a. State what it means for $X$ to be compact.

b. Let $X = \theset{0} \cup \theset{{1\over n} \mid n \in \ZZ^+ }$.
Is $X$ compact?

c. Let $X = (0, 1]$.
Is $X$ compact?
:::

::: {.concept}
See Munkres p.164, especially for (ii).
:::

::: {.solution}
<1>1. A topological space is compact if every open cover has a finite subcover.
::: {.proof}
This is the definition of compactness.
:::

<1>2. The space
\[
X_0=\{0\}\cup\left\{{1\over n}:n\in\ZZ^+\right\}
\]
is compact.
::: {.proof}
Let $\mathcal U$ be an open cover of $X_0$.
Choose $U_0\in\mathcal U$ with $0\in U_0$.
Because $U_0$ is open in the subspace topology, there is $\varepsilon>0$ such that
\[
(-\varepsilon,\varepsilon)\cap X_0\subseteq U_0.
\]
Choose $N$ with $1/N<\varepsilon$.
Then
\[
{1\over n}\in U_0
\qquad\text{for every }n\ge N.
\]
Thus only the finitely many points
\[
1,{1\over2},\ldots,{1\over N-1}
\]
remain to be covered.
Choose one member of $\mathcal U$ containing each of these remaining points.
Together with $U_0$, these finitely many sets cover $X_0$.
:::

<1>3. The family
\[
\mathcal V=\left\{(1/n,1]:n\in\ZZ^+\right\}
\]
is an open cover of $(0,1]$ in the subspace topology.
::: {.proof}
Each $(1/n,1]$ equals
\[
(1/n,2)\cap(0,1],
\]
so it is open in $(0,1]$.
If $x\in(0,1]$, choose $n$ with $1/n<x$; then $x\in(1/n,1]$.
:::

<1>4. No finite subfamily of $\mathcal V$ covers $(0,1]$.
::: {.proof}
Take finitely many members
\[
(1/n_1,1],\ldots,(1/n_k,1]
\]
and let
\[
N=\max\{n_1,\ldots,n_k\}.
\]
Then $1/N\in(0,1]$, but for every $i$,
\[
{1\over N}\le {1\over n_i},
\]
so $1/N\notin(1/n_i,1]$.
:::

<1>5. $(0,1]$ is not compact.
::: {.proof}
By <1>3, $\mathcal V$ is an open cover, and by <1>4 it has no finite subcover.
:::
:::
