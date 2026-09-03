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

:::{.exercise}
Let $(\Omega,\mcb)$ be a measurable space with a Borel $\sigma\dash$algebra and $\mu_n: \mcb \to [0, \infty]$ be a $\sigma\dash$additive measure for each $n$.
Show that the following map is again a $\sigma\dash$additive measure on $\mcb$:
\[
\mu(B) \da \sum_{n\geq 1} \mu_n(B)
.\]
:::

:::{.solution}
Apply Fubini-Tonelli to commute two sums:
\[
\mu\qty{\Union_{1\leq k \leq M} E_k}\da 
&= \sum_{n\geq 1} \mu_n\qty{\Union_{1\leq k \leq M} E_k}\\
&= \sum_{n\geq 1} \sum_{1\leq k \leq M} \mu_n\qty{E_k}\\
&= \sum_{1\leq k \leq M}\sum_{n\geq 1} \mu_n\qty{E_k} \text{FT} \\
&\da \sum_{1\leq k \leq M} \mu(E_k)
.\]
:::
