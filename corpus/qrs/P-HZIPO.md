---
schema: qual/card@1
id: P-HZIPO
kind: problem
title: Schwarz–Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Suppose $f:\DD\to \DD$ is analytic.
Prove that 
\[  
\forall a\in \DD, \qquad {\abs{f'(a)} \over 1 - \abs{f(a)}^2 } \leq {1 \over 1 - \abs{a}^2}
.\]
:::

::: {.solution}
**Goal:** Prove the Schwarz--Pick inequality: if $f: \DD \to \DD$ is analytic, then for every $a \in \DD$,
$$\frac{\abs{f'(a)}}{1 - \abs{f(a)}^2} \leq \frac{1}{1 - \abs a^2}.$$

<1>1. Recall the automorphism $\phi_a(z) := \frac{z - a}{1 - \bar a z}$ of $\DD$, which maps $a$ to $0$.
    Proof: $\phi_a$ is a M\"obius map taking $\DD$ onto $\DD$ (its pole $1/\bar a$ lies outside the unit disk) and $\phi_a(a) = 0$; its inverse is $\phi_a^{-1}(w) = \frac{w + a}{1 + \bar a w}$.

<1>2. Define $F := \phi_{f(a)} \circ f \circ \phi_a^{-1}$; then $F: \DD \to \DD$ is analytic and $F(0) = 0$.
    Proof: $\phi_{f(a)}(f(\phi_a^{-1}(0))) = \phi_{f(a)}(f(a)) = 0$, using $\phi_a^{-1}(0) = a$.

<1>3. By Schwarz's lemma, $\abs{F'(0)} \leq 1$.
    Proof: Schwarz lemma applies to the analytic map $F: \DD \to \DD$ with $F(0) = 0$.

<1>4. Compute $F'(0)$ by the chain rule.
    <2>1. $F'(0) = \phi_{f(a)}'(f(a)) \cdot f'(a) \cdot (\phi_a^{-1})'(0)$.
        Proof: Chain rule for the composition $\phi_{f(a)} \circ f \circ \phi_a^{-1}$.
    <2>2. $\phi_w'(z) = \frac{1 - \abs w^2}{(1 - \bar w z)^2}$, so $\phi_{f(a)}'(f(a)) = \frac{1}{1 - \abs{f(a)}^2}$.
        Proof: Differentiate $\phi_w$; at $z = w$ the denominator is $1 - \abs w^2$.
    <2>3. $(\phi_a^{-1})'(0) = 1 - \abs a^2$.
        Proof: $\phi_a^{-1}(w) = \frac{w + a}{1 + \bar a w}$; differentiate and evaluate at $w = 0$: $\frac{1 \cdot 1 - (0 + a)\bar a}{1^2} = 1 - \abs a^2$.
    <2>4. Hence $F'(0) = f'(a) \cdot \frac{1 - \abs a^2}{1 - \abs{f(a)}^2}$.
        Proof: <2>1--<2>3.

<1>5. Combine with Schwarz's lemma.
    <2>1. $\abs{f'(a)} \cdot \frac{1 - \abs a^2}{1 - \abs{f(a)}^2} \leq 1$.
        Proof: <1>3 and <1>4.4.
    <2>2. Divide by the positive quantity $1 - \abs a^2$.
        Proof: $\abs a < 1$, so $1 - \abs a^2 > 0$.

<1>6. Q.E.D.
    Proof: <1>5 gives $\frac{\abs{f'(a)}}{1 - \abs{f(a)}^2} \leq \frac{1}{1 - \abs a^2}$.

:::
