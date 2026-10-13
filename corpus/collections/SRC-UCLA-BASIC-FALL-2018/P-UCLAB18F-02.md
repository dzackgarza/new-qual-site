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
Let $A\subset\mathbb R^n$ be connected and suppose
\[
\mathbb R^n\setminus A=B\cup C,
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

<1>1. There exist nonempty separated sets
\[
U,V\subseteq A\cup B
\]
such that
\[
A\cup B=U\cup V.
\]

::: {.proof}
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

<1>2. Since $A$ is connected, it lies entirely in one of $U$ or $V$.

::: {.proof}
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

<1>3. Under the convention of step <1>2,
\[
V\subseteq B.
\]

::: {.proof}
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

<1>4. One has
\[
\overline V^{\,\mathbb R^n}\cap C=\varnothing.
\]

::: {.proof}
By step <1>3,
\[
V\subseteq B,
\]
so
\[
\overline V^{\,\mathbb R^n}
\subseteq
\overline B^{\,\mathbb R^n}.
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

<1>5. One has
\[
\overline V^{\,\mathbb R^n}\cap U=\varnothing.
\]

::: {.proof}
Because
\[
V\subseteq A\cup B,
\]
the closure of $V$ in the subspace $A\cup B$ is
\[
\overline V^{\,A\cup B}
=
\overline V^{\,\mathbb R^n}\cap(A\cup B).
\]
The separation in step <1>1 gives
\[
\overline V^{\,A\cup B}\cap U=\varnothing.
\]
Since $U\subseteq A\cup B$, this is exactly
\[
\overline V^{\,\mathbb R^n}\cap U=\varnothing.
\]
:::

<1>6. One has
\[
V\cap\overline C^{\,\mathbb R^n}=\varnothing.
\]

::: {.proof}
By step <1>3,
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

<1>7. One has
\[
V\cap\overline U^{\,\mathbb R^n}=\varnothing.
\]

::: {.proof}
As in step <1>5,
\[
\overline U^{\,A\cup B}
=
\overline U^{\,\mathbb R^n}\cap(A\cup B).
\]
The separation in step <1>1 gives
\[
V\cap\overline U^{\,A\cup B}=\varnothing.
\]
Since $V\subseteq A\cup B$,
\[
V\cap\overline U^{\,\mathbb R^n}=\varnothing.
\]
:::

<1>8. The sets
\[
V
\qquad\text{and}\qquad
U\cup C
\]
are separated in $\mathbb R^n$.

::: {.proof}
By steps <1>4--<1>5,
\[
\overline V
\cap
(U\cup C)
=
\varnothing.
\]
By steps <1>6--<1>7,
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

<1>9. Moreover,
\[
\mathbb R^n
=
V\cup(U\cup C).
\]

::: {.proof}
By the hypotheses,
\[
\mathbb R^n
=
A\cup B\cup C.
\]
By step <1>1,
\[
A\cup B
=
U\cup V.
\]
Hence
\[
\mathbb R^n
=
U\cup V\cup C
=
V\cup(U\cup C).
\]
:::

<1>10. Steps <1>8--<1>9 contradict connectedness of $\mathbb R^n$.

::: {.proof}
The set $V$ is nonempty by step <1>1.
The set $U\cup C$ is nonempty because $U$ is nonempty.
Thus steps <1>8--<1>9 express $\mathbb R^n$ as the union of two nonempty separated sets.
But $\mathbb R^n$ is connected.
This is impossible.
:::

<1>11. Therefore
\[
\boxed{A\cup B\text{ is connected}.}
\]

::: {.proof}
The assumption that $A\cup B$ is disconnected leads to the contradiction in step <1>10.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 is the required conclusion.
:::
:::
