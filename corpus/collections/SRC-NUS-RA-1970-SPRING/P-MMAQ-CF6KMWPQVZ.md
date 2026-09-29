---
schema: qual/card@1
id: P-MMAQ-CF6KMWPQVZ
kind: problem
title: The graph of a measurable function is measurable
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
If $f$ is a finite real valued measurable function on a measurable set $E \subset \mathbb{R}$, show that the set $\{(x, f(x)) : x \in E\}$ is measurable.
:::

::: {.solution}
Let $E \subseteq \RR$ be a Lebesgue measurable set, let $f: E \to \RR$ be measurable, and let $\Gamma(f) = \{(x, f(x)) : x \in E\} \subseteq \RR^2$ be its graph. We show that $\Gamma(f)$ is Lebesgue measurable with measure zero.

::: pf

::: pf-step
**Measurability of coordinate functions and difference mapping.**

::: pf-proof

::: pf-step
Define the mapping $\Phi: E \times \RR \to \RR$ by $\Phi(x, y) = y - f(x)$.
:::

::: pf-step
The projection $\pi_1(x, y) = x$ is measurable from $E \times \RR$ to $E$, so $(x, y) \mapsto f(x) = (f \circ \pi_1)(x, y)$ is measurable on $E \times \RR$.

::: pf-proof
Composition of the measurable function $f$ with the measurable projection mapping $\pi_1$.
:::

:::

::: pf-step
The projection $\pi_2(x, y) = y$ is continuous, hence measurable on $E \times \RR$.
:::

::: pf-step
$\Phi(x, y) = \pi_2(x, y) - (f \circ \pi_1)(x, y)$ is a measurable function on $E \times \RR$.

::: pf-proof
Difference of two real-valued measurable functions.
:::

:::

:::

:::

::: {.pf-step #graph-preimage-measurable}
**Graph as a preimage of a closed set.**

::: pf-proof

::: pf-step
The graph is the level set $\Gamma(f) = \{(x, y) \in E \times \RR : y = f(x)\} = \Phi^{-1}(\{0\})$.
:::

::: pf-step
Since $\{0\}$ is a closed (hence Borel) subset of $\RR$ and $\Phi$ is measurable on $E \times \RR$, $\Phi^{-1}(\{0\})$ is a measurable subset of $E \times \RR$.

::: pf-proof
Preimage of a Borel set under a measurable function is measurable.
:::

:::

::: pf-step
Since $E \subseteq \RR$ is measurable and $\RR$ is measurable, $E \times \RR$ is measurable in $\RR^2$. Therefore, $\Gamma(f) \subseteq \RR^2$ is Lebesgue measurable.

::: pf-proof
Subsets measurable in a product measurable set are measurable in $\RR^2$.
:::

:::

:::

:::

::: {.pf-step #measure-of-graph-is-zero}
**Measure computation via Tonelli / Fubini's Theorem.**

::: pf-proof

::: pf-step
$\chi_{\Gamma(f)}$ is a non-negative measurable function on $\RR^2$.
:::

::: pf-step
By Tonelli's Theorem:
$$
m_2(\Gamma(f)) = \int_{\RR^2} \chi_{\Gamma(f)}(x, y)\,d(x, y) = \int_E \left( \int_\RR \chi_{\Gamma(f)}(x, y)\,dy \right) dx.
$$
:::

::: pf-step
For each fixed $x \in E$, the vertical cross-section is $\Gamma(f)_x = \{y \in \RR : (x, y) \in \Gamma(f)\} = \{f(x)\}$, which is a single point.
:::

::: pf-step
The 1D Lebesgue measure of a singleton is $m_1(\{f(x)\}) = 0$.
:::

::: pf-step
Therefore:
$$
m_2(\Gamma(f)) = \int_E 0\,dx = 0.
$$
:::

::: pf-step
Every subset of $\RR^2$ of Lebesgue outer measure zero is Lebesgue measurable, which gives an alternative proof that $\Gamma(f)$ is Lebesgue measurable.
:::

:::

:::

::: pf-qed
By steps [](#graph-preimage-measurable){.pf-ref} and [](#measure-of-graph-is-zero){.pf-ref}, $\Gamma(f)$ is Lebesgue measurable in $\RR^2$ with $m_2(\Gamma(f)) = 0$.
:::

:::
