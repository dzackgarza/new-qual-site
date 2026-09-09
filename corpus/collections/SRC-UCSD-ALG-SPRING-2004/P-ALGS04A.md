---
schema: qual/card@1
id: P-ALGS04A
kind: problem
title: "Proof of the third Sylow theorem"
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
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Examination, May 2004; the statement agrees with the source.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Prove the third Sylow Theorem: Suppose $p$ is a prime dividing the order of a group $G$.
Then the number of $p$-Sylow subgroups divides the order of $G$ and is congruent to $1 \pmod{p}$.
You may use the first two Sylow Theorems without proof.
:::

::: {.solution}
Let \(\operatorname{Syl}_p(G)\) denote the set of Sylow \(p\)-subgroups of \(G\), and write
\[
n_p:=|\operatorname{Syl}_p(G)|.
\]
Fix \(P\in\operatorname{Syl}_p(G)\).

<1>1. The number \(n_p\) divides \(|G|\).
::: {.proof}
The group \(G\) acts on \(\operatorname{Syl}_p(G)\) by conjugation. By the second Sylow theorem, all Sylow \(p\)-subgroups are conjugate, so this action is transitive. The stabilizer of \(P\) is its normalizer \(N_G(P)\). Hence orbit-stabilizer gives
\[
n_p=[G:N_G(P)],
\]
which divides \(|G|\).
:::

<1>2. Under the conjugation action of \(P\) on \(\operatorname{Syl}_p(G)\), the only fixed point is \(P\) itself.
::: {.proof}
Certainly \(P\) fixes itself. Suppose \(Q\in\operatorname{Syl}_p(G)\) is fixed by every element of \(P\). Then \(P\le N_G(Q)\), so \(P\) normalizes \(Q\). Therefore \(PQ\) is a subgroup of \(G\). Since both \(P\) and \(Q\) are \(p\)-groups, \(PQ\) is a \(p\)-group. But \(Q\) is Sylow, so no larger \(p\)-subgroup can contain it; hence
\[
PQ=Q.
\]
Thus \(P\le Q\). Since \(|P|=|Q|\), we obtain \(P=Q\).
:::

<1>3. One has \(n_p\equiv1\pmod p\).
::: {.proof}
Every orbit of the \(p\)-group \(P\) acting on \(\operatorname{Syl}_p(G)\) has cardinality a power of \(p\). By <1>2 there is exactly one orbit of size \(1\), namely \(\{P\}\); every other orbit therefore has cardinality divisible by \(p\). Consequently
\[
n_p\equiv1\pmod p.
\]
Together with <1>1, this is the third Sylow theorem.
:::
:::
