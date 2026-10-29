---
schema: qual/card@1
id: P-CAEXAMPREP-02
kind: problem
title: Contour integrals as residues outside the contour
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Show informally that if $\gamma$ is a simple closed curve traveled counterclockwise, then
\[
\int_\gamma f(z)\,dz
=-2\pi i\sum(\text{residues of $f$ outside $\gamma$, including $\infty$}).
\]
:::

::: {.solution}

Assume, as implicit in the statement, that \(f\) is meromorphic on the Riemann sphere and has no pole on \(\gamma\). Let \(I\) be the set of poles of \(f\) in the bounded component of \(\CC\setminus\gamma\), and let \(O\) be the set of all remaining poles on \(\CC^*\), including \(\infty\) when it is a pole.

::: pf

::: {.pf-step #s1-1}

The positively oriented contour \(\gamma\) satisfies
\[
\int_\gamma f(z)\,dz
=2\pi i\sum_{a\in I}\operatorname{Res}_{z=a}f.
\]


::: pf-proof

Because \(\gamma\) is traveled counterclockwise, it is positively oriented with respect to its bounded interior. The residue theorem applied to that interior therefore gives the displayed equality.

:::

:::

::: {.pf-step #s1-2}

The residues on the Riemann sphere satisfy
\[
\sum_{a\in I}\operatorname{Res}_{z=a}f
+
\sum_{b\in O}\operatorname{Res}_{z=b}f
=0.
\]


::: pf-proof

The total-residue theorem on the Riemann sphere states that the sum of the residues of a meromorphic differential \(f(z)\,dz\) at all points of \(\CC^*\), including \(\infty\), is zero. The sets \(I\) and \(O\) partition those poles because \(\gamma\) contains none of them, so the theorem gives the displayed identity.

:::

:::

::: {.pf-step #s1-3}

Hence
\[
\boxed{
\int_\gamma f(z)\,dz
=-2\pi i\sum_{b\in O}\operatorname{Res}_{z=b}f}.
\]


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
\sum_{a\in I}\operatorname{Res}_{z=a}f
=-
\sum_{b\in O}\operatorname{Res}_{z=b}f.
\]
Substituting this identity into step [](#s1-1){.pf-ref} gives the claimed outside-residue formula. In particular, the residue at \(\infty\) is included in the second sum exactly as stated in the problem.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required identity.

:::

:::

:::
