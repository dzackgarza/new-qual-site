---
schema: qual/card@1
id: E-MH2FB
kind: problem
title: Continuity of x times y inverse characterizes topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Let $H$ denote a group that is also a topological space satisfying the $T_1$ axiom.
Show that $H$ is a topological group if and only if the map of $H \times H$ into $H$ sending $x \times y$ into $x \cdot y^{-1}$ is continuous.
:::

::: solution
**Goal:** Prove that a $T_1$ group $H$ is a topological group if and only if the division map $\phi: H \times H \to H$ given by $\phi(x, y) = x \cdot y^{-1}$ is continuous.

<1>1. Definition of a topological group:
    *Proof:*
    <2>1. A group $H$ equipped with a topology satisfying the $T_1$ axiom is a topological group if:
        1. The multiplication map $\mu: H \times H \to H$, $\mu(x, y) = x \cdot y$, is continuous.
        2. The inversion map $\iota: H \to H$, $\iota(x) = x^{-1}$, is continuous.

<1>2. Forward direction: $H$ is a topological group $\implies \phi(x, y) = x y^{-1}$ is continuous.
    *Proof:*
    <2>1. Assume $\mu$ and $\iota$ are continuous.
    <2>2. Define the helper map $f: H \times H \to H \times H$ by $f(x, y) = (\operatorname{id}_H(x), \iota(y)) = (x, y^{-1})$.
    <2>3. By the universal property of the product topology, $f$ is continuous because its component coordinate functions $\pi_1 \circ f = \operatorname{id}_H$ and $\pi_2 \circ f = \iota \circ \pi_2$ are continuous.
    <2>4. The division map $\phi(x, y) = x y^{-1}$ is the composition $\phi = \mu \circ f$:
    $$\phi(x, y) = \mu(f(x, y)) = \mu(x, y^{-1}) = x y^{-1}.$$
    <2>5. As the composition of continuous functions, $\phi$ is continuous.

<1>3. Backward direction: $\phi(x, y) = x y^{-1}$ is continuous $\implies H$ is a topological group.
    *Proof:*
    <2>1. Assume $\phi: H \times H \to H$ is continuous.
    <2>2. Continuity of inversion $\iota$: Let $e \in H$ be the identity element. Define the embedding $j: H \to H \times H$ by $j(x) = (e, x)$.
    <2>3. The map $j$ is continuous because its coordinate projections are the constant map $x \mapsto e$ and the identity map $x \mapsto x$.
    <2>4. The inversion map is the composite $\iota = \phi \circ j$, because
    $$\phi(j(x)) = \phi(e, x) = e \cdot x^{-1} = x^{-1} = \iota(x).$$
    Therefore $\iota: H \to H$ is continuous.
    <2>5. Continuity of multiplication $\mu$: Define $g: H \times H \to H \times H$ by $g(x, y) = (x, \iota(y)) = (x, y^{-1})$.
    <2>6. Since $\iota$ is continuous by step 2.4, $g$ is continuous.
    <2>7. The multiplication map is the composite $\mu = \phi \circ g$, because
    $$\phi(g(x, y)) = \phi(x, y^{-1}) = x \cdot (y^{-1})^{-1} = x \cdot y = \mu(x, y).$$
    Therefore $\mu: H \times H \to H$ is continuous.
    <2>8. Since both $\mu$ and $\iota$ are continuous, $H$ is a topological group.

<1>4. Conclusion:
    *Proof:*
    By <1>2 and <1>3, $H$ is a topological group if and only if $\phi(x, y) = x y^{-1}$ is continuous.
:::
