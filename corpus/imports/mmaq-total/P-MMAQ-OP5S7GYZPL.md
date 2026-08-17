---
schema: qual/card@1
id: P-MMAQ-OP5S7GYZPL
kind: problem
title: Let $f$ be a non-constant analytic function on $\mathbb D$ with
classification:
  areas:
  - complex-analysis
  topics:
  - holomorphic-functions
relations: []
review: draft
solved: true
---

::: problem
Let $f$ be a non-constant analytic function on $\mathbb D$ with
$f(\mathbb D) \subseteq \mathbb D$. Use $\psi_{a} (f(z))$ (where
$a=f(0)$, $\displaystyle \psi_a(z) = \frac{a - z}{1 - \bar{a}z}$) to
prove that $$\displaystyle
\frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq
\frac{|f(0)| + |z|}{1 - |f(0)||z|}.$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f: \mathbb{D} \to \mathbb{D}$ be a holomorphic self-map of the unit disk with $a = f(0) \in \mathbb{D}$. Using the Blaschke automorphism $\psi_a(w) = \frac{a - w}{1 - \bar{a}w}$, prove that for all $z \in \mathbb{D}$:
$$\frac{|a| - |z|}{1 + |a||z|} \leq |f(z)| \leq \frac{|a| + |z|}{1 - |a||z|}.$$

---

### Step 1: Application of the Schwarz Lemma to the Composite Map

<1>1. **Define $g(z) = \psi_a(f(z))$. Then $g$ satisfies the hypotheses of the Schwarz Lemma.**
  <2>1. The Möbius transformation $\psi_a(w) = \frac{a - w}{1 - \bar{a}w}$ is an automorphism of $\mathbb{D}$ (i.e. $\psi_a \in \text{Aut}(\mathbb{D})$) with $\psi_a(a) = 0$ and $\psi_a^{-1} = \psi_a$.
    *Proof:* For $|a| < 1$, $\psi_a$ is an involution preserving the unit disk and unit circle.
  <2>2. Since $f(\mathbb{D}) \subseteq \mathbb{D}$, the composite map $g(z) = \psi_a(f(z))$ is holomorphic from $\mathbb{D}$ to $\mathbb{D}$.
    *Proof:* Composition of holomorphic functions.
  <2>3. $g(0) = \psi_a(f(0)) = \psi_a(a) = 0$.
    *Proof:* $f(0) = a$.
  <2>4. By the Schwarz Lemma, $|g(z)| \leq |z|$ for all $z \in \mathbb{D}$.
    *Proof:* Standard Schwarz Lemma applied to $g: \mathbb{D} \to \mathbb{D}$ fixing $0$.
  <2>5. Q.E.D.

<1>2. **Express $f(z)$ in terms of $g(z)$.**
  <2>1. Since $\psi_a$ is an involution, $g(z) = \psi_a(f(z)) \implies f(z) = \psi_a(g(z)) = \frac{a - g(z)}{1 - \bar{a} g(z)}$.
    *Proof:* Applying $\psi_a$ to both sides.
  <2>2. Define $w = g(z)$, which satisfies $|w| \leq |z| < 1$.
    *Proof:* By <1>1.<2>4.
  <2>3. Q.E.D.

---

### Step 2: Upper Bound for $|f(z)|$

<1>3. **Prove $|f(z)| \leq \frac{|a| + |z|}{1 - |a||z|}$.**
  <2>1. Using the triangle inequality on the numerator of $f(z) = \frac{a - w}{1 - \bar{a}w}$:
  $$|a - w| \leq |a| + |w| \leq |a| + |z|.$$
    *Proof:* Triangle inequality and $|w| \leq |z|$.
  <2>2. Using the reverse triangle inequality on the denominator:
  $$|1 - \bar{a}w| \geq 1 - |\bar{a}w| = 1 - |a||w| \geq 1 - |a||z| > 0.$$
    *Proof:* Reverse triangle inequality $|1 - u| \geq 1 - |u|$ and $|w| \leq |z| < 1$.
  <2>3. Combining the bounds for numerator and denominator:
  $$|f(z)| = \frac{|a - w|}{|1 - \bar{a}w|} \leq \frac{|a| + |z|}{1 - |a||z|}.$$
    *Proof:* Maximizing numerator and minimizing positive denominator.
  <2>4. Q.E.D.

---

### Step 3: Lower Bound for $|f(z)|$

<1>4. **Prove $|f(z)| \geq \frac{|a| - |z|}{1 + |a||z|}$.**
  <2>1. If $|z| \geq |a|$, then $\frac{|a| - |z|}{1 + |a||z|} \leq 0$, so the inequality $|f(z)| \geq 0 \geq \frac{|a|-|z|}{1+|a||z|}$ holds trivially.
    *Proof:* Modulus of any complex number is non-negative.
  <2>2. Now assume $|z| < |a|$. By the reverse triangle inequality on the numerator:
  $$|a - w| \geq |a| - |w| \geq |a| - |z| > 0.$$
    *Proof:* Reverse triangle inequality and $|w| \leq |z| < |a|$.
  <2>3. By the triangle inequality on the denominator:
  $$|1 - \bar{a}w| \leq 1 + |\bar{a}w| = 1 + |a||w| \leq 1 + |a||z|.$$
    *Proof:* Standard triangle inequality.
  <2>4. Combining the bounds:
  $$|f(z)| = \frac{|a - w|}{|1 - \bar{a}w|} \geq \frac{|a| - |z|}{1 + |a||z|}.$$
    *Proof:* Minimizing positive numerator and maximizing denominator.
  <2>5. Q.E.D.

---

### Step 4: Conclusion

<1>5. **The double inequality holds for all $z \in \mathbb{D}$.**
  <2>1. By <1>3 and <1>4, for all $z \in \mathbb{D}$:
  $$\frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq \frac{|f(0)| + |z|}{1 - |f(0)||z|}.$$
    *Proof:* Combining <1>3.<2>3 and <1>4.<2>4 with $a = f(0)$.
  <2>2. Q.E.D.
:::
