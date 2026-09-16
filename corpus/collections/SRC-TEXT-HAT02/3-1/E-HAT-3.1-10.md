---
schema: qual/card@1
id: E-HAT-3.1-10
kind: problem
title: Cohomology of lens spaces with various coefficients
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the cochain, exact-sequence, and universal-coefficient calculations directly.
---

# E-HAT-3.1-10

For the lens space $L_m(\ell_1, \cdots, \ell_n)$ defined in Example 2.43, compute the cohomology groups using the cellular cochain complex and taking coefficients in $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{Z}_m$, and $\mathbb{Z}_p$ for $p$ prime.
Verify that the answers agree with those given by the universal coefficient theorem.

::: {.solution}
Let
\[
L=L_m(\ell_1,\ldots,\ell_n)
\]
be the $(2n-1)$-dimensional lens space. Its standard CW structure has one cell in every dimension $0,1,\ldots,2n-1$, with cellular boundary
\[
d_k=\begin{cases}
0,&k\text{ odd},\\
m,&k\text{ even}.
\end{cases}
\]
Hence with coefficients in an abelian group $G$, the cellular cochain complex has one copy of $G$ in every degree and
\[
\delta^k=\begin{cases}
0,&k\text{ even},\\
\times m,&k\text{ odd}.
\end{cases}
\]

<1>1. For arbitrary $G$,
\[
H^k(L;G)\cong
\begin{cases}
G,&k=0,2n-1,\\
G/mG,&0<k<2n-1\text{ and }k\text{ even},\\
G[m],&0<k<2n-1\text{ and }k\text{ odd},\\
0,&\text{otherwise},
\end{cases}
\]
where $G[m]=\ker(m:G\to G)$.
::: {.proof}
This is immediate from the displayed alternating cochain differential.
:::

<1>2. With $G=\mathbb Z$,
\[
H^k(L;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,2n-1,\\
\mathbb Z_m,&0<k<2n-1\text{ even},\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Multiplication by $m$ on $\mathbb Z$ has zero kernel and cokernel $\mathbb Z_m$.
:::

<1>3. With $G=\mathbb Q$,
\[
H^k(L;\mathbb Q)\cong
\begin{cases}
\mathbb Q,&k=0,2n-1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Multiplication by nonzero $m$ is an isomorphism of $\mathbb Q$.
:::

<1>4. With $G=\mathbb Z_m$,
\[
\boxed{H^k(L;\mathbb Z_m)\cong\mathbb Z_m\quad(0\le k\le2n-1).}
\]
::: {.proof}
Multiplication by $m$ is zero on $\mathbb Z_m$, so every cellular coboundary vanishes.
:::

<1>5. For a prime $p$,
\[
H^k(L;\mathbb Z_p)\cong
\begin{cases}
\mathbb Z_p,&0\le k\le2n-1,&p\mid m,\\
\mathbb Z_p,&k=0,2n-1,&p\nmid m,\\
0,&0<k<2n-1,&p\nmid m.
\end{cases}
\]
::: {.proof}
If $p\mid m$, multiplication by $m$ is zero on $\mathbb Z_p$. If $p\nmid m$, it is an automorphism.
:::

<1>6. These answers agree with the universal coefficient theorem.
::: {.proof}
The integral homology of the lens space is
\[
H_k(L;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,2n-1,\\
\mathbb Z_m,&0<k<2n-1\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]
The cohomological universal coefficient sequence
\[
0\to\operatorname{Ext}(H_{k-1}(L),G)
\to H^k(L;G)
\to\operatorname{Hom}(H_k(L),G)\to0
\]
has
\[
\operatorname{Hom}(\mathbb Z_m,G)=G[m],
\qquad
\operatorname{Ext}(\mathbb Z_m,G)=G/mG,
\]
which reproduces exactly the formula in <1>1.
:::
:::
