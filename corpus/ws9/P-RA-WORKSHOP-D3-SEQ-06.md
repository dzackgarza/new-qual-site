---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-06
kind: problem
title: $\lim_{n\to\infty}\sqrt{n}(\sqrt{n+1}-\sqrt{n})=\frac12$
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 2013 #1a) Let $$a_n=\sqrt n\left(\sqrt{n+1}-\sqrt n\right).$$ Prove that $\lim_{n\to\infty}a_n=1/2$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Rationalize the expression.
Proof: \[a_n = \sqrt n\,(\sqrt{n+1} - \sqrt n) = \sqrt n\cdot\frac{(n+1) - n}{\sqrt{n+1} + \sqrt n} = \frac{\sqrt n}{\sqrt{n+1} + \sqrt n} = \frac{1}{\sqrt{1 + 1/n} + 1}.\] <1>2. Take the limit.
Proof: $\sqrt{1 + 1/n} \to \sqrt{1} = 1$ by continuity of the square root, so \[\lim_{n\to\infty} a_n = \frac{1}{1 + 1} = \frac12.\] <1>3. Q.E.D.
:::
