---
schema: qual/card@1
id: E-SMI-8000E-SY10
kind: problem
title: Subgroups of every $p$-power order dividing a finite group
classification:
  areas:
  - algebra
  topics:
  - Sylow Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement and hint with Smith 8000e Sylow problem 10."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Reduced to a Sylow p-subgroup, then proved by induction that a finite p-group has subgroups of every intermediate p-power order using a central subgroup of order p and passage to the quotient."
---

::: {.exercise}
Prove that if $G$ is a finite group such that $p^s$ divides $\#G$, then $G$ has a subgroup of order $p^s$.

[Hint: use induction, and the fact that the center of a group of order $p^r$ is nontrivial.]
:::

::: {.solution}
Write
$$
|G|=p^r m,
\qquad p\nmid m,
$$
so the hypothesis $p^s\mid |G|$ says $s\le r$.

By the Sylow existence theorem, $G$ has a Sylow $p$-subgroup $P$ of order
$p^r$. It is therefore enough to prove the following lemma.

<1>1. Every finite $p$-group of order $p^r$ has a subgroup of order $p^s$ for every $0\le s\le r$.
::: {.proof}
We induct on $r$.

For $r=0$, the group is trivial and there is nothing to prove. Assume
$r>0$ and let $P$ be a group of order $p^r$. A finite $p$-group has
nontrivial center, so
$$
Z(P)\ne1.
$$
Choose $z\in Z(P)$ with $z\ne1$. Since the order of $z$ is a positive
power of $p$, say $p^a$, the element
$$
z^{p^{a-1}}
$$
has order $p$. Hence $P$ has a central subgroup
$$
C\le Z(P),
\qquad |C|=p.
$$

The quotient $P/C$ is a $p$-group of order $p^{r-1}$. Fix
$s$ with $1\le s\le r$. By the induction hypothesis applied to $P/C$,
there is a subgroup
$$
\overline H\le P/C
$$
of order $p^{s-1}$. Let
$$
\pi:P\longrightarrow P/C
$$
be the quotient map and set
$$
H=\pi^{-1}(\overline H).
$$
Then $C\le H$ and
$$
H/C\cong\overline H.
$$
Therefore
$$
|H|=|C|\,|H/C|
=p\cdot p^{s-1}
=p^s.
$$

For $s=0$, take the trivial subgroup. This proves the lemma for all
$0\le s\le r$.
:::

<1>2. Apply the lemma inside a Sylow subgroup of $G$.
::: {.proof}
The Sylow subgroup $P\le G$ has order $p^r$. Since $s\le r$, step <1>1
gives a subgroup
$$
H\le P
$$
with
$$
|H|=p^s.
$$
Because $P\le G$, the same $H$ is a subgroup of $G$. Hence
$$
\boxed{p^s\mid |G|\quad\Longrightarrow\quad
\text{$G$ has a subgroup of order $p^s$.}}
$$
:::
:::
