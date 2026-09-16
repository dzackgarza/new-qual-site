---
schema: qual/card@1
id: P-TRIV-CA18
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{1+a\cos\theta}$ for $|a|<1$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the formula of Complex Analysis Problem 18 against page 15 of the source PDF and added a remark on the stray dx printed in the source.
---

::: {.problem}
Compute $\displaystyle\int_0^{2\pi} \frac{d\theta}{1 + a\cos\theta}\,\mathrm{d}x$ with $|a| < 1$;
:::

::: {.remark}
Erratum: the trailing $\mathrm{d}x$ is printed in the source after $d\theta$ and is a typo; the integral is $\int_0^{2\pi} \frac{d\theta}{1 + a\cos\theta}$ with integration variable $\theta$ and no $x$ in the integrand.
:::
