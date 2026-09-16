---
schema: qual/card@1
id: D-DEFINTEG
kind: definition
title: Integral ring extensions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Integral Extensions
relations:
- kind: uses
  target: D-DEFINTCL
review: draft
prompts:
- When is a ring map integral, and what is an integral extension?
- How does integral compare with finite as a condition on $B \to A$?
- Show that $k[t] \injects k[t, t\inv]$ is not integral.
---

::: {.definition title="integral ring morphism"}
A ring morphism $\phi: B \to A$ is \dfn{integral} if every element of $A$ is a root of a monic polynomial with coefficients in $\phi(B)$.
When $\phi$ is an inclusion $B \subseteq A$, we call $A$ an **integral extension** of $B$.
:::

::: {.remark}
Integral is the ring-level condition; finite is strictly stronger.
$A$ is a finite $B$-algebra iff it is integral and finitely generated as a $B$-algebra, and the standard example separating them is $\bar{\QQ}$ over $\QQ$: integral, and not finite.

The monic requirement is the whole content.
In $k[t] \subseteq k[t,t\inv]$, the element $t\inv$ satisfies $tx - 1 = 0$, which is not monic over $k[t]$, and indeed $t\inv$ is not integral --- which is the algebraic reason the inclusion of the punctured line is an open immersion rather than a finite map.

Integrality is what powers lying over, going up, and the geometric statement that integral morphisms have finite fibres with closed image.
:::
