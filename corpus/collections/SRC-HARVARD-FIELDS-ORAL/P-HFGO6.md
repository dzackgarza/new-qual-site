---
schema: qual/card@1
id: P-HFGO6
kind: problem
title: A Galois extension with quaternion group
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Does there exist a Galois extension whose Galois group is the quaternion group $\{\pm1,\pm i,\pm j,\pm k\}$?
Justify your answer.
:::

::: solution
Yes. More generally, every finite group occurs as the Galois group of some
field extension.

Let
\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\}
\]
and choose a field $k$, for example $k=\mathbb Q$. Introduce algebraically
independent variables
\[
\{x_g:g\in Q_8\}
\]
and set
\[
K=k(x_g:g\in Q_8).
\]

<1>1. The group $Q_8$ acts faithfully on $K$ by $k$-automorphisms.
::: proof
For $h\in Q_8$, define
\[
h(x_g)=x_{hg}
\]
and let $h$ fix $k$. Permuting an algebraically independent transcendence basis
extends uniquely to an automorphism of the rational function field. Moreover,
if $h\ne1$, then
\[
h(x_1)=x_h\ne x_1,
\]
so the action is faithful.
:::

<1>2. If
\[
F=K^{Q_8}
\]
is the fixed field, then $K/F$ is a finite Galois extension and
\[
\operatorname{Gal}(K/F)=Q_8.
\]
::: proof
Artin's fixed-field theorem says that if a finite group $G$ acts faithfully by
automorphisms on a field $K$, then
\[
[K:K^G]=|G|
\]
and $K/K^G$ is Galois with Galois group exactly $G$.
Applying this to the action in <1>1 gives
\[
[K:F]=8
\]
and
\[
\operatorname{Gal}(K/F)\cong Q_8.
\]
:::

Thus a Galois extension with quaternion Galois group does exist.
:::
