---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-09
kind: problem
title: 'Differentiability at zero and a continuous factorization'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 2012 #1a) Suppose that $f:\mathbb R\to\mathbb R$ satisfies $f(0)=0$.
Prove that $f$ is differentiable at $x=0$ if and only if there is a function $g:\mathbb R\to\mathbb R$ which is continuous at $x=0$ and satisfies $f(x)=xg(x)$ for all $x\in\mathbb R$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (⟹) If $f$ is differentiable at $0$, construct $g$.
Proof: define $g(x) = f(x)/x$ for $x \ne 0$ and $g(0) = f'(0)$.
Then $f(x) = xg(x)$ for all $x \ne 0$, and also at $x = 0$ (both sides are $0$). Continuity of $g$ at $0$: \[\lim_{x\to 0}g(x) = \lim_{x\to 0}\frac{f(x)}{x} = \lim_{x\to 0}\frac{f(x) - f(0)}{x} = f'(0) = g(0),\] using $f(0) = 0$.
<1>2. (⟸) If $f(x) = xg(x)$ with $g$ continuous at $0$, then $f$ is differentiable at $0$.
Proof: using $f(0) = 0\cdot g(0) = 0$, \[\lim_{x\to 0}\frac{f(x) - f(0)}{x} = \lim_{x\to 0}\frac{xg(x)}{x} = \lim_{x\to 0}g(x) = g(0),\] so $f'(0)$ exists and equals $g(0)$.
<1>3. Q.E.D.
:::
