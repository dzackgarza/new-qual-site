---
schema: qual/card@1
id: P-HGRO37
kind: problem
title: Outline the proof of the Jordan-Dickson theorem
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction; theorem identification independently checked against standard references for the Jordan--Dickson simplicity theorem.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
State the Jordan-Dickson theorem and outline its proof.
:::

::: solution
Let $q$ be a prime power and $n\ge2$.

**Jordan--Dickson theorem.** The projective special linear group
\[
PSL_n(q)=SL_n(q)/Z(SL_n(q))
\]
is simple, except for
\[
PSL_2(2)\cong S_3
\qquad\text{and}\qquad
PSL_2(3)\cong A_4.
\]

Equivalently, if $N\trianglelefteq SL_n(q)$ is not contained in the center, then
$N=SL_n(q)$, apart from the two exceptional pairs $(n,q)=(2,2),(2,3)$.

<1>1. Reduce a noncentral normal subgroup to a subgroup containing a nontrivial
transvection.
::: proof
Let $N\trianglelefteq SL_n(q)$ contain a noncentral element $A$. One studies
commutators of $A$ with elementary transvections
\[
t_{ij}(a)=I+aE_{ij}.
\]
Because $N$ is normal, every such commutator lies in $N$. By choosing indices
for which $A$ does not act as a scalar and performing elementary row/column
reductions, these commutators can be arranged to produce a nontrivial
transvection in $N$.

For $n=2$, the same reduction is carried out directly with $2\times2$ matrices;
the very small fields $\mathbb F_2$ and $\mathbb F_3$ are exactly where the
argument fails and yield the two exceptions.
:::

<1>2. A normal subgroup containing one nontrivial transvection contains all
elementary transvections.
::: proof
Conjugating by permutation and diagonal matrices in $SL_n(q)$ moves a
transvection between coordinate pairs and changes its parameter. Commutator
relations among elementary matrices then give
\[
[t_{ij}(a),t_{jk}(b)]=t_{ik}(ab)
\]
for distinct $i,j,k$, and
\[
t_{ij}(a)t_{ij}(b)=t_{ij}(a+b).
\]
Normality therefore propagates one nontrivial transvection to the full family
of elementary transvections required to generate $SL_n(q)$.
:::

<1>3. The elementary transvections generate $SL_n(q)$.
::: proof
Gaussian elimination expresses every determinant-one matrix as a product of
elementary matrices. Hence a normal subgroup containing all elementary
transvections is the whole group $SL_n(q)$.
:::

<1>4. Therefore every proper normal subgroup of $SL_n(q)$ is central, outside
the two exceptional cases.
::: proof
If a normal subgroup is not central, <1>1 gives a nontrivial transvection,
<1>2 gives all elementary transvections, and <1>3 gives the whole group.
Quotienting by the center therefore leaves no nontrivial proper normal subgroup
in $PSL_n(q)$.

Finally,
\[
PSL_2(2)\cong S_3
\quad\text{and}\quad
PSL_2(3)\cong A_4,
\]
and neither group is simple.
:::
:::
