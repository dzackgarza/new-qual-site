---
schema: qual/card@1
id: P-UCLAB18F-02
kind: problem
title: Adjoining a separated complementary component preserves connectedness
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $A\subset\RR^n$ be connected and suppose
\[
\RR^n\setminus A=B\cup C,
\]
where $B,C$ are separated, meaning
\[
\overline B\cap C=B\cap\overline C=\varnothing.
\]
Show that $A\cup B$ is connected.
:::

::: {.solution}

Suppose, for contradiction, that
\[
A\cup B
\]
is disconnected.

::: pf

::: {.pf-step #s1-1}

There exist nonempty separated sets
\[
U,V\subseteq A\cup B
\]
such that
\[
A\cup B=U\cup V.
\]


::: pf-proof

This is the definition of disconnectedness: a space is disconnected exactly when it is the union of two nonempty separated subsets.
Here separated means
\[
\overline U^{\,A\cup B}\cap V
=
U\cap\overline V^{\,A\cup B}
=
\varnothing.
\]

:::

:::

::: {.pf-step #s1-2}

Since $A$ is connected, it lies entirely in one of $U$ or $V$.


::: pf-proof

The sets
\[
A\cap U
\qquad\text{and}\qquad
A\cap V
\]
are separated in the subspace $A$, and their union is $A$.
Connectedness of $A$ therefore forces one of them to be empty.
After exchanging $U$ and $V$ if necessary, assume
\[
A\subseteq U.
\]

:::

:::

::: {.pf-step #s1-3}

Under the convention of step [](#s1-2){.pf-ref},
\[
V\subseteq B.
\]


::: pf-proof

Since
\[
V\subseteq A\cup B
\]
and
\[
V\cap A=\varnothing,
\]
every point of $V$ must belong to $B$.

:::

:::

::: {.pf-step #s1-4}

One has
\[
\overline V^{\,\RR^n}\cap C=\varnothing.
\]


::: pf-proof

By step [](#s1-3){.pf-ref},
\[
V\subseteq B,
\]
so
\[
\overline V^{\,\RR^n}
\subseteq
\overline B^{\,\RR^n}.
\]
The hypothesis that $B$ and $C$ are separated gives
\[
\overline B\cap C=\varnothing.
\]
Hence
\[
\overline V\cap C=\varnothing.
\]

:::

:::

::: {.pf-step #s1-5}

One has
\[
\overline V^{\,\RR^n}\cap U=\varnothing.
\]


::: pf-proof

Because
\[
V\subseteq A\cup B,
\]
the closure of $V$ in the subspace $A\cup B$ is
\[
\overline V^{\,A\cup B}
=
\overline V^{\,\RR^n}\cap(A\cup B).
\]
The separation in step [](#s1-1){.pf-ref} gives
\[
\overline V^{\,A\cup B}\cap U=\varnothing.
\]
Since $U\subseteq A\cup B$, this is exactly
\[
\overline V^{\,\RR^n}\cap U=\varnothing.
\]

:::

:::

::: {.pf-step #s1-6}

One has
\[
V\cap\overline C^{\,\RR^n}=\varnothing.
\]


::: pf-proof

By step [](#s1-3){.pf-ref},
\[
V\subseteq B.
\]
The separation hypothesis on $B$ and $C$ gives
\[
B\cap\overline C=\varnothing.
\]
Hence
\[
V\cap\overline C=\varnothing.
\]

:::

:::

::: {.pf-step #s1-7}

One has
\[
V\cap\overline U^{\,\RR^n}=\varnothing.
\]


::: pf-proof

As in step [](#s1-5){.pf-ref},
\[
\overline U^{\,A\cup B}
=
\overline U^{\,\RR^n}\cap(A\cup B).
\]
The separation in step [](#s1-1){.pf-ref} gives
\[
V\cap\overline U^{\,A\cup B}=\varnothing.
\]
Since $V\subseteq A\cup B$,
\[
V\cap\overline U^{\,\RR^n}=\varnothing.
\]

:::

:::

::: {.pf-step #s1-8}

The sets
\[
V
\qquad\text{and}\qquad
U\cup C
\]
are separated in $\RR^n$.


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
\[
\overline V
\cap
(U\cup C)
=
\varnothing.
\]
By steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref},
\[
V
\cap
(\overline U\cup\overline C)
=
\varnothing.
\]
Since
\[
\overline{U\cup C}
\subseteq
\overline U\cup\overline C,
\]
one gets
\[
V\cap\overline{U\cup C}
=
\varnothing.
\]
Thus the two sets are separated.

:::

:::

::: {.pf-step #s1-9}

Moreover,
\[
\RR^n
=
V\cup(U\cup C).
\]


::: pf-proof

By the hypotheses,
\[
\RR^n
=
A\cup B\cup C.
\]
By step [](#s1-1){.pf-ref},
\[
A\cup B
=
U\cup V.
\]
Hence
\[
\RR^n
=
U\cup V\cup C
=
V\cup(U\cup C).
\]

:::

:::

::: {.pf-step #s1-10}

Steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref} contradict connectedness of $\RR^n$.


::: pf-proof

The set $V$ is nonempty by step [](#s1-1){.pf-ref}.
The set $U\cup C$ is nonempty because $U$ is nonempty.
Thus steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref} express $\RR^n$ as the union of two nonempty separated sets.
But $\RR^n$ is connected.
This is impossible.

:::

:::

::: {.pf-step #s1-11}

Therefore
\[
\boxed{A\cup B\text{ is connected}.}
\]


::: pf-proof

The assumption that $A\cup B$ is disconnected leads to the contradiction in step [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required conclusion.

:::

:::

:::
