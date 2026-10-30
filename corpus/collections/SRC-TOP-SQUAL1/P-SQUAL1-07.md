---
schema: qual/card@1
id: P-SQUAL1-07
kind: problem
title: Two nonconjugate index-$4$ subgroups of the free group on two generators
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Use covering-space theory to find two nonconjugate subgroups of index $4$ in the free group
$$F(a,b)$$
on two generators.
:::

::: {.solution}

Let
$$
X=S^1_a\vee S^1_b
$$
be the wedge of two circles, with basepoint at the wedge point. Then
$$
\pi_1(X)\cong F(a,b).
$$

## First $4$-sheeted cover

Define
$$
\phi_1:F(a,b)\to C_4=\ZZ/4
$$
by
$$
\boxed{
\phi_1(a)=1,\qquad
\phi_1(b)=0}.
$$

::: pf

::: pf-step

The homomorphism $\phi_1$ is surjective.


::: pf-proof

The element $1\in\ZZ/4$ generates $C_4$, and it is the image of $a$.

:::

:::

::: {.pf-step #s1-2}

Let
$$
\boxed{H_1=\ker\phi_1}.
$$
Then
$$
\boxed{[F(a,b):H_1]=4}.
$$


::: pf-proof

By the first isomorphism theorem,
$$
F(a,b)/H_1
\cong
C_4.
$$
Thus the index equals $\cardinality{C_4}=4$.

:::

:::

::: {.pf-step #s1-3}

The subgroup $H_1$ corresponds to a connected regular $4$-sheeted cover
$$
p_1:Y_1\to X
$$
whose deck group is
$$
\boxed{\operatorname{Deck}(p_1)\cong C_4}.
$$


::: pf-proof

Index-$4$ subgroups correspond to connected $4$-sheeted covers. Since $H_1$ is normal as a kernel, the cover is regular, and its deck group is
$$
F(a,b)/H_1\cong C_4.
$$

:::

:::

::: pf-step

Concretely, $Y_1$ has four vertices arranged cyclically by the lifts of the $a$-edge, while the lift of the $b$-edge is a loop at each vertex.


::: pf-proof

The fiber can be labeled by $C_4$. Traversing $a$ adds $1$, so the $a$-monodromy is a $4$-cycle. Traversing $b$ adds $0$, so the $b$-monodromy fixes every sheet.

:::

:::

::: pf-step

The homomorphism $\phi_2$ is surjective.


::: pf-proof

The two displayed images generate the two direct factors of
$$
C_2\times C_2.
$$

:::

:::

::: {.pf-step #s1-6}

Let
$$
\boxed{H_2=\ker\phi_2}.
$$
Then
$$
\boxed{[F(a,b):H_2]=4}.
$$


::: pf-proof

By the first isomorphism theorem,
$$
F(a,b)/H_2
\cong
C_2\times C_2,
$$
which has order $4$.

:::

:::

::: pf-step

The subgroup $H_2$ corresponds to a connected regular $4$-sheeted cover
$$
p_2:Y_2\to X
$$
whose deck group is
$$
\boxed{
\operatorname{Deck}(p_2)\cong C_2\times C_2}.
$$


::: pf-proof

As in step [](#s1-3){.pf-ref}, normality of the kernel gives a regular cover, and the deck group is the quotient
$$
F(a,b)/H_2.
$$

:::

:::

::: pf-step

Concretely, label the four sheets by
$$
C_2\times C_2.
$$
Then the $a$-edge flips the first coordinate and the $b$-edge flips the second.


::: pf-proof

The monodromy action is translation by
$$
\phi_2(a)=(1,0)
$$
or
$$
\phi_2(b)=(0,1),
$$
respectively.

:::

:::

::: {.pf-step #s1-9}

The two deck groups are not isomorphic:
$$
\boxed{
C_4\not\cong C_2\times C_2}.
$$


::: pf-proof

The group $C_4$ contains an element of order $4$, while every nonidentity element of $C_2\times C_2$ has order $2$.

:::

:::

::: {.pf-step #s1-10}

Therefore the connected covers $p_1$ and $p_2$ are not equivalent as unbased covering spaces of $X$.


::: pf-proof

Equivalent regular covers have isomorphic deck transformation groups. Step [](#s1-9){.pf-ref} rules this out.

:::

:::

::: {.pf-step #s1-11}

Conjugacy classes of subgroups of $\pi_1(X)$ correspond to equivalence classes of connected unbased covering spaces of $X$.


::: pf-proof

This is the standard classification theorem for connected covering spaces when the base is path connected, locally path connected, and semilocally simply connected; the wedge of two circles satisfies these hypotheses.

:::

:::

::: {.pf-step #s1-12}

Hence
$$
\boxed{
H_1\text{ and }H_2
\text{ are not conjugate in }F(a,b)}.
$$


::: pf-proof

If they were conjugate, the corresponding connected covers would be equivalent by step [](#s1-11){.pf-ref}, contradicting step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

One can also see directly that $H_1\ne H_2$.


::: pf-proof

Since
$$
\phi_1(b)=0,
$$
one has
$$
b\in H_1.
$$
But
$$
\phi_2(b)=(0,1)\ne(0,0),
$$
so
$$
b\notin H_2.
$$

:::

:::

::: {.pf-step #s1-14}

Since both $H_1$ and $H_2$ are normal, distinctness alone also implies nonconjugacy.


::: pf-proof

For a normal subgroup $H$,
$$
gHg^{-1}=H
$$
for every $g$. Thus two conjugate normal subgroups must be equal. Apply step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

Therefore
$$
\boxed{
H_1=\ker\phi_1,
\qquad
H_2=\ker\phi_2}
$$
are two nonconjugate subgroups of index $4$ in $F(a,b)$.


::: pf-proof

The index statements are steps [](#s1-2){.pf-ref} and [](#s1-6){.pf-ref}, and nonconjugacy is step [](#s1-12){.pf-ref} or step [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} gives the required pair of subgroups.

:::

:::

:::
