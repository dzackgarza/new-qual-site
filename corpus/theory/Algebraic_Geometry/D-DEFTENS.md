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

For $A$-modules $M$ and $N$, the \dfn{tensor product} $M \tensor_A N$ satisfies a universal property: for any $A$-bilinear map $M \times N \to T$ there is a unique map of $A$-modules $M \tensor_A N \to T$ through which it factors.

It exists by explicit construction, as the $A$-linear combinations of simple tensors $m \tensor n$ subject to
$$
\begin{aligned}
(a_1m_1 + a_2m_2)\tensor n &= a_1(m_1 \tensor n) + a_2(m_2\tensor n), \\
m \tensor (b_1n_1 + b_2n_2) &= b_1(m\tensor n_1) + b_2(m \tensor n_2), \\
a(m\tensor n) &= (am)\tensor n = m \tensor (an) ,
\end{aligned}
$$
with the bilinear map $(m,n)\mapsto m \tensor n$.
:::

::: {.remark}
The functor $\wait\tensor_AN$ is left adjoint to $\Hom_A(N,\wait)$, so it preserves colimits, in particular cokernels, and is right exact ([[D-DEFADJ]]).
For a short exact sequence $0\to M'\to M\to M''\to0$, the sequence
$$
\Tor_1^A(M'',N)\to M'\tensor_AN\to M\tensor_AN\to M''\tensor_AN\to0
$$
is exact; for $A=\ZZ$, $N=\ZZ/2$, and $0\to\ZZ\xrightarrow{2}\ZZ\to\ZZ/2\to0$, the map $\ZZ\tensor\ZZ/2\to\ZZ\tensor\ZZ/2$ is zero, with kernel the image of $\Tor_1^\ZZ(\ZZ/2,\ZZ/2)\cong\ZZ/2$.

A simple tensor $m\tensor n$ can vanish with $m\ne0$ and $n\ne0$: in $\ZZ \tensor_\ZZ \ZZ/2$, $2\tensor1=1\tensor2=0$.
Not every element is a simple tensor: $e_1\tensor e_1+e_2\tensor e_2\in k^2\tensor_kk^2$ corresponds to the identity matrix, which has rank $2$, while simple tensors correspond to matrices of rank at most $1$.
For ring maps $C\to A$ and $C\to B$, $\Spec A \times_{\Spec C} \Spec B = \Spec(A \tensor_C B)$.
:::
