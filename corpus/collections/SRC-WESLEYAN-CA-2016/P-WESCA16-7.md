---
schema: qual/card@1
id: P-WESCA16-7
kind: problem
title: 'The disk, plane, and sphere are pairwise not conformally equivalent'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Prove that no two of the unit disk $\mathbb D$, the complex plane $\mathbb C$, and the Riemann sphere are conformally equivalent.
:::

::: pf

::: pf-step

The unit disk $\mathbb D$ and the complex plane $\mathbb C$ are not
conformally equivalent.


::: pf-proof

Suppose there were a conformal equivalence
\[
F:\mathbb C\longrightarrow\mathbb D.
\]
Then $F$ would be a bounded entire function, so Liouville's theorem would
force $F$ to be constant, contradicting bijectivity.

If instead a conformal equivalence were given in the other direction,
\[
G:\mathbb D\longrightarrow\mathbb C,
\]
then its holomorphic inverse
\[
G^{-1}:\mathbb C\longrightarrow\mathbb D
\]
would contradict the preceding argument. Hence no conformal equivalence
exists.

:::

:::

::: pf-step

The Riemann sphere is not conformally equivalent to either
$\mathbb C$ or $\mathbb D$.


::: pf-proof

The Riemann sphere is compact. The complex plane is not compact, since the
open cover
\[
\{B(0,n):n\ge1\}
\]
has no finite subcover. The unit disk is not compact either: the open cover
\[
\left\{B\!\left(0,1-\frac1n\right):n\ge2\right\}
\]
has no finite subcover.

A conformal equivalence is, in particular, a homeomorphism. Compactness is
preserved by homeomorphisms. Therefore the compact Riemann sphere cannot be
conformally equivalent to either noncompact domain.

:::

:::

::: pf-step

Consequently the three spaces are pairwise not conformally equivalent.


::: pf-proof

Step <1>1 separates $\mathbb D$ from $\mathbb C$, while step <1>2 separates
the Riemann sphere from each of them.

:::

:::

::: pf-qed

Step <1>3 is the required conclusion.

:::

:::
