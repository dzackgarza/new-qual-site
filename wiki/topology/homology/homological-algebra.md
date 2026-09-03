---
order: 298
topics:
- Homological Algebra
- Exact Sequences
---

# Appendix: Homological Algebra

## Exact Sequences

[[PR-QDIOC]]

::: {.fact}
Some useful results:

- $0 \into A \injects_{f} B$ is exact iff $f$ is **injective**

- $B\surjects_{f} C \into 0$ is exact iff $f$ is **surjective**

- $0\into A \into B \into 0$ is exact iff $A \cong B$.

- $A \injects B \to C \to D \surjects E$ iff $C = 0$

- $0\to A \to B \mapsvia{\cong} C \to D\to 0$ iff $A = D = 0$.

  - *Proof.* Write $f\colon A\to B$ and $h\colon C\to D$, and let $g\colon B\to C$ be the given isomorphism.
    Exactness at $B$ says $\im f = \ker g$.
    An isomorphism has trivial kernel, so $\im f = 0$; exactness at $A$ says $f$ is injective, so $A=0$.
    Exactness at $C$ says $\im g = \ker h$.
    An isomorphism is surjective, so $\ker h = C$ and $h=0$.
    Exactness at $D$ says $\im h = D$, hence $D=0$.
    Conversely, if $A=D=0$ the sequence is $0\to 0\to B\xrightarrow{\cong} C\to 0\to 0$, which is exact.

- $0\to A\to B \to C \to 0$ splits iff $C$ is free.

- Can think of $C \cong \frac{B}{\im f_1}$.
:::

[[D-3WX4Z]]

::: {.example title="of exact sequences"}
\envlist

- $0 \into \ZZ \mapsvia{\times 2} \ZZ \mapsvia{\text{mod}~2} \frac{\ZZ}{2\ZZ} \into 0$

- $1 \into N \mapsvia{\iota} G \mapsvia{p} \frac{G}{N} \into 1$

  - Groups and normal subgroups

- $1 \into \frac{\ZZ}{n\ZZ} \mapsvia{\iota} D_{2n} \mapsvia{?} \frac{\ZZ}{2\ZZ} \into 1$

  - Dihedral group and cyclic groups

- $0 \into I \intersect J \mapsvia{\Delta: x\mapsto(x,x)} I \oplus J \mapsvia{f:(x,y) \mapsto x-y} I + J \into 0$

  - $R$-Modules

- $0 \into \frac{R}{I \intersect J} \mapsvia{\Delta: x\mapsto(x,x)} \frac{R}{I} \oplus \frac{R}{J} \mapsvia{f:(x,y) \mapsto x-y} \frac{R}{I + J} \into 0$

- $0 \into \mathbb{H}_1 \mapsvia{\nabla} \mathbb{H}_\text{curl} \mapsvia{\nabla \cross} \mathbb{H}_\text{div} \mapsvia{\nabla \cdot} \mathbb{L}_2 \into 0$

  - Since $\nabla \cross \nabla F = \nabla \cdot\nabla\cross \bar{v} = 0$ in Hilbert spaces
:::

::: {.remark}
Is $f_1\circ f_2 = 0$ equivalent to exactness..? Answer: yes, every exact sequence is a chain complex with trivial homology.
Therefore homology measures the failure of exactness.

> Alternatively stated: Exact sequences are chain complexes with no cycles.
:::

::: {.remark}
Any LES $A_1 \into \cdots \into A_6$ decomposes into a twisted collection of SES's; define $C_k = \ker (A_k \into A_{k+1}) \cong \im(A_{k-1} \into A_k)) \cong \coker(A_{k-2} \into A_{k-1})$, then all diagonals here are exact:
<!--![Long short exact sequences.png](https://upload.wikimedia.org/wikipedia/commons/b/b9/Long_short_exact_sequences.png)-->
:::

## Five Lemma

[[T-BRWA7]]

## Free Resolutions

::: {.example}
The canonical example:
$$
0 \to \ZZ \mapsvia{\times m} \ZZ \mapsvia{\mod m} \ZZ_m \to 0
$$

Or more generally for a finitely generated group $G = \generators{g_1, g_2, \cdots, g_n}$,
$$
\cdots \to \ker(f) \to F[g_1, g_2, \cdots, g_n] \mapsvia{f} G \to 0
$$
where $F$ denotes taking the free group.

Every abelian groups has a resolution of this form and length 2.
:::

## Properties of Tensor

- $A\tensor B \cong B\tensor A$

- $(\wait) \tensor_R R^n = \id$

- $\bigoplus_i A_i \tensor \bigoplus_j B_j = \bigoplus_i\bigoplus_j(A_i \tensor B_j)$

- $\ZZ_m \tensor \ZZ_n = \ZZ_d$

- $\ZZ_n \tensor A = A/nA$

## Properties of Hom

- $\hom_R (\bigoplus_i A_i, \prod B_j) = \bigoplus_i \prod_j \hom(A_i, B_j)$

- Contravariant in first slot, covariant in second

- Exact over vector spaces

[[FF-JXE7U]]

## Properties of Tor

- $\tor_R^0(A, B) = A \tensor_R B$

- $\tor(\bigoplus_i A_i, \bigoplus_j B) = \bigoplus_i \bigoplus_j \tor(\mathbf{T}A_i, \mathbf{T}B_j)$  where $\mathbf{T}G$ is the torsion component of $G$.

- $\tor(A, B) = \tor(B, A)$

- $\tor(\ZZ_n, G) = \ker (g \mapsto ng) = \theset{g\in G\mid ng = 0}$

## Properties of Ext

- $\ext_R^0(A, B) = \hom_R(A, B)$

- $\ext(\bigoplus_i A_i, \prod_j B_j) = \bigoplus_i \prod_j \ext(\mathbf{T}A_i, B_j)$

- $\ext(F, G) = 0$ if $F$ is free

- $\ext(\ZZ_n, G) \cong G/nG$

## Computing Tor

$$
\tor(A, B) = h[\cdots \to A_n \tensor B \to A_{n-1}\tensor B \to \cdots A_1\tensor B \to 0]
$$
where $A_*$ is any free resolution of $A$.

Shorthand/mnemonic:
$$
\tor: \mathcal{F}(A) \to (\wait \tensor B) \to H_*
$$

[[FF-5QPHF]]

## Computing Ext

$$
\ext(A, B) = h[\cdots \hom(A, B_n) \to \hom(A, B_{n-1}) \to \cdots \to \hom(A, B_1) \to 0 ]
$$
where $B_*$ is a any free resolution of $B$.

Shorthand/mnemonic:
$$
\ext: \mathcal{F}(B) \to \hom(A, \wait) \to H_*
$$

[[FF-WZDSS]]

## Hom/Ext/Tor Tables

| $\hom$ | $\ZZ_m$ | $\ZZ$ | $\QQ$ |
| --- | --- | --- | --- |
| $\ZZ_n$ | $\ZZ_d$ | $0$ | $0$ |
| $\ZZ$ | $\ZZ_m$ | $\ZZ$ | $\QQ$ |
| $\QQ$ | $0$ | $0$ | $\QQ$ |

| $\tor$ | $\ZZ_m$ | $\ZZ$ | $\QQ$ |
| --- | --- | --- | --- |
| $\ZZ_n$ | $\ZZ_d$ | $0$ | $0$ |
| $\ZZ$ | $0$ | $0$ | $0$ |
| $\QQ$ | $0$ | $0$ | $0$ |

| $\ext$ | $\ZZ_m$ | $\ZZ$ | $\QQ$ |
| --- | --- | --- | --- |
| $\ZZ_n$ | $\ZZ_d$ | $\ZZ_n$ | $0$ |
| $\ZZ$ | $0$ | $0$ | $0$ |
| $\QQ$ | $0$ | $\mathcal{A_p}/\QQ$ | $0$ |

Where $d = \gcd(m, n)$ and $\ZZ_0 \definedas 0$.

[[FF-D2KJJ]]

Things that behave like "the zero functor":

- $\ext(\ZZ, \wait)$

- $\tor(\wait, \ZZ), \tor(\ZZ, \wait)$

- $\tor(\wait, \QQ), \tor(\QQ, \wait)$

Thins that behave like "the identity functor":

- $\hom(\ZZ, \wait)$

- $\wait \tensor_\ZZ \ZZ$ and $\ZZ \tensor_\ZZ \wait$

For description of $\mathcal{A_p}$, see [here](http://math.jhu.edu/~jmb/note/torext.pdf).
This is a certain ring of adeles.
