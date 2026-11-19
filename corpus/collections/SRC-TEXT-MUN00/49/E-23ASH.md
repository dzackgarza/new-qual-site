---
schema: qual/card@1
id: E-23ASH
kind: problem
title: Small functions in the nowhere-differentiability open sets
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §49 Exercise 2 (printed p. 304) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. The exercise has to be read with the book's own set U_n,
    defined on printed p. 301: for n >= 2, f lies in U_n iff for some h with 0 < h <= 1/n one has Delta_h f > n,
    where Delta_h f is the infimum over x of the larger of the two step-h difference quotients. What was
    corrected: the card had stated U_n as a pointwise condition, with a step t allowed to depend on the point x
    and only on the bound |x - t| < 1/n, and had checked that condition for its sawtooth; the book's condition is
    that one single step h works uniformly at every point, and the card's own sawtooth does not satisfy the
    pointwise condition it had written either, since at a point where the height is eps/2 the step-h secant
    along the rising side can vanish. The solution now proves the book's condition: with mesh delta = 1/(2k) and
    step h = delta/2 = 1/(4k), at most one of the intervals [x-h,x] and [x,x+h] contains a vertex in its
    interior, so the other lies in a single linear piece of slope eps/delta, and choosing 2k eps > n and
    4k >= n gives Delta_h f > n with h <= 1/n, while 0 <= f <= eps.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The only located treatment of Munkres §49 Exercise 2 (printed
    p. 304) is the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630), whose answer survives in the extraction as
    "We may let for if is even and for if is odd", that is, an alternating $\pm\varepsilon$ on a partition,
    with every formula lost; the site answers an automated request with a human check, which was not worked
    around, so nothing of it can be read or transcribed. Murayama's selection has no Chapter 8, dbFin has no
    chapter-7 or chapter-8 page, the ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop
    before §36, and the Stack Exchange queries "nowhere differentiable U_n Munkres" and "continuous function
    arbitrary small nowhere differentiable dense" returned nothing on the section. The alternating function
    that post suggests is the card's sawtooth with values $0$ and $\varepsilon$ instead of
    $\pm\varepsilon$; both need the same mesh condition, which the card writes out: with mesh $\delta$ and
    step $h=\delta/2$ only one of $[x-h,x]$ and $[x,x+h]$ can contain a vertex, so that interval lies in one
    linear piece of slope $\varepsilon/\delta$, and choosing $2k\varepsilon>n$ and $4k\ge n$ gives
    $\Delta_h f>n$ with $h\le1/n$. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. The argument said that at least one of $[x-h,x]$, $[x,x+h]$ has no vertex in its
    interior and hence lies in one linear piece; at $x=0$ the backward interval leaves $I$ and at $x=1$ the
    forward one does, so neither is an interval of a linear piece there. The endpoint cases are now separate:
    $[0,h]\subseteq[0,\delta]$ and $[1-h,1]\subseteq[1-\delta,1]$, one piece each because $h=\delta/2<\delta$.
    For $0<x<1$ the two-interval argument stands, and the conclusion that the vertex-free interval lies in a
    single linear piece is drawn from its interior lying in one component of $I$ minus the vertices. Nothing
    else changed: the constants, the mesh $\delta=1/(2k)$, the bound $0\le f\le\varepsilon$ and the choice
    $2k\varepsilon>n$, $4k\ge n$ are as before.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that the sentence "For 0 < x < 1 both intervals lie in I" is false at
    x < h and at x > 1 - h, where the backward or the forward interval of length h leaves I. The step now
    argues that an interval leaving I has 0 or 1 in its interior, that t_0 = 0 and t_{2k} = 1 are vertices
    of this sawtooth, and hence that the interval which has no vertex in its interior lies in I, which is
    what the passage to "lies in one linear piece" needs. Nothing else on the card changed.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked the construction: $k$ with
    $2k\varepsilon>n$ and $4k\ge n$ exists since $\varepsilon>0$; the sawtooth is continuous and
    takes values in $[0,\varepsilon]$ with every slope of absolute value $\varepsilon/\delta$; two
    vertices cannot lie on opposite sides of $x$ at distance $h$, since distinct vertices are
    $\delta=2h$ apart; an interval with no vertex in its interior stays in $I$ because a backward
    interval leaving $I$ contains the vertex $0$ and a forward one contains $1$; and hence some
    difference quotient at each $x$ has absolute value $2k\varepsilon>n$, giving
    $\Delta_h f>n$ at $h=1/(4k)\le1/n$. Added: the well-definedness of $f$ at the shared endpoints
    and the statement that a quotient over a linear piece equals its slope. Not claimed: a
    published solution of §49 Exercise 2 on printed p. 304, which the earlier event records as not
    located; the construction is the card's own. One presentation repair: the statement wrote
    `\epsilon`, which STYLE-04 spells `\varepsilon` and which is the glyph the book prints; the
    wording of the statement is unchanged.
---

::: {.exercise}

Given $n$ and $\varepsilon$, define a continuous function $f: I \to \RR$ such that $f \in U_n$ and $\abs{f(x)} \leq \varepsilon$ for all $x$.
:::

::: {.solution}
No complete published solution of this exercise was located, so the argument is the card's own; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. It is read with the book's set $U_n$ of printed p. 301: for $n\ge2$, $f\in U_n$ when $\Delta_h f>n$ for some $h$ with $0<h\le1/n$, where $\Delta f(x,h)$ is the larger in absolute value of the step-$h$ difference quotients of $f$ at $x$ that are defined, and $\Delta_h f=\inf_{x\in I}\Delta f(x,h)$.

::: pf

::: {.pf-step #parameters}
Given $n\ge2$ and $\varepsilon>0$ there is an integer $k\ge1$ with $2k\varepsilon>n$ and $4k\ge n$; then $\delta=1/(2k)$ and $h=\delta/2=1/(4k)$ satisfy $0<h\le1/n$.

::: pf-proof
Since $\varepsilon>0$, any integer $k>\max\{n/(2\varepsilon),\ n/4\}$ satisfies both inequalities. Then $h=1/(4k)\le1/n$ because $4k\ge n$, and $h>0$.
:::

:::

::: {.pf-step #construction}
With $t_j=j\delta$ for $j=0,\ldots,2k$, the function that is linear on each $[t_{j-1},t_j]$ and takes the value $\varepsilon$ at the odd $t_j$ and $0$ at the even $t_j$ is well defined and continuous, with $0\le f(x)\le\varepsilon$ for all $x\in I$.

::: pf-proof
The intervals $[t_{j-1},t_j]$ cover $I$ and their pairwise intersections are single points, and the two prescriptions agree at each shared endpoint, so the piecewise formula defines a function on $I$; it is continuous because it is continuous on each closed piece and the pieces agree at the endpoints. On each piece $f$ is linear between the values $0$ and $\varepsilon$, so every value lies between those two, and every slope has absolute value $\varepsilon/\delta$.
:::

:::

::: {.pf-step #quotient}
For every $x\in I$ one of the two intervals $[x-h,x]$, $[x,x+h]$ that meet $I$ contains no vertex $t_j$ in its interior, and then the corresponding difference quotient has absolute value $\varepsilon/\delta$.

:::: pf-proof

::: {.pf-step #no-two-vertices}
The intervals $(x-h,x)$ and $(x,x+h)$ are not both nonempty of vertices.

::: pf-proof
Suppose $t\in(x-h,x)$ and $t'\in(x,x+h)$ are vertices. Then $t<x<t'$, so $t'-t<(x+h)-(x-h)=2h=\delta$, while distinct vertices are at distance at least $\delta$ from one another, since $t_j=j\delta$. This is a contradiction.
:::

:::

::: {.pf-step #one-piece}
An interval $[x-h,x]$ or $[x,x+h]$ with no vertex in its interior lies in $I$ and in the closure of one linear piece.

::: pf-proof
The backward interval leaves $I$ only if $x-h<0$, and then the vertex $t_0=0$ lies in $(x-h,x)$; the forward one leaves $I$ only if $x+h>1$, and then the vertex $t_{2k}=1$ lies in $(x,x+h)$. So the interval stays in $I$. Its interior holds no vertex, hence lies in one of the open intervals between consecutive vertices, whose closure contains the interval, and $f$ is linear on that closure by step [](#construction){.pf-ref}.
:::

:::

::: {.pf-step}
Some difference quotient at $x$ has absolute value exactly $\varepsilon/\delta$, so $\Delta f(x,h)\ge\varepsilon/\delta$.

::: pf-proof
By step [](#no-two-vertices){.pf-ref} at least one of the two intervals has no vertex in its interior; by step [](#one-piece){.pf-ref} it lies in a single piece, over which $f$ is linear with a slope of absolute value $\varepsilon/\delta$. A difference quotient over an interval on which $f$ is linear equals the slope, so its absolute value is $\varepsilon/\delta$, and $\Delta f(x,h)$ is the larger of the two quotients, hence at least this value.
:::

:::

:::

:::

::: {.pf-step}
$\boxed{f\in U_n\text{ and }\abs{f(x)}\le\varepsilon\text{ for all }x\in I}$.

::: pf-proof
Step [](#quotient){.pf-ref} gives $\Delta f(x,h)\ge\varepsilon/\delta=2k\varepsilon$ for every $x\in I$, so $\Delta_h f\ge2k\varepsilon>n$ by step [](#parameters){.pf-ref}; since $0<h\le1/n$, the criterion for membership in $U_n$ at step $h$ is met and $f\in U_n$. Step [](#construction){.pf-ref} gives $0\le f(x)\le\varepsilon$ on $I$, which is the required bound on $\abs{f}$.
:::

:::

:::
:::
