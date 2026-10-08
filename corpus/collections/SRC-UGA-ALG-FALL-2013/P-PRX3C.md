---
schema: qual/card@1
id: P-PRX3C
kind: problem
title: Prime and maximal ideals, with examples in $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Ideals
relations: []
review: draft
---

::: {.problem}
a. Define *prime ideal*, give an example of a nontrivial ideal in the ring $\ZZ$ that is not prime, and prove that it is not prime.

b. Define *maximal ideal*, give an example of a nontrivial maximal ideal in $\ZZ$ and prove that it is maximal.
:::

::: {.solution}
<1>1. An ideal $\mathfrak p$ of a commutative ring $R$ is prime if it is proper and $ab\in\mathfrak p$ implies $a\in\mathfrak p$ or $b\in\mathfrak p$.

::: {.proof}
This is the defining condition for a prime ideal.
:::

<1>2. The nonzero proper ideal $8\mathbb Z$ is not prime.

::: {.proof}
The integers $2$ and $4$ do not belong to $8\mathbb Z$, but their product $8$ does. Thus the implication in step <1>1 fails.
:::

<1>3. An ideal $\mathfrak m$ of a commutative ring $R$ is maximal if it is proper and every ideal $J$ satisfying $\mathfrak m\subseteq J\subseteq R$ equals $\mathfrak m$ or $R$.

::: {.proof}
This is the defining condition for a maximal ideal.
:::

<1>4. The ideal $2\mathbb Z$ is a nonzero maximal ideal of $\mathbb Z$.

::: {.proof}
The quotient $\mathbb Z/2\mathbb Z$ is a field. An ideal is maximal exactly when its quotient ring is a field, so $2\mathbb Z$ is maximal. Equivalently, any ideal containing $2\mathbb Z$ is $d\mathbb Z$ for a positive divisor $d$ of $2$, hence is either $2\mathbb Z$ or $\mathbb Z$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 answer part (a), and steps <1>3 and <1>4 answer part (b).
:::
:::
