---
schema: qual/card@1
id: P-MMAQ-KF366R6HF2
kind: problem
title: Argument principle
classification:
  areas:
  - complex-analysis
  topics:
  - argument-principle
  - cauchy-integral-theorem
  - integrals
  - meromorphic-functions
relations: []
review: draft
solved: true
---

::: problem
Use Cauchy's theorem to prove the argument principle.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** State and prove the Argument Principle using Cauchy's Theorem.
Specifically, if $f$ is meromorphic in a simply connected domain $\Omega$, and $\gamma$ is a positively oriented simple closed contour in $\Omega$ passing through no zeros or poles of $f$, then: $$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = Z_f - P_f,$$ where $Z_f$ and $P_f$ are the total number of zeros and poles of $f$ inside $\gamma$, counted with multiplicity.

* * *

### Step 1: Local Analysis of the Logarithmic Derivative $\frac{f'(z)}{f(z)}$

<1>1. **Behavior near a zero $z_0$ of multiplicity $m \geq 1$.** <2>1. In a disk $D(z_0, r)$, $f(z) = (z - z_0)^m g(z)$, where $g$ is holomorphic and $g(z) \neq 0$ for all $z \in D(z_0, r)$.
*Proof:* Factoring out the zero of order $m$.
<2>2. Differentiating $f(z)$: $$f'(z) = m(z - z_0)^{m-1} g(z) + (z - z_0)^m g'(z).$$ *Proof:* Product rule.
<2>3. Compute the logarithmic derivative: $$\frac{f'(z)}{f(z)} = \frac{m(z - z_0)^{m-1} g(z) + (z - z_0)^m g'(z)}{(z - z_0)^m g(z)} = \frac{m}{z - z_0} + \frac{g'(z)}{g(z)}.$$ *Proof:* Division by $(z-z_0)^m g(z)$.
<2>4. Since $g$ is holomorphic and non-vanishing on $D(z_0, r)$, $\frac{g'(z)}{g(z)}$ is holomorphic on $D(z_0, r)$.
*Proof:* Quotient of holomorphic functions with non-zero denominator.
<2>5. Thus, $\frac{f'(z)}{f(z)}$ has a simple pole at $z_0$ with residue $\text{Res}\left(\frac{f'}{f}, z_0\right) = m$.
*Proof:* Laurent expansion has principal part $\frac{m}{z-z_0}$.
<2>6. Q.E.D.

<1>2. **Behavior near a pole $w_0$ of order $k \geq 1$.** <2>1. In a disk $D(w_0, r)$, $f(z) = (z - w_0)^{-k} h(z)$, where $h$ is holomorphic and $h(z) \neq 0$ on $D(w_0, r)$.
*Proof:* Factoring out the pole of order $k$.
<2>2. Differentiating $f(z)$: $$f'(z) = -k(z - w_0)^{-k-1} h(z) + (z - w_0)^{-k} h'(z).$$ *Proof:* Product rule.
<2>3. Compute the logarithmic derivative: $$\frac{f'(z)}{f(z)} = \frac{-k(z - w_0)^{-k-1} h(z) + (z - w_0)^{-k} h'(z)}{(z - w_0)^{-k} h(z)} = \frac{-k}{z - w_0} + \frac{h'(z)}{h(z)}.$$ *Proof:* Division by $(z-w_0)^{-k} h(z)$.
<2>4. Since $h$ is holomorphic and non-vanishing on $D(w_0, r)$, $\frac{h'(z)}{h(z)}$ is holomorphic on $D(w_0, r)$.
*Proof:* Quotient of holomorphic functions with non-vanishing denominator.
<2>5. Thus, $\frac{f'(z)}{f(z)}$ has a simple pole at $w_0$ with residue $\text{Res}\left(\frac{f'}{f}, w_0\right) = -k$.
*Proof:* Laurent expansion has principal part $\frac{-k}{z-w_0}$.
<2>6. Q.E.D.

* * *

### Step 2: Global Integration via Cauchy's Theorem on Multiply Connected Domains

<1>3. **Finiteness of zeros and poles inside $\gamma$.** <2>1. The interior $\text{Int}(\gamma)$ is bounded, and its closure $\text{Int}(\gamma) \cup \gamma$ is compact.
*Proof:* $\gamma$ is a Jordan curve in $\mathbb{C}$.
<2>2. Since zeros and poles of a non-trivial meromorphic function are isolated, $\text{Int}(\gamma)$ contains only finitely many zeros $a_1, \dots, a_p$ (with multiplicities $m_1, \dots, m_p$) and finitely many poles $b_1, \dots, b_q$ (with orders $k_1, \dots, k_q$). *Proof:* Compactness prevents infinite accumulation of isolated points.
<2>3. Q.E.D.

<1>4. **Apply Cauchy's Theorem on the deformed contour.** <2>1. Choose pairwise disjoint small disks $D_j = D(a_j, \varepsilon)$ and $\Delta_l = D(b_l, \varepsilon)$ centered at each zero and pole inside $\text{Int}(\gamma)$, with positively oriented boundaries $C(a_j, \varepsilon)$ and $C(b_l, \varepsilon)$.
*Proof:* Small enough $\varepsilon > 0$ ensures disks are disjoint and contained in $\text{Int}(\gamma)$.
<2>2. The function $\frac{f'(z)}{f(z)}$ is holomorphic on the region $\Omega' = \text{Int}(\gamma) \setminus \left( \bigcup_{j=1}^p D_j \cup \bigcup_{l=1}^q \Delta_l \right)$.
*Proof:* All zeros and poles of $f$ have been removed.
<2>3. By Cauchy's Integral Theorem for multiply connected domains: $$\oint_\gamma \frac{f'(z)}{f(z)} \, dz - \sum_{j=1}^p \oint_{C(a_j, \varepsilon)} \frac{f'(z)}{f(z)} \, dz - \sum_{l=1}^q \oint_{C(b_l, \varepsilon)} \frac{f'(z)}{f(z)} \, dz = 0.$$ *Proof:* The boundary of $\Omega'$ is $\gamma - \sum C(a_j, \varepsilon) - \sum C(b_l, \varepsilon)$.
<2>4. Therefore: $$\oint_\gamma \frac{f'(z)}{f(z)} \, dz = \sum_{j=1}^p \oint_{C(a_j, \varepsilon)} \frac{f'(z)}{f(z)} \, dz + \sum_{l=1}^q \oint_{C(b_l, \varepsilon)} \frac{f'(z)}{f(z)} \, dz.$$ *Proof:* Rearrangement of terms.
<2>5. Q.E.D.

* * *

### Step 3: Evaluate Circle Integrals and Conclude

<1>5. **Evaluate the small circle integrals.** <2>1. For each zero $a_j$, using <1>1.<2>3 and Cauchy's Theorem on the holomorphic term $\frac{g_j'}{g_j}$: $$\oint_{C(a_j, \varepsilon)} \frac{f'(z)}{f(z)} \, dz = \oint_{C(a_j, \varepsilon)} \left( \frac{m_j}{z - a_j} + \frac{g_j'(z)}{g_j(z)} \right) dz = m_j (2\pi i) + 0 = 2\pi i m_j.$$ *Proof:* $\oint_{|z-a_j|=\varepsilon} \frac{dz}{z-a_j} = 2\pi i$ and $\oint \frac{g_j'}{g_j}\,dz = 0$ by Cauchy's theorem for holomorphic functions.
<2>2. For each pole $b_l$, using <1>2.<2>3 and Cauchy's Theorem on the holomorphic term $\frac{h_l'}{h_l}$: $$\oint_{C(b_l, \varepsilon)} \frac{f'(z)}{f(z)} \, dz = \oint_{C(b_l, \varepsilon)} \left( \frac{-k_l}{z - b_l} + \frac{h_l'(z)}{h_l(z)} \right) dz = -k_l (2\pi i) + 0 = -2\pi i k_l.$$ *Proof:* $\oint_{|z-b_l|=\varepsilon} \frac{dz}{z-b_l} = 2\pi i$ and $\oint \frac{h_l'}{h_l}\,dz = 0$ by Cauchy's theorem for holomorphic functions.
<2>3. Substituting into <1>4.<2>4: $$\oint_\gamma \frac{f'(z)}{f(z)} \, dz = \sum_{j=1}^p 2\pi i m_j + \sum_{l=1}^q (-2\pi i k_l) = 2\pi i \left( \sum_{j=1}^p m_j - \sum_{l=1}^q k_l \right) = 2\pi i (Z_f - P_f).$$ *Proof:* Definition of total zeros $Z_f = \sum m_j$ and total poles $P_f = \sum k_l$ counting multiplicities.
<2>4. Dividing both sides by $2\pi i$ yields $\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = Z_f - P_f$.
*Proof:* Division by $2\pi i$.
<2>5. Q.E.D.
:::
