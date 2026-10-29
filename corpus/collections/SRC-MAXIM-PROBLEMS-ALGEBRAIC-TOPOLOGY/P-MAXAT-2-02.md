---
schema: qual/card@1
id: P-MAXAT-2-02
kind: problem
title: Maxim algebraic topology 2.2
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 2, problem 2 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Describe the cell structure on lens spaces.
:::

::: {.solution}

For the standard $(2n-1)$-dimensional lens space
\[
L^{2n-1}(p;q_1,\ldots,q_n)
=S^{2n-1}/C_p,
\]
where the cyclic group acts freely by
\[
(z_1,\ldots,z_n)\longmapsto
(\zeta^{q_1}z_1,\ldots,\zeta^{q_n}z_n),
\qquad \zeta=e^{2\pi i/p},
\]
there is a CW structure with exactly one cell in every dimension $0,1,\ldots,2n-1$.

::: pf

::: {.pf-step #s1-1}

The sphere $S^{2n-1}$ admits a $C_p$-equivariant CW decomposition with $p$ cells in each dimension $0,1,\ldots,2n-1$, on which $C_p$ acts transitively in each dimension.


::: pf-proof

Filter the sphere by the coordinate subspaces
\[
S^1\subset S^3\subset\cdots\subset S^{2n-1},
\]
where $S^{2k-1}$ is given by $z_{k+1}=\cdots=z_n=0$. On each successive coordinate layer, choose a fundamental angular sector for the free $C_p$-action and decompose it into one cell in dimensions $2k-2$ and $2k-1$. Translating this sector by the $p$ group elements produces $p$ cells in each of those dimensions. Repeating for $k=1,\ldots,n$ gives the asserted equivariant decomposition.

:::

:::

::: {.pf-step #s1-2}

Passing to the quotient gives one cell
\[
e^k
\]
in each dimension
\[
k=0,1,\ldots,2n-1.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, the $p$ cells of each fixed dimension form a single $C_p$-orbit. The quotient therefore identifies them to one cell, and equivariance of the attaching maps makes the quotient a CW complex.

:::

:::

::: {.pf-step #s1-3}

For the ordinary cellular chain complex with integral coefficients, the boundary maps alternate as
\[
0\longrightarrow\ZZ
\xrightarrow{0}\ZZ
\xrightarrow{p}\ZZ
\xrightarrow{0}\ZZ
\xrightarrow{p}\cdots
\xrightarrow{p}\ZZ
\xrightarrow{0}\ZZ
\longrightarrow0.
\]
Equivalently,
\[
d_k=
\begin{cases}
0,&k\text{ odd},\\
p,&k\text{ even},\ 0<k<2n.
\end{cases}
\]


::: pf-proof

The universal cover has deck group $C_p=\langle t\rangle$. In the equivariant cellular chain complex over $\ZZ[C_p]$, after suitable choices of lifted cells, the differentials alternate between a factor of $t^{a_k}-1$ and the norm element
\[
N=1+t+\cdots+t^{p-1},
\]
where each $a_k$ is a unit modulo $p$ determined by the lens-space weights. Passing to ordinary cellular chains tensors with the trivial $\ZZ[C_p]$-module $\ZZ$, so $t$ acts as $1$. Thus $t^{a_k}-1$ becomes $0$, while $N$ becomes multiplication by $p$. Since the top dimension $2n-1$ is odd, this yields the displayed alternating complex.

:::

:::

::: {.pf-step #s1-4}

In particular, the CW structure recovers the standard homology groups
\[
H_k(L^{2n-1};\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,2n-1,\\
\ZZ/p,&k\text{ odd},\ 0<k<2n-1,\\
0,&k\text{ even},\ 0<k<2n-1.
\end{cases}
\]


::: pf-proof

Compute kernels modulo images in the cellular chain complex of step [](#s1-3){.pf-ref}. At an interior odd degree, the outgoing differential is zero and the incoming differential is multiplication by $p$, giving $\ZZ/p$. At an interior even degree, multiplication by $p$ is injective, giving zero homology. The bottom and top groups are $\ZZ$ because the space is connected and the top differential is zero with no incoming differential.

:::

:::

::: {.pf-step #s1-5}

For the classical three-dimensional lens space $L(p,q)$, this specializes to one cell in each dimension $0,1,2,3$ with cellular complex
\[
0\to\ZZ\xrightarrow{0}\ZZ
\xrightarrow{p}\ZZ
\xrightarrow{0}\ZZ\to0.
\]


::: pf-proof

Set $n=2$ in steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}. The parameter $q$ affects the equivariant attaching map, and hence finer invariants such as the homotopy type, but after passing to ordinary integral cellular chains only the factor $p$ remains.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} describe the cell structure and attaching differentials, while steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} record their standard consequences and the classical $3$-dimensional case.

:::

:::

:::
