---
schema: qual/card@1
id: T-SM8EW
kind: theorem
title: Differentiation of functions of bounded variation and absolutely continuous functions
slogan: 'Bounded variation gives a derivative almost everywhere; only absolute continuity gives back the function by integrating it.'
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $a<b$ and $f\colon[a,b]\to\RR$.

(a) If $f$ is monotone, or more generally of bounded variation, then $f'(x)$ exists for almost every $x\in[a,b]$ and $\int_a^b\abs{f'} < \infty$.

(b) If $f$ is absolutely continuous, then $f(x) = f(a) + \int_a^x f'$ for all $x\in[a,b]$.

(c) If $f\in L^1([a,b])$, then $F(x) \coloneqq\int_a^x f$ is absolutely continuous on $[a,b]$ and $F' = f$ almost everywhere.

[@Fol13, sect. 3.5]
:::

::: {.example}
The Cantor function is continuous and increasing, so it has bounded variation, and its derivative is $0$ almost everywhere, but it is not constant.
Hence the identity $f(x) - f(a) = \int_a^x f'$ of (b) can fail for $f$ of bounded variation.
:::
