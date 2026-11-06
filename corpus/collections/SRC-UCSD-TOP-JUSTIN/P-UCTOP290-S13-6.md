---
schema: qual/card@1
id: P-UCTOP290-S13-6
kind: problem
title: Cohomology and manifold type of a projective-space quotient
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Poincaré Duality
  - Projective Spaces
relations: []
review: draft
audit:
- event: source-corrected
  by: chatgpt
  date: 2026-10-31
  note: >-
    Justin sheet 13, Problem 6 asks when the quotient is homotopy
    equivalent to a manifold, without specifying closedness.
    Every finite CW complex has the homotopy type of an open
    manifold by regular-neighborhood thickening. The intended
    Poincare-duality obstruction concerns closed manifolds, so
    both readings are answered.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 13, problem 6
    (assets/attachments/UCSD_290_F14_sheet13.pdf, printed page 389), from the
    checked-in extraction and a 300 dpi render. The printed problem is: for
    n >= 2 and 0 < k < n, let X = CP^n/CP^k, calculate the integral cohomology
    ring of X, and say for which n and k (as above) X is homotopy-equivalent to a
    manifold. The card asks in addition whether the manifold may be taken
    closed, and answers the noncompact case separately. That addition is
    necessary rather than ornamental: every finite CW complex is homotopy
    equivalent to an open manifold, so the printed question without closedness
    has the trivial answer "always", and the card records the reading in a
    source-corrected event that was checked here and stands.
---

::: {.problem}
Let $0<k<n$ and
$X=\CP^n/\CP^k$. Compute the integral cohomology ring of $X$.
For which $n,k$ is $X$ homotopy equivalent to a closed manifold?
What changes if noncompact manifolds are allowed?
:::

::: {.solution}

Let $0<k<n$, let $q\colon\CP^n\to X=\CP^n/\CP^k$ collapse $\CP^k$ to a point,
and recall $H^*(\CP^n;\ZZ)=\ZZ[x]/(x^{n+1})$ with $\deg x=2$.

::: pf

::: {.pf-step #ring}

As a graded ring, $H^*(X;\ZZ)\cong\ZZ\oplus\bigoplus_{j=k+1}^{n}\ZZ u_j$ with
$\deg u_j=2j$, $q^*(u_j)=x^j$, and $u_iu_j=u_{i+j}$ when $i+j\le n$,
$u_iu_j=0$ otherwise.

::: pf-proof

$\CP^k$ is the $2k$-skeleton of the standard cell structure of $\CP^n$, so $X$
is a CW complex with one $0$-cell and one cell in each even dimension
$2k+2,2k+4,\dots,2n$; hence $H^{2j}(X;\ZZ)=\ZZ$ for those $j$ and $0$
otherwise, which is the additive statement. The pair $(\CP^n,\CP^k)$ gives the
exact sequence $H^*(\CP^n,\CP^k)\to H^*(\CP^n)\xrightarrow{j^*}H^*(\CP^k)$,
where $j^*$ kills $x^{k+1}$ and above and is injective in degrees at most
$2k$; so $H^*(\CP^n,\CP^k)$ is the ideal $(x^{k+1})\subseteq\ZZ[x]/(x^{n+1})$,
the free group on $x^{k+1},\dots,x^{n}$. Excision identifies
$H^*(\CP^n,\CP^k)$ with the reduced cohomology of $X$, and under this
identification the class named $u_j$ is $x^j$; the ring structure transported
from the ideal is $x^ix^j=x^{i+j}$ when $i+j\le n$ and $0$ when $i+j>n$. That
the identification is multiplicative, not just additive, follows because
$q^*\colon H^*(X)\to H^*(\CP^n)$ is injective with image the ideal and is a
ring map, so $u_iu_j$ is the unique class with $q^*(u_iu_j)=x^{i+j}$.

:::

:::

::: {.pf-step #sphere}

If $n=k+1$ then $X$ is homeomorphic to $S^{2n}$.

::: pf-proof

Then $2k+2=2n$, so the only cell of $X$ above the basepoint is one in
dimension $2n$; a CW complex with one $0$-cell and one $2n$-cell, $2n\ge2$, is
obtained from a point by attaching a $2n$-cell along a map into a point, which
is $S^{2n}$.

:::

:::

::: {.pf-step #obstruction}

If $n\ge k+2$ then $X$ is not homotopy equivalent to any closed manifold.

::: pf-proof

Over $\FF_2$ the same cell count gives $H^2(X;\FF_2)=0$, because the smallest
positive-dimensional cell has dimension $2k+2\ge4$, and
$H^{2n-2}(X;\FF_2)=\FF_2$, because $2n-2\ge2k+2$ and is one of the degrees
$2k+2,\dots,2n$. Suppose $X\simeq M$ with $M$ a closed $m$-manifold. Since
$H^{2n}(X;\FF_2)=\FF_2$ and $H^{i}(X;\FF_2)=0$ for $i>2n$, we get $2n\le m$
from the first and $m\le2n$ because $H^m(M;\FF_2)=\FF_2\ne0$ must sit in a
nonzero group of $X$; so $m=2n$. Poincaré duality over the field $\FF_2$ gives
$H^i(M;\FF_2)\cong H_{m-i}(M;\FF_2)$ and, by the universal coefficient theorem
over a field, $\dim H^i(M)=\dim H^{m-i}(M)$; with $m=2n$ that makes $\dim
H^2(M;\FF_2)=\dim H^{2n-2}(M;\FF_2)$, that is $0=1$, a contradiction.

:::

:::

::: {.pf-step #noncompact}

If noncompact manifolds are allowed then every pair $0<k<n$ gives a manifold
homotopy equivalent to $X$, namely the interior of a regular neighbourhood of
an embedding of the finite CW complex $X$ in a Euclidean space.

::: pf-proof

A finite CW complex embeds in $\RR^N$ for large $N$, being a compact metric
space of finite dimension, and it has a regular neighbourhood: a compact
manifold with boundary $W\subset\RR^N$ that deform retracts onto $X$. The
interior of $W$ is a manifold without boundary, and it is homotopy equivalent
to $W$, hence to $X$. So the closedness in the previous steps is exactly what
makes the question nontrivial, and the answer for closed manifolds is $n=k+1$
alone by steps [](#sphere){.pf-ref} and [](#obstruction){.pf-ref}.

:::

:::

:::


:::
