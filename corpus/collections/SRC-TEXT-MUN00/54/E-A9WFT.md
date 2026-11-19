---
schema: qual/card@1
id: E-A9WFT
kind: problem
title: Induced homomorphisms of the power and reciprocal power maps
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 54: Problem 6 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-54-the-fundamental-group-of-the-circle/problem-6-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-54-the-fundamental-group-of-the-circle/problem-6-solution.txt), and against Munkres,
    Topology (2000), Section 54 Exercise 6, printed p. 348. dbFin's is the same computation of the two induced homomorphisms as multiplication by $n$ and by $-n$; the card does it through the lifts $s\mapsto ns$ and $s\mapsto -ns$. Nothing needed repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution on 2026-11-19. Its three steps opened with run-in titles
    ("Identification of pi_1(S^1,1) with Z", "Computation of g_*", "Computation
    of h_*") instead of claims, their substeps were fragments of one computation,
    the page carried no citation, and the closing pf-qed only announced that the
    earlier steps answered the question. It is now three labelled steps whose
    claims are the results, with the two answers boxed where they are proved, and
    it cites the published solution it transcribes, dbFin, "Section 54: Problem 6
    Solution"
    (https://dbfin.com/topology/munkres/chapter-9/section-54-the-fundamental-group-of-the-circle/problem-6-solution/),
    kept at tmp/sources/dbfin/section-54-the-fundamental-group-of-the-circle/problem-6-solution.txt
    and read on 2026-11-11. Checked against the book in
    tmp/sources/munkres-2000-topology.md and the retained PDF: the exercise on
    printed p. 348 (PDF p. 363, printed page = PDF page - 15) with its de Moivre
    hint, and Theorem 54.5 on printed p. 345 (PDF p. 360). No statement changes.

---

::: {.exercise}

Consider the maps $g, h: S^1 \to S^1$ given by $g(z) = z^n$ and $h(z) = 1/z^n$.
(Here we represent $S^1$ as the set of complex numbers $z$ of absolute value 1.) Compute the induced homomorphisms $g_*$, $h_*$ of the infinite cyclic group $\pi_1(S^1, b_0)$ into itself.
[Hint: Recall the equation $(\cos \theta + i \sin \theta)^n = \cos n\theta + i \sin n\theta$.]
:::

::: {.solution}
The computation is that of the published solution of dbFin, "Section 54: Problem 6 Solution": the generator is $[f]$ with $f(t)=(\cos2\pi t,\sin2\pi t)$, the composite $g\circ f$ is $f$ traversed $n$ times and $h\circ f$ is $\bar f$ traversed $n$ times, so the induced homomorphisms are multiplication by $n$ and by $-n$. The exercise is Munkres, *Topology* (2000), Section 54, Exercise 6, printed p. 348; the isomorphism $\pi_1(S^1,b_0)\cong\ZZ$ is Theorem 54.5, printed p. 345, and the identity in the exercise's hint is de Moivre's.

Throughout, $b_0=1=e^{2\pi i\cdot0}$, $\gamma(s)=e^{2\pi is}$ for $s\in[0,1]$, and $p(t)=e^{2\pi it}$ is the covering $\RR\to S^1$.

::: pf

::: {.pf-step #generator}
$[\gamma]$ generates $\pi_1(S^1,b_0)$ and corresponds to $1$ under $\pi_1(S^1,b_0)\cong\ZZ$.

::: pf-proof
Theorem 54.5, printed p. 345, identifies $\pi_1(S^1,b_0)$ with $\ZZ$ through the displacement of the lift of a loop to $\RR$. The lift of $\gamma$ with $\tilde\gamma(0)=0$ is $\tilde\gamma(s)=s$, because $p(s)=e^{2\pi is}=\gamma(s)$, and its displacement is $\tilde\gamma(1)-\tilde\gamma(0)=1$.
:::

:::

::: {.pf-step #g}
$g_*$ is multiplication by $n$: $g_*(k)=\boxed{nk}$ for every $k\in\ZZ$.

::: pf-proof
$(g\circ\gamma)(s)=(e^{2\pi is})^n=e^{2\pi ins}=p(ns)$ by the identity the exercise's hint records, so the lift of $g\circ\gamma$ starting at $0$ is $s\mapsto ns$, with displacement $n$. Hence $g_*$ carries the generator $[\gamma]$ to $n$, and a homomorphism of $\ZZ$ is determined by its value at a generator, so $g_*(k)=nk$.
:::

:::

::: {.pf-step #h}
$h_*$ is multiplication by $-n$: $h_*(k)=\boxed{-nk}$ for every $k\in\ZZ$.

::: pf-proof
$(h\circ\gamma)(s)=(e^{2\pi is})^{-n}=e^{-2\pi ins}=p(-ns)$, so the lift of $h\circ\gamma$ starting at $0$ is $s\mapsto-ns$, with displacement $-n$. Hence $h_*$ carries the generator to $-n$, that is, $h_*(k)=-nk$.
:::

:::

:::

:::
