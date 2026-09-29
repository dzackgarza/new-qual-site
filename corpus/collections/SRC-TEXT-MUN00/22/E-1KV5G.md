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

::: {.solution}
Let $m\colon G\times G\to G$ be the continuous multiplication.

::: pf

::: {.pf-step #translations-continuous}
$f_\alpha$ and $g_\alpha$ are continuous for every $\alpha\in G$.

::: pf-proof
The maps $x\mapsto(\alpha,x)$ and $x\mapsto(x,\alpha)$ from $G$ to $G\times G$ are continuous, since their coordinates are constant or the identity.
Composing with $m$ gives $f_\alpha$ and $g_\alpha$.
:::

:::

::: {.pf-step #translations-homeomorphisms}
$f_\alpha$ and $g_\alpha$ are homeomorphisms.

::: pf-proof
$f_{\alpha^{-1}}\circ f_\alpha=f_\alpha\circ f_{\alpha^{-1}}=\operatorname{id}_G$ and $g_{\alpha^{-1}}\circ g_\alpha=g_\alpha\circ g_{\alpha^{-1}}=\operatorname{id}_G$ by associativity, and the inverses are continuous by step [](#translations-continuous){.pf-ref}.
:::

:::

::: pf-qed
Given $x,y\in G$, put $\alpha=yx^{-1}$.
By step [](#translations-homeomorphisms){.pf-ref}, $f_\alpha$ is a homeomorphism of $G$ onto itself, and $f_\alpha(x)=yx^{-1}x=y$.
So $G$ is homogeneous.
:::

:::

:::
