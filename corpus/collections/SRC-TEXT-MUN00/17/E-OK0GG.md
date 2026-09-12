---
schema: qual/card@1
id: E-OK0GG
kind: problem
title: Closure behavior under unions
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $A$, $B$, and $A_\alpha$ denote subsets of a space $X$.
Prove the following:

(a) If $A \subset B$, then $\overline{A} \subset \overline{B}$.

(b) $\overline{A \cup B} = \overline{A} \cup \overline{B}$.

(c) $\overline{\bigcup A_\alpha} \supset \bigcup \overline{A}_\alpha$; give an example where equality fails.
:::

::: {.solution}
(a) If $A\subseteq B$, every closed set containing $B$ also contains $A$. Since $\overline A$ is the intersection of all closed sets containing $A$ and $\overline B$ is one such closed set, $\overline A\subseteq\overline B$.

(b) By monotonicity,
\[
\overline A\cup\overline B\subseteq\overline{A\cup B}.
\]
Conversely, $\overline A\cup\overline B$ is closed and contains $A\cup B$, so minimality of closure gives
\[
\overline{A\cup B}\subseteq\overline A\cup\overline B.
\]
Hence equality holds.

(c) For every $\alpha$, $A_\alpha\subseteq\bigcup_\beta A_\beta$, so
\[
\overline{A_\alpha}\subseteq\overline{\bigcup_\beta A_\beta}.
\]
Taking the union over $\alpha$ gives
\[
\bigcup_\alpha\overline{A_\alpha}\subseteq\overline{\bigcup_\alpha A_\alpha}.
\]
Equality can fail. In $\mathbb R$, let $A_n=\{1/n\}$. Then
\[
\bigcup_n\overline{A_n}=\{1/n:n\ge1\},
\]
whereas
\[
\overline{\bigcup_nA_n}=\{1/n:n\ge1\}\cup\{0\}.
\]
:::
