---
schema: qual/card@1
id: E-ID1F7
kind: problem
title: The theorem of meteorology
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
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
    Checked line by line against Munkres, Topology (2000), Section 57 Exercise 1, printed p. 359,
    with Theorem 57.3, the Borsuk-Ulam theorem for $S^2$. The card applies the theorem to $F=(T,P):S^2\to\RR^2$ and reads the equality of both coordinates as equality of temperature and of pressure at the antipodal pair. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Harvard Math 131 (2000-01), Solution Set 10, item
    9.57.1, on the first page of the set, held at tmp/sources/harvard131-soln10.md, read in the
    MinerU extraction. The set's pages carry no folio, so the citation is by set and item; the
    set's three scanned pages are the extraction's first page range. The solution is that answer
    transcribed: model the earth by $S^2$, let $t$ and $b$ be temperature and pressure, note
    $p\mapsto(t(p),b(p))$ is continuous into $\RR^2$, and apply Borsuk-Ulam. The answer is correct
    and needed no repair; what it leaves implicit, and the card states, is that both quantities
    vary continuously, which is the hypothesis the argument uses. Checked against the book: the
    exercise text on printed p. 359, Theorem 57.3 (Borsuk-Ulam for $S^2$) on printed p. 358, the
    definition of the antipode opening §57 on printed p. 356, and Theorem 18.4 (maps into
    products) on printed p. 110, which is the continuity step. Not claimed: that the set states
    the continuity hypothesis -- it takes it as given.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source named
    in its own text. The earlier proof was the same argument in one paragraph and was removed
    because the card is to carry the published one.
---

::: {.exercise}

Prove the following "theorem of meteorology": at any given moment in time, there exists a pair of antipodal points on the surface of the earth at which both the temperature and the barometric pressure are equal.
:::

::: {.solution}
The exercise is §57 Exercise 1. The proof is transcribed from
Harvard Math 131 (2000--01), Solution Set 10, item 9.57.1, the first page of the
set, held at `tmp/sources/harvard131-soln10.md`: model the earth by $S^2$, take
the temperature $t(p)$ and the barometric pressure $b(p)$ at a point $p$, note
that $p\mapsto(t(p),b(p))$ is a continuous map of $S^2$ into $\RR^2$, and apply
the Borsuk--Ulam theorem (Theorem 57.3). The one hypothesis the
argument uses and the exercise leaves to the reader is that both quantities vary
continuously over the surface at the fixed moment; the solution states it.

::: pf

::: {.pf-step #continuous}
$F=(t,b):S^2\to\RR^2$ is continuous.

::: pf-proof
By hypothesis $t$ and $b$ are continuous real-valued functions on $S^2$, so
$F$ is continuous because a map into a product is continuous exactly when its
coordinate functions are (Theorem 18.4).
:::

:::

::: {.pf-step #antipodal}
There is $x\in S^2$ with $F(x)=F(-x)$.

::: pf-proof
$F$ is a continuous map of $S^2$ into $\RR^2$, so the Borsuk--Ulam theorem for
$S^2$ (Theorem 57.3) supplies such an $x$; the point $-x$ is
the antipode of $x$ in the sense of the definition opening §57.
:::

:::

::: {.pf-step}
$\boxed{t(x)=t(-x)\ \text{and}\ b(x)=b(-x)}$ for the antipodal pair
$\theset{x,-x}$, both coordinates of $F(x)=F(-x)$ being equal.

::: pf-proof
Two elements of $\RR^2$ are equal exactly when their coordinates are, so
$F(x)=F(-x)$ from step [](#antipodal){.pf-ref} gives $t(x)=t(-x)$ and
$b(x)=b(-x)$: at the antipodal points $x$ and $-x$ the temperature and the
barometric pressure agree simultaneously, which is the theorem of meteorology.
:::

:::

:::
:::
