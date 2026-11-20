---
schema: qual/card@1
id: E-ORVG4
kind: problem
title: Where path lifting fails for local homeomorphisms
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 54: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-54-the-fundamental-group-of-the-circle/problem-1-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-54-the-fundamental-group-of-the-circle/problem-1-solution.txt), and against Munkres,
    Topology (2000), Section 54 Exercise 1, printed p. 347. dbFin's answer is the same: the failure is at $b_0=(1,0)$, whose neighbourhoods have an incomplete sheet over the interval $(0,\varepsilon)$, and the clockwise loop from $1$ must lift initially as $1-t$ and dies at $0\notin\RR_+$ when $t=1$. The card states both halves. Nothing needed repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the exponential map restricted to R_+ is a
    surjective local homeomorphism, that no neighbourhood of b0 = (1,0) is evenly covered
    because of the incomplete sheet (0, epsilon), that the subdivision step of Lemma 54.1
    therefore fails, and that the clockwise loop has no lift to R_+ from 1. The argument is
    the card's own; no retained set is cited. Munkres §54 Exercise 2, printed p. 341, with
    Example 2 of §53. The printed statement needed no repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two corrections on 2026-11-19. The rendered preamble said "The argument is
    the card's own; no retained solution set is cited on the card", which is
    false, since the event of 2026-11-11 cites dbFin's Section 54 Problem 1
    solution and compares it with the card; and it gave the exercise as "§54
    Exercise 2, printed p. 341", as the event of 2026-11-18 does. The exercise is
    Exercise 1 of §54, printed p. 347 (PDF p. 362 of the retained PDF, folio 347,
    printed page = PDF page - 15); printed p. 341 is the exercise page of §53. The
    preamble now cites dbFin's solution, with Lemma 54.1 on printed p. 342
    (PDF p. 357) and the definition of a covering map on printed p. 336. The event
    of 2026-11-18 is left as written and its "Exercise 2, printed p. 341" is
    superseded by this one. No step or statement changes: the two halves the card
    proves are the two halves of dbFin's answer, the incomplete sheet over the
    initial interval and the clockwise loop whose lift dies at 0.

---

::: {.exercise}

What goes wrong with the "path-lifting lemma" (Lemma 54.1) for the local homeomorphism of Example 2 of §53?
:::

::: {.solution}
The argument is that of the published solution of dbFin, "Section 54: Problem 1 Solution": the subdivision step of the path-lifting lemma fails at $b_0=(1,0)$, whose neighbourhoods have an incomplete sheet over an initial interval, and the clockwise loop from $1$ lifts initially as $1-t$ and dies at $0\notin\RR_+$. The exercise is Munkres, *Topology* (2000), Section 54, Exercise 1; Lemma 54.1, Example 2 of §53 is the map described below, and an evenly covered set and a covering map are defined in §53.

In Example 2 of §53 the map
$$
p:\RR_{+}\to S^{1},\qquad p(x)=(\cos 2\pi x,\ \sin 2\pi x),
$$
is a surjective local homeomorphism and not a covering map.

::: pf

::: {.pf-step #not-evenly-covered}
No neighbourhood of $b_{0}=(1,0)$ is evenly covered.

::: pf-proof
Let $U$ be a neighbourhood of $b_{0}$; shrink it to an arc $U$ of $S^{1}$ around $b_{0}$, of the form $\{(\cos 2\pi t,\sin 2\pi t)\mid -\varepsilon<t<\varepsilon\}$. Then $p^{-1}(U)$ is the union of the intervals $(n-\varepsilon,n+\varepsilon)$ for integers $n\ge1$, together with the initial interval $(0,\varepsilon)$. On each $(n-\varepsilon,n+\varepsilon)$ with $n\ge1$ the map $p$ is a homeomorphism onto $U$; on $(0,\varepsilon)$ it is a homeomorphism onto the half $\{(\cos2\pi t,\sin2\pi t)\mid 0<t<\varepsilon\}$, which is a proper subset of $U$. So $p^{-1}(U)$ is not a disjoint union of open sets each mapped homeomorphically onto $U$, and $U$ is not evenly covered. Since every neighbourhood of $b_{0}$ contains such an arc, no neighbourhood of $b_{0}$ is evenly covered.
:::

:::

::: {.pf-step #no-even-neighbourhood}
There is no evenly covered neighbourhood of $b_{0}$ at all, so the first step of the proof of Lemma 54.1 fails at $b_{0}$.

::: pf-proof
Step [](#not-evenly-covered){.pf-ref}. The proof of the path lifting lemma begins by subdividing the parameter interval of a path so that each subpath lies in an evenly covered open set of $B$; a subdivision of a path passing through $b_{0}$ would need an evenly covered neighbourhood containing $b_{0}$, and none exists.
:::

:::

::: {.pf-step #explicit-failure}
The loop $f(t)=(\cos2\pi t,-\sin2\pi t)$ on $[0,1]$, based at $1=(\cos0,\sin0)$, has no lift to $\RR_{+}$ beginning at $1$.

::: pf-proof
A lift $\widetilde f$ of $f$ with $\widetilde f(0)=1$ would satisfy $p\circ\widetilde f=f$. On a small interval $[0,\delta)$ the point $f(t)$ is near $b_{0}$ on the lower side, and the only lift near $1$ is $\widetilde f(t)=1-t$, by the uniqueness of lifts on a connected parameter interval (Lemma 54.1's uniqueness clause, which holds because $p$ is a local homeomorphism). Continuing, one gets $\widetilde f(t)=1-t$ as long as the lift exists. If a lift existed on all of $[0,1]$ it would be continuous and defined at $t=1$, where it would have to be the point mapping to $f(1)=b_{0}$ closest to $1$ from below along the line, namely $0$; but $0\notin\RR_{+}$. So no lift on $[0,1]$ exists.
:::

:::

::: {.pf-step}
A local homeomorphism alone does not suffice for the path-lifting lemma.

::: pf-proof
$p$ is a surjective local homeomorphism, and steps [](#no-even-neighbourhood){.pf-ref} and [](#explicit-failure){.pf-ref} show that the lemma's conclusion fails for it; the hypothesis of Lemma 54.1, that $p$ be a covering map, is what excludes this example.
:::

:::

:::
:::
