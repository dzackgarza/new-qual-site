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
<1>1. For each positive integer $k$, define a function
$$
F_k:R\longrightarrow R,
\qquad
F_k(x)=x^k.
$$

::: {.proof}
Multiplication in a ring is associative, so the positive power $x^k$ is defined for every $x\in R$ and every $k\geq1$. Hence $F_k$ is a well-defined function from $R$ to itself.
:::

<1>2. Only finitely many distinct functions $R\to R$ exist.

::: {.proof}
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

<1>3. There exist positive integers $m>n$ such that
$$
F_m=F_n.
$$

::: {.proof}
The infinite sequence
$$
F_1,F_2,F_3,\ldots
$$
takes values in the finite set $R^R$ from step <1>2. By the pigeonhole principle, two of these functions are equal. Thus there are positive integers $m>n$ with $F_m=F_n$.
:::

<1>4. For the integers $m>n$ from step <1>3,
$$
x^m=x^n
$$
for every $x\in R$.

::: {.proof}
Equality $F_m=F_n$ means equality at every argument $x\in R$. By the definition in step <1>1,
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

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required uniform equality of powers.
:::
:::
