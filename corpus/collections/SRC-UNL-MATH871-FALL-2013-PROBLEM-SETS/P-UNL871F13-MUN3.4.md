---
schema: qual/card@1
id: P-UNL871F13-MUN3.4
kind: problem
title: Quotient a set by the fibers of a surjection
classification:
  areas: [topology]
  topics: [Equivalence Relations]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: The Math 871 packet assigns Munkres 3.4. The local Munkres corpus omits Section 3; the assigned exercise statement was independently recovered as the standard surjection/fiber equivalence-relation exercise.
---

::: {.problem}
Let $f:A\to B$ be a surjective function.
Define a relation on $A$ by
\[
a_0\sim a_1\quad\Longleftrightarrow\quad f(a_0)=f(a_1).
\]

1. Show that $\sim$ is an equivalence relation.

2. Let $A^*$ be the set of equivalence classes.
   Show that there is a bijective correspondence between $A^*$ and $B$.
:::

::: pf

::: pf-step

The relation $\sim$ is reflexive.


::: pf-proof

For every
\[
a\in A,
\]
one has
\[
f(a)=f(a).
\]
Hence
\[
a\sim a.
\]

:::

:::

::: pf-step

The relation $\sim$ is symmetric.


::: pf-proof

Suppose
\[
a_0\sim a_1.
\]
Then
\[
f(a_0)=f(a_1).
\]
By symmetry of equality,
\[
f(a_1)=f(a_0),
\]
so
\[
a_1\sim a_0.
\]

:::

:::

::: pf-step

The relation $\sim$ is transitive.


::: pf-proof

Suppose
\[
a_0\sim a_1
\qquad\text{and}\qquad
a_1\sim a_2.
\]
Then
\[
f(a_0)=f(a_1)
\]
and
\[
f(a_1)=f(a_2).
\]
Therefore
\[
f(a_0)=f(a_2),
\]
so
\[
a_0\sim a_2.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\sim
\text{ is an equivalence relation on }A.
}
\]


::: pf-proof

Steps <1>1--<1>3 verify reflexivity, symmetry, and transitivity.

:::

:::

::: pf-step

Define
\[
\Phi:A^*\to B
\]
by
\[
\boxed{
\Phi([a])
=
f(a).
}
\]


::: pf-proof

Here
\[
[a]
\]
denotes the equivalence class of $a$.
The next step verifies that the displayed rule does not depend on the chosen
representative.

:::

:::

::: pf-step

The map $\Phi$ is well defined.


::: pf-proof

Suppose
\[
[a]=[a'].
\]
Then
\[
a\sim a'.
\]
By definition of the relation,
\[
f(a)=f(a').
\]
Therefore
\[
\Phi([a])
=
f(a)
=
f(a')
=
\Phi([a']).
\]

:::

:::

::: pf-step

The map $\Phi$ is injective.


::: pf-proof

Suppose
\[
\Phi([a_0])
=
\Phi([a_1]).
\]
Then
\[
f(a_0)=f(a_1).
\]
Hence
\[
a_0\sim a_1,
\]
so
\[
[a_0]=[a_1].
\]
Thus $\Phi$ is injective.

:::

:::

::: pf-step

The map $\Phi$ is surjective.


::: pf-proof

Let
\[
b\in B.
\]
Since
\[
f:A\to B
\]
is surjective, there exists
\[
a\in A
\]
such that
\[
f(a)=b.
\]
Then
\[
\Phi([a])
=
b.
\]
Thus every element of $B$ is in the image.

:::

:::

::: pf-step

Therefore
\[
\boxed{
A^*
\xrightarrow[\ [a]\mapsto f(a)\ ]{\cong}
B
}
\]
is a bijection.


::: pf-proof

Steps <1>6--<1>8 show that $\Phi$ is a well-defined bijection.

:::

:::

::: pf-qed

Step <1>4 proves part (1), and step <1>9 proves part (2).

:::

:::
