---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-08
kind: problem
title: 'A function and its derivative cannot converge to nonzero limits at infinity'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - limits
  - counterexamples
relations: []
review: draft
---

::: {.problem title="?"}
(January 2012 #4b, extended) Let $f:\mathbb R\to\mathbb R$ be a differentiable function with $f'\in C(\mathbb R)$.
Assume that there are $a,b\in\mathbb R$ with $$\lim_{x\to\infty}f(x)=a\qquad\text{and}\qquad\lim_{x\to\infty}f'(x)=b.$$ Prove that $b=0$.
Then, find a counterexample to show that the assumption $\lim_{x\to\infty}f'(x)$ exists is necessary.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Apply the mean value theorem on $[x, x+1]$.
    Proof: for each $x \in \mathbb{R}$, $f$ is differentiable (hence continuous) on $[x, x+1]$, so by MVT there is $\xi_x \in (x, x+1)$ with
    \[f(x+1) - f(x) = f'(\xi_x).\]
    As $x \to \infty$, $f(x+1) \to a$ and $f(x) \to a$, so $f(x+1) - f(x) \to 0$; hence $f'(\xi_x) \to 0$.
<1>2. $b = 0$.
    Proof: since $\xi_x \to \infty$ and $\lim_{t\to\infty}f'(t) = b$ exists, the limit along the particular sequence $(\xi_x)$ is $b$: $f'(\xi_x) \to b$. But <1>1 gives $f'(\xi_x) \to 0$. Hence $b = 0$.
<1>3. The assumption $\lim_{x\to\infty} f'(x)$ exists is necessary.
    Proof: take $f(x) = \frac{\sin(x^2)}{x}$ for $x \ge 1$. Then $f(x) \to 0$ as $x \to \infty$ (as $|\sin(x^2)| \le 1$), but
    \[f'(x) = \frac{2x^2\cos(x^2) - \sin(x^2)}{x^2} = 2\cos(x^2) - \frac{\sin(x^2)}{x^2},\]
    which oscillates (e.g. along $x_n = \sqrt{n\pi}$, $f'(x_n) \to 2(-1)^n$, no limit). So $f \to 0$ while $f'$ has no limit; the conclusion $b = 0$ is vacuous and the MVT argument cannot be run without the existence of the limit. (The counterexample shows the theorem's hypothesis is not superfluous.)
<1>4. Q.E.D.
:::
