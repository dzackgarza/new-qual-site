---
schema: qual/card@1
id: P-MMAQ-ZMRHOSV3OG
kind: problem
title: Schwarz lemma and the Schwarz–Pick inequality
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (5) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMCA5, whose solution repeats this Möbius-composition argument."
---

::: {.problem}
1. State the Schwarz lemma for analytic functions in the unit disc.

2. Let $f: \mathbb{D} \to \mathbb{D}$ be an analytic map from the unit disc $\mathbb{D}$ into itself.
   Use the Schwarz lemma to show that for each $a\in \mathbb{D}$ we have `\begin{align*} \dfrac{|f'(a)|}{1-|f(a)|^2} \leq \dfrac{1}{1-|a|^2} \end{align*}`{=tex}
:::

::: {.solution}
### Part 1: Statement of the Schwarz Lemma

**Schwarz Lemma:** Let $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$.
If $g: \mathbb{D} \to \mathbb{D}$ is a holomorphic function satisfying $g(0) = 0$, then:

1. $|g(z)| \leq |z|$ for all $z \in \mathbb{D}$.

2. $|g'(0)| \leq 1$.
   Furthermore, if $|g(z)| = |z|$ for some non-zero $z \in \mathbb{D}$, or if $|g'(0)| = 1$, then $g(z) = e^{i\theta} z$ for some constant $\theta \in \mathbb{R}$ (i.e. $g$ is a rotation).

* * *

### Part 2: Proof of the Schwarz-Pick Derivative Inequality

::: pf

::: pf-step

**Define the disk automorphisms $\phi_a$ and $\psi_{f(a)}$.**

::: pf-proof

::: pf-step

For any $w \in \mathbb{D}$, define the Möbius transformation $\phi_w(z) = \frac{w - z}{1 - \bar{w} z}$.

::: pf-proof

This is a definition; the denominator does not vanish for $|z|<1$ because $|\bar w z|<1$.

:::

:::

::: pf-step

$\phi_w$ is a biholomorphic map from $\mathbb{D}$ onto $\mathbb{D}$ with $\phi_w(w) = 0$, $\phi_w(0) = w$, and $\phi_w^{-1} = \phi_w$.

::: pf-proof

Direct substitution gives $\phi_w(w)=0$, $\phi_w(0)=w$, and $\phi_w(\phi_w(z))=z$. The identity $1-|\phi_w(z)|^2=\frac{(1-|w|^2)(1-|z|^2)}{|1-\bar wz|^2}$ shows that $\phi_w$ maps $\mathbb D$ into $\mathbb D$; being its own inverse, it is a biholomorphism of $\mathbb D$.

:::

:::

::: pf-step

Compute the derivative of $\phi_w(z)$: $$\phi_w'(z) = \frac{-(1 - \bar{w}z) - (w - z)(-\bar{w})}{(1 - \bar{w}z)^2} = \frac{-1 + \bar{w}z + |w|^2 - \bar{w}z}{(1 - \bar{w}z)^2} = \frac{-(1 - |w|^2)}{(1 - \bar{w}z)^2}.$$

::: pf-proof

Quotient rule.

:::

:::

::: {.pf-step #s1-4}

Evaluating $\phi_w'$ at $z = 0$ and $z = w$: $$\phi_w'(0) = -(1 - |w|^2), \qquad \phi_w'(w) = \frac{-(1 - |w|^2)}{(1 - |w|^2)^2} = -\frac{1}{1 - |w|^2}.$$

::: pf-proof

Substitution into derivative formula.

:::

:::

:::

:::

::: pf-step

**Construct the normalized map $g: \mathbb{D} \to \mathbb{D}$.**

::: pf-proof

::: pf-step

Set $b = f(a) \in \mathbb{D}$.
Define $g: \mathbb{D} \to \mathbb{D}$ by: $$g(z) = (\phi_b \circ f \circ \phi_a)(z) = \phi_b(f(\phi_a(z))).$$

::: pf-proof

Composition of holomorphic maps.

:::

:::

::: pf-step

Since $\phi_a(\mathbb{D}) = \mathbb{D}$, $f(\mathbb{D}) \subseteq \mathbb{D}$, and $\phi_b(\mathbb{D}) = \mathbb{D}$, $g$ maps $\mathbb{D}$ into $\mathbb{D}$.

::: pf-proof

Image containment under composition.

:::

:::

::: pf-step

Evaluate $g(0)$: $$g(0) = \phi_b(f(\phi_a(0))) = \phi_b(f(a)) = \phi_b(b) = 0.$$

::: pf-proof

$\phi_a(0) = a$, $f(a) = b$, $\phi_b(b) = 0$.

:::

:::

:::

:::

::: pf-step

**Apply the Schwarz Lemma to $g$.**

::: pf-proof

::: {.pf-step #s3-1}

By Part 1, since $g$ is holomorphic on $\mathbb{D}$, $g(\mathbb{D}) \subseteq \mathbb{D}$, and $g(0) = 0$, we have: $$|g'(0)| \leq 1.$$

::: pf-proof

Schwarz Lemma derivative bound.

:::

:::

:::

:::

::: pf-step

**Compute $g'(0)$ via the Chain Rule.**

::: pf-proof

::: pf-step

By the chain rule applied to $g(z) = \phi_b(f(\phi_a(z)))$: $$g'(z) = \phi_b'(f(\phi_a(z))) \cdot f'(\phi_a(z)) \cdot \phi_a'(z).$$

::: pf-proof

Chain rule for holomorphic functions.

:::

:::

::: pf-step

Evaluating at $z = 0$: $$g'(0) = \phi_b'(f(\phi_a(0))) \cdot f'(\phi_a(0)) \cdot \phi_a'(0) = \phi_b'(f(a)) \cdot f'(a) \cdot \phi_a'(0) = \phi_b'(b) \cdot f'(a) \cdot \phi_a'(0).$$

::: pf-proof

$\phi_a(0) = a$ and $f(a) = b$.

:::

:::

::: pf-step

Substitute $\phi_b'(b) = -\frac{1}{1 - |b|^2} = -\frac{1}{1 - |f(a)|^2}$ and $\phi_a'(0) = -(1 - |a|^2)$ from step [](#s1-4){.pf-ref}: $$g'(0) = \left(-\frac{1}{1 - |f(a)|^2}\right) \cdot f'(a) \cdot \big(-(1 - |a|^2)\big) = \frac{1 - |a|^2}{1 - |f(a)|^2} f'(a).$$

::: pf-proof

Product of the derivative values.

:::

:::

::: {.pf-step #s4-4}

Taking the absolute value: $$|g'(0)| = \frac{1 - |a|^2}{1 - |f(a)|^2} |f'(a)|.$$

::: pf-proof

$1 - |a|^2 > 0$ and $1 - |f(a)|^2 > 0$.

:::

:::

:::

:::

::: pf-step

**Conclusion.**

::: pf-proof

::: pf-step

From steps [](#s3-1){.pf-ref} and [](#s4-4){.pf-ref}: $$\frac{1 - |a|^2}{1 - |f(a)|^2} |f'(a)| \leq 1.$$

::: pf-proof

$|g'(0)| \leq 1$.

:::

:::

::: pf-step

Dividing both sides by $1 - |a|^2 > 0$: $$\frac{|f'(a)|}{1 - |f(a)|^2} \leq \frac{1}{1 - |a|^2}.$$

::: pf-proof

Division by positive real number.

:::

:::

:::

:::

:::

:::
