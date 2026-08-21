---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-W2
kind: problem
title: A quadratic difference bound forces constancy
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Mean Value Theorem
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
([Rud76, Exercise 5.1]) If $f:\mathbb R\to\mathbb R$ satisfies $|f(x)-f(y)|\le(x-y)^2$ for all $x,y$, then $f$ is constant.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Show $f$ is differentiable everywhere with derivative $0$.
Proof: fix $y \in \mathbb{R}$.
For $x \ne y$, \[\left|\frac{f(x) - f(y)}{x - y}\right| \le \frac{(x-y)^2}{|x-y|} = |x - y| \to 0 \quad \text{as } x \to y.\] Hence $f'(y) = \lim_{x\to y}\frac{f(x)-f(y)}{x-y}$ exists and equals $0$, for every $y$.
<1>2. Apply the zero-derivative theorem.
Proof: by the mean value theorem (D5-W1), a function differentiable on $\mathbb{R}$ with $f' \equiv 0$ is constant.
<1>3. Q.E.D.
:::
