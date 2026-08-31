---
schema: qual/card@1
id: PR-YO7MV
kind: proposition
title: Markov/Chebyshev's Inequality
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Lp Spaces
  - Integrals
relations: []
review: draft
---

:::{.proposition}
The most often used form here:
\[  
\mu \qty{ f\inv\qty{(\alpha, \infty)} } \da \mu\qty{\ts{ x\in X \st \abs{f(x)} > \alpha  }} \leq {1\over \alpha} \norm{f}_1 \da {1\over \alpha} \int_X \abs{f}
.\]
:::

::: {.proof}
Let $S_\alpha \da \ts{x \in X \st \abs{f(x)} > \alpha}$.
On $S_\alpha$ the integrand satisfies $\abs{f(x)} > \alpha$, so
\[
\int_X \abs{f} \geq \int_{S_\alpha} \abs{f} \geq \int_{S_\alpha} \alpha = \alpha\,\mu(S_\alpha).
\]
Dividing by $\alpha > 0$ gives $\mu(S_\alpha) \leq \frac1\alpha \int_X \abs{f}$, which is the claim.

![figures/image_2021-06-02-22-59-46.png](../../assets/figures/image_2021-06-02-22-59-46.png)
:::

The probability interpretation: $\PP(X\geq \alpha) \leq {1\over \alpha} \EE(X)$.

The more general version:
\[
\mu \qty{ f\inv\qty{(\alpha, \infty)} } \da \mu\qty{\ts{ x\in X \st \abs{f(x)} > \alpha }  } \leq {1\over \alpha^p} \norm{f}_p^p \da{1\over \alpha^p} \int_X \abs{f}^p 
.\]

::: {.proof}
On $S_\alpha$ we have $\abs{f(x)} > \alpha$, hence $\abs{f(x)}^p > \alpha^p$, so
\[
\norm{f}_p^p = \int \abs{f}^p \geq \int_{S_\alpha} \abs{f}^p \geq \int_{S_\alpha} \alpha^p = \alpha^p \mu(S_\alpha).
\]
Dividing by $\alpha^p > 0$ gives $\mu(S_\alpha) \leq \frac1{\alpha^p} \norm{f}_p^p$.
:::
