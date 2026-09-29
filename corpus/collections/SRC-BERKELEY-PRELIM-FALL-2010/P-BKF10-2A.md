---
schema: qual/card@1
id: P-BKF10-2A
kind: problem
title: Every finite ring satisfies an identity $x^m=x^n$ with $m>n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the finite-function pigeonhole argument with positive exponents.
---

::: {.problem}
Let $R$ be a finite ring.
Prove that there are positive integers $m$ and $n$ with $m>n$ such that every $x\in R$ satisfies $x^m=x^n$.
:::

::: {.solution}

::: pf

::: pf-step

For each positive integer $k$, define a function
$$
f_k\colon R\longrightarrow R,
\qquad
f_k(x)=x^k.
$$

::: pf-proof

Positive powers are defined using the multiplication in $R$, so each
$f_k$ is a well-defined function from the finite set $R$ to itself.

:::

:::

::: {.pf-step #s2}

There exist positive integers $m>n$ such that $f_m=f_n$.

::: pf-proof

If $\abs{R}=q$, then there are only $q^q$ functions from $R$ to $R$.
The infinite sequence
$$
f_1,f_2,f_3,\ldots
$$
therefore contains two equal functions by the pigeonhole principle.
Choose distinct positive indices $m,n$ with $f_m=f_n$, and relabel them
so that $m>n$.

:::

:::

::: {.pf-step #s3}

For these $m>n$, every $x\in R$ satisfies
$$
\boxed{x^m=x^n}.
$$

::: pf-proof

The equality $f_m=f_n$ from step [](#s2){.pf-ref} is equality as functions on all of
$R$. Evaluating it at an arbitrary $x\in R$ gives
$x^m=f_m(x)=f_n(x)=x^n$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is exactly the required common power identity.

:::

:::

:::
