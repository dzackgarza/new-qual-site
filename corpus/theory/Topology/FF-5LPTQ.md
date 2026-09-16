---
schema: qual/card@1
id: FF-5LPTQ
kind: fact
title: Mayer--Vietoris sequence for $X = A\cup B$
prompts:
- Write the Mayer-Vietoris long exact sequence for $X = A \cup B$.
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
---

::: {.fact}
Let $X$ be a topological space and $A, B\subseteq X$ subspaces whose interiors cover $X$.
Let $i\colon A\cap B\hookrightarrow A$, $j\colon A\cap B\hookrightarrow B$, $k\colon A\hookrightarrow X$, and $l\colon B\hookrightarrow X$ be the inclusions.
The [[D-FAIJX|Mayer--Vietoris sequence]] is the long exact sequence
$$
\cdots\to H_n(A\cap B)\xrightarrow{(i_*,\,j_*)}H_n(A)\oplus H_n(B)\xrightarrow{k_*-l_*}H_n(X)\xrightarrow{\del}H_{n-1}(A\cap B)\to\cdots\to H_0(X)\to 0
$$
[@Hat02, §2.2, p. 149].
:::
