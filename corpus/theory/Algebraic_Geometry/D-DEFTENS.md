---
schema: qual/card@1
id: D-DEFTENS
kind: definition
title: The tensor product of modules, and extension of scalars
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Modules
  - Tensor Products
relations:
- kind: uses
  target: D-DEFADJ
review: draft
prompts:
- State the universal property of $M \tensor_A N$, and sketch the construction.
- What is extension of scalars along $B \to A$?
- Why is tensoring right exact but not exact?
---

::: {.definition title="tensor product"}
Let $B \to A$ be a map of rings and $M$ a $B$-module.
Any $A$-module is naturally a $B$-module; to endow $M$ with an $A$-module structure one forms $M \tensor_B A$, \dfn{extension of scalars}, and $\wait \tensor_B A$ is a covariant functor from $B$-modules to $A$-modules.

For $A$-modules $M$ and $N$, the tensor product $M \tensor_A N$ satisfies a universal property: for any $A$-bilinear map $M \times N \to T$ there is a unique map of $A$-modules $M \tensor_A N \to T$ through which it factors.

It exists by explicit construction, as the $A$-linear combinations of simple tensors $m \tensor n$ subject to
\[
\begin{aligned}
(a_1m_1 + a_2m_2)\tensor n &= a_1(m_1 \tensor n) + a_2(m_2\tensor n), \\
m \tensor (b_1n_1 + b_2n_2) &= b_1(m\tensor n_1) + b_2(m \tensor n_2), \\
a(m\tensor n) &= (am)\tensor n = m \tensor (an) ,
\end{aligned}
\]
with the bilinear map $(m,n)\mapsto m \tensor n$.
:::

::: {.remark}
Tensor functors are right exact and are left adjoints to the corresponding $\Hom$ functor; by LAPC the right exactness is a consequence of the adjunction rather than a separate computation.
The failure of left exactness is measured by $\Tor$.

Simple tensors are not a basis and $m \tensor n = 0$ does not force $m$ or $n$ to vanish: over $\ZZ$, $2 \tensor 1 = 0$ in $\ZZ \tensor_\ZZ \ZZ/2$ read through $\ZZ/2 \tensor \ZZ/2$-style identifications, and this is the usual source of errors.
Tensoring is also the algebraic side of the fibre product of schemes, $\Spec A \times_{\Spec C} \Spec B = \Spec(A \tensor_C B)$.
:::
