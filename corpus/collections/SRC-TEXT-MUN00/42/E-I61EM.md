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
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (b) concluded non-paracompactness from the assertion that a countably compact metrizable space is
    compact, which is not one of the book's numbered results; the card now uses limit point compactness,
    which is: an infinite subset of $S_\Omega$ contains an increasing sequence whose supremum is a countable
    ordinal below $\Omega$ and is a limit point of the subset. With Theorem 28.2 (a metrizable limit point
    compact space is compact) and the cover $\{[0,\alpha)\mid\alpha<\Omega\}$, which has no finite subcover,
    the contradiction is the one the exercise asks for. Checked against Theorem 42.1 (Smirnov), Theorem 28.2
    and the countability of the ordinals below $\Omega$.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (a) said that an ordered space is regular without a reference; the section $S_x$ is a well-ordered
    set in the order topology, hence normal by Theorem 32.4 and regular, which is the hypothesis the Urysohn
    metrization theorem (Theorem 34.1) needs, its countable basis being the countability of $S_x$.
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
is countable, since every element of $S_\Omega$ is a countable ordinal. The order topology on $S_x$ has a basis consisting of open intervals and end intervals with endpoints in $S_x$. Since $S_x$ is countable, this basis is countable. The order topology on the well-ordered set $S_x$ makes it normal (Theorem 32.4), hence regular, so the Urysohn metrization theorem (Theorem 34.1) implies that $S_x$ is metrizable.

In particular, $S_\Omega$ is locally metrizable: for each $x<\Omega$, the open initial segment
$$
[0,x+1)=S_{x+1}
$$
is a metrizable neighborhood of $x$.

(b) Suppose $S_\Omega$ were paracompact. Since it is locally metrizable, the Smirnov metrization theorem would imply that $S_\Omega$ is metrizable. But $S_\Omega$ is limit point compact: an infinite subset of it contains an increasing sequence $\alpha_1<\alpha_2<\cdots$, whose supremum is a countable ordinal $\alpha<\Omega$ and a limit point of the subset. By Theorem 28.2 a metrizable space that is limit point compact is compact, and $S_\Omega$ is not compact, the cover $\{[0,\alpha)\mid\alpha<\Omega\}$ having no finite subcover. This contradiction shows that $S_\Omega$ is not paracompact.
:::
