---
schema: qual/card@1
id: E-MPI86
kind: problem
title: Metrically equivalent metrics and completeness
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
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
  date: 2026-11-11
  note: >-
    Transcribed from two located published solutions, one per part. Part (a) from "Tze Heng", *Munkres'
    Topology: Self-study Notes and Exercises Attempts*, Chapter 7, "Exercises Attempts", the item numbered
    3(a) under "Exercise after §43" (URL
    https://blog.ttheng.com/docs/mathematics/munkres-topology-self-study/chapt-7/exercises/, read
    2026-11-11): the identity is uniformly continuous both ways because d-bar <= d, and conversely
    d-bar(x,y) < min{eps,1} forces d(x,y) = d-bar(x,y). Part (b) from "Solutions to exercises for
    Mathematics 205A" (University of California, Riverside, Fall 2014), Part 3, section "III.2: Complete
    metric spaces", answer to §43 Exercise 3 (printed p. 270)(b) on the set's own printed p. 4 (in
    tmp/sources/munkres-solutions-ucr-math205-gentop.pdf, PDF p. 45): uniform continuity carries Cauchy
    sequences both ways, completeness under d gives the limit, and continuity of the identity gives
    convergence under d-prime. Checked against Munkres, Topology (2000), §43 Exercise 3, printed p. 270,
    with the definition of metric equivalence, the standard bounded metric of §20, and the fact that a
    uniformly continuous map carries Cauchy sequences to Cauchy sequences. What was corrected: the blog's
    part (b) is a single paragraph that reuses "delta = eps" from part (a) and never records that the
    limit found under d must be the same point as the d-prime limit; the card's part (b) is the
    Riverside argument, with the identity's continuity supplying the last step. The card also has the
    printed statement's part (a), which the Riverside set does not answer.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The solution opened by claiming that no retained solution set covers the exercise, contradicting the
    audit note above it, which transcribes Tze Heng for part (a) and the Riverside Math 205A set for part (b).
    Both citations were re-read in the retained text versions: Tze Heng's "Exercise after §43" does contain
    the metrically-equivalent item as number 3, parts (a) and (b), at lines 51--61 of
    tmp/sources/munkres-solutions-ttheng-ch7.txt, and the statement matches Munkres's printed Section 43
    Exercise 3 verbatim. The sentence now names both sets and the page to the book. Not verified here: the
    page of the Riverside PDF, which the earlier session records as its printed p. 4; the retained file is a
    scan whose pagination was not re-measured in this session.

---

::: {.exercise}

Two metrics $d$ and $d'$ on a set $X$ are said to be metrically equivalent if the identity map $i: (X, d) \to (X, d')$ and its inverse are both uniformly continuous.

(a) Show that $d$ is metrically equivalent to the standard bounded metric $\bar{d}$ derived from $d$.

(b) Show that if $d$ and $d'$ are metrically equivalent, then $X$ is complete under $d$ if and only if it is complete under $d'$.
:::

::: {.solution}

The retained solutions cover one part each, as the audit records: part (a) is Tze Heng's item 3(a) under "Exercise after §43" (`tmp/sources/munkres-solutions-ttheng-ch7.txt`, lines 51--61), where the identity is uniformly continuous both ways because $\bar d\le d$ and conversely $d(x,y)= \bar d(x,y)$ once $\bar d(x,y)<1$; part (b) is the Riverside *Solutions to exercises for Mathematics 205A* answer to Section 43 Exercise 3(b) (`tmp/sources/munkres-solutions-ucr-math205-gentop.pdf`), transferred through uniform continuity of the identity and its inverse. The card's own contribution is what the audit records as corrected: the blog's part (b) reuses $\delta=\varepsilon$ from part (a) and never says that the limit found under $d$ is the same point as the $d'$-limit, so the card's part (b) closes the Riverside argument with continuity of the identity. The statement is Munkres's Section 43 Exercise 3, printed p. 270, the page the book's index gives for "metrically equivalent" (`tmp/sources/munkres-2000-topology.md`), and the bounded metric is that of Section 20.

Recall that $d$ and $d'$ are metrically equivalent when the identity $i:(X,d)\to(X,d')$ and its inverse are both uniformly continuous, and that $\bar d(x,y)=\min\theset{d(x,y),1}$.

::: pf

::: {.pf-step #bounded}
(a) The identity $(X,d)\to(X,\bar d)$ is uniformly continuous and so is its inverse.

::: pf-proof
Since $\bar d\le d$, given $\varepsilon>0$ the choice $\delta=\varepsilon$ gives $d(x,y)<\delta\Rightarrow\bar d(x,y)<\varepsilon$. Conversely, given $\varepsilon>0$ put $\delta=\tfrac12\min\theset{\varepsilon,1}$, so $\delta<1$; if $\bar d(x,y)<\delta$ then in particular $\bar d(x,y)<1$, which forces $\bar d(x,y)=d(x,y)$ because $\min\theset{d(x,y),1}<1$ only when $d(x,y)<1$; hence $d(x,y)<\delta\le\varepsilon$.
:::

:::

::: {.pf-step #cauchy}
(b) If $d$ and $d'$ are metrically equivalent, a sequence is $d$-Cauchy exactly when it is $d'$-Cauchy.

::: pf-proof
A uniformly continuous map sends Cauchy sequences to Cauchy sequences: given $\varepsilon>0$ choose $\delta>0$ from uniform continuity and then $N$ so that $d(x_{m},x_{n})<\delta$ for $m,n\ge N$. Applying this to the identity $(X,d)\to(X,d')$ gives that every $d$-Cauchy sequence is $d'$-Cauchy, and applying it to the inverse identity gives the converse.
:::

:::

::: {.pf-step #complete}
(b) $(X,d)$ is complete if and only if $(X,d')$ is.

::: pf-proof
Suppose $(X,d)$ is complete and let $(x_{n})$ be $d'$-Cauchy. It is $d$-Cauchy by step [](#cauchy){.pf-ref}, so $d(x_{n},x)\to0$ for some $x\in X$. The identity $(X,d)\to(X,d')$ is uniformly continuous, hence continuous, so $d'(x_{n},x)\to0$; thus $(x_{n})$ converges in $d'$ and $(X,d')$ is complete. The converse is the same argument with $d$ and $d'$ exchanged.
:::

:::

::: {.pf-qed}
Part (a) is step [](#bounded){.pf-ref}; part (b) follows from steps [](#cauchy){.pf-ref} and [](#complete){.pf-ref}.
:::

:::

:::
