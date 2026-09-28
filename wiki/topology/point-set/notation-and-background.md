---
order: 0
---

# Preface

References:

- [@Mun00]
- [@Hat02]

Further reading:

- [The line with two origins](https://blogs.scientificamerican.com/roots-of-unity/a-few-of-my-favorite-spaces-the-line-with-2-origins/)

## Notation

::: {.remark title="Conventions"}
\envlist

- Maps between spaces are continuous.
- Maps of spaces are pointed unless stated otherwise, that is, they are morphisms in $\Top_*$.
- Homology and cohomology have $\ZZ$ coefficients unless stated otherwise.

:::

| Notation                                             | Definition                          |
|------------------------------------------------------|-------------------------------------|
| $X\cross Y, \prod_{j\in J} X_j, X^{\cross n}$        | Direct products                     |
| $X\oplus Y, \bigoplus_{j\in J} X_j, X^{\oplus n}$    | Direct sums                         |
| $X\tensor Y, \bigotimes_{j\in J} X_j, X^{\tensor n}$ | Tensor products                     |
| $X\ast Y, \ast_{j\in J} X_j, X^{\ast n}$             | Free products                       |
| $\ZZ^n$                                              | The free abelian group of rank $n$  |
| $F_n, \ZZ^{\ast n}$                                  | The free group on $n$ generators    |
| $\pi_0(X)$                                           | The set of path components of $X$ |
| $G=1$                                                | The trivial group, written multiplicatively |
| $G=0$                                                | The trivial group, written additively       |

::: {.remark}
The identity element of a group $G$ is written $e_G$, $1_G$, or $0_G$.

:::

::: {.remark title="Direct sums and direct products"}
For a family of modules $(X_j)_{j\in J}$, the direct product $\prod_{j\in J} X_j$ is the set of all tuples $(x_j)_{j\in J}$ with coordinatewise operations, and the direct sum $\bigoplus_{j\in J} X_j$ is the submodule of tuples with only finitely many nonzero entries.
The inclusion $\bigoplus_{j\in J} X_j \injects \prod_{j\in J} X_j$ is an isomorphism when $J$ is finite, and it is not surjective when infinitely many $X_j$ are nonzero.

:::

::: {.remark title="Free groups and free products"}
The free group on $n$ generators is the free product of $n$ copies of $\ZZ$, and it is nonabelian for $n\geq 2$.
It is written multiplicatively: elements of
$$
\ZZ^{\ast n} = \gens{a_1, \ldots, a_n}
$$
are reduced finite words in the symbols $a_i^k$ for $k\in \ZZ$, such as
$$
x = a_1^2 a_2^4 a_1 a_2^{-2}.
$$

:::

::: {.remark title="Free abelian groups"}
The free abelian group $\ZZ^n$ of rank $n$ is the abelianization of $\ZZ^{\ast n}$, written additively.
For a basis $a_1,\ldots,a_n$, each $x\in\ZZ^n$ is uniquely $x = \sum_{i=1}^n c_i a_i$ with $c_i \in \ZZ$; for example,
$$
2a_1 + 4a_2 + a_1 - a_2 = 3a_1 + 3a_2.
$$

:::

::: {.remark title="Indexing conventions and list notation"}
Spaces are usually path connected, in which case $\pi_0(X)$ is a point and $H_0(X) \cong \ZZ$.
Graded objects such as $\pi_*$, $H_*$, and $H^*$ are sometimes written as lists starting in degree $1$:
$$
\begin{aligned}
\pi_*(X) &= [\pi_1(X), \pi_2(X), \pi_3(X), \ldots], \\
H_*(X) &= [H_1(X), H_2(X), H_3(X), \ldots].
\end{aligned}
$$

:::

## Background algebra

::: {.fact}
If $f\colon X\injects Y$ is an injective group homomorphism and $Y$ is trivial, then $X$ is trivial.

:::

[[PR-WB7MM]]

::: {.proof}
Let $f\colon G\to H$ be a homomorphism from a finite group to a free group, so $f(1_G) = 1_H$.
Each $g\in G$ has finite order $n$, and
$$
1_H = f(1_G) = f(g^n) = f(g)^n,
$$
so $f(g)$ has finite order dividing $n$.
Free groups are torsion-free, so $f(g) = 1_H$.

:::

::: {.remark}
The same argument shows that every homomorphism from a finite group to a torsion-free group is trivial.
For a continuous map $f\colon A\to B$ with $\pi_1(A)$ finite and $\pi_1(B)$ torsion-free, such as $\pi_1(B)\cong\ZZ^n$ or a free group, the induced homomorphism $f_*\colon \pi_1(A) \to \pi_1(B)$ is trivial.
The same holds for homomorphisms induced on homology or cohomology groups.

:::
