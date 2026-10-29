---
schema: qual/card@1
id: P-WESTOP05-06
kind: problem
title: Define the fundamental group and sketch the proof that it is a group
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Given a pointed space $(X,x_0)$, define the fundamental group
$$
\pi_1(X,x_0)
$$
and sketch the proof that the resulting set of homotopy classes is in fact a group.
:::

::: {.solution}

Let
$$
I=[0,1].
$$

::: pf

::: pf-step

A based loop at $x_0$ is a continuous map
$$
\gamma:I\to X
$$
such that
$$
\boxed{
\gamma(0)=\gamma(1)=x_0}.
$$


::: pf-proof

This is the standard definition of a loop based at $x_0$.

:::

:::

::: {.pf-step #s1-2}

Two based loops $\gamma_0,\gamma_1$ are equivalent if there is a
homotopy
$$
H:I\times I\to X
$$
such that
$$
H(s,0)=\gamma_0(s),
\qquad
H(s,1)=\gamma_1(s),
$$
and
$$
\boxed{
H(0,t)=H(1,t)=x_0}
$$
for every $t\in I$.


::: pf-proof

This is homotopy relative to the endpoints.

:::

:::

::: pf-step

The fundamental group is the set
$$
\boxed{
\pi_1(X,x_0)
=
\{\text{based loops at }x_0\}
/\simeq_{\partial I}}.
$$


::: pf-proof

The equivalence relation is based homotopy from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

For based loops $\alpha,\beta$, define their concatenation
$$
\alpha*\beta:I\to X
$$
by
$$
\boxed{
(\alpha*\beta)(s)
=
\begin{cases}
\alpha(2s),&0\le s\le1/2,\\[3pt]
\beta(2s-1),&1/2\le s\le1.
\end{cases}}
$$


::: pf-proof

At $s=1/2$, both formulas equal
$$
\alpha(1)=x_0=\beta(0),
$$
so the pasting lemma gives continuity. The endpoints are $x_0$, so it is a
based loop.

:::

:::

::: {.pf-step #s1-5}

Define multiplication on homotopy classes by
$$
\boxed{
[\alpha]\,[\beta]
=
[\alpha*\beta]}.
$$


::: pf-proof

Well-definedness is proved in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The multiplication in step [](#s1-5){.pf-ref} is well defined.


::: pf-proof

Suppose
$$
\alpha\simeq_{\partial I}\alpha'
$$
through $H_\alpha$, and
$$
\beta\simeq_{\partial I}\beta'
$$
through $H_\beta$.

Define
$$
H(s,t)
=
\begin{cases}
H_\alpha(2s,t),&0\le s\le1/2,\\[3pt]
H_\beta(2s-1,t),&1/2\le s\le1.
\end{cases}
$$
The two formulas agree at $s=1/2$ because both homotopies fix the
basepoint. Thus $H$ is a based homotopy
$$
\alpha*\beta
\simeq_{\partial I}
\alpha'*\beta'.
$$
Hence the class depends only on $[\alpha]$ and $[\beta]$.

:::

:::

::: pf-step

Let
$$
c(s)=x_0
$$
be the constant loop.


::: pf-proof

This is a based loop.

:::

:::

::: {.pf-step #s1-8}

For every loop $\alpha$,
$$
\boxed{
[c][\alpha]=[\alpha]}.
$$


::: pf-proof

The loop $c*\alpha$ stays at $x_0$ on the first half of the interval and
then traverses $\alpha$ on the second half.

It differs from $\alpha$ only by a monotone reparametrization that inserts
a constant initial segment. Any two nondecreasing continuous
reparametrizations
$$
\rho_0,\rho_1:I\to I
$$
with
$$
\rho_j(0)=0,\qquad \rho_j(1)=1
$$
are homotopic through
$$
\rho_t=(1-t)\rho_0+t\rho_1.
$$
Thus
$$
H(s,t)=\alpha(\rho_t(s))
$$
gives a based homotopy from $c*\alpha$ to $\alpha$.

:::

:::

::: {.pf-step #s1-9}

Likewise,
$$
\boxed{
[\alpha][c]=[\alpha]}.
$$


::: pf-proof

The same reparametrization argument removes the constant terminal segment of
$\alpha*c$.

:::

:::

::: {.pf-step #s1-10}

Thus
$$
\boxed{[c]}
$$
is the identity element.


::: pf-proof

Combine steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-step

Define the reverse loop
$$
\boxed{
\overline\alpha(s)=\alpha(1-s)}.
$$


::: pf-proof

It begins and ends at $x_0$, so it is a based loop.

:::

:::

::: {.pf-step #s1-12}

One has
$$
\boxed{
[\alpha][\overline\alpha]=[c]}.
$$


::: pf-proof

The concatenation $\alpha*\overline\alpha$ traverses $\alpha$ and then
retraces it.

Define
$$
H(s,t)
=
\begin{cases}
\alpha\!\left(2s(1-t)\right),
&0\le s\le1/2,\\[4pt]
\alpha\!\left(2(1-s)(1-t)\right),
&1/2\le s\le1.
\end{cases}
$$
At $t=0$, this is $\alpha*\overline\alpha$. At $t=1$, it is the
constant loop at $\alpha(0)=x_0$. The two pieces agree at $s=1/2$, and
the endpoints remain $x_0$. Hence this is a based nullhomotopy.

:::

:::

::: {.pf-step #s1-13}

Likewise,
$$
\boxed{
[\overline\alpha][\alpha]=[c]}.
$$


::: pf-proof

Apply step [](#s1-12){.pf-ref} to the loop $\overline\alpha$, whose reverse is
$\alpha$.

:::

:::

::: {.pf-step #s1-14}

Thus
$$
\boxed{
[\alpha]^{-1}
=
[\overline\alpha]}.
$$


::: pf-proof

Steps [](#s1-12){.pf-ref} through [](#s1-13){.pf-ref} show that $[\overline\alpha]$ is a two-sided inverse.

:::

:::

::: pf-step

For based loops $\alpha,\beta,\gamma$, the loops
$$
(\alpha*\beta)*\gamma
$$
and
$$
\alpha*(\beta*\gamma)
$$
traverse the same three paths in the same order, but at different speeds.


::: pf-proof

The first loop allocates one quarter of the interval to $\alpha$, one
quarter to $\beta$, and one half to $\gamma$. The second allocates one
half to $\alpha$, one quarter to $\beta$, and one quarter to $\gamma$.

:::

:::

::: {.pf-step #s1-16}

These two loops are based-homotopic.


::: pf-proof

Let
$$
p_0,p_1:I\to[0,3]
$$
be the piecewise-linear nondecreasing parametrizations that encode the
traversal schedules of
$$
(\alpha*\beta)*\gamma
$$
and
$$
\alpha*(\beta*\gamma),
$$
respectively, where the intervals
$$
[0,1],\quad[1,2],\quad[2,3]
$$
correspond to $\alpha,\beta,\gamma$.

The convex interpolation
$$
p_t=(1-t)p_0+tp_1
$$
is still nondecreasing and fixes the endpoints. Composing the common
three-stage path with $p_t$ gives a based homotopy between the two
concatenations.

:::

:::

::: {.pf-step #s1-17}

Therefore multiplication is associative:
$$
\boxed{
([\alpha][\beta])[\gamma]
=
[\alpha]([\beta][\gamma])}.
$$


::: pf-proof

By step [](#s1-16){.pf-ref},
$$
[(\alpha*\beta)*\gamma]
=
[\alpha*(\beta*\gamma)].
$$

:::

:::

::: {.pf-step #s1-18}

Consequently,
$$
\boxed{
\pi_1(X,x_0)
}
$$
is a group under concatenation.


::: pf-proof

Closure and well-definedness are steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}, the identity is step
[](#s1-10){.pf-ref}, inverses are step [](#s1-14){.pf-ref}, and associativity is step [](#s1-17){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-18){.pf-ref} proves that the homotopy classes of based loops form the
fundamental group.

:::

:::

:::
