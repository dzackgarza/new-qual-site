---
schema: qual/card@1
id: E-HAT-4.K-4
kind: problem
title: "$SP_2(S^1)$ is a Möbius band"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 4 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $SP_2(S^1)$ is a Möbius band, and that this is consistent with the description of $SP_2(S^n)$ as a mapping cone given in Example 4K.5.

::: {.solution}
Represent an unordered pair of points of \(S^1\subset\mathbb C\) by the chord joining them. Thus
\[
\{z,w\}\longmapsto [z,w]
\]
identifies \(SP_2(S^1)\) with the space of unoriented chords of the circle, including degenerate chords \(z=w\).

A nondegenerate chord is determined by two parameters: the unoriented line through the origin perpendicular to the chord, and the signed distance of the chord from the origin along this line. Equivalently, choose an angle \(\theta\) for a unit normal and a number \(s\in[-1,1]\). Reversing the normal changes \((\theta,s)\) to
\[
(\theta+\pi,-s).
\]
Hence the chord space is
\[
(S^1\times[-1,1])/igl((\theta,s)\sim(\theta+\pi,-s)\bigr),
\]
which is the standard interval-bundle model of the Möbius band. The boundary \(|s|=1\) consists exactly of the degenerate chords \(\{z,z\}\), so the diagonal copy of \(S^1\) is the boundary circle of the Möbius band. Therefore
\[
\boxed{SP_2(S^1)\cong\text{Möbius band}.}
\]

This agrees with Example 4K.5. For \(n=1\), the space denoted there by \(S^n\mathbb{RP}^{\,n-1}\) is the unreduced suspension of \(\mathbb{RP}^0\), hence an interval. The example describes \(SP_2(S^1)\) as the mapping cone obtained by attaching the cone on this interval to the diagonal \(S^1\) via the endpoint identification coming from interchanging the two points. Attaching this twisted strip to the diagonal circle is precisely the usual mapping-cone construction of a Möbius band. Thus the two descriptions coincide.
:::
