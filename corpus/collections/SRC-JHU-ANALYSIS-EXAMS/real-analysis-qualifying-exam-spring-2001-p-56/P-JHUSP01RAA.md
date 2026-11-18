---
schema: qual/card@1
id: P-JHUSP01RAA
kind: problem
title: 'Mollifier convolutions converge in $L^p$ but not in $L^\infty$'
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $\phi\in C_c^\infty(\RR^n)$ satisfy $\int\phi=1$, and define
$$
\phi_\varepsilon(x)=\varepsilon^{-n}\phi(x/\varepsilon).
$$
Prove that if $1\le p<\infty$ and $f\in L^p(\RR^n)$, then
$$
f*\phi_\varepsilon\to f
\qquad\text{in }L^p.
$$
Show that the analogous statement fails for $p=\infty$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the change of variables, Minkowski's inequality and the counterexample at $p=\infty$ as separate steps.

::: pf

::: {.pf-step #rewrite}
$(f*\phi_{\varepsilon})(x)-f(x)=\displaystyle\int_{\RR^{n}}\phi(z)\big(f(x-\varepsilon z)-f(x)\big)dz$.

::: pf-proof
$(f*\phi_{\varepsilon})(x)=\int f(x-y)\varepsilon^{-n}\phi(y/\varepsilon)dy$; substituting $y=\varepsilon z$ gives $\int f(x-\varepsilon z)\phi(z)dz$, and $\int\phi(z)f(x)dz=f(x)\int\phi=f(x)$ since $\int\phi=1$.
:::

:::

::: {.pf-step #minkowski}
$\norm{f*\phi_{\varepsilon}-f}_{p}\le\displaystyle\int\abs{\phi(z)}\,\norm{f(\cdot-\varepsilon z)-f}_{p}\,dz$.

::: pf-proof
By step [](#rewrite){.pf-ref} the difference is the integral over $z$ of the functions $x\mapsto\phi(z)\big(f(x-\varepsilon z)-f(x)\big)$; Minkowski's integral inequality bounds the $L^{p}$ norm of such an integral by the integral of the $L^{p}$ norms.
:::

:::

::: {.pf-step #limit}
For $1\le p<\infty$, $\norm{f*\phi_{\varepsilon}-f}_{p}\to0$.

::: pf-proof
Translation is continuous in $L^{p}$: $\norm{f(\cdot-h)-f}_{p}\to0$ as $h\to0$. So the integrand in step [](#minkowski){.pf-ref} tends to $0$ for each $z$, and it is dominated by $2\norm{f}_{p}\abs{\phi(z)}$, which is integrable on the compact support of $\phi$; dominated convergence gives the limit $0$.
:::

:::

::: {.pf-step #infinite}
The statement fails for $p=\infty$.

::: pf-proof
Let $f=\chi_{(-\infty,0]}\in L^{\infty}$, which is discontinuous at $0$. Each $f*\phi_{\varepsilon}$ is continuous, being a convolution with a smooth compactly supported function. If $f*\phi_{\varepsilon}\to f$ in $L^{\infty}$, the limit would be a uniform limit of continuous functions, hence continuous; but $f$ is not continuous at $0$. So convergence fails in $L^{\infty}$.
:::

:::

::: {.pf-qed}
For $1\le p<\infty$ the convergence holds by steps [](#rewrite){.pf-ref}--[](#limit){.pf-ref}, and it fails at $p=\infty$ by step [](#infinite){.pf-ref}.
:::

:::

:::
