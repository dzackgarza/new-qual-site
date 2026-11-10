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

::: pf

::: {.pf-step #join-irreducible-dim-bound}
The join $X$ is irreducible and has dimension at most $r+1$.

::: pf-proof
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

:::

::: {.pf-step #join-equals-y-forces-linear}
The equality $X=Y$ would force $Y$ to be a linear variety.

::: pf-proof
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

:::

::: {.pf-step #join-dimension-r-plus-one}
The variety $X$ has dimension
$$
\boxed{\dim X=r+1}.
$$

::: pf-proof
We have $Y\subseteq X$, so $\dim X\ge r$.
If equality held, irreducibility of both $Y$ and $X$ and the inclusion $Y\subseteq X$ would imply $X=Y$.
Step [](#join-equals-y-forces-linear){.pf-ref} would then make $Y$ linear, hence of degree one by [[P-AGH76DEGONELINEAR|Exercise I.7.6]], contradicting $d>1$.
Therefore $\dim X>r$.
Together with step [](#join-irreducible-dim-bound){.pf-ref} this gives $\dim X=r+1$, proving part (a).
:::

:::

::: {.pf-step #cone-degree-equals-projection-degree}
Projection from $P$ exhibits $X$ as the cone over an $r$-dimensional projective variety $Z$, and
$$
\deg X=\deg Z.
$$

::: pf-proof
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
Step [](#join-dimension-r-plus-one){.pf-ref} gives $\dim X=r+1$, hence $\dim Z=r$.

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

:::

::: {.pf-step #blowup-resolves-projection}
Blowing up the smooth point $P$ resolves the projection $\rho$ to a generically finite morphism
$$
\widetilde\rho:\widetilde Y=\Bl_PY\longrightarrow Z.
$$
If $E$ is the exceptional divisor and $H$ is the hyperplane class on $Y$, then
$$
\widetilde\rho^*\OO_Z(1)\cong\OO_{\widetilde Y}(\beta^*H-E),
$$
where $\beta:\widetilde Y\to Y$ is the blowup map.

::: pf-proof
The rational projection is given by the restrictions to $Y$ of the $n$ linear forms $x_1,\ldots,x_n$, which are global sections of the invertible sheaf $\OO_Y(1)$ whose common zero locus on $Y$ is exactly $\{P\}$.
On the chart $D_+(x_0)$ the section $x_0$ trivializes $\OO_Y(1)$, so there the base ideal of these sections, in the sense of [@Har77, Example II.7.17.3], is generated by the restrictions of $x_1/x_0,\ldots,x_n/x_0$.
These are the affine coordinates of $P$ in that chart, so the ideal they generate on $Y$ is the inverse image of the ideal of $P$ in $\PP^n$: it is the ideal sheaf $\mathcal I$ of the point $P$ on $Y$, whose stalk at the smooth point $P$ is the maximal ideal $\mathfrak m=\mathfrak m_{P,Y}$ of the regular local ring $\OO_{Y,P}$.
The individual generators need not vanish to order one at $P$: on the smooth conic $x_0x_2=x_1^2$ at $P=[1:0:0]$, the chart $x_0=1$ gives $x_1=t$ and $x_2=t^2$, so $x_2/x_0$ vanishes to order two there, while the ideal $(t,t^2)=(t)$ is still the maximal ideal.
What is used below is this ideal, not the order of vanishing of any single generator.

The [[D-SCHBLOWUP|blowup]] $\beta:\widetilde Y\to Y$ is the blowing-up of the ideal sheaf $\mathcal I$ of the point.
By [@Har77, Proposition II.7.13(a)] the inverse image ideal
$$
\mathcal J=\beta^{-1}\mathcal I\cdot\OO_{\widetilde Y}
$$
is invertible, and by [@Har77, Example II.7.17.3] the sections $\beta^*x_1,\ldots,\beta^*x_n$ of $\beta^*\OO_Y(1)$ generate the invertible subsheaf
$$
\mathcal L'=\mathcal J\cdot\beta^*\OO_Y(1)\subseteq\beta^*\OO_Y(1),
$$
which, together with those sections, defines the morphism
$$
\widetilde\rho:\widetilde Y\longrightarrow\PP^{n-1}
$$
extending $\rho$, with $\widetilde\rho^*\OO_{\PP^{n-1}}(1)\cong\mathcal L'$ [@Har77, Theorem II.7.1].
The image of the irreducible projective variety $\widetilde Y$ is closed, contains the dense subset $\rho(Y\setminus\{P\})$ of $Z$, and has dimension at most $r=\dim Z$; hence it is $Z$.
Since both $\widetilde Y$ and $Z$ have dimension $r$, this dominant morphism is generically finite; let its degree be
$$
\delta=[K(Y):K(Z)]\ge1.
$$

It remains to identify $\mathcal J$ with $\OO_{\widetilde Y}(-E)$.
Let $t_1,\ldots,t_r$ be local parameters at the smooth point $P$, meaning elements of $\mathfrak m$ whose images form a basis of $\mathfrak m/\mathfrak m^2$; they generate $\mathfrak m$ by Nakayama's lemma, so $\mathcal I$ is generated by $t_1,\ldots,t_r$ on a neighborhood of $P$.
On the blowup chart in which $t_i=t_1y_i$ for $i\ge2$, the inverse image ideal is
$$
\mathcal J=(t_1,\ldots,t_r)\cdot\OO=(t_1),
$$
and the exceptional divisor meets this chart in $\{t_1=0\}$: the coordinate ring of that intersection is the chart ring modulo $t_1$, namely $\OO_{Y,P}/(t_1,\ldots,t_r)[y_2,\ldots,y_r]\cong k[y_2,\ldots,y_r]$, so it is reduced and irreducible.
The invertible ideal $\mathcal J=(t_1)$ therefore cuts the reduced irreducible divisor $E$ on this chart, and since the effective Cartier divisor defined by $\mathcal J$ has support $\beta^{-1}(P)=E$ [@Har77, Proposition II.7.13(b)], that divisor is $E$ itself with multiplicity one:
$$
\mathcal J=\OO_{\widetilde Y}(-E).
$$
Consistently, $E\cong\PP^{r-1}$, as used again in step [](#exceptional-self-intersection){.pf-ref}.
Consequently
$$
\widetilde\rho^*\OO_Z(1)\cong\mathcal L'=\mathcal J\cdot\beta^*\OO_Y(1)\cong\OO_{\widetilde Y}(\beta^*H-E),
$$
which is the displayed line-bundle identity.
:::

:::

::: {.pf-step #exceptional-self-intersection}
The top self-intersection of the divisor $\beta^*H-E$ is
$$
(\beta^*H-E)^r=d-1.
$$

::: pf-proof
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
vanishes, because $\beta^*\OO_Y(H)\restrict_E$ is trivial: the map $E\to Y$ is constant with image $P$.
Expanding gives
$$
(\beta^*H-E)^r
=H^r+(-1)^rE^r
=d-1.
$$
:::

:::

::: {.pf-step #projection-degree-formula}
The projection degree satisfies
$$
\delta\deg Z=d-1.
$$

::: pf-proof
For a generically finite morphism of degree $\delta$ between $r$-dimensional projective varieties, the top self-intersection of the pullback of a hyperplane is $\delta$ times the degree of the target.
Indeed, intersect $Z$ with $r$ sufficiently general hyperplanes.
The resulting zero-dimensional intersection has total length $\deg Z$.
Over the dense open locus where $\widetilde\rho$ is finite of degree $\delta$, its inverse image has total length $\delta\deg Z$; this inverse image is precisely the intersection of the $r$ pulled-back hyperplanes on $\widetilde Y$.
Therefore
$$
(\widetilde\rho^*\OO_Z(1))^r=\delta\deg Z.
$$
Step [](#blowup-resolves-projection){.pf-ref} identifies the left side with $(\beta^*H-E)^r$, which step [](#exceptional-self-intersection){.pf-ref} evaluates as $d-1$.
Hence
$$
\delta\deg Z=d-1.
$$
:::

:::

::: {.pf-step #degree-drop-conclusion}
The degree of the variety in the problem satisfies
$$
\boxed{\deg X<d}.
$$

::: pf-proof
By steps [](#cone-degree-equals-projection-degree){.pf-ref} and [](#projection-degree-formula){.pf-ref},
$$
\deg X=\deg Z=\frac{d-1}{\delta}\le d-1<d,
$$
proving part (b).
:::

:::

::: pf-qed
Steps [](#join-irreducible-dim-bound){.pf-ref}, [](#join-equals-y-forces-linear){.pf-ref} and [](#join-dimension-r-plus-one){.pf-ref} prove part (a), and steps [](#cone-degree-equals-projection-degree){.pf-ref}, [](#blowup-resolves-projection){.pf-ref}, [](#exceptional-self-intersection){.pf-ref}, [](#projection-degree-formula){.pf-ref} and [](#degree-drop-conclusion){.pf-ref} prove part (b).
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 7.7, PDF pp. 9--10: (a) "$X$ is birational to the cone on $Y$, which will show that $X$ is irreducible and of dimension $r+1$", by mapping each line $PQ$ to the corresponding line of the cone and writing down a rational inverse; (b) "if $Y$ has dimension $0$ then it is a union of $d$ points and $X$ is a union of at most $d-1$ lines, so the result is true in this case. If $Y$ has dimension $>0$ choose a generic hyperplane $H$ containing $P$, which can be chosen to intersect $Y$ transversely at generic points of the intersection as $Y$ is nonsingular at $P$. The intersection of $Y$ and $H$ has degree at most $d$ by 7.7. The intersection of $X$ with $H$ is the union of the set of lines joining $P$ and $H\cap Y$ which has degree less than $d$ by induction on $\dim(Y)$. Again by 7.7, the degree of $X$ is equal to the degree of $X\cap H$ as all components of $X\cap H$ have multiplicity $1$ in the intersection (as $H$ is generic). Hence the degree of $X$ is less than that of $Y$", with the caveat "the intersection $X\cap H$ of an irreducible algebraic set $X$ with a generic hyperplane $H$ need not be irreducible! But see remark 7.9.1 on p.~245 of Hartshorne."
William Troiani, *Hartshorne Exercise Solutions* (October 2020), stops at §I.5 and gives no solution to 7.7.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.7.7, PDF p. 58: (a) the cone over $Y$ with a rational inverse, "note that the cone has dimension $r+1$"; (b) "if $\dim Y=0$, then $Y$ has $d$ points and $X$ has $d-1$ lines. If $\dim Y=r$ and $H$ is a hyperplane containing $P$ but not $Y$, then by Thm 7.7, 7.6b, $\deg X\cap H=\deg X$. By induction $\deg X\cap H\le\deg Y\cap H\le\deg Y=d$."
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.7.7, PDF p. 27: (a) "fix $P$ and consider the projection map to $\PP^1$. $X$ is parameterized by the fibers of this map, of which are same dimension and irreducible, so $X$ is a variety of $\dim r+1$"; (b) "for $\dim Y=0$, $Y$ consists of $d$ points, so $X$ is $d-1$ lines. Now suppose $\dim Y=r$. Choose a hyperplane $H$ through $P$ not containing $Y$ so that the intersection multiplicity along any component of $X\cap H$ is $1$. Then by Thm 7.7 and 7.6(b), $\deg X\cap H=\deg X$, and $\deg Y\cap H\le\deg Y=d$. $X\cap H$ is the cone over $Y\cap H$ so by induction, $\deg X\cap H\le\deg Y\cap H=d$. So $\deg X<d$."
All three take the induction on $\dim Y$ that the printed hint asks for. Egbert and Cutrone--Marshburn assert $\deg X\cap H=\deg X$ and $\deg X\cap H\le\deg Y\cap H$; Borcherds names the genericity these need, which is Bertini's theorem together with (III, 7.9.1 after II, 8.18) applied to $X$, and his argument also identifies $X\cap H$ with the join of $P$ and $H\cap Y$, which is what makes the induction hypothesis applicable to that section and is not proved either; his conclusion "less than that of $Y$" passes through that identification as well. No set proves the degree identity under a hyperplane section of $X$, which the induction requires. Part (b) is therefore recorded in COMPLAINTS.md as having no complete published solution. Steps [](#blowup-resolves-projection){.pf-ref} to [](#degree-drop-conclusion){.pf-ref} replace the induction by the blowup of $P$ and the resolved projection $\widetilde\rho:\widetilde Y\to Z$, whose degree $\delta$ satisfies $\delta\deg Z=(\beta^*H-E)^r=d-1$; part (a) is proved from the incidence variety and, for the inequality $\dim X>r$, from step [](#join-equals-y-forces-linear){.pf-ref} with I.7.6.
:::
