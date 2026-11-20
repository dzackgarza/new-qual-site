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
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The event above, of the same day, had been rewritten in place by
    2e25f12802; it is restored here to the text it carried when 4578427ace
    wrote it, and this event carries the corrections, its own and this pass's.

    Read for this pass: Yang Pi-Yeh, solution 5.6.1, printed p. 115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf (folio read on the PDF's own
    text layer), in tmp/sources/lfwin-hartshorne-solutions.md; A. Egbert,
    V.6.1, printed p. 303 of tmp/sources/hartshorne-solutions-egbert.md; the
    exercise at Hartshorne V.6, printed p. 423 (PDF p. 438 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, printed page = PDF page
    minus 15); Theorems 6.1--6.5 on printed p. 422, after the marker for PDF
    p. 437; and Exercise II.8.4(e), printed p. 188, with Example II.8.20.3,
    printed p. 183, for the canonical class of a complete intersection.

    Corrected: Yang's entry cites no theorem of the book. What it gives is the
    canonical class from adjunction and the two enumerations, and it is
    Egbert, printed p. 303, who places them --- for n = 3 with d_1 = 2 or 3 he
    has K_X a negative multiple of the ample hyperplane class, so that
    |12K| is empty and Theorem 6.1 makes X rational or ruled, and for n = 4
    with (d_1,d_2) = (2,3) and n = 5 with (2,2,2) he has K_X trivial, so that
    X is K3 by Theorem 6.3. Both placements are now transcribed in the steps
    negative-a-del-pezzo and zero-a-k3 with those pages, and the remark cites
    him as well.

    Withdrawn: the paragraph in step classification-summary that read the
    Kodaira dimension off the sign of a and excluded kappa = 1. It was
    written in this batch and is not needed: a > 0 is general type by
    positivity, and the six remaining tuples are placed by the two steps
    above. With it goes the sentence of the remark that listed which of the
    card's arguments are its own, which is curation and not mathematics
    (QUAL-08). The sentence "these cases lie in the kappa = -infinity part of
    the surface classification" is replaced by Theorem 6.1's statement, kappa
    = -1, which is the book's convention at V.6, printed p. 422, and the same
    card already used -1 in another step. The phrase "the familiar rational
    del Pezzo surfaces", which carried an uncited rationality claim, is
    replaced by the computation of the squares K_X^2 = 8, 3, 4 that the step
    already makes. Also corrected: Theorems 6.1 and 6.3 are on printed p. 422,
    not p. 421, and the canonical class formula is Exercise II.8.4(e) on
    printed p. 188, not a statement of II.8.4.

    Not checked in this pass: the del Pezzo and K3 identifications were
    re-read but not re-derived, and no published proof of the placement in the
    classification beyond Yang's enumerations and Egbert's two cases was
    sought. Egbert samples cases rather than listing them: his entry does not
    reach (3;4) or (4;2,2).
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repaired on a reader's third report of this date, which is right on both
    points. First, the sentence that read Hartshorne's Theorem 6.5, printed
    p. 422, as making kappa(X) = 2 exactly the case a > 0 here is removed. It
    was written in this batch, it is not in the card at 83d33296ae, and its
    "exactly" needs kappa(X) = 2 to fail for a <= 0, which at that point in
    the card no step and no source establishes. What the step proves is the
    first request alone: for a > 0 the canonical divisor is a positive
    multiple of the ample class H, hence ample, hence big, hence X is of
    general type.

    Second, that proof, and the identification of the three a < 0 cases as del
    Pezzo surfaces of degrees 8, 3 and 4 with K_X^2 = a^2H^2, are the card's
    own and now say so in the steps. They were on the card before this batch.
    Yang's printed route to the first request is not this one: at printed
    p. 115 he excludes kappa = 1 and concludes that the remaining tuples are of
    general type, where the card takes ampleness of K_X directly. Read for
    this: Yang, solution 5.6.1, printed p. 115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf in
    tmp/sources/lfwin-hartshorne-solutions.md, and Egbert, V.6.1, printed
    p. 303 of tmp/sources/hartshorne-solutions-egbert.md, whose two placements
    the steps transcribe. Not checked: nothing new; the del Pezzo and K3
    identifications were not re-derived.
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

This is Hartshorne's Exercise II.8.4(e), for a nonsingular
complete intersection, and for a hypersurface Example II.8.20.3. Yang Pi-Yeh's solution 5.6.1, printed p. 115, opens with the same
formula.
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

This step is the card's own.
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

Thus these are the del Pezzo surfaces of degrees $8$, $3$ and $4$; over the
algebraically closed ground field the smooth quadric is
$\PP^1\times\PP^1$. That each of the three is a del Pezzo surface of the
stated degree is this card's own computation, from $-K_X$ a positive
multiple of the ample class $H$ and $K_X^2=a^2H^2$.

Since $a<0$, the divisor $12K_X\sim12aH$ is a negative multiple of the ample
class $H$, so
$$
\linearsystem{12K_X}=\emptyset,
$$
a nonzero section being an effective divisor linearly equivalent to a
negative multiple of an ample class. Hartshorne's Theorem 6.1, then makes $X$ rational or ruled, that is $\kappa(X)=-1$. This is
Egbert's step at printed p. 303, who for $n=3$ takes $d_1=2$ or $d_1=3$ so
that $K_X$ is a negative multiple of ample and concludes from
$\linearsystem{12K}=\emptyset$ by 6.1 that $X$ is rational or ruled; Yang
gives the same three tuples at printed p. 115, as the case
$\sum d_i-n-1<0$.
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

Yang gives these three tuples at printed p. 115, as the case
$\sum d_i-n-1=0$, and records that they are K3 surfaces; Egbert, printed
p. 303, places them so, taking $n=4$ with $(d_1,d_2)=(2,3)$ and $n=5$ with
$(2,2,2)$, where $K_X\equiv0$, and citing Theorem 6.3, which
lists the surfaces of Kodaira dimension zero with those invariants. The
verification above, that $\omega_X\cong\OO_X$ with $H^1(X,\OO_X)=0$ gives
$q=0$ and $p_g=1$, is the card's own.
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
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.6, exercise 6.1, printed p. 423, and the classification it asks the exceptions to be placed in is Theorems 6.1--6.5, printed p. 422: $\kappa=-1$ for the rational and ruled surfaces, $\kappa=0$ for the K3, Enriques, abelian and hyperelliptic surfaces, $\kappa=1$ for the elliptic ones, and $\kappa=2$ for the surfaces of general type.

Yang Pi-Yeh, *Hartshorne Solutions*, solution 5.6.1, printed p. 115, gives both enumerations: $\sum_i d_i-n-1<0$ with the tuples $(3;2)$, $(3;3)$, $(4;2,2)$, and $\sum_i d_i-n-1=0$ with the tuples $(3;4)$, $(4;2,3)$, $(5;2,2,2)$, which he records as K3 surfaces. His bounds are $n<5$ and $n\le5$, that is $2(n-2)\le n$ and $2(n-2)\le n+1$.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.6.1, printed p. 303, places two of the cases: for $n=3$ with $d_1=2$ or $d_1=3$ the canonical class is a negative multiple of the ample hyperplane class, so $\linearsystem{12K}=\emptyset$ and Theorem 6.1 makes $X$ rational or ruled; for $n=4$ with $(2,3)$ and $n=5$ with $(2,2,2)$ the canonical class is trivial, and $X$ is K3 by Theorem 6.3.
:::
