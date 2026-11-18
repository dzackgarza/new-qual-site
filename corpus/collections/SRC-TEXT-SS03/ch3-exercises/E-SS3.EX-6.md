---
schema: qual/card@1
id: E-SS3.EX-6
kind: problem
title: $\int_{-\infty}^\infty\frac{dx}{(1+x^2)^{n+1}}=\frac{1\cdot3\cdots(2n-1)}{2\cdot4\cdots(2n)}\pi$
classification:
  areas:
    - complex-analysis
  topics: [Residue Theorem, Contour Integration, Improper Integrals]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
---

::: {.exercise}
Show that
$$
\int_{-\infty}^{\infty} \frac{dx}{(1+x^{2})^{n+1}} = \frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\cdot\pi .
$$
:::

::: {.solution}

The argument is the card's own: an integration by parts on $x/(1+x^{2})^{m-1}$ gives a two-term recursion, and iterating it from $J_{1}=\pi$ gives the product.

::: pf

::: {.pf-step #base}

$J_{1}=\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^{2}}=\pi$.

::: pf-proof

$\frac{d}{dx}\arctan x=\frac1{1+x^{2}}$, so the integral is $\lim_{R\to\infty}\arctan R-\lim_{R\to-\infty}\arctan R=\frac{\pi}{2}-\bigl(-\frac{\pi}{2}\bigr)=\pi$.

:::

:::

::: {.pf-step #parts}

For $m\ge2$, $\displaystyle 0=\int_{-\infty}^{\infty}\Bigl[\frac{1}{(1+x^{2})^{m-1}}-\frac{2(m-1)x^{2}}{(1+x^{2})^{m}}\Bigr]dx$.

::: pf-proof

The function $\frac{x}{(1+x^{2})^{m-1}}$ is differentiable with derivative
$$
\frac{1}{(1+x^{2})^{m-1}}-\frac{2(m-1)x^{2}}{(1+x^{2})^{m}},
$$
by the quotient rule. Its boundary values at $\pm\infty$ are $0$ because the denominator grows like $\abs{x}^{2m-2}$ with $m\ge2$, while the numerator grows like $\abs{x}$. The integral of a derivative over $\RR$ is the difference of the limits at $\pm\infty$, by the fundamental theorem of calculus applied on $[-R,R]$ and then $R\to\infty$, so the integral is $0-0=0$.

:::

:::

::: {.pf-step #recursion}

$J_{m}=\dfrac{2m-3}{2m-2}J_{m-1}$ for $m\ge2$.

::: pf-proof

Since $\frac{x^{2}}{(1+x^{2})^{m}}=\frac{1}{(1+x^{2})^{m-1}}-\frac{1}{(1+x^{2})^{m}}$, step [](#parts){.pf-ref} reads
$$
0=J_{m-1}-2(m-1)\bigl(J_{m-1}-J_{m}\bigr).
$$
Solving, $2(m-1)J_{m}=\bigl(2(m-1)-1\bigr)J_{m-1}=(2m-3)J_{m-1}$, and dividing by the nonzero $2(m-1)$ gives the recursion.

:::

:::

::: {.pf-step #iterate}

$J_{n+1}=\dfrac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\pi$.

::: pf-proof

Induct on $n\ge0$, where $J_{1}=\pi$ is the empty product case. If $J_{n}=\frac{1\cdot3\cdots(2n-3)}{2\cdot4\cdots(2n-2)}\pi$, then by step [](#recursion){.pf-ref} with $m=n+1$,
$$
J_{n+1}=\frac{2n-1}{2n}J_{n}=\frac{1\cdot3\cdots(2n-3)(2n-1)}{2\cdot4\cdots(2n-2)(2n)}\pi.
$$

:::

:::

::: {.pf-step #conclusion}

$\displaystyle\int_{-\infty}^{\infty}\frac{dx}{(1+x^{2})^{n+1}}=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\pi$.

::: pf-proof

The integral in the statement is $J_{n+1}$ by the definition of $J_{m}$, and step [](#iterate){.pf-ref} is exactly the asserted value:
$$
\boxed{\int_{-\infty}^{\infty}\frac{dx}{(1+x^{2})^{n+1}}=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\,\pi.}
$$
At $n=1$ this reads $\int_{\RR}\frac{dx}{(1+x^{2})^{2}}=\frac{\pi}{2}$, which agrees with the recursion $J_{2}=\frac{1}{2}J_{1}$.

:::

:::

:::

:::

::: {.remark title="Variations"}
At $n=1$ the statement gives $\int_\RR\frac{dx}{(1+x^2)^2}=\frac{\pi}{2}$.
:::
