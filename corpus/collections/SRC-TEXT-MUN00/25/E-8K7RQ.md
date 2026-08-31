---
schema: qual/card@1
id: E-8K7RQ
kind: exercise
title: Components and continuous maps out of the lower limit line
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

What are the components and path components of $\mathbb{R}_\ell$?
What are the continuous maps $f: \mathbb{R} \to \mathbb{R}_\ell$?
:::

::: solution
**Goal:** Determine the connected components and path components of the lower limit line $\mathbb{R}_\ell$, and classify all continuous maps $f: \mathbb{R} \to \mathbb{R}_\ell$ from the standard real line.

<1>1. Components and path components of $\mathbb{R}_\ell$:
    The connected components and path components of $\mathbb{R}_\ell$ are the singletons $\{x\}$ for each $x \in \mathbb{R}$ (i.e. $\mathbb{R}_\ell$ is totally disconnected).
    *Proof:*
    <2>1. For any $a \in \mathbb{R}$, the rays $(-\infty, a) = \bigcup_{n=1}^\infty [a-n, a)$ and $[a, \infty) = \bigcup_{n=0}^\infty [a+n, a+n+1)$ are unions of basic open sets in $\mathbb{R}_\ell$, hence open in $\mathbb{R}_\ell$.
    <2>2. Consequently, each ray is also closed in $\mathbb{R}_\ell$, being the complement of the other.
    <2>3. Let $x, y \in \mathbb{R}_\ell$ with $x < y$. Choosing $a \in (x, y)$ gives a separation of $\mathbb{R}_\ell$ into disjoint open sets:
        $$\mathbb{R}_\ell = (-\infty, a) \cup [a, \infty),$$
        with $x \in (-\infty, a)$ and $y \in [a, \infty)$.
    <2>4. Thus no two distinct points can lie in the same connected subset of $\mathbb{R}_\ell$.
    <2>5. Therefore, the connected components of $\mathbb{R}_\ell$ are the one-point sets $\{x\}$.
    <2>6. Since every path component is contained in a connected component, the path components of $\mathbb{R}_\ell$ are also the singletons $\{x\}$.

<1>2. Continuous maps $f: \mathbb{R} \to \mathbb{R}_\ell$:
    The continuous maps $f: \mathbb{R} \to \mathbb{R}_\ell$ are precisely the constant maps.
    *Proof:*
    <2>1. The real line $\mathbb{R}$ with the standard Euclidean topology is connected.
    <2>2. The continuous image of a connected space is connected, so $f(\mathbb{R})$ must be a connected subset of $\mathbb{R}_\ell$.
    <2>3. By <1>1, the only non-empty connected subsets of $\mathbb{R}_\ell$ are singletons.
    <2>4. Hence $f(\mathbb{R}) = \{c\}$ for some $c \in \mathbb{R}$, which means $f(x) = c$ for all $x \in \mathbb{R}$.
    <2>5. Conversely, every constant map is continuous (the preimage of any open set is either $\emptyset$ or the whole space).

<1>3. Conclusion:
    The components and path components of $\mathbb{R}_\ell$ are the singletons $\{x\}$, and the continuous maps $\mathbb{R} \to \mathbb{R}_\ell$ are the constant maps. Q.E.D.
:::
