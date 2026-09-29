---
schema: qual/card@1
id: P-BKS08-1B
kind: problem
title: Representing $p\mapsto\int_0^1 \frac{p(x)}{x^2+1}\,dx$ by the $L^2$ pairing on polynomials of degree $\le n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the positive-definite integral pairing and the
    finite-dimensional duality argument against the vendored solution.
---

::: {.problem}
For $n\ge1$, let $P_n$ be the real vector space of polynomials of degree at most $n$. Show that there exists $q\in P_n$ such that for every $p\in P_n$,
$$
\int_0^1 p(x)q(x)\,dx
=
\int_0^1 \frac{p(x)}{x^2+1}\,dx.
$$
:::

::: {.solution}
Define a linear functional
$$
T:P_n\longrightarrow\RR,
\qquad
T(p)=\int_0^1\frac{p(x)}{x^2+1}\,dx.
$$

::: pf

::: {.pf-step #l-linear}
Define
$$
L:P_n\longrightarrow P_n^*
$$
by
$$
L(q)(p)=\int_0^1p(x)q(x)\,dx.
$$
Then $L$ is linear.

::: pf-proof
For $q_1,q_2\in P_n$ and $a,b\in\RR$,
$$
\begin{aligned}
L(aq_1+bq_2)(p)
&=\int_0^1p(x)(aq_1(x)+bq_2(x))\,dx\\
&=aL(q_1)(p)+bL(q_2)(p)
\end{aligned}
$$
for every $p\in P_n$. Thus
$L(aq_1+bq_2)=aL(q_1)+bL(q_2)$.
:::

:::

::: {.pf-step #l-injective}
The map $L$ is injective.

::: pf-proof
Suppose $L(q)=0$. Taking $p=q$ gives
$$
0=L(q)(q)=\int_0^1q(x)^2\,dx.
$$
The integrand is continuous and nonnegative. If $q(x_0)^2>0$ at some
$x_0\in[0,1]$, continuity would make it positive on an interval of
positive length, forcing the integral to be positive. Hence $q$ vanishes
on $[0,1]$. A polynomial vanishing on an interval is the zero
polynomial, so $q=0$.
:::

:::

::: {.pf-step #l-isomorphism}
The map $L$ is an isomorphism.

::: pf-proof
The real vector space $P_n$ has dimension $n+1$, and its dual
$P_n^*$ has the same dimension. By step [](#l-injective){.pf-ref}, the linear map
$L:P_n\to P_n^*$ is injective between vector spaces of equal finite
dimension, hence is surjective as well.
:::

:::

::: {.pf-step #q-exists-with-lq-equals-t}
There exists $q\in P_n$ such that
$$
L(q)=T.
$$

::: pf-proof
The functional $T$ belongs to $P_n^*$, and step [](#l-isomorphism){.pf-ref} says that $L$ is
surjective.
:::

:::

::: {.pf-step #pairing-identity}
For this $q$, every $p\in P_n$ satisfies
$$
\boxed{
\int_0^1p(x)q(x)\,dx
=
\int_0^1\frac{p(x)}{x^2+1}\,dx.
}
$$

::: pf-proof
The identity $L(q)=T$ from step [](#q-exists-with-lq-equals-t){.pf-ref} means precisely the displayed
equality after evaluating both functionals at an arbitrary $p\in P_n$.
:::

:::

::: pf-qed
Step [](#pairing-identity){.pf-ref} proves the required existence statement.
:::

:::

:::
