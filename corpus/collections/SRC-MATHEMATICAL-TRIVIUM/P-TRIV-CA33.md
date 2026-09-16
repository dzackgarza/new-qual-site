---
schema: qual/card@1
id: P-TRIV-CA33
kind: problem
title: Poles and residues of the Gamma function at nonpositive integers
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 33, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow against Complex Analysis Problem 33 on page 18 of the source PDF and added an erratum remark for the source's t > 0.
---

::: {.problem}
The Gamma function $\Gamma(z) = \int_0^\infty x^{z-1} e^{-x}\,\mathrm{d}x$ is originally defined only for $t > 0$; it can however be analytically continued to negative values of $z$.
Show that, as $z \to -n$, where $n \in \mathbb{N}_0$, $\Gamma(z)$ has poles; compute the order and the residue of these poles.
:::

::: {.remark}
Erratum: the source's condition "$t > 0$" involves a variable that does not occur in the problem.
The defining integral converges exactly for $\operatorname{Re} z > 0$: at $z = 0$ the integrand behaves like $x^{-1}$ near $x = 0$ and the integral diverges.
The intended condition is $\operatorname{Re} z > 0$.
:::
