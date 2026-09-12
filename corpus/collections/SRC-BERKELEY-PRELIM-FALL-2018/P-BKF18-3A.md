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

::: problem
Let $X$ be a metric space.

(a) If $U$ is a subset of $X$, show that there is a unique open set $\neg U$ disjoint from $U$ and containing all open sets disjoint from $U$.

(b) Give an example of an open set $U$ with $U\ne\neg\neg U$.

(c) Prove that for every open set $U$, $\neg U=\neg\neg\neg U$.
:::

::: {.solution}
(a) Take $\neg U$ ¬U to be the union of all open sets disjoint from U , which is open as the union of any collection of open sets is open.

(b) Take X to be the real line and U to be the nonzero reals.
Then ¬U is empty so $\neg \neg U$ is the real line.

(c) We have $A \subseteq \neg \neg A$ and applying this to $A = \neg U$ we get $\neg U \subseteq \neg \neg \neg U$ . On the other hand, if $A \subseteq B$ then $\neg B \subseteq \neg A$ , and applying this to $A = U , B = \neg \neg U$ we get $\neg \neg \neg U \subseteq \neg U$
:::
