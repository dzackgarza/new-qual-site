---
schema: qual/card@1
id: E-1KV5G
kind: problem
title: Translations are homeomorphisms; topological groups are homogeneous
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $\alpha$ be an element of the topological group $G$.
Show that the maps $f_\alpha, g_\alpha: G \to G$ defined by

$$
f_\alpha(x) = \alpha \cdot x \quad \text{and} \quad g_\alpha(x) = x \cdot \alpha
$$

are homeomorphisms of $G$.
Conclude that $G$ is a homogeneous space.
(This means that for every pair $x, y$ of points of $G$, there exists a homeomorphism of $G$ onto itself that carries $x$ to $y$.)
:::

::: solution
**Goal:** Prove that left and right translations by any element in a topological group $G$ are homeomorphisms, and deduce that $G$ is homogeneous.

<1>1. Continuity of translation maps $f_\alpha$ and $g_\alpha$:
    *Proof:*
    <2>1. By definition of a topological group, the multiplication map $m: G \times G \to G$ given by $m(a, b) = a \cdot b$ is continuous.
    <2>2. The map $i_\alpha: G \to G \times G$ defined by $i_\alpha(x) = (\alpha, x)$ has continuous components: the constant map $x \mapsto \alpha$ and the identity map $x \mapsto x$. Hence $i_\alpha$ is continuous.
    <2>3. Since $f_\alpha = m \circ i_\alpha$, $f_\alpha$ is a composition of continuous maps, so $f_\alpha$ is continuous.
    <2>4. Similarly, $j_\alpha: G \to G \times G$ defined by $j_\alpha(x) = (x, \alpha)$ is continuous, so $g_\alpha = m \circ j_\alpha$ is continuous.

<1>2. $f_\alpha$ and $g_\alpha$ are homeomorphisms:
    *Proof:*
    <2>1. For the left translation $f_\alpha$, consider $f_{\alpha^{-1}}: G \to G$.
    <2>2. For every $x \in G$:
        $$(f_{\alpha^{-1}} \circ f_\alpha)(x) = \alpha^{-1}(\alpha x) = (\alpha^{-1}\alpha)x = ex = x,$$
        $$(f_\alpha \circ f_{\alpha^{-1}})(x) = \alpha(\alpha^{-1}x) = (\alpha\alpha^{-1})x = ex = x.$$
    <2>3. Thus $f_\alpha$ is invertible with two-sided inverse $(f_\alpha)^{-1} = f_{\alpha^{-1}}$.
    <2>4. By <1>1, $f_{\alpha^{-1}}$ is continuous. Therefore $f_\alpha$ is a continuous bijection with a continuous inverse, so $f_\alpha$ is a homeomorphism.
    <2>5. By the identical reasoning, $g_\alpha$ is invertible with continuous inverse $(g_\alpha)^{-1} = g_{\alpha^{-1}}$, so $g_\alpha$ is a homeomorphism.

<1>3. $G$ is a homogeneous space:
    *Proof:*
    <2>1. Let $x, y \in G$ be an arbitrary pair of points.
    <2>2. Define $\alpha = y x^{-1} \in G$.
    <2>3. By <1>2, the left translation $f_\alpha: G \to G$ is a homeomorphism of $G$ onto itself.
    <2>4. Evaluating at $x$:
        $$f_\alpha(x) = \alpha x = (y x^{-1})x = y(x^{-1}x) = ye = y.$$
    <2>5. Thus $f_\alpha$ is a homeomorphism of $G$ that carries $x$ to $y$.
    <2>6. Therefore $G$ is homogeneous. Q.E.D.
:::
