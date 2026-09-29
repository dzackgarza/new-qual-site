---
schema: qual/card@1
id: P-BERK98S-18
kind: problem
title: Every unipotent complex matrix has an $r$-th root
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
- event: solution-written
  by: chatgpt
  date: 2026-09-24
---

::: {.problem}
Let $N$ be a nilpotent $n\times n$ complex matrix, and let $r$ be a positive integer. Show that there is an $n\times n$ complex matrix $A$ such that
\[
A^r=I+N.
\]
:::

::: {.solution}
Choose $m\ge1$ such that
$$
N^m=0,
$$
and put
$$
\alpha\coloneqq\frac1r.
$$
For $k\ge0$, write
$$
\binom{\alpha}{0}\coloneqq1,
\qquad
\binom{\alpha}{k}
\coloneqq
\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}.
$$

::: pf

::: {.pf-step #s1}

The formal power series
$$
F(t)\coloneqq\sum_{k=0}^{\infty}\binom{\alpha}{k}t^k
\in\CC[[t]]
$$
satisfies
$$
F(t)^r=1+t.
$$

::: pf-proof

Let $c_k=\binom{\alpha}{k}$. Then
$$
(k+1)c_{k+1}=(\alpha-k)c_k,
$$
so
$$
(1+t)F'(t)=\alpha F(t).
$$
Put $G(t)=F(t)^r$. Formal differentiation gives
$$
(1+t)G'(t)
=
rF(t)^{r-1}(1+t)F'(t)
=
r\alpha F(t)^r
=
G(t).
$$
Also $G(0)=1$. Writing $G(t)=\sum_{k\ge0}g_kt^k$, comparison of coefficients gives
$$
g_1=g_0=1
$$
and, for every $k\ge1$,
$$
(k+1)g_{k+1}=(1-k)g_k.
$$
Thus $g_2=0$, and induction gives $g_k=0$ for every $k\ge2$. Hence
$$
G(t)=1+t.
$$

:::

:::

::: {.pf-step #s2}

In $\CC[t]/(t^m)$,
$$
\left(
\sum_{k=0}^{m-1}\binom{\alpha}{k}t^k
\right)^r
=
1+t.
$$

::: pf-proof

Reduce the identity in step [](#s1){.pf-ref} modulo $t^m$. The image of $F(t)$ is represented by its truncation through degree $m-1$, which gives the displayed identity.

:::

:::

::: {.pf-step #s3}

The matrix
$$
A\coloneqq
\sum_{k=0}^{m-1}\binom{1/r}{k}N^k
$$
satisfies
$$
\boxed{A^r=I+N}.
$$

::: pf-proof

Since $N^m=0$, evaluation at $N$ defines a ring homomorphism
$$
\CC[t]/(t^m)\longrightarrow M_n(\CC),
\qquad
t\longmapsto N.
$$
Applying it to the identity in step [](#s2){.pf-ref} gives $A^r=I+N$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} constructs the required matrix and proves the required identity.

:::

:::

:::
