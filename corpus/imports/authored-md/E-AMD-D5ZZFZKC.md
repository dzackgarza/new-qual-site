---
schema: qual/card@1
id: E-AMD-D5ZZFZKC
kind: exercise
title: Every $p$-group has a nontrivial center
classification:
  areas:
  - algebra
  topics:
  - p-groups
  - class-equation
  - centralizers-and-normalizers
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that every $p\dash$group has a nontrivial center.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $p$ be a prime number, and let $G$ be a finite $p$-group of order $|G| = p^n$ with $n \ge 1$.
Prove that the center $Z(G)$ is non-trivial, i.e., $|Z(G)| \ge p > 1$.

<1>1. Group action by conjugation and the Class Equation: <2>1. Let $G$ act on itself by conjugation: $(g, x) \mapsto g x g^{-1}$ for $g, x \in G$.
Proof: Standard group action axioms: $e x e^{-1} = x$ and $g (h x h^{-1}) g^{-1} = (g h) x (g h)^{-1}$.
<2>2. The orbit of an element $x \in G$ under conjugation is its conjugacy class $\operatorname{Cl}(x) = \{g x g^{-1} \mid g \in G\}$.
Proof: Definition of conjugacy class.
<2>3. The stabilizer of $x \in G$ is its centralizer $C_G(x) = \{g \in G \mid g x = x g\}$.
Proof: $g x g^{-1} = x \iff g x = x g$.
<2>4. By the Orbit-Stabilizer Theorem, $|\operatorname{Cl}(x)| = [G : C_G(x)] = \frac{|G|}{|C_G(x)|}$.
Proof: Standard Orbit-Stabilizer Theorem for group actions on finite sets.
<2>5. An element $x$ belongs to the center $Z(G)$ if and only if $|\operatorname{Cl}(x)| = 1$.
Proof: $x \in Z(G) \iff g x g^{-1} = x \text{ for all } g \in G \iff \operatorname{Cl}(x) = \{x\} \iff |\operatorname{Cl}(x)| = 1$.
<2>6. The Class Equation: Partitioning $G$ into disjoint conjugacy classes gives: $$|G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)],$$ where $x_1, \dots, x_k$ are representatives of the distinct conjugacy classes of size strictly greater than 1. Proof: $G$ is the disjoint union of its single-element orbits (which form $Z(G)$) and its orbits of size $> 1$.

<1>2. Congruence modulo $p$: <2>1. For each representative $x_i$ with $|\operatorname{Cl}(x_i)| > 1$, $C_G(x_i) \lneq G$, so $[G : C_G(x_i)] > 1$.
Proof: By definition of the representatives $x_i$.
<2>2. By Lagrange's Theorem, $[G : C_G(x_i)]$ divides $|G| = p^n$.
Proof: Index of a subgroup divides the group order.
<2>3. The divisors of $p^n$ are $1, p, p^2, \dots, p^n$.
Since $[G : C_G(x_i)] > 1$, we must have $p \mid [G : C_G(x_i)]$.
Proof: Any divisor of $p^n$ strictly greater than 1 is a multiple of $p$.
<2>4. Therefore, $\sum_{i=1}^k [G : C_G(x_i)] \equiv 0 \pmod p$.
Proof: A sum of multiples of $p$ is a multiple of $p$.

<1>3. Deducing that $|Z(G)|$ is a multiple of $p$: <2>1. Reducing the Class Equation (<1>1.<2>6) modulo $p$: $$|G| \equiv |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)] \pmod p.$$ Proof: Taking modular equivalence of both sides.
<2>2. Since $|G| = p^n \equiv 0 \pmod p$ (as $n \ge 1$) and $\sum_{i=1}^k [G : C_G(x_i)] \equiv 0 \pmod p$ (<1>2.<2>4): $$0 \equiv |Z(G)| + 0 \pmod p \implies |Z(G)| \equiv 0 \pmod p.$$ Proof: Substitution into <2>1. <2>3. Thus $p$ divides $|Z(G)|$.
Proof: From <2>2.

<1>4. $Z(G)$ is non-trivial: <2>1. The identity element $e \in Z(G)$, so $|Z(G)| \ge 1$.
Proof: $e g = g e$ for all $g \in G$.
<2>2. Since $p \mid |Z(G)|$ and $|Z(G)| \ge 1$, we must have $|Z(G)| \ge p \ge 2$.
Proof: The smallest positive multiple of $p$ is $p$.
<2>3. Therefore, $Z(G) \neq \{e\}$.
Proof: $|Z(G)| \ge 2 > 1$.

<1>5. Conclusion: Every finite $p$-group has a non-trivial center.
Proof: By <1>4.
:::
