---
schema: qual/card@1
id: E-AMD-BII4UYJ7
kind: problem
title: Prime ideals are primary
classification:
  areas:
  - algebra
  topics:
  - Primary Decomposition
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that every prime ideal is primary.
:::

::: {.solution}
**Goal:** Let $R$ be a commutative ring with identity $1 \neq 0$, and let $\mathfrak{p} \subsetneq R$ be a prime ideal.
Prove that $\mathfrak{p}$ is a primary ideal.

<1>1. Definitions: <2>1. A proper ideal $\mathfrak{p} \subsetneq R$ is a prime ideal if whenever $a, b \in R$ satisfy $a b \in \mathfrak{p}$, then either $a \in \mathfrak{p}$ or $b \in \mathfrak{p}$.
::: {.proof}
Standard definition of a prime ideal.
:::
<2>2. A proper ideal $\mathfrak{q} \subsetneq R$ is a primary ideal if whenever $a, b \in R$ satisfy $a b \in \mathfrak{q}$, then either $a \in \mathfrak{q}$ or $b^n \in \mathfrak{q}$ for some positive integer $n \ge 1$ (equivalently, $a \in \mathfrak{q}$ or $b \in \sqrt{\mathfrak{q}}$).
::: {.proof}
Standard definition of a primary ideal.
:::

<1>2. Verification of the primary condition for $\mathfrak{p}$: <2>1. Let $\mathfrak{p}$ be a prime ideal.
Then $\mathfrak{p} \subsetneq R$ is proper.
::: {.proof}
By definition of prime ideal.
:::
<2>2. Let $a, b \in R$ be arbitrary elements such that $a b \in \mathfrak{p}$.
::: {.proof}
Setting up the hypothesis of the primary condition.
:::
<2>3. Since $\mathfrak{p}$ is prime, either $a \in \mathfrak{p}$ or $b \in \mathfrak{p}$.
::: {.proof}
By <1>1.<2>1. <2>4. If $a \in \mathfrak{p}$, the primary condition is satisfied.
:::
::: {.proof}
The first branch of the primary condition holds.
:::
<2>5. If $b \in \mathfrak{p}$, then $b^1 = b \in \mathfrak{p}$.
::: {.proof}
Choosing the integer exponent $n = 1 \ge 1$.
:::
<2>6. In either case, $a \in \mathfrak{p}$ or $b^n \in \mathfrak{p}$ for some $n \ge 1$.
::: {.proof}
From <2>4 and <2>5. <2>7. Since $a, b$ were arbitrary, $\mathfrak{p}$ satisfies the defining condition of a primary ideal.
:::
::: {.proof}
Universal quantification over $a, b \in R$ with $a b \in \mathfrak{p}$.
:::

<1>3. Conclusion: Every prime ideal $\mathfrak{p}$ is primary (specifically, $\mathfrak{p}$-primary with radical $\sqrt{\mathfrak{p}} = \mathfrak{p}$).
::: {.proof}
By <1>2.
:::
:::
