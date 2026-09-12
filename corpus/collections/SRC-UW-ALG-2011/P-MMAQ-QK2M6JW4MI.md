---
schema: qual/card@1
id: P-MMAQ-QK2M6JW4MI
kind: problem
title: Irreducible representations of $\mathrm{GL}_2(\mathbb{F}_2)$, and reducibility
  of the adjoint representation in order $12$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Given a finite group $G$, recall that its *regular representation* is the representation on the complex group algebra $\mathbb C[G]$ induced by left multiplication of $G$ on itself and its `\textit{adjoint representation}`{=tex} is the representation on the complex group algebra $\mathbb C[G]$ induced by conjugation of $G$ on itself.

- Let $G=\GL_2(\mathbb F_2)$.
  Describe the number and dimensions of the irreducible representations of $G$.
  Then describe the decomposition of its regular representation as a direct sum of irreducible representations.

- Let $H$ be a group of order 12. Show that its adjoint representation is reducible; that is, there is an $H$-invariant subspace of $\mathbb C[H]$ besides 0 and $\mathbb C[H]$.
:::


::: solution
<1>1. The group $\operatorname{GL}_2(\mathbb F_2)$ is isomorphic to $S_3$.
::: {.proof}
There are exactly three nonzero vectors in $\mathbb F_2^2$. Every invertible linear map permutes them, giving a homomorphism
\[
\operatorname{GL}_2(\mathbb F_2)\longrightarrow S_3.
\]
If an invertible linear map fixes all three nonzero vectors, then in particular it fixes a basis, hence is the identity. Thus the homomorphism is injective. Also
\[
|\operatorname{GL}_2(\mathbb F_2)|=(2^2-1)(2^2-2)=3\cdot2=6=|S_3|,
\]
so it is an isomorphism.
:::

<1>2. Up to isomorphism, $G=\operatorname{GL}_2(\mathbb F_2)$ has exactly three irreducible complex representations, of dimensions
\[
1,\quad1,\quad2.
\]
::: {.proof}
By <1>1 it is enough to work with $S_3$. The trivial representation and the sign representation are distinct irreducible representations of dimension $1$. The permutation representation of $S_3$ on $\mathbb C^3$ has the invariant decomposition
\[
\mathbb C^3
=\mathbb C(1,1,1)\oplus
V,
\qquad
V=\{(z_1,z_2,z_3):z_1+z_2+z_3=0\}.
\]
The $2$-dimensional summand $V$ is irreducible: a proper nonzero invariant subspace would be one-dimensional, hence would give a common eigenline for a transposition and a $3$-cycle; direct inspection of their actions on $V$ shows no such common eigenline exists.

The number of irreducible complex representations of a finite group equals its number of conjugacy classes. The group $S_3$ has three conjugacy classes: the identity, the transpositions, and the $3$-cycles. Hence these three irreducibles are all of them.
:::

<1>3. The regular representation decomposes as
\[
\mathbb C[G]
\cong \mathbf 1\oplus\operatorname{sgn}\oplus V\oplus V.
\]
::: {.proof}
For a finite group over $\mathbb C$, each irreducible representation occurs in the regular representation with multiplicity equal to its dimension. Applying this to the irreducible dimensions $1,1,2$ from <1>2 gives multiplicities $1,1,2$. The total dimension is
\[
1^2+1^2+2^2=6=|G|,
\]
as required.
:::

<1>4. If $H$ is any group of order $12$, its adjoint representation on $\mathbb C[H]$ is reducible.
::: {.proof}
Let
\[
u=\sum_{h\in H}h\in\mathbb C[H].
\]
For any $g\in H$, conjugation permutes the elements of $H$, so
\[
gug^{-1}
=\sum_{h\in H}ghg^{-1}
=\sum_{h\in H}h
=u.
\]
Thus the one-dimensional subspace $\mathbb C u$ is invariant under the adjoint action. It is nonzero and proper because
\[
1=\dim_\mathbb C(\mathbb C u)<12=\dim_\mathbb C\mathbb C[H].
\]
Hence the adjoint representation is reducible.
:::
:::
