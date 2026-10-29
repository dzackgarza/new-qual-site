---
schema: qual/card@1
id: P-WESCA05-I3
kind: problem
title: "State the global Cauchy Theorem"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 3 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State the global Cauchy Theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The global Cauchy theorem states: let \(U\subseteq\CC\) be open, let \(f:U\to\CC\) be analytic, and let \(\Gamma\) be a cycle in \(U\) that is homologous to zero in \(U\). Then
\[
\boxed{\int_\Gamma f(z)\,dz=0.}
\]


::: pf-proof

Here “\(\Gamma\) is homologous to zero in \(U\)” means that its winding number satisfies
\[
\operatorname{Ind}(\Gamma,w)=0
\qquad
\text{for every }w\in\CC\setminus U.
\]
Under this hypothesis the global Cauchy theorem asserts precisely the displayed vanishing of the contour integral.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested statement of the theorem.

:::

:::

:::
