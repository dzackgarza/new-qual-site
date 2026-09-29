---
schema: qual/card@1
id: E-MUN-9-2
kind: problem
title: Choice functions for countable collections
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Find if possible a choice function for each of the following collections, without using the choice axiom:

(a) The collection $\mathcal{A}$ of nonempty subsets of $\mathbb{Z}_{+}$ .

(b) The collection B of nonempty subsets of Z.

(c) The collection C of nonempty subsets of the rational numbers Q.

(d) The collection $\mathcal{D}$ of nonempty subsets of $X^{\omega}$, where $X = \{0,1\}$ .
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) Yes: $c(A)=\min A$ (least element) is a choice function for nonempty subsets of $\ZZ_+$.

::: pf-proof

$\ZZ_+$ well-ordered.

:::

:::

::: pf-step

(b) Yes: well-order $\ZZ$ as $0,1,-1,2,-2,\dots$ and take least in that order.

::: pf-proof

explicit well-ordering.

:::

:::

::: pf-step

(c) Yes: $\QQ$ countable, fix enumeration $q_1,q_2,\dots$ and take $c(A)=q_{\min\{n:q_n\in A\}}$.

::: pf-proof

countable well-ordering.

:::

:::

::: {.pf-step #s4}

(d) No: $\mathcal D$ is all nonempty subsets of Cantor set $2^\omega$; no definable choice without AC (requires AC).

::: pf-proof

$2^\omega$ uncountable with no definable well-order in ZF.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::
