---
schema: qual/card@1
id: P-BKS81-8
kind: problem
title: Existence of a best uniform polynomial approximation of bounded degree
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked compactness of the bounded degree-k polynomial ball and the comparison excluding all polynomials outside it.
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$ be continuous and let $k\in\mathbb N$.
Prove that there is a real polynomial $P$ of degree at most $k$ which minimizes
\[
\sup_{0\le x\le1}|f(x)-P(x)|
\]
among all real polynomials of degree at most $k$.
:::

::: {.solution}
Let
$$
\mathcal P_k
\coloneqq
\operatorname{span}_{\RR}\{1,x,\ldots,x^k\},
$$
with the norm
$$
\norm{P}_\infty
\coloneqq
\sup_{0\le x\le1}\abs{P(x)}.
$$
Put
$$
M\coloneqq\norm{f}_\infty.
$$

::: pf

::: {.pf-step #trivial-case-m-zero}
If $M=0$, then $P=0$ is a minimizing polynomial.

::: pf-proof
In this case $f=0$, so the approximation error of $P=0$ is zero, the
smallest possible value.
:::

:::

::: {.pf-step #outside-ball-not-minimizing}
Suppose $M>0$. Any polynomial $P\in\mathcal P_k$ satisfying
$$
\norm{P}_\infty>2M
$$
has larger error than the polynomial $0$.

::: pf-proof
The reverse triangle inequality gives
$$
\norm{f-P}_\infty
\ge
\norm{P}_\infty-\norm{f}_\infty
>
2M-M
=
M.
$$
On the other hand,
$$
\norm{f-0}_\infty=M.
$$
Thus such a $P$ cannot minimize the error.
:::

:::

::: {.pf-step #ball-is-compact}
The set
$$
K\coloneqq
\{P\in\mathcal P_k:\norm{P}_\infty\le2M\}
$$
is compact.

::: pf-proof
The space $\mathcal P_k$ is a real vector space of dimension $k+1$.
Therefore every closed bounded subset is compact with respect to any norm
on $\mathcal P_k$. The set $K$ is the closed ball of radius $2M$ in the
supremum norm, hence is compact.
:::

:::

::: {.pf-step #error-continuous}
The error function
$$
E:\mathcal P_k\longrightarrow\RR,
\qquad
E(P)\coloneqq\norm{f-P}_\infty,
$$
is continuous.

::: pf-proof
For $P,Q\in\mathcal P_k$, the reverse triangle inequality gives
$$
\abs{E(P)-E(Q)}
\le
\norm{P-Q}_\infty.
$$
Thus $E$ is in fact $1$-Lipschitz.
:::

:::

::: {.pf-step #minimizer-exists}
There is a polynomial $P_*\in\mathcal P_k$ such that
$$
\boxed{
\norm{f-P_*}_\infty
=
\inf_{P\in\mathcal P_k}\norm{f-P}_\infty
}.
$$

::: pf-proof
By steps [](#ball-is-compact){.pf-ref} and [](#error-continuous){.pf-ref}, the continuous function $E$ attains a minimum on
the compact set $K$. Let $P_*$ be a minimizer there. Step [](#outside-ball-not-minimizing){.pf-ref} shows that
every polynomial outside $K$ has error strictly larger than $E(0)=M$, while
$0\in K$. Hence no polynomial outside $K$ can improve on $P_*$, so $P_*$
is a global minimizer on $\mathcal P_k$.
:::

:::

::: pf-qed
Step [](#trivial-case-m-zero){.pf-ref} handles $M=0$, and step [](#minimizer-exists){.pf-ref} handles $M>0$.
:::

:::
:::
