---
order: 250
---

# Surfaces and Manifolds

:::{.remark}
The most common spaces appearing in this theory:

- $\SS ^2$, 
- $\TT^2 \definedas  S^1\cross S^1$, 
- $\RP^2$
- $\KK$ the Klein bottle
- $\bbm$ the Möbius Strip
- $\Sigma_n \definedas \#_{i=1}^n \TT^2$.

The first 4 can be obtained from the following pasting diagrams:

![Pasting Diagrams for Surfaces](../../../../assets/assets/40_Topology/figures/PastingDiagrams.png)

:::

## Classification of Surfaces

### The Classification Theorem

[[T-NBARV]]

[[FF-GBHJL]]

[[FF-D5Q4S]] [[FF-WDTKX]]

[[PR-JL5JP]]

[[PR-ZW6XI]]

:::{.remark}
Examples, general procedure?

:::

### Euler Characteristic

:::{.remark}
For closed surfaces the Euler characteristic and orientability together decide the homeomorphism type, so most classification questions reduce to computing $\chi$ and then reading the table below.
:::

[[FF-IEHB2]] [[FF-CKGXX]]

[[FF-W3AIU]]

:::{.fact table="Table of surfaces possible for a given Euler characteristic"}

| Orientable?  | $-4$       | $-3$        | $-2$       | $-1$        | $0$                  | $1$     | $2$         |
| ------------ | ---        | ----        | ----       | ---         | ---                  | ---     | ---         |
| Yes          | $\Sigma_3$ | $\emptyset$ | $\Sigma_2$ | $\emptyset$ | $\TT^2, S^1\cross I$ | $\DD^2$ | $\SS^2$     |
| No           | ?          | ?           | ?          | ?           | $\KK, \bbm$          | $\RP^2$ | $\emptyset$ |

:::

[[FF-23V5J]] [[FF-4DFKT]]

[[FF-SM63J]] [[FF-I5FIJ]]

[[FF-BOIT5]] [[FF-WLJEK]]

[[PR-QV4U5]]

:::{.proof title="Inclusion-exclusion for $\chi$"}
Assume $U,V,U\cap V,X$ have finitely generated homology, so that Euler characteristics are defined.
Mayer–Vietoris is the long exact sequence
\[
\cdots
\to H_n(U\cap V)
\to H_n(U)\oplus H_n(V)
\to H_n(X)
\to H_{n-1}(U\cap V)
\to \cdots
.\]
For any long exact sequence of finitely generated abelian groups the alternating sum of ranks vanishes, so
\[
\chi(U\cap V) - \bigl(\chi(U)+\chi(V)\bigr) + \chi(X)
= 0
,\]
which is the stated identity.

:::

[[FF-AE7ID]]

[[C-CT2NX]]

:::{.proof}
Set $U\simeq A$ and $V\simeq B$ so that $U\cap V\simeq S^2$.
Inclusion-exclusion then gives $\chi(A\# B)=\chi(A)+\chi(B)-\chi(S^2)=\chi(A)+\chi(B)-2$.

:::

### Connect Sums and Polygon Decompositions

[[PR-GKRFP]]

[[PR-LIXWH]]

:::{.proof title="Klein bottle as two projective planes"}
Removing an open disc from $\RP^2$ leaves a Möbius strip (the projective plane is a Möbius strip with a disc glued along the boundary).
The connected sum $\RP^2\#\RP^2$ is therefore two Möbius strips glued along their boundary circles.
That gluing is the standard decomposition of the Klein bottle: $\KK$ is two Möbius bands identified along $\partial$.

:::

[[PR-BDH3V]]

:::{.proof title="Crosscap plus Klein versus crosscap plus torus"}
The classification theorem [[T-NBARV]] includes the relation $3\RP^2 = \RP^2 \# \TT^2$.
From [[PR-LIXWH]], $\KK\cong \RP^2\#\RP^2$, so
\[
\RP^2 \# \KK
\cong \RP^2 \# \RP^2 \# \RP^2
\cong \RP^2 \# \TT^2
.\]
Equivalently: both sides are closed nonorientable surfaces with
\[
\chi(\RP^2\#\KK)
= 1+0-2
= -1
= \chi(\RP^2\#\TT^2)
,\]
and there is a unique such surface up to homeomorphism.

:::

## Manifolds

:::{.remark}
To show something is not a manifold, try looking at local homology. 
Can use point-set style techniques like removing points, i.e. $H_1(X, X-\pt)$; this should essentially always yield $\ZZ$ by excision arguments.

:::

[[PR-ZCPDD]]

[[PR-LR35S]]

[[PR-4X6G2]]

[[PR-AZQ6S]]

[[PR-TU4G5]]

:::{.proof title="Odd-dimensional closed manifolds"}
Work with rational homology, so Poincaré duality reads $H^k(M;\QQ)\cong H_{n-k}(M;\QQ)$ and the Betti numbers satisfy $b_k(M)=b_{n-k}(M)$.
Then
\[
\chi(M)
= \sum_{k=0}^n (-1)^k b_k
= \sum_{k=0}^n (-1)^k b_{n-k}
= (-1)^n \sum_{k=0}^n (-1)^{n-k} b_{n-k}
= (-1)^n \chi(M)
.\]
If $n$ is odd then $\chi(M)=-\chi(M)$, so $\chi(M)=0$.

:::

[[PR-3FB24]]

[[PR-BQKHS]]

[[T-QNYSB]]

### 3-Manifolds, and Knot Complements

:::{.fact}
Every $\CC\dash$manifold is canonically orientable.

:::

[[PR-UL3KL]]

[[PR-6HORN]]

:::{.proof title="Knot complements"}
Papakyriakopoulos's sphere theorem implies that an irreducible orientable $3$-manifold with infinite fundamental group is aspherical.
A knot complement $S^3\setminus K$ is an open irreducible $3$-manifold with $\pi_1$ infinite (a knot group is never trivial), so $\pi_j(S^3\setminus K)=0$ for $j\geq 2$: it is a $K(\pi,1)$.

For the wedge: $\RR^3\setminus K$ is $S^3\setminus (K\cup\theset{\infty})$.
A small sphere about the point at infinity is homotopically independent of the knot complement, and
\[
\RR^3\setminus K
\simeq
(S^3\setminus K) \vee S^2
.\]

If $K$ is nullhomologous in a $3$-manifold $X$, Mayer–Vietoris for $X = \bigl(X\setminus\nu(K)\bigr)\cup \nu(K)$ has intersection a torus.
The solid torus $\nu(K)\simeq S^1$ kills the meridian, while $[K]=0$ in $H_1(X)$ means the longitude dies in $H_1(X)$.
The remaining generator of $H_1(T^2)$ survives in $H_1(X\setminus\nu(K))$ as a $\ZZ$ factor, and
\[
H_1\bigl(X\setminus\nu(K)\bigr)
\cong
H_1(X)\times\ZZ
.\]

:::

[[PR-WCHFF]]

:::{.proof}
Apply Mayer-Vietoris, taking $S^3 = n(K) \cup (S^3-K)$, where $n(K) \homotopic S^1$ and $S^3-K \cap n(K) \homotopic T^2$. 
Use the fact that $S^3-K$ is a connected, open 3-manifold, so $H^3(S^3-K) =0$.

:::
