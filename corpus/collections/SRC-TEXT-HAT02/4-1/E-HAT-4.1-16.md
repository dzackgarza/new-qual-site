---
schema: qual/card@1
id: E-HAT-4.1-16
kind: problem
title: "Factoring maps through $n$-connective covers"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 16 and the cell-attachment construction preceding Proposition 4.13; the stored statement matches.
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
    Read against the book (AT.txt:17887-17889 for the statement, 17590-17602 and 17605-17609 for the
    cell-attachment constructions it follows). The construction is correct: cells of dimension at least
    n+1 preserve pi_i for i <= n, and at each k the map is made surjective by wedging k-spheres and then
    injective by attaching (k+1)-cells along representatives of the kernel. One step was asserted and is
    now given: passing from an isomorphism at the stage k = i to an isomorphism on the union Z_n needs
    pi_i(Z_n) = colim_k pi_i(Z_k), which holds because a map S^i -> Z_n has compact image, hence lies in
    a finite subcomplex and so in a single stage (Hatcher, Proposition A.1, AT.txt:25888-25889). The
    pi_0 hypothesis is met because X, Y and Z_n are connected. Not checked: no verification of the
    book's own construction beyond the two cited spans.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 16 of §4.1, printed p. 359, and against the construction the
    card follows, printed p. 353 — the two steps preceding Proposition 4.13, which is itself on that
    page; the section's Exercises 1--11 are on p. 358 and 12--22 on p. 359, checked at PDF pages 367
    and 368 of the held book. Checked: attaching cells of dimension at least $n+1$ leaves $\pi_i$
    unchanged for $i\le n$; at stage $k$ a wedge of $k$-spheres makes $\pi_k$ surjective onto
    $\pi_k(Y)$ without changing lower groups, and $(k+1)$-cells attached along representatives of the
    kernel, extended over the chosen nullhomotopies, make it injective; the first stage has constant
    attaching maps, so $Z_{n+1}$ keeps $\pi_i$ for $i\le n$; and the passage to the union uses
    compactness — a map $S^i\to Z_n$ has image in a finite subcomplex, hence in a single stage, so
    $\pi_i(Z_n)=\varinjlim\pi_i(Z_k)$ (Hatcher, Proposition A.1). No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.1 Exercise 16. The construction is correct, but its opening was muddled:
    it began by attaching $(n+1)$-cells with constant attaching maps although the construction does
    not need them, and it left the induction's starting point implicit. The solution is rewritten as
    the same construction with the induction stated from $Z_0=X$ and $f_0=f$: at stage $k\ge n+1$ a
    $k$-cell attached along the constant map for each element of $\pi_k(Y)$ outside the image makes
    $\pi_k$ surjective, then a $(k+1)$-cell along a based map for each element of the kernel makes it
    injective, neither disturbing $\pi_i$ for $i\le k-1$; the isomorphisms $\pi_i(X)\cong\pi_i(Z_n)$
    for $i\le n$ come from $\pi_i(Z_k,Z_{k-1})=0$ below $k$, and those for $i\ge n+1$ from the
    isomorphism at stage $i$ together with the vanishing of the later cells and Proposition A.1. The
    provenance is added: no retained set holds a proof — Sam's §4.1 has no entry for the exercise and
    Proudfoot's Homework #6 covers Exercises 4, 11, 12, 14 and 15 — so the construction is the
    card's. The card remains prose and is still listed by the prose-only queue.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Two corrections to the rewritten proof, both raised by an independent reading. (1) The sentence
    "cells of dimension $k$ do not change $\pi_i$ for $i\le k-1$" is false for an arbitrary attaching
    map — a 2-cell attached to $S^1$ by a degree-2 map changes $\pi_1$ — and it is now restricted to
    the cells actually used, those attached along the constant map, which add no class in degree $k$
    either. (2) "every later cell has dimension at least $i+2$" is false: stage $i+1$ attaches
    $(i+1)$-cells as well as $(i+2)$-cells. The step now says that the cells added after stage $i$
    have dimension at least $i+1$ and that those of dimension $i+1$ are attached along constant maps,
    so no class in $\pi_i$ is killed.
---

::: {.problem}
Show that a map $f: X \to Y$ between connected CW complexes factors as a composition $X \to Z_n \to Y$ where the first map induces isomorphisms on $\pi_i$ for $i \leq n$ and the second map induces isomorphisms on $\pi_i$ for $i \geq n+1$.
:::

::: {.solution}
The exercise is §4.1 Exercise 16. No retained solution set holds a proof of it: Sam's §4.1 has no entry for the exercise, and Proudfoot's Homework #6 covers Exercises 4, 11, 12, 14 and 15. The construction below is the card's, and is the cell-attachment argument the book uses for its $n$-connected models, run in the direction that builds the factorisation.

Put $Z_0=X$ and $f_0=f\colon Z_0\to Y$. Inductively, suppose $Z_k\supset Z_{k-1}$ with an extension $f_k\colon Z_k\to Y$ of $f_{k-1}$ inducing an isomorphism on $\pi_i$ for $n+1\le i<k$. At stage $k\ge n+1$, first make $f_k$ surjective on $\pi_k$: for each element of $\pi_k(Y)$ not in the image of $\pi_k(Z_k)$, attach a $k$-cell to $Z_k$ along the constant map and extend $f_k$ over it by a based map representing that element. A $k$-cell attached along the constant map changes no $\pi_i$ with $i\le k-1$ and adds no class to $\pi_k$, so nothing already established is disturbed and the map on $\pi_k$ becomes surjective. Then make it injective: for each element of the kernel of $\pi_k(Z_k)\to\pi_k(Y)$, attach a $(k+1)$-cell along a based map representing it, and extend $f$ over the cell by a nullhomotopy of the composite, which exists because the class lies in the kernel. Cells of dimension $k+1$ do not change $\pi_i$ for $i\le k-1$, and the classes so killed generate the kernel, so the map on $\pi_k$ becomes injective. Hence $f_k$ induces an isomorphism on $\pi_k$ and still does on $\pi_i$ for $n+1\le i<k$, which advances the induction.

Let $Z_n=\bigcup_kZ_k$ with the induced CW structure and $g\colon Z_n\to Y$ the common extension of the $f_k$. For each $k$ the pair $(Z_k,Z_{k-1})$ is built by attaching cells of dimension at least $k$, so $\pi_i(Z_k,Z_{k-1})=0$ for $i\le k-1$, and the long exact sequence of the pair gives $\pi_i(X)\cong\pi_i(Z_n)$ for $i\le n$. For $i\ge n+1$ the map $f_i\colon Z_i\to Y$ is an isomorphism on $\pi_i$ by the construction, and the inclusion $Z_i\to Z_n$ induces an isomorphism on $\pi_i$ because the cells added after stage $i$ have dimension at least $i+1$, and those of dimension $i+1$ are attached along constant maps and so kill no class in $\pi_i$; passing to the union uses compactness, a map $S^i\to Z_n$ having compact image and so lying in a finite subcomplex, hence in some single stage $Z_k$ (Proposition A.1), which identifies $\pi_i(Z_n)$ with the direct limit of the $\pi_i(Z_k)$. The map $g$ therefore induces an isomorphism on $\pi_i$ for $i\ge n+1$, and the original map is the composite
$$
X\longrightarrow Z_n\xrightarrow{\ g\ }Y,
$$
since $g$ extends $f$ on $X$. Thus $f$ has the required factorization.
:::
