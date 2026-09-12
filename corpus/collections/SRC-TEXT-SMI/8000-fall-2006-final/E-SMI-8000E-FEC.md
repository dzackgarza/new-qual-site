---
schema: qual/card@1
id: E-SMI-8000E-FEC
kind: problem
title: Stating Sylow's theorem and Jordan-Hölder
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
  note: "Compared both theorem prompts and the proof-choice instruction with Smith 8000 Fall 2006 final part C."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Stated all three Sylow assertions and Jordan--Hoelder, then proved Sylow existence, containment/conjugacy, and the congruence/divisibility count without circularity."
---

::: {.exercise}
(i) State all 3 parts of Sylow's theorem.

(ii) State the Jordan-Hölder theorem.

(And prove one of them.)
:::

::: solution
Let
$$
|G|=p^a m,
\qquad p\nmid m.
$$

<1>1. State the three Sylow assertions.
::: proof
The **Sylow theorems** state:

1. **Existence.** $G$ has a subgroup of order $p^a$.
2. **Containment and conjugacy.** Every $p$-subgroup of $G$ is contained in a
   Sylow $p$-subgroup; all Sylow $p$-subgroups are conjugate in $G$.
3. **Number.** If $n_p$ is the number of Sylow $p$-subgroups, then
   $$
   n_p\equiv1\pmod p
   $$
   and
   $$
   n_p\mid m.
   $$
:::

<1>2. State the Jordan--Hoelder theorem.
::: proof
A **composition series** of a finite group is a subnormal series
$$
G=G_0\trianglerighteq G_1\trianglerighteq\cdots
\trianglerighteq G_r=1
$$
such that every quotient
$$
G_i/G_{i+1}
$$
is simple.

The **Jordan--Hoelder theorem** says that any two composition series of a
finite group have the same length, and after a permutation their composition
factors are pairwise isomorphic. Thus the multiset of simple composition
factors is an invariant of the group.
:::

We now prove the Sylow theorems.

<1>3. Prove existence of a subgroup of order $p^a$.
::: proof
Let $X$ be the set of all subsets of $G$ having exactly $p^a$ elements. The
group $G$ acts on $X$ by left translation.

First,
$$
|X|=\binom{p^a m}{p^a}.
$$
Modulo $p$,
$$
(1+t)^{p^a}
\equiv1+t^{p^a}\pmod p,
$$
so
$$
(1+t)^{p^am}
\equiv(1+t^{p^a})^m\pmod p.
$$
Comparing coefficients of $t^{p^a}$ gives
$$
\binom{p^am}{p^a}\equiv m\not\equiv0\pmod p.
$$
Thus the total number of points in $X$ is not divisible by $p$.

The $G$-orbits partition $X$, so at least one orbit has size not divisible by
$p$. Choose $A\in X$ in such an orbit and let
$$
H=\operatorname{Stab}_G(A).
$$
By orbit--stabilizer,
$$
[G:H]=|G\cdot A|
$$
is not divisible by $p$. Hence the full factor $p^a$ in $|G|$ divides
$|H|$.

On the other hand, $H$ acts freely on $A$ by left multiplication: if
$ha=a$ for some $a\in A$, then $h=1$. Therefore every $H$-orbit in $A$ has
size $|H|$, so
$$
|H|\mid|A|=p^a.
$$
Combining the two divisibilities gives
$$
|H|=p^a.
$$
Thus $H$ is a Sylow $p$-subgroup.
:::

<1>4. Prove containment of arbitrary $p$-subgroups and conjugacy of Sylow subgroups.
::: proof
Fix a Sylow $p$-subgroup $P$ supplied by step <1>3, and let $Q\le G$ be any
$p$-subgroup. Let $Q$ act by left multiplication on the set of left cosets
$$
G/P.
$$
This set has
$$
[G:P]=m
$$
elements, not divisible by $p$. Every $Q$-orbit has size a power of $p$.
Therefore at least one orbit has size one. Thus there is a coset $gP$ fixed
by all of $Q$:
$$
qgP=gP
\qquad(q\in Q).
$$
Equivalently,
$$
g^{-1}Qg\le P,
$$
so
$$
Q\le gPg^{-1}.
$$
Hence every $p$-subgroup is contained in a Sylow $p$-subgroup.

If $Q$ itself is Sylow, then $Q$ and $gPg^{-1}$ both have order $p^a$, so
the containment is equality. Hence all Sylow $p$-subgroups are conjugate.
:::

<1>5. Prove the congruence and divisibility conditions on the number of Sylow subgroups.
::: proof
Let $\mathcal S$ be the set of Sylow $p$-subgroups and let $P\in\mathcal S$.
The group $P$ acts on $\mathcal S$ by conjugation.

We claim $P$ is the only fixed point. Certainly $P$ fixes itself. If
$Q\in\mathcal S$ is fixed by $P$, then
$$
P\le N_G(Q).
$$
Since $Q\trianglelefteq N_G(Q)$, the product $PQ$ is a subgroup of
$N_G(Q)$. It is a $p$-group, so maximality of the Sylow subgroup $Q$ forces
$$
PQ=Q,
$$
and hence $P=Q$.

Thus the conjugation action of $P$ has exactly one orbit of size one, and all
other orbit sizes are positive powers of $p$. Consequently
$$
\boxed{n_p\equiv1\pmod p.}
$$

By conjugacy, $G$ acts transitively on $\mathcal S$, and the stabilizer of
$P$ is its normalizer. Hence
$$
n_p=[G:N_G(P)].
$$
Since $P\le N_G(P)$, write
$$
|N_G(P)|=p^a d
$$
with $d\mid m$. Then
$$
n_p=\frac{p^am}{p^ad}=\frac md,
$$
so
$$
\boxed{n_p\mid m.}
$$
This completes the proof of all three Sylow assertions.
:::
:::
