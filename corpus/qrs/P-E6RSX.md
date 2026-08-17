---
schema: qual/card@1
id: P-E6RSX
kind: problem
title: "Find the number of roots of $z^4 - 6z + 3 =0$ in $|z|<1$ and $1 < |z| < 2$ respectively."
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
relations: []
review: draft
---

::: problem
Find the number of roots of $z^4 - 6z + 3 =0$ in $|z|<1$ and $1 < |z| < 2$ respectively.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Find the number of roots of $z^4 - 6z + 3 = 0$ in $\abs z < 1$ and in $1 < \abs z < 2$.

<1>1. On $\abs z = 1$: $\abs{z^4} = 1$ and $\abs{-6z + 3} \geq \abs{-6z} - \abs{3} = 6 - 3 = 3$.
    Proof: Reverse triangle inequality.

<1>2. $z^4 - 6z + 3$ has exactly one zero in $\abs z < 1$.
    <2>1. On $\abs z = 1$, $\abs{z^4} < \abs{-6z + 3}$.
        Proof: <1>1: $1 < 3$.
    <2>2. $z^4 - 6z + 3$ and $-6z + 3$ have the same number of zeros in $\abs z < 1$.
        Proof: Rouch\'e's theorem with $f(z) = -6z + 3$ and $g(z) = z^4$, using <2>1.
    <2>3. $-6z + 3$ has exactly one zero in $\abs z < 1$.
        Proof: Its only zero is $z = 1/2$, and $\abs{1/2} < 1$.
    <2>4. Conclusion.
        Proof: <2>2 and <2>3.

<1>3. On $\abs z = 2$: $\abs{z^4} = 16$ and $\abs{-6z + 3} \leq 6\abs z + 3 = 15$.
    Proof: Triangle inequality.

<1>4. $z^4 - 6z + 3$ has exactly four zeros in $\abs z < 2$.
    <2>1. On $\abs z = 2$, $\abs{-6z + 3} < \abs{z^4}$.
        Proof: <1>3: $15 < 16$.
    <2>2. $z^4 - 6z + 3$ and $z^4$ have the same number of zeros in $\abs z < 2$.
        Proof: Rouch\'e's theorem with $f(z) = z^4$ and $g(z) = -6z + 3$, using <2>1.
    <2>3. $z^4$ has exactly four zeros in $\abs z < 2$.
        Proof: $z = 0$ is a zero of multiplicity 4.
    <2>4. Conclusion.
        Proof: <2>2 and <2>3.

<1>5. The number of zeros in $1 < \abs z < 2$ is $4 - 1 = 3$.
    <2>1. There are no zeros on the circle $\abs z = 1$.
        Proof: On $\abs z = 1$, $\abs{z^4} = 1$ while $\abs{6z - 3} \geq 3$, so $z^4 = 6z - 3$ is impossible; the polynomial vanishes only where $z^4 = 6z - 3$.
    <2>2. All four zeros in $\abs z < 2$ (<1>4) lie in $\abs z < 1$ or in the annulus $1 < \abs z < 2$.
        Proof: <2>1 rules out the circle $\abs z = 1$ itself.
    <2>3. Exactly one zero lies in $\abs z < 1$ (<1>2), so exactly $4 - 1 = 3$ lie in $1 < \abs z < 2$.
        Proof: <2>2 and <1>2.

<1>6. Q.E.D.
    Proof: <1>2 gives one root in $\abs z < 1$; <1>5 gives three roots in $1 < \abs z < 2$.

:::
