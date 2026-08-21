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
solved: true
---

::: {.problem title="?"}
(January 2006 #7a) Let $f$ be continuous on $[0,1]$ and $f(0)=f(1)=0$.
Show that there is a sequence of polynomials $\{P_n\}$ such that $x(1-x)P_n(x)$ converges to $f$ uniformly.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Given $f \in C[0,1]$ with $f(0) = f(1) = 0$, find polynomials $P_n$ with $x(1-x)P_n(x) \to f(x)$ uniformly on $[0,1]$.

<1>1. The Bernstein polynomials $B_N f$ converge to $f$ uniformly on $[0,1]$.
Proof: the Weierstrass approximation theorem via Bernstein polynomials: $B_Nf(x) = \sum_{k=0}^N f(k/N)\binom{N}{k}x^k(1-x)^{N-k} \to f(x)$ uniformly.

<1>2. $B_Nf$ vanishes at both endpoints: $B_Nf(0) = f(0) = 0$ and $B_Nf(1) = f(1) = 0$.
Proof: in the sum, at $x = 0$ only the $k = 0$ term survives and equals $f(0)$; at $x = 1$ only the $k = N$ term survives and equals $f(1)$.
Both are $0$ by hypothesis.

<1>3. Every polynomial $p$ with $p(0) = p(1) = 0$ is divisible by $x(1-x)$: $p(x) = x(1-x)q(x)$ for a polynomial $q$.
Proof: $p(0) = 0$ means the constant term of $p$ is $0$, so $p(x) = x\tilde p(x)$; $p(1) = 0$ means $\tilde p(1) = 0$, so $\tilde p(x) = (1-x)q(x)$.
Since $x$ and $1-x$ are coprime, $p = x(1-x)q$.

<1>4. Apply <1>3 to $p = B_Nf$: there are polynomials $q_N$ with $B_Nf(x) = x(1-x)q_N(x)$ for all $x$.
Proof: <1>2 gives the two endpoint zeros; <1>3 then gives the factorization.

<1>5. Q.E.D. Proof: by <1>1, $x(1-x)q_N(x) = B_Nf(x) \to f(x)$ uniformly; take $P_N := q_N$.
:::
