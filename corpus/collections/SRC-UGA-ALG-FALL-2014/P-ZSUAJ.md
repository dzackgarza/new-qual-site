---
schema: qual/card@1
id: P-ZSUAJ
kind: problem
title: $xR$ is proper in a nonzero commutative ring without unit and with no proper
  maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $R$ be a nonzero commutative ring without unit such that $R$ does not contain a proper maximal ideal.
Prove that for all $x\in R$, the ideal $xR$ is proper.

> You may assume the axiom of choice.
:::

::: {.solution}

::: pf

::: {.pf-step #assume-xr-equals-r}
Suppose for contradiction that $xR = R$ for some $x \in R$.

::: pf-proof
assume the contrary.
:::

:::

::: {.pf-step #x-equals-xy}
Then $x \in xR = R$, so there is $y \in R$ with $x = xy$.

::: pf-proof
since $xR = R$, the element $x$ lies in $xR$, so $x = xy$ for some $y \in R$.
:::

:::

::: {.pf-step #consider-ideal-j}
Consider the ideal $J = \{r \in R : r = ry\}$.

::: pf-proof

::: pf-step
$J$ is an ideal.

::: pf-proof
$0 = 0y$; if $r = ry$ and $s = sy$, then $r + s = ry + sy = (r+s)y$; and for $t \in R$, $tr = t(ry) = (tr)y$ (using commutativity).
:::

:::

::: pf-step
$J$ is proper.

::: pf-proof
if $J = R$, then $r = ry$ for all $r \in R$, so $y$ is a right identity; since $R$ is commutative, $y$ is a two-sided identity (a unit), contradicting that $R$ has no unit. Hence $J \neq R$.
:::

:::

:::

:::

::: {.pf-step #zorn-gives-maximal-ideal}
By Zorn's lemma, $J$ is contained in a maximal ideal $M$.

::: pf-proof

::: {.pf-step #poset-setup}
Consider the poset of proper ideals of $R$ containing $J$, ordered by inclusion.

::: pf-proof
setup.
:::

:::

::: {.pf-step #chain-bound-proper}
Every chain has an upper bound (the union of the chain), and this union is proper.

::: pf-proof
the union of a chain of ideals is an ideal; if the union were $R$, then $x$ would lie in some member $K$ of the chain, and since $xR = R$ (step [](#assume-xr-equals-r){.pf-ref}), we would get $R = xR \subseteq K$, contradicting that $K$ is proper.
:::

:::

::: pf-step
Hence by Zorn's lemma there is a maximal proper ideal $M$ containing $J$.

::: pf-proof
Step [](#poset-setup){.pf-ref} and step [](#chain-bound-proper){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #contradicts-hypothesis}
This contradicts the hypothesis that $R$ has no proper maximal ideal.

::: pf-proof
Step [](#zorn-gives-maximal-ideal){.pf-ref} produces a maximal ideal $M$.
:::

:::

::: {.pf-step #xr-proper-conclusion}
Therefore $xR \neq R$, i.e. $xR$ is proper, for every $x \in R$.

::: pf-proof
Steps [](#assume-xr-equals-r){.pf-ref}, [](#x-equals-xy){.pf-ref}, [](#consider-ideal-j){.pf-ref}, [](#zorn-gives-maximal-ideal){.pf-ref} and [](#contradicts-hypothesis){.pf-ref}.
:::

:::

::: pf-qed
Step [](#xr-proper-conclusion){.pf-ref}.
:::

:::

:::
