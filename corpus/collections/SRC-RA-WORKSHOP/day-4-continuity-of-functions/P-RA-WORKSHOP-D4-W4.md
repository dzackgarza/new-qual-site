---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W4
kind: problem
title: A limit at negative infinity
classification:
  areas:
  - real-analysis
  topics:
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(June 2013 #1b) Prove that $$\lim_{x\to-\infty}\frac{x-1}{x}=1.$$
:::

::: {.solution}
<1>1. For every $x\ne0$,
\[
\left|\frac{x-1}{x}-1\right|=\frac1{|x|}.
\]

::: {.proof}
Subtracting the fractions gives $(x-1)/x-1=-1/x$. Taking absolute values yields the identity.
:::

<1>2. The limit is $\boxed{\lim_{x\to-\infty}(x-1)/x=1}$.

::: {.proof}
Given $\varepsilon>0$, choose $M=1/\varepsilon$. If $x<-M$, then $|x|=-x>M$, and by step <1>1,
\[
\left|\frac{x-1}{x}-1\right|=\frac1{|x|}<\frac1M=\varepsilon.
\]
This is the definition of convergence to $1$ as $x\to-\infty$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 proves the requested limit.
:::
:::
