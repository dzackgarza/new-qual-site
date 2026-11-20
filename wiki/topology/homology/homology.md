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

[[FF-2Q7RD]]

[[PR-B6BB2]]

::: {.example title="Wedges of spheres"}
For $n\geq 1$ and $k\geq 1$,
$$
H_{n}\qty{\bigvee^{k} S^n} \cong \ZZ^k
$$
by additivity of reduced homology over a wedge [[PR-B6BB2]], with $\tilde H_n(S^n)\cong\ZZ$.

:::

[[FF-UBJ3S]]

[[T-FBMYQ]]

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

## Mayer--Vietoris

::: {.fact title="Splitting over a free quotient"}
Since $\ZZ^m$ is free, every exact sequence of abelian groups $0\to\ZZ^n\to B\to\ZZ^m\to 0$ splits by the [[D-SIUWU|splitting lemma]], so $B\cong \ZZ^{n}\oplus \ZZ^m$ [@Hat02, §2.2].
:::

[[D-FAIJX]]

::: {.example title="Homology of a connected sum"}
For connected closed $n$-manifolds $M$ and $N$, $M\# N = (M\sm D)\union_{S^{n-1}} (N\sm D')$ for open $n$-balls $D\subseteq M$ and $D'\subseteq N$.
The Mayer--Vietoris sequence for open neighborhoods of the two pieces, which deformation retract onto them and meet in a neighborhood of $S^{n-1}$ deformation retracting onto $S^{n-1}$, computes $H_*(M\# N)$ from $H_*(M\sm D)$, $H_*(N\sm D')$, and $H_*(S^{n-1})$.

:::

[[PR-6PENU]]

## Further exact sequences

[[T-TZ3X7]]

[[T-2W5WN]]

## Relative homology

[[D-UEWPN]]

[[PR-P222G]]

For the cellular filtration of a CW complex, $H_j(X^{(k)},X^{(k-1)})\cong\ZZ[\theset{\text{$k$-cells of $X$}}]$ for $j=k$ and $0$ otherwise, since $X^{(k)}/X^{(k-1)}$ is a wedge of $k$-spheres.

## Exercises

[[P-S7WVQ]]

[[E-AUAOC]]
