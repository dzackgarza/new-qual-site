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

# Theorems: Algebraic Topology

## General Homotopies

:::{.fact title="Contracting Spaces in Products"}
\[
X\cross \RR^n \homotopic X \cross \pt \cong X
.\]

:::

:::{.fact title="$\pi_0, H_0$ detect path components"}
$\pi_0(X)$ is the set of path components of $X$, while $H_0(X;\ZZ)$ is the free
abelian group on those path components.  Thus if $X$ has finitely many path components,
$\operatorname{rank}H_0(X;\ZZ)=|\pi_0(X)|$.

:::

[[T-2YTCZ]]

:::{.proof}
The linear homotopy. Supposing $X$ is convex, for any two points $x,y\in X$, the line $tx + (1-t)y$ is contained in $X$ for every $t\in[0,1]$.
So let $f, g: Z \into X$ be any continuous functions into $X$. Then define $H: Z \cross I \into X$ by $H(z,t) = tf(z) + (1-t)g(z)$, the linear homotopy between $f,g$. By convexity, the image is contained in $X$ for every $t,z$, so this is a homotopy between $f,g$.

:::

## Fundamental Group

### Definition

[[D-YD6DH]]

:::{.remark title="a summary"}
Elements of the fundamental group are *homotopy classes of loops*, and every continuous map between spaces induces a homomorphism on fundamental groups.

:::

### Conjugacy in $\pi_{1}$

- See [@Hat02, prop. 1.19, p. 28].
- See the proof that $\pi_1$ is a group in [@Hat02].
- See change of basepoint map

### Calculating $\pi_1$ 

[[PR-HQE2T]]

[[PR-FG4DK]]

[[T-BTPU4]]

:::{.proof title="Sketch"}
\envlist

- Construct a map going backwards
- Show it is surjective
  - "There and back" paths
- Show it is injective
  - Divide $I\times I$ into a grid

:::

:::{.example title="Pushing out with van Kampen"}
$A = \ZZ/4\ZZ = \gens{x \suchthat x^4}, B = \ZZ/6\ZZ = \gens{y \suchthat x^6}, Z = \ZZ/2\ZZ = \gens{z \suchthat z^2}$.
Then we can identify $Z$ as a subgroup of $A, B$ using $\iota_{A}(z) = x^2$ and $\iota_{B}(z) = y^3$.
So $$A\ast_{Z} B = \gens{x, y \suchthat x^4, y^6, x^2y^{-3}}$$.

:::

[[PR-3APOT]]

:::{.proof}
By van Kampen, this is equivalent to the amalgamated product over $\pi_1(x_0) = 1$, which is just a free product.

:::

### Facts

:::{.fact}
$H_{1}$ is the abelianization of $\pi_{1}$.

:::

[[PR-OO3DH]]

:::{.proof title="sketch"}
\envlist

- A loop in \( X \cross Y \) is a continuous map \( \gamma : I \mapsvia{} X \cross Y \) given by \( \gamma (t) = (f(t), g(t) \) in components.
- $\gamma$ being continuous in the product topology is equivalent to $f, g$ being continuous maps to $X, Y$ respectively.
- Similarly a homotopy $F: I^2 \to X \cross Y$ is equivalent to a pair of homotopies $f_t, g_t$ of the corresponding loops.
- So the map $[ \gamma ] \mapsto ([f], [g])$ is the desired bijection.

:::

[[PR-EWJMJ]]

:::{.proof}
$\Rightarrow$: Suppose $X$ is simply connected. Then every loop in $X$ contracts to a point, so if $\alpha$ is a loop in $X$, $[\alpha] = [\id_{x_{0}}]$, the identity element of $\pi_{1}(X)$. But then there is only one element in in this group.

$\Leftarrow$: Suppose $\pi_{1}(X) = 0$. Then there is just one element in the fundamental group, the identity element, so if $\alpha$ is a loop in $X$ then $[\alpha] = [\id_{x_{0}}]$. So there is a homotopy taking $\alpha$ to the constant map, which is a contraction of $\alpha$ to a point.

:::

:::{.fact}
For a finite connected graph $G$ and a maximal tree $T\subseteq G$,
\[
\pi_1(G)\cong F_n,
\qquad
n=|E(G\setminus T)|=1-\chi(G),
\]
where $F_n$ is the free group of rank $n$.  Equivalently,
$G\homotopic\bigvee^n S^1$, and hence $H_1(G;\ZZ)\cong\ZZ^n$.

:::

## General Homotopy Theory

[[T-SDEOY]]

:::{.warnings}
Individual maps may not work: take $S^2 \cross \RP^3$ and $S^3 \cross \RP^2$ which have isomorphic homotopy but not homology.

:::

[[T-GL7E6]]

[[T-I2X3M]]

:::{.example title="Applications of cellular approximation"}
\envlist

- $\pi_k(S^n)=0$ for $k<n$.
- By cellular approximation, every element of $\pi_n(X)$ has a representative with image in the $n$-skeleton $X^{(n)}$.
  The inclusion $X^{(n+1)}\hookrightarrow X$ induces an isomorphism on $\pi_n$.

:::

[[T-HZUM7]]

:::{.fact title="Higher homotopy groups: quick facts"}
\envlist

- $\pi_{i\geq 2}(X)$ is always abelian.

	* $X$ simply connected $\implies \pi_{k}(X) \cong H_{k}(X)$ up to and including the first nonvanishing $H_{k}$

* $\pi_{k} \bigvee X \neq \prod \pi_{k} X$ (counterexample: $S^1 \vee S^2$)
  * Nice case: $\pi_{1}\bigvee X = \ast \pi_{1} X$ by Van Kampen.

* $\pi_{i}(\hat X) \cong \pi_{i}(X)$ for $i\geq 2$ whenever $\hat X \surjects X$ is a universal cover.

* $\pi_{i}(S^n) = 0$ for $i < n$, while $\pi_{n}(S^n) = \ZZ$.
  Higher groups need not vanish; for example $\pi_3(S^2)=\ZZ$.

* $S^n / S^k \homotopic S^n \vee \Sigma S^{k}$
  * $\Sigma S^n = S^{n+1}$

* Homotopy groups preserve products:
  \[
  \pi_k\qty{\prod_\alpha X_\alpha}\cong\prod_\alpha\pi_k(X_\alpha).
  \]
  Fibrations are controlled by the long exact sequence of homotopy groups.

- If $\pi=\langle S\mid R\rangle$, the presentation complex obtained from $\bigvee_{s\in S}S^1$ by attaching one $2$-cell for each relation has fundamental group $\pi$.
  It is not generally a $K(\pi,1)$; higher-dimensional cells may be required to kill its higher homotopy groups.

:::
