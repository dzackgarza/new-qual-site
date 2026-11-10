---
schema: qual/card@1
id: E-LZX97
kind: problem
title: Local metrizability criteria as cases of the Smirnov metrization theorem
classification:
  areas:
  - topology
  topics:
  - Metrizability
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
    Checked against Munkres, Topology (2000), Section 42 Exercise 1, printed p. 262, with Theorem 42.1, Theorem 41.4 and Theorem 41.5 (which supply the paracompactness that Exercises 34.7 and 34.8 do not state), and the two exercises themselves. What was corrected: the card now names Theorem 41.5 for the paracompactness of a regular Lindelof space, where it previously referred only to the construction on the card of E-KVFCT.
---

::: {.exercise}

Compare Theorem 42.1 (the Smirnov metrization theorem) with Exercises 7 and 8 of §34.
:::

::: {.solution}
The Smirnov metrization theorem says
$$
X\text{ metrizable}
\quad\Longleftrightarrow\quad
X\text{ paracompact Hausdorff and locally metrizable}.
$$
Both criteria of §34 follow from it, because each hypothesis implies paracompactness.

In [[E-MQTBP]], $X$ is compact Hausdorff and locally metrizable. Every compact space is paracompact (§41, the remark following the definition), so the Smirnov theorem gives metrizability.

In [[E-KK77N]], $X$ is regular, Lindelöf, and locally metrizable. Every regular Lindelöf space is paracompact (Theorem 41.5; the construction on the card of [[E-KVFCT]](a) gives a locally finite open refinement of every open cover), so the Smirnov theorem gives metrizability.

Conversely, compactness with the Hausdorff property and regularity with the Lindelöf property are two sufficient conditions for the paracompactness hypothesis of the Smirnov theorem.
:::
