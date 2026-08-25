---
schema: qual/card@1
id: P-Y34JB
kind: problem
title: The graph of a measurable function on $\RR$ has measure zero in $\RR^2$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fubini-Tonelli
relations: []
review: draft
---

:::{.problem}
Let $f$ be a measurable function on $\mathbb{R}$. Show that the graph of $f$ has measure zero in $\mathbb{R}^{2}$.
:::

:::{.solution}
Write
\[
\Gamma \da \ts{(x, f(x)) \st x\in \RR} \subseteq \RR^d
.\]
Then
\[
\mu(\Gamma) 
&= \int_{\RR^d} \chi_\Gamma \dmu \\
&= \int_{\RR^{d-1}}\int_\RR \chi_\Gamma(x, y) \dy \dx \\
&= \int_{\RR^{d-1}} 0 \dx \\
&= 0
,\]
using that $\int_\RR \chi_\Gamma(x, y) \dy = 0$ since if $x$ is fixed then $\chi_\Gamma(x, y) = \ts{f(x)}$ is a point with measure zero.
Since $f$ is measurable, $\Gamma$ is a measurable set and $\chi_\Gamma$ is measurable.
Since the iterated integral was finite, the equalities are justified by Fubini-Tonelli.
:::

