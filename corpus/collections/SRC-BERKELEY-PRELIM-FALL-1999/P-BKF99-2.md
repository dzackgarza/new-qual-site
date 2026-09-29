---
schema: qual/card@1
id: P-BKF99-2
kind: problem
title: Nested closed sets of vanishing diameter in a complete metric space intersect
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Chose one point from each nested set, proved the resulting sequence is
    Cauchy using the vanishing diameters, and used closedness of each fixed
    set to place the complete-space limit in every set.
---

::: {.problem}
Let $E_1,E_2,\ldots$ be nonempty closed subsets of a complete metric space $(X,d)$ such that
\[
E_{n+1}\subseteq E_n
\]
for every positive integer $n$, and
\[
\lim_{n\to\infty}\operatorname{diam}(E_n)=0,
\qquad
\operatorname{diam}(E)=\sup\{d(x,y):x,y\in E\}.
\]
Prove that
\[
\bigcap_{n=1}^{\infty}E_n\ne\varnothing.
\]
:::

::: {.solution}

Choose $x_n\in E_n$ for every $n$.

::: pf

::: {.pf-step #sequence-cauchy}
The sequence $(x_n)$ is Cauchy.

::: pf-proof
Let $\varepsilon>0$. Since
$\operatorname{diam}(E_n)\to0$, choose $N$ such that
$$
\operatorname{diam}(E_N)<\varepsilon.
$$
If $m,n\geq N$, nestedness gives
$$
x_m\in E_m\subseteq E_N,
\qquad
x_n\in E_n\subseteq E_N.
$$
Therefore
$$
d(x_m,x_n)
\leq
\operatorname{diam}(E_N)
<
\varepsilon.
$$
Thus $(x_n)$ is Cauchy.
:::

:::

::: {.pf-step #limit-exists}
There exists $x\in X$ such that $x_n\to x$.

::: pf-proof
The metric space $X$ is complete, and $(x_n)$ is Cauchy by step [](#sequence-cauchy){.pf-ref}.
:::

:::

::: {.pf-step #x-in-Ek}
For every positive integer $k$, $x\in E_k$.

::: pf-proof
Fix $k$. For every $n\geq k$, nestedness gives
$$
x_n\in E_n\subseteq E_k.
$$
Hence the tail $(x_n)_{n\geq k}$ lies in $E_k$ and converges to $x$ by step
[](#limit-exists){.pf-ref}. Since $E_k$ is closed, it contains the limit $x$.
:::

:::

::: {.pf-step #x-in-intersection}
$$
x\in\bigcap_{n=1}^{\infty}E_n.
$$

::: pf-proof
This follows from step [](#x-in-Ek){.pf-ref}, since $x$ belongs to every $E_k$.
:::

:::

::: pf-qed
Step [](#x-in-intersection){.pf-ref} exhibits an element of the required intersection.
:::

:::

:::
