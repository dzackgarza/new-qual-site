---
schema: qual/card@1
id: P-OY3KM
kind: problem
title: Definition and an example of a Noetherian ring
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
(1) State the definition of a **Noetherian ring** (give all three equivalent characterizations).
(2) Give standard examples and non-examples of Noetherian rings.
:::

::: solution
For a ring $R$, the following are equivalent:

1. every ascending chain of ideals stabilizes;
2. every ideal of $R$ is finitely generated;
3. every nonempty set of ideals has a maximal element under inclusion.

Indeed, (1)$\Rightarrow$(2): if an ideal $I$ were not finitely generated, choose successively $x_i\in I$ outside $(x_1,\dots,x_{i-1})$ to obtain a strictly ascending chain. For (2)$\Rightarrow$(1), if $I_1\subseteq I_2\subseteq\cdots$, then $I=\bigcup I_n$ is an ideal; finite generation of $I$ places all generators in some $I_N$, so $I=I_N$ and the chain stabilizes. The equivalence with (3) is the standard maximal-condition reformulation of ACC.

Examples: fields and PIDs are Noetherian; Hilbert's basis theorem shows that $R[x_1,\dots,x_n]$ is Noetherian whenever $R$ is; quotients and localizations of Noetherian rings are Noetherian. In particular $k[[x_1,\dots,x_n]]$ is Noetherian.

A standard nonexample is $k[x_1,x_2,\dots]$, since
\[
(x_1)\subsetneq(x_1,x_2)\subsetneq\cdots
\]
does not stabilize.
:::
