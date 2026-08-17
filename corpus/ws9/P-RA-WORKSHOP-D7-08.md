---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-08
kind: problem
title: 'The integral limit of $f(x^n)$'
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2005 #4, June 2010 #6b) If $f:[0,1]\to\mathbb R$ is continuous, prove that $$\lim_{n\to\infty}\int_0^1f(x^n)\,dx=f(0).$$
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove $\lim_{n\to\infty}\int_0^1 f(x^n)\,dx = f(0)$ for continuous $f: [0,1] \to \mathbb R$.

<1>1. $f(x^n) \to f(0)$ pointwise on $[0,1)$ and equals $f(1)$ at $x = 1$.
Proof: for $x \in [0,1)$, $x^n \to 0$ and $f$ is continuous at $0$; at $x=1$, $f(x^n) = f(1)$ for all $n$.

<1>2. The integrands are uniformly bounded.
Proof: $f$ is continuous on the compact interval $[0,1]$, hence bounded: $|f| \le M$ for some $M$.
Then $|f(x^n)| \le M$ for all $n$ and all $x$.

<1>3. $\int_0^1 f(x^n)\,dx \to \int_0^1 f(0)\,dx = f(0)$.
Proof: Dominated Convergence Theorem: pointwise convergence by <1>1 (the single point $x = 1$ has measure zero, so the value $f(1)$ there is irrelevant) and the domination $|f(x^n)| \le M$ of <1>2 with the constant function $M$ integrable on $[0,1]$.

<1>4. Q.E.D. Proof: <1>3 is exactly the claim.
:::
