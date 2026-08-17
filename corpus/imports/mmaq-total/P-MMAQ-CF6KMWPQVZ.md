---
schema: qual/card@1
id: P-MMAQ-CF6KMWPQVZ
kind: problem
title: If $f$ is a finite real valued measurable function on a measurable…
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
If $f$ is a finite real valued measurable function on a measurable set $E \subset \mathbb{R}$, show that the set $\{(x, f(x)) : x \in E\}$ is measurable.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $E \subseteq \RR$ be a Lebesgue measurable set and $f: E \to \RR$ be a measurable function. Prove that the graph $\Gamma(f) = \{(x, f(x)) : x \in E\} \subseteq \RR^2$ is Lebesgue measurable (with Lebesgue measure zero).

<1>1. **Measurability of coordinate functions and difference mapping.**
  <2>1. Define the mapping $\Phi: E \times \RR \to \RR$ by $\Phi(x, y) = y - f(x)$.
  <2>2. The projection $\pi_1(x, y) = x$ is measurable from $E \times \RR$ to $E$, so $(x, y) \mapsto f(x) = (f \circ \pi_1)(x, y)$ is measurable on $E \times \RR$.
    Proof: Composition of the measurable function $f$ with the measurable projection mapping $\pi_1$.
  <2>3. The projection $\pi_2(x, y) = y$ is continuous, hence measurable on $E \times \RR$.
  <2>4. $\Phi(x, y) = \pi_2(x, y) - (f \circ \pi_1)(x, y)$ is a measurable function on $E \times \RR$.
    Proof: Difference of two real-valued measurable functions.

<1>2. **Graph as a preimage of a closed set.**
  <2>1. The graph is the level set $\Gamma(f) = \{(x, y) \in E \times \RR : y = f(x)\} = \Phi^{-1}(\{0\})$.
  <2>2. Since $\{0\}$ is a closed (hence Borel) subset of $\RR$ and $\Phi$ is measurable on $E \times \RR$, $\Phi^{-1}(\{0\})$ is a measurable subset of $E \times \RR$.
    Proof: Preimage of a Borel set under a measurable function is measurable.
  <2>3. Since $E \subseteq \RR$ is measurable and $\RR$ is measurable, $E \times \RR$ is measurable in $\RR^2$. Therefore, $\Gamma(f) \subseteq \RR^2$ is Lebesgue measurable.
    Proof: Subsets measurable in a product measurable set are measurable in $\RR^2$.

<1>3. **Measure computation via Tonelli / Fubini's Theorem.**
  <2>1. $\chi_{\Gamma(f)}$ is a non-negative measurable function on $\RR^2$.
  <2>2. By Tonelli's Theorem:
    $$
    m_2(\Gamma(f)) = \int_{\RR^2} \chi_{\Gamma(f)}(x, y)\,d(x, y) = \int_E \left( \int_\RR \chi_{\Gamma(f)}(x, y)\,dy \right) dx.
    $$
  <2>3. For each fixed $x \in E$, the vertical cross-section is $\Gamma(f)_x = \{y \in \RR : (x, y) \in \Gamma(f)\} = \{f(x)\}$, which is a single point.
  <2>4. The 1D Lebesgue measure of a singleton is $m_1(\{f(x)\}) = 0$.
  <2>5. Therefore:
    $$
    m_2(\Gamma(f)) = \int_E 0\,dx = 0.
    $$
  <2>6. Every subset of $\RR^2$ of Lebesgue outer measure zero is Lebesgue measurable, which gives an alternative proof that $\Gamma(f)$ is Lebesgue measurable.

<1>4. **Conclusion.**
  The graph $\Gamma(f)$ is measurable in $\RR^2$ (and has 2D measure zero). Q.E.D.
:::
