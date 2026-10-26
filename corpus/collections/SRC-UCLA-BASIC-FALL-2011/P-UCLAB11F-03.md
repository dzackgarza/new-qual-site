---
schema: qual/card@1
id: P-UCLAB11F-03
kind: problem
title: Partition the real line into uncountably many uncountable sets
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 3. Prove that the set of real numbers can be written as the union of uncountably many pairwise disjoint subsets, each of which is uncountable.
:::

Let $C\subseteq[0,1]$ be the middle-thirds Cantor set. Every point of $C$ has a unique ternary expansion using only the digits $0$ and $2$.

::: pf

::: pf-step

Let
\[
\Sigma=\{0,2\}^{\mathbb N}.
\]
For each sequence
\[
a=(a_1,a_2,\ldots)\in\Sigma,
\]
define
\[
E_a
=
\left\{
x\in C:
\text{the odd-position ternary digits of }x
\text{ are }a_1,a_2,\ldots
\right\}.
\]


::: pf-proof

Using this ternary expansion, every point $x\in C$ has a well-defined sequence of digits
\[
d_1(x),d_2(x),\ldots\in\{0,2\}.
\]
The set $E_a$ consists of those $x$ with
\[
d_{2j-1}(x)=a_j
\]
for every $j$.

:::

:::

::: pf-step

The sets $E_a$ are pairwise disjoint and
\[
C=\bigcup_{a\in\Sigma}E_a.
\]


::: pf-proof

Every $x\in C$ has a unique odd-position digit sequence
\[
\bigl(d_1(x),d_3(x),d_5(x),\ldots\bigr)\in\Sigma,
\]
so $x$ belongs to exactly one $E_a$. This proves both the union and pairwise disjointness.

:::

:::

::: pf-step

For every $a\in\Sigma$, the set $E_a$ is uncountable.


::: pf-proof

Fix $a$. For every sequence
\[
b=(b_1,b_2,\ldots)\in\Sigma,
\]
form the ternary expansion whose odd digits are $a_j$ and whose even digits are $b_j$:
\[
x_{a,b}
=
\sum_{j=1}^{\infty}
\frac{a_j}{3^{2j-1}}
+
\sum_{j=1}^{\infty}
\frac{b_j}{3^{2j}}.
\]
This defines a point of $E_a$.

If $b\ne b'$, let $j$ be the first index where they differ. The corresponding ternary expansions first differ at the even position $2j$. Two distinct sequences consisting only of ternary digits $0$ and $2$ represent distinct points, so the resulting points are distinct. Thus
\[
b\longmapsto x_{a,b}
\]
is injective from $\Sigma$ into $E_a$.

The set $\Sigma$ is uncountable by Cantor's diagonal argument. Hence $E_a$ is uncountable.

:::

:::

::: pf-step

There are uncountably many distinct sets $E_a$.


::: pf-proof

By step <1>2, the sets $E_a$ are pairwise disjoint, and by step <1>3 each is nonempty. Therefore distinct sequences $a\in\Sigma$ give distinct sets $E_a$. Since $\Sigma$ is uncountable, the family
\[
\{E_a:a\in\Sigma\}
\]
is uncountable.

:::

:::

::: pf-step

Fix one sequence $a_0\in\Sigma$ and define
\[
F_{a_0}=E_{a_0}\cup(\mathbb R\setminus C),
\]
while for $a\ne a_0$ define
\[
F_a=E_a.
\]
Then the sets $F_a$ are pairwise disjoint and
\[
\mathbb R=\bigcup_{a\in\Sigma}F_a.
\]


::: pf-proof

The sets $E_a$ partition $C$ by step <1>2. The set $\mathbb R\setminus C$ is disjoint from every $E_a$, so adjoining it to exactly one member of the partition preserves pairwise disjointness and changes the union from $C$ to all of $\mathbb R$.

:::

:::

::: pf-step

Every $F_a$ is uncountable, and there are uncountably many of them.


::: pf-proof

For $a\ne a_0$,
\[
F_a=E_a
\]
is uncountable by step <1>3. Also
\[
E_{a_0}\subseteq F_{a_0},
\]
so $F_{a_0}$ is uncountable as well. Step <1>4 shows that the indexing set yields uncountably many distinct members.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\mathbb R
\text{ is a union of uncountably many pairwise disjoint uncountable subsets}
}.
\]


::: pf-proof

This is exactly the partition constructed in steps <1>5--<1>6.

:::

:::

::: pf-qed

Step <1>7 is the required conclusion.

:::

:::
