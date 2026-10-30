---
schema: qual/card@1
id: P-BKF18-6A
kind: problem
title: Square root of a unipotent matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $A$ be an $n\times n$ real matrix such that $(A-I)^m=0$ for some $m\ge1$.
Prove that there exists an $n\times n$ real matrix $B$ such that $B^2=A$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is a polynomial $P\in\RR[x]$ and a polynomial $Q\in\RR[x]$ with
$$
P(x)^2=1+x+x^mQ(x).
$$

::: pf-proof

Let $P$ be the Taylor polynomial of degree $m-1$ of $\sqrt{1+x}$ at $0$, so $\sqrt{1+x}=P(x)+O(x^m)$ near $0$. Then $P(x)^2=1+x+O(x^m)$. Since $P(x)^2-1-x$ is a polynomial that is $O(x^m)$ at $0$, it is divisible by $x^m$.

:::

:::

::: {.pf-step #s2}

$B=P(A-I)$ is a real matrix with $B^2=A$.

::: pf-proof

Put $N=A-I$, so $N^m=0$. Polynomials in $N$ commute, so by step [](#s1){.pf-ref}, $P(N)^2=I+N+N^mQ(N)=I+N=A$. $P$ has real coefficients, so $B$ is real.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives the required $B$.

:::

:::

:::
