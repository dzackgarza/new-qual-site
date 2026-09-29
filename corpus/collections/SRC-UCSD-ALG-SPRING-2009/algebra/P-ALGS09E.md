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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 5 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Verified both directions using extension of F-embeddings in a finite Galois extension and the fixed-field identity E^(gHg^-1)=g(E^H).
---

::: {.problem}
Let $E/F$ be a Galois extension and let $K$, $L$ be intermediate fields.
Show that $K$ and $L$ are $F$-isomorphic (i.e.\ there exists an isomorphism from $K$ to $L$ which is the identity on $F$) if and only if the subgroups of $G = \operatorname{Gal}(E/F)$ corresponding to $K$ and $L$ are conjugate in $G$.
:::

::: {.solution}
**Goal.** Show $K \cong_F L$ iff the corresponding subgroups $H = \Gal(E/K)$ and $H' = \Gal(E/L)$ are conjugate in $G$.

::: pf

::: {.pf-step #s1}
($\Rightarrow$) Suppose $\sigma: K \to L$ is an $F$-isomorphism.

::: pf-proof

::: pf-step
Extend $\sigma$ to an automorphism $\tilde\sigma \in G = \Gal(E/F)$.

::: pf-proof
$E/F$ is Galois, so any $F$-embedding $K \to E$ extends to an automorphism of $E$ (extend $\sigma$ to an $F$-embedding $K \to E$ and use normality).
:::

:::

::: pf-step
$\tilde\sigma(K) = L$.

::: pf-proof
$\tilde\sigma$ extends $\sigma$, and $\sigma(K) = L$.
:::

:::

::: {.pf-step #s1-3}
Hence $\Gal(E/L) = \Gal(E/\tilde\sigma(K)) = \tilde\sigma \Gal(E/K) \tilde\sigma^{-1}$.

::: pf-proof
the Galois group of $\tilde\sigma(K)$ is the conjugate of the Galois group of $K$ by $\tilde\sigma$.
:::

:::

::: pf-step
Hence $H' = \tilde\sigma H \tilde\sigma^{-1}$, so $H$ and $H'$ are conjugate.

::: pf-proof
step [](#s1-3){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s2}
($\Leftarrow$) Suppose $H' = g H g^{-1}$ for some $g \in G$.

::: pf-proof

::: pf-step
$L = E^{H'} = E^{gHg^{-1}} = g(E^H) = g(K)$.

::: pf-proof
the fixed field of $gHg^{-1}$ is $g$ applied to the fixed field of $H$.
:::

:::

::: pf-step
Hence $g|_K: K \to L$ is an $F$-isomorphism.

::: pf-proof
$g$ fixes $F$ (it is in $\Gal(E/F)$) and maps $K$ onto $L$.
:::

:::

:::

:::

::: pf-qed
step [](#s1){.pf-ref} and step [](#s2){.pf-ref} give both directions.
:::

:::
:::
