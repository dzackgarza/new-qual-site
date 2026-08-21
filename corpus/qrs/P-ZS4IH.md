---
schema: qual/card@1
id: P-ZS4IH
kind: problem
title: A bound on the difference quotient of a holomorphic function on a half-radius
  disc
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Schwarz Lemma
relations: []
review: draft
solved: true
---

::: problem
Let $\bar B(a, r)$ denote the closed disc of radius $r$ about $a\in \CC$.
Let $f$ be holomorphic on an open set containing $\bar B(a, r)$ and let 
\[  
M \definedas \sup_{z\in \bar B(a, r)} \abs{f(z)}
.\]

Prove that 
\[  
z\in \bar B\qty{a, {r\over 2}},\,z\neq a, \qquad {\abs{ f(z) - f(a)} \over \abs{z-a}} \leq {2M \over r}
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $\bar B(a, r)$ be the closed disk of radius $r$ about $a$, and let $f$ be holomorphic on an open set containing it, with $M := \sup_{z \in \bar B(a,r)} \abs{f(z)}$. Prove that for $z \in \bar B\qty{a, \frac{r}{2}}$, $z \neq a$:
$$\frac{\abs{f(z) - f(a)}}{\abs{z - a}} \leq \frac{2M}{r}.$$

<1>1. Reduce to the unit disk by scaling: define $g(w) := f(a + rw)$ for $\abs w \leq 1$.
    Proof: $g$ is holomorphic on a neighborhood of the closed unit disk, and $\abs{g(w)} \leq M$ there.

<1>2. Define $h(w) := g(w) - g(0)$; then $h(0) = 0$ and $\abs{h(w)} \leq 2M$ on $\abs w \leq 1$.
    Proof: $\abs{h(w)} = \abs{g(w) - g(0)} \leq \abs{g(w)} + \abs{g(0)} \leq 2M$.

<1>3. Apply Schwarz's lemma to $\frac{h}{2M}$.
    <2>1. $\frac{h}{2M}$ is holomorphic on $\DD$ and maps $\DD$ into $\overline{\DD}$, with value $0$ at $w = 0$.
        Proof: <1>2; if $M = 0$ then $f \equiv 0$ and the result is trivial, so assume $M > 0$.
    <2>2. $\abs{h(w)} \leq 2M \abs w$ for $\abs w < 1$.
        Proof: Schwarz's lemma applied to $h/2M$.

<1>4. Translate back to $z$.
    <2>1. For $z \in \bar B(a, r/2)$, set $w := (z - a)/r$; then $\abs w \leq 1/2 < 1$.
        Proof: $\abs{z - a} \leq r/2$.
    <2>2. $\abs{f(z) - f(a)} = \abs{h(w)} \leq 2M\abs w = \frac{2M}{r}\abs{z - a}$.
        Proof: <1>1, <1>2 and <1>3.2, with $f(z) - f(a) = g(w) - g(0) = h(w)$.

<1>5. Q.E.D.
    Proof: <1>4.2 is exactly the claimed inequality (both sides well-defined since $z \neq a$).

:::
