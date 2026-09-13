---
schema: qual/card@1
id: P-BERK84S-14
kind: problem
title: Intersection of hyperplanes containing a subspace
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 14 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified both inclusions using basis extension to separate any vector outside W by a hyperplane containing W.
---

::: {.problem}
Suppose $V$ is an $n$-dimensional vector space over the field $F$.
Let $W\subset V$ be a subspace of dimension $r<n$.
Show that
\[
W=\bigcap\{U\mid U\text{ is an }(n-1)\text{-dimensional subspace of }V\text{ and }W\subset U\}.
\]
:::


::: {.solution}
Let
\[
\mathcal H=\{U\le V:\dim U=n-1\text{ and }W\subseteq U\}.
\]

<1>1. One has $W\subseteq\bigcap_{U\in\mathcal H}U$.
::: {.proof}
By definition, every $U\in\mathcal H$ contains $W$. Therefore every vector of $W$ lies in every such $U$, hence lies in their intersection.
:::

<1>2. If $v\notin W$, then some hyperplane $U\in\mathcal H$ does not contain $v$.
::: {.proof}
Choose a basis
\[
w_1,\ldots,w_r
\]
of $W$. Since $v\notin W$, the list
\[
w_1,\ldots,w_r,v
\]
is linearly independent. Extend it to a basis of $V$:
\[
w_1,\ldots,w_r,v,u_{r+2},\ldots,u_n.
\]
Now set
\[
U=\operatorname{span}(w_1,\ldots,w_r,u_{r+2},\ldots,u_n).
\]
This subspace is spanned by $n-1$ basis vectors, so
\[
\dim U=n-1.
\]
It contains $W$, hence $U\in\mathcal H$. But $v\notin U$, because otherwise the displayed basis of $V$ would be linearly dependent.
:::

<1>3. Therefore the intersection is exactly $W$.
::: {.proof}
By <1>1,
\[
W\subseteq\bigcap_{U\in\mathcal H}U.
\]
By <1>2, every $v\notin W$ is omitted by at least one member of $\mathcal H$, so no vector outside $W$ belongs to the intersection. Hence
\[
\boxed{W=\bigcap_{U\in\mathcal H}U}.
\]
:::
:::
