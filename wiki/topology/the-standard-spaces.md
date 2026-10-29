---
title: The standard spaces
order: 8
topics:
- Cell Complexes
- Surfaces
- Projective Spaces
- Spheres
- Suspension
- Suspensions
- Simply Connected
- Graphs

---

# The standard spaces

Definitions, fundamental groups, homology, cell structures, and cohomology rings of the spaces from which exam problems are built: spheres, tori, projective spaces, closed surfaces, wedges of spheres, and punctured spaces.
$F_m$ is the free group of rank $m$, and $D(k,X)$ is $X$ with $k$ points deleted, as in [Deleting points](#deleting-points).

| $X$ | $\pi_1$ | $H_*$ | Notes |
| --- | --- | --- | --- |
| $\RR^n$, $D^n$ | $1$ | $\ZZ$ in degree $0$ | contractible |
| $S^n$, $n\geq 2$ | $1$ | $\ZZ$ in degrees $0, n$ | simply connected, its own universal cover |
| $S^1$ | $\ZZ$ | $\ZZ, \ZZ$ | universal cover $\RR$ |
| $T^n$ | $\ZZ^n$ | $\ZZ^{\binom nk}$ in degree $k$ | universal cover $\RR^n$; product of circles |
| $\RP^n$, $n\geq 2$ | $\ZZ/2$ | $\ZZ, \ZZ/2, 0, \ZZ/2, \ldots$ | universal cover $S^n$; $H_n = \ZZ$ iff $n$ odd |
| $\CP^n$ | $1$ | $\ZZ$ in every even degree $\leq 2n$ | no odd cells, so all boundary maps vanish |
| Klein bottle $K$ | $\generators{a,b \st aba\inverseof{b}}$ | $\ZZ, \ZZ\oplus\ZZ/2, 0$ | non-orientable, so $H_2 = 0$ |
| $\Sigma_g$, genus $g$ | $\generators{a_i,b_i \st \prod[a_i,b_i]}$ | $\ZZ, \ZZ^{2g}, \ZZ$ | closed orientable |
| $N_k$, $k$ crosscaps | $\generators{a_i \st \prod a_i^2}$ | $\ZZ, \ZZ^{k-1}\oplus\ZZ/2, 0$ | closed non-orientable |
| $\bigvee_n S^1$ | free on $n$ | $\ZZ, \ZZ^n$ | $\pi_1$ free, homology free |
| $\bigvee_n S^2$ | $1$ | $\ZZ, 0, \ZZ^n$ |  |
| Möbius band | $\ZZ$ | $\ZZ, \ZZ$ | deformation retracts to its core circle |
| $S^1\times S^2$ | $\ZZ$ | $\ZZ, \ZZ, \ZZ, \ZZ$ |  |
| $D(k,\RR^n)$, $n\geq 2$ | $F_k$ if $n=2$; $1$ if $n\geq 3$ | $\ZZ$ in degree $0$, $\ZZ^k$ in degree $n-1$ | $\homotopic\bigvee_k S^{n-1}$ |
| $D(k,S^n)$, $n\geq 2$ | $F_{k-1}$ if $n=2$; $1$ if $n\geq 3$ | $\ZZ$ in degree $0$, $\ZZ^{k-1}$ in degree $n-1$ | $\homotopic\bigvee_{k-1} S^{n-1}$ |
| $D(k,T^2)$ | $F_{k+1}$ | $\ZZ, \ZZ^{k+1}$ | $\homotopic\bigvee_{k+1} S^1$ |

## Definitions

::: {.example title="Spheres and balls"}
For $n\geq 0$,
$$
\begin{aligned}
\DD^n &\coloneqq \theset{ \vector x \in \RR^{n} \st \norm{\vector x} \leq 1}, \\
\SS^n &\coloneqq \theset{ \vector x \in \RR^{n+1} \st \norm{\vector x} = 1} = \bd \DD^{n+1}.
\end{aligned}
$$
Outside this block the blackboard-bold is dropped, and $D^n\coloneqq\DD^n$, $S^n\coloneqq\SS^n$.

The sphere $S^n$ is an $n$-manifold, and
$$
S^n \cong D^n / \bd D^n \cong D^n \Disjoint_{\bd D^n} D^n,
$$
the quotient collapsing the boundary to a point and the union of two discs glued by the identity of their boundaries.

![The discs $\DD^1,\DD^2,\DD^3$ and their boundary spheres $\SS^0,\SS^1,\SS^2$](../../../assets/Topology/figures/image_2021-01-10-23-20-27.png)

:::

::: {.example title="Real projective space"}
For $n\geq 1$, $\RP^n$ is the quotient of $S^n$ by the antipodal identification $\vector x \sim -\vector x$; equivalently, it is the space of lines through $0$ in $\RR^{n+1}$.
The inclusions $\RP^n\injects\RP^{n+1}$ define $\RP^\infty \coloneqq \injectivelim_{n} \RP^n$.
The quotient map $S^n\to\RP^n$ is a $2$-sheeted covering map, a fiber bundle with fiber $S^0$:
$$
S^0 \to S^n \to \RP^n.
$$

:::

::: {.example title="Complex projective space"}
For $n\geq 1$, $\CP^n$ is the quotient of the unit sphere $S^{2n+1}\subseteq\CC^{n+1}$ by the action of $S^1\subseteq \CC^\times$ by scalar multiplication, $\vector z\sim\lambda\vector z$ for $\abs\lambda=1$; equivalently, it is the space of complex lines through $0$ in $\CC^{n+1}$.
The inclusions $\CP^n\injects\CP^{n+1}$ define $\CP^\infty \coloneqq \injectivelim_n \CP^n$.
The quotient map is a fiber bundle, the Hopf fibration when $n=1$:
$$
S^1 \to S^{2n+1} \to \CP^n.
$$

:::

::: {.example title="Tori"}
For $n\geq 1$, the $n$-torus is
$$
T^n \coloneqq \prod_{j=1}^n S^1.
$$

:::

::: {.example title="Grassmannians"}
The real Grassmannian $\Gr(k,\RR^n)$ is the space of $k$-dimensional linear subspaces of $\RR^n$, and $\Gr(k,\CC^n)$ is the space of complex $k$-dimensional subspaces of $\CC^n$.
In particular, $\RP^{n-1}=\Gr(1,\RR^n)$ and $\CP^{n-1}=\Gr(1,\CC^n)$.

:::

::: {.example title="Stiefel manifolds"}
The real Stiefel manifold $V_k(\RR^n)$ is the space of ordered orthonormal $k$-frames in $\RR^n$, topologized as a subspace of $(S^{n-1})^k$.
$V_1(\RR^n)=S^{n-1}$ and $V_n(\RR^n)=O(n)$.

:::

::: {.example title="Matrix groups"}
The following are topological groups, with the subspace topology from the space of matrices:

- the general linear group $\GL_n(\RR)$ and the special linear group $\SL_n(\RR)$;

- the orthogonal group $O(n)$ and the special orthogonal group $\SO(n)$;

- the unitary group $U(n)$ and the special unitary group $\SU(n)$ of complex unitary matrices of determinant $1$;

- the real symplectic group $\operatorname{Sp}(2n,\RR)$.

:::

::: {.example title="Eilenberg--MacLane spaces"}
For a group $G$ when $n=1$, or an abelian group $G$ when $n\geq2$, an [[D-MENR4|Eilenberg--MacLane space]] $K(G,n)$ is a path-connected space with
$$
\pi_{k}(K(G, n)) \cong
\begin{cases}
G & k=n, \\
0 & k\neq n.
\end{cases}
$$
Such a space exists as a CW complex, and any two CW complexes of type $K(G,n)$ are homotopy equivalent.

- $S^1$ is a $K(\ZZ, 1)$.

- $\CP^\infty$ is a $K(\ZZ, 2)$.

- $\RP^\infty$ is a $K(\ZZ/2, 1)$.

:::

::: {.example title="Moore spaces"}
For an abelian group $G$ and $n\geq 1$, a [[D-KC4BS|Moore space]] $M(G,n)$ is a CW complex with
$$
\tilde H_{k}(M(G,n);\ZZ) \cong
\begin{cases}
G & k=n, \\
0 & k\neq n,
\end{cases}
$$
simply connected when $n\geq 2$.
For $n\geq 2$ it is unique up to homotopy equivalence.

- $S^n$ is an $M(\ZZ, n)$.

- $\RP^2$ is an $M(\ZZ/2, 1)$.

- For $p\geq 2$, attaching an $(n+1)$-cell to $S^n$ by a map of degree $p$ gives an $M(\ZZ/p,n)$.

:::

::: {.fact title="Low-dimensional identifications"}
\envlist

- The Möbius band $\mcm$ deformation retracts onto its core circle, so $\mcm \homotopic S^1$.

- As a set, $\CP^n = \CC^n \Disjoint \CP^{n-1} = \coprod_{i=0}^n \CC^i$, which gives a CW structure with one cell in each even dimension $0,2,\ldots,2n$.

- For $0\leq k<n$ and the standard inclusion $S^k\subseteq S^n$, $S^n / S^k \homotopic S^n \vee S^{k+1}$.

:::

::: {.remark title="Exceptional homeomorphisms"}
$\RP^1 \cong S^1$, $\CP^1 \cong S^2$, and $\SO(3) \cong \RP^3$.

:::

## Deleting points

::: {.example title="Punctured spaces"}
For a space $X$ and $k\geq 1$ distinct points $x_1,\ldots,x_k\in X$, write $D(k, X)\coloneqq X \sm \theset{x_{1}, \ldots, x_{k}}$.
For $n\geq 2$,
$$
\begin{aligned}
D(k,\RR^n) &\homotopic \bigvee_{i=1}^k S^{n-1}, \\
D(k,S^n) &\homotopic \bigvee_{i=1}^{k-1} S^{n-1}, \\
D(k,T^2) &\homotopic \bigvee_{i=1}^{k+1} S^{1},
\end{aligned}
$$
where an empty wedge is a point.
The second follows from the first because $D(1,S^n)\cong\RR^n$ by stereographic projection.

:::

## Cell structures and cohomology

::: {.fact title="Cell structures and cohomology rings"}
In the cell column, $c_0 + c_1 x + c_2 x^2 + \cdots$ records a CW structure with $c_i$ cells of dimension $i$; for a space listed up to homotopy equivalence it records a CW complex of that homotopy type.
In the cohomology column $\abs{x}$ is the degree of a generator.

| $X$ | Cells | $H^*(X;\ZZ)$ |
| --- | --- | --- |
| $\RR^n$, $D^n$ | $1$ | $\ZZ$ |
| $D(k,\RR^n)$, $n\geq 2$ | $1+kx^{n-1}$ | $\ZZ$ in degree $0$, $\ZZ^k$ in degree $n-1$, zero products |
| $S^n$, $n\geq 1$ | $1+x^n$ | $\ZZ[x]/(x^2)$, $\abs x=n$ |
| $D(k,S^n)$, $n\geq 2$ | $1+(k-1)x^{n-1}$ | $\ZZ$ in degree $0$, $\ZZ^{k-1}$ in degree $n-1$, zero products |
| $T^n$ | $(1+x)^n$ | exterior algebra on $x_1,\ldots,x_n$, $\abs{x_i}=1$ |
| $D(k,T^2)$ | $1+(k+1)x$ | $\ZZ$, $\ZZ^{k+1}$, zero products |
| $\bigvee^n S^1$ | $1+nx$ | $\ZZ$, $\ZZ^n$, zero products |
| $\RP^n$, $n\geq 2$ even | $1+x+\cdots+x^n$ | $\ZZ$ in degree $0$, $\ZZ/2$ in even degrees $2,\ldots,n$ |
| $\RP^n$, $n\geq 3$ odd | $1+x+\cdots+x^n$ | $\ZZ$ in degrees $0,n$, $\ZZ/2$ in even degrees $2,\ldots,n-1$ |
| $\CP^n$ | $1+x^2+\cdots+x^{2n}$ | $\ZZ[x]/(x^{n+1})$, $\abs x=2$ |
| Möbius band | $1+x$ | $\ZZ[x]/(x^2)$, $\abs x=1$ |
| Klein bottle | $1+2x+x^2$ | $\ZZ$, $\ZZ$, $\ZZ/2$ |

With $\ZZ/2$ coefficients, $H^*(\RP^n;\ZZ/2)\cong\FF_2[a]/(a^{n+1})$ with $\abs a=1$.

:::

## Higher homotopy groups

::: {.fact title="Higher homotopy groups"}
\envlist

- A covering map induces isomorphisms on $\pi_k$ for $k\geq 2$, so $\pi_k(\RP^n)\cong\pi_k(S^n)$ for $k\geq 2$.

- $T^n$, the Klein bottle, and $\bigvee^n S^1$ have contractible universal covers ($\RR^n$, $\RR^2$, and a tree), so their $\pi_k$ vanish for $k\geq 2$.

- The long exact sequence of the fibration $S^1\to S^{2n+1}\to\CP^n$ gives $\pi_2(\CP^n)\cong\ZZ$ and $\pi_k(\CP^n)\cong\pi_k(S^{2n+1})$ for $k\geq 3$.

- $\RR^n$ and $D^n$ are contractible, so all their homotopy groups vanish.

:::

## Constructions

::: {.fact}
\envlist

- **Wedges.** For good pointed spaces, $\tilde H_*(X\vee Y) \cong \tilde H_*(X)\oplus\tilde H_*(Y)$, and if $X$ and $Y$ are CW complexes wedged at $0$-cells, $\pi_1(X\vee Y)\cong\pi_1(X)*\pi_1(Y)$ by van Kampen's theorem.

- **Products.** $\pi_1(X\times Y)\cong\pi_1(X)\times\pi_1(Y)$, and by the Künneth theorem for CW complexes
  $$
  H_n(X\times Y)\cong \bigoplus_{i+j=n} H_i(X)\tensor H_j(Y)\ \oplus \bigoplus_{i+j=n-1}\Tor(H_i(X),H_j(Y)).
  $$

- **Deleting a point.** If a closed $n$-manifold $M$ has a CW structure with a single $n$-cell, then $M$ minus a point in that cell deformation retracts onto the $(n-1)$-skeleton; a closed surface minus a point deformation retracts onto a wedge of circles.

- **Connected sums.** For closed $n$-manifolds with $n\geq 2$, the homology of $M\# N$ is computed by the Mayer--Vietoris sequence for the decomposition along the separating $S^{n-1}$; $\Sigma_g\#\Sigma_h\cong\Sigma_{g+h}$.

:::

## Spaces distinguished by one invariant

::: {.example title="$T^2$ and the Klein bottle"}
$H_1(T^2)\cong\ZZ^2$ and $H_1(K)\cong\ZZ\oplus\ZZ/2$, and $H_2(T^2)\cong\ZZ$ while $H_2(K)=0$.

:::

::: {.example title="$\RP^2$ and $S^2$"}
$\pi_1(\RP^2)\cong\ZZ/2$ and $\pi_1(S^2)=1$.

:::

::: {.example title="$\RP^3$ and $S^1\times S^2$"}
$\pi_1(\RP^3)\cong\ZZ/2$ and $\pi_1(S^1\times S^2)\cong\ZZ$; also $H_1(\RP^3)\cong\ZZ/2$ and $H_1(S^1\times S^2)\cong\ZZ$.

:::

::: {.example title="$S^1\vee S^1\vee S^2$ and $T^2$"}
Both have homology $\ZZ,\ZZ^2,\ZZ$, and $\pi_1(S^1\vee S^1\vee S^2)$ is free of rank $2$ while $\pi_1(T^2)\cong\ZZ^2$ is abelian, so they are not homotopy equivalent.

:::
