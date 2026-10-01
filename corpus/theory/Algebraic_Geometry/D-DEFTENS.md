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
Let $B \to A$ be a map of commutative rings and $M$ a $B$-module.
Any $A$-module is naturally a $B$-module; to endow $M$ with an $A$-module structure one forms $M \tensor_B A$, \dfn{extension of scalars}, and $\wait \tensor_B A$ is a covariant functor from $B$-modules to $A$-modules.

For $A$-modules $M$ and $N$, the tensor product $M \tensor_A N$ satisfies a universal property: for any $A$-bilinear map $M \times N \to T$ there is a unique map of $A$-modules $M \tensor_A N \to T$ through which it factors.

It exists by explicit construction, as the $A$-linear combinations of simple tensors $m \tensor_A n$ subject to
$$
\begin{aligned}
(a_1m_1 + a_2m_2)\tensor_A n &= a_1(m_1 \tensor_A n) + a_2(m_2\tensor_A n), \\
m \tensor_A (b_1n_1 + b_2n_2) &= b_1(m\tensor_A n_1) + b_2(m \tensor_A n_2), \\
a(m\tensor_A n) &= (am)\tensor_A n = m \tensor_A (an) ,
\end{aligned}
$$
with the bilinear map $(m,n)\mapsto m \tensor_A n$.
:::

::: {.remark}
Tensor functors are right exact and are left adjoints to the corresponding $\Hom$ functor; by LAPC the right exactness is a consequence of the adjunction rather than a separate computation.
The failure of left exactness is measured by $\Tor$.

Simple tensors are not a basis and $m \tensor_A n = 0$ does not force $m$ or $n$ to vanish: over $\ZZ$,
$$
2\tensor_\ZZ \bar 1=0
\qquad\text{in}\qquad
\ZZ\tensor_\ZZ\ZZ/2,
$$
although $2\neq0$ in $\ZZ$ and $\bar1\neq0$ in $\ZZ/2$.
Tensoring is also the algebraic side of the fibre product of schemes, $\Spec A \times_{\Spec C} \Spec B = \Spec(A \tensor_C B)$.
:::
