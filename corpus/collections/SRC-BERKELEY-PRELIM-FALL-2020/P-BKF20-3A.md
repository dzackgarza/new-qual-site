---
schema: qual/card@1
id: P-BKF20-3A
kind: problem
title: Nested compact sets have nonempty intersection
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 solution: if the intersection
    were empty, the open complements X\T_n would cover compact T_1; nestedness
    reduces a finite subcover to one complement, contradicting nonemptiness.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked openness of the complements, the finite-subcover step, reversal
    of inclusions under complements, and the final contradiction with the
    assumed nonemptiness of every T_n.
---

::: {.problem}
Let $X$ be a metric space and let $T_1\supseteq T_2\supseteq\cdots$ be nonempty closed subsets of $X$. If $T_1$ is compact, show that
\[
\bigcap_{n=1}^{\infty}T_n\ne\varnothing.
\]
:::

::: {.solution}
<1>1. Suppose for contradiction that
$$
\bigcap_{n=1}^{\infty}T_n=\varnothing.
$$
Then
$$
\{X\setminus T_n:n\ge1\}
$$
is an open cover of $T_1$.

::: {.proof}
Each $T_n$ is closed, so $X\setminus T_n$ is open. The assumed empty
intersection implies, by De Morgan's law,
$$
X
=
X\setminus\bigcap_{n=1}^{\infty}T_n
=
\bigcup_{n=1}^{\infty}(X\setminus T_n).
$$
In particular these open sets cover $T_1$.
:::

<1>2. There is an integer $N\ge1$ such that
$$
T_1\subseteq X\setminus T_N.
$$

::: {.proof}
Since $T_1$ is compact, step <1>1 has a finite subcover. Thus there are
indices
$$
n_1,\ldots,n_k
$$
such that
$$
T_1
\subseteq
\bigcup_{j=1}^k(X\setminus T_{n_j}).
$$
Let
$$
N\coloneqq\max\{n_1,\ldots,n_k\}.
$$
The nesting
$$
T_1\supseteq T_2\supseteq\cdots
$$
implies
$$
X\setminus T_{n_j}
\subseteq
X\setminus T_N
$$
for every $j$. Hence the whole finite union is contained in
$X\setminus T_N$, proving the claim.
:::

<1>3. Step <1>2 contradicts the nonemptiness of $T_N$.

::: {.proof}
Because the sets are nested,
$$
T_N\subseteq T_1.
$$
Step <1>2 says that every point of $T_1$ lies outside $T_N$. Therefore
$$
T_N
\subseteq
T_1\cap(X\setminus T_N)
=
\varnothing.
$$
Thus $T_N=\varnothing$, contrary to the hypothesis that every $T_n$ is
nonempty.
:::

<1>4. Therefore
$$
\boxed{
\bigcap_{n=1}^{\infty}T_n\ne\varnothing.
}
$$

::: {.proof}
The contrary assumption in step <1>1 leads to the contradiction in
step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
