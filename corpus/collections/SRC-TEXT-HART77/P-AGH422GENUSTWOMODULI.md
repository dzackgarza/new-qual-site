---
schema: qual/card@1
id: P-AGH422GENUSTWOMODULI
kind: problem
title: Curves of genus $2$ correspond to six branch points on $\PP^1$ modulo $\Sigma_6$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Riemann-Hurwitz
  - Hyperelliptic Curves
  - Canonical Divisor
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
review: draft
---

::: {.problem}
Fix an algebraically closed field $k$ of characteristic $\neq 2$.

a. If $X$ is a curve of genus 2 over $k$, the canonical linear system $\abs{K}$ determines a finite morphism $f: X \to \PP^1$ of degree 2 (Ex.
1.7). Show that it is ramified at exactly 6 points, with ramification index 2 at each one.
Note that $f$ is uniquely determined, up to an automorphism of $\PP^1$, so $X$ determines an (unordered) set of 6 points of $\PP^1$, up to an automorphism of $\PP^1$.

b. Conversely, given six distinct elements $\alpha_1, \ldots, \alpha_6 \in k$, let $K$ be the extension of $k(x)$ determined by the equation $z^2=(x-\alpha_1) \cdots (x-\alpha_6)$.
Let $f: X \to \PP^1$ be the corresponding morphism of curves.
Show that $g(X)=2$, the map $f$ is the same as the one determined by the canonical linear system, and $f$ is ramified over the six points $x=\alpha_i$ of $\PP^1$, and nowhere else.
(Cf.
(II, Ex.
6.4).)

c. Using (I, Ex.
6.6), show that if $P_1, P_2, P_3$ are three distinct points of $\PP^1$, then there exists a unique $\varphi \in \Aut \PP^1$ such that $\varphi(P_1)=0, \varphi(P_2)=1, \varphi(P_3)=\infty$.
Thus in (a), if we order the six points of $\PP^1$, and then normalize by sending the first three to $0,1,\infty$ respectively, we may assume that $X$ is ramified over $0,1,\infty, \beta_1, \beta_2, \beta_3$, where $\beta_1, \beta_2, \beta_3$ are three distinct elements of $k$, $\neq 0,1$.

d. Let $\Sigma_6$ be the symmetric group on 6 letters.
Define an action of $\Sigma_6$ on sets of three distinct elements $\beta_1, \beta_2, \beta_3$ of $k$, $\neq 0,1$, as follows: reorder the set $0,1,\infty, \beta_1, \beta_2, \beta_3$ according to a given element $\sigma \in \Sigma_6$, then renormalise as in (c) so that the first three become $0,1,\infty$ again.
Then the last three are the new $\beta_1', \beta_2', \beta_3'$.

e. Summing up, conclude that there is a one-to-one correspondence between the set of isomorphism classes of curves of genus 2 over $k$, and triples of distinct elements $\beta_1, \beta_2, \beta_3$ of $k$, $\neq 0,1$, modulo the action of $\Sigma_6$ described in (d). In particular, there are many non-isomorphic curves of genus 2. We say that curves of genus 2 depend on three parameters, since they correspond to the points of an open subset of $\AA_k^3$ modulo a finite group.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The canonical degree-two map of a genus-$2$ curve is ramified at
exactly six points, each with ramification index $2$.

::: pf-proof

By [[P-AGH417HYPERELLIPTIC|Exercise IV.1.7]], the canonical system gives
a finite morphism
$$
f:X\longrightarrow\PP^1
$$
of degree $2$. Since $\operatorname{char}k\ne2$, the induced degree-two
extension of function fields is separable and any ramification is tame.

Riemann--Hurwitz gives
$$
2g(X)-2
=
(\deg f)\bigl(2g(\PP^1)-2\bigr)
+
\sum_{P\in X}(e_P-1).
$$
Thus
$$
2
=
2(-2)+\sum_P(e_P-1),
$$
so
$$
\sum_P(e_P-1)=6.
$$
For a degree-two map, every ramification index is at most $2$; at a
ramification point it is therefore exactly $2$ and contributes $1$.
Hence there are exactly six ramification points.

Their images in $\PP^1$ are distinct: a ramification point already has
multiplicity $2$ in its fibre, which exhausts the degree of $f$. Thus the
map has exactly six branch points as well.

:::

:::

::: {.pf-step #s2}

Any finite morphism
$$
h:X\longrightarrow\PP^1
$$
of degree $2$ from a genus-$2$ curve is the canonical morphism up to an
automorphism of $\PP^1$.

::: pf-proof

Let
$$
D=h^*(q)
$$
for a point $q\in\PP^1$. Then $\deg D=2$, and pullback of the two
independent sections of $\mco_{\PP^1}(1)$ gives
$$
\ell(D)\ge2.
$$
Riemann--Roch on the genus-$2$ curve gives
$$
\ell(D)-\ell(K-D)=1.
$$
Hence $\ell(K-D)\ge1$. But
$$
\deg(K-D)=0.
$$
A degree-zero line bundle with a nonzero section is trivial: the zero
divisor of such a section is effective of degree zero, hence zero.
Therefore
$$
K\sim D.
$$
Moreover $\ell(D)=\ell(K)=2$, so the pencil defining $h$ is the complete
canonical pencil. Choosing a different basis of its two-dimensional
section space changes the target coordinates by an element of
$\PGL_2(k)$. This proves the uniqueness assertion in part (a).

:::

:::

::: {.pf-step #s3}

For
$$
K(X)=k(x)(z),
\qquad
z^2=\prod_{i=1}^6(x-\alpha_i),
$$
the corresponding degree-two map
$$
f:X\longrightarrow\PP^1
$$
is ramified exactly over the six points $x=\alpha_i$, with ramification
index $2$ above each one.

::: pf-proof

Put
$$
h(x)=\prod_{i=1}^6(x-\alpha_i).
$$
At $x=\alpha_i$, the function $h$ has valuation $1$. If $v$ is a
valuation of $K(X)$ above the corresponding valuation of $k(x)$, then
$$
2v(z)
=
v(h)
=
e_v.
$$
Thus $e_v$ is even. Since the extension has degree $2$, one must have
$$
e_v=2.
$$
So each $\alpha_i$ is a simple branch point.

At a finite point $a\ne\alpha_i$, one has $h(a)\ne0$. On the affine
double cover
$$
z^2=h(x),
$$
the derivative with respect to $z$ is $2z$, which is nonzero above such a
point because $z^2=h(a)\ne0$. Hence the cover is étale there.

It remains to inspect infinity. Put
$$
u=x^{-1},
\qquad
w=zu^3.
$$
Then near $u=0$ the equation becomes
$$
w^2
=
\prod_{i=1}^6(1-\alpha_i u).
$$
At $u=0$ this gives
$$
w^2=1.
$$
Since $\operatorname{char}k\ne2$, the two points $w=\pm1$ are nonsingular
and the derivative $2w$ is nonzero there. Thus the cover is unramified at
infinity. Hence the six $\alpha_i$ are exactly the branch points.

:::

:::

::: {.pf-step #s4}

The curve $X$ in step [](#s3){.pf-ref} has genus $2$.

::: pf-proof

The extension is separable because its degree is $2$ and
$\operatorname{char}k\ne2$. By step [](#s3){.pf-ref} there are exactly six tame
ramification points, each with $e_P=2$. Riemann--Hurwitz gives
$$
2g(X)-2
=
2(-2)+6,
$$
so
$$
2g(X)-2=2
$$
and therefore
$$
\boxed{g(X)=2}.
$$

:::

:::

::: {.pf-step #s5}

The map $f$ in step [](#s3){.pf-ref} is the morphism determined by the
canonical linear system, up to an automorphism of $\PP^1$.

::: pf-proof

Step [](#s4){.pf-ref} gives $g(X)=2$, and $f$ has degree $2$. Step [](#s2){.pf-ref} says that
every degree-two morphism from a genus-$2$ curve to $\PP^1$ is the
canonical morphism up to an automorphism of the target. This proves the
remaining assertion of part (b).

:::

:::

::: {.pf-step #s6}

Given three distinct points
$$
P_1,P_2,P_3\in\PP^1,
$$
there is a unique
$$
\varphi\in\Aut\PP^1
$$
such that
$$
\varphi(P_1)=0,
\qquad
\varphi(P_2)=1,
\qquad
\varphi(P_3)=\infty.
$$

::: pf-proof

By [[P-AGH66AUTP1|Exercise I.6.6]],
$$
\Aut\PP^1=\PGL_2(k).
$$
Choose a fractional linear transformation sending $P_1$ to $0$ and
$P_3$ to $\infty$. Its value at $P_2$ is a nonzero finite scalar; multiply
the target coordinate by its inverse to send $P_2$ to $1$. This proves
existence.

For uniqueness, if $\varphi$ and $\psi$ both have the required values,
then
$$
\psi\circ\varphi^{-1}
$$
fixes $0$, $1$, and $\infty$. A fractional linear transformation fixing
$0$ and $\infty$ has the form $x\mapsto cx$, and fixing $1$ forces
$c=1$. Hence $\psi=\varphi$.

:::

:::

::: {.pf-step #s7}

After ordering the six branch points of a genus-$2$ curve and
applying the unique normalization of step [](#s6){.pf-ref}, the branch set has the
form
$$
0,\ 1,\ \infty,\ \beta_1,\ \beta_2,\ \beta_3,
$$
where
$$
\beta_i\ne0,1,
\qquad
\beta_i\ne\beta_j\quad(i\ne j).
$$

::: pf-proof

Part (a) gives six distinct branch points on $\PP^1$. Choose an ordering
and apply step [](#s6){.pf-ref} to the first three. Since the six points are distinct,
the remaining three normalized points are distinct from each other and
from $0$, $1$, and $\infty$. Thus they are finite elements of $k$,
different from $0$ and $1$.

:::

:::

::: {.pf-step #s8}

The rule in part (d) defines an action of $\Sigma_6$ on
$$
U
=
\left\{
(\beta_1,\beta_2,\beta_3)\in\AA^3:
\beta_i\ne0,1,
\beta_i\ne\beta_j
\right\}.
$$

::: pf-proof

Associate to a point of $U$ the ordered six-tuple
$$
(0,1,\infty,\beta_1,\beta_2,\beta_3).
$$
Given $\sigma\in\Sigma_6$, reorder this six-tuple by $\sigma$. Its first
three entries are still distinct, so step [](#s6){.pf-ref} gives a unique projective
automorphism sending them to $0$, $1$, and $\infty$. Apply that
automorphism to the remaining three entries; because all six entries were
distinct, the resulting last three lie in $U$.

The identity permutation clearly acts trivially. For two permutations,
performing the first reordering and normalization and then the second
produces the same normalized ordered six-tuple as performing the combined
reordering once: both projective automorphisms send the same first three
ordered points to $0$, $1$, and $\infty$, and step [](#s6){.pf-ref} makes that
normalizing automorphism unique. Hence the rule satisfies the group law
and defines the stated action.

:::

:::

::: {.pf-step #s9}

A separable degree-two cover of $\PP^1$ over $k$ is determined,
up to isomorphism over $\PP^1$, by its branch locus.

::: pf-proof

Let
$$
F=k(\PP^1)=k(x),
$$
and let $L_1/F$ and $L_2/F$ be the function-field extensions of two such
covers with the same branch locus. Since $\operatorname{char}k\ne2$, each
quadratic extension has Kummer form
$$
L_i=F(\sqrt{d_i})
$$
for some $d_i\in F^\times$, determined modulo $F^{\times 2}$.

For a place $P$ of $F$, the quadratic extension $F(\sqrt{d_i})/F$ is
ramified at $P$ exactly when $v_P(d_i)$ is odd. Equality of the branch
loci therefore implies that
$$
v_P(d_1/d_2)
$$
is even for every $P\in\PP^1$. Hence
$$
\operatorname{div}(d_1/d_2)=2D
$$
for an integral divisor $D$ on $\PP^1$. This divisor has degree $0$.
Since every degree-zero divisor on $\PP^1$ is principal, there is
$g\in F^\times$ with
$$
D=\operatorname{div}(g).
$$
Consequently
$$
\operatorname{div}\!\left(\frac{d_1}{d_2g^2}\right)=0,
$$
so
$$
\frac{d_1}{d_2g^2}=c
$$
for some $c\in k^\times$. Because $k$ is algebraically closed, $c=a^2$
for some $a\in k^\times$. Thus
$$
d_1=d_2(ag)^2,
$$
and therefore
$$
F(\sqrt{d_1})=F(\sqrt{d_2}).
$$
The corresponding nonsingular projective curves are consequently
isomorphic over $\PP^1$.

:::

:::

::: {.pf-step #s10}

There is a bijection
$$
\left\{
\begin{array}{c}
\text{isomorphism classes of}\\
\text{genus-$2$ curves over $k$}
\end{array}
\right\}
\longleftrightarrow
U/\Sigma_6.
$$

::: pf-proof

Given a genus-$2$ curve $X$, step [](#s1){.pf-ref} gives the six branch points of its
canonical map. Order them and apply step [](#s6){.pf-ref} to the first three. Step
[](#s7){.pf-ref} then produces a point
$$
(\beta_1,\beta_2,\beta_3)\in U.
$$
Changing the ordering changes this point by exactly the action defined in
step [](#s8){.pf-ref}. Changing coordinates on the target $\PP^1$ does not change its
$\Sigma_6$-orbit: after applying the coordinate change, the unique
normalization of the same ordered first three points is obtained by
composing the old normalization with the inverse coordinate change.
Thus $X$ determines a well-defined element of $U/\Sigma_6$.

An isomorphism $X\cong Y$ identifies $H^0(Y,K_Y)$ with $H^0(X,K_X)$.
Hence the two canonical maps differ only by an automorphism of their
targets, so isomorphic curves determine the same orbit.

Conversely, suppose two genus-$2$ curves determine the same orbit. After
choosing orderings and normalizations, their canonical maps have the same
six-point branch locus. Step [](#s9){.pf-ref} then identifies the two quadratic
function-field extensions of $k(\PP^1)$, and hence identifies the two
nonsingular projective curves. Thus distinct isomorphism classes cannot
determine the same orbit.

Finally, let
$$
(\beta_1,\beta_2,\beta_3)\in U.
$$
Set
$$
B=\{0,1,\infty,\beta_1,\beta_2,\beta_3\}\subset\PP^1.
$$
Choose a point $q\in\PP^1\setminus B$ and an automorphism
$\tau\in\Aut\PP^1$ with $\tau(q)=\infty$. Then $\tau(B)$ consists of six
finite points. Part (b), proved in steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}, constructs a genus-$2$
curve whose canonical map is branched exactly over $\tau(B)$. Composing
that map with $\tau^{-1}$ gives branch locus $B$, so the resulting curve
maps to the prescribed orbit. Therefore the correspondence is surjective
as well as injective.

:::

:::

::: {.pf-step #s11}

The parameter space in step [](#s10){.pf-ref} is an open subset of
$\AA_k^3$ modulo a finite group, and it has infinitely many orbits.

::: pf-proof

Explicitly,
$$
U
=
\AA_k^3
\setminus
\left(
\bigcup_{i=1}^3\{\beta_i=0\}
\cup
\bigcup_{i=1}^3\{\beta_i=1\}
\cup
\bigcup_{1\le i<j\le3}\{\beta_i=\beta_j\}
\right),
$$
so $U$ is open in $\AA_k^3$. The group $\Sigma_6$ is finite. This is the
three-parameter description asserted in part (e).

Moreover an algebraically closed field is infinite. Fixing two admissible
distinct values of $\beta_1$ and $\beta_2$ leaves infinitely many choices
of $\beta_3$, while every $\Sigma_6$-orbit is finite. Hence $U/\Sigma_6$
is infinite, so there are infinitely many pairwise non-isomorphic curves
of genus $2$ over $k$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b), steps
[](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (c), step [](#s8){.pf-ref} proves part (d), and steps
[](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref} prove part (e).

:::

:::

:::
