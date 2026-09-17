---
schema: qual/card@1
id: P-AGCANVAMPLE
kind: problem
title: When the canonical divisor is very ample
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Divisor
  - Very Ample Divisors
  - Hyperelliptic Curves
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Wodzicki's question asking when the canonical divisor is very ample.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
When is a canonical divisor very ample?
:::

::: {.solution}
Let $C$ be a smooth projective curve of genus $g$ over an algebraically closed field.

<1>1. A divisor $L$ on $C$ is very ample if and only if
\[
\ell(L-p-q)=\ell(L)-2
\]
for every pair of points $p,q\in C$, allowing $p=q$.
::: {.proof}
For $p\ne q$, this condition says that the complete linear system $|L|$ separates the two points.  For $p=q$, it says that $|L|$ separates tangent directions at $p$.  A base-point-free linear system defines a closed immersion exactly when it separates points and tangent vectors, which is the stated length-two criterion.
:::

<1>2. Assume $g\ge2$.  For every effective divisor
\[
D=p+q
\]
of degree $2$,
\[
\boxed{\ell(K_C-D)=g-3+\ell(D).}
\]
::: {.proof}
Riemann--Roch for $D$ gives
\[
\ell(D)-\ell(K_C-D)
=\deg D+1-g
=3-g.
\]
Rearranging yields the displayed formula.
:::

<1>3. Since
\[
\ell(K_C)=g,
\]
the canonical divisor is very ample exactly when
\[
\ell(D)=1
\]
for every effective divisor $D$ of degree $2$.
::: {.proof}
By <1>1, $K_C$ is very ample exactly when
\[
\ell(K_C-D)=\ell(K_C)-2=g-2
\]
for every degree-two effective $D$.  By <1>2, this becomes
\[
g-3+\ell(D)=g-2,
\]
which is equivalent to $\ell(D)=1$.
:::

<1>4. For a curve of genus at least $2$, there exists an effective degree-two divisor $D$ with
\[
\ell(D)\ge2
\]
if and only if $C$ is hyperelliptic.
::: {.proof}
Such a divisor carries a pencil of meromorphic functions with poles bounded by $D$.  The associated nonconstant map
\[
C\longrightarrow\mathbb P^1
\]
has degree at most $2$: after removing the base divisor of the pencil, its degree is the degree of the moving part of $D$.  It cannot have degree $1$, since a degree-one map of smooth projective curves would make $C\cong\mathbb P^1$, contradicting $g\ge2$.  Hence the moving part has degree $2$, so there is no base divisor and the map has degree $2$.  This is the definition of a hyperelliptic curve.

Conversely, a degree-two morphism
\[
C\longrightarrow\mathbb P^1
\]
pulls a point of $\mathbb P^1$ back to a degree-two divisor whose complete linear system contains the pulled-back pencil, so $\ell(D)\ge2$.
:::

<1>5. Therefore, for $g\ge2$,
\[
K_C\text{ is very ample}
\quad\Longleftrightarrow\quad
C\text{ is nonhyperelliptic}.
\]
::: {.proof}
Combine <1>3 and <1>4.
:::

<1>6. The low-genus cases give the final criterion
\[
\boxed{
K_C\text{ is very ample}
\quad\Longleftrightarrow\quad
g\ge3\text{ and }C\text{ is nonhyperelliptic}.
}
\]
::: {.proof}
If $g=0$, then
\[
\deg K_C=-2,
\]
so $K_C$ is not even effective and cannot be very ample.

If $g=1$, then
\[
K_C\sim0,
\]
so the canonical system is constant and is not very ample.

If $g=2$, then
\[
\deg K_C=2,
\qquad
\ell(K_C)=2.
\]
The canonical system has no base point: if $p$ were a base point, then
\[
\ell(K_C-p)=\ell(K_C)=2,
\]
so the degree-one divisor $K_C-p$ would have two independent sections and would define a nonconstant map of degree at most $1$ to $\mathbb P^1$, forcing $C\cong\mathbb P^1$.  Thus the canonical system itself is a base-point-free degree-two pencil, so every genus-two curve is hyperelliptic and the canonical map is the double cover
\[
C\longrightarrow\mathbb P^1,
\]
not an embedding.

For $g\ge3$, <1>5 gives the asserted equivalence.
:::

<1>7. In the hyperelliptic case, the canonical map is explicitly two-to-one onto a rational normal curve of degree $g-1$ in $\mathbb P^{g-1}$.
::: {.proof}
Let
\[
\pi:C\longrightarrow\mathbb P^1
\]
be the hyperelliptic double cover.  The canonical bundle satisfies
\[
K_C\cong\pi^*\mathcal O_{\mathbb P^1}(g-1).
\]
Indeed, put
\[
L=\pi^*\mathcal O_{\mathbb P^1}(g-1).
\]
Then
\[
\deg L=2g-2=\deg K_C,
\]
and pullback gives at least
\[
h^0(\mathbb P^1,\mathcal O(g-1))=g
\]
independent sections of $L$.  Riemann--Roch gives
\[
h^0(L)-h^0(K_C\otimes L^{-1})=g-1.
\]
Thus $h^0(K_C\otimes L^{-1})\ge1$.  The line bundle $K_C\otimes L^{-1}$ has degree $0$, so a nonzero section has no zeros and trivializes it.  Hence $L\cong K_C$.

Therefore the canonical map factors as
\[
C\xrightarrow{\pi}\mathbb P^1
\xrightarrow{|\mathcal O(g-1)|}\mathbb P^{g-1},
\]
where the second map is the rational normal curve embedding.  The first map has degree $2$, so the composition cannot be an embedding.
:::

<1>8. Q.E.D.
::: {.proof}
Step <1>6 is the requested criterion; step <1>7 describes the exceptional hyperelliptic map geometrically.
:::
:::
