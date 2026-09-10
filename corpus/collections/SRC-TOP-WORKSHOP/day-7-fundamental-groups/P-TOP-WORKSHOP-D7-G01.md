---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G01
kind: problem
title: Fundamental groups of punctured products and a wedge of projective planes
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Michigan May ’09) Let $X$ be the space obtained from $S^1\times\mathbb R$ by removing the interior of $k$ disjoint $2$-disks.

(a) Compute the fundamental group $\pi_1(X)$.

(b) What would be your answer to part (a) if $S^1\times\mathbb R$ is replaced by $S^2\times\mathbb R$ and $2$-disks are replaced by $3$-balls?

(c) Let $Y$ be the union of two copies of the real projective plane $\mathbb{RP}^2$ having exactly one point $y$ in common.
Compute $\pi_1(Y,y)$.
:::

::: {.solution}
(a) Choose a compact annular region \(S^1\times[-N,N]\) containing all \(k\) deleted disks. The two noncompact ends deformation retract onto its boundary circles, so \(X\) deformation retracts onto a compact annulus with the interiors of \(k\) disks removed. This is an orientable genus-zero surface with \(k+2\) boundary components, hence it deformation retracts onto a wedge of \(k+1\) circles. Therefore
\[
\pi_1(X)\cong F_{k+1}.
\]

(b) The answer is trivial. Start with \(S^2\times\mathbb R\), which is simply connected. Removing the interior of one embedded \(3\)-ball does not change the fundamental group: if \(M=(M\setminus\operatorname{int}B^3)\cup B^3\), then after thickening the intersection it deformation retracts to \(S^2\), so Seifert--van Kampen gives
\[
\pi_1(M)\cong \pi_1(M\setminus\operatorname{int}B^3).
\]
Applying this successively to the \(k\) disjoint balls gives
\[
\pi_1\bigl((S^2\times\mathbb R)\setminus\textstyle\bigcup_i\operatorname{int}B_i^3\bigr)=0.
\]

(c) The space \(Y\) is the wedge \(\mathbb{RP}^2\vee\mathbb{RP}^2\). Van Kampen therefore gives
\[
\pi_1(Y,y)\cong \pi_1(\mathbb{RP}^2)*\pi_1(\mathbb{RP}^2)
\cong (\mathbb Z/2)*(\mathbb Z/2)
\cong \langle a,b\mid a^2=b^2=1\rangle.
\]
:::
