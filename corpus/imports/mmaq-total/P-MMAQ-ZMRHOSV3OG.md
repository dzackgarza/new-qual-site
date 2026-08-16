---
schema: qual/card@1
id: P-MMAQ-ZMRHOSV3OG
kind: problem
title: State the Schwarz lemma for analytic functions in the unit disc.
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
relations: []
review: draft
---

::: problem
1.  State the Schwarz lemma for analytic functions in the unit disc.

2.  Let $f: \mathbb{D} \to \mathbb{D}$ be an analytic map from the
    unit disc $\mathbb{D}$ into itself. Use the Schwarz lemma to
    show that for each $a\in \mathbb{D}$ we have
    `\begin{align*}
    \dfrac{|f'(a)|}{1-|f(a)|^2} \leq \dfrac{1}{1-|a|^2}
    \end{align*}`{=tex}
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**
1. State the classical Schwarz Lemma for holomorphic self-maps of the unit disk fixing the origin.
2. Prove the Schwarz-Pick Lemma: for any holomorphic $f: \mathbb{D} \to \mathbb{D}$ and any $a \in \mathbb{D}$,
$$\frac{|f'(a)|}{1 - |f(a)|^2} \leq \frac{1}{1 - |a|^2}.$$

---

### Part 1: Statement of the Schwarz Lemma

**Schwarz Lemma:** Let $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$. If $g: \mathbb{D} \to \mathbb{D}$ is a holomorphic function satisfying $g(0) = 0$, then:
1. $|g(z)| \leq |z|$ for all $z \in \mathbb{D}$.
2. $|g'(0)| \leq 1$.
Furthermore, if $|g(z)| = |z|$ for some non-zero $z \in \mathbb{D}$, or if $|g'(0)| = 1$, then $g(z) = e^{i\theta} z$ for some constant $\theta \in \mathbb{R}$ (i.e. $g$ is a rotation).

---

### Part 2: Proof of the Schwarz-Pick Derivative Inequality

<1>1. **Define the disk automorphisms $\phi_a$ and $\psi_{f(a)}$.**
  <2>1. For any $w \in \mathbb{D}$, define the Möbius transformation $\phi_w(z) = \frac{w - z}{1 - \bar{w} z}$.
    *Proof:* Standard disk automorphism.
  <2>2. $\phi_w$ is a biholomorphic map from $\mathbb{D}$ onto $\mathbb{D}$ with $\phi_w(w) = 0$, $\phi_w(0) = w$, and $\phi_w^{-1} = \phi_w$.
    *Proof:* Direct algebraic properties of the Blaschke factor.
  <2>3. Compute the derivative of $\phi_w(z)$:
  $$\phi_w'(z) = \frac{-(1 - \bar{w}z) - (w - z)(-\bar{w})}{(1 - \bar{w}z)^2} = \frac{-1 + \bar{w}z + |w|^2 - \bar{w}z}{(1 - \bar{w}z)^2} = \frac{-(1 - |w|^2)}{(1 - \bar{w}z)^2}.$$
    *Proof:* Quotient rule.
  <2>4. Evaluating $\phi_w'$ at $z = 0$ and $z = w$:
  $$\phi_w'(0) = -(1 - |w|^2), \qquad \phi_w'(w) = \frac{-(1 - |w|^2)}{(1 - |w|^2)^2} = -\frac{1}{1 - |w|^2}.$$
    *Proof:* Substitution into derivative formula.
  <2>5. Q.E.D.

<1>2. **Construct the normalized map $g: \mathbb{D} \to \mathbb{D}$.**
  <2>1. Set $b = f(a) \in \mathbb{D}$. Define $g: \mathbb{D} \to \mathbb{D}$ by:
  $$g(z) = (\phi_b \circ f \circ \phi_a)(z) = \phi_b(f(\phi_a(z))).$$
    *Proof:* Composition of holomorphic maps.
  <2>2. Since $\phi_a(\mathbb{D}) = \mathbb{D}$, $f(\mathbb{D}) \subseteq \mathbb{D}$, and $\phi_b(\mathbb{D}) = \mathbb{D}$, $g$ maps $\mathbb{D}$ into $\mathbb{D}$.
    *Proof:* Image containment under composition.
  <2>3. Evaluate $g(0)$:
  $$g(0) = \phi_b(f(\phi_a(0))) = \phi_b(f(a)) = \phi_b(b) = 0.$$
    *Proof:* $\phi_a(0) = a$, $f(a) = b$, $\phi_b(b) = 0$.
  <2>4. Q.E.D.

<1>3. **Apply the Schwarz Lemma to $g$.**
  <2>1. By Part 1, since $g$ is holomorphic on $\mathbb{D}$, $g(\mathbb{D}) \subseteq \mathbb{D}$, and $g(0) = 0$, we have:
  $$|g'(0)| \leq 1.$$
    *Proof:* Schwarz Lemma derivative bound.
  <2>2. Q.E.D.

<1>4. **Compute $g'(0)$ via the Chain Rule.**
  <2>1. By the chain rule applied to $g(z) = \phi_b(f(\phi_a(z)))$:
  $$g'(z) = \phi_b'(f(\phi_a(z))) \cdot f'(\phi_a(z)) \cdot \phi_a'(z).$$
    *Proof:* Multivariable/complex chain rule.
  <2>2. Evaluating at $z = 0$:
  $$g'(0) = \phi_b'(f(\phi_a(0))) \cdot f'(\phi_a(0)) \cdot \phi_a'(0) = \phi_b'(f(a)) \cdot f'(a) \cdot \phi_a'(0) = \phi_b'(b) \cdot f'(a) \cdot \phi_a'(0).$$
    *Proof:* $\phi_a(0) = a$ and $f(a) = b$.
  <2>3. Substitute $\phi_b'(b) = -\frac{1}{1 - |b|^2} = -\frac{1}{1 - |f(a)|^2}$ and $\phi_a'(0) = -(1 - |a|^2)$ from <1>1.<2>4:
  $$g'(0) = \left(-\frac{1}{1 - |f(a)|^2}\right) \cdot f'(a) \cdot \big(-(1 - |a|^2)\big) = \frac{1 - |a|^2}{1 - |f(a)|^2} f'(a).$$
    *Proof:* Product of the derivative values.
  <2>4. Taking the absolute value:
  $$|g'(0)| = \frac{1 - |a|^2}{1 - |f(a)|^2} |f'(a)|.$$
    *Proof:* $1 - |a|^2 > 0$ and $1 - |f(a)|^2 > 0$.
  <2>5. Q.E.D.

<1>5. **Conclusion.**
  <2>1. From <1>3.<2>1 and <1>4.<2>4:
  $$\frac{1 - |a|^2}{1 - |f(a)|^2} |f'(a)| \leq 1.$$
    *Proof:* $|g'(0)| \leq 1$.
  <2>2. Dividing both sides by $1 - |a|^2 > 0$:
  $$\frac{|f'(a)|}{1 - |f(a)|^2} \leq \frac{1}{1 - |a|^2}.$$
    *Proof:* Division by positive real number.
  <2>3. Q.E.D.
:::
