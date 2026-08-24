---
schema: qual/card@1
id: P-OASVA
kind: problem
title: Entire functions with a pole at $\infty$ are the nonconstant polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Singularities
relations: []
review: draft
---

::: problem
Find all entire functions with have poles at $\infty$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Find all entire functions $f$ such that $f$ has a pole at $\infty$.

<1>1. A pole at $\infty$ means $g(w) \definedas f(1/w)$ has a pole at $w = 0$.
Proof: This is the definition of the singularity at $\infty$: $f$ has a pole at $\infty$ iff $f(1/w)$ has a pole at $0$.

<1>2. If $f$ is entire with a pole at $\infty$, then $f$ is a nonconstant polynomial.
Proof: By <1>1, $g(w) = f(1/w)$ has a pole at $w=0$, so its Laurent expansion about $0$ has only finitely many negative terms: $g(w) = \sum_{n=-N}^{\infty} b_n w^n$ with $b_{-N} \neq 0$.
Substituting $w = 1/z$ gives $f(z) = \sum_{n=-N}^{\infty} b_n z^{-n} = \sum_{k=-\infty}^{N} b_{-k} z^k$; since $f$ is entire (no poles in $\CC$), all coefficients of negative powers vanish and $f(z) = \sum_{k=0}^{N} a_k z^k$ is a polynomial, nonconstant because the pole at $\infty$ has positive order ($N \geq 1$).

<1>3. Conversely, every nonconstant polynomial has a pole at $\infty$.
Proof: If $f(z) = a_N z^N + \cdots + a_0$ with $N \geq 1$ and $a_N \neq 0$, then $f(1/w) = a_N w^{-N} + \cdots + a_0$ has a pole of order $N$ at $w = 0$, so $f$ has a pole of order $N$ at $\infty$ by <1>1.

<1>4. Q.E.D. Proof: <1>2 and <1>3 together show the entire functions with a pole at $\infty$ are exactly the nonconstant polynomials.
:::
