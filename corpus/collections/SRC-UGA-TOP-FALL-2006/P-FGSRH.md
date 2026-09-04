---
schema: qual/card@1
id: P-FGSRH
kind: problem
title: Every compact metric space is sequentially compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: {.problem}
A topological space is **sequentially compact** if every infinite sequence in $X$ has a convergent subsequence.

Prove that every compact metric space is sequentially compact.
:::

::: {.solution}
Let $(X,d)$ be compact and let $(x_n)$ be a sequence in $X$.

<1>1. We may reduce to the case in which the set of values of $(x_n)$ is infinite.
::: {.proof}
If some value occurs infinitely often, the corresponding constant subsequence converges. Otherwise every value occurs only finitely often, so
\[
A=\{x_n:n\ge1\}
\]
is infinite, as required.
:::

<1>2. The infinite set $A$ has a limit point $p\in X$.
::: {.proof}
Suppose not. For each $x\in X$ there is then an open neighborhood $U_x$ such that
\[
U_x\cap A\subseteq\{x\}.
\]
The family $\{U_x:x\in X\}$ covers $X$, so compactness gives a finite subcover $U_{x_1},\ldots,U_{x_m}$. Consequently
\[
A\subseteq\{x_1,\ldots,x_m\},
\]
contrary to <1>1.
:::

<1>3. Every neighborhood of $p$ contains infinitely many points of $A$.
::: {.proof}
If a neighborhood $U$ of $p$ met $A\setminus\{p\}$ in only finitely many points $a_1,\ldots,a_r$, then, because a metric space is $T_1$, the set
\[
U\setminus\{a_1,\ldots,a_r\}
\]
would still be a neighborhood of $p$ and would miss $A\setminus\{p\}$. This contradicts that $p$ is a limit point of $A$ by <1>2.
:::

<1>4. There are indices $n_1<n_2<\cdots$ such that
\[
x_{n_k}\in B(p,1/k).
\]
::: {.proof}
Choose the indices recursively. After $n_1,\ldots,n_{k-1}$ have been chosen, <1>3 says that $B(p,1/k)$ contains infinitely many values from $A$. Since each value occurs only finitely often by the reduction in <1>1, some occurrence has index larger than $n_{k-1}$; choose it as $n_k$.
:::

<1>5. The subsequence $(x_{n_k})$ converges to $p$.
::: {.proof}
By <1>4,
\[
d(x_{n_k},p)<{1\over k}\to0,
\]
which is precisely $x_{n_k}\to p$.
:::

<1>6. $X$ is sequentially compact.
::: {.proof}
The sequence $(x_n)$ was arbitrary. Either <1>1 supplied a constant convergent subsequence, or <1>5 supplied a subsequence converging to a limit point. Hence every sequence has a convergent subsequence.
:::
:::
