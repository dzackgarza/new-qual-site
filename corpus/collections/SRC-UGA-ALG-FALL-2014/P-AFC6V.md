---
schema: qual/card@1
id: P-AFC6V
kind: problem
title: A group of order $96$ has one or three Sylow $2$-subgroups, and a normal subgroup
  of order $32$ or $16$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
---

::: {.problem}
Let $G$ be a group of order 96.

a. Show that $G$ has either one or three 2-Sylow subgroups.

b. Show that either $G$ has a normal subgroup of order 32, or a normal subgroup of order 16.
:::

::: {.solution}
Since
\[
|G|=96=2^5\cdot3,
\]
the number $n_2$ of Sylow $2$-subgroups satisfies
\[
n_2\equiv1\pmod2,
\qquad
n_2\mid3.
\]
Hence
\[
\boxed{n_2\in\{1,3\}},
\]
proving (a).

If $n_2=1$, the unique Sylow $2$-subgroup is normal and has order $32$, so
we are done.

Assume now that $n_2=3$. Conjugation gives an action of $G$ on the set
$\mathcal P$ of its three Sylow $2$-subgroups, hence a homomorphism
\[
\varphi:G\longrightarrow S_3.
\]
The action is transitive, because all Sylow $2$-subgroups are conjugate.
Therefore $|\operatorname{im}\varphi|$ is divisible by $3$. Since it also
divides $|S_3|=6$, we have
\[
|\operatorname{im}\varphi|\in\{3,6\}.
\]
Thus
\[
|\ker\varphi|
=\frac{96}{|\operatorname{im}\varphi|}
\in\{32,16\}.
\]
The kernel is normal in $G$, so $G$ has a normal subgroup of order $32$ or
$16$, as required.
:::
