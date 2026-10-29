---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-12
kind: problem
title: Polynomial approximation with endpoint factors
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Uniform Convergence
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $f$ be continuous on $[0,1]$ and $f(0)=f(1)=0$.
Show that there is a sequence of polynomials $\{P_n\}$ such that $x(1-x)P_n(x)$ converges to $f$ uniformly.
:::

::: {.solution}
For each integer $n\geq1$, define the Bernstein polynomial
$$
B_nf(x)\coloneqq\sum_{k=0}^n f(k/n)\binom nk x^k(1-x)^{n-k}.
$$

::: pf

::: {.pf-step #s1}

The polynomials $B_nf$ converge uniformly to $f$ on $[0,1]$.

::: pf-proof

The Bernstein approximation theorem states that the Bernstein polynomials of every continuous function on $[0,1]$ converge uniformly to that function.

:::

:::

::: {.pf-step #s2}

Each polynomial $B_nf$ vanishes at $0$ and $1$.

::: pf-proof

At $x=0$ only the $k=0$ term in the defining sum survives, giving $B_nf(0)=f(0)=0$. At $x=1$ only the $k=n$ term survives, giving $B_nf(1)=f(1)=0$.

:::

:::

::: {.pf-step #s3}

Every polynomial $p\in\RR[x]$ satisfying $p(0)=p(1)=0$ admits a factorization $p(x)=x(1-x)q(x)$ with $q\in\RR[x]$.

::: pf-proof

The factor theorem applied at zero gives $p(x)=xr(x)$ for a polynomial $r$. Evaluating at one gives $r(1)=p(1)=0$, so the factor theorem at one gives $r(x)=(1-x)q(x)$ for a polynomial $q$ (absorbing the minus sign into $q$). Substitution gives the asserted factorization.

:::

:::

::: pf-step

There exist polynomials $P_n\in\RR[x]$ such that $x(1-x)P_n(x)\to f(x)$ uniformly on $[0,1]$.

::: pf-proof

By step [](#s2){.pf-ref} and step [](#s3){.pf-ref}, there are polynomials $P_n$ with $B_nf(x)=x(1-x)P_n(x)$ for each $n\geq1$. Step [](#s1){.pf-ref} gives
$$
\sup_{x\in[0,1]}\abs{x(1-x)P_n(x)-f(x)}
=\norm{B_nf-f}_\infty\longrightarrow0.
$$

:::

:::

:::

:::
