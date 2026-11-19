---
schema: qual/card@1
id: E-HAT-4.G-1
kind: problem
title: Infinite mapping cylinder deformation retracts onto telescope
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.G, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.G Exercise 1, printed p. 456, the mapping telescope and the instruction to do the case $n=2$ first matching the printed text; the card's argument is the $n=2$ picture applied stage by stage. No retained solution set covers this exercise; the argument is the card's own. Checked: the finite telescope $T_n$ sits inside the finite iterated mapping cylinder $M_n$; the ordinary mapping cylinder retracts onto its target fixed on the target, so the $r_n$ are compatible; and the direct-limit topology of the union makes the assembled homotopy continuous.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 465 carries the running head 456, so
    the printed page is the one the card's earlier event claimed. The durable part of the locator is
    that printed page; the file path names this machine's copy and `tmp/sources` does not survive a VM
    reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 4.G of Hatcher, *Algebraic Topology* (2002), printed p. 456, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

Show that for a sequence of maps $X_0 \xrightarrow{f_1} X_1 \xrightarrow{f_2} \cdots$, the infinite iterated mapping cylinder $M(f_1, f_2, \ldots)$, which is the union of the finite iterated mapping cylinders $M(f_1, \ldots, f_n)$, deformation retracts onto the mapping telescope.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.G Exercise 1, printed p. 456.

::: pf

::: {.pf-step #finite}
Each finite iterated mapping cylinder $M_n=M(f_1,\dots,f_n)$ contains the finite telescope $T_n=X_0\times[0,1]\cup\dots\cup X_{n-1}\times[n-1,n]\cup X_n$ as a closed subspace.

::: pf-proof
By definition $M_n$ is obtained from $\coprod_{j<n}X_j\times I\amalg X_n$ by identifying $(x,1)\in X_j\times I$ with $(f_{j+1}(x),0)\in X_{j+1}\times I$; the copies $X_j\times[j,j+1]$ together with the top copy $X_n$ form a closed subspace of this quotient, which is $T_n$.
:::
:::

::: {.pf-step #retract}
There is a deformation retraction $r_n:M_n\times I\to M_n$ onto $T_n$, and these may be chosen so that $r_{n+1}$ restricts to $r_n$ on $M_n$.

::: pf-proof
The ordinary mapping cylinder of $f$ deformation retracts onto the union of the interval cylinder over its source with its target, by straightening the interval coordinate, and the retraction can be chosen to fix the target pointwise. Applying this to the mapping-cylinder piece added at stage $n$ while leaving the earlier pieces fixed gives $r_n$; because the added piece is disjoint from $M_{n-1}$ away from its boundary, the construction at stage $n+1$ restricts to the earlier one.
:::
:::

::: {.pf-step #assemble}
The $r_n$ assemble to a continuous homotopy $r:M(f_1,f_2,\dots)\times I\to M(f_1,f_2,\dots)$.

::: pf-proof
The infinite iterated mapping cylinder is the union of the nested closed subspaces $M_n$ with the direct-limit topology, so a map on it is continuous exactly when its restrictions to the $M_n$ are; by step [](#retract){.pf-ref} these restrictions agree on overlaps, so they define a continuous $r$.
:::
:::

::: {.pf-step #image}
At time $1$ the image of $r$ is $\bigcup_nT_n$, the mapping telescope, and $r$ fixes it pointwise throughout.

::: pf-proof
Each $r_n$ ends in $T_n$ and fixes $T_n$ at every time, so $r$ ends in $\bigcup_nT_n$ and is the identity there for all $t$; conversely $\bigcup_nT_n\subset\bigcup_nM_n$ is contained in the image at every time because $r$ fixes it.
:::
:::

::: {.pf-step}
$M(f_1,f_2,\dots)$ deformation retracts onto the mapping telescope.

::: pf-proof
Steps [](#assemble){.pf-ref} and [](#image){.pf-ref} exhibit the deformation retraction and identify its image.
:::
:::

:::
:::
