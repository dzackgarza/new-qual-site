---
schema: qual/card@1
id: P-AGH527ELLRULEDSECT
kind: problem
title: Sections of self-intersection one on the elliptic ruled surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.7 and the retained companion argument using the
    e=-1 elliptic ruled surface of V.2.11.6, the section/quotient
    correspondence for P(E), and degree-one line bundles on an elliptic curve.
    The proof below derives existence and uniqueness of the quotient to O(P)
    by Riemann--Roch and normalization, constructs the family algebraically by
    cohomology and base change from O(Delta), and computes the divisor class of
    each section to prove pairwise non-linear-equivalence.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
On the elliptic ruled surface $X$ of (2.11.6), show that the sections $C_0$ with $C_0^2=1$ form a one-dimensional algebraic family, parametrized by the points of the base curve $C$, and that no two are linearly equivalent.
:::

::: {.solution}
Let
$$
\pi:X=\PP(\mathcal E)\longrightarrow C
$$
be the ruled surface of (2.11.6), with $\mathcal E$ normalized.

::: pf

::: {.pf-step #s1}

One has
$$
\deg\mathcal E=1.
$$

::: pf-proof

For the elliptic ruled surface of (2.11.6), the invariant is
$$
e=-1.
$$
By the definition of the invariant of a normalized ruled surface,
$$
e=-\deg\det\mathcal E.
$$
Hence
$$
\deg\mathcal E=\deg\det\mathcal E=1.
$$

:::

:::

::: {.pf-step #s2}

For every point $P\in C$,
$$
\dim_k\Hom\qty(\mathcal E,\OO_C(P))=1.
$$

::: pf-proof

Set
$$
\mathcal F_P=\mathcal E^\vee\tensor\OO_C(P).
$$
Since $\mathcal E$ has rank two and degree one,
$$
\deg\mathcal F_P=-1+2=1.
$$
On the elliptic curve $C$, Riemann--Roch gives
$$
\chi(\mathcal F_P)=\deg\mathcal F_P=1.
$$
Also $K_C\cong\OO_C$, so Serre duality gives
$$
H^1(C,\mathcal F_P)^\vee
\cong
H^0\qty(C,\mathcal F_P^\vee)
=
H^0\qty(C,\mathcal E\tensor\OO_C(-P)).
$$
The line bundle $\OO_C(-P)$ has negative degree, and $\mathcal E$ is
normalized. Therefore the last space is zero. Hence
$$
h^0(C,\mathcal F_P)=\chi(\mathcal F_P)=1.
$$
Finally,
$$
H^0(C,\mathcal F_P)
=
\Hom\qty(\mathcal E,\OO_C(P)).
$$

:::

:::

::: {.pf-step #s3}

Every nonzero morphism
$$
\mathcal E\longrightarrow\OO_C(P)
$$
is surjective.

::: pf-proof

Let the image be
$$
\OO_C(P-Z)\subseteq\OO_C(P)
$$
for an effective divisor $Z$. If $Z\ne0$, the kernel is an invertible
subsheaf $\mathcal N\subseteq\mathcal E$ with
$$
\deg\mathcal N
=
\deg\mathcal E-\deg\OO_C(P-Z)
=
1-(1-\deg Z)
=
\deg Z>0.
$$
Then the inclusion $\mathcal N\hookrightarrow\mathcal E$ gives a nonzero
section of
$$
\mathcal E\tensor\mathcal N^{-1},
$$
where $\deg\mathcal N^{-1}<0$, contradicting normalization. Thus $Z=0$, and
the map is surjective.

:::

:::

::: {.pf-step #s4}

For every $P\in C$ there is a unique section $C_P\subseteq X$
corresponding to the quotient
$$
\mathcal E\twoheadrightarrow\OO_C(P).
$$

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, there is a surjection
$$
\mathcal E\twoheadrightarrow\OO_C(P),
$$
unique up to a nonzero scalar. Under the quotient convention for
$\PP(\mathcal E)$, a line-bundle quotient of $\mathcal E$ gives a section of
$\pi$. Multiplying the quotient map by a scalar does not change the section,
so the resulting section $C_P$ is unique.

:::

:::

::: {.pf-step #s5}

If a section $D\subseteq X$ corresponds to an exact sequence
$$
0\longrightarrow\mathcal N
\longrightarrow\mathcal E
\longrightarrow\mathcal L
\longrightarrow0,
$$
then
$$
D^2=2\deg\mathcal L-1.
$$

::: pf-proof

The normal bundle of the section determined by the quotient
$\mathcal E\twoheadrightarrow\mathcal L$ is
$$
\mathcal N^\vee\tensor\mathcal L.
$$
Indeed this follows fibrewise from the tangent space to the projective line of
one-dimensional quotients, and the local splittings of the exact sequence
glue the resulting identification. Therefore
$$
D^2
=
\deg\qty(\mathcal N^\vee\tensor\mathcal L)
=
\deg\mathcal L-\deg\mathcal N.
$$
Since
$$
\deg\mathcal N+\deg\mathcal L=\deg\mathcal E=1
$$
by step [](#s1){.pf-ref}, one obtains
$$
D^2=2\deg\mathcal L-1.
$$

:::

:::

::: {.pf-step #s6}

The sections of self-intersection one are exactly the sections
$C_P$ from step [](#s4){.pf-ref}.

::: pf-proof

If $D^2=1$, step [](#s5){.pf-ref} gives
$$
1=2\deg\mathcal L-1,
$$
so $\deg\mathcal L=1$. On an elliptic curve, Riemann--Roch and Serre duality
give
$$
h^0(C,\mathcal L)=1
$$
for every degree-one line bundle $\mathcal L$. Its unique nonzero section has
an effective divisor consisting of one point $P$, so
$$
\mathcal L\cong\OO_C(P).
$$
Thus $D=C_P$ by uniqueness in step [](#s4){.pf-ref}.

Conversely, for the quotient to $\OO_C(P)$ one has $\deg\mathcal L=1$, so
step [](#s5){.pf-ref} gives
$$
C_P^2=1.
$$

:::

:::

::: {.pf-step #s7}

The sections $C_P$ form an algebraic family parametrized by $C$.

::: pf-proof

Let $p,q:C\times C\to C$ be the first and second projections, and let
$\Delta\subseteq C\times C$ be the diagonal. The line bundle
$$
\OO_{C\times C}(\Delta)
$$
restricts on $C\times\{P\}$ to $\OO_C(P)$. Put
$$
\mathcal G
=
p^*\mathcal E^\vee\tensor\OO_{C\times C}(\Delta).
$$
By step [](#s2){.pf-ref} and its proof, every fibre of $q$ satisfies
$$
h^0(\mathcal G|_{C\times\{P\}})=1,
\qquad
h^1(\mathcal G|_{C\times\{P\}})=0.
$$
Cohomology and base change therefore makes
$$
\mathcal R=q_*\mathcal G
$$
an invertible sheaf on the parameter curve $C$. The universal evaluation map
is equivalently a morphism
$$
p^*\mathcal E\tensor q^*\mathcal R
\longrightarrow
\OO_{C\times C}(\Delta)
$$
whose restriction over $P$ is the unique nonzero map
$\mathcal E\to\OO_C(P)$ up to scalar. By step [](#s3){.pf-ref} every fibre map is
surjective, hence this is a relative line-bundle quotient. Projectivizing it
gives a family of sections of $X\to C$ over the second copy of $C$, with fibre
$C_P$ over $P$. Thus the self-intersection-one sections form a
one-dimensional algebraic family parametrized by $C$.

:::

:::

::: {.pf-step #s8}

For $P,Q\in C$,
$$
\OO_X(C_P-C_Q)
\cong
\pi^*\OO_C(P-Q).
$$

::: pf-proof

Let
$$
0\longrightarrow\mathcal N_P
\longrightarrow\mathcal E
\longrightarrow\OO_C(P)
\longrightarrow0
$$
be the quotient defining $C_P$. The composite
$$
\pi^*\mathcal N_P
\longrightarrow
\pi^*\mathcal E
\longrightarrow
\OO_X(1)
$$
is a section of
$$
\OO_X(1)\tensor\pi^*\mathcal N_P^{-1},
$$
and its zero divisor is exactly $C_P$. Hence
$$
\OO_X(C_P)
\cong
\OO_X(1)\tensor\pi^*\mathcal N_P^{-1}.
$$
Taking determinants in the defining exact sequence gives
$$
\mathcal N_P
\cong
\det\mathcal E\tensor\OO_C(-P).
$$
Thus
$$
\OO_X(C_P)
\cong
\OO_X(1)\tensor\pi^*\qty((\det\mathcal E)^{-1}\tensor\OO_C(P)).
$$
Dividing the formulas for $P$ and $Q$ gives the displayed identity.

:::

:::

::: {.pf-step #s9}

No two distinct sections in this family are linearly equivalent.

::: pf-proof

Suppose
$$
C_P\sim C_Q.
$$
Step [](#s8){.pf-ref} gives
$$
\pi^*\OO_C(P-Q)\cong\OO_X.
$$
Pulling back along any section of $\pi$ shows
$$
\OO_C(P-Q)\cong\OO_C.
$$
Thus
$$
\OO_C(P)\cong\OO_C(Q).
$$
Each degree-one line bundle on the elliptic curve has a one-dimensional space
of sections, so its unique effective divisor is determined by the line bundle.
Hence $P=Q$. Therefore distinct parameters give non-linearly-equivalent
sections.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} identify the self-intersection-one sections with an algebraic
family parametrized by $C$, and steps [](#s8){.pf-ref} and [](#s9){.pf-ref} prove that no two distinct
members are linearly equivalent.

:::

:::

:::
