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

::: problem
Let $p, q$ be distinct primes.

a. Let $\bar q \in \ZZ_p$ be the class of $q\mod p$ and let $k$ denote the order of $\bar q$ as an element of $\ZZ_p\units$.
Prove that no group of order $pq^k$ is simple.

b. Let $G$ be a group of order $pq$, and prove that $G$ is not simple.
:::

::: {.solution}
<1>1. Let $G$ have order $pq^k$, and let $n_p$ be the number of Sylow $p$-subgroups of $G$.
Then
\[
n_p\mid q^k
\qquad\text{and}\qquad
n_p\equiv 1\pmod p.
\]
::: {.proof}
This is Sylow's theorem.
:::

<1>2. One has $n_p=1$ or $n_p=q^k$.
::: {.proof}
Since $n_p\mid q^k$, write $n_p=q^j$ with $0\le j\le k$.
The congruence $n_p\equiv1\pmod p$ says $q^j\equiv1\pmod p$.
By definition, $k$ is the order of $q$ in $(\ZZ/p\ZZ)^\times$, so $k\mid j$.
Because $0\le j\le k$, one has $j=0$ or $j=k$.
:::

<1>3. If $n_p=1$, then $G$ is not simple.
::: {.proof}
The unique Sylow $p$-subgroup is normal and is a proper nontrivial subgroup of $G$.
:::

<1>4. Suppose $n_p=q^k$.
Then the union of the nonidentity elements of the Sylow $p$-subgroups has exactly
\[
q^k(p-1)
\]
elements.
::: {.proof}
Distinct subgroups of order $p$ intersect trivially: their intersection has order dividing $p$, and if it were nontrivial then the two order-$p$ subgroups would coincide.
Thus each of the $q^k$ Sylow $p$-subgroups contributes $p-1$ distinct nonidentity elements.
:::

<1>5. Exactly $q^k$ elements of $G$ remain after removing those nonidentity elements.
::: {.proof}
By <1>4, the number remaining is
\[
|G|-q^k(p-1)=pq^k-q^k(p-1)=q^k.
\]
The identity is among these remaining elements.
:::

<1>6. Any Sylow $q$-subgroup $Q$ has order $q^k$, so it is exactly the set of remaining elements from <1>5. Hence $Q$ is the unique Sylow $q$-subgroup of $G$.
::: {.proof}
No nonidentity element of $Q$ can lie in a Sylow $p$-subgroup, since its order is a power of $q$, not $p$.
Thus all $q^k$ elements of $Q$ lie among the $q^k$ elements counted in <1>5, so equality holds.
Every Sylow $q$-subgroup has the same property and therefore equals $Q$.
:::

<1>7. Consequently no group of order $pq^k$ is simple.
::: {.proof}
If $n_p=1$, use <1>3. If $n_p=q^k$, then <1>6 gives a unique Sylow $q$-subgroup, which is normal and proper.
:::

<1>8. Now let $|G|=pq$ with $p\ne q$.
Then $G$ is not simple.
::: {.proof}
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
