---
schema: qual/card@1
id: P-7GK3C
kind: problem
title: Rouché's theorem and $\max_{|z|=1}|P(z)|\ge 1$ for a monic polynomial $P$
classification:
  areas:
  - complex-analysis
  topics:
  - maximum-modulus-principle
  - rouche
  - polynomials
relations: []
review: draft
solved: true
---

::: problem
Prove that
\[
\max_{\abs z = 1} \abs{a_0 + a_1 z + \cdots + a_{n-1}z^{n-1} + z^n} \geq 1
.\]

> Hint: the first part of the problem asks for a statement of Rouche's theorem.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that for any monic polynomial $P(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$ of degree $n \geq 1$, one has $\max_{\abs z = 1} \abs{P(z)} \geq 1$.

<1>1. State Rouch\'e's theorem.
    Proof: If $f, g$ are holomorphic on a domain containing a simple closed contour $\gamma$, and $\abs{g(z)} < \abs{f(z)}$ for all $z \in \gamma$, then $f$ and $f + g$ have the same number of zeros (counting multiplicity) inside $\gamma$.

<1>2. Assume for contradiction that $\max_{\abs z = 1} \abs{P(z)} < 1$.
    Proof: Suppose the claimed inequality fails, so $\abs{P(z)} < 1$ for every $z$ on the unit circle.

<1>3. Define $Q(z) \definedas z^n P\qty(\frac{1}{z}) = 1 + a_{n-1}z + \cdots + a_0 z^n$.
    <2>1. $Q$ is a polynomial, hence entire.
        Proof: Since $P$ is monic of degree $n$, the substitution $z \mapsto 1/z$ clears denominators: $z^n P(1/z) = z^n\qty(z^{-n} + a_{n-1} z^{-(n-1)} + \cdots + a_0) = 1 + a_{n-1}z + \cdots + a_0 z^n$.
    <2>2. $Q(0) = 1$.
        Proof: Evaluate $Q$ at $z = 0$: only the constant term survives.
    <2>3. For $\abs z = 1$, $\abs{Q(z)} = \abs{P(1/z)} = \abs{P(z)} < 1$.
        Proof: On the unit circle $\abs z^n = 1$, so $\abs{Q(z)} = \abs{P(1/z)}$; since $\abs{1/z} = 1$, step <1>2 gives the strict inequality.

<1>4. Apply Rouch\'e's theorem on $\abs z = 1$ to $f(z) \equiv -1$ and $g(z) = Q(z)$.
    <2>1. $\abs{g(z)} < \abs{f(z)} = 1$ on the circle.
        Proof: <1>3.3 gives $\abs{Q(z)} < 1$ for $\abs z = 1$.
    <2>2. Hence $f + g = Q - 1$ has the same number of zeros in $\abs z < 1$ as the constant function $-1$, namely none.
        Proof: Rouch\'e's theorem, <1>1, applied to $f \equiv -1$ and $g = Q$.

<1>5. $Q - 1$ has a zero in $\abs z < 1$.
    Proof: $Q(0) - 1 = 0$ by <1>3.2, and $z = 0$ lies in the unit disk.

<1>6. Q.E.D.
    Proof: Steps <1>4 and <1>5 contradict each other, so the assumption <1>2 is false; hence $\max_{\abs z = 1} \abs{P(z)} \geq 1$.

:::
