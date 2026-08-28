---
schema: qual/card@1
id: P-H7ERV
kind: problem
title: At most two $F$-conjugates of $L$ when $[K:F]=2$ and $L/K$ is finite Galois
classification:
  areas:
  - prelim
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $F$ be a field of characteristic zero and $\overline{F}$ be an algebraic closure of $F$.
Suppose that $K$ and $L$ are fields, with $F \subseteq K \subseteq L \subseteq \overline{F}$, such that $[K : F] = 2$ and $L/K$ is a finite Galois extension.
Prove that there are at most two fields $M \subseteq \overline{F}$ conjugate to $L$ over $F$ (remember that $M \subseteq \overline{F}$ is conjugate to $L$ over $F$ just in case there is an isomorphism of $L$ onto $M$ which is the identity on $F$).
:::

::: {.solution}
**Goal.** For $[K:F] = 2$ and $L/K$ finite Galois, show there are at most two fields conjugate to $L$ over $F$.

<1>1. The $F$-conjugates of $L$ are the images $\sigma(L)$ for $\sigma \in \operatorname{Aut}_F(\overline F)$.
Proof: an $F$-isomorphism $L \to M$ extends to an automorphism of $\overline F$ fixing $F$, so $M = \sigma(L)$ for some $\sigma$.

<1>2. $K/F$ is Galois (degree $2$ in characteristic $0$).
Proof: any degree-$2$ extension in characteristic $0$ is Galois (it is the splitting field of a quadratic).

<1>3. Hence $\sigma(K) = K$ for all $\sigma \in \operatorname{Aut}_F(\overline F)$.
Proof: $K/F$ is Galois, so it is stable under every $F$-automorphism of $\overline F$.

<1>4. $L/K$ is Galois, so $\sigma(L)$ depends only on $\sigma|_K$.
<2>1. For $\sigma \in \operatorname{Aut}_F(\overline F)$, $\sigma(L)$ is a $K$-conjugate of $L$ (since $\sigma(K) = K$).
Proof: $\sigma|_K$ is an automorphism of $K$, and $\sigma(L)$ is a $K$-conjugate of $L$.
<2>2. Since $L/K$ is Galois, $\sigma(L) = L$ for all $\sigma$ fixing $K$.
Proof: a Galois extension is stable under all $K$-automorphisms of $\overline F$.
<2>3. Hence $\sigma(L)$ depends only on $\sigma|_K$.
Proof: if $\sigma|_K = \tau|_K$, then $\sigma^{-1}\tau$ fixes $K$, so $\sigma^{-1}\tau(L) = L$, i.e. $\sigma(L) = \tau(L)$.

<1>5. There are at most two choices for $\sigma|_K$.
<2>1. $\operatorname{Aut}_F(K)$ has order $2$ (since $[K:F] = 2$ and $K/F$ is Galois).
Proof: $|\operatorname{Aut}_F(K)| = [K:F] = 2$.
<2>2. Hence $\sigma|_K$ is one of at most two automorphisms.
Proof: $\sigma|_K \in \operatorname{Aut}_F(K)$, which has two elements.

<1>6. Hence there are at most two $F$-conjugates of $L$.
Proof: by <1>4.3, $\sigma(L)$ is determined by $\sigma|_K$, and by <1>5.2 there are at most two such restrictions.

<1>7. Q.E.D.
Proof: <1>6 is the claim.
:::
