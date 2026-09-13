---
schema: qual/card@1
id: P-AGH5110WEILRH
kind: problem
title: Weil's proof of the Riemann hypothesis for curves over finite fields
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
relations: []
review: draft
---

::: problem
Let $C$ be a curve of genus $g$ defined over the finite field $\FF_q$, and let $N$ be the number of points of $C$ rational over $\FF_q$.
Then $N=1-a+q$, with $|a| \leqslant 2 g \sqrt{q}$.

To prove this, we consider $C$ as a curve over the algebraic closure $k$ of $\FF_q$.
Let $f: C \rightarrow C$ be the $k$-linear Frobenius morphism obtained by taking $q$ th powers, which makes sense since $C$ is defined over $\FF_q$, so $X_q \cong X$ (See $V, 2.4.1$).

Let $\Gamma \subseteq C \times C$ be the graph of $f$, and let $\Delta \subseteq C \times C$ be the diagonal.

Show that $\Gamma^2=q(2-2 g)$, and $\Gamma . \Delta=N$.
Then apply (Ex.
1.9) to $D=r \Gamma+s \Delta$ for all $r$ and $s$ to obtain the result.

See (App.
C, Ex.
5.7) for another interpretation of this result.
:::
