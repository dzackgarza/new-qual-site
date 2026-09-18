---
schema: qual/card@1
id: P-AGH77CONEDEGDROP
kind: problem
title: The cone over $Y$ from a nonsingular point has dimension $r+1$ and smaller degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Cones
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.7 and its induction hint in Hartshorne, together with Proposition I.7.6 and Theorem I.7.7. The proof treats the join as the image of an irreducible incidence variety and uses smoothness at P to rule out the cone-point degeneracy. For the degree drop it uses the characteristic-independent blowup/projection computation, avoiding an unstated fixed-point Bertini theorem in the hinted hyperplane argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a variety of dimension $r$ and degree $d > 1$ in $\PP^n$.
Let $P \in Y$ be a nonsingular point.
Define $X$ to be the closure of the union of all lines $PQ$, where $Q \in Y$ and $Q \neq P$.

(a) Show that $X$ is a variety of dimension $r + 1$.

(b) Show that $\deg X < d$.

*Hint for part 2:* Use induction on $\dim Y$.
:::

::: {.solution}
For a reduced projective algebraic set $W\subseteq\PP^n$ and a point $P\in W$, write
$$
J_P(W)=\overline{\bigcup_{Q\in W\setminus\{P\}}\overline{PQ}}
$$
for the join of $P$ with $W$.
Thus the variety in the problem is $X=J_P(Y)$.

<1>1. The join $X$ is irreducible and has dimension at most $r+1$.

::: {.proof}
Consider the incidence set
$$
I^\circ
=\{(Q,R)\in (Y\setminus\{P\})\times\PP^n:R\in\overline{PQ}\}.
$$
Over $Y\setminus\{P\}$ its first projection has fibres projective lines.
On an affine chart containing $P$, the line through $P$ and $Q$ is parametrized algebraically by one projective parameter, so $I^\circ$ is locally a product with $\PP^1$.
Hence $I^\circ$ is irreducible of dimension $r+1$.

The second projection has image equal to the union of the secant lines in the definition of $X$.
The closure of the image of an irreducible variety is irreducible, so $X$ is irreducible.
Since $I^\circ\to X$ is dominant,
$$
\dim X\le r+1.
$$
:::

<1>2. The equality $X=Y$ would force $Y$ to be a linear variety.

::: {.proof}
Assume $X=Y$.
Then for every $Q\in Y\setminus\{P\}$ the whole line $\overline{PQ}$ lies in $Y$.
Its tangent direction at $P$ is therefore contained in the projective tangent space $T_PY$.
Consequently every point $Q\in Y$ belongs to the linear subspace $T_PY\subseteq\PP^n$.

Because $P$ is nonsingular and $\dim Y=r$, the projective tangent space has dimension $r$.
Thus
$$
Y\subseteq T_PY\cong\PP^r.
$$
Both are irreducible closed subsets of dimension $r$, so $Y=T_PY$.
Hence $Y$ is linear.
:::

<1>3. The variety $X$ has dimension
$$
\boxed{\dim X=r+1}.
$$

::: {.proof}
We have $Y\subseteq X$, so $\dim X\ge r$.
If equality held, irreducibility of both $Y$ and $X$ and the inclusion $Y\subseteq X$ would imply $X=Y$.
Step <1>2 would then make $Y$ linear, hence of degree one by [[P-AGH76DEGONELINEAR|Exercise I.7.6]], contradicting $d>1$.
Therefore $\dim X>r$.
Together with step <1>1 this gives $\dim X=r+1$, proving part (a).
:::

<1>4. Projection from $P$ exhibits $X$ as the cone over an $r$-dimensional projective variety $Z$, and
$$
\deg X=\deg Z.
$$

::: {.proof}
Choose homogeneous coordinates with
$$
P=[1:0:\cdots:0]
$$
and let $H_0=V(x_0)\cong\PP^{n-1}$.
Projection from $P$ is the rational map
$$
\rho:Y\dashrightarrow H_0,
\qquad
[x_0:x_1:\cdots:x_n]\longmapsto[x_1:\cdots:x_n].
$$
Let $Z$ be the closure of its image.
Every line through $P$ and a point of $Y\setminus\{P\}$ meets $H_0$ at the corresponding projected point, so $X$ is exactly the projective cone over $Z$ with vertex $P$.
Step <1>3 gives $\dim X=r+1$, hence $\dim Z=r$.

Let $B$ be the homogeneous coordinate ring of $Z$ in $H_0$.
The homogeneous ideal of the cone $X$ is the same ideal, viewed in the larger polynomial ring with the extra variable $x_0$.
Thus
$$
S(X)\cong B[x_0].
$$
If
$$
P_Z(m)=\frac{\deg Z}{r!}m^r+O(m^{r-1}),
$$
then
$$
\dim_k S(X)_m
=\sum_{j=0}^m\dim_k B_j
=\frac{\deg Z}{(r+1)!}m^{r+1}+O(m^r).
$$
Therefore $\deg X=\deg Z$.
:::

<1>5. Blowing up the smooth point $P$ resolves the projection $\rho$ to a generically finite morphism
$$
\widetilde\rho:\widetilde Y=\Bl_PY\longrightarrow Z.
$$
If $E$ is the exceptional divisor and $H$ is the hyperplane class on $Y$, then
$$
\widetilde\rho^*\OO_Z(1)\cong\OO_{\widetilde Y}(\beta^*H-E),
$$
where $\beta:\widetilde Y\to Y$ is the blowup map.

::: {.proof}
The rational projection is defined by the $n$ linear forms $x_1,\ldots,x_n$, all of which vanish at $P$ to order one.
The [[D-SCHBLOWUP|blowup]] makes the inverse image of the ideal $(x_1,\ldots,x_n)$ invertible, so by its universal property the rational map extends to a morphism
$$
\widetilde\rho:\widetilde Y\to\PP^{n-1}
$$
whose image is $Z$.
Since both $\widetilde Y$ and $Z$ have dimension $r$, this dominant morphism is generically finite; let its degree be
$$
\delta=[K(Y):K(Z)]\ge1.
$$

The pullback of a hyperplane of $Z$ is the strict transform of a hyperplane of $\PP^n$ through $P$.
Such a strict transform has divisor class $\beta^*H-E$, because the original hyperplane has multiplicity one at the smooth point $P$.
This gives the displayed line-bundle identity.
:::

<1>6. The top self-intersection of the divisor $\beta^*H-E$ is
$$
(\beta^*H-E)^r=d-1.
$$

::: {.proof}
The top self-intersection of $H$ on the projective variety $Y$ is its degree:
$$
H^r=d.
$$
Because $P$ is nonsingular of dimension $r$, the exceptional divisor is
$$
E\cong\PP^{r-1},
$$
and its normal bundle in the blowup is $\OO_E(-1)$.
Thus
$$
E^r
=\deg c_1(\OO_E(E))^{r-1}
=\deg c_1(\OO_{\PP^{r-1}}(-1))^{r-1}
=(-1)^{r-1}.
$$

For $1\le i\le r-1$, the mixed intersection
$$
(\beta^*H)^{r-i}E^i
$$
vanishes, because $\beta^*\OO_Y(H)|_E$ is trivial: the map $E\to Y$ is constant with image $P$.
Expanding gives
$$
(\beta^*H-E)^r
=H^r+(-1)^rE^r
=d-1.
$$
:::

<1>7. The projection degree satisfies
$$
\delta\deg Z=d-1.
$$

::: {.proof}
For a generically finite morphism of degree $\delta$ between $r$-dimensional projective varieties, the top self-intersection of the pullback of a hyperplane is $\delta$ times the degree of the target.
Indeed, intersect $Z$ with $r$ sufficiently general hyperplanes.
The resulting zero-dimensional intersection has total length $\deg Z$.
Over the dense open locus where $\widetilde\rho$ is finite of degree $\delta$, its inverse image has total length $\delta\deg Z$; this inverse image is precisely the intersection of the $r$ pulled-back hyperplanes on $\widetilde Y$.
Therefore
$$
(\widetilde\rho^*\OO_Z(1))^r=\delta\deg Z.
$$
Step <1>5 identifies the left side with $(\beta^*H-E)^r$, which step <1>6 evaluates as $d-1$.
Hence
$$
\delta\deg Z=d-1.
$$
:::

<1>8. The degree of the variety in the problem satisfies
$$
\boxed{\deg X<d}.
$$

::: {.proof}
By steps <1>4 and <1>7,
$$
\deg X=\deg Z=\frac{d-1}{\delta}\le d-1<d,
$$
proving part (b).
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove part (a), and steps <1>4--<1>8 prove part (b).
:::
:::
