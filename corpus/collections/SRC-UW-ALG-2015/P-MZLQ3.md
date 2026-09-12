---
schema: qual/card@1
id: P-MZLQ3
kind: problem
title: At most one nonabelian group of order $pq$, and the pairs of distinct primes
  with none
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
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $p$, $q$ be two distinct primes.
Prove that there is at most one non-abelian group of order $pq$ and describe the pairs $(p,q)$ such that there is no non-abelian group of order $pq$.
:::


::: solution
<1>1. Without loss of generality, suppose \(p<q\). Then every group \(G\) of order \(pq\) has a unique Sylow \(q\)-subgroup \(Q\), hence
\[
Q\trianglelefteq G,
\qquad
Q\cong C_q.
\]
::: {.proof}
The number \(n_q\) of Sylow \(q\)-subgroups satisfies
\[
n_q\mid p,
\qquad
n_q\equiv1\pmod q.
\]
Since \(p<q\), the only possibility is \(n_q=1\). A group of prime order is cyclic, so \(Q\cong C_q\).
:::

<1>2. If \(P\) is a Sylow \(p\)-subgroup, then
\[
G\cong C_q\rtimes_\varphi C_p
\]
for some homomorphism
\[
\varphi:C_p\to\operatorname{Aut}(C_q).
\]
::: {.proof}
We have \(Q\cap P=1\) and
\[
|QP|=|Q||P|=pq=|G|,
\]
so \(G=QP\). Since \(Q\trianglelefteq G\), this is a semidirect product. Conjugation by \(P\) on \(Q\) gives the action \(\varphi\).
:::

<1>3. The semidirect product is nonabelian exactly when \(\varphi\) is nontrivial.
::: {.proof}
If \(\varphi\) is trivial, then \(P\) centralizes \(Q\), so
\[
G\cong C_q\times C_p\cong C_{pq},
\]
which is abelian. Conversely, a nontrivial action means some element of \(P\) acts nontrivially by conjugation on \(Q\), so \(G\) is nonabelian.
:::

<1>4. A nontrivial action exists if and only if
\[
p\mid(q-1).
\]
::: {.proof}
Since \(Q\cong C_q\),
\[
\operatorname{Aut}(Q)\cong(\mathbb Z/q\mathbb Z)^\times\cong C_{q-1}.
\]
A nontrivial homomorphism \(C_p\to C_{q-1}\) is injective because \(p\) is prime. Such an injection exists exactly when \(C_{q-1}\) has an element of order \(p\), equivalently when \(p\mid(q-1)\).
:::

<1>5. When \(p\mid(q-1)\), there is exactly one nonabelian group of order \(pq\) up to isomorphism.
::: {.proof}
The cyclic group \(\operatorname{Aut}(C_q)\cong C_{q-1}\) has a unique subgroup of order \(p\). Therefore all injective homomorphisms
\[
C_p\hookrightarrow\operatorname{Aut}(C_q)
\]
have the same image. Any two differ only by an automorphism of the source \(C_p\), and precomposing the action by an automorphism of the complement does not change the semidirect product up to isomorphism. Hence there is a unique nontrivial semidirect-product isomorphism type.
:::

<1>6. Therefore, for distinct primes \(p,q\), there is at most one nonabelian group of order \(pq\). Such a group exists precisely when the smaller prime divides one less than the larger prime.
::: {.proof}
If \(r=\min\{p,q\}\) and \(s=\max\{p,q\}\), apply <1>1--<1>5 with \(r<s\). Thus no nonabelian group exists exactly when
\[
\boxed{r\nmid(s-1)}.
\]
:::
:::
