---
schema: qual/card@1
id: P-OKCT6
kind: problem
title: Classification of groups of order $pq$
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
  date: 2026-09-11
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-11
---

::: {.problem}
How many groups are there up to isomorphism of order $pq$ where $p<q$ are prime integers?
:::

::: {.solution}
Let $G$ be a group of order $pq$, where $p<q$ are prime.

<1>1. The Sylow $q$-subgroup of $G$ is unique and therefore normal.
::: {.proof}
Let $n_q$ be the number of Sylow $q$-subgroups. Sylow's theorems give
\[
n_q\equiv1\pmod q
\qquad\text{and}\qquad
n_q\mid p.
\]
Since $p<q$, the only divisor of $p$ congruent to $1$ modulo $q$ is $1$. Hence $n_q=1$.
Thus the Sylow $q$-subgroup $Q$ is normal, and because $|Q|=q$, we have $Q\cong C_q$.
:::

<1>2. If $P$ is a Sylow $p$-subgroup, then
\[
G\cong C_q\rtimes_\varphi C_p
\]
for some homomorphism
\[
\varphi:C_p\longrightarrow \operatorname{Aut}(C_q).
\]
::: {.proof}
A Sylow $p$-subgroup $P$ has order $p$, so $P\cong C_p$. Since $Q\trianglelefteq G$, $Q\cap P=1$, and
\[
|QP|=\frac{|Q||P|}{|Q\cap P|}=pq=|G|,
\]
we have $G=QP$. Thus $G$ is the semidirect product of $Q$ by $P$, with action given by conjugation.
:::

<1>3. We have
\[
\operatorname{Aut}(C_q)\cong C_{q-1}.
\]
Hence a nontrivial action $C_p\to\operatorname{Aut}(C_q)$ exists if and only if
\[
p\mid(q-1).
\]
::: {.proof}
If $C_q=\langle x\rangle$, every automorphism sends $x$ to $x^a$ with $a\in(\mathbb Z/q\mathbb Z)^\times$. Thus
\[
\operatorname{Aut}(C_q)\cong(\mathbb Z/q\mathbb Z)^\times,
\]
which is cyclic of order $q-1$.
A nontrivial homomorphism from $C_p$ into this cyclic group must have image of order $p$, and such a subgroup exists exactly when $p\mid(q-1)$.
:::

<1>4. If $p\nmid(q-1)$, then every group of order $pq$ is cyclic, so there is exactly one isomorphism class.
::: {.proof}
By <1>3, the action in <1>2 must be trivial. Hence
\[
G\cong C_q\times C_p.
\]
Since $p$ and $q$ are coprime,
\[
C_q\times C_p\cong C_{pq}.
\]
:::

<1>5. If $p\mid(q-1)$, then there are exactly two isomorphism classes: the cyclic group $C_{pq}$ and one nonabelian semidirect product $C_q\rtimes C_p$.
::: {.proof}
The trivial action gives $C_{pq}$.

Because $\operatorname{Aut}(C_q)\cong C_{q-1}$ is cyclic, it has a unique subgroup $H$ of order $p$. Every nontrivial homomorphism
\[
\varphi:C_p\to\operatorname{Aut}(C_q)
\]
is injective and has image $H$.
Any two such homomorphisms differ only by an automorphism of the source $C_p$: if $u,v$ are generators of $H$, then $v=u^a$ for some $a\in(\mathbb Z/p\mathbb Z)^\times$, and replacing a generator of $C_p$ by its $a$th power changes one action into the other. The corresponding semidirect products are therefore isomorphic.

This nontrivial semidirect product is nonabelian because the action is nontrivial, so it is not isomorphic to the cyclic group.
:::

<1>6. Therefore the number of groups of order $pq$ up to isomorphism is
\[
\boxed{
\begin{cases}
1,& p\nmid(q-1),\\
2,& p\mid(q-1).
\end{cases}}
\]
:::
