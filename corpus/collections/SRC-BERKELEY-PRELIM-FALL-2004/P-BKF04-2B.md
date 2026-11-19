---
schema: qual/card@1
id: P-BKF04-2B
kind: problem
title: Decay of the Newtonian potential $\int f(y)/\norm{x-y}\,dy$ of a compactly supported $f$ on $\RR^3$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured both parts into numbered steps. In (a) supplied that the maximum exists because a
    continuous function on a compact support is bounded, and the explicit polar evaluation of the
    majorant. In (b) supplied what the prose compressed into "using linearity reduces to nonnegative
    f": the decomposition f = f+ - f-, the linearity of u in f and of the integral, and the
    conclusion that the limit is the integral of f (not of |f|), which is the content of the
    sandwich for a signed function. Also made the quantifier step explicit: the estimate holds for
    every n with |x| >= n R0, so the ratio can be pushed to 1. Every macro used is one the preamble
    defines. No source text is retained for this examination.
---

::: {.problem}
Let $f \colon \RR^{3} \to \RR$ be a continuous function of compact support (i.e., $f$ vanishes outside some bounded set).

(a) Show that
$$
u(x) := \int \frac{f(y)}{\norm{x - y}}\, dy
$$
converges, where the integral is over all $y \in \RR^{3}$.

(b) Show that $\lim_{\norm{x}\to\infty} u(x)\norm{x}$ exists.
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it.

Let $f\colon\RR^{3}\to\RR$ be continuous with compact support and $u(x)=\int_{\RR^{3}}\frac{f(y)}{\norm{x-y}}dy$.

::: pf

::: {.pf-step #bounded}
$f$ is bounded and supported in a bounded set.

::: pf-proof
The support is contained in a closed ball $\overline{B(0,R_{0})}$, which is compact, and $f$ is continuous, so $f$ attains a maximum $M=\max\abs{f}<\infty$ on it; outside it $f=0$.
:::

:::

::: {.pf-step #converges}
For each $x$ the integral defining $u(x)$ converges absolutely.

::: pf-proof
Since $f(y)=0$ for $\norm{y}>R_{0}$, the integrand is supported in $B(x,R_{1})$ for $R_{1}=R_{0}+\norm{x}$. Using polar coordinates centred at $x$, where the surface measure of the sphere of radius $r$ is $4\pi r^{2}$,
$$
\int\frac{\abs{f(y)}}{\norm{x-y}}dy\leq\int_{0}^{R_{1}}\frac{M}{r}4\pi r^{2}dr=2\pi MR_{1}^{2}<\infty .
$$
:::

:::

::: {.pf-step #linear}
$u$ is linear in $f$.

::: pf-proof
For $f,g$ and scalars $a,b$, the integrand of $u(af+bg)$ at $y$ is $\frac{af(y)+bg(y)}{\norm{x-y}}$, and the integral of a finite sum of integrable functions is the sum of the integrals, each integrable by step [](#converges){.pf-ref}; so $u(af+bg)=au(f)+bu(g)$ for each $x$.
:::

:::

::: {.pf-step #positive}
If $f\geq0$ then $u(x)\norm{x}\to\int f\,dy$ as $\norm{x}\to\infty$.

::: pf-proof
Fix $n\geq2$ and let $\norm{x}\geq nR_{0}$. For $y$ in the support, $\norm{y}\leq R_{0}\leq\norm{x}/n$, so by the triangle inequality
$$
\frac{n}{n+1}=\frac{1}{1+1/n}\leq\frac{\norm{x}}{\norm{x}+\norm{y}}\leq\frac{\norm{x}}{\norm{x-y}}\leq\frac{\norm{x}}{\norm{x}-\norm{y}}\leq\frac{1}{1-1/n}=\frac{n}{n-1}.
$$
Multiplying by $f(y)\geq0$ and integrating, and using $\int f(y)\,dy>-\infty$,
$$
\frac{n}{n+1}\int f\,dy\leq u(x)\norm{x}\leq\frac{n}{n-1}\int f\,dy .
$$
Given $\varepsilon>0$ choose $n$ so large that $\frac{n}{n\pm1}$ are within $\varepsilon$ of $1$; then for all $\norm{x}\geq nR_{0}$ the value $u(x)\norm{x}$ lies within $\varepsilon\int f$ of $\int f$, which is convergence.
:::

:::

::: {.pf-step #signed}
For arbitrary $f$, $u(x)\norm{x}\to\int f\,dy$.

::: pf-proof
Write $f=f^{+}-f^{-}$ with $f^{\pm}=\max\{\pm f,0\}\geq0$, both continuous with the same compact support. By steps [](#linear){.pf-ref} and [](#positive){.pf-ref}, $u(f^{\pm})(x)\norm{x}\to\int f^{\pm}dy$, hence
$$
u(x)\norm{x}=u(f^{+})(x)\norm{x}-u(f^{-})(x)\norm{x}\longrightarrow\int f^{+}dy-\int f^{-}dy=\int f\,dy .
$$
The limit of the difference exists because both limits do.
:::

:::

::: {.pf-step}
$u$ is well defined by an absolutely convergent integral and $\lim_{\norm{x}\to\infty}u(x)\norm{x}=\int_{\RR^{3}}f(y)\,dy$ exists.

::: pf-proof
Steps [](#converges){.pf-ref} and [](#signed){.pf-ref} are parts (a) and (b). Note that the limit is the integral of $f$, not of $\abs{f}$; for a signed $f$ the two differ, and it is the decomposition of step [](#signed){.pf-ref} that identifies the correct value.
:::

:::

:::

:::
