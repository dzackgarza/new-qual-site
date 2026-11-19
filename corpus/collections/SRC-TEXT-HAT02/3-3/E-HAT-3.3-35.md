---
schema: qual/card@1
id: E-HAT-3.3-35
kind: problem
title: Poincaré duality for noncompact manifolds with boundary
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 35; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 35; it matches the printed text. The diagram is transcribed as printed.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument and repaired one sentence: the four neighbouring vertical maps in Hatcher's
    diagram are isomorphisms by the noncompact duality applied to the interior and to $\partial M$,
    and the five lemma then makes the middle map $D_M$ an isomorphism. The stored text broke off
    mid-sentence ("The middle map is ... are isomorphisms"), which is corrected.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked the five-lemma strategy: the collar
    gives the compactly supported LES of the pair; cap product with fundamental classes gives the
    vertical maps, natural by Exercise 34; excision through the collar identifies
    $H_c^k(M,\partial M)$ with $H_c^k$ of the interior, and noncompact duality identifies that with
    $H_{n-k}$ of the interior, which is $H_{n-k}(M)$; $\partial M$ being an $(n-1)$-manifold without
    boundary gives the two adjacent isomorphisms; and the five-lemma then yields the middle one.
    Added: the reason $H_{n-k}(M-\partial M)\cong H_{n-k}(M)$, namely the homotopy equivalence
    supplied by the collar, which the earlier text used without saying, and the identification of
    which one of the two $D_M$ columns is being proved. No defect found in the statement, §3.3
    Exercise 35; the earlier repair of the broken sentence stands. No retained solution set covers
    it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 269 carries the running head 260.
    The durable part of the locator is that printed page; the file path names this machine's copy and
    `tmp/sources` does not survive a VM reset. No mathematics changed.
---

::: {.problem}
This is Exercise 35 of Section 3.3 of Hatcher, *Algebraic Topology* (2002), printed p. 260, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

If $M$ is a noncompact $R$-orientable $n$-manifold with boundary $\partial M$ having a collar neighborhood in $M$, show that there are Poincaré duality isomorphisms $H_c^k(M;R)\approx H_{n-k}(M,\partial M;R)$ for all $k$, using the five-lemma and the following diagram:

$$
\begin{array}{ccccccc}
\cdots\to H_c^{k-1}(\partial M;R)&\to&H_c^k(M,\partial M;R)&\to&H_c^k(M;R)&\to&H_c^k(\partial M;R)\to\cdots\\
\downarrow D_{\partial M}&&\downarrow D_M&&\downarrow D_M&&\downarrow D_{\partial M}\\
\cdots\to H_{n-k}(\partial M;R)&\to&H_{n-k}(M;R)&\to&H_{n-k}(M,\partial M;R)&\to&H_{n-k-1}(\partial M;R)\to\cdots
\end{array}
$$
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; it is the five-lemma comparison of the two exact sequences in the printed diagram. Write $D$ for cap product with the appropriate fundamental class.

::: pf

::: {.pf-step #sequences}
Because $\partial M$ has a collar, there is a long exact sequence
$$
\cdots\to H_c^{k-1}(\partial M;R)\to H_c^k(M,\partial M;R)\to H_c^k(M;R)\to H_c^k(\partial M;R)\to\cdots,
$$
and the pair $(M,\partial M)$ has the homology long exact sequence displayed as the bottom row of the diagram.

::: pf-proof
The collar $\partial M\times[0,1)$ lets one extend compactly supported cochains on $\partial M$ to $M$ and restrict those on $M$ to the complement of the collar, which gives the exact sequence of the pair for compactly supported cohomology; this is the standard compactly supported LES of a manifold with collared boundary. The bottom row is the ordinary LES of the pair in degree $n-k$.
:::

:::

::: {.pf-step #commutes}
Cap product with fundamental classes gives vertical maps making the diagram commute up to sign.

::: pf-proof
The vertical maps are cap products with the fundamental classes of $M$ and of $\partial M$, and naturality of the cap product with respect to inclusions and connecting homomorphisms is the computation of Exercise 34. The signs are the ones arising from the boundary orientation of $\partial M$.
:::

:::

::: {.pf-step #four-iso}
All vertical maps other than $D_M\colon H_c^k(M;R)\to H_{n-k}(M,\partial M;R)$ are isomorphisms.

::: pf-proof
$M-\partial M$ is an $R$-orientable noncompact $n$-manifold without boundary, and excision through the collar gives $H_c^k(M,\partial M;R)\cong H_c^k(M-\partial M;R)$; the noncompact Poincaré duality theorem then identifies this with $H_{n-k}(M-\partial M;R)\cong H_{n-k}(M;R)$, since $M-\partial M$ is homotopy equivalent to $M$. That is the vertical map in the column of $H_c^k(M,\partial M;R)$. For $\partial M$, which is an $R$-orientable $(n-1)$-manifold without boundary, the same theorem gives $H_c^{k-1}(\partial M)\cong H_{n-k}(\partial M)$ and $H_c^k(\partial M)\cong H_{n-k-1}(\partial M)$, the two remaining columns. The shift $H_c^{k+1}(M,\partial M)\cong H_{n-k-1}(M)$ is the same interior duality one degree up, and it is the fourth isomorphism needed.
:::

:::

::: {.pf-step}
$\boxed{H_c^k(M;R)\cong H_{n-k}(M,\partial M;R)}$ for all $k$.

::: pf-proof
The five-lemma applied to the commutative diagram of steps [](#commutes){.pf-ref} and [](#four-iso){.pf-ref} — in which four of every five consecutive vertical maps are isomorphisms — makes the remaining one, $D_M\colon H_c^k(M;R)\to H_{n-k}(M,\partial M;R)$, an isomorphism. As $k$ was arbitrary, Poincaré duality holds in this form for every degree.
:::

:::

:::
:::
