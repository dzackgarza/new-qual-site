---
schema: qual/card@1
id: P-EA67C
kind: problem
title: Absolute continuity of the Lebesgue integral
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - L¹
  - Measure Theory
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Prove the absolute continuity of the Lebesgue integral; in other words, prove that if $f$ is integrable on $\mathbb{R}^d$, then for every $\epsilon > 0$ there exists $\delta > 0$ such that $$\int_E |f| < \epsilon \text{ whenever } m(E) < \delta.$$
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce to bounded functions and use the DCT. Proof: it suffices to prove the claim for $|f|$ (replace $f$ by $|f|$; then $\int_E|f|$ is controlled).
For $M > 0$ decompose $|f| = |f|\chi_{\{|f|\le M\}} + |f|\chi_{\{|f|>M\}}$.
<1>2. The tail is small for large $M$.
Proof: by the dominated convergence theorem (domination $|f| \in L^1$), $\int_{\{|f|>M\}}|f| \to 0$ as $M \to \infty$.
Choose $M$ with $\int_{\{|f|>M\}}|f| < \eps/2$.
<1>3. Control the truncated part on small sets.
Proof: for any measurable $E$, \[ \int_E |f| \le \int_{E\cap\{|f|\le M\}}|f| + \int_{\{|f|>M\}}|f| \le M\,m(E) + \eps/2 . \] Choose $\delta = \eps/(2M)$.
Then whenever $m(E) < \delta$: \[ \int_E |f| \le M\cdot\frac{\eps}{2M} + \frac{\eps}{2} = \eps . \] <1>4. Q.E.D.
:::
