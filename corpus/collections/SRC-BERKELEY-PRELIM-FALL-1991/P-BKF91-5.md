---
schema: qual/card@1
id: P-BKF91-5
kind: problem
title: $f(1)=f(0)=\cdots=f^{(n)}(0)=0$ forces a zero of $f^{(n+1)}$ in $(0,1)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Iterated Rolle's theorem between the prescribed derivative zeros at zero
    and successively produced interior zeros.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be infinitely differentiable. Suppose that, for some positive integer $n$,
\[
f(1)=f(0)=f'(0)=f''(0)=\cdots=f^{(n)}(0)=0.
\]
Prove that $f^{(n+1)}(x)=0$ for some $x\in(0,1)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There exists $x_1\in(0,1)$ such that
$$
f'(x_1)=0.
$$

::: pf-proof

The hypotheses give $f(0)=f(1)=0$. Rolle's theorem applied to $f$ on $[0,1]$ gives such a point $x_1$.

:::

:::

::: {.pf-step #s2}

Suppose $1\le k\le n$ and there exists $x_k\in(0,1)$ such that
$$
f^{(k)}(x_k)=0.
$$
Then there exists $x_{k+1}\in(0,x_k)$ such that
$$
f^{(k+1)}(x_{k+1})=0.
$$

::: pf-proof

By hypothesis,
$$
f^{(k)}(0)=0,
$$
and by assumption $f^{(k)}(x_k)=0$. Rolle's theorem applied to $f^{(k)}$ on $[0,x_k]$ gives a point $x_{k+1}\in(0,x_k)$ with
$$
(f^{(k)})'(x_{k+1})=f^{(k+1)}(x_{k+1})=0.
$$

:::

:::

::: {.pf-step #s3}

There exists $x_{n+1}\in(0,1)$ such that
$$
f^{(n+1)}(x_{n+1})=0.
$$

::: pf-proof

Step [](#s1){.pf-ref} supplies $x_1$. Apply step [](#s2){.pf-ref} successively for
$$
k=1,2,\ldots,n.
$$
This produces
$$
0<x_{n+1}<x_n<\cdots<x_1<1
$$
and $f^{(n+1)}(x_{n+1})=0$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the required point in $(0,1)$.

:::

:::

:::
