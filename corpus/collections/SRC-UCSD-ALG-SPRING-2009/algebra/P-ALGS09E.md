---
schema: qual/card@1
id: P-ALGS09E
kind: problem
title: "F-isomorphic intermediate fields correspond to conjugate subgroups of the Galois group"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $E/F$ be a Galois extension and let $K$, $L$ be intermediate fields.
Show that $K$ and $L$ are $F$-isomorphic (i.e.\ there exists an isomorphism from $K$ to $L$ which is the identity on $F$) if and only if the subgroups of $G = \operatorname{Gal}(E/F)$ corresponding to $K$ and $L$ are conjugate in $G$.
:::

::: {.solution}
**Goal.** Show $K \cong_F L$ iff the corresponding subgroups $H = \Gal(E/K)$ and $H' = \Gal(E/L)$ are conjugate in $G$.

<1>1. ($\Rightarrow$) Suppose $\sigma: K \to L$ is an $F$-isomorphism.
<2>1. Extend $\sigma$ to an automorphism $\tilde\sigma \in G = \Gal(E/F)$.
Proof: $E/F$ is Galois, so any $F$-embedding $K \to E$ extends to an automorphism of $E$ (extend $\sigma$ to an $F$-embedding $K \to E$ and use normality).
<2>2. $\tilde\sigma(K) = L$.
Proof: $\tilde\sigma$ extends $\sigma$, and $\sigma(K) = L$.
<2>3. Hence $\Gal(E/L) = \Gal(E/\tilde\sigma(K)) = \tilde\sigma \Gal(E/K) \tilde\sigma^{-1}$.
Proof: the Galois group of $\tilde\sigma(K)$ is the conjugate of the Galois group of $K$ by $\tilde\sigma$.
<2>4. Hence $H' = \tilde\sigma H \tilde\sigma^{-1}$, so $H$ and $H'$ are conjugate.
Proof: <1>2.3.

<1>2. ($\Leftarrow$) Suppose $H' = g H g^{-1}$ for some $g \in G$.
<2>1. $L = E^{H'} = E^{gHg^{-1}} = g(E^H) = g(K)$.
Proof: the fixed field of $gHg^{-1}$ is $g$ applied to the fixed field of $H$.
<2>2. Hence $g|_K: K \to L$ is an $F$-isomorphism.
Proof: $g$ fixes $F$ (it is in $\Gal(E/F)$) and maps $K$ onto $L$.

<1>3. Q.E.D.
Proof: <1>1 and <1>2 give both directions.
:::
