---
schema: qual/card@1
id: E-SS8.EX-13
kind: problem
title: "SS 8.13: The pseudo-hyperbolic metric and the Schwarz-Pick inequality"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
The **pseudo-hyperbolic distance** between two points $z, w \in \mathbb{D}$ is defined by:
$$\rho(z, w) = \left| \frac{z - w}{1 - \bar{w} z} \right|.$$

(a) Prove that if $f: \mathbb{D} \to \mathbb{D}$ is holomorphic, then:
$$\rho(f(z), f(w)) \le \rho(z, w) \quad \text{for all } z, w \in \mathbb{D}.$$
Moreover, prove that if $f \in \operatorname{Aut}(\mathbb{D})$ is a conformal automorphism of $\mathbb{D}$, then $f$ preserves the pseudo-hyperbolic distance:
$$\rho(f(z), f(w)) = \rho(z, w) \quad \text{for all } z, w \in \mathbb{D}.$$

(b) Prove the **Schwarz-Pick Lemma**: for any holomorphic function $f: \mathbb{D} \to \mathbb{D}$,
$$\frac{|f'(z)|}{1 - |f(z)|^2} \le \frac{1}{1 - |z|^2} \quad \text{for all } z \in \mathbb{D}.$$
:::

::: solution
**Goal:** Prove the contractivity of holomorphic self-maps on the unit disk with respect to the pseudo-hyperbolic metric and derive the infinitesimal Schwarz-Pick inequality.

<1>1. Blaschke Factors on $\mathbb{D}$:
    *Proof:*
    <2>1. For any $\alpha \in \mathbb{D}$, the Blaschke factor (Möbius automorphism):
        $$\psi_\alpha(\zeta) \coloneqq \frac{\zeta - \alpha}{1 - \bar{\alpha} \zeta}$$
        is a conformal automorphism $\psi_\alpha \in \operatorname{Aut}(\mathbb{D})$ with $\psi_\alpha(\alpha) = 0$ and $\psi_\alpha^{-1} = \psi_{-\alpha}$.
    <2>2. Notice that the pseudo-hyperbolic distance can be expressed as:
        $$\rho(z, w) = |\psi_w(z)|.$$

<1>2. Part (a): Proof that $\rho(f(z), f(w)) \le \rho(z, w)$ via Schwarz Lemma:
    *Proof:*
    <2>1. Fix $w \in \mathbb{D}$, and consider the composite function:
        $$g(\zeta) \coloneqq (\psi_{f(w)} \circ f \circ \psi_w^{-1})(\zeta) = \psi_{f(w)}\left( f(\psi_w^{-1}(\zeta)) \right).$$
    <2>2. Since $\psi_w^{-1}: \mathbb{D} \to \mathbb{D}$, $f: \mathbb{D} \to \mathbb{D}$, and $\psi_{f(w)}: \mathbb{D} \to \mathbb{D}$, the map $g$ is a **holomorphic function from $\mathbb{D}$ to $\mathbb{D}$**.
    <2>3. Evaluating at $\zeta = 0$:
        $$g(0) = \psi_{f(w)}(f(\psi_w^{-1}(0))) = \psi_{f(w)}(f(w)) = \frac{f(w) - f(w)}{1 - \overline{f(w)} f(w)} = 0.$$
    <2>4. By the classical **Schwarz Lemma**, since $g: \mathbb{D} \to \mathbb{D}$ is holomorphic with $g(0) = 0$:
        $$|g(\zeta)| \le |\zeta| \quad \text{for all } \zeta \in \mathbb{D}.$$
    <2>5. Setting $\zeta = \psi_w(z)$, we have $\psi_w^{-1}(\zeta) = z$.
    <2>6. Substituting into the Schwarz inequality:
        $$|g(\psi_w(z))| = |\psi_{f(w)}(f(z))| \le |\psi_w(z)|.$$
    <2>7. Recalling the definition of $\rho$:
        $$\rho(f(z), f(w)) = |\psi_{f(w)}(f(z))| \le |\psi_w(z)| = \rho(z, w).$$
    <2>8. **Isometry for Automorphisms:**
        If $f \in \operatorname{Aut}(\mathbb{D})$, then $f^{-1}: \mathbb{D} \to \mathbb{D}$ is also holomorphic.
        Applying the inequality to $f^{-1}$ on the points $f(z)$ and $f(w)$:
        $$\rho(z, w) = \rho(f^{-1}(f(z)), f^{-1}(f(w))) \le \rho(f(z), f(w)).$$
        Combining $\rho(f(z), f(w)) \le \rho(z, w) \le \rho(f(z), f(w))$ gives:
        $$\rho(f(z), f(w)) = \rho(z, w).$$

<1>3. Part (b): Proof of the Schwarz-Pick Lemma:
    *Proof:*
    <2>1. By the Schwarz Lemma applied to $g$, we also have the derivative bound at the origin:
        $$|g'(0)| \le 1.$$
    <2>2. By the Chain Rule, differentiating $g(\zeta) = \psi_{f(w)}(f(\psi_w^{-1}(\zeta)))$ at $\zeta = 0$:
        $$g'(0) = \psi_{f(w)}'(f(w)) \cdot f'(w) \cdot (\psi_w^{-1})'(0).$$
    <2>3. We compute the derivatives of the Blaschke factors:
        - For $\psi_\alpha(\zeta) = \frac{\zeta - \alpha}{1 - \bar{\alpha}\zeta}$:
          $$\psi_\alpha'(\zeta) = \frac{1(1 - \bar{\alpha}\zeta) - (\zeta - \alpha)(-\bar{\alpha})}{(1 - \bar{\alpha}\zeta)^2} = \frac{1 - |\alpha|^2}{(1 - \bar{\alpha}\zeta)^2}.$$
        - At $\zeta = \alpha$: $\psi_\alpha'(\alpha) = \frac{1 - |\alpha|^2}{(1 - |\alpha|^2)^2} = \frac{1}{1 - |\alpha|^2}$.
        - At $\zeta = 0$: $(\psi_w^{-1})'(0) = \psi_{-w}'(0) = \frac{1 - |-w|^2}{(1 - 0)^2} = 1 - |w|^2$.
    <2>4. Substituting these into the formula for $g'(0)$:
        $$g'(0) = \left( \frac{1}{1 - |f(w)|^2} \right) \cdot f'(w) \cdot \left( 1 - |w|^2 \right) = \frac{1 - |w|^2}{1 - |f(w)|^2} f'(w).$$
    <2>5. Since $|g'(0)| \le 1$:
        $$\left| \frac{1 - |w|^2}{1 - |f(w)|^2} f'(w) \right| \le 1 \implies \frac{|f'(w)|}{1 - |f(w)|^2} \le \frac{1}{1 - |w|^2}.$$
    <2>6. Replacing $w$ with $z$ gives the desired Schwarz-Pick inequality.

<1>4. Conclusion:
    $\rho(f(z), f(w)) \le \rho(z, w)$ by Schwarz lemma on Blaschke conjugation, and differentiating at 0 yields $\frac{|f'(z)|}{1-|f(z)|^2} \le \frac{1}{1-|z|^2}$. Q.E.D.
:::
