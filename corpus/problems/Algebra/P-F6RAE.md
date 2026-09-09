---
schema: qual/card@1
id: P-F6RAE
kind: problem
title: A normal $p$-subgroup is contained in every Sylow $p$-subgroup
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: problem
Let $G$ be a finite group, and let $N \trianglelefteq G$ be a normal $p$-subgroup of $G$ (for a prime $p$).
Prove that $N$ is contained in **every** Sylow $p$-subgroup of $G$.
:::

::: solution
Let $P$ be any Sylow $p$-subgroup of $G$. Since $N\trianglelefteq G$, the product $NP$ is a subgroup of $G$. Moreover,
\[
|NP|=\frac{|N||P|}{|N\cap P|},
\]
which is a power of $p$. Thus $NP$ is a $p$-subgroup of $G$ containing the Sylow $p$-subgroup $P$.

By maximality of $P$ among $p$-subgroups,
\[
NP=P.
\]
Therefore
\[
N\subseteq NP=P.
\]
Since $P$ was arbitrary, $N$ is contained in every Sylow $p$-subgroup of $G$.
:::
