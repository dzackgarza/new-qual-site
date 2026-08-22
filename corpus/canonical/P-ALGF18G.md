---
schema: qual/card@1
id: P-ALGF18G
kind: problem
title: Galois group of irreducible of prime degree; Sylow $p$ normalizer
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Sylow Theory
relations: []
review: draft
solved: false
---

::: problem
Suppose $f(x) \in \mathbb{Q}[x]$ is an irreducible polynomial of degree $p$ where $p$ is prime. Let $E$ be the splitting field of $f(x)$ over $\mathbb{Q}$. Let $\alpha \in E$ be a zero of $f$, $G := \mathrm{Gal}(E/\mathbb{Q})$, and $H := \mathrm{Gal}(E/\mathbb{Q}[\alpha])$. Suppose $H$ is not trivial.

(a) Prove that $[G : H] = p$ and $\gcd(|H|, p) = 1$.

(b) Prove that $H$ is not a normal subgroup of $G$.

(c) Let $P$ be a Sylow $p$-subgroup of $G$. Prove that $N_G(P) \neq P$.
(Hint: assuming $N_G(P) = P$, deduce that $H = \{ g \in G \mid o(g) \neq p \}$ where $o(g)$ is the order of $g$.)
:::
