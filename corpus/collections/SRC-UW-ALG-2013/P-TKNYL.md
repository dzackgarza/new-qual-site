---
schema: qual/card@1
id: P-TKNYL
kind: problem
title: A group of order $2013=3\cdot 11\cdot 61$ has a cyclic normal subgroup of index
  $3$, and $11$ divides $|Z(G)|$
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

::: {.problem}
Suppose that $G$ is a finite group of order 2013. Prove that $G$ has a normal subgroup $N$ of index 3 and that $N$ is a cyclic group.
Furthermore, prove that the center of $G$ has order divisible by 11. (You will need the factorization $2013=3\cdot11\cdot61$.)
:::


::: {.solution}
<1>1. The Sylow \(61\)-subgroup \(P_{61}\) of \(G\) is unique and hence normal.
::: {.proof}
By Sylow's theorem, the number \(n_{61}\) of Sylow \(61\)-subgroups satisfies
\[
n_{61}\mid 33,
\qquad
n_{61}\equiv1\pmod{61}.
\]
The divisors of \(33\) are \(1,3,11,33\), and only \(1\) is congruent to \(1\) modulo \(61\). Thus \(n_{61}=1\).
:::

<1>2. The Sylow \(11\)-subgroup \(P_{11}\) of \(G\) is unique and hence normal.
::: {.proof}
Again by Sylow's theorem,
\[
n_{11}\mid 3\cdot61=183,
\qquad
n_{11}\equiv1\pmod{11}.
\]
The divisors of \(183\) are \(1,3,61,183\), whose residues modulo \(11\) are \(1,3,6,7\), respectively. Hence \(n_{11}=1\).
:::

<1>3. The subgroup
\[
N=P_{11}P_{61}
\]
is normal of order \(11\cdot61=671\).
::: {.proof}
Both factors are normal by <1>1 and <1>2, so their product is a normal subgroup. Their intersection is trivial because their orders are coprime. Therefore
\[
|N|=|P_{11}||P_{61}|=11\cdot61=671.
\]
Since \(|G|=3\cdot671\), the index of \(N\) is \(3\).
:::

<1>4. The subgroup \(N\) is cyclic.
::: {.proof}
For normal subgroups \(A,B\trianglelefteq G\), every commutator \([a,b]\) lies in both \(A\) and \(B\). Hence
\[
[P_{11},P_{61}]\subseteq P_{11}\cap P_{61}=1.
\]
Thus the two subgroups commute elementwise. Since each has prime order, they are cyclic, and therefore
\[
N\cong C_{11}\times C_{61}\cong C_{671},
\]
because \(11\) and \(61\) are coprime.
:::

<1>5. The Sylow \(11\)-subgroup lies in the center of \(G\).
::: {.proof}
Since \(P_{11}\trianglelefteq G\), conjugation gives a homomorphism
\[
G\longrightarrow \operatorname{Aut}(P_{11}).
\]
Now \(P_{11}\cong C_{11}\), so
\[
|\operatorname{Aut}(P_{11})|=10.
\]
The order of the image divides both \(|G|=2013\) and \(10\). Since
\[
\gcd(2013,10)=1,
\]
the image is trivial. Thus every element of \(G\) centralizes \(P_{11}\), so
\[
P_{11}\subseteq Z(G).
\]
:::

<1>6. Consequently \(11\mid |Z(G)|\).
::: {.proof}
By <1>5, the center contains the subgroup \(P_{11}\) of order \(11\). Lagrange's theorem therefore gives \(11\mid |Z(G)|\).
:::
:::
