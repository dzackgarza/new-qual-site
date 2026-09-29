---
schema: qual/card@1
id: P-QCF34
kind: problem
title: The annihilator of a module is an ideal, every ideal is an annihilator, and
  a faithful module of torsion elements
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a commutative ring with unit and let $M$ be an $R$-module.
Define the annihilator of $M$ to be
\[
\operatorname{Ann}(M):=\{r \in R \mid r \cdot m=0 \text { for all } m \in M\}
\]

a. Prove that $\operatorname{Ann}(M)$ is an ideal in $R$.

b. Conversely, prove that every ideal in $R$ is the annihilator of some $R$-module.

c. Give an example of a module $M$ over a ring $R$ such that each element $m \in M$ has a nontrivial annihilator $\operatorname{Ann}(m):=\{r \in R \mid r \cdot m=0\}$, but $\operatorname{Ann}(M)=\{0\}$
:::

::: {.solution}
**Goal:** Prove that module annihilators are ideals, every ideal is a module annihilator, and provide a faithful torsion module.

::: pf

::: pf-step
Part (a): $\operatorname{Ann}(M)$ is an ideal of $R$.

::: pf-proof

::: pf-step
Non-emptiness: For all $m \in M$, $0_R \cdot m = 0_M$, so $0_R \in \operatorname{Ann}(M)$.
:::

::: pf-step
Closure under subtraction: Let $r_1, r_2 \in \operatorname{Ann}(M)$. For any $m \in M$:
$$(r_1 - r_2) \cdot m = r_1 \cdot m - r_2 \cdot m = 0 - 0 = 0.$$
Thus $r_1 - r_2 \in \operatorname{Ann}(M)$, so $\operatorname{Ann}(M)$ is an additive subgroup of $R$.
:::

::: pf-step
Ideal absorption: Let $r \in \operatorname{Ann}(M)$ and $s \in R$. For any $m \in M$:
$$(s \cdot r) \cdot m = s \cdot (r \cdot m) = s \cdot 0 = 0.$$
Since $R$ is commutative, $(r \cdot s) \cdot m = 0$ as well. Thus $s \cdot r \in \operatorname{Ann}(M)$.
:::

::: pf-step
Therefore $\operatorname{Ann}(M)$ is an ideal of $R$.
:::

:::

:::

::: pf-step
Part (b): Every ideal $I \subseteq R$ is the annihilator of some $R$-module.

::: pf-proof

::: pf-step
Let $I$ be an ideal of $R$. Consider the quotient $R$-module $M = R/I$.
:::

::: pf-step
If $r \in I$, then for every $x + I \in R/I$, $r \cdot (x + I) = rx + I = 0 + I$ because $rx \in I$. Thus $I \subseteq \operatorname{Ann}(R/I)$.
:::

::: pf-step
Conversely, if $r \in \operatorname{Ann}(R/I)$, then $r \cdot (1_R + I) = 0 + I$, which means $r \cdot 1_R + I = r + I = I$.
:::

::: pf-step
Thus $r \in I$, proving $\operatorname{Ann}(R/I) \subseteq I$.
:::

::: pf-step
Therefore $\operatorname{Ann}(R/I) = I$.
:::

:::

:::

::: pf-step
Part (c): A module with non-trivial element annihilators but $\operatorname{Ann}(M) = \{0\}$.

::: pf-proof

::: pf-step
Take the ring $R = \mathbb{Z}$ and the $\mathbb{Z}$-module $M = \mathbb{Q}/\mathbb{Z}$ (the group of roots of unity / torsion elements of the circle group).
:::

::: pf-step
For every non-zero element $m = \frac{a}{b} + \mathbb{Z} \in \mathbb{Q}/\mathbb{Z}$ (with $\gcd(a, b) = 1$ and $b \ge 1$),
$$\operatorname{Ann}(m) = \{n \in \mathbb{Z} : n \cdot m = 0\} = b\mathbb{Z} \neq \{0\}.$$
Thus every single element of $M$ has a non-trivial (non-zero) annihilator.
:::

::: pf-step
However, if $n \in \operatorname{Ann}(M)$, then $n \cdot m = 0$ for all $m \in M$.
:::

::: pf-step
For every integer $k \ge 1$, $\frac{1}{k} + \mathbb{Z} \in M$, so $n \cdot \left(\frac{1}{k} + \mathbb{Z}\right) = \frac{n}{k} + \mathbb{Z} = 0 \implies k \mid n$.
:::

::: pf-step
Since $n$ must be divisible by every positive integer $k \ge 1$, $n = 0$.
:::

::: pf-step
Thus $\operatorname{Ann}(M) = \{0\}$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
All three parts are established.
:::

:::

:::
:::
