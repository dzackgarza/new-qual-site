---
schema: qual/card@1
id: E-4NGIV
kind: exercise
title: Entire doubly periodic functions are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that an entire doubly periodic function is constant.
:::

::: solution
**Goal:** Prove that any entire function $f: \mathbb{C} \to \mathbb{C}$ that is doubly periodic with respect to two $\mathbb{R}$-linearly independent periods $\omega_1, \omega_2 \in \mathbb{C}$ is constant.

<1>1. Setting and fundamental period domain: *Proof:* <2>1. Let $\omega_1, \omega_2 \in \mathbb{C}^\times$ with $\omega_2 / \omega_1 \notin \mathbb{R}$ be two periods of $f$: $$f(z + \omega_1) = f(z) \quad \text{and} \quad f(z + \omega_2) = f(z) \quad \text{for all } z \in \mathbb{C}.$$ <2>2. Define the period lattice $\Lambda = \mathbb{Z}\omega_1 \oplus \mathbb{Z}\omega_2$.
<2>3. Consider the closed fundamental parallelogram: $$P = \{t_1 \omega_1 + t_2 \omega_2 \mid t_1, t_2 \in [0, 1]\}.$$ <2>4. The set $P$ is closed and bounded in $\mathbb{C} \cong \mathbb{R}^2$, hence compact by the Heine-Borel theorem.

<1>2. Boundedness of $f$ on $\mathbb{C}$: *Proof:* <2>1. Since $f$ is entire, $f$ is continuous on $\mathbb{C}$, so its modulus $|f|$ is continuous on the compact set $P$.
<2>2. By the Extreme Value Theorem, $|f|$ attains a finite maximum on $P$: $$M = \sup_{z \in P} |f(z)| < \infty.$$ <2>3. For every $z \in \mathbb{C}$, write $z = x_1 \omega_1 + x_2 \omega_2$ with $x_1, x_2 \in \mathbb{R}$.
<2>4. Setting $m = \lfloor x_1 \rfloor \in \mathbb{Z}$ and $n = \lfloor x_2 \rfloor \in \mathbb{Z}$, the point: $$z_0 := z - m\omega_1 - n\omega_2 = (x_1 - m)\omega_1 + (x_2 - n)\omega_2 \in P.$$ <2>5. By double periodicity of $f$, $f(z) = f(z_0)$.
<2>6. Therefore, $|f(z)| = |f(z_0)| \le M$ for all $z \in \mathbb{C}$.

<1>3. Application of Liouville's Theorem: *Proof:* <2>1. The function $f$ is entire and globally bounded on $\mathbb{C}$.
<2>2. By Liouville's Theorem, any bounded entire function is constant.
<2>3. Hence $f(z) = c$ for all $z \in \mathbb{C}$.
Q.E.D.
:::
