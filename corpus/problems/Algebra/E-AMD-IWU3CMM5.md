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
  - Simple Groups
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
Let $G$ be a group of order $pq$, where $p$ and $q$ are primes with $q<p$.

(a) Show that $G$ is never simple.

(b) Show that if $q\nmid p-1$, then $G$ is cyclic.

(c) Classify $G$ when $q\mid p-1$.
:::

::: {.hint}
Consider the cases when $q$ does or does not divide $p-1$.
:::

::: {.solution}
Let $|G|=pq$ with primes $q<p$.

::: pf

::: pf-step
The Sylow $p$-subgroup is normal.

::: pf-proof
Its number $n_p$ satisfies
$$
n_p\mid q,\qquad n_p\equiv1\pmod p.
$$
Since $q<p$, the possibility $n_p=q$ is impossible, hence $n_p=1$. Thus the Sylow $p$-subgroup $P\cong C_p$ is normal, so $G$ is not simple.
:::

:::

::: pf-step
Every such group is a semidirect product $C_p\rtimes C_q$.

::: pf-proof
Let $Q$ be a Sylow $q$-subgroup. Then $P\cap Q=1$ and $|PQ|=pq$, so $G=PQ$. Since $P\trianglelefteq G$,
$$
G\cong P\rtimes Q\cong C_p\rtimes_\theta C_q,
$$
where $\theta:C_q\to\Aut(C_p)\cong C_{p-1}$.
:::

:::

::: pf-step
If $q\nmid p-1$, then $G\cong C_{pq}$.

::: pf-proof
The image of $\theta$ has order dividing both $q$ and $p-1$. If $q\nmid p-1$, the image is trivial. Hence
$$
G\cong C_p\times C_q\cong C_{pq}.
$$
:::

:::

::: pf-step
If $q\mid p-1$, there are exactly two isomorphism types.

::: pf-proof
Because $C_{p-1}$ is cyclic, it has a unique subgroup of order $q$. Thus there is the trivial action, giving $C_{pq}$, and a nontrivial action with image that unique subgroup. Any two nontrivial homomorphisms $C_q\to C_{p-1}$ differ by an automorphism of $C_q$, hence yield isomorphic semidirect products. Therefore the two groups are
$$
C_{pq},\qquad C_p\rtimes C_q
$$
with the latter the unique nonabelian isomorphism type.
:::

:::

:::

:::

::: {.remark title="Variations"}
Part (a) is often posed in its stronger form: a group of order $pq$ with primes $q<p$ has a unique, hence normal, Sylow $p$-subgroup of order $p$.
The first step of the proof shows exactly this.

Part (b) is also posed with the conclusion that $G$ is abelian: a cyclic group is abelian, and conversely an abelian group of order $pq$ is $C_p\times C_q\cong C_{pq}$.
Part (c) is also posed as asking only for the possibilities, without justification: they are $C_{pq}$ and the nonabelian $C_p\rtimes C_q$.
:::

::: {.remark}
Part (b) also follows from Sylow counting without semidirect products.
The number $n_q$ of Sylow $q$-subgroups divides $p$ and is $\equiv1\pmod q$; if $q\nmid p-1$ then $n_q\neq p$, so $n_q=1$.
Then the Sylow $p$-subgroup $P$ and the Sylow $q$-subgroup $Q$ are both normal with $P\cap Q=1$ and $PQ=G$, so normal subgroups with trivial intersection commute elementwise and $G\cong P\times Q\cong C_{pq}$.
:::
