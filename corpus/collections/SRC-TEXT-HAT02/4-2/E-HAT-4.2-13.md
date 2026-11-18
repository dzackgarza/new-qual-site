---
schema: qual/card@1
id: E-HAT-4.2-13
kind: problem
title: "Isomorphism on $\\pi_i$ for $i \\leq n$ in $n$-dimensional complexes"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 13 (AT.txt 19396-19398) and correct as it stands. Checked the
    delicate step: the pair (M_f~, X~) is n-connected, so relative Hurewicz kills H_i for i<=n and
    identifies pi_{n+1} of the pair with H_{n+1} of the pair; pi_{n+1}(M_f~,X~) is a quotient of
    pi_{n+1}(M_f~) because pi_n(X~) -> pi_n(M_f~) is an isomorphism; and that quotient maps to
    H_{n+1}(M_f~) = H_{n+1}(Y~) = 0 by naturality, since Y~ is n-dimensional. Hence H_{n+1} of the pair
    vanishes too, the homology exact sequence gives an isomorphism in degrees <= n, and both sides vanish
    above n, so the lift is a homology isomorphism in all degrees. Then Exercise 12 applies. Also checked
    the low cases the card separates: n=0 gives two points, and n=1 gives contractible universal covers so
    Exercise 12 applies directly. Not checked: nothing outside this exercise.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument above, whose shape is correct.
    Made explicit: the vanishing of $\pi_i$ of the mapping-cylinder pair from the two long
    exact sequences, the surjectivity half of the relative Hurewicz theorem being all that is
    needed in degree $n+1$ (the prose used the isomorphism it does not give), the naturality
    square that kills the Hurewicz images, and the two low-dimensional cases. Cited:
    Proposition 4.1 printed p. 342, the pair sequence printed p. 344, Theorem 4.37 printed
    p. 371, Exercise 12 printed p. 389, the exercise printed p. 390. Not claimed: a retained
    solution set, so the argument is the card's own; and the citation of Corollary 2.34 for
    the vanishing of $H_{>n}$ of an $n$-dimensional CW complex is by chapter and statement,
    the cellular argument on printed p. 139 being the reason.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Correction to this date's earlier note, from a search of the retained sets after the
    proof was written. The card said no retained solution set covers the exercise; Steven
    V. Sam's set does, at Exercise 4.2.13, PDF p. 22, following the same reduction and
    closing with Exercise 4.2.12. The body now cites it and states what the card supplies
    that the set does not: the pair $(M_{\widetilde f},\widetilde X)$ and the relative
    Hurewicz step in degree $n+1$. Mathematics unchanged and re-read; the exercise is on
    printed p. 390.
---

::: {.problem}
Show that a map between connected $n$-dimensional CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_i$ for $i \leq n$. [Pass to universal covers and use homology.]
:::

::: {.solution}
The published solution is **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), Exercise 4.2.13, PDF p. 22**: the passage to universal covers, the reduction to proving that $\widetilde f$ is a homology isomorphism, and the closing appeal to Exercise 4.2.12 are that solution's. What the card supplies is the step the set elides: the absolute Hurewicz theorem does not apply to $\widetilde X$, whose own homotopy groups need not vanish below $n$, so the argument runs through the relative Hurewicz theorem for the mapping-cylinder pair, Theorem 4.37, printed p. 371, and needs its surjectivity in degree $n+1$. The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 13, printed p. 390, and the hint followed is the exercise's own.

Throughout $f:X\to Y$ is a map of connected $n$-dimensional CW complexes inducing isomorphisms $f_*:\pi_i(X)\to\pi_i(Y)$ for $i\le n$, and $p_X:\widetilde X\to X$, $p_Y:\widetilde Y\to Y$ are the universal covers.

::: pf

::: {.pf-step #lift}
$f_*$ is an isomorphism on $\pi_1$, so $f$ lifts to a map of universal covers $\widetilde f:\widetilde X\to\widetilde Y$ with $p_Y\widetilde f=fp_X$, and $\widetilde f_*:\pi_i(\widetilde X)\to\pi_i(\widetilde Y)$ is an isomorphism for $2\le i\le n$.

::: pf-proof
A map lifts to the universal covers exactly when it carries $\pi_1$ of the domain into the subgroup $\pi_1(\widetilde Y)=0$ of $\pi_1(Y)$, that is, when $f_*\pi_1(X)=0$; here $f_*$ is an isomorphism onto $\pi_1(Y)$, so this holds only after choosing the basepoints in the same path component, which is the case. For $i\ge2$ the covering projection induces an isomorphism $\pi_i(\widetilde X)\cong\pi_i(X)$ and likewise for $Y$ (Proposition 4.1, printed p. 342), so $\widetilde f_*$ is the conjugate of $f_*$ and is an isomorphism in the stated range.

:::

:::

::: {.pf-step #low-dimensions}
The claim holds for $n\le1$.

::: pf-proof
For $n=0$ a connected $0$-dimensional CW complex is a point, so $f$ is a homeomorphism. For $n=1$ the universal covers of connected graphs are trees (Proposition 1A.2, printed p. 84), hence contractible, so $\widetilde f$ is a homotopy equivalence; a map whose lift to universal covers is a homotopy equivalence is itself a homotopy equivalence, and $\widetilde f$ is one because it is a map between contractible spaces.

:::

:::

::: {.pf-step #n-connected}
For $n\ge2$ the pair $(M_{\widetilde f},\widetilde X)$, where $M_{\widetilde f}$ is the mapping cylinder of $\widetilde f$, is $(n-1)$-connected: $\pi_i(M_{\widetilde f},\widetilde X)=0$ for $i\le n$.

::: pf-proof
The pair is path connected. Its homotopy exact sequence (printed p. 344) reads
$$
\pi_i(\widetilde X)\xrightarrow{\ \widetilde f_*\ }\pi_i(\widetilde Y)\to\pi_i(M_{\widetilde f},\widetilde X)\to\pi_{i-1}(\widetilde X)\xrightarrow{\ \widetilde f_*\ }\pi_{i-1}(\widetilde Y)
$$
for $i\ge2$, using $M_{\widetilde f}\simeq\widetilde Y$. For $2\le i\le n$ both outer maps are isomorphisms by step [](#lift){.pf-ref}, so the middle group is zero; for $i=1$ the pair is simply connected relative to $\widetilde X$ because $\widetilde X$ is, and $\pi_1$ of the pair vanishes whenever the inclusion induces a surjection on $\pi_1$.

:::

:::

::: {.pf-step #hurewicz-low}
$H_i(M_{\widetilde f},\widetilde X;\ZZ)=0$ for $i\le n$.

::: pf-proof
Theorem 4.37 (relative Hurewicz, printed p. 371) for the $(n-1)$-connected pair of step [](#n-connected){.pf-ref} gives $H_i(M_{\widetilde f},\widetilde X)=0$ for $i\le n$.

:::

:::

::: {.pf-step #hurewicz-degree}
$H_{n+1}(M_{\widetilde f},\widetilde X;\ZZ)=0$.

::: pf-proof
Theorem 4.37 also gives that the Hurewicz map $\pi_{n+1}(M_{\widetilde f},\widetilde X)\to H_{n+1}(M_{\widetilde f},\widetilde X)$ is surjective; it is enough to show that every element of the source dies. Every element of $\pi_{n+1}(M_{\widetilde f},\widetilde X)$ is the image of an element of $\pi_{n+1}(M_{\widetilde f})$ by exactness of the pair sequence, and naturality of the Hurewicz map makes the diagram
$$
\begin{array}{ccc}
\pi_{n+1}(M_{\widetilde f})&\longrightarrow&\pi_{n+1}(M_{\widetilde f},\widetilde X)\\
\downarrow&&\downarrow\\
H_{n+1}(M_{\widetilde f})&\longrightarrow&H_{n+1}(M_{\widetilde f},\widetilde X)
\end{array}
$$
commute. Since $M_{\widetilde f}\simeq\widetilde Y$ and $\widetilde Y$ is an $n$-dimensional CW complex, $H_{n+1}(M_{\widetilde f})=H_{n+1}(\widetilde Y)=0$, so the image of every element is zero.

:::

:::

::: {.pf-step #homology-iso}
$\widetilde f_*:H_i(\widetilde X)\to H_i(\widetilde Y)$ is an isomorphism for all $i$.

::: pf-proof
The long exact sequence of the pair $(M_{\widetilde f},\widetilde X)$, with $M_{\widetilde f}\simeq\widetilde Y$, contains
$$
H_{i+1}(M_{\widetilde f},\widetilde X)\to H_i(\widetilde X)\to H_i(\widetilde Y)\to H_i(M_{\widetilde f},\widetilde X) .
$$
For $i\le n$ the outer groups vanish by step [](#hurewicz-low){.pf-ref} and step [](#hurewicz-degree){.pf-ref} (the latter for $i=n$), so the middle map is an isomorphism for $i\le n$. For $i>n$ both $\widetilde X$ and $\widetilde Y$ are $n$-dimensional CW complexes, so both groups vanish (Corollary 2.34 or the cellular complex of printed p. 139), and the map between two zero groups is an isomorphism.

:::

:::

::: {.pf-step #conclusion}
$f$ is a homotopy equivalence.

::: pf-proof
$f_*:\pi_1(X)\to\pi_1(Y)$ is an isomorphism by hypothesis and $\widetilde f$ is a homology isomorphism by step [](#homology-iso){.pf-ref}; Exercise 12 of §4.2, printed p. 389, then gives that $f$ is a homotopy equivalence. (Equivalently, $\widetilde f$ is a homotopy equivalence by Whitehead's theorem applied to the simply connected complexes $\widetilde X,\widetilde Y$, and a map with that lift and an isomorphism on $\pi_1$ is a homotopy equivalence.)

:::

:::

:::
:::
