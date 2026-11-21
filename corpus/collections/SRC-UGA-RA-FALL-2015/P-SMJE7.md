---
schema: qual/card@1
id: P-SMJE7
kind: problem
title: The limit $\lim_{n\to\infty}\int_1^n \frac{n e^{-x}}{1+nx^2}\sin(x/n)\,dx$
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
  date: 2026-09-08
  note: Checked against Problem 3 of the UGA Fall 2015 real-analysis qualifying exam recorded by SRC-UGA-RA-FALL-2015.
- event: solution-written
  by: prior-author
  date: 2026-08-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's solution into numbered steps and cleaned the display: the pointwise
    limit, the dominating function and the appeal to the dominated convergence theorem are the
    card's own. Checked: the pointwise convergence of n/(1+nx^2) and of sin(x/n), the bound
    n/(1+nx^2) <= 1/x^2, and the integrability of e^{-x}/x^2 on (1, infinity). Not checked against
    a printed source: the UGA preliminary examinations are not retained in tmp/sources and the
    card records no page.
---

::: {.problem}
Compute the following limit:
$$
\lim _{n \rightarrow \infty} \int_{1}^{n} \frac{n e^{-x}}{1+n x^{2}} \, \sin \left(\frac x n\right) \, dx
$$

:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $f_n(x)=\frac{ne^{-x}}{1+nx^{2}}\sin(x/n)\chi_{[1,n]}(x)$ on $(1,\infty)$, so the integral in the statement is $\int_1^{\infty}f_n$, and the criterion used is the dominated convergence theorem.

::: pf

::: {.pf-step #pointwise}

$f_n(x)\to0$ for every $x>1$.

::: pf-proof

$\frac{n}{1+nx^{2}}=\frac{1}{1/n+x^{2}}\to\frac{1}{x^{2}}$ as $n\to\infty$ for fixed $x>0$, $\sin(x/n)\to0$, and $\chi_{[1,n]}(x)=1$ once $n\geq x$. The product of a bounded convergent factor with one tending to $0$ tends to $0$.

:::

:::

::: {.pf-step #dominated}

$\abs{f_n(x)}\leq g(x)\coloneqq\frac{e^{-x}}{x^{2}}$ for $x>1$.

::: pf-proof

$\frac{n}{1+nx^{2}}\leq\frac{n}{nx^{2}}=\frac{1}{x^{2}}$ since $1+nx^{2}\geq nx^{2}$, and $\abs{\sin(x/n)}\leq1$, $\chi_{[1,n]}\leq1$.

:::

:::

::: {.pf-step #l1}

$g\in L^{1}(1,\infty)$.

::: pf-proof

$\int_1^{\infty}x^{-2}\,dx=1<\infty$ and $0<e^{-x}\leq1$, so $\int_1^{\infty}g\leq1$.

:::

:::

::: {.pf-step #done}

$\lim_{n\to\infty}\int_1^{\infty}f_n=0$.

::: pf-proof

The dominated convergence theorem applies by steps [](#pointwise){.pf-ref}, [](#dominated){.pf-ref} and [](#l1){.pf-ref}, and gives $\lim\int_1^{\infty}f_n=\int_1^{\infty}\lim f_n=0$.

:::

:::

:::

:::
