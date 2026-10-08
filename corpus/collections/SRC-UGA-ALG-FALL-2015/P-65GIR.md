---
schema: qual/card@1
id: P-65GIR
kind: problem
title: Ascending chains of ideals in a PID stabilize
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Noetherian Rings
  - Ideals
relations: []
review: draft
---

::: {.problem}
Let $R$ be a principal ideal domain (PID), and let $(a_1) \subseteq (a_2) \subseteq (a_3) \subseteq \cdots$ be an ascending chain of ideals in $R$.

Prove that there exists $n \in \mathbb{N}$ such that $(a_j) = (a_n)$ for all $j \ge n$ (that is, $R$ satisfies the ascending chain condition on ideals).
:::

::: {.solution}
<1>1. The union $I=\bigcup_{j\geq1}(a_j)$ is an ideal of $R$.

::: {.proof}
It contains zero. If $x\in(a_i)$ and $y\in(a_j)$, then both belong to $(a_k)$ for $k=\max(i,j)$, and so $x-y\in(a_k)\subseteq I$. If $r\in R$ and $x\in(a_i)$, then $rx\in(a_i)\subseteq I$. Thus $I$ is an ideal.
:::

<1>2. There is an integer $n$ for which $I=(a_n)$.

::: {.proof}
Since $R$ is a PID, step <1>1 gives $I=(b)$ for some $b\in R$. Membership $b\in I$ implies $b\in(a_n)$ for some $n$, hence $I=(b)\subseteq(a_n)$. Conversely $(a_n)\subseteq I$ by definition of the union, so equality holds.
:::

<1>3. The chain stabilizes at $n$:
\[
\boxed{(a_j)=(a_n)\quad\text{for all }j\geq n}.
\]

::: {.proof}
By monotonicity, $(a_n)\subseteq(a_j)\subseteq I$ for $j\geq n$. Step <1>2 identifies the outer ideals, forcing equality throughout.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the ascending chain condition.
:::
:::
