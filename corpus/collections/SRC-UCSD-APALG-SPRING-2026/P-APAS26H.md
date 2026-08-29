---
schema: qual/card@1
id: P-APAS26H
kind: problem
title: Convolution algebra of an odd-order group has a subalgebra not of subgroup type
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $G$ be a nontrivial finite group of odd order.
Show that the convolution algebra $\mathcal{C}(G)$ contains a subalgebra $\mathcal{B}$ not isomorphic to $\mathcal{C}(H)$ for any subgroup $H \le G$.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation; algebra homomorphisms respect multiplication, conjugation, and units.
:::

::: {.solution}
<1>1. $\mathcal{C}(G) \cong \mathbb{C}[G]$, the group algebra, which decomposes as $\bigoplus_i M_{n_i}(\mathbb{C})$ (by Maschke's theorem and the Artin–Wedderburn theorem).
Proof: the convolution algebra is the group algebra, which is semisimple.

<1>2. For any subgroup $H \le G$, $\mathcal{C}(H) \cong \mathbb{C}[H]$ is a direct sum of matrix algebras $M_{m_j}(\mathbb{C})$.
Proof: same as <1>1 for $H$.

<1>3. Since $|G|$ is odd, the group algebra $\mathbb{C}[G]$ has a nontrivial $1$-dimensional factor (the trivial representation), and more importantly, $\mathbb{C}[G]$ contains a copy of $\mathbb{C}$ (the trivial representation) as a direct summand.
Proof: the trivial representation is always present.

<1>4. Consider the subalgebra $\mathcal{B} = \mathbb{C} \oplus \mathbb{C}$ (the direct sum of two copies of $\mathbb{C}$, embedded as the span of the trivial character and one other $1$-dimensional character, or more simply as a $2$-dimensional commutative subalgebra).
Proof: construct a candidate subalgebra.

<1>5. Since $|G|$ is odd, $G$ has no element of order $2$, so $\mathbb{C}[G]$ has no nontrivial $1$-dimensional real subalgebra of the form $\mathbb{C} \oplus \mathbb{C}$ arising from a subgroup of order $2$; more precisely, any subgroup $H$ of odd order has $\mathbb{C}[H]$ with an odd number of $1$-dimensional factors, so $\mathbb{C}[H]$ cannot be isomorphic to $\mathbb{C} \oplus \mathbb{C}$ (which has two $1$-dimensional factors).
Proof: a subgroup $H$ of odd order has $\mathbb{C}[H] \cong \bigoplus_j M_{m_j}(\mathbb{C})$ where the number of $1$-dimensional factors equals the number of linear characters of $H$, which is $|H^{\mathrm{ab}}|$, an odd number.

<1>6. Hence $\mathcal{B} = \mathbb{C} \oplus \mathbb{C}$ is a subalgebra of $\mathcal{C}(G)$ that is not isomorphic to $\mathcal{C}(H)$ for any subgroup $H$ (since $\mathcal{C}(H)$ has an odd number of $1$-dimensional factors, while $\mathcal{B}$ has two).
Proof: <1>2 and <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
