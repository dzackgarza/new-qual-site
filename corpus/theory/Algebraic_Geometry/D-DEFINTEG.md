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
- 'For a subring $R \subseteq F$ and $a \in F$, show that the following are equivalent: $a$ is integral over $R$; $R[a]$ is a finitely generated $R$-module; there is a ring $R[a] \subseteq L \subseteq F$ that is a finitely generated $R$-module.'
- If $F$ is a field integral over a subring $R$, show that $R$ is a field.
- Show that $k[x][f^{-1}]$ is not a field for any $f \in k[x]$.
---

::: {.definition title="integral ring morphism"}
A ring morphism $\phi: B \to A$ is \dfn{integral} if every element of $A$ is a root of a monic polynomial with coefficients in $\phi(B)$.
When $\phi$ is an inclusion $B \subseteq A$, we call $A$ an \dfn{integral extension} of $B$.
:::

::: {.remark}
$A$ is a finite $B$-algebra if and only if it is integral and finitely generated as a $B$-algebra.
For example, $\bar{\QQ}$ is integral over $\QQ$ and not finite.

In $k[t] \subseteq k[t,t\inv]$, the element $t\inv$ is a root of the non-monic polynomial $tx - 1$ and is not integral over $k[t]$: multiplying a relation $t^{-n}+b_1t^{-(n-1)}+\cdots+b_n=0$ by $t^n$ gives $1\in tk[t]$.
So the open immersion $\Spec k[t,t\inv]\to\Spec k[t]$ is not finite; its image $\AA^1\sm\ts{0}$ is not closed.

For an integral extension $B\subseteq A$, lying over and going up hold, and no two distinct primes of $A$ over the same prime of $B$ are comparable [@AM18, Chapter 5].
Hence $\Spec A\to\Spec B$ is surjective and closed, and its fibres have dimension $0$; the fibres need not be finite, since the fibre of $\Spec\bar\ZZ\to\Spec\ZZ$ over $(p)$ is infinite, where $\bar\ZZ$ is the ring of algebraic integers.
:::
