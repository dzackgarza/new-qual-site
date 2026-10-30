---
schema: qual/card@1
id: P-ARTALG-AL04-2
kind: problem
title: Every group of size 15 is cyclic
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---
::: {.problem}
Prove that any group of size 15 is cyclic.
:::

::: {.solution}

::: pf

::: pf-step

The Sylow $3$-subgroup and Sylow $5$-subgroup of $G$ are both unique and normal.

::: pf-proof

Since
$$
\cardinality{G}=15=3\cdot5,
$$
Sylow's theorems give
$$
n_3\mid5,
\qquad
n_3\equiv1\pmod3.
$$
The only divisor of $5$ congruent to $1$ modulo $3$ is $1$, so
$$
n_3=1.
$$
Likewise,
$$
n_5\mid3,
\qquad
n_5\equiv1\pmod5,
$$
so
$$
n_5=1.
$$
Thus there are unique Sylow subgroups
$$
P\cong C_3,
\qquad
Q\cong C_5,
$$
and both are normal in $G$.

:::

:::

::: {.pf-step #s2}

The subgroups $P$ and $Q$ intersect trivially and commute elementwise.

::: pf-proof

Because $\cardinality{P}=3$ and $\cardinality{Q}=5$,
$$
\cardinality{P\cap Q}\mid\gcd(3,5)=1,
$$
so
$$
P\cap Q=\{e\}.
$$

For $p\in P$ and $q\in Q$, the commutator
$$
[p,q]=pqp^{-1}q^{-1}
$$
lies in $P$ because $P\trianglelefteq G$, and it lies in $Q$ because $Q\trianglelefteq G$. Hence
$$
[p,q]\in P\cap Q=\{e\}.
$$
Therefore
$$
pq=qp
$$
for all $p\in P$ and $q\in Q$.

:::

:::

::: {.pf-step #s3}

The multiplication map
$$
\varphi:P\times Q\longrightarrow G,
\qquad
(p,q)\longmapsto pq
$$
is an isomorphism.

::: pf-proof

By step [](#s2){.pf-ref}, $P$ and $Q$ commute elementwise, so $\varphi$ is a homomorphism. If
$$
\varphi(p,q)=e,
$$
then
$$
p=q^{-1}\in P\cap Q=\{e\},
$$
so $p=q=e$. Thus $\varphi$ is injective.

Finally,
$$
\cardinality{P\times Q}=3\cdot5=15=\cardinality{G},
$$
so an injective map between these finite sets is surjective. Hence $\varphi$ is an isomorphism.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{G\cong C_{15}}.
$$

::: pf-proof

By step [](#s3){.pf-ref},
$$
G\cong C_3\times C_5.
$$
Since $\gcd(3,5)=1$, the direct product $C_3\times C_5$ is cyclic of order $15$; equivalently, the Chinese remainder theorem gives
$$
C_3\times C_5\cong C_{15}.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::

::: {.remark title="Variations"}
Equivalently: there is exactly one group of order $15$ up to isomorphism.
:::
