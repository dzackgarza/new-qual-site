---
schema: qual/card@1
id: P-AGH561COMPLETEINT
kind: problem
title: Complete intersection surfaces are of general type with finitely many exceptions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Canonical Divisor
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Hartshorne V.6.1 transcription and collection context,
    together with the complete-intersection adjunction formula recorded from
    Hartshorne II.8.4 in P-AGH284COMPINT and the complete-intersection
    cohomology vanishing recorded from Hartshorne III.5 in P-AGH355COMPINT.
    The retained Hartshorne solution attachment ends before Chapter V, and
    the separate AG Solutions extraction is unreadable, so there is no usable
    retained V.6.1 source solution to incorporate. The proof below is an
    independent computation in the nonsingular surface-classification setting
    of the exercise.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Recomputed a=sum d_i-n-1 from adjunction and independently enumerated
    every tuple with a<=0 from 2(n-2)<=sum d_i<=n+1. Checked the three
    negative cases have K^2 equal to 8, 3, and 4 and hence are the stated
    del Pezzo surfaces. Checked the three zero cases have trivial canonical
    bundle and H^1(O_X)=0 by the complete-intersection cohomology result,
    hence are K3 surfaces of polarization degrees 4, 6, and 8.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Read for issue #121 and cited the published solution on the card: Yang
    Pi-Yeh, solution 5.6.1, printed p. 115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf (folio confirmed on the PDF's
    own text layer), read in tmp/sources/lfwin-hartshorne-solutions.md and
    checked against the exercise at Hartshorne V.6, printed p. 423 (PDF p. 438
    of tmp/sources/hartshorne-1977-algebraic-geometry.md, printed = PDF
    minus 15), and against Theorems 6.1--6.5 on printed pp. 421--422. Each step
    of the solution now names the source of its statement: the adjunction
    formula (Hartshorne II.8.4, and Yang's opening line), the six tuples
    (Yang's two enumerations, with the bounds n < 5 and n <= 5 made explicit),
    the del Pezzo placement (Theorem 6.1), the K3 placement (Theorem 6.3), and
    the general-type conclusion (Theorem 6.5). Added: the paragraph that reads
    kappa off the sign of a in omega = O(aH), which is what makes the two
    enumerations exhaustive and excludes kappa = 1 (Theorem 6.4). Corrected on
    the remark: Egbert's V.6.1 entry, printed p. 303, samples cases and does
    not reach (3;4) or (4;2,2), so it is not a complete solution of this
    exercise, and Yang's 5.6.1 is. Not checked: nothing beyond the enumerated
    list was recomputed; the del Pezzo and K3 identifications are the card's
    earlier ones, re-read but not re-derived in this pass.

---

::: {.problem}
Let $X$ be a surface in $\PP^n$, $n \geqslant 3$, defined as the complete intersection of hypersurfaces of degrees $d_1, \ldots, d_{n-2}$, with each $d_i \geqslant 2$.
Show that for all but finitely many choices of $\left(n, d_1, \ldots, d_{n-2}\right)$, the surface $X$ is of general type.
List the exceptional cases, and where they fit into the classification picture.
:::

::: {.solution}
Write
$$
H=\OO_X(1)
$$
for the hyperplane class and put
$$
a=\sum_{i=1}^{n-2}d_i-n-1.
$$

::: pf

::: {.pf-step #canonical-class-formula}
The canonical class of $X$ is
$$
\boxed{K_X\sim aH}.
$$

::: pf-proof
For a nonsingular complete intersection of hypersurfaces of degrees
$d_1,\ldots,d_{n-2}$ in $\PP^n$, the adjunction formula
[[P-AGH284COMPINT]] gives
$$
\omega_X
\cong
\OO_X\left(\sum_{i=1}^{n-2}d_i-n-1\right).
$$
With the notation fixed above, this is
$$
\omega_X\cong\OO_X(a),
$$
or equivalently
$$
K_X\sim aH.
$$

This is Hartshorne's adjunction formula (II, 8.4) for a complete
intersection and is the opening line of Yang Pi-Yeh's solution 5.6.1,
printed p. 115 of his set (read in
`tmp/sources/lfwin-hartshorne-solutions.md`), who writes it as
$\omega\cong\OO_X(\sum d_i-n-1)$ with the reference 2.8.4.
:::

:::

::: {.pf-step #positive-a-general-type}
If $a>0$, then $X$ is of general type.

::: pf-proof
The hyperplane class $H$ is ample on $X$. Hence for $a>0$ the canonical
divisor
$$
K_X\sim aH
$$
is ample. Every ample divisor is big, so $K_X$ is big. Therefore $X$ is
of general type.

Hartshorne's Theorem 6.5, printed p. 422, identifies surfaces of general
type as those $X$ with $\kappa(X)=2$, and $\kappa(X)=2$ is exactly the case
$a>0$ here, since $\omega_X\cong\OO_X(aH)$ with $H$ ample.
:::

:::

::: {.pf-step #exceptional-tuples-enumerated}
If $X$ is not covered by step [](#positive-a-general-type){.pf-ref}, then, up to permuting the
$d_i$, its degree data are exactly
$$
\boxed{
\left\{
(3;2),\,
(3;3),\,
(3;4),\,
(4;2,2),\,
(4;2,3),\,
(5;2,2,2)
\right\}.
}
$$

::: pf-proof
The exceptional condition is
$$
a\le0,
$$
equivalently
$$
\sum_{i=1}^{n-2}d_i\le n+1.
$$
Since every $d_i\ge2$ and there are $n-2$ of them,
$$
\sum_{i=1}^{n-2}d_i\ge2(n-2)=2n-4.
$$
Thus an exceptional tuple must satisfy
$$
2n-4\le n+1,
$$
so
$$
n\le5.
$$

For $n=3$ there is one degree $d_1\ge2$, and
$$
d_1\le4,
$$
giving
$$
d_1=2,3,4.
$$

For $n=4$ there are two degrees at least $2$ with
$$
d_1+d_2\le5.
$$
Up to order, the only possibilities are
$$
(d_1,d_2)=(2,2),(2,3).
$$

For $n=5$ there are three degrees at least $2$ with
$$
d_1+d_2+d_3\le6,
$$
so necessarily
$$
(d_1,d_2,d_3)=(2,2,2).
$$
There are no possibilities for $n\ge6$.

The bound $n\le5$ and the six tuples are Yang's, printed p. 115, who
splits them into $\sum_i d_i-n-1<0$, giving $(3;2)$, $(3;3)$, $(4;2,2)$,
and $\sum_i d_i-n-1=0$, giving $(3;4)$, $(4;2,3)$, $(5;2,2,2)$; his
bound is $n<5$ in the first case and $n\le5$ in the second, the first
following from $2(n-2)\le n$.
:::

:::

::: {.pf-step #negative-a-del-pezzo}
The three exceptional tuples with $a<0$ are del Pezzo surfaces:
$$
\begin{array}{c|c|c|c}
(n;d_i) & K_X & K_X^2 & \text{surface}\\
\hline
(3;2) & -2H & 8 & \text{quadric surface}\\
(3;3) & -H & 3 & \text{cubic surface}\\
(4;2,2) & -H & 4 & \text{intersection of two quadrics}.
\end{array}
$$

::: pf-proof
For each of these tuples step [](#canonical-class-formula){.pf-ref} gives $-K_X$ as a positive multiple
of the ample hyperplane class. Hence $-K_X$ is ample, so $X$ is a del
Pezzo surface.

For a complete-intersection surface,
$$
H^2=\deg X=\prod_i d_i.
$$
Consequently
$$
K_X^2=a^2H^2.
$$
For the quadric in $\PP^3$, one has $a=-2$ and $H^2=2$, so
$$
K_X^2=8.
$$
For the cubic in $\PP^3$, one has $a=-1$ and $H^2=3$, so
$$
K_X^2=3.
$$
For the $(2,2)$ complete intersection in $\PP^4$, one has $a=-1$ and
$H^2=4$, so
$$
K_X^2=4.
$$

Thus these are the del Pezzo surfaces of degrees $8$, $3$, and $4$,
respectively. Over the algebraically closed ground field, the smooth
quadric is $\PP^1\times\PP^1$, while the cubic surface and the degree-$4$
del Pezzo surface are the familiar rational del Pezzo surfaces. Hence
these cases lie in the $\kappa=-\infty$ part of the surface
classification.

Yang states the same three tuples at printed p. 115 as the case
$\omega\cong\OO_X(\sum d_i-n-1)$ with $\sum d_i-n-1<0$, and places them
through Hartshorne's Theorem 6.1, printed p. 421, which identifies
$\kappa=-1$ with $\linearsystem{12K}=\emptyset$ and with $X$ rational or ruled.
:::

:::

::: {.pf-step #zero-a-k3}
The three exceptional tuples with $a=0$ are K3 surfaces:
$$
\begin{array}{c|c}
(n;d_i) & H^2\\
\hline
(3;4) & 4\\
(4;2,3) & 6\\
(5;2,2,2) & 8.
\end{array}
$$

::: pf-proof
For these three tuples,
$$
\sum_i d_i=n+1,
$$
so step [](#canonical-class-formula){.pf-ref} gives
$$
\omega_X\cong\OO_X.
$$

The complete-intersection cohomology calculation
[[P-AGH355COMPINT]] applies to a surface and gives
$$
H^1(X,\OO_X)=0.
$$
It also gives
$$
H^0(X,\OO_X)=k.
$$
Hence
$$
q(X)=0
$$
and, since $\omega_X\cong\OO_X$,
$$
p_g(X)
=
h^0(X,\omega_X)
=
h^0(X,\OO_X)
=1.
$$
Thus these are K3 surfaces in the surface-classification picture, and
they lie in the $\kappa=0$ class.

Their indicated polarization degrees are simply
$$
H^2=\deg X=\prod_i d_i,
$$
namely $4$, $6$, and $8$.

Yang states these three tuples at printed p. 115 as the case
$\sum d_i-n-1=0$ and records that they are all K3 surfaces; Hartshorne's
Theorem 6.3, printed p. 421, is what places them there, a K3 surface being
one with $K=0$ and $q=0$, hence $p_a=p_g=1$.
:::

:::

::: {.pf-step #classification-summary}
All other degree data give surfaces of general type, while the six
tuples in step [](#exceptional-tuples-enumerated){.pf-ref} are precisely the del Pezzo and K3 exceptions listed
in steps [](#negative-a-del-pezzo){.pf-ref} and [](#zero-a-k3){.pf-ref}.

::: pf-proof
Step [](#exceptional-tuples-enumerated){.pf-ref} exhausts every tuple for which $a\le0$. Therefore every tuple
not in that list has $a>0$, and step [](#positive-a-general-type){.pf-ref} makes $X$ of general type.
Among the six exceptions, step [](#negative-a-del-pezzo){.pf-ref} classifies the three cases with
$a<0$, and step [](#zero-a-k3){.pf-ref} classifies the three cases with $a=0$.

Since $\omega_X\cong\OO_X(aH)$ with $H$ ample, the Kodaira dimension of
$X$ is $-1$, $0$ or $2$ according as $a<0$, $a=0$ or $a>0$, and never $1$:
the case $a<0$ makes $-K_X$ ample, the case $a=0$ makes $\omega_X$ trivial,
and the case $a>0$ makes $K_X$ ample. A complete intersection surface of
the kind considered is therefore never of the elliptic kind of Hartshorne's
Theorem 6.4, printed p. 422.
:::

:::

::: pf-qed
Step [](#canonical-class-formula){.pf-ref} computes the canonical class. Steps [](#positive-a-general-type){.pf-ref} and [](#exceptional-tuples-enumerated){.pf-ref} reduce the
problem to exactly six exceptional degree patterns. Steps [](#negative-a-del-pezzo){.pf-ref} and [](#zero-a-k3){.pf-ref}
place those exceptions in the del Pezzo and K3 parts of the surface
classification, and step [](#classification-summary){.pf-ref} proves that every remaining case is of
general type.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.6, exercise 6.1, printed p. 423, text version `tmp/sources/hartshorne-1977-algebraic-geometry.md` (printed page = its marker minus 15). Theorems 6.1--6.5, printed pp. 421--422, are the classification the exercise asks the exceptions to be placed in: $\kappa=-1$ for the rational and ruled surfaces, $\kappa=0$ for the K3, Enriques, abelian and hyperelliptic surfaces, $\kappa=1$ for the elliptic ones, and $\kappa=2$ for the surfaces of general type.

Yang Pi-Yeh, *Hartshorne Solutions*, solution 5.6.1, printed p. 115 of that set (`tmp/sources/lfwin-hartshorne-solutions.pdf`, whose folios are its PDF pages; read in `tmp/sources/lfwin-hartshorne-solutions.md`), proves the exercise. He reads $\omega\cong\OO_X(\sum d_i-n-1)$ off adjunction (II, 8.4); from $\kappa(X)=-1$ he gets $\sum d_i-n-1<0$, and $d_i\ge2$ then gives $n+1>\sum d_i\ge2(n-2)$, so $n<5$ and the tuples are $(3;2)$, $(3;3)$, $(4;2,2)$; from $\kappa(X)=0$ he gets $\sum d_i-n-1=0$, so $n\le5$ and the tuples are $(3;4)$, $(4;2,3)$, $(5;2,2,2)$, all K3; $\kappa(X)=1$ he rules out; and the remaining tuples are of general type.

Two of his lines are compressed and are made explicit in the steps above. First, $\kappa$ is read off the sign of $a$ in $\omega_X\cong\OO_X(aH)$ with $H$ ample, which is why the two enumerations are exhaustive; his $n<5$ and $n\le5$ are the bounds $2(n-2)\le n$ and $2(n-2)\le n+1$. Second, his $\kappa=1$ paragraph argues through $\omega^2=0$, which here reads $a^2H^2=0$, that is $a=0$ --- the $\kappa=0$ case he has just placed among K3 surfaces --- and his identification of $\kappa=1$ with an elliptic surface is Hartshorne's Theorem 6.4.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.6.1, printed p. 303 of that set, text version `tmp/sources/hartshorne-solutions-egbert.md`, samples cases instead of listing them: the K3 case $(3;4)$ and the del Pezzo case $(4;2,2)$ are missing and nothing shows the sample exhaustive, so his entry is not used here.
:::
