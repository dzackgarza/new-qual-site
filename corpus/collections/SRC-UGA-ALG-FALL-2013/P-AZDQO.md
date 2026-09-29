---
schema: qual/card@1
id: P-AZDQO
kind: problem
title: No simple group of order $pq^k$ with $k$ the order of $q$ in $(\ZZ/p\ZZ)^\times$,
  nor of order $pq$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $p, q$ be distinct primes.

a. Let $\bar q \in \ZZ_p$ be the class of $q\mod p$ and let $k$ denote the order of $\bar q$ as an element of $\unitsof{\ZZ_p}$.
   Prove that no group of order $pq^k$ is simple.

b. Let $G$ be a group of order $pq$, and prove that $G$ is not simple.
:::

::: {.solution}

::: pf

::: pf-step
Let $G$ have order $pq^k$, and let $n_p$ be the number of Sylow $p$-subgroups of $G$.
Then
\[
n_p\mid q^k
\qquad\text{and}\qquad
n_p\equiv 1\pmod p.
\]

::: pf-proof
This is Sylow's theorem.
:::

:::

::: pf-step
One has $n_p=1$ or $n_p=q^k$.

::: pf-proof
Since $n_p\mid q^k$, write $n_p=q^j$ with $0\le j\le k$.
The congruence $n_p\equiv1\pmod p$ says $q^j\equiv1\pmod p$.
By definition, $k$ is the order of $q$ in $(\ZZ/p\ZZ)^\times$, so $k\mid j$.
Because $0\le j\le k$, one has $j=0$ or $j=k$.
:::

:::

::: {.pf-step #np-equals-one-not-simple}
If $n_p=1$, then $G$ is not simple.

::: pf-proof
The unique Sylow $p$-subgroup is normal and is a proper nontrivial subgroup of $G$.
:::

:::

::: {.pf-step #nonidentity-elements-count}
Suppose $n_p=q^k$.
Then the union of the nonidentity elements of the Sylow $p$-subgroups has exactly
\[
q^k(p-1)
\]
elements.

::: pf-proof
Distinct subgroups of order $p$ intersect trivially: their intersection has order dividing $p$, and if it were nontrivial then the two order-$p$ subgroups would coincide.
Thus each of the $q^k$ Sylow $p$-subgroups contributes $p-1$ distinct nonidentity elements.
:::

:::

::: {.pf-step #remaining-elements-count}
Exactly $q^k$ elements of $G$ remain after removing those nonidentity elements.

::: pf-proof
By step [](#nonidentity-elements-count){.pf-ref}, the number remaining is
\[
|G|-q^k(p-1)=pq^k-q^k(p-1)=q^k.
\]
The identity is among these remaining elements.
:::

:::

::: {.pf-step #unique-sylow-q}
Any Sylow $q$-subgroup $Q$ has order $q^k$, so it is exactly the set of remaining elements from step [](#remaining-elements-count){.pf-ref}. Hence $Q$ is the unique Sylow $q$-subgroup of $G$.

::: pf-proof
No nonidentity element of $Q$ can lie in a Sylow $p$-subgroup, since its order is a power of $q$, not $p$.
Thus all $q^k$ elements of $Q$ lie among the $q^k$ elements counted in step [](#remaining-elements-count){.pf-ref}, so equality holds.
Every Sylow $q$-subgroup has the same property and therefore equals $Q$.
:::

:::

::: pf-step
Consequently no group of order $pq^k$ is simple.

::: pf-proof
If $n_p=1$, use step [](#np-equals-one-not-simple){.pf-ref}. If $n_p=q^k$, then step [](#unique-sylow-q){.pf-ref} gives a unique Sylow $q$-subgroup, which is normal and proper.
:::

:::

::: pf-step
Now let $|G|=pq$ with $p\ne q$.
Then $G$ is not simple.

::: pf-proof
Assume without loss of generality that $p<q$.
If $n_q$ denotes the number of Sylow $q$-subgroups, then Sylow's theorem gives
\[
n_q\mid p
\qquad\text{and}\qquad
n_q\equiv1\pmod q.
\]
Hence $n_q$ is either $1$ or $p$.
Since $1<p<q$, the possibility $n_q=p$ cannot satisfy $n_q\equiv1\pmod q$.
Thus $n_q=1$, so the Sylow $q$-subgroup is normal and $G$ is not simple.
:::

:::

:::

:::
