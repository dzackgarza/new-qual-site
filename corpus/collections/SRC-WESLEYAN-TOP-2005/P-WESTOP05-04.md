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

::: {.solution}

Let \(\mathbb S\) denote the Sorgenfrey line.

## 1. Normal factors with nonnormal product

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

The Sorgenfrey line is Lindelöf.


::: pf-proof

Let \(\mathcal U\) be an open cover. Refine it by basic intervals, choosing
for each \(x\in\RR\) a basic interval
\[
[x,b_x)
\]
contained in some member of \(\mathcal U\).

Set
\[
O=\bigcup_{x\in\RR}(x,b_x)
\]
using the ordinary Euclidean topology. The family
\[
\{(x,b_x):x\in\RR\}
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
A=\RR-O.
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

::: {.pf-step #s1-3}

Therefore \(\mathbb S\) is normal.


::: pf-proof

A regular Lindelöf space is normal. Apply steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The Sorgenfrey plane
\[
\mathbb S^2
\]
is separable.


::: pf-proof

The countable set
\[
\QQ\times\QQ
\]
is dense. Every nonempty basic rectangle
\[
[a,b)\times[c,d)
\]
contains a pair of rational points.

:::

:::

::: {.pf-step #s1-5}

The anti-diagonal
\[
D=\{(x,-x):x\in\RR\}
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

::: {.pf-step #s1-6}

The subspace \(D\) is discrete.


::: pf-proof

For \(x\in\RR\), the basic rectangle
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

::: {.pf-step #s1-7}

Hence \(D\) is a closed discrete subspace of cardinality
\[
\boxed{\mathfrak c}.
\]


::: pf-proof

Closedness is step [](#s1-5){.pf-ref}, discreteness is step [](#s1-6){.pf-ref}, and the map
\[
x\longmapsto(x,-x)
\]
is a bijection from \(\RR\) to \(D\).

:::

:::

::: {.pf-step #s1-8}

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

::: {.pf-step #s1-9}

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

::: {.pf-step #s1-10}

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
compare steps [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref}, and [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Therefore
\[
\boxed{
\mathbb S\text{ and }\mathbb S\text{ are normal, but }
\mathbb S\times\mathbb S\text{ is not normal}.}
\]


::: pf-proof

Normality of each factor is step [](#s1-3){.pf-ref}, while nonnormality of the product is
steps [](#s1-4){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

The Sorgenfrey line is completely regular Hausdorff.


::: pf-proof

The Sorgenfrey line is normal by step [](#s1-3){.pf-ref} and Hausdorff. Every normal
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

::: {.pf-step #s1-15}

The ambient space \(X\) is normal, but the embedded subspace \(Y\) is
not normal.


::: pf-proof

Compact Hausdorff spaces are normal. The subspace \(Y\cong\mathbb S^2\) is
not normal by step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Thus this \(X\) and \(Y\subseteq X\) answer part \(2\).


::: pf-proof

Step [](#s1-15){.pf-ref} gives exactly the requested phenomenon.

:::

:::

::: {.pf-step #s1-17}

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

::: {.pf-step #s1-18}

The space
\[
\boxed{
K=\{0\}\cup\{1/n:n\in\NN\}}
\]
is infinite and compact.


::: pf-proof

It is a closed and bounded subset of \(\RR\), hence compact by
Heine--Borel.

:::

:::

::: {.pf-step #s1-19}

Every point \(1/n\) is isolated in \(K\).


::: pf-proof

Choose an ordinary open interval around \(1/n\) small enough to contain no
other point of the sequence and not \(0\). Its intersection with \(K\) is
the singleton \(\{1/n\}\).

:::

:::

::: {.pf-step #s1-20}

The set of isolated points
\[
\{1/n:n\in\NN\}
\]
is dense in \(K\).


::: pf-proof

Its closure contains all sequence points and also the limit point \(0\).
Thus its closure is all of \(K\).

:::

:::

::: {.pf-step #s1-21}

The space \(D^*\) is infinite compact Hausdorff.


::: pf-proof

The one-point compactification of a locally compact noncompact Hausdorff
space is compact Hausdorff. An uncountable discrete space is locally compact,
Hausdorff, and noncompact.

:::

:::

::: {.pf-step #s1-22}

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

::: {.pf-step #s1-23}

Thus \(D^*\) answers part \(4\).


::: pf-proof

Use steps [](#s1-21){.pf-ref} through [](#s1-22){.pf-ref}.

:::

:::

::: {.pf-step #s1-24}

The space \(D\) is first countable.


::: pf-proof

At each point \(x\in D\), the singleton
\[
\{x\}
\]
is a one-element local base.

:::

:::

::: {.pf-step #s1-25}

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

::: {.pf-step #s1-26}

Therefore an uncountable discrete space answers part \(5\).


::: pf-proof

Combine steps [](#s1-24){.pf-ref} through [](#s1-25){.pf-ref}.

:::

:::

::: {.pf-step #s1-27}

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

::: {.pf-step #s1-28}

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

::: {.pf-step #s1-29}

Hence the Sorgenfrey line is not metrizable.


::: pf-proof

Every separable metric space is second countable. Steps [](#s1-27){.pf-ref} through [](#s1-28){.pf-ref}
contradict this consequence.

:::

:::

::: {.pf-step #s1-30}

Therefore the Sorgenfrey line answers part \(6\).


::: pf-proof

It is separable by step [](#s1-27){.pf-ref} and nonmetrizable by step [](#s1-29){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-11){.pf-ref}, [](#s1-16){.pf-ref}, [](#s1-17){.pf-ref} through [](#s1-20){.pf-ref}, [](#s1-23){.pf-ref}, and [](#s1-26){.pf-ref}, and [](#s1-30){.pf-ref} provide the six
requested Hausdorff examples.

:::

:::

:::
