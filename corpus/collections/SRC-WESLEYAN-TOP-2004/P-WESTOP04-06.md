---
schema: qual/card@1
id: P-WESTOP04-06
kind: problem
title: Cardinal invariants under closed subspaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Carefully define any three standard cardinal invariants associated with every topological space, excluding the cardinality $|X|$ itself.
2. For each invariant $c$ you chose, prove or disprove:
   \[
   F\subseteq X\text{ closed}\quad\Longrightarrow\quad c(F)\le c(X).
   \]
3. For each chosen invariant, prove or disprove the same assertion under the additional hypothesis that $X$ is metrizable.
:::

::: {.solution}

Use the following three cardinal invariants.

::: pf

::: {.pf-step #s1-1}

Define the weight, density, and cellularity of a topological space $X$ by
$$
w(X)
\coloneqq
\min\{
|\mathcal B|:
\mathcal B\text{ is a base for }X
\},
$$
$$
d(X)
\coloneqq
\min\{
|D|:
D\subseteq X,\ \overline D=X
\},
$$
and
$$
c(X)
\coloneqq
\sup\{
|\mathcal U|:
\mathcal U
\text{ is a pairwise-disjoint family of nonempty open subsets of }X
\}.
$$


::: pf-proof

These are standard cardinal invariants: respectively the smallest size of a base, the smallest size of a dense subset, and the supremal size of a disjoint family of nonempty open sets.

:::

:::

::: {.pf-step #s1-2}

For every subspace
$$
F\subseteq X,
$$
one has
$$
\boxed{w(F)\le w(X)}.
$$


::: pf-proof

Let
$$
\mathcal B
$$
be a base for $X$. Then
$$
\mathcal B_F
\coloneqq
\{
B\cap F:
B\in\mathcal B
\}
\setminus\{\varnothing\}
$$
is a base for the subspace topology on $F$. Hence
$$
w(F)
\le
|\mathcal B_F|
\le
|\mathcal B|.
$$
Taking $\mathcal B$ of minimum size gives
$$
w(F)\le w(X).
$$
Closedness and metrizability are not needed.

:::

:::

::: {.pf-step #s1-3}

Density need not satisfy
$$
d(F)\le d(X)
$$
for closed subspaces.


::: pf-proof

Let
$$
\sorgenfrey
$$
be the Sorgenfrey line, whose basic open sets are intervals
$$
[a,b).
$$
Set
$$
X=\sorgenfrey\times\sorgenfrey.
$$
The countable set
$$
\QQ\times\QQ
$$
is dense in $X$, because every basic rectangle
$$
[a,b)\times[c,d)
$$
contains a pair of rationals. Thus
$$
d(X)=\aleph_0.
$$

Now let
$$
F
\coloneqq
\{
(x,-x):
x\in\RR
\}.
$$
This set is closed. Indeed, if
$$
(u,v)\notin F,
$$
then
$$
u+v\ne0.
$$
If
$$
u+v>0,
$$
any sufficiently small basic rectangle
$$
[u,u+\varepsilon)
\times
[v,v+\varepsilon)
$$
has all coordinate sums positive. If
$$
u+v<0,
$$
choose
$$
0<\varepsilon<-\frac{u+v}{2};
$$
then every point of the same rectangle has negative coordinate sum. In either case the rectangle misses $F$.

The subspace $F$ is discrete: for each
$$
x\in\RR,
$$
$$
\bigl(
[x,x+1)
\times
[-x,-x+1)
\bigr)
\cap F
=
\{(x,-x)\}.
$$
Hence every dense subset of $F$ must equal $F$, so
$$
d(F)
=
|F|
=
2^{\aleph_0}
>
\aleph_0
=
d(X).
$$
Thus the closed-subspace inequality fails in general.

:::

:::

::: {.pf-step #s1-4}

Cellularity likewise need not satisfy
$$
c(F)\le c(X)
$$
for closed subspaces.


::: pf-proof

Use the same
$$
X=\sorgenfrey\times\sorgenfrey
$$
and closed discrete
$$
F.
$$
Since $X$ is separable, every pairwise-disjoint family of nonempty open subsets of $X$ is countable: choose one point of the countable dense set
$$
\QQ\times\QQ
$$
from each open set; disjointness makes these chosen points distinct. Hence
$$
c(X)\le\aleph_0.
$$
Since $X$ has infinitely many disjoint nonempty open sets,
$$
c(X)=\aleph_0.
$$

But $F$ is discrete of cardinality
$$
2^{\aleph_0},
$$
so its singleton subsets form a pairwise-disjoint family of
$$
2^{\aleph_0}
$$
nonempty open subsets. Therefore
$$
c(F)
=
2^{\aleph_0}
>
\aleph_0
=
c(X).
$$

:::

:::

::: {.pf-step #s1-5}

If $X$ is metrizable, then every subspace
$$
F\subseteq X
$$
satisfies
$$
\boxed{d(F)\le d(X)}.
$$


::: pf-proof

Let
$$
D\subseteq X
$$
be dense with
$$
|D|=d(X).
$$
Fix a metric $d_X$ inducing the topology.

For each
$$
n\ge1
$$
and each
$$
p\in D
$$
for which
$$
B(p,1/n)\cap F\ne\varnothing,
$$
choose one point
$$
x_{p,n}
\in
B(p,1/n)\cap F.
$$
Let
$$
E
\coloneqq
\{
x_{p,n}
\}.
$$
Then
$$
|E|
\le
|D|\cdot\aleph_0.
$$
If $d(X)$ is infinite, this equals
$$
d(X);
$$
the finite case is immediate.

To see that $E$ is dense in $F$, let
$$
y\in F
$$
and let
$$
B(y,\varepsilon)\cap F
$$
be a basic neighborhood in $F$. Choose $n$ with
$$
2/n<\varepsilon.
$$
Since $D$ is dense in $X$, choose
$$
p\in D\cap B(y,1/n).
$$
Then
$$
y\in B(p,1/n)\cap F,
$$
so the chosen
$$
x_{p,n}
$$
exists. Moreover,
$$
d_X(x_{p,n},y)
<
\frac2n
<
\varepsilon.
$$
Thus
$$
x_{p,n}
\in
B(y,\varepsilon)\cap F.
$$
Hence $E$ is dense in $F$, proving
$$
d(F)\le d(X).
$$

:::

:::

::: {.pf-step #s1-6}

If $X$ is metrizable, then every subspace
$$
F\subseteq X
$$
satisfies
$$
\boxed{c(F)\le c(X)}.
$$


::: pf-proof

Let
$$
\mathcal U
$$
be a pairwise-disjoint family of nonempty open subsets of $F$. For each
$$
U\in\mathcal U,
$$
choose
$$
x_U\in U
$$
and
$$
r_U>0
$$
such that
$$
B_X(x_U,r_U)\cap F
\subseteq
U.
$$

For
$$
n\ge1,
$$
let
$$
\mathcal U_n
\coloneqq
\{
U\in\mathcal U:
r_U>1/n
\}.
$$
Then
$$
\mathcal U
=
\bigcup_{n=1}^{\infty}\mathcal U_n.
$$

If
$$
U,V\in\mathcal U_n
$$
are distinct, then
$$
d_X(x_U,x_V)\ge1/n;
$$
otherwise
$$
x_V
\in
B_X(x_U,1/n)\cap F
\subseteq
U,
$$
contradicting
$$
x_V\in V
$$
and
$$
U\cap V=\varnothing.
$$
Therefore the ambient balls
$$
B_X\left(x_U,\frac1{3n}\right),
\qquad
U\in\mathcal U_n,
$$
are pairwise disjoint nonempty open subsets of $X$. Hence
$$
|\mathcal U_n|
\le
c(X).
$$

Thus
$$
|\mathcal U|
\le
c(X)\cdot\aleph_0.
$$
If $X$ is infinite and metrizable, then
$$
c(X)\ge\aleph_0,
$$
because either $X$ contains a countably infinite closed discrete subset, whose points admit pairwise-disjoint open neighborhoods, or else $X$ has a nonisolated point $x$ and one may choose distinct
$$
x_n\to x
$$
with
$$
d_X(x_{n+1},x)
<
\frac13 d_X(x_n,x);
$$
then sufficiently small balls around the $x_n$ are pairwise disjoint.
Therefore, for infinite metric $X$, the right-hand side equals
$$
c(X).
$$
If $X$ is finite, every subspace has at most as many nonempty pairwise-disjoint open sets as $X$ itself, so the assertion is immediate. Therefore
$$
c(F)\le c(X).
$$

:::

:::

::: {.pf-step #s1-7}

For the three chosen invariants, the closed-subspace conclusions are:
$$
\boxed{
\begin{array}{c|c|c}
\text{Invariant}
&
\text{Closed }F\subseteq X
&
\text{Closed }F\subseteq X,\ X\text{ metrizable}
\\
\hline
w
&
w(F)\le w(X)
&
w(F)\le w(X)
\\
d
&
\text{false in general}
&
d(F)\le d(X)
\\
c
&
\text{false in general}
&
c(F)\le c(X)
\end{array}}
$$


::: pf-proof

The weight assertions are step [](#s1-2){.pf-ref}; the general counterexamples for density and cellularity are steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}; the metrizable assertions are steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} define three standard cardinal invariants and completely determine the requested closed-subspace inequalities in the general and metrizable cases.

:::

:::

:::
