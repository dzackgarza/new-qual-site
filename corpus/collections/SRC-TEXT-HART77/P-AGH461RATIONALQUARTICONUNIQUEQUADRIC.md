---
schema: qual/card@1
id: P-AGH461RATIONALQUARTICONUNIQUEQUADRIC
kind: problem
title: A rational quartic in $\PP^3$ lies on a unique, nonsingular, quadric surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Genus
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.1 and the retained companion solution. The source
    statement needs no correction. The companion's cohomological
    existence/uniqueness argument is retained, while its final appeal to a
    "rational normal quartic" is replaced by Hartshorne's quadric-cone genus
    calculation, recorded on FE-CRVQUAD.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
A rational curve of degree 4 in $\PP^3$ is contained in a unique quadric surface $Q$, and $Q$ is necessarily nonsingular.
:::

::: {.solution}
Let $X\subseteq\PP^3$ be the given rational quartic, and put
$H=\OO_X(1)$.

::: pf

::: {.pf-step #s1}

The curve $X$ is not contained in a plane.

::: pf-proof

If $X$ lay in a plane, then, being a nonsingular plane curve of degree $4$,
it would have genus
$$
\frac{(4-1)(4-2)}2=3.
$$
But $X$ is rational, so its genus is $0$.  Hence $X$ is nondegenerate in
$\PP^3$.

:::

:::

::: {.pf-step #s2}

At least one quadric surface contains $X$.

::: pf-proof

Since $X\cong\PP^1$ and $\deg H=4$,
$$
\deg(2H)=8,
\qquad
h^0(X,\OO_X(2))=8+1=9.
$$
Twisting the ideal sequence of $X$ by $\OO_{\PP^3}(2)$ gives
$$
0\longrightarrow\mathcal I_X(2)
\longrightarrow\OO_{\PP^3}(2)
\longrightarrow\OO_X(2)
\longrightarrow0.
$$
On global sections,
$$
h^0(\PP^3,\OO_{\PP^3}(2))=\binom{5}{3}=10>9,
$$
so the restriction map cannot be injective.  Thus
$$
H^0(\PP^3,\mathcal I_X(2))\neq0,
$$
and a nonzero element is the equation of a quadric containing $X$.

:::

:::

::: {.pf-step #s3}

That containing quadric is unique.

::: pf-proof

Suppose two linearly independent quadrics $Q_1,Q_2$ contain $X$.
They cannot have a common plane component: otherwise, because $X$ is
irreducible and lies in each quadric, the common-factor alternatives force
$X$ into a plane, contrary to step [](#s1){.pf-ref}.  Hence
$$
Y=Q_1\cap Q_2
$$
is a complete-intersection curve of type $(2,2)$.

By Bezout,
$$
\deg Y=2\cdot2=4=\deg X.
$$
The surjection $\OO_Y\twoheadrightarrow\OO_X$ therefore has kernel supported
in dimension $0$: its Hilbert polynomial has zero leading coefficient because
$X$ and $Y$ have the same degree.  But the complete-intersection curve $Y$ is
Cohen--Macaulay of pure dimension $1$, so $\OO_Y$ has no nonzero
zero-dimensional subsheaf.  Thus the kernel is zero and
$Y=X$ scheme-theoretically.
But the complete-intersection genus formula gives
$$
p_a(Y)
=1+\frac{(2)(2)(2+2-4)}2
=1,
$$
whereas the nonsingular rational curve $X$ has $p_a(X)=0$.  This
contradiction proves uniqueness.

:::

:::

::: {.pf-step #s4}

The unique quadric $Q$ is nonsingular.

::: pf-proof

Over the algebraically closed ground field, a singular quadric surface in
$\PP^3$ is either a union (possibly doubled) of planes or an irreducible
quadric cone.  The first possibility would put the irreducible curve $X$ in
a plane, contradicting step [](#s1){.pf-ref}.

Suppose therefore that $Q$ is a quadric cone.  The quadric-cone calculation
on [[FE-CRVQUAD]] says that an integral curve of even degree $2a$ on $Q$
has
$$
p_a=(a-1)^2.
$$
Here $\deg X=4=2\cdot2$, so this gives
$$
p_a(X)=(2-1)^2=1,
$$
again contradicting the fact that the nonsingular rational curve $X$ has
genus $0$.  Thus $Q$ cannot be singular.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives existence, step [](#s3){.pf-ref} gives uniqueness, and step [](#s4){.pf-ref} proves
that the unique quadric is nonsingular.

:::

:::

:::
