---
schema: qual/card@1
id: P-RASP21C
kind: problem
title: "Function with prescribed moments"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Spring 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps. The collection is a course examination, so the problem
    statement is the source and the argument is the card's own. Each step re-read: h = f - x is in
    L^2 and hence L^1 on the finite measure space, and its even moments vanish because the moments
    of x match; vanishing against powers x^{2n} gives vanishing against every polynomial in x^2; and
    the Weierstrass step is applied to psi composed with the square root, which is where the
    structure of the moments is used, and then a single epsilon absorbs the L^1 norm of h. The
    conclusion that a density integrating every continuous function to zero is zero is kept as a
    step. Not claimed: any statement about the converse, or about moments against all powers rather
    than the even ones.
---

::: {.problem}
If $f \in L^2([0,1])$ and $\int_0^1 x^{2n} f(x)\,dx = \frac{1}{2n+2}$ for all $n = 0, 1, 2, \ldots$, is $f(x) = x$ a.e.?
:::


::: {.solution}
The argument is the card's own; the collection is a course examination, so the problem statement is the source.

::: pf

::: {.pf-step #h}
With $h=f-x$: $h\in L^{1}([0,1])$ and $\int_{0}^{1}x^{2n}h(x)\,dx=0$ for every $n\ge0$.

::: pf-proof
$f\in L^{2}([0,1])$ and $x\in L^{2}([0,1])$, so $h\in L^{2}([0,1])$; and $L^{2}([0,1])\subseteq L^{1}([0,1])$ because $[0,1]$ has finite measure, so $h\in L^{1}$. The hypothesis gives $\int x^{2n}f=\frac{1}{2n+2}$, and $\int_{0}^{1}x^{2n+1}dx=\frac{1}{2n+2}$; subtracting gives the vanishing.
:::

:::

::: {.pf-step #polys}
$\int_{0}^{1}h(x)p(x^{2})\,dx=0$ for every polynomial $p$.

::: pf-proof
A polynomial $p(t)=\sum_{n=0}^{N}c_{n}t^{n}$ gives $p(x^{2})=\sum_{n}c_{n}x^{2n}$, and the integral is the finite sum $\sum_{n}c_{n}\int x^{2n}h$, which vanishes term by term by step [](#h){.pf-ref}.
:::

:::

::: {.pf-step #weierstrass}
For every continuous $\psi$ on $[0,1]$ and every $\varepsilon>0$ there is a polynomial $p$ with $\norm{\psi-p(x^{2})}_{\infty}<\varepsilon$.

::: pf-proof
$\psi\circ\sqrt{\cdot}$ is continuous on $[0,1]$, where $\sqrt\cdot$ is continuous and $\psi$ is continuous; by the Weierstrass approximation theorem there is a polynomial $p$ with $\sup_{t\in[0,1]}\abs{\psi(\sqrt t)-p(t)}<\varepsilon$. Substituting $t=x^{2}\in[0,1]$ gives $\abs{\psi(x)-p(x^{2})}<\varepsilon$ for all $x\in[0,1]$.
:::

:::

::: {.pf-step #annihilate}
$\int_{0}^{1}h\,\psi=0$ for every continuous $\psi$.

::: pf-proof
By steps [](#polys){.pf-ref} and [](#weierstrass){.pf-ref},
$$
\abs{\int_{0}^{1}h\psi}\le\abs{\int_{0}^{1}h\,p(x^{2})}+\int_{0}^{1}\abs{h}\abs{\psi-p(x^{2})}\le0+\norm{h}_{1}\varepsilon ,
$$
so the integral is smaller than $\norm{h}_{1}\varepsilon$ for every $\varepsilon>0$, hence is $0$.
:::

:::

::: {.pf-step #zero}
$h=0$ almost everywhere.

::: pf-proof
The finite signed measure $h\,dx$ annihilates every continuous function on $[0,1]$ by step [](#annihilate){.pf-ref}. A finite Borel measure that integrates every continuous function to $0$ is the zero measure (test against continuous functions approximating the indicator of an open set from both sides), and a measure with density $h$ is zero exactly when $h=0$ a.e.
:::

:::

::: {.pf-step}
$f(x)=x$ almost everywhere.

::: pf-proof
Steps [](#h){.pf-ref} to [](#zero){.pf-ref} give
$$
\boxed{f(x)=x\text{ for almost every }x\in[0,1],}
$$
so the answer to the question is yes. The moments used are those against $x^{2n}$, that is against polynomials in $x^{2}$; that is why the argument passes through $\psi\circ\sqrt{\cdot}$ rather than through the plain Weierstrass theorem.
:::

:::

:::
:::
