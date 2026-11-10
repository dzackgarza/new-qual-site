---
schema: qual/card@1
id: E-I61EM
kind: problem
title: Sections of the minimal uncountable well-ordered set are second countable
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 42 Exercise 2, printed p. 262, with Theorem 42.1 (Smirnov), Theorem 28.2 (in a metrizable space limit point compactness implies compactness) and the countability of the ordinals below $\Omega$. No correction was needed; part (a) is the countability of the section and part (b) derives a contradiction by metrizing $S_\Omega$ and then compactifying it.
---

::: {.exercise}

(a) Show that for each $x \in S_\Omega$, the section of $S_\Omega$ by $x$ has a countable basis and hence is metrizable.

(b) Conclude that $S_\Omega$ is not paracompact.
:::

::: {.solution}
(a) Fix $x\in S_\Omega=[0,\Omega)$. Its section
$$
S_x=\{y:y<x\}
$$
is countable, since every element of $S_\Omega$ is a countable ordinal. The order topology on $S_x$ has a basis consisting of open intervals and end intervals with endpoints in $S_x$. Since $S_x$ is countable, this basis is countable. An ordered space is regular, so the Urysohn metrization theorem implies that $S_x$ is metrizable.

In particular, $S_\Omega$ is locally metrizable: for each $x<\Omega$, the open initial segment
$$
[0,x+1)=S_{x+1}
$$
is a metrizable neighborhood of $x$.

(b) Suppose $S_\Omega$ were paracompact. Since it is locally metrizable, the Smirnov metrization theorem would imply that $S_\Omega$ is metrizable. But $S_\Omega$ is countably compact and not compact, whereas every countably compact metrizable space is compact. This contradiction shows that $S_\Omega$ is not paracompact.
:::
