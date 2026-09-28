---
order: 298
topics:
- Homological Algebra
- Exact Sequences
---

# Appendix: homological algebra

## Exact sequences

[[PR-QDIOC]]

::: {.fact}
For maps of abelian groups ($R$-modules):

- $0 \to A \xrightarrow{f} B$ is exact if and only if $f$ is injective.
- $B\xrightarrow{g} C \to 0$ is exact if and only if $g$ is surjective.
- $0\to A \xrightarrow{f} B \to 0$ is exact if and only if $f$ is an isomorphism.
- If $A \xrightarrow{a} B \xrightarrow{b} C \xrightarrow{c} D \xrightarrow{d} E$ is exact, $a$ is surjective, and $d$ is injective, then $C = 0$.
- If $0\to A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{h} D\to 0$ is exact, then $g$ is an isomorphism if and only if $A = D = 0$.
- If $0\to A\xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact, then $g$ induces $C \cong B/\im f$.
- If $0\to A\to B \to C \to 0$ is exact and $C$ is free, then the sequence splits.

:::

::: {.proof title="Proof of the fifth item"}
Suppose $g$ is an isomorphism.
Exactness at $B$ gives $\im f = \ker g = 0$, and $f$ is injective, so $A=0$.
Exactness at $C$ gives $\ker h = \im g = C$, so $h=0$, and $h$ is surjective, so $D=0$.
Conversely, if $A=D=0$, then exactness at $B$ gives $\ker g = 0$ and exactness at $C$ gives $\im g = \ker(C\to 0) = C$.

:::

::: {.example title="A short exact sequence that splits with $C$ not free"}
$0\to\ZZ/2\to\ZZ/2\oplus\ZZ/2\to\ZZ/2\to 0$, with the inclusion of the first factor and the projection onto the second, splits, and $\ZZ/2$ is not free.

:::

[[D-3WX4Z]]

::: {.example title="Exact sequences"}
\envlist

- $0 \to \ZZ \xrightarrow{\times 2} \ZZ \xrightarrow{\operatorname{mod} 2} \ZZ/2 \to 0$.
- For a normal subgroup $N$ of a group $G$, $1 \to N \xrightarrow{\iota} G \xrightarrow{p} G/N \to 1$ with $\iota$ the inclusion and $p$ the quotient map.
- For $n\geq 3$, $1 \to \ZZ/n \xrightarrow{\iota} D_{2n} \xrightarrow{s} \ZZ/2 \to 1$, with $\iota$ the inclusion of the rotations and $s$ sending rotations to $0$ and reflections to $1$.
- For ideals $I,J$ of a commutative ring $R$, $0 \to I \intersect J \xrightarrow{x\mapsto(x,x)} I \oplus J \xrightarrow{(x,y) \mapsto x-y} I + J \to 0$.
- For ideals $I,J$ of a commutative ring $R$, $0 \to R/(I \intersect J) \xrightarrow{x\mapsto(x,x)} R/I \oplus R/J \xrightarrow{(x,y) \mapsto x-y} R/(I + J) \to 0$.
- For a bounded Lipschitz domain $\Omega\subseteq\RR^3$ homeomorphic to a ball, the Sobolev de Rham sequence $0\to\RR \to H^1(\Omega) \xrightarrow{\nabla} H(\operatorname{curl},\Omega) \xrightarrow{\nabla \cross} H(\operatorname{div},\Omega) \xrightarrow{\nabla \cdot} L^2(\Omega) \to 0$ is exact, with $\RR$ the constant functions.

:::

::: {.remark}
A sequence $\cdots\to A_{k-1}\xrightarrow{f_{k-1}} A_k\xrightarrow{f_k} A_{k+1}\to\cdots$ with $f_k\circ f_{k-1} = 0$ for all $k$ is a chain complex, and it is exact if and only if its homology $\ker f_k/\im f_{k-1}$ vanishes in every degree.
Homology measures the failure of a chain complex to be exact.

:::

::: {.remark}
A long exact sequence $\cdots\to A_{k-1}\xrightarrow{f_{k-1}} A_k\xrightarrow{f_k} A_{k+1}\to\cdots$ splits into short exact sequences: with $C_k \coloneqq \ker f_k = \im f_{k-1} \cong \coker f_{k-2}$, each
$$
0\to C_k\to A_k\xrightarrow{f_k} C_{k+1}\to 0
$$
is exact.

:::

## The five lemma

[[T-BRWA7]]

## Free resolutions

::: {.example}
For $m\geq 1$,
$$
0 \to \ZZ \xrightarrow{\times m} \ZZ \xrightarrow{\operatorname{mod} m} \ZZ/m \to 0
$$
is a free resolution of $\ZZ/m$.

For an abelian group $G$ with generating set $S$, let $F$ be the free abelian group on $S$ and $f\colon F\to G$ the induced surjection.
Subgroups of free abelian groups are free, so
$$
0 \to \ker(f) \to F \xrightarrow{f} G \to 0
$$
is a free resolution of $G$ of length $1$.

:::

## Properties of tensor products

::: {.fact}
For abelian groups ($R$-modules over a commutative ring $R$) $A$, $B$, $A_i$, $B_j$, and integers $m,n\geq 1$ with $d=\gcd(m,n)$:

- $A\tensor B \cong B\tensor A$.
- $A \tensor_R R^n \cong A^n$.
- $\qty{\bigoplus_i A_i} \tensor \qty{\bigoplus_j B_j} \cong \bigoplus_i\bigoplus_j(A_i \tensor B_j)$.
- $\ZZ/m \tensor \ZZ/n \cong \ZZ/d$.
- $\ZZ/n \tensor A \cong A/nA$.

:::

## Properties of Hom

::: {.fact}
\envlist

- $\Hom_R \qty{\bigoplus_i A_i, \prod_j B_j} \cong \prod_i \prod_j \Hom_R(A_i, B_j)$.
- $\Hom_R(\wait,\wait)$ is contravariant in the first variable and covariant in the second.
- Over a field, $\Hom(\wait, B)$ and $\Hom(A,\wait)$ are exact.

:::

[[FF-JXE7U]]

## Properties of Tor

::: {.fact}
For abelian groups, with $\mathbf{T}G$ the torsion subgroup of $G$:

- $\tor_0^R(A, B) \cong A \tensor_R B$.
- $\tor\qty{\bigoplus_i A_i, \bigoplus_j B_j} \cong \bigoplus_i \bigoplus_j \tor(\mathbf{T}A_i, \mathbf{T}B_j)$.
- $\tor(A, B) \cong \tor(B, A)$.
- $\tor(\ZZ/n, G) \cong \ker (G\xrightarrow{\times n} G) = \theset{g\in G\mid ng = 0}$.

:::

## Properties of Ext

::: {.fact}
For abelian groups:

- $\ext_R^0(A, B) \cong \Hom_R(A, B)$.
- $\ext\qty{\bigoplus_i A_i, \prod_j B_j} \cong \prod_i \prod_j \ext(A_i, B_j)$.
- $\ext(F, G) = 0$ if $F$ is free.
- $\ext(\ZZ/n, G) \cong G/nG$.

:::

## Computing Tor

::: {.fact}
If $\cdots \to F_1\to F_0\to A\to 0$ is a free resolution of $A$, then
$$
\tor_n(A, B) \cong H_n\qty{\cdots \to F_n \tensor B \to F_{n-1}\tensor B \to \cdots \to F_0\tensor B \to 0}.
$$

:::

[[FF-5QPHF]]

## Computing Ext

::: {.fact}
If $\cdots \to F_1\to F_0\to A\to 0$ is a free resolution of $A$, then
$$
\ext^n(A, B) \cong H^n\qty{0 \to \Hom(F_0, B) \to \Hom(F_1, B) \to \cdots \to \Hom(F_n, B) \to \cdots}.
$$

:::

[[FF-WZDSS]]

## Hom, Ext, and Tor tables

::: {.fact}
For $m,n\geq 1$ and $d = \gcd(m, n)$, with the first argument indexing rows and the second columns:

| $\Hom$ | $\ZZ/m$ | $\ZZ$ | $\QQ$ |
| --- | --- | --- | --- |
| $\ZZ/n$ | $\ZZ/d$ | $0$ | $0$ |
| $\ZZ$ | $\ZZ/m$ | $\ZZ$ | $\QQ$ |
| $\QQ$ | $0$ | $0$ | $\QQ$ |

| $\tor$ | $\ZZ/m$ | $\ZZ$ | $\QQ$ |
| --- | --- | --- | --- |
| $\ZZ/n$ | $\ZZ/d$ | $0$ | $0$ |
| $\ZZ$ | $0$ | $0$ | $0$ |
| $\QQ$ | $0$ | $0$ | $0$ |

| $\ext$ | $\ZZ/m$ | $\ZZ$ | $\QQ$ |
| --- | --- | --- | --- |
| $\ZZ/n$ | $\ZZ/d$ | $\ZZ/n$ | $0$ |
| $\ZZ$ | $0$ | $0$ | $0$ |
| $\QQ$ | $0$ | $\mathbb{A}_f/\QQ$ | $0$ |

Here $\mathbb{A}_f$ is the ring of finite adeles of $\QQ$, containing $\QQ$ diagonally.
A computation of $\ext(\QQ,\ZZ)$ is in [these notes on Tor and Ext](http://math.jhu.edu/~jmb/note/torext.pdf).

:::

[[FF-D2KJJ]]

::: {.remark}
The following functors are zero: $\ext(\ZZ, \wait)$, $\tor(\wait, \ZZ)$, $\tor(\ZZ, \wait)$, $\tor(\wait, \QQ)$, and $\tor(\QQ, \wait)$.
The following are naturally isomorphic to the identity functor: $\Hom(\ZZ, \wait)$, $\wait \tensor_\ZZ \ZZ$, and $\ZZ \tensor_\ZZ \wait$.

:::
