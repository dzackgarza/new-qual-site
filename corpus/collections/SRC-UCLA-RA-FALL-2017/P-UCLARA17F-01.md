---
schema: qual/card@1
id: P-UCLARA17F-01
kind: problem
title: Nondecreasing functions map Borel sets to Borel sets
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Functions
  - Borel Measures
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Suppose $f:\RR\to\RR$ is non-decreasing; specifically, for $x,y\in\RR$ we have the implication
$$
x\le y \Longrightarrow f(x)\le f(y).
$$
Show that if $A\subset\RR$ is a Borel set, then so is
$$
f(A)=\{f(x):x\in A\}.
$$
:::

::: {.solution}

Let
$$
f:\RR\to\RR
$$
be nondecreasing.

We first isolate the values for which the fibers of $f$ are nontrivial.

::: pf

::: {.pf-step #s1-1}

For every $y\in\RR$, the fiber
$$
f^{-1}(\{y\})
$$
is an interval, possibly empty or a singleton.


::: pf-proof

Suppose
$$
x_1<x_2
$$
and
$$
f(x_1)=f(x_2)=y.
$$
For any
$$
x_1\le x\le x_2,
$$
monotonicity gives
$$
y=f(x_1)\le f(x)\le f(x_2)=y.
$$
Hence
$$
f(x)=y.
$$
Thus every nonempty fiber is order-convex, hence an interval.

:::

:::

::: {.pf-step #s1-2}

The set $Y_0$ is countable.


::: pf-proof

For each $y\in Y_0$, the fiber
$$
I_y=f^{-1}(\{y\})
$$
is a nondegenerate interval by step [](#s1-1){.pf-ref}, so it contains a rational number.

If $y_1\ne y_2$, then the fibers $I_{y_1}$ and $I_{y_2}$ are disjoint. Choose one rational
$$
q_y\in I_y
$$
for each $y\in Y_0$. The map
$$
y\longmapsto q_y
$$
is injective from $Y_0$ into $\QQ$. Hence $Y_0$ is countable.

:::

:::

::: {.pf-step #s1-3}

For each $y\in Y_0$, the fiber
$$
f^{-1}(\{y\})
$$
is a Borel subset of $\RR$.


::: pf-proof

By step [](#s1-1){.pf-ref}, the fiber is an interval. Every interval in $\RR$, with any choice of open or closed endpoints, is Borel.

:::

:::

::: {.pf-step #s1-4}

The set $N$ is Borel.


::: pf-proof

By step [](#s1-2){.pf-ref}, the index set $Y_0$ is countable, and by step [](#s1-3){.pf-ref} each fiber is Borel. Hence $N$ is a countable union of Borel sets.

:::

:::

::: {.pf-step #s1-5}

The restriction
$$
f\restrict_{X_0}:X_0\to\RR
$$
is injective.


::: pf-proof

Suppose
$$
x_1,x_2\in X_0
$$
and
$$
f(x_1)=f(x_2)=y.
$$
If $x_1\ne x_2$, then the fiber
$$
f^{-1}(\{y\})
$$
contains at least two points, so
$$
y\in Y_0
$$
and therefore
$$
x_1,x_2\in N,
$$
contradicting
$$
x_1,x_2\in X_0.
$$
Thus $x_1=x_2$.

:::

:::

::: {.pf-step #s1-6}

For every $a\in\RR$, the set
$$
\boxed{
\{x:f(x)>a\}}
$$
is an interval of the form
$$
(c,\infty),\quad[c,\infty),\quad\varnothing,\quad\text{or }\RR.
$$


::: pf-proof

If
$$
x_1<x_2
$$
and
$$
f(x_1)>a,
$$
then monotonicity gives
$$
f(x_2)\ge f(x_1)>a.
$$
Thus once the inequality $f(x)>a$ becomes true, it remains true to the right. Hence the set is an upper interval of one of the displayed forms.

:::

:::

::: {.pf-step #s1-7}

Therefore $f$ is Borel measurable.


::: pf-proof

By step [](#s1-6){.pf-ref}, the inverse image of every ray
$$
(a,\infty)
$$
is Borel. Such rays generate the Borel $\sigma$-algebra on $\RR$, so $f$ is Borel measurable.

:::

:::

::: pf-step

The set
$$
A_0=A\cap X_0
$$
is Borel.


::: pf-proof

The set $A$ is Borel by hypothesis, and $X_0$ is Borel because $N$ is Borel by step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

By the Lusin--Souslin theorem,
$$
\boxed{
f(A_0)\text{ is Borel}.}
$$


::: pf-proof

The space $X_0$, with its inherited Borel structure, is a standard Borel space because it is a Borel subset of the Polish space $\RR$. The map
$$
f\restrict_{X_0}
$$
is Borel measurable by step [](#s1-7){.pf-ref} and injective by step [](#s1-5){.pf-ref}.

The Lusin--Souslin theorem states that the image of a Borel set under an injective Borel map between standard Borel spaces is Borel. Apply it to the Borel set $A_0$.

:::

:::

::: {.pf-step #s1-10}

The set
$$
f(A\cap N)
$$
is a subset of $Y_0$.


::: pf-proof

If
$$
x\in A\cap N,
$$
then
$$
x\in f^{-1}(Y_0),
$$
so
$$
f(x)\in Y_0.
$$

:::

:::

::: pf-step

Hence
$$
\boxed{
f(A\cap N)\text{ is countable}.}
$$


::: pf-proof

By step [](#s1-10){.pf-ref},
$$
f(A\cap N)\subseteq Y_0,
$$
and $Y_0$ is countable by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\boxed{
f(A\cap N)\text{ is Borel}.}
$$


::: pf-proof

Every countable subset of $\RR$ is Borel.

:::

:::

::: {.pf-step #s1-13}

One has
$$
\boxed{
f(A)
=
f(A_0)\cup f(A\cap N)}.
$$


::: pf-proof

Since
$$
A
=
(A\cap X_0)\cup(A\cap N)
=
A_0\cup(A\cap N),
$$
apply $f$ to the union.

:::

:::

::: {.pf-step #s1-14}

Hence
$$
\boxed{
f(A)\text{ is Borel}.}
$$


::: pf-proof

By step [](#s1-9){.pf-ref}, $f(A_0)$ is Borel. By step [](#s1-12){.pf-ref}, $f(A\cap N)$ is Borel. Their union is Borel by step [](#s1-13){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is the required conclusion.

:::

:::

:::
