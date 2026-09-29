---
schema: qual/card@1
id: P-BKF08-7A
kind: problem
title: Products of pairwise trivially intersecting normal subgroups
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked that normality forces H_1 and H_2 to commute when their
    intersection is trivial, and checked the elementary-abelian
    counterexamples for every k at least 3.
---

::: {.problem}
Suppose $H_i$ is a normal subgroup of a group $G$ for $1\le i\le k$, and $H_i\cap H_j=\{1\}$ whenever $i\ne j$.
Prove that $G$ contains a subgroup isomorphic to
$$
H_1\times H_2\times\cdots\times H_k
$$
if $k=2$, but not necessarily if $k\ge3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $k=2$, every element of $H_1$ commutes with every element of
$H_2$.

::: pf-proof

Let $h_1\in H_1$ and $h_2\in H_2$. Since $H_2\triangleleft G$,
$$
h_1h_2h_1^{-1}\in H_2,
$$
and therefore the commutator
$$
[h_1,h_2]
=h_1h_2h_1^{-1}h_2^{-1}
$$
lies in $H_2$. Since $H_1\triangleleft G$,
$h_2h_1^{-1}h_2^{-1}\in H_1$, and multiplying by $h_1\in H_1$ shows
that the same commutator lies in $H_1$. Hence
$$
[h_1,h_2]\in H_1\cap H_2=\{1\}.
$$
Thus $[h_1,h_2]=1$, so $h_1h_2=h_2h_1$.

:::

:::

::: {.pf-step #s2}

If $k=2$, the multiplication map
$$
\mu\colon H_1\times H_2\longrightarrow G,
\qquad
\mu(h_1,h_2)=h_1h_2,
$$
is an injective homomorphism.

::: pf-proof

By step [](#s1){.pf-ref}, elements of $H_1$ commute with elements of $H_2$. Hence
for $h_i,h_i'\in H_i$,
$$
\begin{aligned}
\mu(h_1,h_2)\mu(h_1',h_2')
&=h_1h_2h_1'h_2'\\
&=h_1h_1'h_2h_2'\\
&=\mu(h_1h_1',h_2h_2'),
\end{aligned}
$$
so $\mu$ is a homomorphism.

If $\mu(h_1,h_2)=1$, then $h_1=h_2^{-1}$. Thus
$h_1\in H_1\cap H_2=\{1\}$, and consequently $h_1=h_2=1$. The kernel
of $\mu$ is therefore trivial, so $\mu$ is injective.

:::

:::

::: {.pf-step #s3}

Consequently, when $k=2$, the subgroup $H_1H_2\le G$ is
isomorphic to $H_1\times H_2$.

::: pf-proof

The image of the homomorphism $\mu$ from step [](#s2){.pf-ref} is precisely
$H_1H_2$. Since $\mu$ is injective, it identifies $H_1\times H_2$ with
that subgroup of $G$.

:::

:::

::: {.pf-step #s4}

For every $k\ge3$, there are normal subgroups satisfying the
hypotheses for which the direct-product conclusion fails.

::: pf-proof

Let
$$
G=(\ZZ/2\ZZ)^{k-1}
$$
with standard basis $e_1,\ldots,e_{k-1}$, and use additive notation. Set
$$
H_i=\langle e_i\rangle
\quad(1\le i\le k-1),
\qquad
H_k=\langle e_1+\cdots+e_{k-1}\rangle.
$$
The group $G$ is abelian, so all the $H_i$ are normal. Each has order
$2$. They are distinct: the first $k-1$ are distinct coordinate lines,
and since $k-1\ge2$, the generator of $H_k$ has at least two nonzero
coordinates and hence lies in none of those coordinate lines. Distinct
subgroups of order $2$ intersect only in the identity $0$.

On the other hand,
$$
\abs{H_1\times\cdots\times H_k}=2^k,
$$
whereas $\abs{G}=2^{k-1}$. Therefore no subgroup of $G$ can be
isomorphic to $H_1\times\cdots\times H_k$.

:::

:::

::: {.pf-step #s5}

Thus the direct-product subgroup always exists for $k=2$, whereas
for every $k\ge3$ the conclusion need not hold.

::: pf-proof

Step [](#s3){.pf-ref} proves the assertion for $k=2$, and step [](#s4){.pf-ref} supplies a
counterexample for every $k\ge3$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives both requested conclusions.

:::

:::

:::
