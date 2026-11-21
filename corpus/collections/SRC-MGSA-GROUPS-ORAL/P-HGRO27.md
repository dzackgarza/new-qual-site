---
schema: qual/card@1
id: P-HGRO27
kind: problem
title: A finite group whose elements have prime-power order
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, whose answer
    (yes, the order is a power of p) is correct. Added: explicit statement of the hypothesis as
    a step, including that the identity has order p^0 = 1; Cauchy's theorem as the named input,
    with a note that it does not require the Sylow theorems; and the arithmetic step that a
    prime q of the form p^k forces k = 1 and q = p, which the prose compressed into "no
    positive power of p equals the distinct prime q". Not claimed: a retained solution set; the
    provenance names the oral question list.
---

::: {.problem}
Suppose every element of a finite group $G$ has order equal to a power of one fixed prime $p$.
Must $\cardinality{G}$ be a power of $p$?
Justify your answer.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the groups oral question list, which carries no solutions. The answer is **yes**, and the numbered steps below are the card's previous prose with Cauchy's theorem and the arithmetic of prime powers stated explicitly.

Throughout $G$ is a finite group, $p$ is a fixed prime, and every element $g\in G$ has order $p^{k}$ for some integer $k\ge0$.

::: pf

::: {.pf-step #orders}
Every element of $G$ has order a power of $p$, and $1$ has order $p^0=1$.

::: pf-proof
This is the hypothesis; the identity element is included, with $k=0$.

:::

:::

::: {.pf-step #cauchy}
If a prime $q$ divides $\cardinality G$, then $G$ has an element of order $q$.

::: pf-proof
Cauchy's theorem: for a prime $q$ dividing the order of a finite group, there is an element of order exactly $q$. (This does not need the Sylow theorems; a proof by induction on the order, splitting on whether a proper subgroup has index divisible by $q$, is standard.)

:::

:::

::: {.pf-step #contradiction}
No prime $q\ne p$ divides $\cardinality G$.

::: pf-proof
Suppose $q\ne p$ is a prime divisor. By step [](#cauchy){.pf-ref} there is $g\in G$ of order $q$. By step [](#orders){.pf-ref} that order is $p^k$ for some $k\ge0$, so $q=p^k$. Since $q$ is prime, $k=1$ and $q=p$, contradicting $q\ne p$.

:::

:::

::: {.pf-step #conclusion}
$\cardinality G=p^n$ for some $n\ge0$.

::: pf-proof
The prime factorisation of $\cardinality G$ involves no prime other than $p$ by step [](#contradiction){.pf-ref}, so $\cardinality G=p^n$ with $n=v_p(\cardinality G)\ge0$ — the case $n=0$ being the trivial group, whose single element has order $1=p^0$.

:::

:::

:::
:::
