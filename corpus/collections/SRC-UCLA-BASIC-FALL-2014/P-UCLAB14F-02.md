---
schema: qual/card@1
id: P-UCLAB14F-02
kind: problem
title: Connectedness from a connected union and intersection
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 2. Let $A,B$ be two closed subsets of $\RR^n$ such that $A\cup B$ and $A\cap B$ are connected. Prove that $A$ is connected.
:::

::: {.solution}

::: pf

::: pf-step

Suppose, for contradiction, that $A$ is disconnected.


::: pf-proof

Then there exist nonempty disjoint subsets
\[
U,V\subseteq A
\]
such that
\[
A=U\cup V
\]
and both $U$ and $V$ are open and closed in the subspace topology on $A$.

:::

:::

::: pf-step

Since $A\cap B$ is connected,
\[
A\cap B
\]
is contained entirely in one of $U$ or $V$.


::: pf-proof

The sets
\[
(A\cap B)\cap U
\qquad\text{and}\qquad
(A\cap B)\cap V
\]
are disjoint, relatively open and relatively closed subsets of $A\cap B$, and their union is $A\cap B$.
Connectedness therefore forces one of them to be empty.
Thus $A\cap B$ lies entirely in the other.

:::

:::

::: {.pf-step #s1-3}

After exchanging $U$ and $V$ if necessary, assume
\[
A\cap B\subseteq U.
\]
Then
\[
V\cap B=\varnothing.
\]


::: pf-proof

If $v\in V\cap B$, then $v\in A\cap B$, hence $v\in U$ by the assumption.
But $U\cap V=\varnothing$.
Thus no such $v$ exists.

:::

:::

::: {.pf-step #s1-4}

The set $V$ is closed in $A\cup B$.


::: pf-proof

The set $V$ is closed in $A$.
Since $A$ is closed in $\RR^n$, it is also closed in the subspace $A\cup B$.
A subset closed in a closed subspace is closed in the ambient subspace.
Hence $V$ is closed in $A\cup B$.

:::

:::

::: {.pf-step #s1-5}

The complement of $V$ in $A\cup B$ is
\[
(A\cup B)\setminus V
=
U\cup B,
\]
and this set is closed in $A\cup B$.


::: pf-proof

Because
\[
A=U\cup V
\]
and $V\cap B=\varnothing$ by step [](#s1-3){.pf-ref},
\[
(A\cup B)\setminus V=U\cup B.
\]

The set $U$ is closed in $A$, hence closed in $A\cup B$ because $A$ is closed there.
The set $B$ is closed in $\RR^n$, hence closed in $A\cup B$.
Therefore their finite union $U\cup B$ is closed in $A\cup B$.

:::

:::

::: {.pf-step #s1-6}

The set $V$ is both open and closed in $A\cup B$.


::: pf-proof

Step [](#s1-4){.pf-ref} gives that $V$ is closed.
Step [](#s1-5){.pf-ref} gives that its complement in $A\cup B$ is closed, so $V$ is open.

:::

:::

::: {.pf-step #s1-7}

The set $V$ is a nonempty proper subset of $A\cup B$.


::: pf-proof

It is nonempty by the assumed disconnection of $A$.
It is proper because $U$ is nonempty and
\[
U\subseteq(A\cup B)\setminus V.
\]

:::

:::

::: {.pf-step #s1-8}

Steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} contradict connectedness of $A\cup B$.


::: pf-proof

A connected space has no nonempty proper subset that is both open and closed.
But $V$ has exactly these properties.

:::

:::

::: {.pf-step #s1-9}

Therefore
\[
\boxed{A\text{ is connected}.}
\]


::: pf-proof

The assumption that $A$ is disconnected leads to the contradiction in step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
