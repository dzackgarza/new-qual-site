---
schema: qual/card@1
id: P-ALGS20B
kind: problem
title: "Counting Sylow p-subgroups containing a given p-subgroup"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose that $G$ is a finite group and $P$ is a $p$-subgroup of $G$ for some prime $p$.
Prove that $$|\{Q \in \operatorname{Syl}_p(G) \mid P \subseteq Q\}| \equiv 1 \pmod{p},$$ where $\operatorname{Syl}_p(G)$ is the set of Sylow $p$-subgroups of $G$.
:::


::: {.solution}
<1>1. Let \(X=\operatorname{Syl}_p(G)\). The \(p\)-group \(P\) acts on \(X\) by conjugation:
\[
p\cdot Q=pQp^{-1}.
\]
::: {.proof}
Conjugation preserves order, so it sends Sylow \(p\)-subgroups to Sylow \(p\)-subgroups. Hence this is a well-defined action of \(P\) on the finite set \(X\).
:::

<1>2. The fixed points of this action are exactly the Sylow \(p\)-subgroups containing \(P\).
::: {.proof}
If \(P\le Q\), then every element of \(P\) lies in \(Q\), so it normalizes \(Q\); thus \(Q\) is fixed.

Conversely, suppose \(Q\in X\) is fixed by \(P\). Then \(P\le N_G(Q)\), so \(Q\trianglelefteq PQ\). Therefore \(PQ\) is a subgroup of \(G\). Since both \(P\) and \(Q\) are \(p\)-groups and \(Q\trianglelefteq PQ\), the order formula
\[
|PQ|=\frac{|P||Q|}{|P\cap Q|}
\]
shows that \(PQ\) is a \(p\)-group. But \(Q\) is Sylow in \(G\), so no larger \(p\)-subgroup can contain it. Hence \(PQ=Q\), and therefore \(P\le Q\).
:::

<1>3. For any action of a finite \(p\)-group on a finite set,
\[
|X|\equiv |X^P|\pmod p.
\]
::: {.proof}
Every orbit has cardinality a power of \(p\). The orbits of size \(1\) are exactly the fixed points, and every other orbit has cardinality divisible by \(p\). Summing the orbit sizes gives the congruence.
:::

<1>4. By Sylow's theorem,
\[
|X|=|\operatorname{Syl}_p(G)|\equiv1\pmod p.
\]
::: {.proof}
The number of Sylow \(p\)-subgroups of a finite group is congruent to \(1\) modulo \(p\).
:::

<1>5. Therefore
\[
\left|\{Q\in\operatorname{Syl}_p(G)\mid P\subseteq Q\}\right|
=|X^P|\equiv1\pmod p.
\]
::: {.proof}
By <1>2 the set in the statement is \(X^P\). Combine <1>3 and <1>4.
:::
:::
