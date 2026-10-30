---
schema: qual/card@1
id: P-BKS06-1B
kind: problem
title: Decreasing intersection of compact connected sets in $\RR^n$ is connected
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Let $A_{1} \supseteq A_{2} \supseteq \cdots$ be compact connected subsets of $\RR^{n}$. Show that the set $A = \bigcap A_{m}$ is connected.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$A$ is compact and nonempty.

::: pf-proof

$A$ is a closed subset of the compact set $A_1$, so it is compact. If $A$ were empty, the sets $A_1-A_m$ would be an open cover of $A_1$ in the relative topology. They increase with $m$, so a finite subcover would give $A_1=A_1-A_r$ for some $r$, that is $A_r=\varnothing$, which is false because $A_r$ is connected and therefore nonempty.

:::

:::

::: {.pf-step #s2}

Suppose that $A=B_0\cup C_0$ with $B_0$ and $C_0$ disjoint, nonempty and closed in $A$. Then there are disjoint open sets $B\supseteq B_0$ and $C\supseteq C_0$ in $\RR^n$.

::: pf-proof

$B_0$ and $C_0$ are closed subsets of the compact set $A$, so they are compact, and their distance $\delta=\operatorname{dist}(B_0,C_0)$ is positive. Let $B$ and $C$ be the open $\delta/2$-neighborhoods of $B_0$ and $C_0$.

:::

:::

::: {.pf-step #s3}

With the notation of step [](#s2){.pf-ref}, $A_r\subseteq B\cup C$ for some $r$.

::: pf-proof

The sets $A_m-(B\cup C)$ are compact, decreasing, and their intersection is $A-(B\cup C)=\varnothing$. By the argument of step [](#s1){.pf-ref}, one of them is empty.

:::

:::

::: pf-qed

Suppose that $A$ is not connected, and take $B_0,C_0,B,C$ and $r$ as in steps [](#s2){.pf-ref} and [](#s3){.pf-ref}. Then $A_r\cap B$ and $A_r\cap C$ are disjoint and open in $A_r$, their union is $A_r$, and they contain $B_0$ and $C_0$, so both are nonempty. This contradicts the connectedness of $A_r$. Hence $A$ is connected.

:::

:::

:::
