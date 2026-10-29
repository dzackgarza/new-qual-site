---
order: 202
topics:
- Homotopy Equivalence
- Homotopy
- Homotopy Type
- Higher Homotopy Groups
- Homotopy Groups
- Hurewicz Theorem

---

# Theorems: algebraic topology

## General homotopies

::: {.fact title="Contractible factors of products"}
For any space $X$ and $n\geq 0$, the projection is a [[D-HFR32|homotopy equivalence]]
$$
X\cross \RR^n \homotopic X \cross \pt \cong X.
$$

:::

::: {.fact title="$\pi_0$ and $H_0$ detect path components"}
$\pi_0(X)$ is the set of path components of $X$, and $H_0(X;\ZZ)$ is the free abelian group on $\pi_0(X)$.
If $X$ has finitely many path components, then $\operatorname{rank}H_0(X;\ZZ)=\abs{\pi_0(X)}$.

:::

[[T-2YTCZ]]

## Fundamental group

### Definition

[[D-EBNUE]]

::: {.remark}
Elements of $\pi_1(X,x_0)$ are homotopy classes of loops at $x_0$ rel endpoints, and a continuous map $f\colon (X,x_0)\to(Y,y_0)$ induces a homomorphism $f_*\colon\pi_1(X,x_0)\to\pi_1(Y,y_0)$, $[\gamma]\mapsto[f\circ\gamma]$.

:::

### Calculating $\pi_1$

[[PR-HQE2T]]

[[PR-FG4DK]]

[[T-BTPU4]]

::: {.example title="An amalgamated product"}
Let $A = \ZZ/4 = \generators{x \suchthat x^4}$, $B = \ZZ/6 = \generators{y \suchthat y^6}$, and $Z = \ZZ/2 = \generators{z \suchthat z^2}$, with injections $\iota_{A}(z) = x^2$ and $\iota_{B}(z) = y^3$.
Then
$$
A\ast_{Z} B = \generators{x, y \suchthat x^4, y^6, x^2y^{-3}}.
$$

:::

[[PR-3APOT]]

### Facts

::: {.fact}
For path-connected $X$, the Hurewicz map induces an isomorphism $\pi_1(X)^{\mathrm{ab}}\cong H_1(X)$.

:::

[[PR-OO3DH]]

[[PR-EWJMJ]]

::: {.fact}
For a finite connected graph $G$ and a maximal tree $T\subseteq G$,
$$
\pi_1(G)\cong F_n,
\qquad
n=\abs{E(G)\sm E(T)}=1-\chi(G),
$$
where $F_n$ is the free group of rank $n$ on the edges not in $T$.
Collapsing $T$ gives a homotopy equivalence $G\homotopic\bigvee^n S^1$, so $H_1(G;\ZZ)\cong\ZZ^n$.

:::

## General homotopy theory

[[T-SDEOY]]

::: {.example title="Isomorphic homotopy groups without a weak equivalence"}
$S^2 \cross \RP^3$ and $S^3 \cross \RP^2$ have universal cover $S^2\cross S^3$ and fundamental group $\ZZ/2$, so their homotopy groups are isomorphic in every degree.
They are not homotopy equivalent, since by the Künneth theorem $H_2(S^2 \cross \RP^3)\cong\ZZ$ while $H_2(S^3 \cross \RP^2)=0$.
Whitehead's theorem concludes that a map $f\colon X\to Y$ of connected CW complexes is a homotopy equivalence when $f_*\colon\pi_n(X)\to\pi_n(Y)$ is an isomorphism for every $n$; no map $S^2\cross\RP^3\to S^3\cross\RP^2$ induces these isomorphisms.

:::

[[T-GL7E6]]

[[T-I2X3M]]

::: {.example title="Applications of cellular approximation"}
\envlist

- $\pi_k(S^n)=0$ for $k<n$: with the CW structure $e^0\union e^n$, a map $S^k\to S^n$ is homotopic to a cellular map, whose image lies in the $k$-skeleton, a point.

- For a CW complex $X$, every element of $\pi_n(X)$ has a representative with image in the $n$-skeleton $X^{(n)}$, and the inclusion $X^{(n+1)}\injects X$ induces an isomorphism on $\pi_n$.

:::

[[T-HZUM7]]

::: {.fact title="Higher homotopy groups"}
\envlist

- For $i\geq 2$, $\pi_{i}(X)$ is abelian.

- If $X$ is simply connected and $n\geq 2$ is the least integer with $H_n(X)\neq 0$, then $\pi_k(X)=0$ for $k<n$ and $\pi_n(X)\cong H_n(X)$.

- Homotopy groups of a wedge are not in general the products of the homotopy groups: $\pi_2(S^1\vee S^2)\cong\ZZ[t,\inverseof{t}]$, the homology $H_2$ of the universal cover, a line with a sphere attached at each integer, while $\pi_2(S^1)\times\pi_2(S^2)\cong\ZZ$.

- For a covering map $\hat X \to X$, the induced maps $\pi_{i}(\hat X) \to \pi_{i}(X)$ are isomorphisms for $i\geq 2$.

- $\pi_{i}(S^n) = 0$ for $i < n$, and $\pi_{n}(S^n) \cong \ZZ$; higher groups need not vanish, for example $\pi_3(S^2)\cong\ZZ$.

- For $0\leq k<n$, $S^n / S^k \homotopic S^n \vee \Sigma S^{k}$, and $\Sigma S^k \cong S^{k+1}$.

- For path-connected spaces $X_\alpha$, the projections induce $\pi_k\qty{\prod_\alpha X_\alpha}\cong\prod_\alpha\pi_k(X_\alpha)$.

- A fibration $F\to E\to B$ with $B$ path connected induces a long exact sequence $\cdots\to\pi_k(F)\to\pi_k(E)\to\pi_k(B)\to\pi_{k-1}(F)\to\cdots$.

- For a presentation $\pi=\generators{S\suchthat R}$, the presentation complex obtained from $\bigvee_{s\in S}S^1$ by attaching one $2$-cell along each relation has fundamental group $\pi$.
  It need not be a $K(\pi,1)$: attaching cells of dimension at least $3$ to kill its higher homotopy groups produces a $K(\pi,1)$.

:::
