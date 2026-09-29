---
schema: qual/card@1
id: P-BKF88-1
kind: problem
title: Uniform eventual periodicity of powers in a finite ring
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Let $R$ be a finite ring.
Prove that there exist positive integers $m>n$ such that
\[
x^m=x^n
\]
for every $x\in R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For each positive integer $k$, define a function
$$
F_k:R\longrightarrow R,
\qquad
F_k(x)=x^k.
$$

::: pf-proof

Multiplication in a ring is associative, so the positive power $x^k$ is defined for every $x\in R$ and every $k\geq1$. Hence $F_k$ is a well-defined function from $R$ to itself.

:::

:::

::: {.pf-step #s2}

Only finitely many distinct functions $R\to R$ exist.

::: pf-proof

Since $R$ is finite, the set
$$
R^R=\{F:R\to R\}
$$
has cardinality
$$
\abs{R}^{\abs{R}},
$$
which is finite.

:::

:::

::: {.pf-step #s3}

There exist positive integers $m>n$ such that
$$
F_m=F_n.
$$

::: pf-proof

The infinite sequence
$$
F_1,F_2,F_3,\ldots
$$
takes values in the finite set $R^R$ from step [](#s2){.pf-ref}. By the pigeonhole principle, two of these functions are equal. Thus there are positive integers $m>n$ with $F_m=F_n$.

:::

:::

::: {.pf-step #s4}

For the integers $m>n$ from step [](#s3){.pf-ref},
$$
x^m=x^n
$$
for every $x\in R$.

::: pf-proof

Equality $F_m=F_n$ means equality at every argument $x\in R$. By the definition in step [](#s1){.pf-ref},
$$
x^m
=
F_m(x)
=
F_n(x)
=
x^n.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required uniform equality of powers.

:::

:::

:::
