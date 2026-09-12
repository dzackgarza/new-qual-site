---
schema: qual/card@1
id: E-KVFCT
kind: problem
title: Sigma-compact regular spaces are paracompact
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Compactness
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

(a) Let $X$ be a regular space.
If $X$ is a countable union of compact subspaces of $X$, then $X$ is paracompact.

(b) Show that $\mathbb{R}^\infty$ is paracompact as a subspace of $\mathbb{R}^\omega$ in the box topology.
:::

::: {.solution}
(a) Suppose
\[
X=\bigcup_{n=1}^{\infty}K_n
\]
with each \(K_n\) compact. Then \(X\) is Lindelöf: if \(\mathcal U\) is an open cover, each \(K_n\) has a finite subcover, and the union of these finite subcovers over \(n\) is countable and covers \(X\).

We now prove directly that a regular Lindelöf space is paracompact. Let \(\mathcal U\) be an open cover. For every \(x\in X\), regularity gives open sets \(V_x\) and \(U_x\in\mathcal U\) such that
\[
x\in V_x\subset\overline{V_x}\subset U_x.
\]
By Lindelöfness choose \(V_1,V_2,\ldots\) covering \(X\), with corresponding \(U_n\in\mathcal U\). Define
\[
W_n=U_n-\bigcup_{i<n}\overline{V_i}.
\]
Each \(W_n\) is open and refines \(\mathcal U\). The family covers \(X\): for \(x\), choose the least \(i\) such that \(x\in\overline{V_i}\); then \(x\in U_i\) and \(x\notin\overline{V_j}\) for \(j<i\), hence \(x\in W_i\). It is locally finite: if \(x\in V_m\), then \(V_m\cap W_n=\varnothing\) for every \(n>m\), since \(W_n\) omits \(\overline{V_m}\). Thus \(V_m\) meets only \(W_1,\ldots,W_m\). Hence \(X\) is paracompact.

(b) Let \(\mathbb R^\infty\) be the eventually-zero sequences, with the topology inherited from the box topology on \(\mathbb R^\omega\). For \(n,m\ge1\), put
\[
K_{n,m}=[-m,m]^n\times\{0\}\times\{0\}\times\cdots.
\]
On \(K_{n,m}\), the box-subspace topology is just the usual finite product topology, so \(K_{n,m}\) is compact. Moreover
\[
\mathbb R^\infty=\bigcup_{n,m\ge1}K_{n,m}.
\]
The box product \(\mathbb R^\omega\) is completely regular, hence its subspace \(\mathbb R^\infty\) is regular. Therefore part (a) applies, and \(\mathbb R^\infty\) is paracompact.
:::
