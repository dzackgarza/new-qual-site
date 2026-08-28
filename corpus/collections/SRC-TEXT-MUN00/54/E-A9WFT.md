---
schema: qual/card@1
id: E-A9WFT
kind: exercise
title: Induced homomorphisms of the power and reciprocal power maps
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the maps $g, h: S^1 \to S^1$ given by $g(z) = z^n$ and $h(z) = 1/z^n$.
(Here we represent $S^1$ as the set of complex numbers $z$ of absolute value 1.) Compute the induced homomorphisms $g_*$, $h_*$ of the infinite cyclic group $\pi_1(S^1, b_0)$ into itself.
[Hint: Recall the equation $(\cos \theta + i \sin \theta)^n = \cos n\theta + i \sin n\theta$.]
:::

::: solution
**Goal:** Compute the induced homomorphisms $g_*, h_*: \pi_1(S^1, 1) \to \pi_1(S^1, 1)$ for the power map $g(z) = z^n$ and reciprocal power map $h(z) = z^{-n}$.

<1>1. Identification of $\pi_1(S^1, 1)$ with $\mathbb{Z}$:
    *Proof:*
    <2>1. Take the basepoint $b_0 = 1 = e^{i \cdot 0} \in S^1$.
    <2>2. The standard fundamental loop generating $\pi_1(S^1, 1) \cong \mathbb{Z}$ is:
        $$\gamma(s) = e^{2\pi i s} = \cos(2\pi s) + i \sin(2\pi s) \quad \text{for } s \in [0, 1].$$
    <2>3. Under the standard covering map $p: \mathbb{R} \to S^1$ with $p(t) = e^{2\pi i t}$, the unique lift $\tilde{\gamma}: [0, 1] \to \mathbb{R}$ starting at $0$ is $\tilde{\gamma}(s) = s$, with terminal point $\tilde{\gamma}(1) = 1$.
    <2>4. Thus the isomorphism $\operatorname{deg}: \pi_1(S^1, 1) \xrightarrow{\cong} \mathbb{Z}$ sends $[\gamma] \mapsto 1$.

<1>2. Computation of $g_*$:
    *Proof:*
    <2>1. The composition $g \circ \gamma: [0, 1] \to S^1$ is:
        $$(g \circ \gamma)(s) = g(e^{2\pi i s}) = (e^{2\pi i s})^n = e^{2\pi i n s} = \cos(2\pi n s) + i \sin(2\pi n s).$$
    <2>2. The unique lift of $g \circ \gamma$ to $\mathbb{R}$ starting at $0$ is $\widetilde{g \circ \gamma}(s) = n s$.
    <2>3. The endpoint is $\widetilde{g \circ \gamma}(1) = n$.
    <2>4. Thus $g_*([\gamma]) = [g \circ \gamma] = [\gamma]^n$.
    <2>5. Expressing $\pi_1(S^1, 1) \cong \mathbb{Z}$ additively, $g_*$ is multiplication by $n$:
        $$g_*(k) = n k \quad \text{for all } k \in \mathbb{Z}.$$

<1>3. Computation of $h_*$:
    *Proof:*
    <2>1. The composition $h \circ \gamma: [0, 1] \to S^1$ is:
        $$(h \circ \gamma)(s) = h(e^{2\pi i s}) = (e^{2\pi i s})^{-n} = e^{-2\pi i n s} = \cos(-2\pi n s) + i \sin(-2\pi n s).$$
    <2>2. The unique lift of $h \circ \gamma$ to $\mathbb{R}$ starting at $0$ is $\widetilde{h \circ \gamma}(s) = -n s$.
    <2>3. The endpoint is $\widetilde{h \circ \gamma}(1) = -n$.
    <2>4. Thus $h_*([\gamma]) = [h \circ \gamma] = [\gamma]^{-n}$.
    <2>5. Expressing $\pi_1(S^1, 1) \cong \mathbb{Z}$ additively, $h_*$ is multiplication by $-n$:
        $$h_*(k) = -n k \quad \text{for all } k \in \mathbb{Z}.$$

<1>4. Conclusion:
    Under the canonical identification $\pi_1(S^1, 1) \cong \mathbb{Z}$, the induced homomorphisms are $g_*(k) = n k$ and $h_*(k) = -n k$. Q.E.D.
:::
