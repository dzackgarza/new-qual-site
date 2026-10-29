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

::: {.problem}
Let $p$ be an odd prime.
Recall the lens space $L(p, q)$ is a $3$-dimensional compact manifold with
$$
H_\ell(L(p, q); \ZZ) = \begin{cases} \ZZ & \ell = 0, 3 \\ \ZZ_p & \ell = 1 \\ 0 & \ell = 2. \end{cases}
$$
Construct a space $X$ with $H_*(X; \ZZ) = H_*(L(p, q); \ZZ)$ but $X$ is not homotopy equivalent to $L(p, q)$.
Verify that $X$ is not homotopy equivalent to $L(p, q)$.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
M=M(\ZZ/p,1)=S^1\cup_p e^2
$$
be the Moore space obtained by attaching a $2$-cell to $S^1$ by the degree-$p$ map, and set
$$
X=M\vee S^3.
$$

::: pf-proof

This is a finite CW complex.

:::

:::

::: pf-step

The cellular chain complex of $M$ is
$$
0\to\ZZ\xrightarrow{p}\ZZ\xrightarrow0\ZZ\to0,
$$
so
$$
H_0(M)=\ZZ,\quad H_1(M)=\ZZ/p,\quad H_i(M)=0\ (i\ge2).
$$

::: pf-proof

Multiplication by $p$ is injective with cokernel $\ZZ/p$.

:::

:::

::: pf-step

Therefore
$$
H_\ell(X;\ZZ)=
\begin{cases}
\ZZ,&\ell=0,3,\\
\ZZ/p,&\ell=1,\\
0,&\text{otherwise},
\end{cases}
$$
which agrees with the homology of $L(p,q)$.

::: pf-proof

Reduced homology of a wedge is the direct sum of the reduced homologies of its summands.

:::

:::

::: pf-step

We have $\pi_1(X)\cong\ZZ/p$, so its universal cover is a $p$-sheeted cover.

::: pf-proof

The $S^3$ summand is simply connected and van Kampen gives $\pi_1(X)=\pi_1(M)=\ZZ/p$.

:::

:::

::: pf-step

The universal cover of $M$ has nonzero $H_2$ of rank $p-1$.

::: pf-proof

The Euler characteristic of $M$ is $1-1+1=1$, so its $p$-sheeted universal cover has Euler characteristic $p$. This universal cover is simply connected and $2$-dimensional, hence $H_0\cong\ZZ$ and $H_1=0$. Therefore
$$
p=\chi(\widetilde M)=1+\operatorname{rank}H_2(\widetilde M),
$$
so $H_2(\widetilde M)\cong\ZZ^{p-1}$.

:::

:::

::: {.pf-step #s6}

Consequently $\pi_2(X)\ne0$.

::: pf-proof

The universal cover of $X$ is obtained from $\widetilde M$ by attaching $p$ copies of $S^3$ at lifts of the wedge point, so its $H_2$ remains $\ZZ^{p-1}$. By Hurewicz for the simply connected universal cover,
$$
\pi_2(X)\cong\pi_2(\widetilde X)\cong H_2(\widetilde X)\ne0.
$$

:::

:::

::: {.pf-step #s7}

But $\pi_2(L(p,q))=0$.

::: pf-proof

The universal cover of a lens space is $S^3$, and covering maps induce isomorphisms on $\pi_2$. Since $\pi_2(S^3)=0$, the result follows.

:::

:::

::: pf-step

Hence $X$ has the same integral homology as $L(p,q)$ but is not homotopy-equivalent to it.

::: pf-proof

Homotopy equivalence would preserve $\pi_2$, contradicting steps [](#s6){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

:::

:::
