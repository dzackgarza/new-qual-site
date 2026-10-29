---
schema: qual/card@1
id: P-WESTOP09-I3
kind: problem
title: Characterize spaces embeddable in products of unit intervals
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $I=[0,1]$. Characterize exactly the topological spaces that can be obtained as subspaces of possibly infinite products of copies of $I$. Give an explanation of the characterization, though a complete proof is not required.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The spaces that occur as subspaces of products of copies of $I$ are
exactly the
$$
\boxed{\text{completely regular Hausdorff spaces}}
$$
also called Tychonoff spaces.


::: pf-proof

The remaining steps prove both directions of this characterization.

:::

:::

::: {.pf-step #s1-2}

Every subspace of a product of copies of $I$ is completely regular and
Hausdorff.


::: pf-proof

The interval $I$ is a metric space, hence completely regular and Hausdorff.
Arbitrary products of completely regular Hausdorff spaces are completely
regular and Hausdorff, and these two properties pass to subspaces. Therefore
every subspace of a power
$$
I^J
$$
is completely regular and Hausdorff.

:::

:::

::: {.pf-step #s1-3}

Let $X$ be completely regular and Hausdorff, and put
$$
\mathcal F=C(X,I).
$$
The evaluation map
$$
e:X\longrightarrow I^{\mathcal F},
\qquad
e(x)=(f(x))_{f\in\mathcal F},
$$
is continuous and injective.


::: pf-proof

For each $f\in\mathcal F$, the coordinate projection
$$
\pi_f:I^{\mathcal F}\to I
$$
satisfies
$$
\pi_f\circ e=f.
$$
Since every coordinate of $e$ is continuous, the universal property of the
product topology implies that $e$ is continuous.

To prove injectivity, let $x\ne y$. Since $X$ is Hausdorff, $\{y\}$ is
closed. Complete regularity gives a continuous map $f:X\to I$ such that, for
example,
$$
f(x)=0,\qquad f(y)=1.
$$
Thus the $f$-coordinates of $e(x)$ and $e(y)$ differ, so $e(x)\ne e(y)$.

:::

:::

::: {.pf-step #s1-4}

The evaluation map $e$ is a topological embedding.


::: pf-proof

It remains to show that the topology on $X$ is the topology induced from
$e(X)$. Let $U\subseteq X$ be open and let $x\in U$. Set
$$
F=X\setminus U.
$$
The set $F$ is closed and does not contain $x$. By complete regularity there
is $f\in C(X,I)$ such that
$$
f(x)=0,
\qquad
f(F)=\{1\}.
$$
Then
$$
W=\{p\in I^{\mathcal F}:\pi_f(p)<1/2\}
$$
is product-open,
$$
x\in e^{-1}(W),
$$
and
$$
e^{-1}(W)\subseteq U.
$$
Hence every open neighborhood in $X$ contains the inverse image under $e$ of
a product-open neighborhood. Since $e$ is already continuous by step [](#s1-3){.pf-ref},
the original topology on $X$ agrees with the topology pulled back from
$e(X)$. Thus $e:X\to e(X)$ is a homeomorphism.

:::

:::

::: {.pf-step #s1-5}

Every completely regular Hausdorff space is therefore a subspace of a
possibly infinite product of copies of $I$.


::: pf-proof

For such an $X$, step [](#s1-4){.pf-ref} embeds $X$ into the power
$$
I^{C(X,I)}.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves one direction and step [](#s1-5){.pf-ref} proves the converse, establishing
the characterization in step [](#s1-1){.pf-ref}.

:::

:::

:::
