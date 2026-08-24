---
schema: qual/card@1
id: P-DAI2Z
kind: problem
title: Number of solutions of $e^z=az^n$ in the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

::: problem
Let $n\in \ZZ^{\geq 0}$ and show that the equation
\[
e^z = az^n
\]
has $n$ solutions in the open unit disc if $\abs{a} > e$, and no solutions if $\abs{a} < {1\over e}$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that $e^z = az^n$ has exactly $n$ solutions in the open unit disk when $\abs a > e$, and no solutions when $\abs a < \frac{1}{e}$.

<1>1. On $\abs z = 1$: $\abs{e^z} = e^{\Re z} \leq e^{\abs z} = e$.
Proof: $\Re z \leq \abs z = 1$ on the unit circle.

<1>2. Case $\abs a > e$: $e^z - az^n$ has exactly $n$ zeros in $\abs z < 1$.
<2>1. On $\abs z = 1$, $\abs{e^z} < \abs{az^n} = \abs a$.
Proof: <1>1 and $\abs a > e$; also $\abs{z^n} = 1$.
<2>2. $e^z - az^n$ and $-az^n$ have the same number of zeros in $\abs z < 1$.
Proof: Rouch\'e's theorem with $f(z) = -az^n$ and $g(z) = e^z$, using <2>1. <2>3. $-az^n$ has exactly $n$ zeros in $\abs z < 1$ (counting multiplicity).
Proof: Its only zero is $z = 0$, of multiplicity $n$ (for $n \geq 1$; for $n = 0$, $-a \neq 0$ has no zeros, and "$n = 0$ solutions" is consistent).
<2>4. Conclusion.
Proof: <2>2 and <2>3.

<1>3. On $\abs z = 1$: $\abs{e^z} = e^{\Re z} \geq e^{-1} = \frac{1}{e}$.
Proof: $\Re z \geq -\abs z = -1$ on the unit circle.

<1>4. Case $\abs a < \frac{1}{e}$: $e^z - az^n$ has no zeros in $\abs z < 1$.
<2>1. On $\abs z = 1$, $\abs{az^n} = \abs a < \frac{1}{e} \leq \abs{e^z}$.
Proof: <1>3 and the hypothesis on $\abs a$.
<2>2. $e^z - az^n$ and $e^z$ have the same number of zeros in $\abs z < 1$.
Proof: Rouch\'e's theorem with $f(z) = e^z$ and $g(z) = -az^n$, using <2>1. <2>3. $e^z$ has no zeros.
Proof: The exponential never vanishes.
<2>4. Conclusion.
Proof: <2>2 and <2>3.

<1>5. Q.E.D. Proof: <1>2 gives exactly $n$ solutions in the disk when $\abs a > e$; <1>4 gives none when $\abs a < 1/e$.
:::
