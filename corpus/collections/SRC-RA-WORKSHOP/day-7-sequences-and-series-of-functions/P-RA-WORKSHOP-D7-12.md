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
(January 2006 #7a) Let $f$ be continuous on $[0,1]$ and $f(0)=f(1)=0$.
Show that there is a sequence of polynomials $\{P_n\}$ such that $x(1-x)P_n(x)$ converges to $f$ uniformly.
:::

::: {.solution}
For each integer $n\geq1$, define the Bernstein polynomial
\[
B_nf(x):=\sum_{k=0}^n f(k/n)\binom nk x^k(1-x)^{n-k}.
\]

::: pf

::: {.pf-step #s1}

The polynomials $B_nf$ converge uniformly to $f$ on $[0,1]$.

::: pf-proof

The Bernstein approximation theorem states that the Bernstein polynomials of every continuous function on $[0,1]$ converge uniformly to that function. Apply it to $f$.

:::

:::

::: {.pf-step #s2}

Each polynomial $B_nf$ vanishes at $0$ and $1$.

::: pf-proof

At $x=0$ only the $k=0$ term in the defining sum survives, giving $B_nf(0)=f(0)=0$. At $x=1$ only the $k=n$ term survives, giving $B_nf(1)=f(1)=0$.

:::

:::

::: {.pf-step #s3}

Every polynomial $p\in\mathbb R[x]$ satisfying $p(0)=p(1)=0$ admits a factorization $p(x)=x(1-x)q(x)$ with $q\in\mathbb R[x]$.

::: pf-proof

The factor theorem applied at zero gives $p(x)=xr(x)$ for a polynomial $r$. Evaluating at one gives $r(1)=p(1)=0$, so the factor theorem at one gives $r(x)=(1-x)q(x)$ for a polynomial $q$ (absorbing the minus sign into $q$). Substitution gives the asserted factorization.

:::

:::

::: {.pf-step #s4}

There exist polynomials $\boxed{P_n\in\mathbb R[x]}$ such that $x(1-x)P_n(x)\to f(x)$ uniformly on $[0,1]$.

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, choose $P_n$ satisfying $B_nf(x)=x(1-x)P_n(x)$ for each $n\geq1$. Step [](#s1){.pf-ref} gives
\[
\sup_{x\in[0,1]}|x(1-x)P_n(x)-f(x)|
=\|B_nf-f\|_\infty\longrightarrow0.
\]

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} constructs the required sequence and proves its uniform convergence.

:::

:::

:::
