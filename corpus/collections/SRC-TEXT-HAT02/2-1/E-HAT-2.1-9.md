---
schema: qual/card@1
id: E-HAT-2.1-9
kind: problem
title: Homology of $\Delta$-complex from $\Delta^n$ with all faces of same dimension identified
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Observed that the unique k-simplex has boundary coefficient sum 1 for even k and 0 for odd k, so the chain complex alternates identity and zero maps.
---

::: {.problem}
Compute the homology groups of the $\Delta$-complex $X$ obtained from $\Delta^n$ by identifying all faces of the same dimension.
Thus $X$ has a single $k$ simplex for each $k \leq n$.
:::

::: {.solution}
Let $\sigma_k$ denote the unique $k$-simplex of $X$. Then
\[
C_k(X)\cong\mathbb Z\langle\sigma_k\rangle
\qquad(0\le k\le n).
\]

<1>1. The simplicial boundary is
\[
\partial_k(\sigma_k)
=
\left(\sum_{i=0}^k(-1)^i\right)\sigma_{k-1}
=
\begin{cases}
\sigma_{k-1},&k\text{ even},\\
0,&k\text{ odd}.
\end{cases}
\]
::: {.proof}
All $(k-1)$-faces of $\sigma_k$ are identified with the unique simplex $\sigma_{k-1}$. Hence the usual alternating boundary formula collapses to the displayed coefficient sum. This alternating sum is $1$ when $k$ is even and $0$ when $k$ is odd.
:::

<1>2. Thus the chain complex is
\[
0\longrightarrow\mathbb Z
\mathop{\longrightarrow}^{\partial_n}
\mathbb Z
\mathop{\longrightarrow}^{\partial_{n-1}}
\cdots
\mathbb Z
\mathop{\longrightarrow}^{\partial_1}
\mathbb Z
\longrightarrow0,
\]
where $\partial_k$ is the identity for even $k$ and zero for odd $k$.
::: {.proof}
This is exactly <1>1 after identifying each $C_k$ with $\mathbb Z$.
:::

<1>3. For every $0<k<n$ one has
\[
H_k(X)=0.
\]
::: {.proof}
If $k$ is even then $\partial_k=1$, so $\ker\partial_k=0$. If $k$ is odd then $\partial_k=0$, but $k+1$ is even, so
\[
\operatorname{im}\partial_{k+1}=\mathbb Z=C_k.
\]
Thus the homology vanishes in either case.
:::

<1>4. The top homology is
\[
H_n(X)\cong
\begin{cases}
\mathbb Z,&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}
\]
::: {.proof}
There is no incoming boundary in degree $n$. Hence
\[
H_n(X)=\ker\partial_n.
\]
By <1>1, $\partial_n=0$ for odd $n$ and is the identity for even $n$.
:::

<1>5. Therefore
\[
\boxed{
H_0(X)\cong\mathbb Z,
\qquad
H_k(X)=0\ (0<k<n),
\qquad
H_n(X)\cong
\begin{cases}
\mathbb Z,&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}
}
\]
::: {.proof}
The space is connected, so $H_0(X)\cong\mathbb Z$. The higher groups are given by <1>3--<1>4.
:::
:::
