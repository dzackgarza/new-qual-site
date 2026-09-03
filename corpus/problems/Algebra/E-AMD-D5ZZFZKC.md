---
schema: qual/card@1
id: E-AMD-D5ZZFZKC
kind: problem
title: Every $p$-group has a nontrivial center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Class Equation
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that every $p\dash$group has a nontrivial center.
:::

::: {.solution}
**Goal:** Let $p$ be a prime number, and let $G$ be a finite $p$-group of order $|G| = p^n$ with $n \ge 1$.
Prove that the center $Z(G)$ is non-trivial, i.e., $|Z(G)| \ge p > 1$.

<1>1. Group action by conjugation and the Class Equation: <2>1. Let $G$ act on itself by conjugation: $(g, x) \mapsto g x g^{-1}$ for $g, x \in G$.
::: {.proof}
Standard group action axioms: $e x e^{-1} = x$ and $g (h x h^{-1}) g^{-1} = (g h) x (g h)^{-1}$.
:::
<2>2. The orbit of an element $x \in G$ under conjugation is its conjugacy class $\operatorname{Cl}(x) = \{g x g^{-1} \mid g \in G\}$.
::: {.proof}
Definition of conjugacy class.
:::
<2>3. The stabilizer of $x \in G$ is its centralizer $C_G(x) = \{g \in G \mid g x = x g\}$.
::: {.proof}
$g x g^{-1} = x \iff g x = x g$.
:::
<2>4. By the Orbit-Stabilizer Theorem, $|\operatorname{Cl}(x)| = [G : C_G(x)] = \frac{|G|}{|C_G(x)|}$.
::: {.proof}
Standard Orbit-Stabilizer Theorem for group actions on finite sets.
:::
<2>5. An element $x$ belongs to the center $Z(G)$ if and only if $|\operatorname{Cl}(x)| = 1$.
::: {.proof}
$x \in Z(G) \iff g x g^{-1} = x \text{ for all } g \in G \iff \operatorname{Cl}(x) = \{x\} \iff |\operatorname{Cl}(x)| = 1$.
:::
<2>6. The Class Equation: Partitioning $G$ into disjoint conjugacy classes gives: $$|G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)],$$ where $x_1, \dots, x_k$ are representatives of the distinct conjugacy classes of size strictly greater than 1.
::: {.proof}
$G$ is the disjoint union of its single-element orbits (which form $Z(G)$) and its orbits of size $> 1$.
:::

<1>2. Congruence modulo $p$: <2>1. For each representative $x_i$ with $|\operatorname{Cl}(x_i)| > 1$, $C_G(x_i) \lneq G$, so $[G : C_G(x_i)] > 1$.
::: {.proof}
By definition of the representatives $x_i$.
:::
<2>2. By Lagrange's Theorem, $[G : C_G(x_i)]$ divides $|G| = p^n$.
::: {.proof}
Index of a subgroup divides the group order.
:::
<2>3. The divisors of $p^n$ are $1, p, p^2, \dots, p^n$.
Since $[G : C_G(x_i)] > 1$, we must have $p \mid [G : C_G(x_i)]$.
::: {.proof}
Any divisor of $p^n$ strictly greater than 1 is a multiple of $p$.
:::
<2>4. Therefore, $\sum_{i=1}^k [G : C_G(x_i)] \equiv 0 \pmod p$.
::: {.proof}
A sum of multiples of $p$ is a multiple of $p$.
:::

<1>3. Deducing that $|Z(G)|$ is a multiple of $p$: <2>1. Reducing the Class Equation (<1>1.<2>6) modulo $p$: $$|G| \equiv |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)] \pmod p.$$ Proof: Taking modular equivalence of both sides.
<2>2. Since $|G| = p^n \equiv 0 \pmod p$ (as $n \ge 1$) and $\sum_{i=1}^k [G : C_G(x_i)] \equiv 0 \pmod p$ (<1>2.<2>4): $$0 \equiv |Z(G)| + 0 \pmod p \implies |Z(G)| \equiv 0 \pmod p.$$ Proof: Substitution into <2>1. <2>3. Thus $p$ divides $|Z(G)|$.
::: {.proof}
From <2>2.
:::

<1>4. $Z(G)$ is non-trivial: <2>1. The identity element $e \in Z(G)$, so $|Z(G)| \ge 1$.
::: {.proof}
$e g = g e$ for all $g \in G$.
:::
<2>2. Since $p \mid |Z(G)|$ and $|Z(G)| \ge 1$, we must have $|Z(G)| \ge p \ge 2$.
::: {.proof}
The smallest positive multiple of $p$ is $p$.
:::
<2>3. Therefore, $Z(G) \neq \{e\}$.
::: {.proof}
$|Z(G)| \ge 2 > 1$.
:::

<1>5. Conclusion: Every finite $p$-group has a non-trivial center.
::: {.proof}
By <1>4.
:::
:::
