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
---

::: {.problem}
(June 2013 #1b) Prove that $$\lim_{x\to-\infty}\frac{x-1}{x}=1.$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Simplify the difference.
Proof: $\frac{x-1}{x} - 1 = \frac{x-1-x}{x} = -\frac{1}{x}$, so $\left|\frac{x-1}{x} - 1\right| = \frac{1}{|x|}$ for $x \ne 0$.
<1>2. $\epsilon$-$M$ argument for $x \to -\infty$.
Proof: let $\epsilon > 0$ and choose $M = 1/\epsilon$ (any $M > 1/\epsilon$ works).
For $x < -M$: \[\left|\frac{x-1}{x} - 1\right| = \frac{1}{|x|} = \frac{1}{-x} < \frac{1}{M} \le \epsilon.\] Hence $\lim_{x\to-\infty}\frac{x-1}{x} = 1$.
<1>3. Q.E.D.
:::
