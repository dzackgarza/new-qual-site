---
schema: qual/card@1
id: P-AGH315AFFPRODUCT
kind: problem
title: Products of affine varieties and the tensor product of coordinate rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Products
  - Coordinate Rings
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all four parts and the fiberwise irreducibility hint with Hartshorne I.3.15. The proof makes the hinted sets X_i visibly closed by coefficient expansion in A(Y), then uses the same linear-independence argument to identify the product ideal without assuming tensor-product reducedness.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked irreducibility, the coordinate-ring kernel, the categorical universal property, and the dimension calculation against published solutions and the affine dimension theorem.'
---

::: {.problem}
Let $X \subseteq \AA^n$ and $Y \subseteq \AA^m$ be affine varieties.

(a) Show that $X \times Y \subseteq \AA^{n+m}$ with its induced topology is irreducible.
The affine variety $X \times Y$ is called the **product** of $X$ and $Y$.
Note that its topology is in general not the product topology.

(b) Show that $A(X \times Y) \cong A(X) \tensor_k A(Y)$.

(c) Show that $X \times Y$ is a product in the category of varieties, that is:

- the projections $X \times Y \to X$ and $X \times Y \to Y$ are morphisms, and

- given a variety $Z$ and morphisms $Z \to X$ and $Z \to Y$, there is a unique morphism $Z \to X \times Y$ commuting with the projections.

(d) Show that $\dim (X \times Y) = \dim X + \dim Y$.
:::

::: {.hint}
For (a), suppose $X \times Y = Z_1 \union Z_2$ with each $Z_i$ closed.
Let $X_i = \theset{ x \in X \st \theset{x} \times Y \subseteq Z_i }$.
Show that $X = X_1 \union X_2$ with $X_1, X_2$ closed, so $X = X_1$ or $X = X_2$, and hence $X \times Y = Z_1$ or $Z_2$.
:::

::: {.solution}
Write affine coordinates on $\AA^{n+m}$ as $(x_1,\ldots,x_n,y_1,\ldots,y_m)$.

::: pf

::: {.pf-step #s1}

If $Z\subseteq X\times Y$ is closed, then
$$
X_Z=\{x\in X:\{x\}\times Y\subseteq Z\}
$$
is closed in $X$.

::: pf-proof

Choose finitely many polynomials $F_1,\ldots,F_r\in k[x_1,\ldots,x_n,y_1,\ldots,y_m]$ whose common zero set on $X\times Y$ is $Z$.
Fix one $F=F_\ell$.
Its image in
$$
k[x_1,\ldots,x_n]\tensor_k A(Y)
$$
is a finite sum
$$
\sum_{j=1}^N a_j(x)e_j,
$$
where the $e_j\in A(Y)$ may be chosen $k$-linearly independent.
For a point $x\in X$, the polynomial $F(x,-)$ vanishes at every point of $Y$ exactly when its class in $A(Y)$ is zero, which by linear independence is equivalent to
$$
a_1(x)=\cdots=a_N(x)=0.
$$
Thus the condition that $F$ vanish on the whole fiber $\{x\}\times Y$ cuts out a closed subset of $X$.
Intersecting these closed subsets for $F_1,\ldots,F_r$ gives $X_Z$.

:::

:::

::: {.pf-step #s2}

The subset $X\times Y\subseteq\AA^{n+m}$ is irreducible, proving (a).

::: pf-proof

Suppose
$$
X\times Y=Z_1\cup Z_2
$$
with $Z_1,Z_2$ closed, and form $X_i=X_{Z_i}$ as in step [](#s1){.pf-ref}.
For each fixed $x\in X$, the fiber $\{x\}\times Y$ is isomorphic to the irreducible variety $Y$.
It is the union of the two closed subsets
$$
Z_1\cap(\{x\}\times Y),
\qquad
Z_2\cap(\{x\}\times Y),
$$
so it is contained in one of the $Z_i$.
Hence $X=X_1\cup X_2$.

Step [](#s1){.pf-ref} makes $X_1$ and $X_2$ closed in the irreducible variety $X$.
Thus $X=X_1$ or $X=X_2$.
If, say, $X=X_1$, every fiber lies in $Z_1$, so $X\times Y=Z_1$.
This is exactly irreducibility.

:::

:::

::: {.pf-step #s3}

The natural homomorphism
$$
A(X)\tensor_k A(Y)\longrightarrow A(X\times Y)
$$
is an isomorphism, proving (b).

::: pf-proof

Let
$$
S=k[x_1,\ldots,x_n,y_1,\ldots,y_m].
$$
The quotient map
$$
S\longrightarrow A(X)\tensor_k A(Y)
$$
has kernel
$$
I(X)S+I(Y)S.
$$
It therefore suffices to show that this kernel is exactly $I(X\times Y)$.

Every element of $I(X)S+I(Y)S$ vanishes on $X\times Y$.
Conversely, let $F\in I(X\times Y)$ and write its image in the tensor product as
$$
\overline F=\sum_{j=1}^N a_j\tensor b_j
$$
with $b_1,\ldots,b_N\in A(Y)$ $k$-linearly independent.
For each $x\in X$, vanishing of $F$ on $\{x\}\times Y$ says
$$
\sum_j a_j(x)b_j=0
$$
in $A(Y)$.
Linear independence gives $a_j(x)=0$ for every $j$ and every $x\in X$.
Each $a_j$ is therefore the zero element of $A(X)$, so $\overline F=0$.
Thus
$$
I(X\times Y)=I(X)S+I(Y)S,
$$
and taking quotients gives the asserted isomorphism.

:::

:::

::: {.pf-step #s4}

The coordinate projections are morphisms, and the usual pairing of two morphisms gives the required universal morphism.

::: pf-proof

The first projection
$$
\pi_X:X\times Y\to X
$$
is given by the coordinate functions $x_1,\ldots,x_n$, and the second by $y_1,\ldots,y_m$; hence both are morphisms.

Given morphisms $f:Z\to X$ and $g:Z\to Y$, define
$$
h:Z\longrightarrow X\times Y,
\qquad
h(z)=(f(z),g(z)).
$$
Locally on $Z$, the coordinate functions of $f$ and $g$ are regular, so all $n+m$ coordinate functions of $h$ are regular.
Thus $h$ is a morphism, and by construction
$$
\pi_X\circ h=f,
\qquad
\pi_Y\circ h=g.
$$
Any map satisfying these two equations must send $z$ to $(f(z),g(z))$, so $h$ is unique.
This proves (c).

:::

:::

::: {.pf-step #s5}

The dimension satisfies
$$
\dim(X\times Y)=\dim X+\dim Y.
$$

::: pf-proof

Put $A=A(X)$ and $B=A(Y)$.
By step [](#s3){.pf-ref},
$$
A(X\times Y)=A\tensor_k B,
$$
which is a domain by step [](#s2){.pf-ref}.

Choose Noether normalizations
$$
k[u_1,\ldots,u_r]\subseteq A,
\qquad
k[v_1,\ldots,v_s]\subseteq B,
$$
with $A$ and $B$ integral over the indicated polynomial rings.
Here
$$
r=\dim X,
\qquad
s=\dim Y.
$$
Because tensoring injections of $k$-vector spaces preserves injectivity, the tensor product of the two polynomial subrings embeds as
$$
k[u_1,\ldots,u_r,v_1,\ldots,v_s]
\subseteq A\tensor_k B.
$$
The latter ring is integral over this polynomial subring: generators coming from $A$ and from $B$ satisfy the same monic equations after tensoring.
Integral extensions preserve Krull dimension [@AM18, Chapter 5], so
$$
\dim(A\tensor_k B)=r+s=\dim X+\dim Y.
$$
This proves (d).

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove parts (a)--(d), respectively.

:::

:::

:::
