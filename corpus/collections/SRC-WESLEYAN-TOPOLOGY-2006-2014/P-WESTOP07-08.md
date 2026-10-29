---
schema: qual/card@1
id: P-WESTOP07-08
kind: problem
title: Covering-space proof that $\pi_1(S^1)\cong\ZZ$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Explain the covering-space proof of the fundamental group of the circle $S^1$, formulating the proof as generally as possible without asserting more generality than the argument supports.
:::

::: {.solution}

Use the covering map
$$
p:\RR\to S^1,
\qquad
p(t)=e^{2\pi it},
$$
with basepoints
$$
0\in\RR
$$
and
$$
1\in S^1.
$$

::: pf

::: pf-step

Every based loop
$$
\gamma:(I,\partial I)\to(S^1,1)
$$
has a unique lift
$$
\widetilde\gamma:I\to\RR
$$
with
$$
\widetilde\gamma(0)=0.
$$


::: pf-proof

This is the path-lifting theorem for covering spaces, with the initial point in the fiber over
$$
1.
$$

:::

:::

::: pf-step

The endpoint of such a lift is an integer:
$$
\boxed{
\widetilde\gamma(1)\in\ZZ}.
$$


::: pf-proof

Since
$$
\gamma(1)=1,
$$
one has
$$
p(\widetilde\gamma(1))
=
1.
$$
The fiber over
$$
1
$$
is
$$
p^{-1}(1)
=
\ZZ.
$$

:::

:::

::: {.pf-step #s1-3}

If two based loops are based-homotopic, then their lifts beginning at
$$
0
$$
have the same endpoint.


::: pf-proof

Let
$$
H:I\times I\to S^1
$$
be a based homotopy from
$$
\gamma_0
$$
to
$$
\gamma_1.
$$
Thus
$$
H(0,s)
=
H(1,s)
=
1
$$
for every
$$
s.
$$

By the homotopy-lifting theorem, there is a unique lift
$$
\widetilde H:I\times I\to\RR
$$
with
$$
\widetilde H(0,s)=0.
$$
For each
$$
s,
$$
the point
$$
\widetilde H(1,s)
$$
lies in the discrete fiber
$$
\ZZ.
$$
The map
$$
s\longmapsto\widetilde H(1,s)
$$
is continuous from the connected interval
$$
I
$$
to the discrete space
$$
\ZZ,
$$
so it is constant. Therefore the endpoints at
$$
s=0
$$
and
$$
s=1
$$
agree.

:::

:::

::: pf-step

Hence the lift endpoint defines a map
$$
\Phi:
\pi_1(S^1,1)
\to
\ZZ,
\qquad
\Phi([\gamma])
=
\widetilde\gamma(1).
$$


::: pf-proof

Step [](#s1-3){.pf-ref} shows that the endpoint depends only on the based homotopy class
$$
[\gamma].
$$
Thus
$$
\Phi
$$
is well defined.

:::

:::

::: {.pf-step #s1-5}

The map
$$
\Phi
$$
is a homomorphism.


::: pf-proof

Let
$$
\gamma,\eta
$$
be based loops with lift endpoints
$$
m
=
\Phi([\gamma]),
\qquad
n
=
\Phi([\eta]).
$$
Let
$$
\widetilde\gamma
$$
be the lift of
$$
\gamma
$$
starting at
$$
0,
$$
and let
$$
\widetilde\eta
$$
be the lift of
$$
\eta
$$
starting at
$$
0.
$$

Because
$$
p(t+m)=p(t)
$$
for every
$$
m\in\ZZ,
$$
the path
$$
t\longmapsto m+\widetilde\eta(t)
$$
is the lift of
$$
\eta
$$
starting at
$$
m.
$$
Therefore the lift of the concatenation
$$
\gamma*\eta
$$
starting at
$$
0
$$
is obtained by concatenating
$$
\widetilde\gamma
$$
with
$$
m+\widetilde\eta.
$$
Its endpoint is
$$
m+n.
$$
Hence
$$
\Phi([\gamma][\eta])
=
m+n
=
\Phi([\gamma])
+\Phi([\eta]).
$$

:::

:::

::: {.pf-step #s1-6}

The map
$$
\Phi
$$
is surjective.


::: pf-proof

For every
$$
n\in\ZZ,
$$
define
$$
\gamma_n(t)
=
e^{2\pi int}.
$$
Its lift beginning at
$$
0
$$
is
$$
\widetilde\gamma_n(t)=nt,
$$
whose endpoint is
$$
n.
$$
Thus
$$
\Phi([\gamma_n])=n.
$$

:::

:::

::: {.pf-step #s1-7}

The map
$$
\Phi
$$
is injective.


::: pf-proof

Suppose
$$
\Phi([\gamma])=0.
$$
Then the lift
$$
\widetilde\gamma
$$
begins and ends at
$$
0,
$$
so it is a loop in
$$
\RR.
$$
Since
$$
\RR
$$
is contractible, this loop is based-null-homotopic. Let
$$
\widetilde H
$$
be a based null-homotopy.
Composing with
$$
p
$$
gives a based null-homotopy
$$
p\circ\widetilde H
$$
of
$$
\gamma.
$$
Hence
$$
[\gamma]=1
$$
in
$$
\pi_1(S^1,1).
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\pi_1(S^1,1)
\cong
\ZZ}.
$$


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} show that
$$
\Phi
$$
is a bijective homomorphism.

:::

:::

::: {.pf-step #s1-9}

The general part of the argument is the following endpoint-of-lifts statement.


::: pf-proof

Let
$$
p:(\widetilde X,\widetilde x_0)
\to
(X,x_0)
$$
be a covering map with
$$
\widetilde X
$$
path-connected and simply connected.

For every based loop
$$
\gamma
$$
in
$$
X,
$$
lift it uniquely from
$$
\widetilde x_0.
$$
The endpoint lies in the fiber
$$
p^{-1}(x_0).
$$
The homotopy-lifting argument of step [](#s1-3){.pf-ref} shows that the endpoint depends only on
$$
[\gamma].
$$

Conversely, any point
$$
\widetilde x
\in
p^{-1}(x_0)
$$
can be joined to
$$
\widetilde x_0
$$
by a path because
$$
\widetilde X
$$
is path-connected; projecting this path gives a based loop whose lift endpoint is
$$
\widetilde x.
$$

If two loop classes have the same lift endpoint, concatenate one lifted path with the reverse of the other. This gives a loop in
$$
\widetilde X,
$$
which is null-homotopic because
$$
\widetilde X
$$
is simply connected. Projecting the null-homotopy shows that the two original loops are based-homotopic.

Thus there is a canonical bijection of sets
$$
\pi_1(X,x_0)
\longleftrightarrow
p^{-1}(x_0).
$$
In general this statement alone does not put a canonical group law on the fiber. In the circle example, the fiber is already canonically the additive group
$$
\ZZ,
$$
and translation invariance of the covering makes concatenation correspond to addition, as shown in step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} computes the fundamental group of the circle, and step [](#s1-9){.pf-ref} states exactly the general covering-space mechanism used in the proof without claiming more structure on a general fiber than the argument supplies.

:::

:::

:::
