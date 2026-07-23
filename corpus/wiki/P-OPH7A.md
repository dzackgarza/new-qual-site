---
schema: qual/card@1
id: P-OPH7A
kind: problem
title: "Let $f, g: [a, b] \\to \\RR$ be measurable with"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $f, g: [a, b] \to \RR$ be measurable with
$$
\int_{a}^{b} f(x) ~d x=\int_{a}^{b} g(x) ~d x.
$$
Show that either

1. $f(x) = g(x)$ almost everywhere, or
2. There exists a measurable set $E \subset [a, b]$ such that
\[
\int _{E} f(x) \, dx > \int _{E} g(x) \, dx
\]

:::{.concept}
\envlist
- Monotonicity of the Lebesgue integral: $f\leq g$ on $A$ $\implies \int_A f \leq \int_A g$

:::

:::{.strategy}
Take the assumption and the negation of (1) and show (2).
The obvious move: define the set $A$ where they differ.
The non-obvious move: split $A$ itself up to get a strict inequality.

:::

:::{.solution}
\envlist

- Write $X\da [a, b]$,
- Suppose it is *not* the case that $f=g$ almost everywhere; then letting $A\definedas \theset{x\in X \suchthat f(x) \neq g(x)}$, we have $m(A) > 0$.
- Write 
  \[
  A = A_1 \disjoint A_2 \da \ts{f > g} \disjoint \ts{f < g}
  .\]
- Both $A_i$ are measurable:
  - Since $f,g$ are measurable functions, so is $h\da f-g$.
  - We can write
  \[
  A_1 &\da \ts{ x\in X \st h > 0 } = h\inv((0, \infty)) \\
  A_2 &\da \ts{ x\in X \st h < 0 } = h\inv((-\infty, 0))
  ,\]
  and pullbacks of Borel sets by measurable functions are measurable.



- Then on $E$, we have $f(x)>g(x)$ pointwise. 
  This is preserved by monotonicity of the integral, thus
  \[  
  f(x) > g(x) \text{ on } E \implies \int_{E} f(x)\,dx > \int_{E} g(x)\, dx 
  .\] 
:::

