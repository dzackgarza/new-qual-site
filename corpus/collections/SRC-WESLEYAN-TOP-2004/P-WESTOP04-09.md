---
schema: qual/card@1
id: P-WESTOP04-09
kind: problem
title: Compactness and countable compactness of ordinal spaces $W(\xi)$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For an ordinal $\xi$, let
$$
W(\xi)=\{\sigma:\sigma<\xi\}
$$
with its usual order topology. Equivalently, use the subbasis consisting of
$$
A(\eta)=\{\sigma:\eta<\sigma<\xi\},
\qquad
B(\eta)=\{\sigma:\sigma<\eta\}
$$
for $\eta<\xi$.

1. Determine exactly for which ordinals $\xi$ the space $W(\xi)$ is compact.
2. Determine exactly for which ordinals $\xi$ it is countably compact.

Prove both assertions.
:::

::: {.solution}

Write
$$
\operatorname{cf}(\xi)
$$
for the cofinality of the ordinal $\xi$.

::: pf

::: {.pf-step #s1-1}

For every ordinal $\alpha$, the closed ordinal interval
$$
[0,\alpha]
$$
with the order topology is compact.


::: pf-proof

Proceed by transfinite induction on $\alpha$.

If
$$
\alpha=0,
$$
the space has one point and is compact.

Assume
$$
[0,\beta]
$$
is compact for every
$$
\beta<\alpha.
$$
Let
$$
\mathcal U
$$
be an open cover of
$$
[0,\alpha].
$$
Choose
$$
U\in\mathcal U
$$
with
$$
\alpha\in U.
$$
If
$$
\alpha
$$
is a successor, or more generally simply by the form of neighborhoods of the maximal point in an ordinal interval, there exists
$$
\beta<\alpha
$$
such that
$$
(\beta,\alpha]
\subseteq
U.
$$
By the induction hypothesis,
$$
[0,\beta]
$$
has a finite subcover from
$$
\mathcal U.
$$
Adding
$$
U
$$
covers all of
$$
[0,\alpha].
$$
Thus
$$
[0,\alpha]
$$
is compact.

:::

:::

::: {.pf-step #s1-2}

If
$$
\xi=\alpha+1
$$
is a successor ordinal, then
$$
\boxed{W(\xi)\text{ is compact}.}
$$


::: pf-proof

By definition,
$$
W(\alpha+1)
=
\{
\sigma:
\sigma<\alpha+1
\}
=
[0,\alpha].
$$
Step [](#s1-1){.pf-ref} shows this space is compact.

:::

:::

::: {.pf-step #s1-3}

If
$$
\xi
$$
is a nonzero limit ordinal, then
$$
W(\xi)
$$
is not compact.


::: pf-proof

Consider the family
$$
\mathcal U
\coloneqq
\{
B(\eta):
0<\eta<\xi
\},
$$
where
$$
B(\eta)
=
\{
\sigma:
\sigma<\eta
\}.
$$
Because
$$
\xi
$$
is a limit ordinal, for every
$$
\sigma<\xi
$$
one has
$$
\sigma+1<\xi.
$$
Hence
$$
\sigma
\in
B(\sigma+1),
$$
so
$$
\mathcal U
$$
covers
$$
W(\xi).
$$

No finite subfamily covers. Indeed, if
$$
B(\eta_1),\ldots,B(\eta_n)
$$
are chosen and
$$
\eta
=
\max\{\eta_1,\ldots,\eta_n\},
$$
then their union is
$$
B(\eta),
$$
which misses
$$
\eta
$$
itself and every larger ordinal below
$$
\xi.
$$
Thus
$$
W(\xi)
$$
is not compact.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
W(\xi)\text{ is compact}
\iff
\xi=0
\text{ or }
\xi\text{ is a successor ordinal}.}
$$


::: pf-proof

The empty space
$$
W(0)=\varnothing
$$
is compact. Step [](#s1-2){.pf-ref} proves compactness for successors, and step [](#s1-3){.pf-ref} excludes every nonzero limit ordinal.

:::

:::

::: {.pf-step #s1-5}

If
$$
\operatorname{cf}(\xi)=\omega,
$$
then
$$
W(\xi)
$$
is not countably compact.


::: pf-proof

Choose a strictly increasing cofinal sequence
$$
\eta_0<\eta_1<\eta_2<\cdots<\xi
$$
with
$$
\sup_n\eta_n=\xi.
$$
The countable family
$$
\{
B(\eta_n):
n\in\NN
\}
$$
covers
$$
W(\xi):
$$
for every
$$
\sigma<\xi,
$$
cofinality gives some
$$
n
$$
with
$$
\sigma<\eta_n,
$$
so
$$
\sigma\in B(\eta_n).
$$

No finite subfamily covers, because a finite union is
$$
B(\eta_N)
$$
for the largest selected index
$$
N,
$$
and
$$
\eta_N<\xi.
$$
Hence there is a countable open cover with no finite subcover.

:::

:::

::: {.pf-step #s1-6}

Suppose
$$
\operatorname{cf}(\xi)>\omega.
$$
Then every countable open cover of
$$
W(\xi)
$$
has a finite subcover.


::: pf-proof

Let
$$
\mathcal U
=
\{
U_0,U_1,U_2,\ldots
\}
$$
be a countable open cover of
$$
W(\xi).
$$
Assume toward a contradiction that no finite subfamily covers.

For each
$$
n\ge0,
$$
choose
$$
x_n
\in
W(\xi)
\setminus
\bigcup_{j=0}^{n}U_j.
$$
Set
$$
\beta
\coloneqq
\sup_{n<\omega}(x_n+1).
$$
The set
$$
\{
x_n+1:
n<\omega
\}
$$
is countable. Since
$$
\operatorname{cf}(\xi)>\omega,
$$
its supremum is still below
$$
\xi:
$$
$$
\beta<\xi.
$$
Thus every
$$
x_n
$$
lies in the compact ordinal interval
$$
[0,\beta].
$$

The family
$$
\mathcal U
$$
restricts to an open cover of
$$
[0,\beta].
$$
By step [](#s1-1){.pf-ref}, there are indices
$$
i_1,\ldots,i_k
$$
such that
$$
[0,\beta]
\subseteq
U_{i_1}\cup\cdots\cup U_{i_k}.
$$
Let
$$
N
\coloneqq
\max\{i_1,\ldots,i_k\}.
$$
Then
$$
x_N
$$
lies in
$$
[0,\beta],
$$
so it belongs to one of the selected
$$
U_{i_j}.
$$
But every
$$
i_j\le N,
$$
whereas
$$
x_N
$$
was chosen outside
$$
U_0\cup\cdots\cup U_N.
$$
This is a contradiction.

:::

:::

::: {.pf-step #s1-7}

If
$$
\xi=0
$$
or
$$
\xi
$$
is a successor ordinal, then
$$
W(\xi)
$$
is countably compact.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
W(\xi)
$$
is compact in these cases. Every compact space is countably compact.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
W(\xi)\text{ is countably compact}
\iff
\operatorname{cf}(\xi)\ne\omega.}
$$


::: pf-proof

If
$$
\operatorname{cf}(\xi)=\omega,
$$
step [](#s1-5){.pf-ref} gives failure of countable compactness.

If
$$
\operatorname{cf}(\xi)>\omega,
$$
step [](#s1-6){.pf-ref} proves countable compactness.

The remaining cases are
$$
\xi=0
$$
and successor ordinals, whose cofinality is not
$$
\omega
$$
and which are countably compact by step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the complete compactness classification, and step [](#s1-8){.pf-ref} gives the complete countable-compactness classification.

:::

:::

:::
