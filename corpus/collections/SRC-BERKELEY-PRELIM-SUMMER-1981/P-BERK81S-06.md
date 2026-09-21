---
schema: qual/card@1
id: P-BERK81S-06
kind: problem
title: Symmetric nonidentity rotations in $SO(3)$ form a projective plane
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Real projective space is S^2 modulo the antipodal involution, hence
    compact, with quotient metric min(||u-v||,||u+v||). SO(3) is a closed
    bounded subset of M_3(R), hence compact. A symmetric element of SO(3)
    squares to I; if it is not I, its eigenvalues are 1,-1,-1. Thus it is
    the half-turn 2P_L-I about its unique +1 eigenspace L. The map
    [u]↦2uu^T-I is therefore a continuous bijection RP^2→Q, hence a
    homeomorphism.
---

::: {.problem}
Let $SO(3)$ be the group of orthogonal transformations of $\mathbb R^3$ of determinant $1$.
Let
\[
Q=\{A\in SO(3):A^T=A,\ A\ne I\},
\]
and let $\mathbb{RP}^2$ denote the space of lines through the origin in $\mathbb R^3$.

1. Show that $\mathbb{RP}^2$ and $SO(3)$ are compact metric spaces in their usual topologies.

2. Show that $\mathbb{RP}^2$ and $Q$ are homeomorphic.
:::

::: {.solution}
<1>1. The group $SO(3)$ is a closed subset of
$$
M_3(\RR)\cong\RR^9.
$$

::: {.proof}
One has
$$
SO(3)
=
\{A\in M_3(\RR):A^TA=I,\ \det A=1\}.
$$
The maps
$$
A\longmapsto A^TA
$$
and
$$
A\longmapsto\det A
$$
are continuous. Therefore $SO(3)$ is the inverse image of the closed set
$$
\{I\}\times\{1\}
$$
under the continuous map
$$
A\longmapsto(A^TA,\det A).
$$
Hence $SO(3)$ is closed.
:::

<1>2. The group $SO(3)$ is bounded in $M_3(\RR)$.

::: {.proof}
If $A=(a_{ij})\in SO(3)$, each column is a Euclidean unit vector because
$$
A^TA=I.
$$
Thus
$$
\abs{a_{ij}}\leq1
$$
for every $i,j$. Hence $SO(3)$ is contained in the bounded cube
$$
[-1,1]^9.
$$
:::

<1>3. The space $SO(3)$ is a compact metric space in its usual topology.

::: {.proof}
By steps <1>1--<1>2, $SO(3)$ is closed and bounded in the finite
dimensional Euclidean space $M_3(\RR)\cong\RR^9$. The Heine--Borel theorem
therefore gives compactness. The Euclidean metric on $M_3(\RR)$ restricts
to a metric inducing the usual topology on $SO(3)$.
:::

<1>4. The real projective plane is the quotient
$$
\mathbb{RP}^2
\cong
S^2/(u\sim-u).
$$

::: {.proof}
Every line through the origin intersects the unit sphere in exactly two
antipodal points $u$ and $-u$. Thus sending a unit vector to the line it
spans identifies precisely antipodal pairs, giving the stated quotient.
:::

<1>5. The space $\mathbb{RP}^2$ is compact.

::: {.proof}
The sphere $S^2$ is compact, and the quotient map
$$
S^2\longrightarrow S^2/(u\sim-u)
$$
is continuous and surjective. A continuous image of a compact space is
compact. Step <1>4 identifies the quotient with $\mathbb{RP}^2$.
:::

<1>6. For lines $[u],[v]\in\mathbb{RP}^2$, represented by unit vectors
$u,v\in S^2$, define
$$
d([u],[v])
=
\min\{\norm{u-v},\norm{u+v}\}.
$$
This is a metric inducing the usual quotient topology on
$\mathbb{RP}^2$.

::: {.proof}
Replacing $u$ or $v$ by its negative interchanges the two displayed
quantities, so the minimum is well defined on lines.

The formula is the quotient metric for the action of the two-element group
$$
\{I,-I\}
$$
on $S^2$ by Euclidean isometries. Therefore it is a metric. Its metric
balls are exactly the images under the quotient map of antipodally
symmetric unions of sufficiently small spherical metric balls, so it
induces the quotient topology.
:::

<1>7. Consequently, $\mathbb{RP}^2$ is a compact metric space in its usual
topology.

::: {.proof}
Compactness is step <1>5 and metrizability by the usual projective
topology is step <1>6.
:::

<1>8. If $A\in Q$, then
$$
A^2=I.
$$

::: {.proof}
By definition, $A$ is orthogonal and symmetric. Orthogonality gives
$$
A^TA=I,
$$
while symmetry gives $A^T=A$. Hence
$$
A^2=I.
$$
:::

<1>9. Every $A\in Q$ has eigenvalues
$$
1,-1,-1,
$$
counted with multiplicity.

::: {.proof}
By step <1>8, every eigenvalue satisfies
$$
\lambda^2=1,
$$
so every eigenvalue is $\pm1$. Since $A\in SO(3)$,
$$
\det A=1.
$$
The number of eigenvalues equal to $-1$ is therefore even. Because
$A\neq I$, this number is not zero. In dimension three it must therefore
be exactly two.
:::

<1>10. For $A\in Q$, the eigenspace
$$
L_A=\ker(A-I)
$$
is a line, and
$$
A=2P_{L_A}-I,
$$
where $P_{L_A}$ is the orthogonal projection onto $L_A$.

::: {.proof}
By step <1>9, the eigenvalue $1$ has multiplicity one, so $L_A$ is
one-dimensional. Since $A$ is symmetric, eigenspaces for distinct
eigenvalues are orthogonal. Thus
$$
\RR^3=L_A\oplus L_A^\perp,
$$
and $A$ acts as $+I$ on $L_A$ and as $-I$ on $L_A^\perp$.

The operator $2P_{L_A}-I$ has exactly the same action on these two
orthogonal summands, so the operators are equal.
:::

<1>11. For a line $L=[u]\in\mathbb{RP}^2$, with $u$ a unit vector, define
$$
\Phi(L)=2uu^T-I.
$$
Then $\Phi(L)\in Q$.

::: {.proof}
The matrix
$$
uu^T
$$
is the orthogonal projection onto the line $\RR u$. Hence
$$
\Phi(L)=2P_L-I.
$$
It is symmetric. It acts as $+1$ on $L$ and as $-1$ on $L^\perp$, so it is
orthogonal, has determinant
$$
1\cdot(-1)^2=1,
$$
and is not the identity. Therefore $\Phi(L)\in Q$.

Replacing $u$ by $-u$ does not change $uu^T$, so the formula depends only
on the line $L$.
:::

<1>12. The map
$$
\Phi:\mathbb{RP}^2\longrightarrow Q
$$
is bijective.

::: {.proof}
For surjectivity, let $A\in Q$. Step <1>10 gives
$$
A=2P_{L_A}-I=\Phi(L_A).
$$

For injectivity, if
$$
\Phi(L)=\Phi(L'),
$$
then their $+1$ eigenspaces agree. By construction, the $+1$ eigenspace of
$\Phi(L)$ is exactly $L$, and similarly for $L'$. Hence $L=L'$.
:::

<1>13. The map $\Phi$ is continuous.

::: {.proof}
The map
$$
S^2\longrightarrow M_3(\RR),
\qquad
u\longmapsto2uu^T-I,
$$
is polynomial in the coordinates of $u$, hence continuous. It is invariant
under $u\mapsto-u$, so by the universal property of the quotient topology
it descends to a continuous map
$$
\Phi:\mathbb{RP}^2\longrightarrow Q.
$$
:::

<1>14. The map $\Phi$ is a homeomorphism:
$$
\boxed{
\mathbb{RP}^2\cong Q.
}
$$

::: {.proof}
By step <1>7, $\mathbb{RP}^2$ is compact. The space $Q$ is a subspace of
the metric space $SO(3)$, hence is Hausdorff. Steps <1>12--<1>13 show that
$\Phi$ is a continuous bijection from a compact space to a Hausdorff
space. Such a map is a homeomorphism.
:::

<1>15. Q.E.D.

::: {.proof}
Steps <1>3 and <1>7 prove part (1), while step <1>14 proves part (2).
:::
:::
