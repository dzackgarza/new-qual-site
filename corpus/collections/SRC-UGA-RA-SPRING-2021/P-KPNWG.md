---
schema: qual/card@1
id: P-KPNWG
kind: problem
title: $\lim_{n\to\infty}\int_0^n\frac{\cos(x/n)}{x^2+\cos(x/n)}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 2 of the official UGA January 2021 Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Replaced the legacy DCT domination by the uniform integrable bound obtained from cos(x/n) at least cos(1) on the integration range 0<x<n.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps. The collection is a course examination, so the problem
    statement is the source and the argument is the card's own. The exercise asks that each step of
    the calculation be justified, so the domination is a step of its own: on the support x < n one
    has 0 < x/n < 1 and hence cos(x/n) >= cos 1 > 0, which bounds 0 <= F_n(x) <= 1/(x^2 + cos 1),
    and that dominating function is integrable; the pointwise limit is 1/(x^2+1); and the remaining
    integral is arctan. The nonvanishing of the denominator is stated separately since the
    integrand would otherwise be undefined on a set depending on n. Not claimed: any rate of
    convergence, which the theorem does not give.
---

::: {.problem}
Calculate the following limit, justifying each step of your calculation:
$$
L \coloneqq \lim_{n\to \infty} \int_0^n { \cos\qty{x\over n} \over x^2 + \cos\qty{x\over n} }\dx
.$$
:::


::: {.solution}
The argument is the card's own; the collection is a course examination, so the problem statement is the source.

::: pf

::: {.pf-step #integrand}
For $x>0$ define $F_{n}(x)=\mathbf{1}_{(0,n)}(x)\dfrac{\cos(x/n)}{x^{2}+\cos(x/n)}$; then $L=\lim_{n}\int_{0}^{\infty}F_{n}$.

::: pf-proof
$\int_{0}^{n}\frac{\cos(x/n)}{x^{2}+\cos(x/n)}dx=\int_{0}^{\infty}\mathbf{1}_{(0,n)}(x)\frac{\cos(x/n)}{x^{2}+\cos(x/n)}dx$ because the indicator cuts off the integrand at $n$; the $F_{n}$ are measurable as products of measurable functions, provided the denominator never vanishes, which step [](#denominator){.pf-ref} shows.
:::

:::

::: {.pf-step #denominator}
For $0<x<n$ one has $\cos(x/n)\ge\cos1>0$, so the denominator is at least $\cos1>0$ there.

::: pf-proof
$0<x/n<1$ and $\cos$ is decreasing on $[0,\pi]$ with $1<\pi$, so $\cos(x/n)\ge\cos1>0$; then $x^{2}+\cos(x/n)\ge\cos1>0$.
:::

:::

::: {.pf-step #pointwise}
For each fixed $x>0$, $F_{n}(x)\to\dfrac{1}{x^{2}+1}$.

::: pf-proof
For $n>x$ the indicator is $1$, and $x/n\to0$, so by continuity of $\cos$ at $0$ the numerator tends to $\cos0=1$ while the denominator tends to $x^{2}+1$; a quotient of convergent sequences with nonzero limit in the denominator converges to the quotient.
:::

:::

::: {.pf-step #dominated}
$0\le F_{n}(x)\le\dfrac{1}{x^{2}+\cos1}$ for all $x>0$ and all $n$, and $x\mapsto\frac{1}{x^{2}+\cos1}$ is integrable on $(0,\infty)$.

::: pf-proof
If $x\ge n$ then $F_{n}(x)=0$. If $0<x<n$ then by step [](#denominator){.pf-ref} both numerator and denominator are positive, so $F_{n}(x)\ge0$, and $\cos(x/n)\le1$ with $x^{2}+\cos(x/n)\ge x^{2}+\cos1$ give $F_{n}(x)\le\frac{1}{x^{2}+\cos1}$. The dominating function is continuous and $O(x^{-2})$ at infinity, hence integrable, and near $0$ it is bounded by $1/\cos1$.
:::

:::

::: {.pf-step #value}
$L=\int_{0}^{\infty}\dfrac{dx}{x^{2}+1}=\dfrac{\pi}{2}$.

::: pf-proof
Steps [](#pointwise){.pf-ref} and [](#dominated){.pf-ref} are the hypotheses of the dominated convergence theorem, which gives $L=\int_{0}^{\infty}\frac{dx}{x^{2}+1}$. An antiderivative of $\frac{1}{1+x^{2}}$ is $\arctan x$, so the integral is $\lim_{R\to\infty}\arctan R-\arctan0=\frac{\pi}{2}-0$.
:::

:::

::: {.pf-step}
$L=\pi/2$.

::: pf-proof
Step [](#value){.pf-ref} gives
$$
\boxed{L=\lim_{n\to\infty}\int_{0}^{n}\frac{\cos(x/n)}{x^{2}+\cos(x/n)}\,dx=\frac{\pi}{2}.}
$$
The justification the exercise asks for is the domination of step [](#dominated){.pf-ref}, whose constant $\cos1$ comes from the cutoff $x<n$; the bound is not integrable without that constant, so the two hypotheses are used together.
:::

:::

:::
:::
