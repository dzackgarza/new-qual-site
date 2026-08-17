---
schema: qual/card@1
id: P-5U7QZ
kind: problem
title: A sharp bound on $|f'(0)|$ for analytic maps $\mathbb{D}\to\mathbb{H}$ with $f(0)=2$
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
  - conformal-maps
  - fractional-linear-transformations
relations: []
review: draft
solved: true
---

::: problem
Suppose $f: \DD\to \HH$ is analytic and satisfies $f(0) = 2$.
Find a sharp upper bound for $\abs{f'(0)}$, and prove it is sharp by example.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Suppose $f: \DD \to \HH$ is analytic with $f(0) = 2$, where $\HH$ is the upper half-plane.
Find a sharp upper bound for $|f'(0)|$ and prove sharpness by example.

<1>1. Reduce to a self-map of the disk fixing $0$.
<2>1. Define $g: \HH \to \HH$ by $g(z) = \tfrac{i}{2} z$, so $g(2) = i$.
Proof: $g(2) = i$ and $g$ maps $\HH$ into $\HH$ (multiplication by $i/2$ rotates by $90^\circ$ and scales, preserving the upper half-plane).
<2>2. Let $C: \HH \to \DD$, $C(z) = \frac{z - i}{z + i}$ be the Cayley map (with $C(i) = 0$), and set $F = C \circ g \circ f: \DD \to \DD$.
Proof: $f(\DD) \subseteq \HH$, $g(\HH) \subseteq \HH$, $C(\HH) = \DD$; and $F(0) = C(g(f(0))) = C(g(2)) = C(i) = 0$.

<1>2. $|F'(0)| \le 1$.
Proof: Schwarz's lemma applies to $F$ (holomorphic self-map of $\DD$ with $F(0) = 0$).

<1>3. Express $F'(0)$ in terms of $f'(0)$: $|F'(0)| = |C'(i)|\,|g'(2)|\,|f'(0)| = \tfrac14 |f'(0)|$.
Proof: chain rule $F'(0) = C'(g(f(0)))\,g'(f(0))\,f'(0) = C'(i)\,g'(2)\,f'(0)$; compute $C'(z) = \frac{2i}{(z+i)^2}$, so $|C'(i)| = \frac{|2i|}{|2i|^2} = \tfrac12$; and $g'(z) = \tfrac{i}{2}$, so $|g'(2)| = \tfrac12$.

<1>4. $|f'(0)| \le 4$.
Proof: <1>2 and <1>3: $\tfrac14|f'(0)| = |F'(0)| \le 1$.

<1>5. Sharpness: the bound is attained.
<2>1. Take $F(z) = \lambda z$ with $|\lambda| = 1$; then $f = g^{-1} \circ C^{-1} \circ F$ satisfies all hypotheses.
Proof: $f(\DD) \subseteq \HH$ (composite of maps into $\HH$) and $f(0) = g^{-1}(C^{-1}(0)) = g^{-1}(i) = 2$; $F$ attains Schwarz equality so $|F'(0)| = 1$.
<2>2. Explicitly $f(z) = -2\,\frac{\lambda z + 1}{\lambda z - 1}$ and $|f'(0)| = 4$.
Proof: $C^{-1}(w) = -i\frac{w+1}{w-1}$, $g^{-1}(w) = -2iw$, so $f(z) = -2i\cdot\qty{-i\frac{\lambda z+1}{\lambda z - 1}} = -2\frac{\lambda z + 1}{\lambda z - 1}$; differentiating, $f'(z) = \frac{4\lambda}{(\lambda z - 1)^2}$, so $|f'(0)| = 4|\lambda| = 4$.

<1>6. Q.E.D. Proof: <1>1–<1>4 give the sharp bound $|f'(0)| \le 4$; <1>5 exhibits extremal examples.
:::
