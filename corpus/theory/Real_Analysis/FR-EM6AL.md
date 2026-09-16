---
schema: qual/card@1
id: FR-EM6AL
kind: proof
title: Continuity of translation in $L^1$
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

::: {.proposition}
Let $f \in L^1(\RR^n)$, and for $h\in\RR^n$ let $\tau_h f\colon\RR^n\to\CC$ be the translate $\tau_h f(x) \coloneqq f(x + h)$.
Then
$$
\lim_{h \to 0} \norm{\tau_h f - f}_{L^1} = 0.
$$
:::

::: {.proof}
<1>1. Approximate $f$ by a compactly supported continuous function.

<2>1. Let $\varepsilon > 0$.

<2>2. The compactly supported continuous functions are dense in $L^1(\RR^n)$, so there exists $g \in C_c(\RR^n)$ with $\norm{f - g}_{L^1} < \varepsilon / 3$.

<2>3. Lebesgue measure is translation invariant, so $\norm{\tau_h u}_{L^1}=\norm{u}_{L^1}$ for every $u\in L^1(\RR^n)$ and $h\in\RR^n$; hence for every $h$,
$$
\norm{\tau_h f - \tau_h g}_{L^1} = \norm{f - g}_{L^1} < \varepsilon / 3.
$$

<1>2. Bound the translation error of $g$ using uniform continuity.

<2>1. Let $K \coloneqq \supp g + \overline{B(0,1)}$, a compact set, and let $c \coloneqq 1+\vol(K)$.

<2>2. Since $g$ is continuous with compact support, $g$ is [[D-HHVPT|uniformly continuous]] on $\RR^n$.
Hence there exists $\delta \in (0,1]$ such that $\abs{h} < \delta$ implies $\abs{g(x + h) - g(x)} < \varepsilon / (3c)$ for all $x\in\RR^n$.

<2>3. For $\abs{h} < \delta\le 1$, the function $\tau_h g - g$ vanishes outside $K$, so
$$
\norm{\tau_h g - g}_{L^1} \le \vol(K) \cdot \sup_{x\in\RR^n} \abs{g(x+h) - g(x)} \le \vol(K)\cdot\frac{\varepsilon}{3c} < \frac{\varepsilon}{3}.
$$

<1>3. Combine the estimates.

<2>1. For $\abs{h} < \delta$, the triangle inequality and steps <1>1 and <1>2 give
$$
\norm{\tau_h f - f}_{L^1} \le \norm{\tau_h f - \tau_h g}_{L^1} + \norm{\tau_h g - g}_{L^1} + \norm{g - f}_{L^1} < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.
$$

<2>2. Since $\varepsilon > 0$ was arbitrary, $\lim_{h \to 0} \norm{\tau_h f - f}_{L^1} = 0$.
:::
