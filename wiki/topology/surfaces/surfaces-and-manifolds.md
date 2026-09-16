---
order: 250
topics:
- Surfaces
- Manifolds
- Classification of Surfaces
- Classification
- Orientation
- Knot Theory
---

# Surfaces and manifolds

::: {.example title="Standard surfaces"}
\envlist

- the sphere $\SS ^2$;
- the torus $\TT^2 \coloneqq  S^1\cross S^1$;
- the real projective plane $\RP^2$;
- the Klein bottle $\KK$;
- the Möbius band $\bbm$;
- the closed orientable surface of genus $g$, $\Sigma_g \coloneqq \#_{i=1}^g \TT^2$.

The first four are quotients of a square by the edge identifications in the following pasting diagrams:

![Pasting Diagrams for Surfaces](../../../../assets/assets/Topology/figures/PastingDiagrams.png)

:::

## Classification of surfaces

### The classification theorem

[[T-NBARV]]

::: {.remark}
A compact connected surface is therefore determined up to homeomorphism by its orientability, its number $b$ of boundary components, and its Euler characteristic.
A polygon model computes these: the edge word of a polygon with identifications reduces to a normal form $a_1b_1a_1\inv b_1\inv\cdots a_gb_ga_g\inv b_g\inv$ or $a_1a_1\cdots a_ka_k$, together with the unpaired boundary edges.
For example, the torus and the annulus both have Euler characteristic $0$ and are not homeomorphic, since $b=0$ for the torus and $b=2$ for the annulus.

:::

[[FF-GBHJL]]

[[FF-D5Q4S]] [[FF-WDTKX]]

[[PR-JL5JP]]

[[PR-ZW6XI]]

### Euler characteristic

[[FF-IEHB2]] [[FF-CKGXX]]

[[FF-W3AIU]]

::: {.fact title="Closed surfaces by Euler characteristic"}
The closed orientable surface $\Sigma_g$ has $\chi = 2-2g$, and the closed nonorientable surface $N_k \coloneqq \#_{i=1}^k\RP^2$ has $\chi = 2-k$.
Removing the interiors of $b$ disjoint discs lowers $\chi$ by $b$.

| Orientable | $-4$       | $-3$        | $-2$       | $-1$        | $0$     | $1$     | $2$         |
| ---------- | ---        | ----        | ----       | ---         | ---     | ---     | ---         |
| Yes        | $\Sigma_3$ | none        | $\Sigma_2$ | none        | $\TT^2$ | none    | $\SS^2$     |
| No         | $N_6$      | $N_5$       | $N_4$      | $N_3$       | $\KK$   | $\RP^2$ | none        |

With boundary, $\chi=0$ also includes the annulus $S^1\cross I$ and the Möbius band $\bbm$, and $\chi=1$ includes the disc $\DD^2$.

:::

[[FF-23V5J]] [[FF-4DFKT]]

[[FF-SM63J]] [[FF-I5FIJ]]

[[FF-BOIT5]] [[FF-WLJEK]]

[[PR-QV4U5]]

::: {.proof title="Inclusion-exclusion for $\chi$"}
Let $U,V\subseteq X$ be open with $X=U\cup V$, and assume $U$, $V$, $U\cap V$, and $X$ have finitely generated total homology, so that their Euler characteristics are defined.
The Mayer--Vietoris sequence
$$
\cdots
\to H_n(U\cap V)
\to H_n(U)\oplus H_n(V)
\to H_n(X)
\to H_{n-1}(U\cap V)
\to \cdots
$$
is a finite long exact sequence of finitely generated abelian groups, so the alternating sum of the ranks of its terms vanishes:
$$
\chi(U\cap V) - \bigl(\chi(U)+\chi(V)\bigr) + \chi(X)
= 0.
$$

:::

[[FF-AE7ID]]

[[C-CT2NX]]

::: {.proof}
Let $A$ and $B$ be compact surfaces, and let $A'$ and $B'$ be $A$ and $B$ with the interior of a closed disc removed, so that $A\# B = A'\union_{S^1} B'$.
Gluing a disc back along a circle and applying inclusion-exclusion gives $\chi(A) = \chi(A') + \chi(\DD^2) - \chi(S^1) = \chi(A')+1$, and likewise $\chi(B)=\chi(B')+1$.
Applying inclusion-exclusion to open neighborhoods $U\homotopic A'$ and $V\homotopic B'$ with $U\cap V\homotopic S^1$,
$$
\chi(A\# B)=\chi(A')+\chi(B')-\chi(S^1)=\chi(A)+\chi(B)-2.
$$

:::

### Connected sums and polygon decompositions

[[PR-GKRFP]]

[[PR-LIXWH]]

::: {.proof title="Klein bottle as two projective planes"}
Removing an open disc from $\RP^2$ leaves a Möbius band, since $\RP^2$ is a Möbius band with a disc glued along its boundary circle.
The connected sum $\RP^2\#\RP^2$ is therefore two Möbius bands glued along their boundary circles, which is the Klein bottle: cutting $\KK$ along a circle parallel to the boundary edges of its square model decomposes it into two Möbius bands.

:::

[[PR-BDH3V]]

::: {.proof title="Crosscap plus Klein bottle versus crosscap plus torus"}
The classification theorem [[T-NBARV]] gives $\RP^2\#\RP^2\#\RP^2 \cong \RP^2 \# \TT^2$, since both are closed and nonorientable with $\chi = -1$.
By [[PR-LIXWH]], $\KK\cong \RP^2\#\RP^2$, so
$$
\RP^2 \# \KK
\cong \RP^2 \# \RP^2 \# \RP^2
\cong \RP^2 \# \TT^2.
$$

:::

## Manifolds

::: {.fact title="Local homology"}
If $M$ is an $n$-manifold and $x\in M$ is an interior point, then by excision $H_k(M, M\sm\ts x) \cong H_k(\RR^n,\RR^n\sm\ts 0) \cong \tilde H_{k-1}(S^{n-1})$, which is $\ZZ$ for $k=n$ and $0$ otherwise.
A space with a point at which these local homology groups differ from those of every $\RR^n$ is not a manifold near that point.

:::

[[PR-ZCPDD]]

[[PR-LR35S]]

[[PR-4X6G2]]

[[PR-AZQ6S]]

[[PR-TU4G5]]

::: {.proof title="Odd-dimensional closed manifolds"}
Let $M$ be a closed $n$-manifold and work with $\FF_2$ coefficients, for which Poincaré duality holds without an orientability hypothesis: $H^k(M;\FF_2)\cong H_{n-k}(M;\FF_2)$.
Since $H^k(M;\FF_2)\cong\Hom(H_k(M;\FF_2),\FF_2)$, the Betti numbers $b_k\coloneqq\dim_{\FF_2} H_k(M;\FF_2)$ satisfy $b_k=b_{n-k}$, and $\chi(M)=\sum_k(-1)^kb_k$ for any field of coefficients.
Then
$$
\chi(M)
= \sum_{k=0}^n (-1)^k b_{n-k}
= (-1)^n \sum_{j=0}^n (-1)^{j} b_{j}
= (-1)^n \chi(M),
$$
so if $n$ is odd then $\chi(M)=0$.

:::

[[PR-3FB24]]

[[PR-BQKHS]]

[[T-QNYSB]]

### 3-manifolds and knot complements

::: {.fact}
Every complex manifold is canonically oriented by its complex structure.

:::

[[PR-UL3KL]]

[[PR-6HORN]]

::: {.proof title="Knot complements"}
By Alexander's theorem, $S^3\sm K$ is irreducible, and its fundamental group is infinite since its abelianization $H_1(S^3\sm K)\cong\ZZ$.
By the sphere theorem, an irreducible orientable $3$-manifold has $\pi_2=0$; its universal cover is then a noncompact simply connected $3$-manifold with $H_2=H_3=0$, hence contractible by the Hurewicz and Whitehead theorems.
So $\pi_j(S^3\sm K)=0$ for $j\geq 2$, and $S^3\sm K$ is a $K(\pi,1)$.

For the wedge, $\RR^3\sm K \cong (S^3\sm K)\sm\ts{\infty}$.
The space $S^3\sm K$ deformation retracts onto the compact manifold $C\coloneqq S^3\sm\nu(K)$ with torus boundary, and a compact $3$-manifold with nonempty boundary deformation retracts onto a $2$-dimensional spine missing a chosen interior point.
Removing that point therefore gives a space deformation retracting onto the spine together with a small sphere around the point and an arc joining them, so
$$
\RR^3\sm K
\homotopic
(S^3\sm K) \vee S^2.
$$

For the homology statement, assume $X$ is orientable and let $K\subseteq X$ be nullhomologous, with tubular neighborhood $\nu(K)$, complement $C\coloneqq X\sm\nu(K)$, meridian $\mu$, and a longitude $\lambda$ on $\del\nu(K)\cong T^2$ bounding a Seifert surface $S$ for $K$.
Intersection number with $S$ gives a homomorphism $\varphi\colon H_1(C)\to\ZZ$ with $\varphi(\mu)=1$, so $H_1(C)\cong\ZZ\mu\oplus\ker\varphi$, and $\lambda=0$ in $H_1(C)$.
In the Mayer--Vietoris sequence for $X = C\cup\nu(K)$,
$$
H_1(T^2)\to H_1(C)\oplus H_1(\nu(K))\to H_1(X)\to 0,
$$
the first map sends $\mu\mapsto(\mu,0)$ and $\lambda\mapsto(0,1)$, so $H_1(X)\cong H_1(C)/\ZZ\mu\cong\ker\varphi$, and
$$
H_1\bigl(X\sm\nu(K)\bigr)
\cong
H_1(X)\oplus\ZZ.
$$

:::

[[PR-WCHFF]]

::: {.proof}
$S^3\sm K$ is path connected, so $H_0\cong\ZZ$, and $H_1\cong\ZZ$ by [[PR-6HORN]] with $X=S^3$.
In the Mayer--Vietoris sequence for $S^3 = \nu(K) \cup C$ with $C\coloneqq S^3\sm\nu(K)\homotopic S^3\sm K$, $\nu(K) \homotopic S^1$, and $C\cap\nu(K)\homotopic T^2$,
$$
H_3(S^3)\to H_2(T^2)\to H_2(C)\oplus H_2(\nu(K))\to H_2(S^3)=0,
$$
the map $H_3(S^3)\cong\ZZ\to H_2(T^2)\cong\ZZ$ is an isomorphism, so $H_2(C)=0$.
Since $S^3\sm K$ is a connected noncompact $3$-manifold, $H_k(S^3\sm K)=0$ for $k\geq 3$.

:::
