---
schema: qual/card@1
id: E-AMD-H6ID66W4
kind: problem
title: $\ff(R[t])=\ff(R)(t)$
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Polynomials
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that $\operatorname{Frac}(R[t]) \cong \operatorname{Frac}(R)(t)$ for any integral domain $R$.
:::

::: solution
**Goal:** Prove that for any integral domain $R$ with fraction field $K = \operatorname{Frac}(R)$, the fraction field of the polynomial ring $R[t]$ is canonically isomorphic to the field of rational functions $K(t) = \operatorname{Frac}(K[t])$.

<1>1. Definitions of the fields:
    *Proof:*
    <2>1. Let $K = \operatorname{Frac}(R) = \{a/b \mid a, b \in R, b \neq 0\}$.
    <2>2. The polynomial ring $R[t]$ is an integral domain, with fraction field:
        $$\operatorname{Frac}(R[t]) = \left\{ \frac{f(t)}{g(t)} \;\middle|\; f(t), g(t) \in R[t], \, g(t) \neq 0 \right\}.$$
    <2>3. The field of rational functions over $K$ is:
        $$K(t) = \operatorname{Frac}(K[t]) = \left\{ \frac{P(t)}{Q(t)} \;\middle|\; P(t), Q(t) \in K[t], \, Q(t) \neq 0 \right\}.$$

<1>2. Inclusion $\operatorname{Frac}(R[t]) \subseteq K(t)$:
    *Proof:*
    <2>1. Because $R \subseteq K$, the polynomial ring $R[t]$ is a subring of $K[t]$.
    <2>2. For any $\frac{f(t)}{g(t)} \in \operatorname{Frac}(R[t])$, both $f(t), g(t) \in R[t] \subseteq K[t]$ with $g(t) \neq 0$.
    <2>3. Therefore $\frac{f(t)}{g(t)} \in K(t)$, which shows $\operatorname{Frac}(R[t]) \subseteq K(t)$.

<1>3. Inclusion $K(t) \subseteq \operatorname{Frac}(R[t])$:
    *Proof:*
    <2>1. Let $\frac{P(t)}{Q(t)} \in K(t)$, where $P(t), Q(t) \in K[t]$ and $Q(t) \neq 0$.
    <2>2. Write $P(t) = \sum_{i=0}^m \frac{a_i}{b_i} t^i$ and $Q(t) = \sum_{j=0}^n \frac{c_j}{d_j} t^j$ with $a_i, b_i, c_j, d_j \in R$ and non-zero denominators $b_i, d_j \in R \setminus \{0\}$.
    <2>3. Define the common denominator clearing element $D = \left(\prod_{i=0}^m b_i\right) \left(\prod_{j=0}^n d_j\right) \in R \setminus \{0\}$.
    <2>4. Multiplying numerator and denominator by $D$:
        $$\widetilde{P}(t) = D \cdot P(t) \in R[t] \quad \text{and} \quad \widetilde{Q}(t) = D \cdot Q(t) \in R[t] \setminus \{0\}.$$
    <2>5. Thus:
        $$\frac{P(t)}{Q(t)} = \frac{\widetilde{P}(t)}{\widetilde{Q}(t)} \in \operatorname{Frac}(R[t]).$$
    <2>6. Hence $K(t) \subseteq \operatorname{Frac}(R[t])$.

<1>4. Conclusion:
    $\operatorname{Frac}(R[t]) = K(t) = \operatorname{Frac}(R)(t)$. Q.E.D.
:::
