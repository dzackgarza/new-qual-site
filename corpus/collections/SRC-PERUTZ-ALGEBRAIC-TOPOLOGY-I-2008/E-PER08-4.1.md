---
schema: qual/card@1
id: E-PER08-4.1
kind: problem
title: Fundamental groups of connected sums and realization of finitely presented groups
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 4.1 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the two van Kampen computations for connected sums and codimension-three surgery, including the normal-closure effect of each relator surgery.
---

::: {.problem}
An $n$-dimensional manifold is a Hausdorff space covered by open sets homeomorphic to $\mathbb R^n$.
Let $X_1$ and $X_2$ be connected $n$-manifolds.
Form their connected sum by choosing embeddings $i_j:D^n\to X_j$, putting $D'=\tfrac12D^n$, and identifying $i_1(x)$ with $i_2(x)$ for $x\in\partial D'=S^{n-1}$ after removing the two copies of $\operatorname{int}D'$.

1. Prove that if $n>2$, then
   \[
   \pi_1(X_1\#X_2)\cong \pi_1(X_1)*\pi_1(X_2).
   \]

2. Let $X$ be an iterated connected sum of $r$ copies of $S^1\times S^{n-1}$, with $n\ge3$.
   Compute $\pi_1(X)$.

3. Given a finitely presented group
   \[
   G=\langle g_1,\dots,g_k\mid r_1,\dots,r_\ell\rangle,
   \]
   construct a connected compact $4$-manifold $M$ with $\pi_1(M)\cong G$.

For the last part, the source suggests starting with the case of no relations and using
\[
\partial(S^1\times D^3)=S^1\times S^2=\partial(D^2\times S^2).
\]
:::

::: {.solution}
We use van Kampen throughout, replacing closed pieces by small open collars when needed.

<1>1. Removing the interior of the summing ball does not change the fundamental group when $n>2$.
::: {.proof}
For $j=1,2$, set
\[
Y_j=X_j\setminus i_j(\operatorname{int}D').
\]
Recover $X_j$ from $Y_j$ by gluing back an $n$-ball. The intersection of the two pieces is homotopy equivalent to
\[
S^{n-1}.
\]
Since $n>2$, the sphere $S^{n-1}$ is simply connected. The direct proof for $S^2$ extends verbatim to all spheres of dimension at least $2$: homotope a loop to finitely many geodesic arcs, choose a point missed by those arcs, and use stereographic projection to contract the loop.

The $n$-ball is also simply connected. Van Kampen therefore gives
\[
\pi_1(X_j)\cong\pi_1(Y_j).
\]
:::

<1>2. The connected-sum gluing gives a free product.
::: {.proof}
The connected sum is
\[
X_1\#X_2=Y_1\cup_{S^{n-1}}Y_2.
\]
Its two pieces meet in the gluing sphere, which is path connected and simply connected because $n>2$. Van Kampen identifies its fundamental group with the pushout
\[
\pi_1(Y_1)*_{\pi_1(S^{n-1})}\pi_1(Y_2).
\]
Since
\[
\pi_1(S^{n-1})=1,
\]
this pushout is the ordinary free product. Using <1>1,
\[
\boxed{
\pi_1(X_1\#X_2)
\cong
\pi_1(X_1)*\pi_1(X_2)
}.
\]
:::

<1>3. An iterated connected sum of $r$ copies of $S^1\times S^{n-1}$ has free fundamental group $F_r$.
::: {.proof}
A loop in a product is a pair of loops, and homotopies are coordinatewise, so
\[
\pi_1(A\times B,(a,b))
\cong
\pi_1(A,a)\times\pi_1(B,b).
\]
For $n\ge3$,
\[
\pi_1(S^{n-1})=1,
\]
hence
\[
\pi_1(S^1\times S^{n-1})
\cong
\pi_1(S^1)
\cong
\mathbb Z.
\]
Applying <1>2 repeatedly gives
\[
\pi_1\left(\#^r(S^1\times S^{n-1})\right)
\cong
\underbrace{\mathbb Z*\cdots*\mathbb Z}_{r\text{ factors}}
=F_r.
\]
:::

<1>4. Realize the generators by a closed compact $4$-manifold with free fundamental group.
::: {.proof}
Start with
\[
M_0=\#^k(S^1\times S^3).
\]
This is a connected compact smooth $4$-manifold. By <1>3,
\[
\pi_1(M_0)\cong F_k,
\]
and we choose the isomorphism so that the $k$ standard circle factors represent the free generators
\[
g_1,\dots,g_k.
\]
:::

<1>5. Represent the relators by disjoint embedded circles with product tubular neighborhoods.
::: {.proof}
For each relator $r_j\in F_k=\pi_1(M_0)$, choose a smooth loop representing its conjugacy class. Because the ambient dimension is $4$, general position allows the finitely many loops to be perturbed to pairwise disjoint embedded circles: one-dimensional submanifolds generically have neither self-intersections nor mutual intersections in dimension $4$.

The manifold $M_0$ is orientable. The normal bundle of an oriented embedded circle in an oriented $4$-manifold is an oriented real rank-$3$ bundle over $S^1$. Such a bundle is trivial, since oriented rank-$3$ bundles over $S^1$ are classified by
\[
[S^1,BSO(3)]=\pi_1(BSO(3))=\pi_0(SO(3))=0.
\]
Thus each relator circle has a tubular neighborhood
\[
N_j\cong S^1\times D^3,
\]
and the neighborhoods may be chosen pairwise disjoint.
:::

<1>6. Surgery on one relator quotients the fundamental group by its normal closure.
::: {.proof}
Let $M$ be the current $4$-manifold, let $C\subset M$ be one chosen relator circle, and let
\[
N\cong S^1\times D^3
\]
be its tubular neighborhood. Put
\[
Y=M\setminus\operatorname{int}N.
\]

First reconstruct $M$ as
\[
M=Y\cup_{S^1\times S^2}(S^1\times D^3).
\]
The inclusion
\[
S^1\times S^2\hookrightarrow S^1\times D^3
\]
induces an isomorphism on $\pi_1$, both groups being $\mathbb Z$ generated by the $S^1$ factor. Van Kampen therefore identifies
\[
\pi_1(Y)\xrightarrow{\cong}\pi_1(M).
\]
Under this identification, the image of the boundary generator is the element represented by $C$.

Now perform surgery by replacing $S^1\times D^3$ with $D^2\times S^2$:
\[
M'=Y\cup_{S^1\times S^2}(D^2\times S^2).
\]
Since
\[
\pi_1(D^2\times S^2)=1,
\]
van Kampen gives the pushout
\[
\pi_1(M')
\cong
\pi_1(Y)*_{\mathbb Z}1
\cong
\pi_1(M)/\!\langle\!\langle[C]\rangle\!\rangle,
\]
where $\langle\!\langle[C]\rangle\!\rangle$ is the normal closure of the relator represented by $C$.
:::

<1>7. Perform the surgeries for all relators.
::: {.proof}
Because the tubular neighborhoods $N_1,\dots,N_\ell$ are disjoint, perform the surgery of <1>6 on each relator circle. The resulting space $M$ is again a connected compact smooth $4$-manifold: each step removes $S^1\times\operatorname{int}D^3$ and glues in the compact manifold $D^2\times S^2$ along their common boundary $S^1\times S^2$.

Successively applying <1>6 gives
\[
\pi_1(M)
\cong
F_k/\!\langle\!\langle r_1,\dots,r_\ell\rangle\!\rangle.
\]
By the given presentation, the right-hand side is $G$. Hence
\[
\boxed{\pi_1(M)\cong G}.
\]
:::
:::
