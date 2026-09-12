---
schema: qual/card@1
id: E-AMD-IWU3CMM5
kind: problem
title: Groups of order $pq$ with $q<p$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Re-derived the Sylow and semidirect-product classification concisely.
---

::: {.exercise}
Analyze groups of order $pq$ with $q<p$ prime.

- Show that $G$ is never simple.
- Show that if $q\nmid p-1$, then $G$ is cyclic.
- Classify $G$ when $q\mid p-1$.
:::

::: {.solution}
Let $|G|=pq$ with primes $q<p$.

<1>1. The Sylow $p$-subgroup is normal.
::: {.proof}
Its number $n_p$ satisfies
\[
n_p\mid q,\qquad n_p\equiv1\pmod p.
\]
Since $q<p$, the possibility $n_p=q$ is impossible, hence $n_p=1$. Thus the Sylow $p$-subgroup $P\cong C_p$ is normal, so $G$ is not simple.
:::

<1>2. Every such group is a semidirect product $C_p\rtimes C_q$.
::: {.proof}
Let $Q$ be a Sylow $q$-subgroup. Then $P\cap Q=1$ and $|PQ|=pq$, so $G=PQ$. Since $P\trianglelefteq G$,
\[
G\cong P\rtimes Q\cong C_p\rtimes_\theta C_q,
\]
where $\theta:C_q\to\operatorname{Aut}(C_p)\cong C_{p-1}$.
:::

<1>3. If $q\nmid p-1$, then $G\cong C_{pq}$.
::: {.proof}
The image of $\theta$ has order dividing both $q$ and $p-1$. If $q\nmid p-1$, the image is trivial. Hence
\[
G\cong C_p\times C_q\cong C_{pq}.
\]
:::

<1>4. If $q\mid p-1$, there are exactly two isomorphism types.
::: {.proof}
Because $C_{p-1}$ is cyclic, it has a unique subgroup of order $q$. Thus there is the trivial action, giving $C_{pq}$, and a nontrivial action with image that unique subgroup. Any two nontrivial homomorphisms $C_q\to C_{p-1}$ differ by an automorphism of $C_q$, hence yield isomorphic semidirect products. Therefore the two groups are
\[
C_{pq},\qquad C_p\rtimes C_q
\]
with the latter the unique nonabelian isomorphism type.
:::
:::
