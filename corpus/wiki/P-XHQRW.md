---
schema: qual/card@1
id: P-XHQRW
kind: problem
title: If $\lim_{x\to\infty}f(x)$ and $\lim_{x\to\infty}f'(x)$ exist, then $\lim f'=0$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
relations: []
review: draft
solved: true
---

::: problem
- Show that if $f\in C^1(\RR)$ and both $\lim_{x\to \infty} f(x)$ and $\lim_{x\to \infty} f'(x)$ exist, then $\lim_{x\to\infty} f'(x)$ must be zero.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Apply the mean value theorem on $[x, x+1]$.
Proof: $f \in C^1(\RR)$, so for each $x$ there is $\xi_x \in (x, x+1)$ with \[ f(x+1) - f(x) = f'(\xi_x) . \] <1>2. The left-hand side tends to $0$.
Proof: $\lim_{x\to\infty}f(x)$ exists, so $f(x+1) - f(x) \to L - L = 0$.
<1>3. Conclude $\lim_{x\to\infty}f'(x) = 0$.
Proof: $\xi_x \to \infty$ as $x \to \infty$, and $\lim_{x\to\infty}f'(x)$ exists (call it $b$); along the path $x \mapsto \xi_x$, $f'(\xi_x) \to b$.
By <1>1 and <1>2, $b = 0$.
<1>4. Q.E.D.
:::
