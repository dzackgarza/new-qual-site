---
schema: qual/card@1
id: P-2J6HK
kind: problem
title: Groups of order $p^2$ are abelian
classification:
  areas:
  - algebra
  - prelim
  topics:
  - Classification
  - p-Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the center quotient lemma and the elementary abelian/cyclic dichotomy.
---

::: {.problem}
Let $p$ be a prime. Show that every group of order $p^2$ is abelian and classify all such groups.
:::

::: {.hint}
The group is abelian because $G/Z(G)$ cannot be a nontrivial cyclic group.
If there is no element of order $p^2$, take $a\ne1$, take $b\notin\generators{a}$, and recognize $G$ as the internal direct product $\generators{a}\times\generators{b}$.
:::

::: {.solution}
Let $G$ be a group with $\abs G=p^2$, $p$ prime.

::: pf

::: {.pf-step #center}

$\abs{Z(G)}\in\{p,p^2\}$.

::: pf-proof

The class equation of a finite $p$-group gives $p\mid\abs{Z(G)}$, and $\abs{Z(G)}$ divides $p^2$.

:::

:::

::: {.pf-step #cyclic-quotient}

If $G/Z(G)$ is cyclic, then $G$ is abelian.

::: pf-proof

If $G/Z(G)=\langle gZ(G)\rangle$, every element of $G$ has the form $g^az$ with $a\in\ZZ$ and $z\in Z(G)$. Two such elements $g^az$ and $g^bw$ commute, since $g^a$ and $g^b$ commute and $z,w$ are central.

:::

:::

::: {.pf-step #abelian}

$G$ is abelian.

::: pf-proof

By step [](#center){.pf-ref}, if $Z(G)\ne G$ then $\abs{Z(G)}=p$ and $G/Z(G)$ has prime order $p$, so it is cyclic. Step [](#cyclic-quotient){.pf-ref} then gives $Z(G)=G$, a contradiction. Hence $Z(G)=G$.

:::

:::

::: pf-step

$G$ is isomorphic to exactly one of $\boxed{C_{p^2}}$ and $\boxed{C_p\times C_p}$.

::: pf-proof

If $G$ has an element of order $p^2$, then $G\cong C_{p^2}$. Otherwise every nonidentity element has order $p$. Choose $x\ne1$ and $y\notin\langle x\rangle$. Then $\langle x\rangle\cap\langle y\rangle=1$, since this intersection is a proper subgroup of $\langle y\rangle$, which has prime order. By step [](#abelian){.pf-ref}, $\langle x\rangle\langle y\rangle$ is a subgroup of order $p^2$, so
$$
G=\langle x\rangle\times\langle y\rangle\cong C_p\times C_p.
$$
The two groups are not isomorphic, since only $C_{p^2}$ has an element of order $p^2$.

:::

:::

:::

:::

::: {.remark title="Variations"}
Asked only to prove that every group of order $p^2$ is abelian, stop at step [](#abelian){.pf-ref}.
Asked only to classify the groups of order $p^2$, the whole proof applies unchanged.
:::
