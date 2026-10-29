---
schema: qual/card@1
id: P-WOHZ6
kind: problem
title: Uniform convergence of $\sum\sin(nz)/2^n$ on $\{\Im z<\ln 2\}$ and on $\abs{z}\le
  r$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Convergence Tests
  - Series of Functions
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source asks to prove uniform convergence on the half-plane Im z < ln 2, which is false, since the series diverges where Im z <= -ln 2. Part (a) asks whether it converges uniformly there; an earlier hedge inviting the reader to supply a domain was removed.'
---

::: {.problem}
Consider the series of complex functions:
$$
\sum_{n=1}^\infty \frac{\sin(nz)}{2^n}.
$$

(a) Determine whether the series converges uniformly on the half-plane $\{ z \in \CC \mid \Im(z) < \ln 2 \}$.

(b) Prove that for every $r$ with $0<r<\ln 2$, the series converges **uniformly on the closed disk** $\{ z \in \CC \mid \abs{z} \le r \}$.
:::

::: {.solution}
Write $z=x+iy$.

::: pf

::: {.pf-step #bound}

$\abs{\dfrac{\sin(nz)}{2^n}} \le \qty(\dfrac{e^{\abs{y}}}{2})^n$.

::: pf-proof

From $\sin(nz)=\frac{e^{inz}-e^{-inz}}{2i}$ and $\abs{e^{\pm inz}} = e^{\mp ny}$ we get $\abs{\sin(nz)}\le \frac{e^{-ny}+e^{ny}}2\le e^{n\abs{y}}$.

:::

:::

::: {.pf-step #strip}

The series converges uniformly on every closed strip $\abs{\Im z}\le Y$ with $Y<\ln2$.

::: pf-proof

By step [](#bound){.pf-ref} the terms are bounded there by $(e^Y/2)^n$, a convergent geometric series, and the Weierstrass $M$-test applies.

:::

:::

::: {.pf-step #diverge}

The series diverges at every $z$ with $\abs{\Im z}\ge\ln2$.

::: pf-proof

For $\abs{y} \geq \ln 2$, $\abs{\sin(nz)} \geq \frac{e^{n\abs{y}}-e^{-n\abs{y}}}{2}$ by the reverse triangle inequality, so $\frac{\abs{\sin(nz)}}{2^n} \geq \frac12\qty(\frac{e^{\abs{y}}}{2})^n - \frac{1}{2^{n+1}} \geq \frac12 - \frac{1}{2^{n+1}}$, since $e^{\abs{y}}/2 \geq 1$. The terms do not tend to $0$.

:::

:::

::: pf-step

(a) The series does $\boxed{\text{not}}$ converge uniformly on the half-plane $\Im z<\ln2$. It converges exactly on the strip $\abs{\Im z}<\ln2$, uniformly on each closed substrip $\abs{\Im z}\le Y<\ln2$ and hence on compact subsets of the strip.

::: pf-proof

The half-plane contains points with $\Im z \leq -\ln 2$, where the series diverges by step [](#diverge){.pf-ref}. The rest is steps [](#strip){.pf-ref} and [](#diverge){.pf-ref}.

:::

:::

::: pf-step

(b) For $0<r<\ln2$, the series converges uniformly on $\abs{z}\le r$.

::: pf-proof

If $\abs{z}\le r$, then $\abs{\Im z}\le r<\ln 2$, so this follows from step [](#strip){.pf-ref} with $Y = r$.

:::

:::

:::

:::
