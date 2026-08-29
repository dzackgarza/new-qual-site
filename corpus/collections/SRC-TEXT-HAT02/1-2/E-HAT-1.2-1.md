---
schema: qual/card@1
id: E-HAT-1.2-1
kind: exercise
title: Free product of nontrivial groups has trivial center and only conjugates of finite-order elements have finite order
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Groups
  - Free Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Show that the free product $G * H$ of nontrivial groups $G$ and $H$ has trivial center, and that the only elements of $G * H$ of finite order are the conjugates of finite-order elements of $G$ and $H$.

::: {.solution}
<1>1. Every element of $G * H$ has a unique reduced word form $g_1 h_1 g_2 h_2 \cdots$ with $g_i \in G \setminus \{1\}$, $h_i \in H \setminus \{1\}$ (alternating, no adjacent factors from the same group).
Proof: normal form theorem for free products.

<1>2. Let $w \in Z(G * H)$ be a nontrivial central element, written in reduced form.
Proof: suppose the center is nontrivial.

<1>3. If $w$ has length $\ge 2$, then conjugating by a nontrivial element of the group of the first factor changes the word, contradicting centrality.
Proof: e.g. if $w$ starts with $g_1 \in G$, then for $h \in H \setminus \{1\}$, $h w h^{-1}$ has a different reduced form than $w$ (the first factor changes), so $h w h^{-1} \ne w$.

<1>4. If $w$ has length $1$, say $w = g_1 \in G$, then for $h \in H \setminus \{1\}$, $h g_1 h^{-1} \ne g_1$.
Proof: $h g_1 h^{-1}$ is a reduced word of length $3$, not equal to the length-$1$ word $g_1$.

<1>5. Hence no nontrivial element is central, so $Z(G * H) = 1$.
Proof: <1>2–<1>4.

<1>6. Let $w \in G * H$ have finite order, with reduced form $w = a_1 a_2 \cdots a_n$.
Proof: take a finite-order element.

<1>7. If $n \ge 2$, then $w$ is cyclically reduced (after conjugation) and $w^k$ has reduced length $kn$ for all $k \ge 1$, so $w^k \ne 1$.
Proof: the reduced form of $w^k$ is the concatenation of $k$ copies of the cyclically reduced form, of length $kn > 0$.

<1>8. Hence $n = 1$, so $w$ is conjugate to an element of $G$ or of $H$.
Proof: <1>7 (a finite-order element must have length $1$, i.e. lie in a single factor, up to conjugation).

<1>9. Therefore the finite-order elements of $G * H$ are exactly the conjugates of finite-order elements of $G$ and $H$.
Proof: <1>6–<1>8.

<1>10. Q.E.D.
Proof: <1>5 and <1>9.
:::
