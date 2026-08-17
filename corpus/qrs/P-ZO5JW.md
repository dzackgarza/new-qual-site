---
schema: qual/card@1
id: P-ZO5JW
kind: problem
title: "Prove that all entire functions that are injective are of\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - casorati-weierstrass
  - biholomorphisms
  - singularities
relations: []
review: draft
solved: true
---

::: problem
Prove that all entire functions that are injective are of the form $f(z) = az + b$ with $a,b\in \CC$ and $a\neq 0$.

> Hint: Apply the Casorati-Weierstrass theorem to $f(1/z)$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $f: \CC \to \CC$ be an injective entire function.

1. **Behavior at infinity:** Consider the function $g(z) = f(1/z)$ on the punctured disk $\DD^* = \DD \setminus \{0\} = \{z \in \CC : 0 < |z| < 1\}$.
   The origin $z = 0$ is an isolated singularity of $g$.

2. **Classification of the singularity at $z = 0$:**

   - **Case 1: Essential singularity.** Suppose $z = 0$ is an essential singularity of $g(z) = f(1/z)$.
     By the **Casorati-Weierstrass Theorem**, the image $g(\DD^*) = f(\CC \setminus \overline{\DD})$ is dense in $\CC$.
     On the other hand, the unit disk $\DD = \{z \in \CC : |z| < 1\}$ is open and non-empty.
     Since $f$ is non-constant (being injective) and entire, by the **Open Mapping Theorem**, $f(\DD)$ is an open, non-empty subset of $\CC$.
     Since $f(\CC \setminus \overline{\DD})$ is dense in $\CC$ and $f(\DD)$ is open and non-empty, their intersection must be non-empty:
     $$
     f(\DD) \cap f(\CC \setminus \overline{\DD}) \neq \emptyset.
     $$
     This means there exist $z_1 \in \DD$ and $z_2 \in \CC \setminus \overline{\DD}$ such that $f(z_1) = f(z_2)$.
     Since $|z_1| < 1 < |z_2|$, $z_1 \neq z_2$, which directly contradicts the injectivity of $f$.
     Thus, $z = 0$ cannot be an essential singularity.

   - **Case 2: Removable singularity.** If $z = 0$ is a removable singularity, then $\lim_{z \to 0} g(z) = \lim_{w \to \infty} f(w) = L \in \CC$.
     This implies $f(z)$ is bounded on $\CC$.
     By **Liouville's Theorem**, $f$ must be constant, contradicting injectivity.

   - **Case 3: Pole.** Therefore, $z = 0$ must be a pole of order $m \geq 1$ for $g(z) = f(1/z)$.
     This means the Laurent expansion of $g(z)$ at $z = 0$ terminates:
     $$
     g(z) = \frac{a_m}{z^m} + \frac{a_{m-1}}{z^{m-1}} + \cdots + a_0 + \sum_{n=1}^\infty c_n z^n.
     $$
     Since $f(w) = g(1/w)$ is entire, there are no positive powers of $z$ in $g(z)$, so $f(w)$ is a polynomial of degree $m \geq 1$:
     $$
     f(z) = a_m z^m + a_{m-1} z^{m-1} + \cdots + a_1 z + a_0, \qquad (a_m \neq 0).
     $$

3. **Determining the degree $m$:** By the Fundamental Theorem of Algebra, for any $c \in \CC$, the equation $f(z) = c$ has exactly $m$ roots in $\CC$ (counted with multiplicity).
   If $m \geq 2$, by choosing $c$ not equal to any critical value of $f$, the equation $f(z) = c$ has $m \geq 2$ distinct solutions in $\CC$.
   This violates injectivity of $f$.
   Thus, we must have $m = 1$.

Therefore, $f(z) = az + b$ with $a, b \in \CC$ and $a \neq 0$.
:::
