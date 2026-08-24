---
schema: qual/card@1
id: P-SKT7G
kind: problem
title: $\lim_{x\to\infty}f'(x)=0$ whenever $\lim f$ and $\lim f'$ exist at infinity;
  a counterexample when $\lim f'$ fails to exist
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
  - Counterexamples
relations: []
review: draft
---

::: problem
Let $f:\mathbb{R}\to\mathbb{R}$ be a differentiable function with $f'\in C(\mathbb{R})$.
Assume that there are $a,b\in\mathbb{R}$ with $\lim_{x\to\infty}f(x)=a$ and $\lim_{x\to\infty}f'(x)=b$.
Prove that $b=0$.
Then, find a counterexample to show that the assumption $\lim_{x\to\infty}f'(x)$ exists is necessary.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $b = 0$.
Proof: by the mean value theorem applied to $f$ on $[x, x+1]$, for each $x$ there is $\xi_x \in (x, x+1)$ with \[ f(x+1) - f(x) = f'(\xi_x) . \] As $x \to \infty$, the left side tends to $a - a = 0$ (both $f(x+1)$ and $f(x)$ tend to $a$). Also $\xi_x \to \infty$, so $f'(\xi_x) \to b$ (since $\lim_{x\to\infty} f'(x) = b$). Hence $b = 0$.
<1>2. The assumption that $\lim_{x\to\infty} f'(x)$ exists is necessary.
Proof: $f(x) = \sin(x^2)/x$ tends to $0$ as $x \to \infty$, but \[ f'(x) = 2\cos(x^2) - \frac{\sin(x^2)}{x^2}, \] whose limit as $x \to \infty$ does not exist (the term $2\cos(x^2)$ oscillates between $-2$ and $2$ while the second term tends to $0$). So $f$ is differentiable, $\lim f = 0$, yet $\lim f'$ fails to exist.
<1>3. Q.E.D.
:::
