---
schema: qual/card@1
id: P-AGH423DUALCURVE
kind: problem
title: The dual curve, its class $d(d-1)$, and the counts of inflection points and bitangents
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Embeddings
  - Linear Systems
relations: []
review: draft
---

::: problem
Let $X$ be a curve of degree $d$ in $\PP^2$.
For each point $P \in X$, let $T_P(X)$ be the tangent line to $X$ at $P$ (I, Ex.
7.3). Considering $T_P(X)$ as a point of the dual projective plane $(\PP^2)^*$, the map $P \mapsto T_P(X)$ gives a morphism of $X$ to its **dual curve** $X^*$ in $(\PP^2)^*$ (I, Ex.
7.3).

Note that even though $X$ is nonsingular, $X^*$ in general will have singularities.
We assume $\characteristic k=0$ below.

a. Fix a line $L \subseteq \PP^2$ which is not tangent to $X$.
Define a morphism $\varphi: X \to L$ by $\varphi(P)=T_P(X) \intersect L$, for each point $P \in X$.
Show that $\varphi$ is ramified at $P$ if and only if either (1) $P \in L$, or (2) $P$ is an inflection point of $X$, which means that the intersection multiplicity (I, Ex.
5.4) of $T_P(X)$ with $X$ at $P$ is $\geq 3$.
Conclude that $X$ has only finitely many inflection points.

b. A line of $\PP^2$ is a **multiple tangent** of $X$ if it is tangent to $X$ at more than one point.
It is a **bitangent** if it is tangent to $X$ at exactly two points.
If $L$ is a multiple tangent of $X$, tangent to $X$ at the points $P_1, \ldots, P_r$, and if none of the $P_i$ is an inflection point, show that the corresponding point of the dual curve $X^*$ is an ordinary $r$-fold point, which means a point of multiplicity $r$ with distinct tangent directions (I, Ex.
5.3). Conclude that $X$ has only finitely many multiple tangents.

c. Let $O \in \PP^2$ be a point which is not on $X$, nor on any inflectional or multiple tangent of $X$.
Let $L$ be a line not containing $O$.
Let $\psi: X \to L$ be the morphism defined by projection from $O$.
Show that $\psi$ is ramified at a point $P \in X$ if and only if the line $OP$ is tangent to $X$ at $P$, and in that case the ramification index is 2. Use Hurwitz's theorem and (I, Ex.
7.2) to conclude that there are exactly $d(d-1)$ tangents of $X$ passing through $O$.
Hence the degree of the dual curve (sometimes called the **class** of $X$) is $d(d-1)$.

d. Show that for all but a finite number of points of $X$, a point $O$ of $X$ lies on exactly $(d+1)(d-2)$ tangents of $X$, not counting the tangent at $O$.

e. Show that the degree of the morphism $\varphi$ of a. is $d(d-1)$.
Conclude that if $d \geq 2$, then $X$ has $3d(d-2)$ inflection points, properly counted.
(If $T_P(X)$ has intersection multiplicity $r$ with $X$ at $P$, then $P$ should be counted $r-2$ times as an inflection point.
If $r=3$ we call it an ordinary inflection point.)
Show that an ordinary inflection point of $X$ corresponds to an ordinary cusp of the dual curve $X^*$.

f. Now let $X$ be a plane curve of degree $d \geq 2$, and assume that the dual curve $X^*$ has only nodes and ordinary cusps as singularities (which should be true for sufficiently general $X$). Then show that $X$ has exactly $\frac{1}{2} d(d-2)(d-3)(d+3)$ bitangents.
Hint: Show that $X$ is the normalization of $X^*$.
Then calculate $p_a(X^*)$ two ways: once as a plane curve of degree $d(d-1)$, and once using (Ex.
1.8).

g. For example, a plane cubic curve has exactly 9 inflection points, all ordinary.
The line joining any two of them intersects the curve in a third one.

h. A plane quartic curve has exactly 28 bitangents.
(This holds even if the curve has a tangent with four-fold contact, in which case the dual curve $X^*$ has a tacnode.)
:::
