---
schema: qual/card@1
id: P-VG7GK
kind: problem
title: $\int_0^1\cos x\frac{x\phi'(x)-\phi(x)+\phi(0)}{x^2}\,dx<\frac{3}{2}\|\phi''\|_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Differentiation
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $\phi$ be a real-valued function defined on $[0,1]$ such that $\phi$, $\phi'$, and $\phi''$ are continuous on $[0,1]$.
Prove that $$\int_0^1 \cos x \frac{x\phi'(x)-\phi(x)+\phi(0)}{x^2}\,dx<\frac{3}{2}||\phi''||_\infty,$$ where $||\phi''||_\infty = \sup_{[0,1]}|\phi''(x)|.$ Note that $3/2$ may not be the smallest possible constant.
:::
::: {.solution}
<1>1. Rewrite the numerator as an integral.
    ::: {.proof}
    let $N(x) \da x\phi'(x) - \phi(x) + \phi(0)$. Differentiating,
    :::
    \[
    \frac{d}{dx}\big(x\phi'(x) - \phi(x) + \phi(0)\big) = \phi'(x) + x\phi''(x) - \phi'(x) = x\phi''(x),
    \]
    and $N(0) = 0\cdot\phi'(0) - \phi(0) + \phi(0) = 0$. Hence by the fundamental theorem of calculus,
    \[
    N(x) = \int_0^x y\,\phi''(y)\,dy .
    \]
<1>2. Bound $|N(x)|$.
    ::: {.proof}
    by <1>1,
    :::
    \[
    |N(x)| \le \int_0^x y\,|\phi''(y)|\,dy \le \norm{\phi''}_\infty \int_0^x y\,dy = \norm{\phi''}_\infty \frac{x^2}{2} .
    \]
<1>3. Bound the integrand.
    ::: {.proof}
    for $x > 0$,
    :::
    \[
    \Big|\cos x \cdot \frac{N(x)}{x^2}\Big| \le \frac{|N(x)|}{x^2} \le \frac{\norm{\phi''}_\infty}{2},
    \]
    using $|\cos x| \le 1$ and <1>2. (The integrand is bounded as $x \to 0^+$ by the same estimate, so it extends continuously to $0$.)
<1>4. Conclude.
    ::: {.proof}
    integrating <1>3 over $[0,1]$,
    :::
    \[
    \int_0^1 \cos x \,\frac{x\phi'(x) - \phi(x) + \phi(0)}{x^2}\,dx \le \int_0^1 \frac{\norm{\phi''}_\infty}{2}\,dx = \frac{1}{2}\norm{\phi''}_\infty < \frac{3}{2}\norm{\phi''}_\infty .
    \]
    (The constant $3/2$ in the problem is not optimal; $1/2$ suffices.)
<1>5. Q.E.D.
:::
