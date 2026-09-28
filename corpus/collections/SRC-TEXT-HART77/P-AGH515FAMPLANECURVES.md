---
schema: qual/card@1
id: P-AGH515FAMPLANECURVES
kind: problem
title: The space $\PP^N$ of plane curves of degree $d$ and its nonsingular locus
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Families Of Varieties
  - Zariski Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.5.15, Elimination Theorem I.5.7A, and Exercises I.5.5, I.5.8, and I.5.9 in the Hartshorne source. The proof describes the fibres of the coefficient-space correspondence, cuts out the discriminant by elimination, and uses the explicit nonsingular degree-d curves already proved in I.5.5 to show the complement is nonempty.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
A homogeneous polynomial $f$ of degree $d$ in three variables $x, y, z$ has $\binom{d+2}{2}$ coefficients.
Let these coefficients represent a point in $\PP^N$, where
$$
N = \binom{d+2}{2} - 1 = \frac{1}{2} d(d+3).
$$

(a) Show that this gives a correspondence between points of $\PP^N$ and algebraic sets in $\PP^2$ that can be defined by an equation of degree $d$.
   The correspondence is one-to-one except in some cases where $f$ has a multiple factor.

(b) Show that under this correspondence the irreducible nonsingular curves of degree $d$ correspond one-to-one to the points of a nonempty Zariski-open subset of $\PP^N$.

*Hint:* Use elimination theory (5.7A) applied to the homogeneous polynomials $\frac{\partial f}{\partial x_0}, \ldots, \frac{\partial f}{\partial x_n}$, and use (Ex. 5.5, 5.8, 5.9).
:::

::: {.solution}
Let
$$
V_d=k[x,y,z]_d,
$$
so $\dim_kV_d=\binom{d+2}{2}=N+1$ and the parameter space of nonzero degree-$d$ forms up to scalar is $\PP(V_d)\cong\PP^N$.

<1>1. A point $[f]\in\PP(V_d)$ determines the algebraic set $Z(f)\subseteq\PP^2$, and every algebraic set cut out by one degree-$d$ equation occurs in this way.

::: {.proof}
Replacing $f$ by a nonzero scalar multiple does not change its zero set, so the assignment is well-defined on projective coefficient space.
Conversely, by definition, an algebraic set in $\PP^2$ which can be defined by one homogeneous equation of degree $d$ is $Z(f)$ for some nonzero $f\in V_d$, hence comes from the point $[f]$.
:::

<1>2. If $f$ is square-free, then $[f]$ is the unique point of $\PP(V_d)$ defining $Z(f)$; nonuniqueness can occur only when repeated irreducible factors are present.

::: {.proof}
Factor
$$
f=c\prod_{i=1}^r p_i^{a_i},
$$
where the $p_i$ are pairwise nonassociate irreducible homogeneous polynomials.
Over the algebraically closed field $k$, the projective Nullstellensatz says that the reduced homogeneous ideal of $Z(f)$ has the same irreducible hypersurface factors $p_i$.
Thus if another degree-$d$ form $g$ satisfies $Z(g)=Z(f)$, then
$$
g=c'\prod_{i=1}^r p_i^{b_i}
$$
with all $b_i\ge1$.

If $f$ is square-free, then every $a_i=1$ and
$$
d=\sum_i\deg p_i.
$$
Since $g$ also has degree $d$ and every $b_i\ge1$,
$$
d=\sum_i b_i\deg p_i\ge\sum_i\deg p_i=d,
$$
so equality forces every $b_i=1$.
Thus $g$ is a scalar multiple of $f$ and $[g]=[f]$, even if no square-freeness hypothesis was imposed on $g$.
Hence every failure of injectivity requires repeated factors.
Such failures do occur: the distinct cubic forms $x^2y$ and $xy^2$ define the same union of the two coordinate lines.
This proves part (a).
:::

<1>3. The set of coefficient points whose degree-$d$ form has a singular projective zero is Zariski closed in $\PP^N$.

::: {.proof}
Write the universal degree-$d$ form as
$$
F_A(x,y,z)=\sum_{i+j+k=d}A_{ijk}x^iy^jz^k,
$$
where the $A_{ijk}$ are homogeneous coordinates on the coefficient space.
A point $P=[x:y:z]\in\PP^2$ is singular on $Z(F_A)$ exactly when
$$
F_A(P)=\frac{\partial F_A}{\partial x}(P)
=\frac{\partial F_A}{\partial y}(P)
=\frac{\partial F_A}{\partial z}(P)=0.
$$
Including $F_A$ itself is necessary in characteristics dividing $d$, where Euler's relation does not recover $F_A(P)=0$ from the partial derivatives alone.

Apply the elimination theorem to these four homogeneous polynomials in $x,y,z$ with indeterminate coefficient coordinates $A_{ijk}$.
It produces homogeneous polynomial conditions in the $A_{ijk}$ whose simultaneous vanishing is equivalent to the existence of a common nonzero solution $(x,y,z)$.
Therefore the singular forms constitute a projective algebraic subset
$$
\Delta_d\subseteq\PP^N.
$$
Its complement $U_d=\PP^N\setminus\Delta_d$ is Zariski open.
:::

<1>4. The open set $U_d$ is nonempty for every $d>0$, and every point of $U_d$ defines an irreducible nonsingular plane curve of degree $d$.

::: {.proof}
The card [[P-AGH55NONSINGDEGD|a nonsingular plane curve of each degree in each characteristic]] gives an explicit degree-$d$ homogeneous form whose three partial derivatives and defining equation have no common projective zero.
Its coefficient point therefore belongs to $U_d$, so $U_d$ is nonempty.

If $[f]\in U_d$, then $Z(f)$ is nonsingular by construction.
It is also irreducible.
Indeed, if $f=gh$ with $g,h$ nonconstant homogeneous forms, then the two positive-degree plane curves $Z(g)$ and $Z(h)$ meet in $\PP^2$.
At any point of intersection,
$$
\partial(gh)=g\,\partial h+h\,\partial g=0
$$
for every first partial derivative, and $gh=0$ as well, producing a singular point of $Z(f)$.
This contradicts $[f]\in U_d$.
Thus $f$ is irreducible and defines an irreducible nonsingular curve.
:::

<1>5. Irreducible nonsingular degree-$d$ curves correspond one-to-one with the points of $U_d$.

::: {.proof}
Step <1>4 shows that every point of $U_d$ gives such a curve.
Conversely, the defining form of an irreducible nonsingular degree-$d$ plane curve has no singular projective zero, so its coefficient point lies in $U_d$.

If two points of $U_d$ define the same curve, their defining forms are irreducible and hence square-free.
Step <1>2 then shows that the two forms differ by a scalar, so the two points of $\PP^N$ are equal.
This gives the required bijection and proves part (b).
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove the coefficient-space correspondence and its possible nonuniqueness, while steps <1>3--<1>5 identify the irreducible nonsingular curves with the nonempty Zariski-open set $U_d$.
:::
:::
