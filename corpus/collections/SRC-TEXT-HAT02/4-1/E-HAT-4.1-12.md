---
schema: qual/card@1
id: E-HAT-4.1-12
kind: problem
title: "$n$-connected $n$-dimensional CW complexes are contractible"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17871 for the statement, 17254-17256 for n-connected, 18258-18262
    for the Hurewicz theorem). The argument is correct except at one hypothesis: it said without
    qualification that the Hurewicz map pi_m -> H_m is an isomorphism, and Hatcher's absolute form
    (Theorem 4.32) requires (m-1)-connected with m >= 2. At m = 1 it gives only the abelianised pi_1,
    so a nonzero perfect pi_1 would not be contradicted. The card now disposes of n = 0 first (a
    path-connected 0-dimensional CW complex is a point), which makes m >= n+1 >= 2 and restores the
    hypothesis. The remaining steps were checked and are unchanged: minimality of m makes X
    (m-1)-connected, X has no cells above dimension n so the cellular chain complex vanishes there so
    H_m = 0, and Whitehead applies since X and a point are CW complexes. Not checked: Hatcher's proof
    of Theorem 4.32 was not re-read, only its statement and hypothesis.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 12 of §4.1, which is on printed p. 359 and not p. 358 — the
    section's Exercises 1--11 are on p. 358 and 12--22 on p. 359, checked at PDF page 368 of
    `tmp/sources/hatcher-2002-algebraic-topology.pdf`, whose folio is 359 — and against the published
    solution of the exercise, Andrew Proudfoot, *Math 634: Algebraic Topology I*, Partial Solutions to
    Homework #6, Problem 12, printed p. 1 of `tmp/sources/uoregon-proudfoot-634-hw6.pdf`. The card's
    own Hurewicz argument was checked in the event of 2026-11-02 and is unchanged. Proudfoot's route is
    now transcribed on the card with two corrections that the transcribed text needs. (1) His citation
    "Corollary 4.16" is the statement printed as **Proposition 4.15 on printed p. 353** of the book
    held here — for an $n$-connected CW pair $(X,A)$ there is $(Z,A)\simeq(X,A)$ rel $A$ with all cells
    of $Z-A$ of dimension greater than $n$ — which with $A$ a $0$-cell gives his $Z$; the errata's
    renumbering table moves the earlier 4.16 to 4.15, and the book calls it a proposition. (2) His
    sentence "the image of $f$ lies in the $n$-skeleton of $Z$, which is a single point" requires $X$
    to be $n$-dimensional, which is the exercise's hypothesis and is missing from his restatement of
    it: a cellular map sends $X_n$ to $Z_n$, and $X=X_n$ only then. With both supplied the argument
    closes. Checked also: cellular approximation (Theorem 4.8) is available for maps of CW complexes,
    and a nullhomotopic homotopy equivalence has contractible source and target. Not claimed: that
    the printed set states the dimension hypothesis.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.1 Exercise 12. The card's proof is correct: at $n=0$ a $0$-dimensional
    CW complex is discrete and $0$-connected, so a point; for $n\ge1$, if $m>n$ is the least degree
    with $\pi_m(X)\ne0$ then $X$ is $(m-1)$-connected with $m\ge2$, so Hurewicz (Theorem 4.32) makes
    $\pi_m(X)\to H_m(X;\ZZ)$ an isomorphism, while $C_m(X)=0$ above dimension $n$; the contradiction
    gives $\pi_i(X)=0$ in every degree and Whitehead's theorem makes $X\to\ast$ a homotopy
    equivalence. The proof is independent of the published one and is kept; Proudfoot's Problem 12 of
    Homework #6 does cover the exercise and is quoted, with its two qualifications. Three corrections
    to the live text. (1) The citation of Proudfoot carried a printed page and a `.pdf` path; it now
    names the Markdown file `tmp/sources/uoregon-proudfoot-634-hw6.md`, with no page. (2) So did the
    citation of Proposition 4.15. (3) The sentence that the errata's renumbering table moves an
    earlier Corollary 4.16 to 4.15 is not supported by the retained errata, which lists no such
    entry; the held printing has no Corollary 4.16, and the statement Proudfoot uses is Proposition
    4.15, which is what the card now says.
---

::: {.problem}
Show that an $n$-connected, $n$-dimensional CW complex is contractible.
:::

::: {.solution}

The proof below is the card's own — Hurewicz in the least degree above $n$ where a homotopy group survives, against the vanishing of cellular homology above the dimension, then Whitehead — and it is kept because it is correct. A retained published solution covers the exercise and is quoted in the second part: **Andrew Proudfoot, *Math 634: Algebraic Topology I*, Partial Solutions to Homework #6, Problem 12** (`tmp/sources/uoregon-proudfoot-634-hw6.md`), Problem 12 there being Hatcher's §4.1 Exercise 12; the two qualifications that argument needs are recorded with it.

Let $X$ be an $n$-connected, $n$-dimensional CW complex, so that $\pi_{i}(X)=0$ for $0\le i\le n$.

::: pf

::: {.pf-step #zero}
If $n=0$ then $X$ is a point, hence contractible.

::: pf-proof
A $0$-dimensional CW complex is a discrete space, and $0$-connected means path connected, so $X$ is a single point; a point is contractible. This case is separated because the Hurewicz theorem below needs $m\ge2$, and at $m=1$ it would only identify the abelianised $\pi_{1}$.
:::

:::

::: {.pf-step #hurewicz}
If $n\ge1$ and some homotopy group $\pi_{m}(X)$ with $m>n$ is nonzero, then $H_{m}(X;\ZZ)\ne0$ for the least such $m$.

::: pf-proof
Let $m>n$ be the least integer with $\pi_{m}(X)\ne0$, which exists by hypothesis. Then $\pi_{i}(X)=0$ for all $i<m$, that is $X$ is $(m-1)$-connected, and $m\ge n+1\ge2$. The absolute Hurewicz theorem (Hatcher, Theorem 4.32) then says the Hurewicz map $\pi_{m}(X)\to H_{m}(X;\ZZ)$ is an isomorphism, so $H_{m}(X;\ZZ)\cong\pi_{m}(X)\ne0$.
:::

:::

::: {.pf-step #homology}
$H_{m}(X;\ZZ)=0$ for every $m>n$.

::: pf-proof
The cellular chain group $C_{m}(X)$ is free on the $m$-cells, of which there are none when $m>n$, so the cellular chain complex vanishes in degrees above $n$ and its homology does too; cellular homology agrees with singular homology.
:::

:::

::: {.pf-step #contractible}
$X$ is contractible.

::: pf-proof
Steps [](#hurewicz){.pf-ref} and [](#homology){.pf-ref} contradict each other unless no such $m$ exists, so $\pi_{i}(X)=0$ for every $i\ge0$; with step [](#zero){.pf-ref} this covers $n=0$ as well. Hence the map $X\to\ast$ induces isomorphisms on all homotopy groups, and both $X$ and the point are CW complexes, so Whitehead's theorem gives that $X\to\ast$ is a homotopy equivalence. Therefore
$$
\boxed{X\text{ is contractible}.}
$$
*The published route.* Andrew Proudfoot, *Math 634: Algebraic Topology I*, Partial Solutions to Homework #6, Problem 12 (`tmp/sources/uoregon-proudfoot-634-hw6.md`), argues from the cell structure instead of from Hurewicz:

> Let $X$ be an $n$-connected CW complex. Applying Corollary 4.16 when $A$ is a single $0$-cell, we see that there exists a CW complex $Z$ which is homotopy equivalent to $X$ and has the property that $Z$ has one $0$-cell and no $k$-cells for $1\leq k\leq n$. Let $f:X\to Z$ be a homotopy equivalence. By cellular approximation, we may assume that the image of $f$ lies in the $n$-skeleton of $Z$, which is a single point! Hence $f$ is a nullhomotopic homotopy equivalence, which implies that $X$ and $Z$ are contractible.

Two points of the printed argument need attention before it is used. (1) The statement it cites is **Proposition 4.15** of the book held here: if $(X,A)$ is an $n$-connected CW pair then there is a CW pair $(Z,A)\simeq(X,A)$ rel $A$ with all cells of $Z-A$ of dimension greater than $n$. With $A=\{x_0\}$ this is Proudfoot's $Z$; his "Corollary 4.16" is not a statement of the held printing, which has no corollary at that number, and the statement he uses is Proposition 4.15. (2) The step "the image of $f$ lies in the $n$-skeleton of $Z$, which is a single point" uses that $X$ is $n$-dimensional, which the exercise's hypothesis supplies and Proudfoot's sentence does not: a cellular map carries $X_n$ into $Z_n$, and $X=X_n$ only under that hypothesis. With it restored the argument is complete — $f$ is homotopic to a cellular map with image the single $0$-cell, hence nullhomotopic, and a nullhomotopic homotopy equivalence has contractible source and target.

:::

:::

:::
:::
