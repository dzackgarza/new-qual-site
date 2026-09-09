---
schema: qual/card@1
id: P-TOPS05I
kind: problem
title: A space with the homology but not the homotopy type of a lens space
classification:
  areas:
  - topology
  topics:
  - Homology
  - Homotopy Type
  - Lens Spaces
relations: []
review: draft
---

::: problem
Let $p$ be an odd prime.
Recall the lens space $L(p, q)$ is a $3$-dimensional compact manifold with
$$
H_\ell(L(p, q); \mathbb{Z}) = \begin{cases} \mathbb{Z} & \ell = 0, 3 \\ \mathbb{Z}_p & \ell = 1 \\ 0 & \ell = 2. \end{cases}
$$
Construct a space $X$ with $H_*(X; \mathbb{Z}) = H_*(L(p, q); \mathbb{Z})$ but $X$ is not homotopy equivalent to $L(p, q)$.
Verify that $X$ is not homotopy equivalent to $L(p, q)$.
:::

::: {.solution}
<1>1. Let
$$
M=M(\mathbb Z/p,1)=S^1\cup_p e^2
$$
be the Moore space obtained by attaching a $2$-cell to $S^1$ by the degree-$p$ map, and set
$$
X=M\vee S^3.
$$
::: {.proof}
This is a finite CW complex.
:::

<1>2. The cellular chain complex of $M$ is
$$
0\to\mathbb Z\xrightarrow{p}\mathbb Z\xrightarrow0\mathbb Z\to0,
$$
so
$$
H_0(M)=\mathbb Z,\quad H_1(M)=\mathbb Z/p,\quad H_i(M)=0\ (i\ge2).
$$
::: {.proof}
Multiplication by $p$ is injective with cokernel $\mathbb Z/p$.
:::

<1>3. Therefore
$$
H_\ell(X;\mathbb Z)=
\begin{cases}
\mathbb Z,&\ell=0,3,\\
\mathbb Z/p,&\ell=1,\\
0,&\text{otherwise},
\end{cases}
$$
which agrees with the homology of $L(p,q)$.
::: {.proof}
Reduced homology of a wedge is the direct sum of the reduced homologies of its summands.
:::

<1>4. We have $\pi_1(X)\cong\mathbb Z/p$, so its universal cover is a $p$-sheeted cover.
::: {.proof}
The $S^3$ summand is simply connected and van Kampen gives $\pi_1(X)=\pi_1(M)=\mathbb Z/p$.
:::

<1>5. The universal cover of $M$ has nonzero $H_2$ of rank $p-1$.
::: {.proof}
The Euler characteristic of $M$ is $1-1+1=1$, so its $p$-sheeted universal cover has Euler characteristic $p$. This universal cover is simply connected and $2$-dimensional, hence $H_0\cong\mathbb Z$ and $H_1=0$. Therefore
$$
p=\chi(\widetilde M)=1+\operatorname{rank}H_2(\widetilde M),
$$
so $H_2(\widetilde M)\cong\mathbb Z^{p-1}$.
:::

<1>6. Consequently $\pi_2(X)\ne0$.
::: {.proof}
The universal cover of $X$ is obtained from $\widetilde M$ by attaching $p$ copies of $S^3$ at lifts of the wedge point, so its $H_2$ remains $\mathbb Z^{p-1}$. By Hurewicz for the simply connected universal cover,
$$
\pi_2(X)\cong\pi_2(\widetilde X)\cong H_2(\widetilde X)\ne0.
$$
:::

<1>7. But $\pi_2(L(p,q))=0$.
::: {.proof}
The universal cover of a lens space is $S^3$, and covering maps induce isomorphisms on $\pi_2$. Since $\pi_2(S^3)=0$, the result follows.
:::

<1>8. Hence $X$ has the same integral homology as $L(p,q)$ but is not homotopy-equivalent to it.
::: {.proof}
Homotopy equivalence would preserve $\pi_2$, contradicting <1>6--<1>7.
:::
:::
