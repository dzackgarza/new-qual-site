---
schema: qual/card@1
id: P-WESTOP04-10
kind: problem
title: Axiom of Choice and one of its standard equivalent maximality principles
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
The source lists five familiar principles equivalent to the Axiom of Choice: Zorn's Lemma, Tukey's Lemma, the well-ordering principle, the Hausdorff maximality principle, and König's Theorem.

1. State the Axiom of Choice and any two of those five principles.
2. Choose one of the five principles, call it $P$, and prove either
   $$
   \mathrm{AC}\Longrightarrow P
   $$
   or
   $$
   P\Longrightarrow\mathrm{AC}.
   $$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Axiom of Choice states:

For every family
$$
\mathcal A
$$
of nonempty sets, there exists a function
$$
c:\mathcal A\to\bigcup\mathcal A
$$
such that
$$
c(A)\in A
$$
for every
$$
A\in\mathcal A.
$$


::: pf-proof

Such a function is called a choice function for
$$
\mathcal A.
$$
This is the standard formulation of the Axiom of Choice.

:::

:::

::: {.pf-step #s1-2}

Zorn's Lemma states:

If
$$
(P,\le)
$$
is a partially ordered set such that every chain in
$$
P
$$
has an upper bound in
$$
P,
$$
then
$$
P
$$
has a maximal element.


::: pf-proof

This is the standard statement of Zorn's Lemma.

:::

:::

::: {.pf-step #s1-3}

The well-ordering principle states:

$$
\boxed{
\text{Every set admits a well-ordering.}}
$$


::: pf-proof

A well-ordering is a total order under which every nonempty subset has a least element. The assertion that every set can be so ordered is the well-ordering principle.

:::

:::

::: {.pf-step #s1-4}

Assume Zorn's Lemma. Let
$$
\mathcal A
$$
be an arbitrary family of nonempty sets.


::: pf-proof

To prove the Axiom of Choice from Zorn's Lemma, it is enough to construct a choice function for this arbitrary family.

:::

:::

::: {.pf-step #s1-5}

Let
$$
P
$$
be the set of all partial choice functions on
$$
\mathcal A.
$$
Thus an element of
$$
P
$$
is a function
$$
f:\mathcal D_f\to\bigcup\mathcal A,
$$
where
$$
\mathcal D_f\subseteq\mathcal A
$$
and
$$
f(A)\in A
$$
for every
$$
A\in\mathcal D_f.
$$
Order
$$
P
$$
by extension:
$$
f\le g
\iff
g\restrict_{\mathcal D_f}=f.
$$


::: pf-proof

The empty function belongs to
$$
P,
$$
so
$$
P
$$
is nonempty. The extension relation is reflexive, antisymmetric, and transitive, hence a partial order.

:::

:::

::: {.pf-step #s1-6}

Every chain in
$$
P
$$
has an upper bound in
$$
P.
$$


::: pf-proof

Let
$$
\mathcal C\subseteq P
$$
be a chain. Define
$$
f
\coloneqq
\bigcup_{g\in\mathcal C}g.
$$
Because
$$
\mathcal C
$$
is linearly ordered by extension, any two functions in the chain agree wherever both are defined. Hence their union is a function.

Its domain is
$$
\mathcal D_f
=
\bigcup_{g\in\mathcal C}\mathcal D_g
\subseteq
\mathcal A.
$$
If
$$
A\in\mathcal D_f,
$$
then
$$
A\in\mathcal D_g
$$
for some
$$
g\in\mathcal C,
$$
and therefore
$$
f(A)
=
g(A)
\in
A.
$$
Thus
$$
f\in P.
$$
By construction every
$$
g\in\mathcal C
$$
is extended by
$$
f,
$$
so
$$
f
$$
is an upper bound.

:::

:::

::: {.pf-step #s1-7}

By Zorn's Lemma,
$$
P
$$
has a maximal element
$$
f_{\max}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} verifies the hypothesis of Zorn's Lemma for the partially ordered set
$$
P.
$$

:::

:::

::: {.pf-step #s1-8}

The domain of
$$
f_{\max}
$$
is all of
$$
\mathcal A.
$$


::: pf-proof

Suppose instead that there is some
$$
A_0
\in
\mathcal A\setminus\mathcal D_{f_{\max}}.
$$
The set
$$
A_0
$$
is nonempty, so choose one element
$$
a_0\in A_0.
$$
Define
$$
g
=
f_{\max}
\cup
\{
(A_0,a_0)
\}.
$$
Since
$$
A_0
$$
was not already in the domain, this is a function. It is a partial choice function and strictly extends
$$
f_{\max},
$$
contradicting maximality.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
f_{\max}
$$
is a choice function for
$$
\mathcal A.
$$


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
\mathcal D_{f_{\max}}
=
\mathcal A.
$$
By the definition of
$$
P,
$$
one has
$$
f_{\max}(A)\in A
$$
for every
$$
A\in\mathcal A.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\text{Zorn's Lemma}
\Longrightarrow
\mathrm{AC}.}
$$


::: pf-proof

The family
$$
\mathcal A
$$
was arbitrary. Step [](#s1-9){.pf-ref} constructs a choice function for every family of nonempty sets, which is exactly the Axiom of Choice.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} state AC and two of the listed equivalent principles, and steps [](#s1-4){.pf-ref} through [](#s1-10){.pf-ref} prove one required implication.

:::

:::

:::
