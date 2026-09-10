---
schema: qual/card@1
id: P-5EHW6
kind: problem
title: Groups of order 2012
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Classify all groups of order 2012 up to isomorphism.

> Hint: 503 is prime.
:::


::: solution
<1>1. Let \(G\) be a group of order
\[
|G|=2012=4\cdot 503.
\]
Its Sylow \(503\)-subgroup \(N\) is unique, hence normal, and \(N\cong C_{503}\).
::: {.proof}
The number \(n_{503}\) of Sylow \(503\)-subgroups satisfies
\[
n_{503}\mid 4,
\qquad
n_{503}\equiv 1\pmod{503}.
\]
Thus \(n_{503}=1\). Since \(503\) is prime, \(N\cong C_{503}\).
:::

<1>2. If \(P\) is any Sylow \(2\)-subgroup of \(G\), then
\[
G=N\rtimes P,
\qquad |P|=4.
\]
Hence \(P\cong C_4\) or \(C_2\times C_2\).
::: {.proof}
Because \(N\trianglelefteq G\), the product \(NP\) is a subgroup. Also
\[
N\cap P=1
\]
because the two groups have coprime orders. Therefore
\[
|NP|=|N||P|=503\cdot 4=|G|,
\]
so \(G=NP\), and this is the semidirect product \(N\rtimes P\). The two groups of order \(4\) are \(C_4\) and \(C_2\times C_2\).
:::

<1>3. The action of \(P\) on \(N\cong C_{503}\) has image of order at most \(2\).
::: {.proof}
Conjugation gives a homomorphism
\[
\varphi:P\longrightarrow \operatorname{Aut}(N).
\]
Since \(N\cong C_{503}\),
\[
\operatorname{Aut}(N)\cong (\mathbb Z/503\mathbb Z)^\times,
\]
a cyclic group of order \(502=2\cdot 251\). The image of the \(2\)-group \(P\) is therefore a \(2\)-subgroup of a cyclic group whose \(2\)-part has order \(2\). Hence
\[
|\operatorname{im}\varphi|\in\{1,2\}.
\]
The unique automorphism of \(N\) of order \(2\) is inversion \(x\mapsto x^{-1}\).
:::

<1>4. If \(P\cong C_4\), there are exactly two semidirect products up to isomorphism:
\[
C_{503}\times C_4
\quad\text{and}\quad
C_{503}\rtimes C_4,
\]
where a generator of \(C_4\) acts on \(C_{503}\) by inversion.
::: {.proof}
By <1>3, the action is either trivial or has image the unique subgroup of order \(2\) in \(\operatorname{Aut}(C_{503})\). Since \(C_4\) has a unique quotient of order \(2\), there is only one nontrivial homomorphism \(C_4\to C_2\) up to automorphism of \(C_4\). Thus there is one trivial-action and one nontrivial-action isomorphism type.
:::

<1>5. If \(P\cong C_2\times C_2\), there are exactly two semidirect products up to isomorphism:
\[
C_{503}\times C_2\times C_2
\quad\text{and}\quad
C_{503}\rtimes (C_2\times C_2),
\]
where one quotient \(C_2\) of \(C_2\times C_2\) acts by inversion and the kernel of that quotient acts trivially.
::: {.proof}
Again the action is either trivial or has image \(C_2\). Any nontrivial homomorphism
\[
C_2\times C_2\longrightarrow C_2
\]
has kernel one of the three subgroups of order \(2\). The automorphism group of \(C_2\times C_2\) acts transitively on these three subgroups, so all nontrivial actions yield isomorphic semidirect products. Hence there is exactly one nontrivial-action type.
:::

<1>6. Consequently there are exactly four groups of order \(2012\), up to isomorphism:
\[
\boxed{
C_{503}\times C_4,
\quad
C_{503}\times C_2\times C_2,
\quad
C_{503}\rtimes_{\mathrm{inv}} C_4,
\quad
C_{503}\rtimes_{\mathrm{inv}}(C_2\times C_2)
}.
\]
::: {.proof}
Steps <1>1--<1>5 show that every group of order \(2012\) is one of these four. They are pairwise nonisomorphic: the first two are abelian and have nonisomorphic Sylow \(2\)-subgroups; the last two are nonabelian and likewise have Sylow \(2\)-subgroups \(C_4\) and \(C_2\times C_2\), respectively.
:::
:::
