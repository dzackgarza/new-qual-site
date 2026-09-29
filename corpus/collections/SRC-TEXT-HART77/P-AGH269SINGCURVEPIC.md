---
schema: qual/card@1
id: P-AGH269SINGCURVEPIC
kind: problem
title: The Picard group of a singular curve via normalization
classification:
  areas:
  - algebraic-geometry
  topics:
  - Picard Groups
  - Singular Curves
  - Normalization
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts and the Cartier-divisor hint with the retained Hartshorne II.6.9 transcription. Made the source's integral-curve and algebraically closed field convention explicit. Independently proved divisor lifting and the local-unit kernel, and computed both cubic cases from a common local normalization in arbitrary characteristic.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Here we give another method of calculating the Picard group of a singular curve.
Let $k$ be algebraically closed and let $X$ be a projective integral curve over $k$.
Let $\tilde X$ be its normalization, and let $\pi: \tilde X \to X$ be the projection map (Ex. 3.8).
For each point $P \in X$, let $\OO_P$ be its local ring, and let $\tilde\OO_P$ be the integral closure of $\OO_P$.
We use a $*$ to denote the group of units in a ring.

(a) Show there is an exact sequence
$$
0 \to \bigoplus_{P \in X} \tilde\OO_P^* / \OO_P^* \to \Pic X \mapsvia{\pi^*} \Pic \tilde X \to 0
.
$$

(b) Use (a) to give another proof that if $X$ is a plane cuspidal cubic curve then there is an exact sequence
$$
0 \to \GG_a \to \Pic X \to \ZZ \to 0,
$$
   and if $X$ is a plane nodal cubic curve there is an exact sequence
$$
0 \to \GG_m \to \Pic X \to \ZZ \to 0
.
$$
:::

::: {.hint}
For part (a), represent $\Pic X$ and $\Pic\tilde X$ as the groups of Cartier divisors modulo principal divisors, and use the exact sequence of sheaves on $X$
$$
0\to\pi_*\OO_{\tilde X}^*/\OO_X^*
\to\mck^*/\OO_X^*
\to\mck^*/\pi_*\OO_{\tilde X}^*
\to0.
$$
:::

::: {.solution}
Put $K=K(X)=K(\tilde X)$, and write $\operatorname{CaDiv}(X)$ for the group of [[D-5PQ5W|Cartier divisors]].
The [[D-5PQ5W|Cartier class group]] is $\Pic(X)$ because $X$ is integral [@Har10a, Proposition II.6.15].
In the sequences in part (b), $\GG_a$ and $\GG_m$ denote their groups of $k$-points, $(k,+)$ and $k^\times$.

::: pf

::: {.pf-step #s1}

The normalization is a nonsingular projective integral curve, and $\pi$ is an isomorphism outside a finite set $S$ of closed points.
For a closed point $P$, the ring $B_P\coloneqq\tilde\OO_P$ is a finite semilocal normal domain over $A_P\coloneqq\OO_P$, with maximal ideals indexed by the points over $P$.

::: pf-proof

The [[D-QJ5M9|normalization]] is finite and birational for varieties and preserves projectivity [@Har10a, Exercise II.3.8].
A one-dimensional noetherian normal local domain is a DVR, so $\tilde X$ is nonsingular [@Har10a, Theorem I.6.2A].
On an affine open $\Spec A\subseteq X$, the finite module $\tilde A/A$ is torsion, since both rings have fraction field $K$.
A nonzero element annihilates this module after clearing the denominators of finitely many generators.
Thus its support is a proper closed subset of the curve and is finite.
Taking a finite affine cover gives $S$.
At a normal point the integral closure changes nothing, so $\pi$ is an isomorphism on $X\setminus S$.
We may take $S$ to be the singular locus, since a normal local ring of this curve is regular.

Integral closure commutes with localization, so $(\pi_*\OO_{\tilde X})_P=B_P$.
Finiteness over the local ring $A_P$ makes $B_P$ semilocal, with precisely the points of $\pi^{-1}(P)$ as its maximal ideals.
Its localizations there are the DVRs $\OO_{\tilde X,Q}$.

:::

:::

::: {.pf-step #s2}

For any closed point $P$ and any integers $n_Q$, indexed by $Q\in\pi^{-1}(P)$, there is $g\in K^*$ with $v_Q(g)=n_Q$ for every such $Q$.

::: pf-proof

Write the maximal ideals of $B_P$ as $\mathfrak n_1,\ldots,\mathfrak n_r$, corresponding to $Q_1,\ldots,Q_r$ over $P$.
For each $i$, choose a nonzero class in $\mathfrak n_i/\mathfrak n_i^2$.
This vector space is one-dimensional, since localization identifies it with the corresponding quotient in the DVR at $Q_i$.
The Chinese remainder theorem gives $b_i\in B_P$ with this prescribed class modulo $\mathfrak n_i^2$ and with $b_i\equiv1\pmod{\mathfrak n_j}$ for $j\ne i$.
Therefore $v_{Q_i}(b_i)=1$ and $v_{Q_j}(b_i)=0$ for $j\ne i$.
The rational function $g=\prod_i b_i^{n_{Q_i}}$ has the required valuations, including when some exponents are negative.

:::

:::

::: {.pf-step #s3}

Pullback of Cartier divisors gives a surjection
$$
\operatorname{CaDiv}(X)\longrightarrow\operatorname{Div}(\tilde X).
$$

::: pf-proof

Rational local equations on $X$ remain nonzero in the common function field $K$ and have unit ratios after pullback.
They therefore define a Cartier divisor on $\tilde X$, identified with a Weil divisor because $\tilde X$ is nonsingular.

Let $E$ be a divisor on $\tilde X$.
For each $P\in S$, choose $g_P$ by step [](#s2){.pf-ref} with the coefficients of $E$ at the points over $P$.
The divisor $\operatorname{div}(g_P)-E$ has finite support disjoint from $\pi^{-1}(P)$.
Remove its image and the other points of $S$ to obtain an open neighborhood $U_P$ of $P$ on which
$$
\operatorname{div}(g_P)|_{\pi^{-1}(U_P)}=E|_{\pi^{-1}(U_P)}.
$$
On $U_0=X\setminus S$, the normalization is an isomorphism, so $E$ gives a Cartier divisor $D_0$ there.
On $U_P$, use the single rational local equation $g_P$.
Every overlap of these opens lies in $U_0$, where the corresponding Weil divisors agree.
On a nonsingular curve equality of Weil divisors is equality of Cartier divisors, so these local divisors glue.
Their pullback is $E$.

:::

:::

::: {.pf-step #s4}

The kernel of the map in step [](#s3){.pf-ref} is canonically
$$
\bigoplus_{P\in X}B_P^*/A_P^*.
$$

::: pf-proof

A Cartier divisor $D$ with zero pullback is zero on $U_0$.
If $g_P$ is a rational local equation at $P\in S$, zero pullback means that $g_P$ has valuation zero at every point over $P$.
Equivalently, $g_P\in B_P^*$: an element of $K$ lies in $B_P$, respectively $B_P^*$, precisely when it is regular, respectively a unit, at all maximal ideals of this semilocal ring.
Changing a local equation multiplies $g_P$ by an element of $A_P^*$.
Thus $D$ determines one class in $B_P^*/A_P^*$ for each $P\in S$.
If every class is trivial, $D$ is locally zero everywhere, proving injectivity into this direct sum.

Conversely, choose representatives $b_P\in B_P^*$ for a tuple of such classes.
Shrink an open neighborhood $U_P$ so that it contains no other singular point and the rational function $b_P$ has no zero or pole on $\pi^{-1}(U_P)$.
The Cartier divisor with equation $b_P$ on $U_P$ and equation $1$ on $X\setminus\{P\}$ is defined: on the overlap the curve is nonsingular and $b_P$ is a regular unit.
Its pullback is zero, and its only possibly nonzero local class is the prescribed one at $P$.
Adding these divisors gives the tuple.
The construction is independent of representatives by the injectivity just proved.
Outside $S$ the rings $A_P$ and $B_P$ agree, and at the generic point both equal $K$, so their summands vanish.

This is the global kernel of the sheaf inclusion in the source hint: the quotient $\pi_*\OO_{\tilde X}^*/\OO_X^*$ has stalks $B_P^*/A_P^*$ and is supported on $S$.
Step [](#s3){.pf-ref} establishes the needed surjectivity on global divisors, rather than assuming that global sections preserve a sheaf surjection.

:::

:::

::: {.pf-step #s5}

Passing to Cartier divisor classes gives the exact sequence in part (a).

::: pf-proof

Both projective integral curves have only constant global regular functions.
Indeed, such a function defines a morphism to $\PP^1$ whose image is closed by properness and misses $\infty$.
The image is irreducible and hence a point, so the function belongs to $k$.
Consequently
$$
\Gamma(X,\OO_X^*)=\Gamma(\tilde X,\OO_{\tilde X}^*)=k^*.
$$
Principal Cartier divisors on each curve are therefore the image of the same group $K^*/k^*$, and pullback identifies these two principal-divisor subgroups.
In particular, the kernel in step [](#s4){.pf-ref} intersects the principal divisors only in zero.

If the pullback of $D$ is principal, say $\pi^*D=\operatorname{div}_{\tilde X}(g)$, then $D-\operatorname{div}_X(g)$ has zero pullback.
Thus step [](#s4){.pf-ref} gives exactly the kernel on classes, and step [](#s3){.pf-ref} gives surjectivity on classes.
Under $D\mapsto\OO_X(D)$ this map is Picard pullback, since the inverse rational local equations generate the corresponding pulled-back invertible sheaf, as in [[P-AGH268PULLBACKPIC]], step [](#s2){.pf-ref}.
Hence
$$
0\longrightarrow\bigoplus_{P\in X}\tilde\OO_P^*/\OO_P^*
\longrightarrow\Pic(X)\xrightarrow{\pi^*}\Pic(\tilde X)
\longrightarrow0
$$
is exact.

:::

:::

::: {.pf-step #s6}

Let $X$ be an integral singular plane cubic, with singular point $P$.
Its normalization is $\PP^1$, and there is a monic quadratic polynomial $q(t)$ such that, for $A=\OO_{X,P}$ and its integral closure $B$,
$$
\boxed{B^*/A^*\cong\bigl(k[t]/(q(t))\bigr)^*/k^*.}
$$
The polynomial $q$ has a double root in the cuspidal case and two distinct roots in the nodal case.

::: pf-proof

Choose coordinates with $P=[0:0:1]$.
The cubic equation has the form $zq_2(x,y)+q_3(x,y)=0$, where the subscripts denote degrees.
The quadratic term is nonzero: otherwise the equation is a binary cubic and factors over $k$, contrary to integrality.
Also $q_2$ and $q_3$ have no common linear factor, since that would divide the entire equation.

Choose the coordinate $x$ so that $x=0$ is not a tangent direction, and scale the equation so that $q(t)=q_2(1,t)$ is monic of degree two.
Divide $q_3(1,t)$ by $q(t)$, obtaining quotient of degree at most one and remainder $r(t)=a+bt$.
Absorb the quotient into $z$ by a linear coordinate change.
The equation becomes
$$
zq_2(x,y)+x^2(ax+by)=0,\qquad\gcd(q,r)=1.
$$
Projection from $P$ has rational inverse
$$
[s:t]\longmapsto[-s q_2(s,t):-t q_2(s,t):s^2(as+bt)].
$$
These three cubic forms have no common zero: at a root of $q_2$ one has $s\ne0$ and $as+bt\ne0$.
They define a birational morphism $\PP^1\to X$.
Its fibers away from $P$ contain a single point because projection is its inverse there; the fiber over $P$ is the finite set of roots of $q_2$.
The morphism is projective, using its closed graph in $\PP^1\times X$.
Its finite fibers therefore imply that it is finite [@Har10a, Exercise III.11.2].
Its source is normal, so the finite birational map is the normalization [@Har10a, Exercise II.3.8].
The points over $P$ are precisely the roots of $q$.

On the chart $z=1$, put $t=y/x$ in $K=k(t)$.
Then
$$
x=-q(t)/r(t),\qquad y=tx,\qquad q(t)+x(a+bt)=0.
$$
The last equation is monic quadratic in $t$, so $C=A[t]=A+At$ is finite over $A$.
Its maximal ideals all lie over $\mathfrak m=(x,y)A$ and correspond to the roots of $q$.
Indeed, a root $\alpha$ gives evaluation $x=y=0$, $t=\alpha$, while every residue of $t$ over $\mathfrak m$ satisfies $q(t)=0$.
The formulas embed $C$ into the semilocal ring
$$
B_0=k[t]_{\{h:\gcd(h,q)=1\}}.
$$
Each polynomial relatively prime to $q$ avoids every maximal ideal of $C$, so is a unit of $C$.
It follows that $B_0\subseteq C$, and therefore $C=B_0$.
This ring is normal, finite over $A$, and has fraction field $K$, so it is $B$.

Since $B=A+At$ and $xt=y$, one has
$$
xB=Ax+Ay=\mathfrak m.
$$
Thus $I\coloneqq\mathfrak m$ is also an ideal of $B$.
The polynomial $r$ is a unit in $B$, so $I=qB$ and
$$
A/I=k,\qquad B/I=k[t]/(q).
$$
The ideal $I$ is contained in the Jacobson radicals of both rings.
Reduction therefore maps their unit groups onto the unit groups of the quotients, with the same kernel $1+I$.
Taking the quotient gives the claimed unit-group isomorphism, with $k^*$ embedded as constant polynomials.

The tangent cone at $P$ is $q_2$.
An ordinary cusp has a repeated tangent and a node has two distinct tangents, giving exactly the stated alternatives for $q$.
There is no other singular point: a line through two singular points would have intersection multiplicity at least four with a cubic, so its restriction polynomial would vanish identically, forcing a line component.

:::

:::

::: {.pf-step #s7}

For a cuspidal cubic the kernel in part (a) is $(k,+)$, and for a nodal cubic it is $k^\times$.

::: pf-proof

In the cuspidal case translate the double root to zero, so that $k[t]/(q)\cong k[\varepsilon]/(\varepsilon^2)$.
Every unit is uniquely $c(1+u\varepsilon)$ with $c\in k^*$ and $u\in k$.
Since
$$
(1+u\varepsilon)(1+v\varepsilon)=1+(u+v)\varepsilon,
$$
the quotient by constant units is the additive group $k$.

In the nodal case write the distinct roots as $\alpha,\beta$.
The Chinese remainder theorem identifies $k[t]/(q)$ with $k\times k$ by evaluation at these roots.
Its units are $k^*\times k^*$, and the constants form the diagonal subgroup.
The map $(u,v)\mapsto u/v$ identifies the quotient with $k^*$.
These calculations use no characteristic restriction; the distinctness of the node's tangent directions is the relevant condition.

:::

:::

::: {.pf-step #s8}

The exact sequences in part (b) follow, with the right-hand map equal to $\deg\circ\pi^*$.

::: pf-proof

By step [](#s6){.pf-ref}, $\tilde X\cong\PP_k^1$, whose Picard group is $\ZZ$ via degree [@Har10a, Proposition II.6.4 and Corollary II.6.16].
Only the unique singular point contributes to the direct sum in step [](#s5){.pf-ref}.
Substituting the two groups from step [](#s7){.pf-ref} gives
$$
0\to(k,+)\to\Pic(X)\xrightarrow{\deg\circ\pi^*}\ZZ\to0
$$
for the cusp and
$$
0\to k^*\to\Pic(X)\xrightarrow{\deg\circ\pi^*}\ZZ\to0
$$
for the node.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (a), including the injectivity of the local-unit contribution.
Steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} compute that contribution and the quotient for both cubics in part (b).

:::

:::

:::
