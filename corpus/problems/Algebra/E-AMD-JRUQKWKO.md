---
schema: qual/card@1
id: E-AMD-JRUQKWKO
kind: problem
title: $H$ characteristic in $K\trianglelefteq G$ implies $H\trianglelefteq G$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Automorphisms
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement
    (a standard lemma, no repair needed), the existing prose solution against a
    fresh re-derivation (it was correct and is subsumed by the structured
    proof), and the absence of a retained source solution for this card — its
    only appearance is SRC-UNSORTED-ALGEBRA, a compilation with no provenance
    href — so no source comparison was made. What was not checked: any printed
    source, since none exists in this repository for this statement.
---

::: {.exercise}
Show that if $H \leq K \trianglelefteq G$ and $H$ is characteristic in $K$, then $H \trianglelefteq G$.
:::

::: {.solution}
Write $c_g$ for conjugation by $g\in G$, so that $c_g(x)=gxg^{-1}$; for a subgroup $S\leq K$ we write $c_g(S)=\{gxg^{-1}:x\in S\}$.

::: pf

::: {.pf-step #h-le-g}
$H\leq G$.

::: pf-proof
By hypothesis $H\leq K$, and $K\trianglelefteq G$ entails $K\leq G$. Transitivity of the subgroup relation gives $H\leq G$.
:::

:::

::: {.pf-step #conj-aut}
For every $g\in G$ the map $c_g\colon K\to K$ is a group automorphism of $K$.

::: pf-proof
It takes values in $K$: for $k\in K$ we have $gkg^{-1}\in K$, because $K$ is normal in $G$. It is a homomorphism, since $c_g(k_1k_2)=gk_1k_2g^{-1}=(gk_1g^{-1})(gk_2g^{-1})=c_g(k_1)c_g(k_2)$, and it carries the identity to the identity. For the inverse, $g^{-1}$ also lies in $G$, so by the same argument $c_{g^{-1}}$ is a map $K\to K$, and $c_{g^{-1}}(c_g(k))=g^{-1}(gkg^{-1})g=k$ and $c_g(c_{g^{-1}}(k))=g(g^{-1}kg)g^{-1}=k$ for every $k\in K$. Hence $c_g$ is a bijection with inverse $c_{g^{-1}}$.
:::

:::

::: {.pf-step #char}
$c_g(H)=H$ for every $g\in G$.

::: pf-proof
By step [](#conj-aut){.pf-ref}, $c_g$ is an automorphism of $K$, and $H$ is characteristic in $K$, so every automorphism of $K$ carries $H$ onto $H$. Hence $c_g(H)=H$.
:::

:::

::: {.pf-step #conj-set}
$gHg^{-1}=H$ for every $g\in G$.

::: pf-proof
For $g\in G$ the set $gHg^{-1}=\{ghg^{-1}:h\in H\}$ is by definition $c_g(H)$, which equals $H$ by step [](#char){.pf-ref}.
:::

:::

::: {.pf-step}
$H\trianglelefteq G$.

::: pf-proof
By step [](#h-le-g){.pf-ref}, $H$ is a subgroup of $G$, and by step [](#conj-set){.pf-ref}, $gHg^{-1}=H$ for every $g\in G$. These two facts are the definition of $H$ being a normal subgroup of $G$.
:::

:::

:::
:::
