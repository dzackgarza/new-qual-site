---
schema: qual/card@1
id: P-UNL871F13-PS8.1
kind: problem
title: Compactness and separation axioms for four real-line topologies
classification:
  areas: [topology]
  topics: [Compactness, Separation Axioms]
relations: []
review: draft
---

::: {.problem}
For each of the following spaces:

1. determine whether it is compact; and

2. determine the largest natural number $i$ for which it satisfies the separation axiom $T_i$.

Consider:

- $\RR$ with the excluded-point topology;

- $\RR$ with the included-point topology;

- the lower-limit line $\RR_\ell$;

- the subspace $[0,1]\subset\RR_\ell$.
:::

::: {.solution}

Use the standard hierarchy
$$
T_0,T_1,T_2,T_3,T_4,
$$
where
$$
T_2=\text{Hausdorff},
\quad
T_3=\text{regular }T_1,
\quad
T_4=\text{normal }T_1.
$$

::: pf

::: {.pf-step #s1-1}

The excluded-point real line is compact.


::: pf-proof

Let
$$
0
$$
be the excluded point.
In the excluded-point topology, the only open set containing
$$
0
$$
is the whole space
$$
\RR.
$$

Every open cover of
$$
\RR
$$
must contain some open set covering $0$.
That member must be
$$
\RR
$$
itself.
Hence the one-element family
$$
\{\RR\}
$$
is already a finite subcover.

:::

:::

::: {.pf-step #s1-2}

The excluded-point real line is
$$
T_0
$$
but not
$$
T_1.
$$


::: pf-proof

Let
$$
x\ne y.
$$
If neither point is $0$, the singleton
$$
\{x\}
$$
is open and contains $x$ but not $y$.
If one point is $0$, say
$$
x=0,
\quad
y\ne0,
$$
then
$$
\{y\}
$$
is open and contains $y$ but not $x$.
Thus the space is $T_0$.

It is not $T_1$ because no proper open set contains $0$.
In particular there is no open set containing $0$ but excluding a fixed
nonzero point.
Equivalently, a nonzero singleton is not closed:
its complement contains $0$ but is not all of $\RR$, hence is not
open.

:::

:::

::: {.pf-step #s1-3}

Therefore, for the excluded-point topology,
$$
\boxed{
\text{compact: yes},
\qquad
\text{largest }T_i:T_0.
}
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The included-point real line is not compact.


::: pf-proof

Let
$$
0
$$
be the included point.
For each
$$
x\in\RR\setminus\{0\},
$$
set
$$
U_x=\{0,x\}.
$$
Every $U_x$ is open because it contains the included point.
The family
$$
\{U_x:x\ne0\}
$$
covers $\RR$.

Any finite subfamily covers only
$$
0
$$
and finitely many nonzero points.
Thus no finite subfamily covers all of $\RR$.
Hence the space is not compact.

:::

:::

::: {.pf-step #s1-5}

The included-point real line is
$$
T_0
$$
but not
$$
T_1.
$$


::: pf-proof

For distinct nonzero points
$$
x,y,
$$
the open set
$$
\{0,x\}
$$
contains $x$ but not $y$.
For the pair
$$
0,y,
\qquad
y\ne0,
$$
the open singleton
$$
\{0\}
$$
contains $0$ but not $y$.
Thus the space is $T_0$.

It is not $T_1$ because every nonempty open set containing a nonzero point
also contains $0$.
Hence one cannot find an open neighborhood of a nonzero point excluding
$0$.

:::

:::

::: {.pf-step #s1-6}

Therefore, for the included-point topology,
$$
\boxed{
\text{compact: no},
\qquad
\text{largest }T_i:T_0.
}
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The lower-limit line
$$
\RR_\ell
$$
is Hausdorff.


::: pf-proof

Its standard basis consists of intervals
$$
[a,b).
$$
Let
$$
x<y.
$$
Then
$$
\left[x,\frac{x+y}{2}\right)
$$
and
$$
[y,y+1)
$$
are disjoint open neighborhoods of $x$ and $y$.
Thus
$$
\RR_\ell
$$
is Hausdorff, hence $T_1$.

:::

:::

::: {.pf-step #s1-8}

The lower-limit line is normal.


::: pf-proof

Let
$$
A,B\subseteq\RR_\ell
$$
be disjoint closed sets.

For each
$$
a\in A,
$$
the open set
$$
\RR_\ell\setminus B
$$
contains $a$.
Choose
$$
r_a>a
$$
such that
$$
[a,r_a)
\subseteq
\RR_\ell\setminus B.
$$
Similarly, for each
$$
b\in B,
$$
choose
$$
s_b>b
$$
such that
$$
[b,s_b)
\subseteq
\RR_\ell\setminus A.
$$

Define
$$
U
=
\bigcup_{a\in A}[a,r_a),
\qquad
V
=
\bigcup_{b\in B}[b,s_b).
$$
Then $U,V$ are open,
$$
A\subseteq U,
\qquad
B\subseteq V.
$$

Suppose
$$
x\in U\cap V.
$$
Then for some
$$
a\in A,
\qquad
b\in B,
$$
$$
x\in[a,r_a)\cap[b,s_b).
$$
Assume
$$
a\le b.
$$
Since
$$
b\le x<r_a,
$$
one has
$$
b\in[a,r_a),
$$
contradicting the choice
$$
[a,r_a)\cap B=\varnothing.
$$
The case
$$
b\le a
$$
is symmetric.
Thus
$$
U\cap V=\varnothing.
$$
Hence
$$
\RR_\ell
$$
is normal.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\RR_\ell
$$
is
$$
T_4.
$$


::: pf-proof

By step [](#s1-7){.pf-ref} it is $T_1$, and by step [](#s1-8){.pf-ref} it is normal.
Thus it is $T_4$.
In fact, the Sorgenfrey line is perfectly normal, but $T_4$ is the highest
level requested in the standard finite hierarchy.

:::

:::

::: {.pf-step #s1-10}

The lower-limit line is not compact.


::: pf-proof

The family
$$
\mathcal U
=
\{[n,n+2):n\in\ZZ\}
$$
is an open cover of
$$
\RR_\ell.
$$
Indeed, every real number belongs to one of these intervals.

Any finite subfamily is bounded above and below, so it cannot cover all of
$$
\RR.
$$
Thus no finite subcover exists.

:::

:::

::: {.pf-step #s1-11}

Therefore, for the lower-limit line,
$$
\boxed{
\text{compact: no},
\qquad
\text{largest }T_i:T_4.
}
$$


::: pf-proof

Combine steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

The subspace
$$
[0,1]\subset\RR_\ell
$$
is
$$
T_4.
$$


::: pf-proof

The interval
$$
[0,1]
$$
is closed in
$$
\RR_\ell.
$$
Indeed,
$$
(-\infty,0)
$$
and
$$
(1,\infty)
$$
are open in the lower-limit topology, so the complement is open.

A closed subspace of a normal space is normal.
Also the $T_1$ property is hereditary to subspaces.
By steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref},
$$
\RR_\ell
$$
is normal and $T_1$.
Hence
$$
[0,1]
$$
is $T_4$.

:::

:::

::: {.pf-step #s1-13}

The subspace
$$
[0,1]\subset\RR_\ell
$$
is not compact.


::: pf-proof

For
$$
n\ge2,
$$
let
$$
U_n
=
\left[
0,
1-\frac1n
\right).
$$
Each $U_n$ is open in the subspace topology.
Also
$$
\{1\}
=
[1,2)\cap[0,1]
$$
is open in the subspace.

The family
$$
\{U_n:n\ge2\}
\cup
\{\{1\}\}
$$
covers $[0,1]$ because
$$
\bigcup_{n\ge2}U_n
=
[0,1).
$$

Take any finite subfamily.
Among the chosen $U_n$, let
$$
N
$$
be the largest index.
Their union is contained in
$$
\left[
0,
1-\frac1N
\right).
$$
Even after adding
$$
\{1\},
$$
the interval
$$
\left[
1-\frac1N,
1
\right)
$$
remains uncovered.
Thus there is no finite subcover.

:::

:::

::: {.pf-step #s1-14}

Therefore, for
$$
[0,1]\subset\RR_\ell,
$$
$$
\boxed{
\text{compact: no},
\qquad
\text{largest }T_i:T_4.
}
$$


::: pf-proof

Combine steps [](#s1-12){.pf-ref} through [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

The complete table is
$$
\boxed{
\begin{array}{c|cc}
\text{space}
&\text{compact?}
&\text{largest }T_i\\
\hline
\text{excluded-point }\RR
&\mathrm{yes}
&T_0\\
\text{included-point }\RR
&\mathrm{no}
&T_0\\
\RR_\ell
&\mathrm{no}
&T_4\\
[0,1]\subset\RR_\ell
&\mathrm{no}
&T_4
\end{array}
}
$$


::: pf-proof

Collect steps [](#s1-3){.pf-ref}, [](#s1-6){.pf-ref}, and [](#s1-11){.pf-ref}, and [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} gives all requested classifications.

:::

:::

:::
