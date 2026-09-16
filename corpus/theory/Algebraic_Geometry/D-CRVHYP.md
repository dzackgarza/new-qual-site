---
schema: qual/card@1
id: D-CRVHYP
kind: definition
title: Hyperelliptic curves, and what the canonical map does to them
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hyperelliptic Curves
  - Canonical Divisor
  - Linear Systems
relations:
- kind: uses
  target: T-D8TUX
- kind: uses
  target: D-CRVGON
review: draft
prompts:
- What is a hyperelliptic curve?
- What does the canonical map do on a hyperelliptic curve?
- Is the $g^1_2$ on a hyperelliptic curve unique?
---

::: {.definition}
A curve $C$ of genus $g \geq 2$ is \dfn{hyperelliptic} if it admits a finite morphism $C \to \PP^1$ of degree $2$, that is, a $g^1_2$.
:::

::: {.proposition}
A hyperelliptic curve has exactly one $g^1_2$.
The canonical system $\abs{K}$ is base-point free for every $g \geq 2$, so it always defines a morphism $C \to \PP^{g-1}$; on a hyperelliptic curve that morphism factors as
\[
C \to \PP^1 \to \PP^{g-1} ,
\]
the degree-two map followed by the $(g-1)$-uple embedding, whose image is a rational normal curve of degree $g-1$.
Equivalently $\abs{K} = (g-1)\, g^1_2$.
:::

::: {.remark}
Hyperelliptic is the exception clause in almost every theorem about curves, and the reason is always this one picture: the canonical map is two-to-one onto a rational normal curve instead of an embedding.

Base-point freeness of $\abs{K}$ is a Riemann--Roch computation worth being able to run: $\ell(K) = g$, and $\ell(K-p) = g-1$ because $\ell(p) = 1$ for a non-rational curve, so the dimension drops by exactly one at every point.
Very ampleness needs the drop by two at every pair $p, q$, and $\ell(K - p - q) = \ell(K) - 2$ fails exactly when $\ell(p+q) = 2$ — a pencil of degree two, which is the definition.

Every curve of genus $2$ is hyperelliptic, since $\abs{K}$ is then a $g^1_2$ outright.
Hyperelliptic curves of genus $g$ are the double covers of $\PP^1$ branched at $2g+2$ points, so they form a family of dimension $2g-1$ inside $\mathcal{M}_g$, which is everything when $g=2$ and a proper subvariety when $g \geq 3$.
:::
