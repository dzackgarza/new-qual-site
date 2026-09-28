---
schema: qual/card@1
id: P-AGH456PLANEQUINTICNOG13
kind: problem
title: A nonsingular plane quintic has no $g_3^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Genus
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.5.6 and the retained companion solution page. The
    companion notes' residual-series argument is not used: for a hypothetical
    g^1_3 on a genus-six curve, K-D has degree seven and four sections, hence
    maps to P^3 rather than P^2. The proof below instead uses adjunction and
    the quadratic equations of the Veronese surface, then gives an explicit
    genus-six trigonal family on P^1 x P^1 for the existence assertion.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Show that a nonsingular plane curve of degree 5 has no $g_3^1$.
Show that there are nonhyperelliptic curves of genus 6 which cannot be represented as a nonsingular plane quintic curve.
:::

::: {.solution}
Let
$$
C\subseteq\PP^2
$$
be a nonsingular plane quintic.

<1>1. The canonical embedding of $C$ is the restriction of the second
Veronese embedding
$$
v_2:\PP^2\hookrightarrow\PP^5.
$$

::: {.proof}
Adjunction gives
$$
K_C=(K_{\PP^2}+C)|_C=\OO_C(2).
$$
The restriction map
$$
H^0(\PP^2,\OO(2))\longrightarrow H^0(C,K_C)
$$
is injective, since a nonzero conic cannot contain the integral quintic
$C$.  Both vector spaces have dimension $6$: the source is the space of
quadratic forms in three variables, while
$$
h^0(C,K_C)=g(C)
=
\frac{(5-1)(5-2)}2
=6.
$$
Thus restriction is an isomorphism, so the canonical map is
$$
C\hookrightarrow\PP^2\xrightarrow{v_2}\PP^5.
$$
Write
$$
S=v_2(\PP^2)\subseteq\PP^5
$$
for the Veronese surface containing the canonical curve.
:::

<1>2. If $C$ had a $g^1_3$, every divisor in that pencil would span a
trisecant line to the canonical curve.

::: {.proof}
Let $D$ be a divisor in a hypothetical $g^1_3$.  Then
$$
\deg D=3,
\qquad
h^0(D)=2.
$$
Riemann--Roch gives
$$
h^0(K_C-D)
=
h^0(D)+g-1-\deg D
=2+6-1-3
=4.
$$
Canonical hyperplanes containing the length-$3$ subscheme $D$ correspond
to the four-dimensional subspace $H^0(K_C-D)\subseteq H^0(K_C)$.  Hence the
canonical image of $D$ spans a projective space of dimension
$$
h^0(K_C)-h^0(K_C-D)-1
=6-4-1
=1.
$$
Thus $D$ lies on a line
$$
\ell\subseteq\PP^5,
$$
and $\ell\cap C$ has length at least $3$.
:::

<1>3. No line in $\PP^5$ meets the Veronese surface $S$ in a subscheme of
length at least $3$.  Therefore $C$ has no $g^1_3$.

::: {.proof}
In coordinates
$$
[X_0:X_1:X_2:X_3:X_4:X_5]
=
[x^2:y^2:z^2:xy:xz:yz],
$$
the Veronese surface is cut out scheme-theoretically by the quadratic
$2\times2$ minors of the symmetric matrix
$$
\begin{pmatrix}
X_0&X_3&X_4\\
X_3&X_1&X_5\\
X_4&X_5&X_2
\end{pmatrix}.
$$
If a line $\ell$ met $S$ in length at least $3$, every one of these
quadrics would restrict to a degree-$2$ form on
$$
\ell\cong\PP^1
$$
vanishing on a length-$3$ subscheme.  Every restriction would therefore be
zero, so the scheme-theoretic quadratic description would force
$$
\ell\subseteq S.
$$

But $S$ contains no lines.  Indeed, if $B=v_2^{-1}(\ell)$ were such a
curve, then
$$
\OO_S(1)|_\ell\cong\OO_{\PP^1}(1),
$$
whereas
$$
v_2^*\OO_S(1)=\OO_{\PP^2}(2).
$$
Thus
$$
1=\deg\OO_\ell(1)=\deg\OO_B(2),
$$
which is impossible because the latter degree is twice the positive integer
$\deg\OO_B(1)$.

Step <1>2 would produce exactly such a trisecant line from any $g^1_3$.
Hence a nonsingular plane quintic has no $g^1_3$.
:::

<1>4. There exist nonhyperelliptic genus-$6$ curves with a $g^1_3$.

::: {.proof}
Take a smooth member
$$
X\in\left|\OO_{\PP^1\times\PP^1}(3,4)\right|.
$$
Such members exist because this complete linear system is base-point-free
and a general member is smooth.  If $F_1,F_2$ are the two fibre classes,
then
$$
X\sim3F_1+4F_2,
\qquad
K_{\PP^1\times\PP^1}=-2F_1-2F_2.
$$
Adjunction gives
$$
2g(X)-2
=
X\cdot(X+K_{\PP^1\times\PP^1})
=10,
$$
so
$$
g(X)=6.
$$
One of the two projections
$$
X\longrightarrow\PP^1
$$
has degree $3$, and hence gives a base-point-free $g^1_3$.

The curve $X$ is not hyperelliptic.  If it also admitted a degree-$2$ map
to $\PP^1$, the product of that map with the degree-$3$ projection would
have generic degree dividing both $2$ and $3$, hence would be birational
onto its image in $\PP^1\times\PP^1$.  That image would have bidegree
$(2,3)$ and arithmetic genus
$$
(2-1)(3-1)=2,
$$
contradicting $g(X)=6$.
:::

<1>5. The curves from step <1>4 cannot be represented as nonsingular plane
quintics.

::: {.proof}
The existence of a $g^1_3$ is intrinsic to the curve.  By step <1>3, a
nonsingular plane quintic has no such pencil.  Therefore the
nonhyperelliptic genus-$6$ curves constructed in step <1>4 admit no
nonsingular plane quintic model.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove the first assertion, and steps <1>4--<1>5 prove the
second.
:::
:::
