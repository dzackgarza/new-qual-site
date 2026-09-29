---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-09
kind: problem
title: A finite intersection of closed sets contained in a prescribed open neighborhood
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against problem (9) in assets/attachments/Day_1_-_Compactness_Problems.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be a compact space and let $\{C_\alpha\}_{\alpha\in A}$ be a collection of closed sets in $X$.
Let $C=\bigcap_{\alpha\in A}C_\alpha$ and let $U$ be an open set containing $C$.
Prove there is a finite set $\alpha_1,\ldots,\alpha_n$ in $A$ with $C_{\alpha_1}\cap\cdots\cap C_{\alpha_n}\subseteq U$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The family
\[
\{U\}\cup\{X\setminus C_\alpha:\alpha\in A\}
\]
is an open cover of $X$.

::: pf-proof

Each $C_\alpha$ is closed, so every $X\setminus C_\alpha$ is open.
Let $x\in X$.
If $x\in U$, then $x$ is covered by $U$.
If $x\notin U$, then $x\notin C$ because $C\subseteq U$.
Since
\[
C=\bigcap_{\alpha\in A}C_\alpha,
\]
there is some $\alpha$ with $x\notin C_\alpha$, so $x\in X\setminus C_\alpha$.
Thus the displayed family covers $X$.

:::

:::

::: {.pf-step #s2}

Compactness of $X$ gives indices $\alpha_1,\dots,\alpha_n\in A$ such that
\[
X=U\cup(X\setminus C_{\alpha_1})\cup\cdots\cup(X\setminus C_{\alpha_n}).
\]

::: pf-proof

Apply the definition of compactness to the open cover in step [](#s1){.pf-ref}.
If a finite subcover omits $U$, adjoin $U$ without affecting finiteness.

:::

:::

::: {.pf-step #s3}

One has
\[
C_{\alpha_1}\cap\cdots\cap C_{\alpha_n}\subseteq U.
\]

::: pf-proof

Let $x$ lie in the finite intersection on the left.
Then $x$ lies in none of the complements $X\setminus C_{\alpha_i}$.
The covering equality in step [](#s2){.pf-ref} therefore forces $x\in U$.

:::

:::

::: pf-step

This is the required finite family.

::: pf-proof

The indices $\alpha_1,\dots,\alpha_n$ from step [](#s2){.pf-ref} satisfy exactly the inclusion proved in step [](#s3){.pf-ref}.

:::

:::

:::

:::
