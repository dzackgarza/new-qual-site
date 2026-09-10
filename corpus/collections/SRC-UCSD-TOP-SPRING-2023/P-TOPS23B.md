---
schema: qual/card@1
id: P-TOPS23B
kind: problem
title: '$\pi_2$ of a torus with a disk attached along a curve'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Cell Complexes
  - Surfaces
relations: []
review: draft
---

::: problem
Let $X$ be the space obtained by gluing the boundary of a disc to the curve in the torus shown.
Compute the second homotopy group $\pi_2(X)$.
:::

::: {.solution}
<1>1. The curve shown in the source is an essential simple closed curve on the torus. Up to a self-homeomorphism of $T^2$, we may take it to be the standard loop $a$ in
$$
\pi_1(T^2)=\langle a,b\mid [a,b]\rangle.
$$
::: {.proof}
Every essential simple closed curve on an oriented torus represents a primitive element of $H_1(T^2)\cong\mathbb Z^2$, and $SL_2(\mathbb Z)$ acts transitively on primitive vectors. Every matrix in $SL_2(\mathbb Z)$ is induced by an orientation-preserving self-homeomorphism of the torus.
:::

<1>2. After attaching the disk along $a$,
$$
\pi_1(X)\cong\langle a,b\mid [a,b],a\rangle\cong\langle b\rangle\cong\mathbb Z.
$$
::: {.proof}
Van Kampen adds the relation $a=1$; the commutator relation then becomes redundant.
:::

<1>3. Put $R=\mathbb Z[\pi_1(X)]\cong\mathbb Z[t,t^{-1}]$, where $t$ corresponds to $b$. The universal cover has cellular chain groups
$$
C_2(\widetilde X)\cong R^2,\qquad C_1(\widetilde X)\cong R^2,\qquad C_0(\widetilde X)\cong R.
$$
With the $2$-cells ordered as the original torus cell and the newly attached disk, one may choose bases so that
$$
\partial_2=
\begin{pmatrix}
1-t&1\\
0&0
\end{pmatrix},
\qquad
\partial_1=egin{pmatrix}0&t-1\end{pmatrix}.
$$
::: {.proof}
Use the presentation complex for
$\langle a,b\mid [a,b],a\rangle$ and Fox derivatives. After evaluating in the quotient group $a\mapsto1$, $b\mapsto t$, the derivatives of $[a,b]$ are $1-t$ with respect to $a$ and $0$ with respect to $b$, while those of the relator $a$ are $1$ and $0$.
:::

<1>4. Therefore
$$
H_2(\widetilde X;\mathbb Z)=\ker\partial_2
=R\cdot\binom{1}{t-1}\cong R.
$$
::: {.proof}
A pair $(u,v)\in R^2$ lies in the kernel precisely when $(1-t)u+v=0$, i.e. $v=(t-1)u$.
:::

<1>5. Since $\widetilde X$ is simply connected, the Hurewicz theorem gives
$$
\boxed{\pi_2(X)\cong\pi_2(\widetilde X)\cong H_2(\widetilde X)\cong\mathbb Z[t,t^{-1}].}
$$
As an abelian group this is a countable direct sum of copies of $\mathbb Z$.
::: {.proof}
Covering maps induce isomorphisms on homotopy groups in degrees at least $2$, and for a simply connected space the first potentially nonzero homotopy group $\pi_2$ maps isomorphically to $H_2$.
:::
:::
