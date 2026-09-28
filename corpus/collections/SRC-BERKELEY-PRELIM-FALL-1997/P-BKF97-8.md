---
schema: qual/card@1
id: P-BKF97-8
kind: problem
title: Pairwise trivially intersecting normal subgroups and direct products
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    For two normal subgroups, cross-commutators lie in their trivial
    intersection, so the product subgroup is their direct product. For every
    k>=3, used k distinct order-two subgroups of (C_2)^(k-1) as a size
    obstruction.
---

::: {.problem}
Suppose $H_i\trianglelefteq G$ for $1\le i\le k$ and
\[
H_i\cap H_j=\{1\}
\qquad(i\ne j).
\]
Prove that when $k=2$, the group $G$ contains a subgroup isomorphic to
\[
H_1\times H_2,
\]
but that this conclusion need not hold for $k\ge3$.
:::

::: {.solution}
<1>1. If $x\in H_1$ and $y\in H_2$, then the commutator
$$
[x,y]
\coloneqq
xyx^{-1}y^{-1}
$$
lies in
$$
H_1\cap H_2.
$$

::: {.proof}
Since $H_1\trianglelefteq G$,
$$
yx^{-1}y^{-1}\in H_1,
$$
so
$$
[x,y]
=
x(yx^{-1}y^{-1})
\in H_1.
$$
Since $H_2\trianglelefteq G$,
$$
xyx^{-1}\in H_2,
$$
so
$$
[x,y]
=
(xyx^{-1})y^{-1}
\in H_2.
$$
Thus the commutator lies in both subgroups.
:::

<1>2. When $k=2$, the subgroups $H_1$ and $H_2$ commute elementwise.

::: {.proof}
By hypothesis,
$$
H_1\cap H_2=\{1\}.
$$
Step <1>1 therefore gives
$$
[x,y]=1
$$
for every $x\in H_1$ and $y\in H_2$. This is equivalent to
$$
xy=yx.
$$
:::

<1>3. When $k=2$, the set
$$
H_1H_2
\coloneqq
\{h_1h_2:h_1\in H_1,\ h_2\in H_2\}
$$
is a subgroup of $G$.

::: {.proof}
For
$$
h_1,h_1'\in H_1,
\qquad
h_2,h_2'\in H_2,
$$
step <1>2 gives
$$
(h_1h_2)(h_1'h_2')
=
h_1h_1'h_2h_2'
\in H_1H_2.
$$
Also
$$
(h_1h_2)^{-1}
=
h_2^{-1}h_1^{-1}
=
h_1^{-1}h_2^{-1}
\in H_1H_2.
$$
Thus $H_1H_2$ is a subgroup.
:::

<1>4. The map
$$
\mu:H_1\times H_2\longrightarrow H_1H_2,
\qquad
\mu(h_1,h_2)=h_1h_2
$$
is an isomorphism.

::: {.proof}
Step <1>2 implies
$$
\begin{aligned}
\mu(h_1,h_2)\mu(h_1',h_2')
&=
h_1h_2h_1'h_2'\\
&=
h_1h_1'h_2h_2'\\
&=
\mu(h_1h_1',h_2h_2'),
\end{aligned}
$$
so $\mu$ is a homomorphism. It is surjective by the definition of
$H_1H_2$.

If
$$
\mu(h_1,h_2)=1,
$$
then
$$
h_1=h_2^{-1}\in H_1\cap H_2=\{1\}.
$$
Thus $h_1=h_2=1$, so the kernel is trivial. Hence $\mu$ is an isomorphism.
:::

<1>5. Therefore, for $k=2$, the group $G$ contains a subgroup isomorphic
to
$$
H_1\times H_2.
$$

::: {.proof}
Take the subgroup $H_1H_2$ from step <1>3 and apply the isomorphism in
step <1>4.
:::

<1>6. Fix any integer $k\geq3$ and let
$$
G=(C_2)^{k-1}.
$$
Then $G$ contains at least $k$ distinct subgroups of order $2$.

::: {.proof}
Regard $G$ as the additive group of the vector space
$$
\FF_2^{\,k-1}.
$$
Every nonzero vector generates a subgroup of order $2$, and over $\FF_2$
two nonzero vectors generate the same one-dimensional subspace only when
they are equal. Hence $G$ has
$$
2^{k-1}-1
$$
distinct subgroups of order $2$. For $k\geq3$,
$$
2^{k-1}-1\geq k.
$$
Choose any $k$ of them and call them
$$
H_1,\ldots,H_k.
$$
:::

<1>7. The subgroups from step <1>6 are normal and pairwise intersect
trivially.

::: {.proof}
The group $G$ is abelian, so every subgroup is normal. Two distinct
subgroups of order $2$ can share no nonidentity element, because the unique
nonidentity element determines such a subgroup. Therefore
$$
H_i\cap H_j=\{1\}
$$
whenever $i\neq j$.
:::

<1>8. The group $G$ from step <1>6 cannot contain a subgroup isomorphic to
$$
H_1\times\cdots\times H_k.
$$

::: {.proof}
Each $H_i$ has order $2$, so
$$
\abs{H_1\times\cdots\times H_k}
=
2^k.
$$
But
$$
\abs G
=
2^{k-1}.
$$
No subgroup of a finite group can have order larger than the group itself.
Thus the displayed direct product cannot occur as a subgroup of $G$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>5 proves the assertion for $k=2$, while steps <1>6--<1>8 give a
counterexample for every $k\geq3$.
:::
:::
