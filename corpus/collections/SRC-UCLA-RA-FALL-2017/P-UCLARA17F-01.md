---
schema: qual/card@1
id: P-UCLARA17F-01
kind: problem
title: Nondecreasing functions map Borel sets to Borel sets
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 1. Suppose $f:\mathbb R\to\mathbb R$ is non-decreasing; specifically, for $x,y\in\mathbb R$ we have the implication
\[
x\le y \Longrightarrow f(x)\le f(y).
\]
Show that if $A\subset\mathbb R$ is a Borel set, then so is
\[
f(A)=\{f(x):x\in A\}.
\]
:::

::: {.solution}
Let
\[
f:\mathbb R\to\mathbb R
\]
be nondecreasing.

We first isolate the values for which the fibers of \(f\) are nontrivial.

<1>1. For every \(y\in\mathbb R\), the fiber
\[
f^{-1}(\{y\})
\]
is an interval, possibly empty or a singleton.

::: {.proof}
Suppose
\[
x_1<x_2
\]
and
\[
f(x_1)=f(x_2)=y.
\]
For any
\[
x_1\le x\le x_2,
\]
monotonicity gives
\[
y=f(x_1)\le f(x)\le f(x_2)=y.
\]
Hence
\[
f(x)=y.
\]
Thus every nonempty fiber is order-convex, hence an interval.
:::

Define
\[
Y_0
=
\left\{
y\in\mathbb R:
f^{-1}(\{y\})
\text{ contains at least two points}
\right\}.
\]

<1>2. The set \(Y_0\) is countable.

::: {.proof}
For each \(y\in Y_0\), the fiber
\[
I_y=f^{-1}(\{y\})
\]
is a nondegenerate interval by step <1>1, so it contains a rational number.

If \(y_1\ne y_2\), then the fibers \(I_{y_1}\) and \(I_{y_2}\) are disjoint. Choose one rational
\[
q_y\in I_y
\]
for each \(y\in Y_0\). The map
\[
y\longmapsto q_y
\]
is injective from \(Y_0\) into \(\mathbb Q\). Hence \(Y_0\) is countable.
:::

<1>3. For each \(y\in Y_0\), the fiber
\[
f^{-1}(\{y\})
\]
is a Borel subset of \(\mathbb R\).

::: {.proof}
By step <1>1, the fiber is an interval. Every interval in \(\mathbb R\), with any choice of open or closed endpoints, is Borel.
:::

Define
\[
N
=
f^{-1}(Y_0)
=
\bigcup_{y\in Y_0}
f^{-1}(\{y\}).
\]

<1>4. The set \(N\) is Borel.

::: {.proof}
By step <1>2, the index set \(Y_0\) is countable, and by step <1>3 each fiber is Borel. Hence \(N\) is a countable union of Borel sets.
:::

Let
\[
X_0=\mathbb R\setminus N.
\]

<1>5. The restriction
\[
f|_{X_0}:X_0\to\mathbb R
\]
is injective.

::: {.proof}
Suppose
\[
x_1,x_2\in X_0
\]
and
\[
f(x_1)=f(x_2)=y.
\]
If \(x_1\ne x_2\), then the fiber
\[
f^{-1}(\{y\})
\]
contains at least two points, so
\[
y\in Y_0
\]
and therefore
\[
x_1,x_2\in N,
\]
contradicting
\[
x_1,x_2\in X_0.
\]
Thus \(x_1=x_2\).
:::

We next note that \(f\) is Borel measurable.

<1>6. For every \(a\in\mathbb R\), the set
\[
\boxed{
\{x:f(x)>a\}}
\]
is an interval of the form
\[
(c,\infty),\quad[c,\infty),\quad\varnothing,\quad\text{or }\mathbb R.
\]

::: {.proof}
If
\[
x_1<x_2
\]
and
\[
f(x_1)>a,
\]
then monotonicity gives
\[
f(x_2)\ge f(x_1)>a.
\]
Thus once the inequality \(f(x)>a\) becomes true, it remains true to the right. Hence the set is an upper interval of one of the displayed forms.
:::

<1>7. Therefore \(f\) is Borel measurable.

::: {.proof}
By step <1>6, the inverse image of every ray
\[
(a,\infty)
\]
is Borel. Such rays generate the Borel \(\sigma\)-algebra on \(\mathbb R\), so \(f\) is Borel measurable.
:::

Now let
\[
A\subseteq\mathbb R
\]
be Borel.

<1>8. The set
\[
A_0=A\cap X_0
\]
is Borel.

::: {.proof}
The set \(A\) is Borel by hypothesis, and \(X_0\) is Borel because \(N\) is Borel by step <1>4.
:::

<1>9. By the Lusin--Souslin theorem,
\[
\boxed{
f(A_0)\text{ is Borel}.}
\]

::: {.proof}
The space \(X_0\), with its inherited Borel structure, is a standard Borel space because it is a Borel subset of the Polish space \(\mathbb R\). The map
\[
f|_{X_0}
\]
is Borel measurable by step <1>7 and injective by step <1>5.

The Lusin--Souslin theorem states that the image of a Borel set under an injective Borel map between standard Borel spaces is Borel. Apply it to the Borel set \(A_0\).
:::

<1>10. The set
\[
f(A\cap N)
\]
is a subset of \(Y_0\).

::: {.proof}
If
\[
x\in A\cap N,
\]
then
\[
x\in f^{-1}(Y_0),
\]
so
\[
f(x)\in Y_0.
\]
:::

<1>11. Hence
\[
\boxed{
f(A\cap N)\text{ is countable}.}
\]

::: {.proof}
By step <1>10,
\[
f(A\cap N)\subseteq Y_0,
\]
and \(Y_0\) is countable by step <1>2.
:::

<1>12. Therefore
\[
\boxed{
f(A\cap N)\text{ is Borel}.}
\]

::: {.proof}
Every countable subset of \(\mathbb R\) is Borel.
:::

<1>13. One has
\[
\boxed{
f(A)
=
f(A_0)\cup f(A\cap N)}.
\]

::: {.proof}
Since
\[
A
=
(A\cap X_0)\cup(A\cap N)
=
A_0\cup(A\cap N),
\]
apply \(f\) to the union.
:::

<1>14. Hence
\[
\boxed{
f(A)\text{ is Borel}.}
\]

::: {.proof}
By step <1>9, \(f(A_0)\) is Borel. By step <1>12, \(f(A\cap N)\) is Borel. Their union is Borel by step <1>13.
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>14 is the required conclusion.
:::
:::
