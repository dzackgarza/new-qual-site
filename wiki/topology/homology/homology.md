---
title: Homology theory and computations
order: 230
topics:
- Cohomology
- Cohomology Ring
- Cup Product
- Künneth Formula
- Poincaré Duality

---

# Homology theory and computations

## Basic properties

::: {.fact}
$H_0(X)$ is a free abelian group on the set of path components of $X$.
In particular, $H_0(X) \cong \ZZ$ if $X$ is path connected, and $H_0(X) \cong \ZZ^{\abs{\pi_0(X)}}$ if $X$ has finitely many path components.

:::

[[PR-B6BB2]]

::: {.example title="Wedges of spheres"}
For $n\geq 1$ and $k\geq 1$,
$$
H_{n}\qty{\bigvee^{k} S^n} \cong \ZZ^k.
$$

:::

::: {.proof}
Give the finite wedge one $0$-cell and $k$ cells in dimension $n$.
Its cellular chain group in degree $n$ is therefore $\ZZ^k$, with zero incoming and outgoing cellular differential in that degree, so
$$
H_n\qty{\bigvee_{j=1}^k S^n}\cong \ZZ^k.
$$

:::

::: {.remark}
In general $H_{k} \qty{ \prod_ \alpha X_ \alpha}\not\cong\prod_ \alpha H_{k} (X_ \alpha)$; for a finite product, the Künneth theorem computes $H_k$.
If the homology groups of $A$ are free, then
$$
H_{k} (A\cross B) \cong \bigoplus_{i+j=k} H_{i}(A) \tensor H_{j}(B)
$$
and if the homology groups of $X_1,\ldots,X_{k-1}$ are free, iterating gives
$$
H_{n}\qty{\prod_{j=1}^k X_{j}} \cong \bigoplus_{\mathbf{x} \in \mathcal{P}(n,k)} \bigotimes_{i=1}^{k} H_{x_{i}}(X_{i}),
$$
where $\mathcal P(n,k)$ is the set of $k$-tuples $\mathbf x=(x_1,\ldots,x_k)$ of nonnegative integers with $x_1+\cdots+x_k=n$.

:::

[[FF-UBJ3S]]

[[T-FBMYQ]]

::: {.fact title="Cellular-chain quick checks"}
\envlist

- If a CW complex has no $n\dash$cells, then its cellular chain group $C_n(X)$ is zero, hence $H_n(X)=0$.
- If a CW complex has a single $0\dash$cell, then its cellular differential $d_1:C_1(X)\to C_0(X)$ is zero.

:::

## Computed homology groups

::: {.example title="Spheres"}
$$
H_{i}(S^n) = 
\begin{cases}
\ZZ & i = 0, n
\\
0 & \text{else}.
\end{cases}
$$

:::

### Real projective spaces

[[FF-SYCKI]]

[[FF-MJEUU]]

[[FF-7LLAF]]

### Complex projective spaces

[[FF-NEJ3S]]

### Surfaces

[[FF-QOQ2K]]

## Mayer-Vietoris

::: {.fact title="Splitting over a free quotient"}
Since $\ZZ^m$ is free, every exact sequence of abelian groups $0 \to \ZZ^n \to A \to \ZZ^m \to 0$ splits, so $A\cong \ZZ^{n}\oplus \ZZ^m$.

:::

[[FF-5LPTQ]]

[[D-FAIJX]]

::: {.example title="Homology of a connected sum"}
For connected closed $n$-manifolds $M$ and $N$, $M\# N = (M\sm D)\union_{S^{n-1}} (N\sm D')$ for open $n$-balls $D\subseteq M$ and $D'\subseteq N$.
The Mayer--Vietoris sequence for open neighborhoods of the two pieces, which deformation retract onto them and meet in a neighborhood of $S^{n-1}$ deformation retracting onto $S^{n-1}$, computes $H_*(M\# N)$ from $H_*(M\sm D)$, $H_*(N\sm D')$, and $H_*(S^{n-1})$.

:::

[[PR-6PENU]]

::: {.proof}
Let $n\geq 1$ and write $S^n = A \cup B$ with $A$ and $B$ open neighborhoods of the closed northern and southern hemispheres, chosen so that $A$ and $B$ are contractible and $A \cap B$ deformation retracts onto the equator $S^{n-1}$.
The Mayer--Vietoris sequence in reduced cohomology contains

$$
\tilde H^{i-1}(A) \oplus \tilde H^{i-1}(B) \to \tilde H^{i-1}(S^{n-1}) \xrightarrow{\delta} \tilde H^i(S^n) \to \tilde H^iA \oplus \tilde H^i B
.$$

Since $A$ and $B$ are contractible, their reduced cohomology vanishes, so

$$
0 \to \tilde H^{i-1}(S^{n-1}) \xrightarrow{\delta} \tilde H^i(S^n) \to 0
$$
is exact, and $\delta$ is an isomorphism $\tilde H^{i-1}(S^{n-1})\cong \tilde H^i(S^n)$.

:::

## Further exact sequences

[[T-TZ3X7]]

[[T-2W5WN]]

## Relative homology

::: {.fact title="Relative and cellular homology"}
\envlist

- If $(X,A)$ is a good pair, then the quotient map induces
  $$
  H_n(X,A)\cong \widetilde H_n(X/A).
  $$

- The long exact sequence of a pair is
  $$
  \cdots\to H_n(A)\to H_n(X)\to H_n(X,A)\to H_{n-1}(A)\to\cdots.
  $$

- For a CW complex $X$, the cellular filtration satisfies
$$
H_j(X^{(k)},X^{(k-1)}) \cong
\begin{cases}
\ZZ[\theset{\text{$k$-cells of $X$}}] & j=k,\\
0 & j\neq k,
\end{cases}
$$
since $X^{(k)}/X^{(k-1)}$ is a wedge of $k$-spheres, one for each $k$-cell.

:::

## Exercises

[[P-S7WVQ]]

[[E-AUAOC]]
