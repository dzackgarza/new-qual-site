---
schema: qual/card@1
id: P-WESTOP05-04
kind: problem
title: Hausdorff examples separating normality, countability, compactness, and metrizability
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Give Hausdorff examples of each requested phenomenon:

1. normal spaces $X,Y$ whose product $X\times Y$ is not normal;
2. a normal space $X$ with a subspace $Y\subset X$ that is not normal;
3. an infinite compact space with no isolated points, and an infinite compact space with a dense set of isolated points;
4. an infinite compact space having a point with no countable local base;
5. a first-countable space that is not second countable;
6. a separable space that is not metrizable.
:::

Let \(\mathbb S\) denote the Sorgenfrey line.

## 1. Normal factors with nonnormal product

::: pf

::: pf-step

The Sorgenfrey line is regular.


::: pf-proof

The basic neighborhoods are intervals
\[
[a,b).
\]
Let \(x\in[a,b)\). Choose \(c\) with
\[
x<c<b.
\]
Then
\[
x\in[x,c),
\]
and the closure of \([x,c)\) in the Sorgenfrey line is contained in
\[
[x,c]\subseteq[a,b).
\]
Thus points can be separated from closed sets by neighborhoods with closure
inside a prescribed neighborhood, which is regularity.

:::

:::

::: pf-step

The Sorgenfrey line is Lindelöf.


::: pf-proof

Let \(\mathcal U\) be an open cover. Refine it by basic intervals, choosing
for each \(x\in\mathbb R\) a basic interval
\[
[x,b_x)
\]
contained in some member of \(\mathcal U\).

Set
\[
O=\bigcup_{x\in\mathbb R}(x,b_x)
\]
using the ordinary Euclidean topology. The family
\[
\{(x,b_x):x\in\mathbb R\}
\]
is an ordinary open cover of \(O\). Since the Euclidean line is second
countable, hence Lindelöf, choose countably many indices \(x_n\) such that
\[
O=\bigcup_{n=1}^{\infty}(x_n,b_{x_n}).
\]

The corresponding Sorgenfrey intervals
\[
[x_n,b_{x_n})
\]
cover \(O\).

Now let
\[
A=\mathbb R-O.
\]
For distinct \(x<y\) in \(A\), one must have
\[
b_x\le y;
\]
otherwise
\[
y\in(x,b_x)\subseteq O,
\]
contradiction. Thus the ordinary open intervals
\[
(x,b_x)
\qquad(x\in A)
\]
are pairwise disjoint. Each contains a rational number, so \(A\) is
countable.

Adding the countably many intervals \([x,b_x)\) for \(x\in A\) gives a
countable subcover of \(\mathcal U\).

:::

:::

::: pf-step

Therefore \(\mathbb S\) is normal.


::: pf-proof

A regular Lindelöf space is normal. Apply steps <1>1--<1>2.

:::

:::

::: pf-step

The Sorgenfrey plane
\[
\mathbb S^2
\]
is separable.


::: pf-proof

The countable set
\[
\mathbb Q\times\mathbb Q
\]
is dense. Every nonempty basic rectangle
\[
[a,b)\times[c,d)
\]
contains a pair of rational points.

:::

:::

::: pf-step

The anti-diagonal
\[
D=\{(x,-x):x\in\mathbb R\}
\]
is closed in \(\mathbb S^2\).


::: pf-proof

Let
\[
(a,b)\notin D,
\]
so
\[
a+b\ne0.
\]

If \(a+b>0\), then every point of
\[
[a,a+\varepsilon)\times[b,b+\varepsilon)
\]
has coordinate sum \(>0\), for any \(\varepsilon>0\), so this rectangle
misses \(D\).

If \(a+b<0\), choose
\[
0<\varepsilon<-\frac{a+b}{2}.
\]
Then every point \((x,y)\) in the rectangle satisfies
\[
x+y<a+b+2\varepsilon<0,
\]
so again the rectangle misses \(D\).

Thus the complement of \(D\) is open.

:::

:::

::: pf-step

The subspace \(D\) is discrete.


::: pf-proof

For \(x\in\mathbb R\), the basic rectangle
\[
[x,x+1)\times[-x,-x+1)
\]
meets \(D\) only at \((x,-x)\). Indeed, if
\[
(t,-t)
\]
belongs to the rectangle, then
\[
t\ge x
\]
and
\[
-t\ge -x,
\]
so
\[
t=x.
\]

:::

:::

::: pf-step

Hence \(D\) is a closed discrete subspace of cardinality
\[
\boxed{\mathfrak c}.
\]


::: pf-proof

Closedness is step <1>5, discreteness is step <1>6, and the map
\[
x\longmapsto(x,-x)
\]
is a bijection from \(\mathbb R\) to \(D\).

:::

:::

::: pf-step

A separable space has at most \(\mathfrak c\) continuous functions
into \([0,1]\).


::: pf-proof

Let \(Q\) be a countable dense subset. A continuous function
\[
f:X\to[0,1]
\]
is determined uniquely by its restriction to \(Q\): if two continuous
functions agree on the dense set \(Q\), they agree everywhere.

Thus
\[
|C(X,[0,1])|
\le
|[0,1]^Q|
=
\mathfrak c^{\aleph_0}
=
\mathfrak c.
\]

:::

:::

::: pf-step

If \(\mathbb S^2\) were normal, then it would admit at least
\[
2^{\mathfrak c}
\]
distinct continuous functions to \([0,1]\).


::: pf-proof

For each subset
\[
A\subseteq D,
\]
both \(A\) and \(D-A\) are closed in \(\mathbb S^2\), because \(D\) is
closed and discrete.

If \(\mathbb S^2\) were normal, Urysohn's lemma would provide a continuous
function
\[
f_A:\mathbb S^2\to[0,1]
\]
such that
\[
f_A|_A=0,
\qquad
f_A|_{D-A}=1.
\]
Distinct subsets \(A\) give distinct functions. Since
\[
|\mathcal P(D)|=2^{\mathfrak c},
\]
there would be at least \(2^{\mathfrak c}\) such functions.

:::

:::

::: pf-step

This is impossible because
\[
2^{\mathfrak c}>\mathfrak c.
\]


::: pf-proof

Cantor's theorem gives
\[
2^\kappa>\kappa
\]
for every cardinal \(\kappa\). Apply it to \(\kappa=\mathfrak c\), and
compare steps <1>4, <1>8, and <1>9.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\mathbb S\text{ and }\mathbb S\text{ are normal, but }
\mathbb S\times\mathbb S\text{ is not normal}.}
\]


::: pf-proof

Normality of each factor is step <1>3, while nonnormality of the product is
steps <1>4--<1>10.

:::

:::

::: pf-step

The Sorgenfrey line is completely regular Hausdorff.


::: pf-proof

The Sorgenfrey line is normal by step <1>3 and Hausdorff. Every normal
Hausdorff space is completely regular by Urysohn's lemma.

:::

:::

::: pf-step

Therefore
\[
Y=\mathbb S^2
\]
is completely regular Hausdorff.


::: pf-proof

Products of completely regular spaces are completely regular, and products
of Hausdorff spaces are Hausdorff.

:::

:::

::: pf-step

By the Tychonoff embedding theorem proved in the preceding problem,
\(Y\) embeds in a compact Hausdorff space \(X\).


::: pf-proof

Every completely regular Hausdorff space embeds in a cube
\[
[0,1]^{C(Y,[0,1])},
\]
which is compact Hausdorff.

:::

:::

::: pf-step

The ambient space \(X\) is normal, but the embedded subspace \(Y\) is
not normal.


::: pf-proof

Compact Hausdorff spaces are normal. The subspace \(Y\cong\mathbb S^2\) is
not normal by step <1>11.

:::

:::

::: pf-step

Thus this \(X\) and \(Y\subseteq X\) answer part \(2\).


::: pf-proof

Step <1>15 gives exactly the requested phenomenon.

:::

:::

::: pf-step

The interval
\[
\boxed{[0,1]}
\]
is an infinite compact Hausdorff space with no isolated points.


::: pf-proof

It is compact by Heine--Borel. Every neighborhood of every point of
\([0,1]\) contains another point of the interval, so no point is isolated.

:::

:::

::: pf-step

The space
\[
\boxed{
K=\{0\}\cup\{1/n:n\in\mathbb N\}}
\]
is infinite and compact.


::: pf-proof

It is a closed and bounded subset of \(\mathbb R\), hence compact by
Heine--Borel.

:::

:::

::: pf-step

Every point \(1/n\) is isolated in \(K\).


::: pf-proof

Choose an ordinary open interval around \(1/n\) small enough to contain no
other point of the sequence and not \(0\). Its intersection with \(K\) is
the singleton \(\{1/n\}\).

:::

:::

::: pf-step

The set of isolated points
\[
\{1/n:n\in\mathbb N\}
\]
is dense in \(K\).


::: pf-proof

Its closure contains all sequence points and also the limit point \(0\).
Thus its closure is all of \(K\).

:::

:::

::: pf-step

The space \(D^*\) is infinite compact Hausdorff.


::: pf-proof

The one-point compactification of a locally compact noncompact Hausdorff
space is compact Hausdorff. An uncountable discrete space is locally compact,
Hausdorff, and noncompact.

:::

:::

::: pf-step

The point \(\infty\) has no countable local base.


::: pf-proof

As in the previous problem, neighborhoods of \(\infty\) are complements of
finite subsets of \(D\).

If
\[
U_1,U_2,\dots
\]
were a countable local base, choose finite \(F_n\subseteq D\) with
\[
D^*-F_n\subseteq U_n.
\]
The union
\[
F=\bigcup_nF_n
\]
is countable, so choose
\[
d\in D-F.
\]
Then
\[
V=D^*-\{d\}
\]
is a neighborhood of \(\infty\), but \(d\in U_n\) for every \(n\), so no
\(U_n\subseteq V\), contradiction.

:::

:::

::: pf-step

Thus \(D^*\) answers part \(4\).


::: pf-proof

Use steps <1>21--<1>22.

:::

:::

::: pf-step

The space \(D\) is first countable.


::: pf-proof

At each point \(x\in D\), the singleton
\[
\{x\}
\]
is a one-element local base.

:::

:::

::: pf-step

The space \(D\) is not second countable.


::: pf-proof

Let \(\mathcal B\) be any basis. Since the singleton \(\{x\}\) is open, for
each \(x\in D\) there must be some basis element \(B_x\) with
\[
x\in B_x\subseteq\{x\}.
\]
Hence
\[
B_x=\{x\}.
\]
Thus every singleton belongs to every basis, so every basis has cardinality
at least \(|D|\), which is uncountable.

:::

:::

::: pf-step

Therefore an uncountable discrete space answers part \(5\).


::: pf-proof

Combine steps <1>24--<1>25.

:::

:::

::: pf-step

The Sorgenfrey line is separable.


::: pf-proof

The rationals are dense, as in the preceding problem: every nonempty basic
interval
\[
[a,b)
\]
contains a rational point.

:::

:::

::: pf-step

The Sorgenfrey line is not second countable.


::: pf-proof

For each \(x\), any basis must contain some
\[
B_x
\]
with
\[
x\in B_x\subseteq[x,x+1).
\]
If \(x<y\), then \(B_x\ne B_y\), because \(B_y\subseteq[y,y+1)\) cannot
contain \(x\). Thus a basis has at least continuum many elements.

:::

:::

::: pf-step

Hence the Sorgenfrey line is not metrizable.


::: pf-proof

Every separable metric space is second countable. Steps <1>27--<1>28
contradict this consequence.

:::

:::

::: pf-step

Therefore the Sorgenfrey line answers part \(6\).


::: pf-proof

It is separable by step <1>27 and nonmetrizable by step <1>29.

:::

:::

::: pf-qed

Steps <1>11, <1>16, <1>17--<1>20, <1>23, <1>26, and <1>30 provide the six
requested Hausdorff examples.

:::

:::
