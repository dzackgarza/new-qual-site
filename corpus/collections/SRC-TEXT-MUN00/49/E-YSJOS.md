---
schema: qual/card@1
id: E-YSJOS
kind: problem
title: Secant-quotient bounds for the building blocks of a nowhere-differentiable function
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §49 Exercise 1 (printed p. 304) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against Example 1 of §49, printed
    p. 301, and the definition of Delta f(x,h) and of U_n on the same page. The three computations were
    verified: for f(x) = 4 alpha x(1-x) with h = 1/4 the two one-sided quotients are alpha(3 - 8x) and
    alpha(5 - 8x), whose difference is 2 alpha, so the larger is at least alpha in absolute value, and at an
    endpoint the single defined quotient has absolute value at least alpha; for the tent g and for the two-tooth
    sawtooth k every linear piece has slope of absolute value alpha, and an interval of length at most half the
    vertex spacing lies in a single piece. What was corrected: the card had restricted the conclusions to
    n >= 4 for g and n >= 8 for k, because it took h = 1/n and needed h <= 1/4 and h <= 1/8; the book asserts
    both for every n with alpha > n, and the card now takes h = min{1/n, 1/4} and h = min{1/n, 1/8}. The
    argument that one of the two intervals has no vertex in its interior is now given, in place of the bare
    statement that the vertices are spaced further apart than the step.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The only located treatment of Munkres §49 Exercise 1 (printed
    p. 304) is the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630), whose answer to §49 Exercise 1 survives in the
    extraction only as the connectives between its formulas ("Observe that for and , For and , either or , so
    ."), so nothing of it can be read or transcribed, and the site answers an automated request with a human
    check, which was not worked around. Murayama's selection has no Chapter 8, dbFin has no chapter-7 or
    chapter-8 page, the ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop before §36,
    and the Stack Exchange queries "nowhere differentiable U_n Munkres" and "continuous function arbitrary small
    nowhere differentiable dense" returned nothing on the section. The card's reading of the two figures was
    checked against the page image: Figure 49.1 on printed p. 301 (PDF p. 316 of
    tmp/sources/munkres-2000-topology.pdf) shows $g$ as a tent of height $\alpha/2$ with its vertex at $1/2$,
    and $k$ as a two-tooth sawtooth of height $\alpha/4$ with teeth at $1/4$ and $3/4$, which is what the card
    computes with, and the thresholds $h\le1/4$ for $g$ and $h\le1/8$ for $k$ are the ones the book states.
    Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. The argument for $k$ said that one of the two intervals of length $h$ has no vertex
    in its interior and is therefore contained in one linear piece; at $x=0$ the backward interval leaves
    $[0,1]$ and at $x=1$ the forward one does, so there is no such interval there to be contained in a piece.
    The endpoint cases are now separate: at $x=0$ the interval $[0,h]\subseteq[0,1/4]$, and at $x=1$ the
    interval $[1-h,1]\subseteq[3/4,1]$, since $h\le1/8$ is below the vertex spacing $1/4$. For $0<x<1$ the
    two-interval argument stands, and the passage from "no vertex in the interior" to "inside one linear piece"
    is now drawn from the interior lying in one component of $I$ minus the vertices. The parts for $f$ and $g$
    are unchanged: $f$'s quotients are covered by the endpoint cases already on the card, and $g$'s split
    $x\le1/2$, $x\ge1/2$ keeps both intervals inside $I$ because $h\le1/4$.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that the sentence "For 0 < x < 1 both intervals lie in I" is false at
    x < h and at x > 1 - h, where the backward or the forward interval leaves I. The step now argues that
    an interval leaving I has 0 or 1 in its interior, that 0 and 1 are vertices of k, and hence that the
    interval which has no vertex in its interior lies in I, which is what the passage to "lies in one
    linear piece" needs; it also corrects "distinct vertices are at distance exactly 1/4" to "at least
    1/4", the vertices 0 and 1/2 being half an interval apart. Nothing else on the card changed.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for Munkres, Topology (2000), Section 49 Exercise 1, printed p. 304, checked against Example 1 and the definitions on printed p. 301. No retained set covers the exercise, so the argument is the card's own and the card now says so. What the restructuring repaired: the prose concluded "g in U_n" and "k in U_n" without ever stating the definition it was concluding against. The definition on p. 301 is Delta_h f = inf over x of Delta f(x,h) and f in U_n iff Delta_h f > n for some h <= 1/n, so membership needs the bound at EVERY x and the step to be at most 1/n; the card now states the definition and proves the criterion once (step 1) and applies it. The two endpoint cases of g and of k, the quotient computations for f at h = 1/4, and the passage from "no vertex in the interior" to "contained in one closed linear piece" are each separate steps. The numerical thresholds are unchanged from the checked version: h = 1/4 for f, h <= 1/4 for g, h <= 1/8 for k. No statement repair.
---

::: {.exercise}

Check the stated properties of the functions $f$, $g$, and $k$ of Example 1 of §49.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the textbook, and the searches for this exercise are recorded on the card and in the `COMPLAINTS.md` entry for §43--§50 of `SRC-TEXT-MUN00`. The argument below is the card's own, following Example 1 of §49, printed p. 301, and the definitions on the same page.

Write $I=[0,1]$ and let $\alpha>0$. For $f:I\to\RR$ continuous, $x\in I$ and $0<h\le1/2$, let
$$
\Delta f(x,h)=\max\Big\{\frac{\abs{f(x+h)-f(x)}}{h},\ \frac{\abs{f(x-h)-f(x)}}{h}\Big\},
$$
each term taken only when defined, and let $\Delta_h f=\inf\{\Delta f(x,h)\mid x\in I\}$. For $n\ge2$, $f\in U_n$ means that $\Delta_h f>n$ for some $0<h\le1/n$ (Definition and Example 1, printed p. 301).

::: pf

::: {.pf-step #criterion}
For $n\ge2$ and continuous $f:I\to\RR$: if $\Delta f(x,h)\ge\alpha$ for all $x\in I$ and some $0<h\le1/n$, and $\alpha>n$, then $f\in U_n$.

::: pf-proof
$\Delta_h f=\inf_x\Delta f(x,h)\ge\alpha>n$ because $\alpha\le\Delta f(x,h)$ for every $x$, and $h\le1/n$; this is exactly the condition in the definition of $U_n$ (printed p. 301).
:::

:::

::: {.pf-step #parabola}
Let $f(x)=4\alpha x(1-x)$ and $h=1/4$. For every $x\in I$, $\Delta f(x,1/4)\ge\alpha$.

::: pf-proof
This is proved in the three steps below: the two secant quotients for the interior case, and the two endpoint cases.

::: {.pf-step #quotients}
For $0\le x\le1$ with both quotients defined,
$$
\frac{f(x+h)-f(x)}{h}=\alpha(3-8x),\qquad
\frac{f(x-h)-f(x)}{-h}=\alpha(5-8x).
$$

::: pf-proof
With $h=1/4$ and $f=4\alpha x(1-x)$,
$$
f(x+h)-f(x)=4\alpha\big[(x+h)(1-x-h)-x(1-x)\big]=4\alpha\,h\,(1-2x-h)=h\,\alpha(3-8x),
$$
and
$$
f(x-h)-f(x)=4\alpha\big[(x-h)(1-x+h)-x(1-x)\big]=-4\alpha\,h\,(1-2x+h)=h\,\alpha(5-8x)\cdot(-1),
$$
so dividing the first by $h=1/4$ and the second by $-h=-1/4$ gives the two displayed quotient formulas. (Numerically: $4(1-2x-1/4)=3-8x$ and $-4(1-2x+1/4)=-(3-8x)-2=5-8x$.)
:::

:::

::: {.pf-step #interior}
For $1/4\le x\le3/4$ both quotients are defined and one has absolute value at least $\alpha$.

::: pf-proof
$x+1/4\le1$ and $x-1/4\ge0$ here, so both quotients are defined. Their difference is $\alpha(5-8x)-\alpha(3-8x)=2\alpha$, and for two real numbers differing by $2\alpha$ at least one has absolute value at least $\alpha$.
:::

:::

::: {.pf-step #endpoints}
For $0\le x<1/4$ the forward quotient is defined and has absolute value at least $\alpha$; for $3/4<x\le1$ the backward quotient is defined and has absolute value at least $\alpha$.

::: pf-proof
If $0\le x<1/4$ then $x+1/4\le1/2\le1$, so the forward quotient is defined, and $\abs{3-8x}\ge\abs{3-2}=1$ because $8x<2$, so it has absolute value $\alpha\abs{3-8x}\ge\alpha$. If $3/4<x\le1$ then $x-1/4\ge1/2\ge0$, so the backward quotient is defined, and $\abs{5-8x}\ge\abs{5-8}=3\ge1$ because $8x\le8$, so it has absolute value at least $\alpha$.
:::

:::

:::

:::
::: {.pf-step #parabolamember}
If $\alpha>4$ then $f\in U_4$.

::: pf-proof
By step [](#parabola){.pf-ref}, $\Delta f(x,1/4)\ge\alpha>4$ for all $x\in I$, and $1/4\le1/4$; step [](#criterion){.pf-ref} with $n=4$ and $h=1/4$ gives $f\in U_4$.
:::

:::

::: {.pf-step #tent}
Let $g(x)=\alpha x$ for $0\le x\le1/2$ and $g(x)=\alpha(1-x)$ for $1/2\le x\le1$. For every $x\in I$ and every $0<h\le1/4$, $\Delta g(x,h)\ge\alpha$.

::: pf-proof
$g$ is linear of slope $\alpha$ on $[0,1/2]$ and of slope $-\alpha$ on $[1/2,1]$, so on each of the two closed pieces $g$ is linear with slope of absolute value $\alpha$, and a secant quotient over an interval contained in one piece equals that slope.

::: {.pf-step #tentleft}
If $x\le1/2$ then one of the two quotients is defined and has absolute value $\alpha$.

::: pf-proof
If $x+h\le1/2$, the forward interval $[x,x+h]$ lies in $[0,1/2]$ and the forward quotient has absolute value $\alpha$. Otherwise $x>1/2-h\ge1/4$, and $x-h\ge1/2-2h\ge0$ because $h\le1/4$, while $x\le1/2$; so the backward interval $[x-h,x]$ lies in $[0,1/2]$ and the backward quotient has absolute value $\alpha$. (At $x=0$ the first case applies, since $h\le1/4\le1/2$.)
:::

:::

::: {.pf-step #tentright}
If $x\ge1/2$ then one of the two quotients is defined and has absolute value $\alpha$.

::: pf-proof
If $x-h\ge1/2$, the backward interval $[x-h,x]$ lies in $[1/2,1]$ because $x\le1$, and the backward quotient has absolute value $\alpha$. Otherwise $x<1/2+h$, and $x+h\le1/2+2h\le1$ because $h\le1/4$, while $x\ge1/2$; so the forward interval $[x,x+h]$ lies in $[1/2,1]$ and the forward quotient has absolute value $\alpha$. (At $x=1$ the first case applies.)
:::

:::

:::

:::

::: {.pf-step #tentmember}
If $\alpha>n$ with $n\ge2$ then $g\in U_n$.

::: pf-proof
Put $h=\min\{1/n,1/4\}$, a positive number with $h\le1/n$ and $h\le1/4$. By step [](#tent){.pf-ref}, $\Delta g(x,h)\ge\alpha>n$ for every $x$, so step [](#criterion){.pf-ref} gives $g\in U_n$.
:::

:::

::: {.pf-step #sawtooth}
Let $k$ be the piecewise linear function with values $0,\alpha/4,0,\alpha/4,0$ at $0,1/4,1/2,3/4,1$. Its vertices are $0,1/4,1/2,3/4,1$, distinct vertices are at distance at least $1/4$, and on each of the four closed pieces $k$ is linear with slope of absolute value $\alpha$.

::: pf-proof
Successive vertices are at distance exactly $1/4$, so any two distinct vertices are at distance at least $1/4$. On $[0,1/4]$ the slope is $(\alpha/4-0)/(1/4)=\alpha$; on $[1/4,1/2]$ it is $(0-\alpha/4)/(1/4)=-\alpha$; on $[1/2,3/4]$ it is $\alpha$; on $[3/4,1]$ it is $-\alpha$. A function linear on a closed interval has every secant quotient over a subinterval equal to its slope.
:::

:::

::: {.pf-step #sawtoothbound}
For every $x\in I$ and every $0<h\le1/8$, $\Delta k(x,h)\ge\alpha$.

::: pf-proof
The endpoint cases and the two-interval argument follow in the three steps below.

::: {.pf-step #sawends}
At $x=0$ the forward interval $[0,h]$ lies in $[0,1/4]$, and at $x=1$ the backward interval $[1-h,1]$ lies in $[3/4,1]$.

::: pf-proof
$h\le1/8<1/4$ gives $[0,h]\subseteq[0,1/4]$ and $[1-h,1]\subseteq[3/4,1]$. So the corresponding quotient, a secant quotient over an interval inside one linear piece, has absolute value $\alpha$ by step [](#sawtooth){.pf-ref}.
:::

:::

::: {.pf-step #onevertex}
For $0<x<1$ at least one of the intervals $[x-h,x]$ and $[x,x+h]$ has no vertex in its interior.

::: pf-proof
Suppose both have one, say $t\in(x-h,x)$ and $t'\in(x,x+h)$ with $t,t'$ vertices. Then $t'-t<(x+h)-(x-h)=2h\le1/4$, contradicting step [](#sawtooth){.pf-ref}, which separates distinct vertices by at least $1/4$.
:::

:::

::: {.pf-step #onepiece}
For $0<x<1$ an interval among $[x-h,x]$ and $[x,x+h]$ with no vertex in its interior is contained in $I$ and in one of the four closed linear pieces.

::: pf-proof
If $[x-h,x]$ left $I$ then $x-h<0$ with $x>0$, so $0\in(x-h,x)$ is a vertex in the interior; if $[x,x+h]$ left $I$ then $x+h>1$ with $x<1$, so $1\in(x,x+h)$ is a vertex in the interior. So such an interval lies in $I$. Its interior is an interval in $I$ avoiding the four vertices, hence lies in one component of $I$ minus the vertices, one of the four open pieces; the interval is the closure in $I$ of its interior, so it lies in the closure of that piece, which is one of the four closed linear pieces. Hence the secant quotient over it has absolute value $\alpha$ by step [](#sawtooth){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #sawtoothmember}
If $\alpha>n$ with $n\ge2$ then $k\in U_n$.

::: pf-proof
Put $h=\min\{1/n,1/8\}$, so that $0<h\le1/n$ and $h\le1/8$. By step [](#sawtoothbound){.pf-ref}, $\Delta k(x,h)\ge\alpha>n$ for every $x$, and step [](#criterion){.pf-ref} gives $k\in U_n$.
:::

:::

::: {.pf-step}
The three functions satisfy exactly the properties that Example 1 of §49 states for them: $\Delta f(x,1/4)\ge\alpha$ with $f\in U_4$ when $\alpha>4$; $\Delta g(x,h)\ge\alpha$ for $h\le1/4$ with $g\in U_n$ when $\alpha>n$; and $\Delta k(x,h)\ge\alpha$ for $h\le1/8$ with $k\in U_n$ when $\alpha>n$.

::: pf-proof
Steps [](#parabola){.pf-ref}, [](#parabolamember){.pf-ref}, [](#tent){.pf-ref}, [](#tentmember){.pf-ref}, [](#sawtoothbound){.pf-ref} and [](#sawtoothmember){.pf-ref} prove the six assertions, which are those of Example 1 (printed p. 301) word for word: "$\Delta f(x,h)\ge\alpha$ for $h=1/4$ and all $x$", "if $\alpha>4$ the function $f$ belongs to $U_4$", "$\Delta g(x,h)\ge\alpha$ for any $h\le1/4$", "hence $g$ belongs to $U_n$ provided $\alpha>n$", and the same two statements for $k$ with $1/8$ in place of $1/4$.
:::

:::

:::
:::
