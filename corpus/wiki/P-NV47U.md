---
schema: qual/card@1
id: P-NV47U
kind: problem
title: "Let $X$ be an arbitrary topological space, and compute $\\pi_1(\\Sigma X\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
Let $X$ be an arbitrary topological space, and compute $\pi_1(\Sigma X)$.

**Solution**:

Write $\Sigma X = U \union V$ where $U = \Sigma X - (X\cross[0,1/2])$ and $U = \Sigma X - X\cross[1/2, 1])$. Then $U\intersect V = X \cross \{1/2\} \cong X$, so $\pi_1(U\intersect V) =\pi_1(X)$.

But both $U$ and $V$ can be identified by the cone on $X$, given by 
$CX = \frac{X \cross I}{X \cross 1}$, by just rescaling the interval with the maps:

$i_U: U \into CX$ where $(x,s) \mapsto (x, 2s-1)$
(The second component just maps $[1/2, 1] \into [0,1]$. )

$i_V: V \into CX$ where $(x, s) \mapsto (x, 2s)$.
(The second component just maps $[0,1/2] \to [0, 1]$)

But $CX$ is contractible by the homotopy $H:CX \cross I \into CX$ where $H((c,s), t) = (c, s(1-t))$.

So $\pi_1(U) = \pi_1(V) = 0​$. 

By Van Kampen, we have $\pi_1(X) = 0 \ast_{\pi_1(X)} 0 = 0.$
