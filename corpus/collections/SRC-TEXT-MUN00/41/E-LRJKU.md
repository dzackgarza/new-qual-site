---
schema: qual/card@1
id: E-LRJKU
kind: problem
title: Paracompact coverings need not have locally finite subcoverings
classification:
  areas:
  - topology
  topics:
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
    Checked against Munkres, Topology (2000), Section 41 Exercise 1, printed p. 260, with Theorem 41.4 (every metrizable space is paracompact) and the definition of local finiteness. No correction was needed; the cover is the family of intervals $(-n,n)$ of $\RR$, every member of which contains $0$.
---

::: {.exercise}

Give an example to show that if $X$ is paracompact, it does not follow that for every open covering $\mathcal{A}$ of $X$, there is a locally finite subcollection of $\mathcal{A}$ that covers $X$.
:::

::: {.solution}
Take $X=\RR$, which is metrizable and hence paracompact, and consider the open cover
$$
\mathcal U=\{(-n,n):n\in\ZZ_+\}.
$$
Any subcollection that covers $\RR$ must contain intervals with arbitrarily large $n$, so it must be infinite. But every member of $\mathcal U$ contains $0$. Hence any infinite subcollection fails even to be point-finite at $0$, and therefore cannot be locally finite. Thus this open cover has no locally finite subcover, although $X$ is paracompact.
:::
