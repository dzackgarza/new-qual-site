---
schema: qual/card@1
id: P-JHUSP01CAF
kind: problem
title: Gauss--Lucas theorem for polynomial critical points
classification:
  areas:
  - complex-analysis
  topics:
  - Gauss-Lucas Theorem
  - Zeros of Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the derivative-zero and convex-hull conclusion with Spring 2001 Complex Analysis question 6; added the standard nonconstant hypothesis omitted by the printed source."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Handled derivative zeros that are polynomial roots directly; for any other critical point outside the convex hull, used the closest-point inequality to put all logarithmic-derivative summands in one strict half-plane, contradicting P'/P=0."
---

::: problem
Let $P$ be a nonconstant complex polynomial. Show that every zero of $P'$ lies
in the convex hull of the zeros of $P$.
:::


::: remark
The nonconstant hypothesis is necessary to state the theorem: for a constant
polynomial, $P'$ is the zero polynomial and the asserted containment of its
zeros is not a meaningful Gauss--Lucas statement.
:::

::: solution
Let $K$ be the convex hull of the zeros of $P$.

<1>1. A critical point that is itself a zero of $P$ already lies in $K$.
::: proof
If $w$ satisfies $P'(w)=0$ and also $P(w)=0$, then $w$ is one of the zeros used
to form the convex hull $K$. Hence $w\in K$. It remains only to consider a
critical point $w$ with $P(w)\ne0$.
:::

<1>2. A point outside $K$ admits a direction in which every vector from a root to that point has positive real projection.
::: proof
Suppose $w\notin K$. The set $K$ is compact and convex, so there is a point
$q\in K$ minimizing $|w-q|$. Put $v=w-q\ne0$.

For any $\zeta\in K$ and $0\le t\le1$, convexity gives
$q+t(\zeta-q)\in K$. Minimality of $q$ implies
$$
|w-q|^2\le |w-q-t(\zeta-q)|^2.
$$
Expanding and dividing by $t>0$, then letting $t\downarrow0$, gives
$$
\operatorname{Re}\bigl(\overline v(\zeta-q)\bigr)\le0.
$$
Therefore
$$
\operatorname{Re}\bigl(v\,\overline{(w-\zeta)}\bigr)
=|v|^2-\operatorname{Re}\bigl(\overline v(\zeta-q)\bigr)
\ge |v|^2>0.
$$
In particular this holds for every zero $\zeta$ of $P$.
:::

<1>3. The logarithmic derivative rules out a critical point outside $K$.
::: proof
Factor
$$
P(z)=c\prod_{j=1}^n(z-\zeta_j),
$$
where the roots are repeated according to multiplicity. At a point
$w$ with $P(w)\ne0$,
$$
\frac{P'(w)}{P(w)}=\sum_{j=1}^n\frac1{w-\zeta_j}.
$$
If in addition $w\notin K$, step <1>2 gives for every $j$
$$
\operatorname{Re}\left(\frac{v}{w-\zeta_j}\right)
=\frac{\operatorname{Re}\bigl(v\overline{(w-\zeta_j)}\bigr)}{|w-\zeta_j|^2}>0.
$$
Hence
$$
\operatorname{Re}\left(
v\frac{P'(w)}{P(w)}\right)
=\sum_{j=1}^n
\operatorname{Re}\left(\frac{v}{w-\zeta_j}\right)>0.
$$
This is impossible if $P'(w)=0$. Thus no zero of $P'$ lying outside the root
set of $P$ can be outside $K$. Together with step <1>1, every zero of $P'$ lies
in the convex hull of the zeros of $P$.
:::
:::
