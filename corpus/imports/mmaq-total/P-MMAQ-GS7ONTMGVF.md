---
schema: qual/card@1
id: P-MMAQ-GS7ONTMGVF
kind: problem
title: "Let $z, w$ be complex numbers, such that $\\bar{z} w \\neq 1$. Prove that $\\abs{\\frac{w - z}{1 - \\bar{w} z}} < 1 \\; \\; \\; \\mbox{if} \\; |z| < 1 \\; \\mbox{and}\\; |w| < 1$ and also\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - conformal-maps
relations: []
review: draft
---

::: problem
(a) Let $z, w$ be complex numbers, such that $\bar{z} w \neq 1$.
    Prove that
    $$\abs{\frac{w - z}{1 - \bar{w} z}} < 1 \; \; \; \mbox{if} \; |z| < 1 \; \mbox{and}\; |w| < 1,$$
    and also that
    $$\abs{\frac{w - z}{1 - \bar{w} z}} = 1 \; \; \; \mbox{if} \; |z| = 1 \; \mbox{or}\; |w| = 1.$$

(b) Prove that for fixed $w$ in the unit disk $\mathbb D$, the
    mapping $$F: z \mapsto \frac{w - z}{1 - \bar{w} z}$$ satisfies the
    following conditions:

(c) $F$ maps $\mathbb D$ to itself and is holomorphic. 

<!-- -->

(ii) $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and
     $F(w) = 0$.

(iii) $|F(z)| = 1$ if $|z| = 1$.

(iv) $F: {\mathbb D} \mapsto {\mathbb D}$ is bijective.

> Hint: Calculate $F \circ F$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $w, z \in \mathbb{C}$ with $\bar{w}z \neq 1$.
1. (a) Prove that $\left|\frac{w - z}{1 - \bar{w} z}\right| < 1$ if $|z| < 1$ and $|w| < 1$, and equals $1$ if $|z| = 1$ or $|w| = 1$.
2. (b) For fixed $w \in \mathbb{D}$, prove that $F(z) = \frac{w - z}{1 - \bar{w} z}$ satisfies:
   - (i) $F: \mathbb{D} \to \mathbb{D}$ is holomorphic.
   - (ii) $F(0) = w$ and $F(w) = 0$.
   - (iii) $|F(z)| = 1$ for $|z| = 1$.
   - (iv) $F: \mathbb{D} \to \mathbb{D}$ is bijective (an involution, $F \circ F = \text{id}_{\mathbb{D}}$).

---

### Part (a): Modulus Identity for the Blaschke Factor

<1>1. **Algebraic identity comparing numerator and denominator modulus squared.**
  <2>1. Expand $|1 - \bar{w}z|^2 - |w - z|^2$:
  $$|1 - \bar{w}z|^2 = (1 - \bar{w}z)(1 - w\bar{z}) = 1 - w\bar{z} - \bar{w}z + |w|^2|z|^2.$$
  $$|w - z|^2 = (w - z)(\bar{w} - \bar{z}) = |w|^2 - w\bar{z} - \bar{w}z + |z|^2.$$
    *Proof:* Expansion of complex modulus squared $|u|^2 = u \bar{u}$.
  <2>2. Subtracting the two expressions:
  $$|1 - \bar{w}z|^2 - |w - z|^2 = 1 + |w|^2|z|^2 - |w|^2 - |z|^2 = (1 - |w|^2)(1 - |z|^2).$$
    *Proof:* Factoring $1 - |w|^2 - |z|^2 + |w|^2|z|^2 = (1 - |w|^2)(1 - |z|^2)$.
  <2>3. Q.E.D.

<1>2. **Deduce the inequalities.**
  <2>1. If $|z| < 1$ and $|w| < 1$, then $1 - |w|^2 > 0$ and $1 - |z|^2 > 0$, so $(1 - |w|^2)(1 - |z|^2) > 0$.
    *Proof:* Product of two strictly positive numbers.
  <2>2. Thus $|1 - \bar{w}z|^2 > |w - z|^2 \implies |w - z| < |1 - \bar{w}z| \implies \left|\frac{w - z}{1 - \bar{w}z}\right| < 1$.
    *Proof:* Taking positive square roots and dividing by $|1 - \bar{w}z| > 0$.
  <2>3. If $|z| = 1$ or $|w| = 1$, then $(1 - |w|^2)(1 - |z|^2) = 0$, so $|1 - \bar{w}z|^2 = |w - z|^2 \implies \left|\frac{w - z}{1 - \bar{w}z}\right| = 1$.
    *Proof:* At least one factor is zero.
  <2>4. Q.E.D.

---

### Part (b): Properties of the Automorphism $F(z)$

<1>3. **(i) $F$ maps $\mathbb{D} \to \mathbb{D}$ and is holomorphic.**
  <2>1. Since $|w| < 1$, the pole of $F(z)$ is at $z_p = 1/\bar{w}$, which has modulus $|z_p| = 1/|w| > 1$.
    *Proof:* $1 - \bar{w}z = 0 \iff z = 1/\bar{w}$.
  <2>2. Thus the denominator does not vanish on $\overline{\mathbb{D}}$, so $F$ is holomorphic on a neighborhood of $\overline{\mathbb{D}}$.
    *Proof:* Rational function with pole outside the closed unit disk.
  <2>3. By Part (a) (<1>2.<2>2), for all $z \in \mathbb{D}$, $|F(z)| < 1$, so $F(\mathbb{D}) \subseteq \mathbb{D}$.
    *Proof:* $|z| < 1$ and $|w| < 1 \implies |F(z)| < 1$.
  <2>4. Q.E.D.

<1>4. **(ii) $F$ interchanges $0$ and $w$.**
  <2>1. $F(0) = \frac{w - 0}{1 - \bar{w}(0)} = \frac{w}{1} = w$.
    *Proof:* Direct evaluation at $z = 0$.
  <2>2. $F(w) = \frac{w - w}{1 - \bar{w}w} = \frac{0}{1 - |w|^2} = 0$ (since $|w| < 1 \implies 1 - |w|^2 \neq 0$).
    *Proof:* Direct evaluation at $z = w$.
  <2>3. Q.E.D.

<1>5. **(iii) $|F(z)| = 1$ whenever $|z| = 1$.**
  <2>1. This is the $|z| = 1$ case proven in Part (a) (<1>2.<2>3).
    *Proof:* By <1>2.<2>3.
  <2>2. Q.E.D.

<1>6. **(iv) $F: \mathbb{D} \to \mathbb{D}$ is bijective (an involution).**
  <2>1. Compute $(F \circ F)(z) = F(F(z))$:
  $$F(F(z)) = \frac{w - F(z)}{1 - \bar{w} F(z)} = \frac{w - \frac{w - z}{1 - \bar{w} z}}{1 - \bar{w} \frac{w - z}{1 - \bar{w} z}}.$$
    *Proof:* Definition of composition.
  <2>2. Clear denominators by multiplying numerator and denominator by $1 - \bar{w}z$:
  $$F(F(z)) = \frac{w(1 - \bar{w}z) - (w - z)}{(1 - \bar{w}z) - \bar{w}(w - z)} = \frac{w - |w|^2 z - w + z}{1 - \bar{w}z - |w|^2 + \bar{w}z} = \frac{z(1 - |w|^2)}{1 - |w|^2}.$$
    *Proof:* Algebraic expansion and cancellation of terms.
  <2>3. Since $|w| < 1$, $1 - |w|^2 \neq 0$, so $F(F(z)) = z$ for all $z \in \mathbb{D}$.
    *Proof:* Cancellation of $1 - |w|^2$.
  <2>4. Any mapping satisfying $F \circ F = \text{id}_{\mathbb{D}}$ is an involution, hence a bijection of $\mathbb{D}$ onto itself (both injective and surjective).
    *Proof:* $F$ is its own two-sided inverse.
  <2>5. Q.E.D.
:::
