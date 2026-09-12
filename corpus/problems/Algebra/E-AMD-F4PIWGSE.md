---
schema: qual/card@1
id: E-AMD-F4PIWGSE
kind: problem
title: Sylow subgroups of a group of order $240$, and subgroups of order $15$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Semidirect Products
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Suppose $|G| = 240 = 2^4 \cdot 3 \cdot 5$.

- How many Sylow-$p$ subgroups does $G$ have for $p\in \{2, 3, 5\}$?

- Show that if $G$ has a subgroup of order 15, it has an element of order 15.

- Show that if $G$ does not have such a subgroup, the number of Sylow-$3$ subgroups is either 10 or 40.
:::

::: {.solution}
Write \(n_p\) for the number of Sylow \(p\)-subgroups of \(G\).

By Sylow's theorem,
\[
n_2\mid15,\quad n_2\equiv1\pmod2,
\]
so
\[
\boxed{n_2\in\{1,3,5,15\}}.
\]
Likewise,
\[
n_3\mid80,\quad n_3\equiv1\pmod3,
\]
so
\[
\boxed{n_3\in\{1,4,10,16,40\}},
\]
and
\[
n_5\mid48,\quad n_5\equiv1\pmod5,
\]
so
\[
\boxed{n_5\in\{1,6,16\}}.
\]

Now let \(H\le G\) have order \(15\). In \(H\),
\[
n_5(H)\mid3,\quad n_5(H)\equiv1\pmod5,
\]
so \(n_5(H)=1\), and
\[
n_3(H)\mid5,\quad n_3(H)\equiv1\pmod3,
\]
so \(n_3(H)=1\). Thus both Sylow subgroups are normal, and
\[
H\cong C_3\times C_5\cong C_{15}.
\]
Hence \(G\) contains an element of order \(15\).

Finally suppose \(G\) has no subgroup of order \(15\). Fix \(Q\in\operatorname{Syl}_5(G)\) and let \(Q\) act by conjugation on \(\operatorname{Syl}_3(G)\). Every orbit has size \(1\) or \(5\). A fixed Sylow \(3\)-subgroup \(P\) would be normalized by \(Q\), so \(PQ\) would be a subgroup of order \(15\), contrary to hypothesis. Hence every orbit has size \(5\), so \(5\mid n_3\). From the candidate list above,
\[
\boxed{n_3\in\{10,40\}}.
\]
:::
