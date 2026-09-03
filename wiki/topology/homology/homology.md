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

## Useful Facts

:::{.fact}
$H_0(X)$ is a free abelian group on the set of path components of $X$.
Thus if $X$ is path connected, $H_0(X) \cong \ZZ$.
In general, $H_0(X) \cong \ZZ^{\abs{\pi_0(X)}}$, where $\abs{\pi_0(X)}$ is the number of path components of $X$.

:::

[[PR-B6BB2]]

:::{.example title="Application"}
\[
H_{n}(\bigvee_{k} S^n) = \ZZ^k
.\]

:::

:::{.proof}
Give the finite wedge one $0$-cell and $k$ cells in dimension $n$.
Its cellular chain group in degree $n$ is therefore $\ZZ^k$, with zero incoming and outgoing cellular differential in that degree, so
\[
H_n\qty{\bigvee_{j=1}^k S^n}\cong \ZZ^k.
\]

:::

:::{.warnings}
$H_{k} \qty{ \prod_ \alpha X_ \alpha}$ is **not** generally equal to $\prod_ \alpha \qty{ H_{k} X_ \alpha }$.
For a finite product, the Künneth theorem describes the correction terms. In particular, if the relevant homology groups are torsion-free, then
\[
H_{k} (A\cross B) \cong \bigoplus_{i+j=k} H_{i}(A) \tensor H_{j}(B)
\]
and iteration gives the corresponding tensor-product decomposition for a finite product.
\[
H_{n}\qty{\prod_{j=1}^k X_{j}} = \bigoplus_{\mathbf{x} \in \mathcal{P}(n,k)} \bigotimes_{i=1}^{k} H_{x_{i}}(X_{i}).
\]

:::

[[FF-UBJ3S]]

[[T-FBMYQ]]

:::{.fact title="Cellular-chain quick checks"}
\envlist

- If a CW complex has no $n\dash$cells, then its cellular chain group $C_n(X)$ is zero, hence $H_n(X)=0$.
- If a CW complex has a single $0\dash$cell, then its cellular differential $d_1:C_1(X)\to C_0(X)$ is zero.

:::

## Known Homology

:::{.example title="Spheres"}
\[
H_{i}(S^n) = 
\begin{cases}
\ZZ & i = 0, n
\\
0 & \text{else}.
\end{cases}
\]

:::

### Real Projective Spaces

[[FF-SYCKI]] [[FF-LFY7V]]

[[FF-MJEUU]]

[[FF-7LLAF]]

### Complex Projective Spaces

[[FF-NEJ3S]]

### Surfaces

[[FF-EC6QN]] [[FF-QOQ2K]]

## Mayer-Vietoris

:::{.fact title="Useful algebra fact"}
Since $\ZZ$ is free and thus projective, any exact sequence of the form $0 \to \ZZ^n \to A \to \ZZ^m \to 0$ splits and $A\cong \ZZ^{n}\cross \ZZ^m$.

:::

[[FF-5LPTQ]]

[[T-3VUOH]]

:::{.example title="Application: computing the homology of a connect sum"}
$H_*(A \# B)$: Use the fact that $A\# B = A \union_{S^n} B$ to apply Mayer-Vietoris.

:::

[[PR-6PENU]]

:::{.proof}
Write $X = A \cup B$, the northern and southern hemispheres, so that $A \cap B = S^{n-1}$, the equator. In the LES, we have:

\[
H^{i+1}(S^n) \xrightarrow{} H^i(S^{n-1}) \xrightarrow{} H^iA \oplus H^i B \xrightarrow{} H^i S^n \xrightarrow{} H^{i-1}(S^{n-1}) \xrightarrow{} H^{i-1}A \oplus H^{i-1}B
.\]

But $A, B$ are contractible, so $H^iA= H^iB = 0$, so we have

\[
H^{i+1}(S^n) \xrightarrow{} H^{i}(S^{n-1}) \xrightarrow{} 0 \oplus 0 \xrightarrow{}H^i(S^n) \xrightarrow{} H^{i-1}(S^{n-1}) \xrightarrow{} 0
.\]

In particular, we have the shape $0 \to A \to B \to 0$ in an exact sequence, which is always an isomorphism.

:::

## More Exact Sequences

[[T-TZ3X7]]

[[T-2W5WN]]

## Relative Homology

:::{.fact title="Relative and cellular homology"}
\envlist

- If $(X,A)$ is a good pair, then the quotient map induces
  \[
  H_n(X,A)\cong \widetilde H_n(X/A).
  \]

- The long exact sequence of a pair is
  \[
  \cdots\to H_n(A)\to H_n(X)\to H_n(X,A)\to H_{n-1}(A)\to\cdots.
  \]

- For a CW complex $X$, the cellular filtration satisfies
\[
H_j(X^{(k)},X^{(k-1)}) \cong
\begin{cases}
\ZZ[\theset{\text{$k$-cells of $X$}}] & j=k,\\
0 & j\neq k,
\end{cases}
\]
since $X^{(k)}/X^{(k-1)}$ is a wedge of $k$-spheres, one for each $k$-cell.

:::

## Exercises

[[P-S7WVQ]]

[[E-AUAOC]]
