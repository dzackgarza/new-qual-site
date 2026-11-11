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
---

::: {.exercise}

What goes wrong with the "path-lifting lemma" (Lemma 54.1) for the local homeomorphism of Example 2 of §53?
:::

::: {.solution}
In Example 2 of §53,
$$
p:\RR_+\longrightarrow S^1,\qquad p(x)=(\cos2\pi x,\sin2\pi x),
$$
is a surjective local homeomorphism but not a covering map. The failure occurs over
$$
b_0=(1,0).
$$
Every sufficiently small neighborhood $U$ of $b_0$ has inverse image consisting of ordinary full sheets around the positive integers together with an initial interval $(0,\varepsilon)$. On the full sheets $p$ maps homeomorphically onto all of $U$, but the initial interval maps only onto one side of $b_0$; thus $U$ is not evenly covered.

This is exactly what breaks the proof of the path-lifting lemma. That proof first subdivides the path parameter so that each image segment lies in an evenly covered neighborhood and then chooses, inductively, the unique sheet containing the current lifted endpoint. Near $b_0$ there is no evenly covered neighborhood at all, because of the incomplete sheet at $0$. Consequently a path that tries to continue through $b_0$ in the missing direction can have a lift up to the moment it reaches the end $0$, but no continuation in $\RR_+$.

For instance, starting at $1$, the clockwise loop
$$
f(t)=(\cos2\pi t,-\sin2\pi t)
$$
would have to lift initially as $\widetilde f(t)=1-t$. At $t=1$ this reaches $0\notin\RR_+$, so no lift on the whole interval exists. Hence local homeomorphism alone is insufficient for the path-lifting lemma.
:::
