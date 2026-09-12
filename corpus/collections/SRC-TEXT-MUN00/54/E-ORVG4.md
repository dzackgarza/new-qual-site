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
---

::: {.exercise}

What goes wrong with the "path-lifting lemma" (Lemma 54.1) for the local homeomorphism of Example 2 of §53?
:::

::: {.solution}
In Example 2 of §53,
\[
p:\mathbb R_+\longrightarrow S^1,\qquad p(x)=(\cos2\pi x,\sin2\pi x),
\]
is a surjective local homeomorphism but not a covering map. The failure occurs over
\[
b_0=(1,0).
\]
Every sufficiently small neighborhood \(U\) of \(b_0\) has inverse image consisting of ordinary full sheets around the positive integers together with an initial interval \((0,\varepsilon)\). On the full sheets \(p\) maps homeomorphically onto all of \(U\), but the initial interval maps only onto one side of \(b_0\); thus \(U\) is not evenly covered.

This is exactly what breaks the proof of the path-lifting lemma. That proof first subdivides the path parameter so that each image segment lies in an evenly covered neighborhood and then chooses, inductively, the unique sheet containing the current lifted endpoint. Near \(b_0\) there is no evenly covered neighborhood at all, because of the incomplete sheet at \(0\). Consequently a path that tries to continue through \(b_0\) in the missing direction can have a lift up to the moment it reaches the end \(0\), but no continuation in \(\mathbb R_+\).

For instance, starting at \(1\), the clockwise loop
\[
f(t)=(\cos2\pi t,-\sin2\pi t)
\]
would have to lift initially as \(\widetilde f(t)=1-t\). At \(t=1\) this reaches \(0\notin\mathbb R_+\), so no lift on the whole interval exists. Hence local homeomorphism alone is insufficient for the path-lifting lemma.
:::
