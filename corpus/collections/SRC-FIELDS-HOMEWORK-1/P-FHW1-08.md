---
schema: qual/card@1
id: P-FHW1-08
kind: problem
title: A cubic with a root in a quadratic extension has a root in the base field
classification:
  areas: [algebra]
  topics: [Field Extensions, Polynomials]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $f(x)\in K[x]$ be a polynomial of degree $3$. Show that if $f(x)$ has a root in a field extension $K\subset F$ of degree $2$, then $f(x)$ has a root in $K$.
:::

::: {.solution}
Let $\alpha\in F$ be a root of $f$, and let $g\in K[x]$ be the minimal polynomial of $\alpha$ over $K$.

::: pf

::: {.pf-step #g-divides-f}
$g$ divides $f$ in $K[x]$, so $\deg g\in\{1,2,3\}$.

::: pf-proof
The polynomial $g$ is the monic generator of the ideal of polynomials in $K[x]$ vanishing at $\alpha$; since $f(\alpha)=0$ and $f\ne0$, that ideal is nonzero and $g$ divides $f$.
Hence $\deg g\le\deg f=3$.
:::

:::

::: {.pf-step #g-degree-divides-two}
$[K(\alpha):K]=\deg g$ divides $[F:K]=2$.

::: pf-proof
The field $K(\alpha)$ is an intermediate field of $K\subseteq K(\alpha)\subseteq F$, so the tower law gives $[F:K]=[F:K(\alpha)]\,[K(\alpha):K]$, and $[K(\alpha):K]=\deg g$ is the degree of the minimal polynomial.
:::

:::

::: {.pf-step #root-in-k}
$f$ has a root in $K$.

::: pf-proof
By steps [](#g-divides-f){.pf-ref} and [](#g-degree-divides-two){.pf-ref} the degree $\deg g$ is a divisor of both $3$ and $2$, hence $\deg g=1$.
A minimal polynomial of degree $1$ has the form $x-c$ with $c\in K$, and $g(\alpha)=0$ then gives $\alpha=c\in K$.
:::

:::

:::

:::
