---
schema: qual/card@1
id: E-XIHWT
kind: problem
title: Distance to a set in a metric space
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 2, printed p. 177, with Theorem
    27.4, Lemma 26.4 and the Lebesgue number lemma; the five parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.2, PDF p. 16. The distance to A vanishes
    exactly on the closure, is attained when A is compact, and its sublevel sets are unions
    of balls; compactness of A gives a Lebesgue number for a finite cover of A by balls
    inside U, and the tangent graph shows the compactness cannot be dropped.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. Pages verified: the exercise on printed p. 177, and the
    extreme value theorem on printed p. 174. Repair in part (d): the retained argument took
    the Lebesgue number delta of the finite cover of A and put epsilon = delta/2, but the
    ball B_d(a,epsilon) has diameter exactly delta, while the Lebesgue lemma needs a diameter
    strictly below the number, and the lemma speaks of subsets of A while that ball is not one
    -- so the inclusion of the ball in a member of the cover did not follow. The part is now
    proved by the function g(a) = d(a, X - U), which is Lipschitz hence continuous on A and
    positive at each a in A because U is open, so that by the extreme value theorem it has a
    positive minimum delta on A, and then d(a,z) >= delta for every z outside U gives
    U(A, delta/2) inside U by the triangle inequality. Two steps sharpened: continuity of
    a -> d(x,a) in part (b) is now derived from the Lipschitz estimate instead of being cited
    from Exercise 20.3, and part (e) now names the point that witnesses the failure -- with
    nu < epsilon the point (pi/2, tan(pi/2 - nu)) lies outside U and within nu of the point
    (pi/2 - nu, tan(pi/2 - nu)) of C -- instead of saying only that some point of C is near
    the complement. No repair to the statement.
---

::: {.exercise}

Let $X$ be a metric space with metric $d$; let $A \subset X$ be nonempty.

(a) Show that $d(x, A) = 0$ if and only if $x \in \overline{A}$.

(b) Show that if $A$ is compact, $d(x, A) = d(x, a)$ for some $a \in A$.

(c) Define the $\epsilon$-neighborhood of $A$ in $X$ to be the set

$$
U(A, \epsilon) = \theset{x \mid d(x, A) < \epsilon}.
$$

Show that $U(A, \epsilon)$ equals the union of the open balls $B_d(a, \epsilon)$ for $a \in A$.

(d) Assume that $A$ is compact; let $U$ be an open set containing $A$.
Show that some $\epsilon$-neighborhood of $A$ is contained in $U$.

(e) Show the result in (d) need not hold if $A$ is closed but not compact.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.2, PDF p. 16** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps; part (d) is proved here by the minimum of $d(\cdot,X-U)$ rather than by the Lebesgue number, the argument given there needing a diameter that is strictly smaller than the number and a cover of $A$ alone.

Throughout $X$ is a metric space with metric $d$, $A\subset X$ is nonempty, $d(x,A)=\inf\theset{d(x,a) \mid a\in A}$, and $U(A,\varepsilon)=\theset{x \mid d(x,A)<\varepsilon}$; the exercise is §27 Exercise 2 (printed p. 177). Two facts are used repeatedly and proved where they are needed: for fixed $x$ the function $a\mapsto d(x,a)$ is continuous, and so is $a\mapsto d(a,B)$ for a fixed set $B\ne\varnothing$; and a continuous real-valued function on a compact space attains its minimum (the extreme value theorem, Theorem 27.4, printed p. 174).

::: pf

::: {.pf-step #a}
(a) $d(x,A)=0$ if and only if $x\in\closure{A}$.

::: pf-proof
If $d(x,A)=\delta>0$ then $B_d(x,\delta)$ meets $A$ in nothing, since $a\in A\cap B_d(x,\delta)$ would give $d(x,A)\le d(x,a)<\delta$. Conversely let $x\notin\closure{A}$; then there is $\delta>0$ with $B_d(x,\delta)\cap A=\emptyset$, so $d(x,a)\ge\delta$ for every $a\in A$ and $d(x,A)\ge\delta>0$.
:::

:::

::: {.pf-step #b}
(b) If $A$ is compact then $d(x,A)=d(x,a)$ for some $a\in A$.

::: pf-proof
For fixed $x$ the function $d_x:A\to\RR$, $d_x(a)=d(x,a)$, satisfies
$$
\abs{d_x(a)-d_x(a')}\le d(a,a'),
$$
so it is continuous; $A$ is compact, so by the extreme value theorem (Theorem 27.4, printed p. 174) it attains a minimum at some $a\in A$. A minimum of $d_x$ over $A$ is the infimum $d(x,A)$, which is therefore equal to $d(x,a)$.
:::

:::

::: {.pf-step #c}
(c) $U(A,\varepsilon)=\bigcup_{a\in A}B_d(a,\varepsilon)$.

::: pf-proof
If $y\in U(A,\varepsilon)$ then $d(y,A)<\varepsilon$, and since $d(y,A)$ is an infimum there is $a\in A$ with $d(y,a)<\varepsilon$, that is $y\in B_d(a,\varepsilon)$. Conversely if $y\in B_d(a,\varepsilon)$ then $d(y,A)\le d(y,a)<\varepsilon$.
:::

:::

::: {.pf-step #d}
(d) If $A$ is compact and $U$ is an open set containing $A$, then $U(A,\varepsilon)\subset U$ for some $\varepsilon>0$.

::: pf-proof

::: {.pf-step #complement-distance}
The function $g(a)=d(a,X-U)$ is continuous on $A$ and positive at every point of $A$.

::: pf-proof
Continuity: for $a,a'\in A$ and any $z\in X-U$ one has $d(a,X-U)\le d(a,z)\le d(a,a')+d(a',z)$, and taking the infimum over $z$ gives $d(a,X-U)\le d(a,a')+d(a',X-U)$, which with the roles exchanged is $\abs{g(a)-g(a')}\le d(a,a')$. Positivity: if $a\in A$ then $a\in U$ with $U$ open, so some ball $B_d(a,\rho)$ lies in $U$, and then $d(a,z)\ge\rho$ for every $z\in X-U$, that is $g(a)\ge\rho>0$.
:::

:::

::: {.pf-step #minimum}
$g$ attains a positive minimum $\delta$ on $A$.

::: pf-proof
$A$ is compact, so $g$ attains its minimum $\delta$ at some point of $A$ by the extreme value theorem (Theorem 27.4, printed p. 174); by the previous step that minimum is positive.
:::

:::

::: {.pf-step #neighbourhood}
$U(A,\delta/2)\subset U$.

::: pf-proof
Let $x\in U(A,\delta/2)$; since $d(x,A)$ is an infimum there is $a\in A$ with $d(x,a)<\delta/2$. For every $z\in X-U$,
$$
d(x,z)\ge d(a,z)-d(a,x)\ge\delta-d(x,a)>\delta/2>0,
$$
using $d(a,z)\ge g(a)\ge\delta$. So $x\notin X-U$, that is $x\in U$.
:::

:::

:::

:::

::: {.pf-step}
(e) The compactness in (d) cannot be dropped: with $C$ the graph of $\tan$ over $(-\pi/2,\pi/2)$ and $U=(-\pi/2,\pi/2)\times\RR$ there is no $\varepsilon>0$ with $U(C,\varepsilon)\subset U$; together with steps [](#a){.pf-ref} to [](#d){.pf-ref} this proves the exercise.

::: pf-proof
Let $C=\theset{(x,\tan x) \mid -\pi/2<x<\pi/2}\subset\RR^2$, the graph of a continuous function on an open interval. It is closed: if $(x_n,\tan x_n)$ converges in $\RR^2$ to $(x,y)$, then $x_n\to x$ with $x\in[-\pi/2,\pi/2]$, and boundedness of $\tan x_n$ forces $x\in(-\pi/2,\pi/2)$, where continuity gives $y=\tan x$; so $C$ contains all its limits. It is not compact, being unbounded: $\tan x\to\infty$ as $x\to\pi/2$. The set $U=(-\pi/2,\pi/2)\times\RR$ is open in $\RR^2$ and contains $C$. Now fix $\varepsilon>0$ and choose $0<\nu<\min\{\varepsilon,\pi/2\}$; put $Y=\tan(\pi/2-\nu)$, a real number, and $q=(\pi/2,Y)$. Then $q\notin U$, since its first coordinate is $\pi/2$, while
$$
d(q,C)\le d\big(q,(\pi/2-\nu,Y)\big)=\nu<\varepsilon,
$$
because $(\pi/2-\nu,Y)\in C$. So $q\in U(C,\varepsilon)-U$, and no $\varepsilon$-neighbourhood of $C$ is contained in $U$: the hypothesis that $A$ is compact in (d) cannot be replaced by closedness.
:::

:::

:::
:::
