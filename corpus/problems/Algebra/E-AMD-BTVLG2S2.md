---
schema: qual/card@1
id: E-AMD-BTVLG2S2
kind: problem
title: $\cardinality{HK}=\cardinality{H}\cardinality{K}/\cardinality{H\cap K}$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    counting identity with the constraint that no normalizer is used, no repair
    needed), and the existing prose against a fresh re-derivation: mu: H x K -> HK,
    (h,k) -> hk, is onto a set of |H||K|-element domain; over x = h0 k0 the fibre is
    exactly the pairs (h0 d, d^{-1} k0) with d in H cap K, which is a bijection with
    H cap K since the two constructions are mutually inverse; so |H||K| equals
    |HK||H cap K|. Correct, and it uses no normalizer, as the statement requires.
    The prose left the converse construction implicit (that h0 d in H and d^{-1}k0 in
    K for d in the intersection); the proof states it with the reason. No source
    solution is retained for this card, so no source comparison was made. What was not
    checked: any printed source.
---

::: {.exercise}
Let $H, K \leq G$ a finite group, and without using the normalizers of $H$ or $K$, show that $\abs{HK} = \abs{H} \abs{K}/\abs{H\intersect K}$.
:::

::: {.solution}
Let $H,K\leq G$ be subgroups of a finite group $G$ and $HK=\theset{hk:h\in H,\ k\in K}$; write $H\cap K$ for their intersection.

::: pf

::: {.pf-step #map}
$\mu\colon H\times K\to HK$, $\mu(h,k)=hk$, is a surjection from a set of $\abs{H}\abs{K}$ elements onto $HK$.

::: pf-proof
$\mu$ takes values in $HK$ by the definition of $HK$, and it is surjective by the same definition: every element of $HK$ is $hk$ for some $h\in H,k\in K$. Its domain is the Cartesian product, so $\abs{H\times K}=\abs{H}\abs{K}$.
:::

:::

::: {.pf-step #fibre}
For $x=h_0k_0\in HK$, the fibre $\mu^{-1}(x)$ is $\theset{(h_0d,\ d^{-1}k_0):d\in H\cap K}$, and it has exactly $\abs{H\cap K}$ elements.

::: pf-proof
If $hk=h_0k_0$, then $d\coloneqq h_0^{-1}h$ satisfies $h=h_0d$ and $k^{-1}=k_0^{-1}d$, that is $k=d^{-1}k_0$; moreover $d=h_0^{-1}h\in H$ and $d=k_0k^{-1}\in K$, so $d\in H\cap K$. Conversely, if $d\in H\cap K$ then $h_0d\in H$ and $d^{-1}k_0\in K$ — both $d$ and $k_0$ lie in $K$ — and $(h_0d)(d^{-1}k_0)=h_0k_0$, so the pair lies in the fibre. The two constructions are mutually inverse, so $d\mapsto(h_0d,d^{-1}k_0)$ is a bijection from $H\cap K$ onto the fibre; hence the fibre has $\abs{H\cap K}$ elements.
:::

:::

::: {.pf-step}
$\abs{HK}=\abs{H}\abs{K}/\abs{H\cap K}$.

::: pf-proof
The fibres of the surjection $\mu$ of step [](#map){.pf-ref} partition $H\times K$, and each has $\abs{H\cap K}$ elements by step [](#fibre){.pf-ref}; the number of fibres is $\abs{HK}$. Hence $\abs{H}\abs{K}=\abs{H\times K}=\abs{HK}\cdot\abs{H\cap K}$, and dividing by the nonzero integer $\abs{H\cap K}$ gives the formula.
:::

:::

:::
:::
