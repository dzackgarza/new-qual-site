---
schema: qual/card@1
id: P-XSRNS
kind: problem
title: Homology of two $2$-spheres glued along their equators
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Show that if $X = S^2 \disjoint_{\id} S^2$ is a pushout along the equators, then $H_n(X) = [\ZZ, 0, \ZZ^3, 0, \cdots]$.
:::

::: {.solution}
<1>1. $X$ is the union of two copies of $S^2$ glued along a common equator $S^1$.
Proof: the pushout of two $S^2$'s along their equators (identified by the identity map).

<1>2. Apply Mayer–Vietoris with $X = A \cup B$, where $A$ and $B$ are the two hemispheres... more precisely, $A$ and $B$ are the two $S^2$'s, with $A \cap B = S^1$ (the equator).
Proof: setup for Mayer–Vietoris.

<1>3. The Mayer–Vietoris sequence is
$$\cdots \to H_n(S^1) \to H_n(S^2) \oplus H_n(S^2) \to H_n(X) \to H_{n-1}(S^1) \to \cdots.$$
Proof: Mayer–Vietoris with $A = B = S^2$ and $A \cap B = S^1$.

<1>4. $H_0(X) = \ZZ$.
Proof: $X$ is connected.

<1>5. $H_1(X) = 0$.
<2>1. The relevant part is $H_1(S^1) \to H_1(S^2) \oplus H_1(S^2) \to H_1(X) \to H_0(S^1) \to H_0(S^2) \oplus H_0(S^2)$.
Proof: Mayer–Vietoris in low degrees.
<2>2. $H_1(S^2) = 0$, and the map $H_0(S^1) \to H_0(S^2) \oplus H_0(S^2)$ is injective (both inclusions induce the identity on $H_0$).
Proof: $H_0(S^1) = \ZZ$ and $H_0(S^2) = \ZZ$, with the map $\ZZ \to \ZZ \oplus \ZZ$ given by $1 \mapsto (1,1)$, which is injective.
<2>3. Hence $H_1(X) = 0$.
Proof: exactness: $H_1(X) \to H_0(S^1)$ is injective (kernel is image of $H_1(S^2) \oplus H_1(S^2) = 0$), and its image is the kernel of $H_0(S^1) \to H_0(S^2) \oplus H_0(S^2)$, which is $0$ (since that map is injective); so $H_1(X) = 0$.

<1>6. $H_2(X) = \ZZ^3$.
<2>1. The relevant part is $H_2(S^1) \to H_2(S^2) \oplus H_2(S^2) \to H_2(X) \to H_1(S^1) \to H_1(S^2) \oplus H_1(S^2)$.
Proof: Mayer–Vietoris.
<2>2. $H_2(S^1) = 0$ and $H_1(S^2) = 0$.
Proof: standard.
<2>3. Hence $0 \to \ZZ \oplus \ZZ \to H_2(X) \to \ZZ \to 0$ is exact.
Proof: $H_2(S^2) \oplus H_2(S^2) = \ZZ \oplus \ZZ$ and $H_1(S^1) = \ZZ$.
<2>4. Therefore $H_2(X) \cong \ZZ^3$.
Proof: the short exact sequence $0 \to \ZZ^2 \to H_2(X) \to \ZZ \to 0$ splits (the last term is free), so $H_2(X) \cong \ZZ^2 \oplus \ZZ = \ZZ^3$.

<1>7. $H_n(X) = 0$ for $n \ge 3$.
Proof: $H_n(S^1) = H_n(S^2) = 0$ for $n \ge 3$, so the Mayer–Vietoris sequence gives $H_n(X) = 0$.

<1>8. Q.E.D.
Proof: $H_0 = \ZZ$, $H_1 = 0$, $H_2 = \ZZ^3$, $H_n = 0$ for $n \ge 3$ (<1>4–<1>7).
:::
