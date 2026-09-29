---
schema: qual/card@1
id: P-HOBOM
kind: problem
title: Existence of nonabelian groups of order $5$ and $6$
classification:
  areas:
  - prelim
  topics:
  - Groups
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
For $n = 5, 6$, either give an example of a nonabelian group of order $n$, or prove that none exists.
:::

::: {.solution}
**Case $n = 5$:**

::: pf

::: {.pf-step #s1}
Every group of prime order is cyclic, hence abelian.

::: pf-proof

::: pf-step
Let $G$ be a group with $|G| = 5$.

::: pf-proof
setup.
:::

:::

::: pf-step
Choose an element $g \in G \setminus \{e\}$.

::: pf-proof
$|G| = 5 > 1$.
:::

:::

::: pf-step
By Lagrange's theorem, the order of the subgroup $\langle g \rangle$ divides $|G| = 5$.

::: pf-proof
Lagrange's theorem.
:::

:::

::: {.pf-step #s1-4}
Since $g \neq e$, $|\langle g \rangle| > 1$, so $|\langle g \rangle| = 5$.

::: pf-proof
$5$ is prime, so its only positive divisors are $1$ and $5$.
:::

:::

::: {.pf-step #s1-5}
Therefore, $G = \langle g \rangle \cong \mathbb{Z}/5\mathbb{Z}$, which is cyclic and abelian.

::: pf-proof
Step [](#s1-4){.pf-ref}.
:::

:::

::: pf-step
No nonabelian group of order $5$ exists.

::: pf-proof
Step [](#s1-5){.pf-ref}.
:::

:::

:::

:::
:::


**Case $n = 6$:**

::: pf

::: {.pf-step #s2}
The symmetric group $S_3$ is a nonabelian group of order $6$.

::: pf-proof

::: {.pf-step #s2-1}
The order of $S_3$ is $3! = 6$.

::: pf-proof
order formula for symmetric groups on $3$ elements.
:::

:::

::: pf-step
Let $\sigma = (1\ 2)$ and $\tau = (2\ 3)$ in $S_3$.

::: pf-proof
definitions of transpositions in $S_3$.
:::

:::

::: pf-step
$\sigma \tau = (1\ 2)(2\ 3) = (1\ 2\ 3)$.

::: pf-proof
direct cycle composition: $1 \mapsto 1 \mapsto 2$, $2 \mapsto 3 \mapsto 3$, $3 \mapsto 2 \mapsto 1$.
:::

:::

::: pf-step
$\tau \sigma = (2\ 3)(1\ 2) = (1\ 3\ 2)$.

::: pf-proof
direct cycle composition: $1 \mapsto 2 \mapsto 3$, $2 \mapsto 1 \mapsto 1$, $3 \mapsto 3 \mapsto 2$.
:::

:::

::: {.pf-step #s2-5}
Since $\sigma \tau \neq \tau \sigma$, $S_3$ is nonabelian.

::: pf-proof
$(1\ 2\ 3) \neq (1\ 3\ 2)$ (for example, they map $1$ to different elements).
:::

:::

::: pf-step
Hence $S_3$ (or equivalently the dihedral group $D_3$) is a nonabelian group of order $6$.

::: pf-proof
Steps [](#s2-1){.pf-ref} and [](#s2-5){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.
:::

:::
:::
