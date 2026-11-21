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
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher §4.G Exercise 1, the definition of the iterated mapping cylinder in §4.G,
    the mapping-cylinder retraction of §0, Lemma 2.34, and Theorem 4.5. The previous solution's
    central step was false: it claimed that "the ordinary mapping cylinder of $f$ deformation
    retracts onto the union of the interval cylinder over its source with its target", and that
    union is the whole mapping cylinder, so the step said nothing; worse, the retraction it needs is
    onto the telescope inside the iterated cylinder, and no such retraction follows from a
    source-end statement, since a mapping cylinder retracts onto its target end, not its source end.
    The argument is now: $M_n$ and $T_n$ are subcomplexes of the CW complex $M$ and both are
    homotopy equivalent to $X_n$ by explicit collapses, compatibly in $n$; homotopy groups of the
    unions are the direct limits over the finite stages, by compactness of $S^k$ and of $S^k\times I$
    and the finiteness of cells in a compact subspace; the inclusion therefore induces isomorphisms
    on all homotopy groups; and Theorem 4.5, whose second sentence is exactly the statement that an
    inclusion of a subcomplex inducing isomorphisms on homotopy groups is a deformation retract,
    finishes. The page locators are removed from the statement and the lead by the numbering
    convention in force. Not checked: nothing was verified by computation; the disconnected case is
    handled by the componentwise remark in the last step, not separately written out.
---

::: {.problem}
This is Exercise 1 of Section 4.G of Hatcher, *Algebraic Topology* (2002); the statement below is its wording.

Show that for a sequence of maps $X_0 \xrightarrow{f_1} X_1 \xrightarrow{f_2} \cdots$, the infinite iterated mapping cylinder $M(f_1, f_2, \ldots)$, which is the union of the finite iterated mapping cylinders $M(f_1, \ldots, f_n)$, deformation retracts onto the mapping telescope.
:::

::: {.solution}
No retained solution set covers this exercise: Sam's set stops at §4.3, and the retained sets that reach further record no solution for §4.G. The argument is the card's own, using Hatcher's Theorem 4.5, Lemma 2.34 and the mapping-cylinder deformation retraction of §0.

::: pf

::: {.pf-step #setting}
Let $X_0\xrightarrow{f_1}X_1\xrightarrow{f_2}\cdots$ be cellular maps of CW complexes, let $M_n=M(f_1,\dots,f_n)$ and $M=\bigcup_nM_n$ be the finite and infinite iterated mapping cylinders, and let $T_n=X_0\times[0,1]\cup\cdots\cup X_{n-1}\times[n-1,n]\cup X_n$ and $T=\bigcup_nT_n$ be the finite and infinite mapping telescopes. Then $M$ and $T$ are CW complexes and $T$ is a subcomplex of $M$.

::: pf-proof
$M_1$ is the mapping cylinder of $f_1$, a CW complex containing $X_0$ and $X_1$ as subcomplexes. For $n>1$, §4.G defines $M_n$ as the mapping cylinder of the composition $M_{n-1}\to X_{n-1}\xrightarrow{f_n}X_n$ in which the first map is the projection of a mapping cylinder onto its target end; that composition is cellular, so $M_n$ is a CW complex and $M_{n-1}$, its source end, is a subcomplex. The union $M$ carries the weak topology of the $M_n$, hence is a CW complex whose cells are the cells of the $M_n$. Inside $M_n$ the subspace $T_n$ is a subcomplex: $T_1$ is all of $M_1$, and for $n>1$ the space $M_n$ contains $M_{n-1}$ at its source end and the cylinder $X_{n-1}\times[0,1]$ inside $M_{n-1}\times[0,1]$, so $T_n$, which is $T_{n-1}$ together with that cylinder and the copy of $X_n$, is a subcomplex of $M_n$ whenever $T_{n-1}$ is a subcomplex of $M_{n-1}$.
:::
:::

::: {.pf-step #collapses}
Collapsing each interval piece onto its upper end gives deformation retractions $M_n\to X_n$ and $T_n\to X_n$, and these are compatible with the inclusions $M_n\subset M_{n+1}$ and $T_n\subset T_{n+1}$.

::: pf-proof
$M_n$ is the mapping cylinder of $g_n:M_{n-1}\to X_n$, and a mapping cylinder deformation retracts onto its target end, fixing that end (Chapter 0), so $M_n\to X_n$ is a deformation retraction. On $T_n$ the formula sending $(x,s)\in X_j\times[j,j+1]$ to $f_n\circ\cdots\circ f_{j+1}(x)\in X_n$ is continuous, is compatible with the identifications at the ends of the interval pieces, and restricts to the identity on $X_n$, so it is a deformation retraction of $T_n$ onto $X_n$; the deformation is the linear rescaling of $s$ in each piece. Compatibility: the collapse of $M_n$ sends a point to a class in $X_n$, and inside $M_{n+1}$ the collapse of $M_n\subset M_{n+1}$ sends it to the image of that class under $f_{n+1}$, so the two maps $M_n\to X_{n+1}$ obtained from $M_n\to X_n\subset X_{n+1}$ and from $M_n\subset M_{n+1}\to X_{n+1}$ agree; the same computation, and the same formula above, shows that the two maps $T_n\to X_{n+1}$ agree.
:::
:::

::: {.pf-step #pi-union}
For every $k\ge0$, $\pi_k(M)=\varinjlim_n\pi_k(M_n)$ and $\pi_k(T)=\varinjlim_n\pi_k(T_n)$.

::: pf-proof
A based map $S^k\to M$ has compact image, and a compact subset of the CW complex $M$ meets only finitely many cells, so the image lies in a finite subcomplex; a finite subcomplex has finitely many cells, each of which is a cell of some $M_n$, so it lies in $M_n$ for $n$ large. A homotopy $S^k\times I\to M$ is handled the same way, since $S^k\times I$ is compact. Hence every class in $\pi_k(M)$ is represented at some finite stage, and two classes that agree in $M$ already agree at some finite stage after stabilizing: $\pi_k(M)$ is the direct limit of the $\pi_k(M_n)$. The union $T=\bigcup_nT_n$ and the finite subcomplexes of $T$ are treated by the same compactness argument.
:::
:::

::: {.pf-step #iso}
The inclusion $T\subset M$ induces an isomorphism $\pi_k(T)\to\pi_k(M)$ for every $k\ge0$.

::: pf-proof
By steps [](#pi-union){.pf-ref} and [](#collapses){.pf-ref} both sides are the direct limit of one system, $\pi_k(X_0)\to\pi_k(X_1)\to\cdots$: the isomorphisms $\pi_k(T_n)\to\pi_k(X_n)$ and $\pi_k(M_n)\to\pi_k(X_n)$ are compatible with the maps of the system, because step [](#collapses){.pf-ref} shows that the collapse of $M_n$ and the collapse of $T_n$ agree on $T_n$. The map induced by the inclusion $T\subset M$ is, at each stage, the map induced by the inclusion of subcomplexes $T_n\subset M_n$, so under these identifications it is the identity of the direct limit, in particular an isomorphism.
:::
:::

::: {.pf-step #conclusion}
The mapping telescope $T$ is a deformation retract of the infinite iterated mapping cylinder $M$.

::: pf-proof
$T$ is a subcomplex of the CW complex $M$ by step [](#setting){.pf-ref}, and the inclusion induces isomorphisms on $\pi_k$ for all $k$ by step [](#iso){.pf-ref}. Theorem 4.5 states that a map between connected CW complexes inducing isomorphisms on all homotopy groups is a homotopy equivalence, and that when the map is the inclusion of a subcomplex the conclusion strengthens to that subcomplex being a deformation retract of the whole. So $T$ is a deformation retract of $M$ when these complexes are connected, and in general one applies the theorem component by component: step [](#iso){.pf-ref} with $k=0$ shows that each component of $M$ meets $T$ in a single component, and the argument of steps [](#pi-union){.pf-ref} to [](#iso){.pf-ref} restricts to that pair of components.
:::
:::

:::
:::
