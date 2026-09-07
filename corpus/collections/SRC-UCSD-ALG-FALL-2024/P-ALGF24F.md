---
schema: qual/card@1
id: P-ALGF24F
kind: problem
title: Irreducibility of $x^p - x + 1$ over $\mathbb{F}_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Compared the statement with Problem 6 on page 8 of the official FA24 algebra exam PDF.
- event: solution-written
  by: gpt-6-astra-pro
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Verified that Frobenius supplies p distinct roots of the minimal polynomial, forcing its degree to be p; the argument includes p=2.
---

::: problem
Suppose $p$ is a prime.
Prove that $x^p - x + 1$ is irreducible in $\mathbb{F}_p[x]$.
:::

::: {.solution}
Put $f(x)=x^p-x+1$ and choose a root $\alpha$ in an algebraic closure of $\mathbb{F}_p$.
Let $h\in\mathbb{F}_p[x]$ be the monic minimal polynomial of $\alpha$.

<1>1. For every integer $r\ge0$,
\[
\alpha^{p^r}=\alpha-r,
\]
where the integer $r$ on the right denotes its image in $\mathbb{F}_p$.
::: {.proof}
The identity holds for $r=0$.
Since $f(\alpha)=0$, we have $\alpha^p=\alpha-1$.
If the formula holds for $r$, then the characteristic-$p$ binomial theorem and $r^p=r$ in the prime field give
\[
\alpha^{p^{r+1}}=(\alpha-r)^p=\alpha^p-r^p
=\alpha-1-r=\alpha-(r+1).
\]
Induction proves the formula.
:::

<1>2. The polynomial $h$ has at least $p$ distinct roots.
::: {.proof}
For a polynomial with coefficients in $\mathbb{F}_p$, the Frobenius map satisfies
\[
h(z^p)=h(z)^p.
\]
Indeed, raising the sum defining $h(z)$ to the $p$th power raises each monomial to that power and fixes every coefficient.
Iterating and using $h(\alpha)=0$ shows that $h(\alpha^{p^r})=0$ for every $r\ge0$.
By <1>1, the elements
\[
\alpha,\alpha-1,\ldots,\alpha-(p-1)
\]
are therefore roots of $h$.
They are distinct: equality of the $r$th and $s$th terms would give $r-s=0$ in $\mathbb{F}_p$, which for $0\le r,s<p$ forces $r=s$.
Consequently $\deg h\ge p$.
:::

<1>3. The polynomial $f$ equals $h$ and is irreducible.
::: {.proof}
The defining property of the minimal polynomial gives $h\mid f$, because $f(\alpha)=0$.
Thus $\deg h\le\deg f=p$.
Together with <1>2 this yields $\deg h=p$.
The monic polynomials $h$ and $f$ have the same degree and $h\mid f$, so $h=f$.
The minimal polynomial $h$ is irreducible, which proves the claim.
:::
:::
