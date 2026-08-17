---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-09
kind: problem
title: 'An integral bound involving a twice-differentiable function'
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - differentiation
  - norms
relations: []
review: draft
---

::: {.problem title="?"}
(June 2009 #5b) Let $\phi$ be a real-valued function defined on $[0,1]$ such that $\phi$, $\phi'$, and $\phi''$ are continuous on $[0,1]$.
Prove that
$$
\int_0^1\frac{x\phi'(x)-\phi(x)+\phi(0)}{x^2}\cos x\,dx
<\frac32\|\phi''\|_\infty,
$$
where $\|\phi''\|_\infty=\sup_{[0,1]}|\phi''(x)|$.
Note that $3/2$ may not be the smallest possible constant.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Express the numerator as an integral of $\phi''$.
    Proof: fix $x \in (0,1]$. The numerator is
    \[x\phi'(x) - \phi(x) + \phi(0) = \int_0^x t\,\phi''(t)\,dt.\]
    Indeed, integrating by parts: $\int_0^x t\phi''(t)\,dt = \big[t\phi'(t)\big]_0^x - \int_0^x \phi'(t)\,dt = x\phi'(x) - (\phi(x) - \phi(0))$.
<1>2. Bound the integrand.
    Proof: with $\|\phi''\|_\infty = \sup_{[0,1]}|\phi''|$,
    \[\left|\int_0^x t\phi''(t)\,dt\right| \le \int_0^x t\,|\phi''(t)|\,dt \le \|\phi''\|_\infty\int_0^x t\,dt = \|\phi''\|_\infty\frac{x^2}{2}.\]
<1>3. Integrate over $[0,1]$ with $|\cos x| \le 1$.
    Proof:
    \[\int_0^1 \frac{x\phi'(x) - \phi(x) + \phi(0)}{x^2}\cos x\,dx \le \int_0^1 \frac{\|\phi''\|_\infty x^2/2}{x^2}\,dx = \frac{\|\phi''\|_\infty}{2}\int_0^1 dx = \frac12\|\phi''\|_\infty,\]
    where the inequality uses $|\cos x| \le 1$ and $|$numerator$| \le \|\phi''\|_\infty x^2/2$. In fact the left-hand side is $\le \frac12\|\phi''\|_\infty$, which is $< \frac32\|\phi''\|_\infty$ whenever $\|\phi''\|_\infty > 0$; if $\|\phi''\|_\infty = 0$ then $\phi$ is affine and both sides vanish (so the strict inequality degenerates to equality $0 = 0$, and the claimed bound should be read as $\le$).
<1>4. Q.E.D.
:::
