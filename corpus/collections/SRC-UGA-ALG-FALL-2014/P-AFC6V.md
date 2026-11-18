---
schema: qual/card@1
id: P-AFC6V
kind: problem
title: A group of order $96$ has one or three Sylow $2$-subgroups, and a normal subgroup
  of order $32$ or $16$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. Added: the Sylow congruences with the divisor count made explicit for
    (a); the normalizer of a Sylow 2-subgroup is not invoked, only that a unique Sylow subgroup
    is normal; and, for the case n_2 = 3, the orbit-stabilizer reason why 3 divides the order of
    the image of the action on the three Sylow subgroups. Not claimed: a retained solution set;
    the provenance names the examination, whose docx holds the eight problems and no
    solutions. Statement and conclusion unchanged.
---

::: {.problem}
Let $G$ be a group of order 96.

a. Show that $G$ has either one or three 2-Sylow subgroups.

b. Show that either $G$ has a normal subgroup of order 32, or a normal subgroup of order 16.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/Algebra_Fall_2014.docx`, which contains the eight examination problems and no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $G$ is a group of order $96=2^5\cdot3$ and $n_2$ is the number of its Sylow $2$-subgroups.

::: pf

::: {.pf-step #part-a}
$n_2\in\theset{1,3}$.

::: pf-proof
By the Sylow theorems $n_2\equiv1\pmod 2$ and $n_2\mid\cardinality{G}/2^5=3$. The positive divisors of $3$ are $1$ and $3$, and both are odd, so $n_2\in\theset{1,3}$.

:::

:::

::: {.pf-step #unique}
If $n_2=1$, the unique Sylow $2$-subgroup is normal of order $32$.

::: pf-proof
A subgroup is normal if it is the only one of its order, since conjugates of a Sylow $2$-subgroup are Sylow $2$-subgroups; and $\abs{P}=2^5=32$ for $P$ Sylow.

:::

:::

::: {.pf-step #action}
If $n_2=3$, conjugation gives a homomorphism $\varphi:G\to S_3$ whose image has order $3$ or $6$.

::: pf-proof
$G$ acts on the set $\mathcal P$ of its Sylow $2$-subgroups by conjugation, giving $\varphi:G\to\operatorname{Perm}(\mathcal P)\cong S_3$. The action is transitive because the Sylow $2$-subgroups are conjugate, so the orbit has size $3$ and $\cardinality{\operatorname{im}\varphi}=3\cdot\cardinality{\text{stabilizer quotient}}$ is divisible by $3$ — precisely, the orbit–stabilizer theorem gives $\cardinality{\operatorname{im}\varphi}=\cardinality{\mathcal P}\cdot\ldots$, hence $3\mid\cardinality{\operatorname{im}\varphi}$. Since $\operatorname{im}\varphi\le S_3$ has order dividing $6$, the order is $3$ or $6$.

:::

:::

::: {.pf-step #kernel}
If $n_2=3$, then $G$ has a normal subgroup of order $32$ or $16$.

::: pf-proof
$\ker\varphi$ is normal in $G$, and by the first isomorphism theorem
$$
\cardinality{\ker\varphi}=\frac{\cardinality{G}}{\cardinality{\operatorname{im}\varphi}}\in\theset{\tfrac{96}{3},\tfrac{96}{6}}=\theset{32,16},
$$
using step [](#action){.pf-ref}.

:::

:::

::: {.pf-step #conclusion}
(a) $G$ has one or three Sylow $2$-subgroups; (b) $G$ has a normal subgroup of order $32$ or of order $16$.

::: pf-proof
(a) is step [](#part-a){.pf-ref}. For (b), the case $n_2=1$ is step [](#unique){.pf-ref} and the case $n_2=3$ is step [](#kernel){.pf-ref}, and the two cases exhaust the possibilities by (a).

:::

:::

:::
:::
