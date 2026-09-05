---
schema: qual/card@1
id: P-QRCUN
kind: problem
title: The distance between compact sets in a metric space is attained
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section A, problem A4 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Minimized the continuous function (a,b) |-> d(a,b) on the compact product
    A x B. Continuity is justified directly from the triangle inequality, so
    the argument does not assume the desired attainment statement.
---

::: {.problem}
If $(X,d)$ is a metric space, and $A, B \subseteq X$ are non-empty, then we define the *distance between $A$ and $B$* by $$d(A,B) = \inf\{d(a,b) : a \in A, b \in B\}$$ where $d : X \times X \to \mathbb{R}$ is the metric.
Show that if $A$ and $B$ are both compact and non-empty, then there are $a_0 \in A$ and $b_0 \in B$ so that $$d(A,B) = d(a_0,b_0).$$
:::

::: {.solution}
Define
\[
F:A\times B\longrightarrow\mathbb R,
\qquad
F(a,b)=d(a,b).
\]

<1>1. The function $F$ is continuous.
::: {.proof}
For $(a,b),(a',b')\in A\times B$, the triangle inequality gives
\[
d(a,b)
\le d(a,a')+d(a',b')+d(b',b),
\]
so
\[
d(a,b)-d(a',b')
\le d(a,a')+d(b,b').
\]
Interchanging $(a,b)$ and $(a',b')$ yields the reverse inequality, hence
\[
\bigl|d(a,b)-d(a',b')\bigr|
\le d(a,a')+d(b,b').
\]
Thus, if both $d(a,a')<\varepsilon/2$ and $d(b,b')<\varepsilon/2$, then
\[
|F(a,b)-F(a',b')|<\varepsilon.
\]
This proves continuity in the product topology on $A\times B$.
:::

<1>2. The space $A\times B$ is compact and nonempty.
::: {.proof}
Both $A$ and $B$ are compact by hypothesis, and a finite product of compact spaces is compact.
They are both nonempty, so their product is nonempty as well.
:::

<1>3. The function $F$ attains a minimum at some $(a_0,b_0)\in A\times B$.
::: {.proof}
By <1>1 and <1>2, the image
\[
F(A\times B)
\]
is a nonempty compact subset of $\mathbb R$.
Every nonempty compact subset of $\mathbb R$ has a least element.
Choose $(a_0,b_0)\in A\times B$ mapping to this least element.
Then
\[
d(a_0,b_0)
=F(a_0,b_0)
=\min F(A\times B).
\]
:::

<1>4. Therefore
\[
d(A,B)=d(a_0,b_0).
\]
::: {.proof}
By definition,
\[
d(A,B)
=\inf\{d(a,b):a\in A,\ b\in B\}
=\inf F(A\times B).
\]
By <1>3 the set $F(A\times B)$ has minimum $d(a_0,b_0)$, and the infimum of a set with a minimum equals that minimum.
:::
:::
