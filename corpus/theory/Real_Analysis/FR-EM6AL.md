---
schema: qual/card@1
id: FR-EM6AL
kind: proof
title: 'Proposition: Continuity in $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
---

::: {.proof}
**Proposition.** For every $f \in L^1(\mathbb{R}^n)$, the translation map $h \mapsto f(\cdot + h)$ is continuous at $0$:
$$\lim_{h \to 0} \| f(\cdot + h) - f \|_{L^1} = 0.$$

<1>1. Reduce to a compactly supported continuous function.
<2>1. Let $\varepsilon > 0$.
<2>2. The compactly supported continuous functions are dense in $L^1(\mathbb{R}^n)$, so there exists $g \in C_c(\mathbb{R}^n)$ with $\| f - g \|_{L^1} < \varepsilon / 3$.
<2>3. Translation preserves the $L^1$ norm, so for every $h$,
$$\| f(\cdot + h) - g(\cdot + h) \|_{L^1} = \| f - g \|_{L^1} < \varepsilon / 3.$$

<1>2. Bound the translation error of $g$ using uniform continuity.
<2>1. Since $g$ is continuous with compact support, $g$ is uniformly continuous on $\mathbb{R}^n$.
<2>2. Hence there exists $\delta > 0$ such that $|h| < \delta$ implies $|g(x + h) - g(x)| < \varepsilon / (3 \operatorname{vol}(\operatorname{supp} g + B(0,1)))$ for all $x$.
<2>3. For $|h| < \delta$, the function $g(\cdot + h) - g$ is supported in the compact set $\operatorname{supp} g + B(0,1)$, so
$$\| g(\cdot + h) - g \|_{L^1} \le \operatorname{vol}(\operatorname{supp} g + B(0,1)) \cdot \sup_x |g(x+h) - g(x)| < \varepsilon / 3.$$

<1>3. Combine the estimates.
<2>1. For $|h| < \delta$, the triangle inequality gives
$$\| f(\cdot + h) - f \|_{L^1} \le \| f(\cdot + h) - g(\cdot + h) \|_{L^1} + \| g(\cdot + h) - g \|_{L^1} + \| g - f \|_{L^1} < \varepsilon / 3 + \varepsilon / 3 + \varepsilon / 3 = \varepsilon.$$
<2>2. Since $\varepsilon > 0$ was arbitrary, $\lim_{h \to 0} \| f(\cdot + h) - f \|_{L^1} = 0$.
:::
