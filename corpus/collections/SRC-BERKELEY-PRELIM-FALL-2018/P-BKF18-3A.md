---
schema: qual/card@1
id: P-BKF18-3A
kind: problem
title: The largest open set disjoint from a subset
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $X$ be a metric space.

(a) If $U$ is a subset of $X$, show that there is a unique open set $\neg U$ disjoint from $U$ and containing all open sets disjoint from $U$.

(b) Give an example of an open set $U$ with $U\ne\neg\neg U$.

(c) Prove that for every open set $U$, $\neg U=\neg\neg\neg U$.
(Hint: if $A\subseteq B$ and $B\subseteq A$ then $A=B$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) The set $\neg U$ exists and is unique.

::: pf-proof

Let $\neg U$ be the union of all open sets disjoint from $U$. It is open, it is disjoint from $U$, and it contains every open set disjoint from $U$. If $V$ is another open set with these properties, then $V\subseteq\neg U$ and $\neg U\subseteq V$, so $V=\neg U$.

:::

:::

::: {.pf-step #s2}

(b) In $X=\RR$, the open set $U=\RR\setminus\{0\}$ satisfies $U\ne\neg\neg U$.

::: pf-proof

An open set disjoint from $U$ is contained in $\{0\}$, so it is empty. Thus $\neg U=\emptyset$ and $\neg\neg U=\RR\ne U$.

:::

:::

::: {.pf-step #s3}

For subsets $A,B$ of $X$: if $A$ is open, then $A\subseteq\neg\neg A$; if $A\subseteq B$, then $\neg B\subseteq\neg A$.

::: pf-proof

If $A$ is open, then $A$ is an open set disjoint from $\neg A$, so $A\subseteq\neg\neg A$. If $A\subseteq B$, then $\neg B$ is an open set disjoint from $A$, so $\neg B\subseteq\neg A$.

:::

:::

::: {.pf-step #s4}

(c) $\neg U=\neg\neg\neg U$ for every open set $U$.

::: pf-proof

The set $\neg U$ is open, so step [](#s3){.pf-ref} with $A=\neg U$ gives $\neg U\subseteq\neg\neg\neg U$. Step [](#s3){.pf-ref} with $A=U$ gives $U\subseteq\neg\neg U$, and then with $A=U$, $B=\neg\neg U$ it gives $\neg\neg\neg U\subseteq\neg U$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s4){.pf-ref} prove (a), (b) and (c).

:::

:::

:::
