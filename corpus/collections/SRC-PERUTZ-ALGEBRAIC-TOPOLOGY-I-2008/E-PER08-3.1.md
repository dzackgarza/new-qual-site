---
schema: qual/card@1
id: E-PER08-3.1
kind: problem
title: Uniqueness of group pushouts
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 3.1 and Definition 3.3 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified both universal-property comparison maps and uniqueness relative to the structure maps.
---

::: {.problem}
Let $G_1\xleftarrow{f_1}H\xrightarrow{f_2}G_2$ be homomorphisms.
A pushout is a group $P$ with homomorphisms $p_i:G_i\to P$ such that $p_1f_1=p_2f_2$ and with the following universal property: for every group $K$ and maps $k_i:G_i\to K$ satisfying $k_1f_1=k_2f_2$, there is a unique homomorphism $h:P\to K$ such that $k_i=hp_i$.

Prove that this universal property determines $P$ up to isomorphism.
In what sense is the isomorphism unique?
:::

::: {.solution}
Suppose
\[
(P,p_1,p_2)
\qquad\text{and}\qquad
(Q,q_1,q_2)
\]
are two pushouts of the same diagram
\[
G_1\xleftarrow{f_1}H\xrightarrow{f_2}G_2.
\]

<1>1. There is a unique homomorphism $\phi:P\to Q$ compatible with the structure maps.
::: {.proof}
Because $Q$ is a pushout square,
\[
q_1f_1=q_2f_2.
\]
Apply the universal property of $P$ with $K=Q$ and $k_i=q_i$. There is a unique homomorphism
\[
\phi:P\to Q
\]
such that
\[
\phi p_1=q_1,
\qquad
\phi p_2=q_2.
\]
:::

<1>2. There is a unique homomorphism $\psi:Q\to P$ compatible with the structure maps.
::: {.proof}
Similarly, since
\[
p_1f_1=p_2f_2,
\]
the universal property of $Q$ gives a unique homomorphism
\[
\psi:Q\to P
\]
such that
\[
\psi q_1=p_1,
\qquad
\psi q_2=p_2.
\]
:::

<1>3. The maps $\phi$ and $\psi$ are inverse isomorphisms.
::: {.proof}
For $i=1,2$,
\[
(\psi\phi)p_i
=\psi(\phi p_i)
=\psi q_i
=p_i.
\]
The identity map $\operatorname{id}_P:P\to P$ also satisfies
\[
\operatorname{id}_P p_i=p_i.
\]
By the uniqueness clause in the universal property of $P$,
\[
\psi\phi=\operatorname{id}_P.
\]

Likewise,
\[
(\phi\psi)q_i=q_i
\]
for $i=1,2$, and the uniqueness clause for $Q$ gives
\[
\phi\psi=\operatorname{id}_Q.
\]
Therefore $\phi$ is an isomorphism with inverse $\psi$.
:::

<1>4. The isomorphism is unique as an isomorphism of pushout diagrams.
::: {.proof}
Suppose
\[
\theta:P\to Q
\]
is any homomorphism satisfying
\[
\theta p_i=q_i
\qquad(i=1,2).
\]
The universal property of $P$ says that there is exactly one such homomorphism, namely $\phi$. Hence
\[
\theta=\phi.
\]

Thus the pushout is not merely unique up to some abstract group isomorphism: it is unique up to the unique isomorphism that commutes with the canonical maps from $G_1$ and $G_2$.
:::
:::
