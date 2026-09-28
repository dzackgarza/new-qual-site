---
schema: qual/card@1
id: E-WSJ6P
kind: problem
title: The sum of countably many measures is a measure
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fubini-Tonelli
relations: []
review: draft
---

::: {.exercise}
Let $(\Omega,\mcb)$ be a measurable space with a Borel $\sigma\dash$algebra and $\mu_n: \mcb \to [0, \infty]$ be a $\sigma\dash$additive measure for each $n$.
Show that the following map is again a $\sigma\dash$additive measure on $\mcb$:
\[
\mu(B) \da \sum_{n\geq 1} \mu_n(B)
.\]
:::

::: {.solution}
<1>1. $\mu(\emptyset) = 0$ and $\mu$ takes values in $[0,\infty]$.

::: {.proof}
Each $\mu_n(\emptyset) = 0$, and a series of terms in $[0,\infty]$ has a sum in $[0,\infty]$.
:::

<1>2. For pairwise disjoint $E_1, E_2, \ldots \in \mcb$, $\mu\qty{\bigcup_{k\geq1} E_k} = \sum_{k\geq1}\mu(E_k)$.

::: {.proof}
By $\sigma$-additivity of each $\mu_n$,
$$
\mu\qty{\bigcup_{k\geq 1} E_k}
= \sum_{n\geq 1} \mu_n\qty{\bigcup_{k\geq 1} E_k}
= \sum_{n\geq 1} \sum_{k\geq 1} \mu_n(E_k)
= \sum_{k\geq 1}\sum_{n\geq 1} \mu_n(E_k)
= \sum_{k\geq 1} \mu(E_k).
$$
The third equality exchanges two sums of nonnegative terms, which is Tonelli's theorem for counting measure on $\NN \times \NN$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 are the axioms of a measure.
:::
:::
