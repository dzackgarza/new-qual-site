---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-05
kind: problem
title: Hausdorffness of the radial quotient of the open disk
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 5 of the Topology Ph.D. Qualifying Exam dated January 12, 2008 in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Factored the modulus map through the quotient to a continuous bijection D/~ -> [0,1), then exhibited the continuous inverse t -> q(t); hence the quotient is homeomorphic to a Hausdorff interval.
---

::: {.problem}
Let $D$ be the open unit disk in the complex plane that is $D:=\{z\mid |z|<1\}$.
Let $\sim$ be an equivalence relation on $D$ defined by $z_1\sim z_2$ if $|z_1|=|z_2|$.
Is the quotient space $D/\sim$ Hausdorff?
Prove or disprove.
:::

::: {.solution}
Let
\[
q:D\longrightarrow D/\!\sim
\]
be the quotient map and let
\[
r:D\longrightarrow[0,1),
\qquad
r(z)=|z|.
\]

<1>1. The modulus map $r$ is constant exactly on the equivalence classes of $\sim$.
::: {.proof}
By definition,
\[
z_1\sim z_2
\quad\Longleftrightarrow\quad
|z_1|=|z_2|
\quad\Longleftrightarrow\quad
r(z_1)=r(z_2).
\]
Thus the fibers of $r$ are precisely the equivalence classes.
:::

<1>2. There is a unique continuous map
\[
\bar r:D/\!\sim\longrightarrow[0,1)
\]
satisfying
\[
\bar r(q(z))=|z|.
\]
::: {.proof}
The modulus map $r$ is continuous and is constant on equivalence classes by <1>1.
By the universal property of the quotient topology, $r$ therefore factors uniquely as
\[
r=\bar r\circ q
\]
with $\bar r$ continuous.
:::

<1>3. The map $\bar r$ is bijective.
::: {.proof}
For surjectivity, if $t\in[0,1)$, regard $t$ as the point $t+0i\in D$. Then
\[
\bar r(q(t))=|t|=t.
\]
For injectivity, if
\[
\bar r(q(z_1))=\bar r(q(z_2)),
\]
then $|z_1|=|z_2|$, so $z_1\sim z_2$ by definition and hence $q(z_1)=q(z_2)$.
:::

<1>4. The inverse of $\bar r$ is the continuous map
\[
s:[0,1)\longrightarrow D/\!\sim,
\qquad
s(t)=q(t).
\]
::: {.proof}
The inclusion
\[
j:[0,1)\longrightarrow D,
\qquad
j(t)=t+0i,
\]
is continuous, and $q$ is continuous by definition of a quotient map.
Thus
\[
s=q\circ j
\]
is continuous.
Moreover,
\[
(\bar r\circ s)(t)=\bar r(q(t))=t.
\]
Conversely, for $q(z)\in D/\!\sim$,
\[
(s\circ\bar r)(q(z))
=s(|z|)
=q(|z|).
\]
Since $z\sim |z|$, their quotient classes agree, so $q(|z|)=q(z)$.
Hence $s$ and $\bar r$ are mutual inverses.
:::

<1>5. Therefore
\[
D/\!\sim\ \cong [0,1),
\]
and in particular $D/\!\sim$ is Hausdorff.
::: {.proof}
By <1>2--<1>4, $\bar r$ is a homeomorphism.
The interval $[0,1)$ is a subspace of the Hausdorff space $\mathbb R$, hence is Hausdorff.
Hausdorffness is preserved by homeomorphism, so the quotient is Hausdorff.
:::
:::
