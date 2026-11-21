---
schema: qual/card@1
id: P-SAIVF
kind: problem
title: A function in $L^2([0,1])$ orthogonal to every polynomial vanishes a.e.
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Density
  - L²
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2018 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2018.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: {.problem}
Let $f\in L^2([0,1])$ and suppose
$$
\int_0^1 f(x)x^n\,dx=0
\qquad\text{for every integer }n\ge0.
$$
Show that $f=0$ almost everywhere.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper (`assets/attachments/Real_Analysis_Spring_2018.docx`) and no solutions sheet accompanies it, so the argument below is the card's own. The earlier version of the card passed from "polynomials are dense in $C$ and $C$ is dense in $L^{2}$" to "hence polynomials are dense in $L^{2}$" without the comparison of norms that makes that inference valid on $[0,1]$; that comparison is supplied here.

Throughout, $f\in L^{2}([0,1])$ with $\int_{0}^{1}f(x)x^{n}\,dx=0$ for every integer $n\geq0$, the inner product is $\inner{g}{h}=\int_{0}^{1}g\bar h$, and $\norm{\cdot}_{2}$ and $\norm{\cdot}_{\infty}$ are the $L^{2}$ and supremum norms on $[0,1]$.

::: pf

::: {.pf-step #all-polynomials}
$\inner{f}{p}=0$ for every polynomial $p$.

::: pf-proof
A polynomial is a finite sum $p=\sum_{n=0}^{N}c_{n}x^{n}$, so by linearity of the integral $\inner{f}{p}=\sum_{n}c_{n}\int_{0}^{1}f(x)x^{n}\,dx=\sum_{n}c_{n}\cdot0=0$.
:::

:::

::: {.pf-step #dense}
The polynomials are dense in $L^{2}([0,1])$.

:::: pf-proof

::: {.pf-step #norm-comparison}
$\norm{g}_{2}\leq\norm{g}_{\infty}$ for every $g\in C([0,1])$.

::: pf-proof
$\norm{g}_{2}^{2}=\int_{0}^{1}\abs{g}^{2}\leq\int_{0}^{1}\norm{g}_{\infty}^{2}=\norm{g}_{\infty}^{2}$ because $\abs{g}\leq\norm{g}_{\infty}$ on $[0,1]$.
:::

:::

::: {.pf-step #two-approximations}
For every $h\in L^{2}([0,1])$ and $\varepsilon>0$ there is a polynomial $p$ with $\norm{h-p}_{2}<\varepsilon$.

::: pf-proof
Continuous functions are dense in $L^{2}([0,1])$, so choose $g\in C([0,1])$ with $\norm{h-g}_{2}<\varepsilon/2$. By the Weierstrass approximation theorem choose a polynomial $p$ with $\norm{g-p}_{\infty}<\varepsilon/2$; then $\norm{g-p}_{2}\leq\norm{g-p}_{\infty}<\varepsilon/2$ by step [](#norm-comparison){.pf-ref}. The triangle inequality gives $\norm{h-p}_{2}\leq\norm{h-g}_{2}+\norm{g-p}_{2}<\varepsilon$.
:::

:::

::::

:::

::: pf-step
Therefore
$$
\boxed{f=0\text{ almost everywhere}.}
$$

::: pf-proof
By step [](#dense){.pf-ref} choose polynomials $p_{j}$ with $\norm{f-p_{j}}_{2}\to0$. Since $\inner{f}{p_{j}}=0$ by step [](#all-polynomials){.pf-ref},
$$
\norm{f}_{2}^{2}=\inner{f}{f}=\inner{f}{f}-\inner{f}{p_{j}}=\inner{f}{f-p_{j}}\leq\norm{f}_{2}\norm{f-p_{j}}_{2}
$$
by the Cauchy--Schwarz inequality, for every $j$. If $\norm{f}_{2}=0$ we are done; otherwise divide by $\norm{f}_{2}$ to get $\norm{f}_{2}\leq\norm{f-p_{j}}_{2}$ for all $j$, and letting $j\to\infty$ gives $\norm{f}_{2}\leq0$, so $\norm{f}_{2}=0$ in either case. A function in $L^{2}$ with vanishing norm is zero almost everywhere, since $\int_{0}^{1}\abs{f}^{2}=0$ forces $\abs{f}=0$ off a set of measure zero.
:::

:::

:::

:::
