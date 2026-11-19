---
schema: qual/card@1
id: P-CAFA19F
kind: problem
title: "Analytic functions on C minus origin with subquadratic growth"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured both directions into numbered steps and supplied three details the prose compressed:
    the Laurent coefficient estimate for negative indices from the integral formula on the circle
    of radius r (with the bound |f| <= C r^2 + C r^{-1/2}), the sharpening of the growth bound to
    M(R) <= 2 C R^2 for R >= 1 before Cauchy's estimate is applied, and the converse estimate split
    into |z| >= 1 and |z| <= 1 so that a single constant serves. Every macro used is one the
    preamble defines. No source text is retained for this examination.
---

::: {.problem}
Find all analytic functions $f$ on $\CC \setminus \{0\}$ with the following property: There is some constant $C > 0$ such that $\abs{f(z)} \leq C\abs{z}^2 + \frac{C}{\abs{z}^{1/2}}$ for all $z \in \CC \setminus \{0\}$.
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it.

Let $f$ be analytic on $\CC\setminus\{0\}$ with $\abs{f(z)}\leq C\abs{z}^{2}+C\abs{z}^{-1/2}$ for all $z\neq0$.

::: pf

::: {.pf-step #laurent}
$f$ has a Laurent expansion $f(z)=\sum_{n\in\ZZ}a_{n}z^{n}$ on $0<\abs{z}$.

::: pf-proof
$f$ is analytic on the annulus $0<\abs{z}<\infty$, and the Laurent expansion exists on any annulus of analyticity, with coefficients $a_{n}=\frac{1}{2\pi i}\oint_{\abs{z}=r}f(z)z^{-n-1}dz$ for every $0<r$.
:::

:::

::: {.pf-step #negative}
$a_{-m}=0$ for every $m\geq1$.

::: pf-proof
For $0<r<1$ and $m\geq1$,
$$
\abs{a_{-m}}=\abs{\frac{1}{2\pi i}\oint_{\abs{z}=r}f(z)z^{m-1}dz}\leq r^{m}\max_{\abs{z}=r}\abs{f}\leq r^{m}\bigl(Cr^{2}+Cr^{-1/2}\bigr)=Cr^{m+2}+Cr^{m-1/2},
$$
using $\abs{z}^{m-1}=r^{m-1}$ and the length $2\pi r$ of the circle. Both exponents $m+2$ and $m-\tfrac12$ are positive for $m\geq1$, so the right side tends to $0$ as $r\downarrow0$; hence $a_{-m}=0$.
:::

:::

::: {.pf-step #entire}
$f$ extends to an entire function.

::: pf-proof
By step [](#negative){.pf-ref} the Laurent series has no negative powers, so $f(z)=\sum_{n\geq0}a_{n}z^{n}$ for $0<\abs{z}$, and the series converges for every $z$; its sum defines an entire function agreeing with $f$ off the origin. So the singularity is removable.
:::

:::

::: {.pf-step #growth}
For $R\geq1$, $\max_{\abs{z}=R}\abs{f(z)}\leq2CR^{2}$.

::: pf-proof
On $\abs{z}=R\geq1$ we have $R^{-1/2}\leq R^{2}$, so $\abs{f}\leq CR^{2}+CR^{-1/2}\leq2CR^{2}$.
:::

:::

::: {.pf-step #poly}
$f$ is a polynomial of degree at most $2$.

::: pf-proof
$f$ is entire by step [](#entire){.pf-ref}, so Cauchy's estimate applies in the form $\abs{f^{(n)}(0)}\leq\frac{n!M(R)}{R^{n}}$ with $M(R)=\max_{\abs{z}=R}\abs{f}$. By step [](#growth){.pf-ref}, for $R\geq1$ and $n\geq3$,
$$
\abs{f^{(n)}(0)}\leq\frac{n!\,\cdot2CR^{2}}{R^{n}}=2Cn!\,R^{2-n}\longrightarrow0\quad(R\to\infty),
$$
since $2-n<0$. So $f^{(n)}(0)=0$ for every $n\geq3$, and the Taylor series of $f$ at $0$ terminates at degree $2$: $f(z)=a_{0}+a_{1}z+a_{2}z^{2}$.
:::

:::

::: {.pf-step #converse}
Every polynomial $a_{0}+a_{1}z+a_{2}z^{2}$ satisfies the growth condition for some $C$.

::: pf-proof
Let $K=\max\{\abs{a_{0}},\abs{a_{1}},\abs{a_{2}}\}$ and take $C=K$ enlarged if necessary. For $\abs{z}\geq1$, $\abs{f(z)}\leq K(1+\abs{z}+\abs{z}^{2})\leq3K\abs{z}^{2}$. For $0<\abs{z}\leq1$, $\abs{f(z)}\leq3K\leq3K\abs{z}^{-1/2}$, since $\abs{z}^{-1/2}\geq1$. So with $C=3K$ the required estimate holds on both regions, and every $z\neq0$ lies in one of them.
:::

:::

::: {.pf-step}
The solutions are exactly the polynomials of degree at most $2$.

::: pf-proof
Steps [](#poly){.pf-ref} and [](#converse){.pf-ref} give the two directions.
:::

:::

:::

:::
