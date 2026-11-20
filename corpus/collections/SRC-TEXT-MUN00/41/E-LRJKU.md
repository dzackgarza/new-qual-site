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

No retained solution set covers this exercise: the card's own example follows, with paracompactness of $\RR$ cited and the failure of local finiteness proved rather than asserted.

::: pf

::: {.pf-step #paracompact}
$\RR$ is paracompact.

::: pf-proof
$\RR$ is metrizable, and every metrizable space is paracompact (Theorem 41.4).
:::

:::

::: {.pf-step #cover}
$\mathcal{U}=\theset{(-n,n)\mid n\in\ZZ_{+}}$ is an open cover of $\RR$.

::: pf-proof
Each $(-n,n)$ is open in $\RR$, and a real $x$ lies in $(-n,n)$ for every integer $n>\abs{x}$.
:::

:::

::: {.pf-step #infinite}
Every subcollection of $\mathcal{U}$ that covers $\RR$ is infinite.

::: pf-proof
A finite subcollection has a largest index $N$, and its union is then the largest member $(-N,N)$, which is a proper subset of $\RR$; so a finite subcollection never covers $\RR$.
:::

:::

::: {.pf-step #not-locally-finite}
No infinite subcollection of $\mathcal{U}$ is locally finite.

::: pf-proof
Every member $(-n,n)$ of $\mathcal{U}$ contains $0$. So an infinite subcollection meets every neighbourhood of $0$ in infinitely many of its members, that is, it is not locally finite at the point $0$.
:::

:::

::: {.pf-qed}
By steps [](#cover){.pf-ref}, [](#infinite){.pf-ref} and [](#not-locally-finite){.pf-ref} the open cover $\mathcal{U}$ of the paracompact space $\RR$ has no locally finite subcollection that covers $\RR$ — indeed no infinite subcollection is locally finite at all. So paracompactness does not give locally finite subcoverings of a given open covering.
:::

:::

:::
