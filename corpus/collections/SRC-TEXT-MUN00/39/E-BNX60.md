---
schema: qual/card@1
id: E-BNX60
kind: problem
title: Locally finite interval collections in $\RR$ and in $(0,1)$
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
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
    Checked against Munkres, Topology (2000), Section 39 Exercise 1, printed p. 247, with Example 1 of §39, the definition of local finiteness, and the archimedean property of $\RR$ for the two collections that fail in $\RR$. No correction was needed; the card proves each of the three assertions of Example 1, including that $\mathcal B$ and $\mathcal C$ are locally finite in $(0,1)$ and not in $\RR$.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the three local finiteness statements of
    Example 1 of §39, printed p. 244, counting the finitely many indices meeting an explicit
    neighbourhood at each point, and the failure at 0 in R for the two shrink-to-zero
    collections. The argument is the card's own; no retained set is cited. The printed
    statements needed no repair.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against §39 Exercise 1 and found correct; the page in the head is gone, and the
    negative search for a published set is recorded once for §39--§42 in `COMPLAINTS.md`. The
    book's first collection, $\{(n,n+2)\}$, is locally finite in $\RR$; the two interval
    collections that follow, $\{(0,1/n)\}$ and $\{(1/(n+1),1/n)\}$, are locally finite in
    $(0,1)$, a neighbourhood $(a,1)\cap(0,1)$ of a point meeting only those members with
    $1/n\ge a$, and neither is locally finite in $\RR$, where every neighbourhood of $0$ meets
    every member.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 second read, on the verification member's report of this card. Two repairs in the
    proof that $\mathcal C$ is locally finite in $(0,1)$. The inequality excluding the members
    with $m\ge n+2$ was strict at $m=n+2$, where $1/m=1/(n+2)=a$: the correct conclusion is
    $1/m\le a$, and each such member lies in $(0,a]$ and misses $V=(a,1)\cap(0,1)$, so the count
    of the remaining members stands. And the existence of $n$ with
    $1/(n+1)\le x\le1/n$ was asserted; it is now taken as the least $n$ with $1/(n+1)<x$, whose
    existence is the archimedean property, minimality giving $1/n\ge x$. No other step changed.

---

::: {.exercise}

Check the statements in Example 1 of §39: the collection

$$
\mathcal{A} = \theset{(n, n+2) \mid n \in \ZZ}
$$

is locally finite in $\RR$, while the collections

$$
\mathcal{B} = \theset{(0, 1/n) \mid n \in \ZZ_+} \quad \text{and} \quad \mathcal{C} = \theset{(1/(n+1), 1/n) \mid n \in \ZZ_+}
$$

are locally finite in $(0, 1)$ but not in $\RR$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It checks the statements of Example 1 of §39.

::: pf

::: {.pf-step #A}
$\mathcal{A}=\{(n,n+2)\mid n\in\ZZ\}$ is locally finite in $\RR$.

::: pf-proof
Let $x\in\RR$ and put $V=(x-\tfrac12,x+\tfrac12)$, a neighbourhood of $x$. If $V$ meets $(n,n+2)$, then $n<x+\tfrac12$ and $n+2>x-\tfrac12$, that is $x-\tfrac52<n<x+\tfrac12$. Only finitely many integers satisfy those two inequalities, so $V$ meets only finitely many members of $\mathcal{A}$.
:::

:::

::: {.pf-step #B}
$\mathcal{B}=\{(0,1/n)\mid n\in\ZZ_{+}\}$ is locally finite in $(0,1)$ and not in $\RR$.

::: pf-proof
Let $x\in(0,1)$ and choose $a$ with $0<a<x$; then $V=(a,1)\cap(0,1)$ is a neighbourhood of $x$ in $(0,1)$. If $n>1/a$ then $1/n<a$, so $(0,1/n)\subset(0,a)$ and it misses $V$; hence only the finitely many members of $\mathcal{B}$ with $n\le1/a$ can meet $V$. In $\RR$, however, every neighbourhood of $0$ contains an interval $(-\delta,\delta)$ with $\delta>0$, and for every $n$ with $1/n<\delta$ the set $(0,1/n)$ meets $(-\delta,\delta)$; those are infinitely many members, so $\mathcal{B}$ is not locally finite in $\RR$.
:::

:::

::: {.pf-step #C}
$\mathcal{C}=\{(1/(n+1),1/n)\mid n\in\ZZ_{+}\}$ is locally finite in $(0,1)$ and not in $\RR$.

::: pf-proof
Let $x\in(0,1)$. Choose the least $n\ge1$ with $1/(n+1)<x$, which exists because $1/(n+1)\to0$; then $1/n\ge x$ by minimality, so $1/(n+1)\le x\le1/n$. Put $a=1/(n+2)$, so that $0<a<1/(n+1)$. The set $V=(a,1)\cap(0,1)$ is a neighbourhood of $x$ in $(0,1)$. A member $(1/(m+1),1/m)$ with $m\ge n+2$ has $1/m\le1/(n+2)=a$, hence lies in $(0,a]$ and misses $V$; only the finitely many members with $m<n+2$ remain. So $\mathcal{C}$ is locally finite in $(0,1)$. In $\RR$ every neighbourhood of $0$ contains some $(-\delta,\delta)$ with $\delta>0$, and for every $m$ with $1/m<\delta$ the interval $(1/(m+1),1/m)$ meets $(-\delta,\delta)$; infinitely many $m$ satisfy this, so $\mathcal{C}$ is not locally finite in $\RR$.
:::

:::

::: {.pf-step}
The three statements of Example 1 hold.

::: pf-proof
Steps [](#A){.pf-ref}, [](#B){.pf-ref} and [](#C){.pf-ref} are those statements.
:::

:::

:::
:::
