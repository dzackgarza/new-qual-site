---
schema: qual/card@1
id: E-SMI-8000E-FEA
kind: problem
title: Group theory definitions
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all five definition prompts with Smith 8000 Fall 2006 final part A."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Gave standard definitions, including the explicit multiplication convention for the semidirect product determined by c:H→Aut(K)."
---

::: {.exercise}
Define what is meant by:

(i) a normal subgroup of a group $G$;

(ii) a Sylow subgroup of $G$;

(iii) a simple group;

(iv) a left action of a group $G$ on a set $S$;

(v) the semidirect product group defined by a homomorphism $c: H \to \operatorname{Aut}(K)$.
:::

::: {.solution}

::: pf

::: pf-step

Normal subgroup.

::: pf-proof

A subgroup $N\le G$ is **normal**, written
$$
N\trianglelefteq G,
$$
if
$$
gNg^{-1}=N
$$
for every $g\in G$. Equivalently,
$$
gN=Ng
$$
for every $g\in G$.

:::

:::

::: pf-step

Sylow subgroup.

::: pf-proof

Let $G$ be finite and let $p$ be a prime. If
$$
|G|=p^a m,
\qquad p\nmid m,
$$
then a **Sylow $p$-subgroup** of $G$ is a subgroup $P\le G$ of order
$$
|P|=p^a.
$$
Thus it is a $p$-subgroup whose order is the largest power of $p$ dividing
$|G|$.

:::

:::

::: pf-step

Simple group.

::: pf-proof

A group $G$ is **simple** if
$$
G\ne1
$$
and its only normal subgroups are
$$
1\quad\text{and}\quad G.
$$

:::

:::

::: pf-step

Left group action.

::: pf-proof

A **left action** of a group $G$ on a set $S$ is a map
$$
G\times S\longrightarrow S,
\qquad
(g,s)\longmapsto g\cdot s,
$$
such that for all $g,h\in G$ and $s\in S$,
$$
1_G\cdot s=s
$$
and
$$
(gh)\cdot s=g\cdot(h\cdot s).
$$
Equivalently, it is a homomorphism
$$
G\longrightarrow\operatorname{Sym}(S).
$$

:::

:::

::: pf-step

Semidirect product determined by $c:H\to\operatorname{Aut}(K)$.

::: pf-proof

Given a homomorphism
$$
c:H\longrightarrow\operatorname{Aut}(K),
$$
the semidirect product
$$
K\rtimes_c H
$$
is the set $K\times H$ with multiplication
$$
\boxed{
(k,h)(k',h')
=\bigl(k\,c(h)(k'),\,hh'\bigr).}
$$
Its identity is $(1_K,1_H)$, and
$$
(k,h)^{-1}
=\bigl(c(h^{-1})(k^{-1}),h^{-1}\bigr).
$$
Under the embeddings
$$
K\hookrightarrow K\rtimes_cH,
\quad k\mapsto(k,1),
$$
and
$$
H\hookrightarrow K\rtimes_cH,
\quad h\mapsto(1,h),
$$
the subgroup $K$ is normal and conjugation by $h$ acts on it by the
automorphism $c(h)$.

:::

:::

:::

:::
