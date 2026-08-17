---
schema: qual/card@1
id: P-L2HGH
kind: problem
title: Absolute continuity of the integral for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - continuity-of-measure
  - l1
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
Let $f\in L^1(\RR)$.
Show that
\[
\forall\varepsilon > 0 \exists \delta > 0 \text{ such that } \qquad 
m(E) < \delta 
\implies 
\int _{E} |f(x)| \, dx < \varepsilon
\]
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Given $\eps > 0$, choose $M$ with $\int_{\{|f| > M\}} |f| < \eps/2$.
Proof: $\int_{\{|f|>M\}}|f| = \int |f|\,\chi_{\{|f|>M\}} \to 0$ as $M \to \infty$ by dominated convergence ($|f|\chi_{\{|f|>M\}} \to 0$ pointwise, dominated by $|f| \in L^1$).

<1>2. For this $M$, any measurable $E$ satisfies $\int_E |f| \le \int_{\{|f| > M\}\cap E}|f| + M\,m(E) \le \eps/2 + M\,m(E)$.
Proof: split $\int_E|f| = \int_{E\cap\{|f|>M\}}|f| + \int_{E\cap\{|f|\le M\}}|f|$; the first term is $\le \int_{\{|f|>M\}}|f| < \eps/2$ by <1>1, and the second is $\le M\,m(E)$.

<1>3. Set $\delta = \eps/(2M)$; then $m(E) < \delta$ implies $\int_E |f| < \eps$.
Proof: <1>2 gives $\int_E|f| < \eps/2 + M\delta = \eps$.

<1>4. Q.E.D. Proof: <1>1–<1>3.
:::
