---
schema: qual/card@1
id: P-ALGS25B
kind: problem
title: Sylow of a normal subgroup and generation by normalizers
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
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
Suppose $N$ is a normal subgroup of $G$ and $P$ is a Sylow $p$-subgroup of $N$.

(a) Prove that there exists $Q \in \operatorname{Syl}_p(G)$ such that $P = Q \cap N$.

(b) Prove that $N_G(Q) \subseteq N_G(P)$.

(c) Prove that $g \in \langle N_G(P) \cup g N_G(P) g^{-1} \rangle$ for every $g \in G$.
:::


::: {.solution}
**(a).**

<1>1. Choose a Sylow \(p\)-subgroup \(Q\) of \(G\) containing \(P\).
::: {.proof}
Every \(p\)-subgroup of a finite group is contained in a Sylow \(p\)-subgroup.
:::

<1>2. One has
\[
P=Q\cap N.
\]
::: {.proof}
Because \(N\trianglelefteq G\), the intersection \(Q\cap N\) is a \(p\)-subgroup of \(N\). It contains \(P\), since \(P\le Q\) by <1>1 and \(P\le N\) by hypothesis. But \(P\) is a Sylow \(p\)-subgroup of \(N\), so no strictly larger \(p\)-subgroup of \(N\) can contain it. Hence equality holds.
:::

**(b).**

<1>3. If \(g\in N_G(Q)\), then \(g\in N_G(P)\).
::: {.proof}
Using <1>2 and normality of \(N\),
\[
gPg^{-1}
=g(Q\cap N)g^{-1}
=(gQg^{-1})\cap(gNg^{-1})
=Q\cap N
=P.
\]
Thus \(g\) normalizes \(P\).
:::

<1>4. Therefore
\[
N_G(Q)\subseteq N_G(P).
\]
::: {.proof}
This is exactly <1>3.
:::

**(c).**

<1>5. Fix \(g\in G\) and set
\[
H=\left\langle N_G(P)\cup gN_G(P)g^{-1}\right\rangle.
\]
Then both \(Q\) and \(gQg^{-1}\) are subgroups of \(H\).
::: {.proof}
One has \(Q\le N_G(Q)\le N_G(P)\) by part (b), so \(Q\le H\). Conjugating this inclusion gives \(gQg^{-1}\le gN_G(P)g^{-1}\le H\).
:::

<1>6. The subgroups \(Q\) and \(gQg^{-1}\) are Sylow \(p\)-subgroups of \(H\).
::: {.proof}
They have the same order as a Sylow \(p\)-subgroup of \(G\). Since \(H\le G\), no \(p\)-subgroup of \(H\) can have larger order. Thus both are Sylow in \(H\).
:::

<1>7. There exists \(h\in H\) such that
\[
hQh^{-1}=gQg^{-1}.
\]
::: {.proof}
Apply Sylow conjugacy inside the finite group \(H\) to the two Sylow \(p\)-subgroups from <1>6.
:::

<1>8. One has \(g^{-1}h\in N_G(Q)\subseteq H\).
::: {.proof}
Rearranging <1>7 gives
\[
(g^{-1}h)Q(g^{-1}h)^{-1}=Q,
\]
so \(g^{-1}h\in N_G(Q)\). Part (b) gives \(N_G(Q)\le N_G(P)\le H\).
:::

<1>9. Therefore \(g\in H\), i.e.
\[
g\in\left\langle N_G(P)\cup gN_G(P)g^{-1}\right\rangle.
\]
::: {.proof}
Both \(h\) and \(g^{-1}h\) lie in \(H\) by <1>7 and <1>8. Hence \(g^{-1}=(g^{-1}h)h^{-1}\in H\), so \(g\in H\).
:::
:::
