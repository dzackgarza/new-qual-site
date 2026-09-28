---
schema: qual/card@1
id: P-AGH243AFFINTER
kind: problem
title: Intersections of open affines in a separated scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Affine Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.4.3 statement and the diagonal criterion for separatedness.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a separated scheme over an affine scheme $S$.
Let $U$ and $V$ be open affine subsets of $X$.
Then $U \intersect V$ is also affine.

Give an example to show that this fails if $X$ is not separated.
:::

::: {.solution}
Let
\[
p:X\longrightarrow S
\]
be separated, with $S$ affine, and let $U,V\subseteq X$ be affine open subschemes.

<1>1. The fibre product
\[
U\times_SV
\]
is affine.
::: {.proof}
Write
\[
S=\Spec R,
\qquad
U=\Spec A,
\qquad
V=\Spec B.
\]
Then the two structure morphisms are induced by ring maps
\[
R\to A,
\qquad
R\to B,
\]
and the affine fibre-product formula gives
\[
U\times_SV
\cong
\Spec(A\otimes_RB).
\]
:::

<1>2. The intersection $U\cap V$ is canonically the inverse image of $U\times_SV$ under the diagonal
\[
\Delta_{X/S}:X\longrightarrow X\times_SX.
\]
::: {.proof}
The open subscheme
\[
U\times_SV
\subseteq
X\times_SX
\]
consists of pairs whose first coordinate lies in $U$ and second coordinate lies in $V$.

A point $x\in X$ maps under the diagonal to $(x,x)$, which lies in $U\times_SV$ exactly when
\[
x\in U\cap V.
\]
The same statement holds scheme-theoretically by the universal property of the fibre product: the pullback
\[
X\times_{X\times_SX}(U\times_SV)
\]
is precisely the open subscheme $U\cap V$.
:::

<1>3. The morphism
\[
U\cap V\longrightarrow U\times_SV
\]
is a closed immersion.
::: {.proof}
Because $X$ is separated over $S$, the diagonal
\[
\Delta_{X/S}:X\longrightarrow X\times_SX
\]
is a closed immersion.  By <1>2, the displayed morphism is its base change along the open immersion
\[
U\times_SV\hookrightarrow X\times_SX.
\]
Closed immersions are stable under base change.
:::

<1>4. Therefore
\[
\boxed{U\cap V\text{ is affine}.}
\]
::: {.proof}
By <1>1, $U\times_SV$ is affine.  By <1>3, $U\cap V$ is a closed subscheme of it.  Hartshorne II.3.11(b) shows that every closed subscheme of an affine scheme is affine.
:::

<1>5. The statement can fail if $X$ is not separated.
::: {.proof}
Let
\[
U_1\cong\mathbb A^2_k,
\qquad
U_2\cong\mathbb A^2_k
\]
be two copies of the affine plane, and glue them by the identity along
\[
W=\mathbb A^2_k\setminus\{(0,0)\}.
\]
Hartshorne II.2.12 gives a scheme $X$ covered by the two affine opens $U_1,U_2$, with
\[
U_1\cap U_2=W.
\]

We claim $W$ is not affine.  Cover it by
\[
D(x)\cup D(y).
\]
Inside the common function field $k(x,y)$,
\[
\Gamma(W,\mathcal O_W)
=
k[x,y]_x\cap k[x,y]_y
=
k[x,y].
\]
Indeed, a rational function lying in both localizations has denominator supported both on powers of $x$ and on powers of $y$; since $x$ and $y$ are coprime, the denominator must cancel.

If $W$ were affine, the canonical morphism
\[
W\longrightarrow
\Spec\Gamma(W,\mathcal O_W)
=
\mathbb A^2_k
\]
would be an isomorphism.  But this canonical morphism is the usual open immersion
\[
\mathbb A^2_k\setminus\{0\}
\hookrightarrow
\mathbb A^2_k,
\]
which misses the origin.  Hence $W$ is not affine.

Thus the two affine opens $U_1,U_2\subseteq X$ have nonaffine intersection, so $X$ cannot be separated by <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>4 proves the theorem and <1>5 gives the requested nonseparated example.
:::
:::
