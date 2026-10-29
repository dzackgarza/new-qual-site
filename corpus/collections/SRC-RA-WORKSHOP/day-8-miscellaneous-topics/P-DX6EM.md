---
schema: qual/card@1
id: P-DX6EM
kind: problem
title: A function of bounded variation is the difference of two increasing functions
classification:
  areas:
  - real-analysis
  topics:
  - Variation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $f \colon [a,b] \to \RR$.
Suppose $f \in \text{BV}[a,b]$.
Prove $f$ is the difference of two increasing functions.
:::

::: {.solution}

For $a<x\le b$, let $V(x)$ be the supremum of $\sum_{i=1}^n \abs{f(x_i) - f(x_{i-1})}$ over all partitions $a = x_0 < \cdots < x_n = x$ of $[a, x]$, and let $V(a)\coloneqq0$. Every partition of $[a,x]$ extends to one of $[a,b]$, so $0\le V(x)\le V(b)<\infty$ by bounded variation.

::: pf

::: {.pf-step #s3}

$V + f$ and $V - f$ are increasing on $[a,b]$.

::: pf-proof

::: {.pf-step #s3-1}

For $a \le x < y \le b$, $V(y) - V(x) \ge \abs{f(y) - f(x)}$.

::: pf-proof

Fix $\varepsilon>0$. There is a partition of $[a,x]$ whose variation sum exceeds $V(x)-\varepsilon$ (for $x=a$, the empty sum). Appending $y$ produces a partition of $[a,y]$ with variation sum exceeding $V(x)-\varepsilon+\abs{f(y)-f(x)}$. Thus $V(y)\ge V(x)-\varepsilon+\abs{f(y)-f(x)}$. Letting $\varepsilon\downarrow0$ gives the assertion.

:::

:::

::: pf-qed

Let $a\le x<y\le b$ and $u=f(y)-f(x)$. By step [](#s3-1){.pf-ref}, $V(y)-V(x)\ge\abs{u}$, so the increment of $V+f$ is at least $\abs{u}+u\ge0$ and the increment of $V-f$ is at least $\abs{u}-u\ge0$.

:::

:::

:::

::: pf-step

The functions $g=(V+f)/2$ and $h=(V-f)/2$ are increasing and satisfy $f=g-h$.

::: pf-proof

Step [](#s3){.pf-ref} gives monotonicity of $V+f$ and $V-f$, preserved by multiplication by $1/2>0$. Subtracting the definitions gives $g-h=f$ pointwise.

:::

:::

:::

:::
