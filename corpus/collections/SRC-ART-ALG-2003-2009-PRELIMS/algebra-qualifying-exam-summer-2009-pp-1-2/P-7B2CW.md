---
schema: qual/card@1
id: P-7B2CW
kind: problem
title: Groups of order $pq$ with $p<q$ primes are not simple, abelian if $p\nmid q-1$,
  and the possibilities when $p\mid q-1$
classification:
  areas:
  - prelim
  topics:
  - Groups
  - Simple Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $|G|=pq$ where $p$ and $q$ are prime, $p<q$.
a. Show that $G$ is not a simple group.
b. If $p$ does not divide $q-1$, show that $G$ is abelian.
c. If $p$ divides $q-1$, what are the possibilities for $G$?
(You need not give detailed justification for your answer to part (c).)
:::

::: {.solution}
<1>1. The Sylow \(q\)-subgroup of \(G\) is unique and therefore normal.
::: {.proof}
Let \(n_q\) be the number of Sylow \(q\)-subgroups. Sylow's theorems give
\[
n_q\mid p,
\qquad
n_q\equiv1\pmod q.
\]
Thus \(n_q\in\{1,p\}\). Since \(p<q\), the value \(p\) cannot be congruent to \(1\pmod q\). Hence \(n_q=1\).
:::

<1>2. Consequently, \(G\) is not simple.
::: {.proof}
Its unique Sylow \(q\)-subgroup has order \(q\), so it is a nontrivial proper normal subgroup of \(G\).
:::

<1>3. If \(p\nmid(q-1)\), then the Sylow \(p\)-subgroup is also unique and normal.
::: {.proof}
Let \(n_p\) be the number of Sylow \(p\)-subgroups. Sylow's theorems give
\[
n_p\mid q,
\qquad
n_p\equiv1\pmod p.
\]
Hence \(n_p\in\{1,q\}\). If \(n_p=q\), then \(q\equiv1\pmod p\), i.e. \(p\mid(q-1)\), contrary to hypothesis. Therefore \(n_p=1\).
:::

<1>4. Under the hypothesis of <1>3, one has
\[
G\cong C_p\times C_q\cong C_{pq},
\]
so \(G\) is abelian.
::: {.proof}
Let \(P\) and \(Q\) be the unique Sylow \(p\)- and \(q\)-subgroups. They are normal, \(P\cap Q=1\), and \(|PQ|=pq=|G|\), so \(G=PQ\). For \(x\in P\) and \(y\in Q\), the commutator \([x,y]\) lies in both \(P\) and \(Q\), because both subgroups are normal. Hence \([x,y]=1\), so \(P\) and \(Q\) commute and \(G\cong P\times Q\). Groups of prime order are cyclic, and the direct product of cyclic groups of coprime orders \(p\) and \(q\) is cyclic of order \(pq\).
:::

<1>5. If \(p\mid(q-1)\), then up to isomorphism the possibilities are
\[
C_{pq}
\qquad\text{and}\qquad
C_q\rtimes C_p
\]
with nontrivial action of \(C_p\) on \(C_q\).
::: {.proof}
The cyclic group \(C_{pq}\) always occurs. Since
\[
\operatorname{Aut}(C_q)\cong C_{q-1},
\]
the divisibility \(p\mid(q-1)\) gives a subgroup of order \(p\) in \(\operatorname{Aut}(C_q)\), hence a nontrivial homomorphism \(C_p\to\operatorname{Aut}(C_q)\) and therefore a nonabelian semidirect product \(C_q\rtimes C_p\). Because \(\operatorname{Aut}(C_q)\) is cyclic, it has a unique subgroup of order \(p\); all nontrivial actions have the same image and yield isomorphic semidirect products. Thus these are exactly the two isomorphism types.
:::
:::
