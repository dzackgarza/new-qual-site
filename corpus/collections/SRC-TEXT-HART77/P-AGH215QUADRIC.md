---
schema: qual/card@1
id: P-AGH215QUADRIC
kind: problem
title: The quadric surface $xy = zw$ in $\PP^3$ and its two rulings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Segre Embedding
  - Quadric Surfaces
  - Zariski Topology
relations:
- kind: uses
  target: P-AGH214SEGRE
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with the retained Hartshorne I.2.15 transcription. The proof gives explicit parametrizations of both ruling families and a closed diagonal conic whose inverse image is not closed in the product of the two cofinite Zariski topologies. The existing figure is preserved.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Compared the card's statement in full with the printed Exercise 2.15 (scan
    page 28 of the retained PDF), tails included: hypotheses, every lettered
    part and the closing clauses. Agrees, including the equation of Q and the
    two families.
---

::: {.problem}
Let $k$ be algebraically closed.
Consider the surface $Q$ in $\PP^3$ defined by $xy - zw = 0$; a \dfn{surface} is a variety of dimension $2$.

(a) Show that $Q$ is the Segre embedding of $\PP^1 \times \PP^1$ in $\PP^3$, for a suitable choice of coordinates.

(b) Show that $Q$ contains two families of lines $\theset{L_t}$ and $\theset{M_t}$, each parametrized by $t \in \PP^1$, with these properties: if $L_t \neq L_u$ then $L_t \intersect L_u = \emptyset$; if $M_t \neq M_u$ then $M_t \intersect M_u = \emptyset$; and $L_t \intersect M_u$ is a single point for all $t, u$.
A \dfn{line} is a linear variety of dimension $1$.

(c) Show that $Q$ contains curves other than these lines, and deduce that the Zariski topology on $Q$ is not homeomorphic via $\psi$ to the product topology on $\PP^1 \times \PP^1$, where each factor has its Zariski topology.

![The quadric surface $Q \subseteq \PP^3$ with the lines $L_0$ and $M_0$ of its two families.](../../../assets/algebraic-geometry/varieties/quadric-surface-in-p3-two-rulings.png){width=350px}
:::

::: {.solution}
Use the coordinate order $[x:y:z:w]$ on $\PP^3$ and the reordered Segre map
$$
\psi([a:b],[c:d])=[ac:bd:ad:bc].
$$
The topology in (c) is the topology on the classical sets of projective points over $k$.

::: pf

::: {.pf-step #image-of-psi-is-q}
The image of $\psi$ is exactly $Q$.

::: pf-proof
Substituting the four coordinates gives $(ac)(bd)-(ad)(bc)=0$, so the image lies in $Q$.
Conversely, a point $[x:y:z:w]$ of $Q$ defines a nonzero matrix
$$
\begin{pmatrix}x&z\\w&y\end{pmatrix}
$$
whose determinant is zero.
The nonzero-entry calculation in [[P-AGH214SEGRE]], step 2, expresses this matrix as a nonzero column $(a,b)^t$ times a nonzero row $(c,d)$.
It therefore has the four coordinates displayed for $\psi$.
Step 3 of that card proves uniqueness of the two projective factors, so $\psi$ is a bijection onto $Q$.
Its image is a projective variety by the same card.
The chart $x\ne0$ on $Q$ has coordinates $z/x,w/x$, with $y/x=(z/x)(w/x)$, and is an affine plane.
The other nonzero-entry charts have the same form, so $\dim Q=2$ by [[P-AGH27DIMPN]], step 1.
This proves (a).
:::

:::

::: {.pf-step #ruling-lines-construction}
The ruling lines in (b) are
$$
\boxed{L_{[a:b]}=\{[ac:bd:ad:bc]:[c:d]\in\PP^1\},\qquad
M_{[c:d]}=\{[ac:bd:ad:bc]:[a:b]\in\PP^1\}.}
$$

::: pf-proof
For fixed $[a:b]$, the vectors in the first parametrization have the form
$$
c(a,0,0,b)+d(0,b,a,0).
$$
The two displayed vectors are linearly independent, since $(a,b)\ne(0,0)$ and their nonzero coordinates lie in disjoint pairs of positions.
Their projectivized span is consequently a line by [[P-AGH211LINEAR]].
Similarly, for fixed $[c:d]$, the second parametrization is the projectivized span of the independent vectors $(c,0,d,0)$ and $(0,d,0,c)$.
All these lines lie in $Q$ by step [](#image-of-psi-is-q){.pf-ref}.

Under the bijection $\psi$, the first family is the image of the subsets $\{t\}\times\PP^1$, and the second is the image of $\PP^1\times\{u\}$.
Two distinct members of either family are therefore disjoint.
For every $t,u$, their intersection is precisely the one point $\psi(t,u)$.
This also proves that each family is parametrized without repetition by $\PP^1$.
:::

:::

::: {.pf-step #diagonal-curve-not-a-line}
The closed curve
$$
C=Q\cap Z(z-w)=\{[a^2:b^2:ab:ab]:[a:b]\in\PP^1\}
$$
is not a line.

::: pf-proof
In the coordinates of $\psi$, the extra equation $z=w$ is $ad=bc$.
For nonzero two-dimensional vectors, this determinant equation is equivalent to $[a:b]=[c:d]$.
Thus $C$ is precisely the image under $\psi$ of the diagonal of the set $\PP^1\times\PP^1$.
Its displayed parametrization is the quadratic Veronese embedding of $\PP^1$ in the plane $z=w$, by [[P-AGH212DUPLE]].
It is therefore a closed irreducible curve.
It contains the points
$$
[1:0:0:0],\qquad[0:1:0:0],\qquad[1:1:1:1],
$$
whose representative vectors are linearly independent.
A projective line is the projectivization of a two-dimensional vector space, so it cannot contain these three points.
Hence $C$ is a curve other than either ruling line, in every characteristic.
:::

:::

::: {.pf-step #product-topology-not-homeomorphism}
The product topology in (c) does not make $\psi$ a homeomorphism onto $Q$.

::: pf-proof
Every proper Zariski-closed subset of $\PP_k^1$ is finite.
Indeed, it is contained in the zero set of a nonzero homogeneous polynomial, whose zeros on either affine chart are zeros of a nonzero one-variable polynomial, apart from a possible missing endpoint.
Conversely, every finite subset is closed because points are closed.
The field $k$ is infinite, so the set of projective points is infinite and this topology is the cofinite topology.

Let $\Delta=\{(t,t):t\in\PP^1\}$.
Every nonempty basic open rectangle $A\times B$ in the product topology meets $\Delta$: both $A$ and $B$ have finite complement, so $A\cap B\ne\varnothing$.
Thus $\Delta$ is dense in the product topology.
It is a proper subset, since there are distinct projective points, and hence is not closed.

But step [](#diagonal-curve-not-a-line){.pf-ref} gives $\psi^{-1}(C)=\Delta$, whereas $C$ is Zariski-closed in $Q$.
Therefore $\psi$ from the product-topological space to $Q$ is not even continuous, and in particular is not a homeomorphism.
This proves (c).
:::

:::

::: pf-qed
Step [](#image-of-psi-is-q){.pf-ref} proves (a), step [](#ruling-lines-construction){.pf-ref} proves (b), and steps [](#diagonal-curve-not-a-line){.pf-ref} and [](#product-topology-not-homeomorphism){.pf-ref} prove both assertions in (c).
:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 2.15, PDF p. 3: (a) the image of $(a_0:a_1)\times(b_0:b_1)$ satisfies $xt-zw=0$ and is all of it as in 2.14; (b) the two families are point$\times$line and line$\times$point, with the line through a fixed $(a_0:a_1)$ described as the intersection of the two hyperplanes $a_1w=a_0y$ and $a_1x=a_0z$; (c) "The closed subset $x=y$ of $Q$ is not one of these lines", with no argument.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 2.15, PDF p. 8, proves only (a), that the kernel of the substitution is $(z_{00}z_{11}-z_{01}z_{10})$.
The proof above gives both rulings as explicit parametrized spans with the independence of the two spanning vectors checked, and for (c) it proves that $Q\cap Z(z-w)$, the image of the diagonal of $\PP^1\times\PP^1$, contains three points whose representatives are linearly independent and so cannot be a line, then shows the diagonal is dense but not closed in the product topology while its image is Zariski closed.
Agree with Borcherds; (c) is the part the published argument states without proof.
:::
