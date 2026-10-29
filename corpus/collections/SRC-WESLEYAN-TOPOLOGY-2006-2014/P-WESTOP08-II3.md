---
schema: qual/card@1
id: P-WESTOP08-II3
kind: problem
title: Change of basepoint isomorphism for the fundamental group
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
State the definition of a path-connected space. Let $X$ be path-connected and let $x_0,x_1\in X$. Describe in detail an isomorphism
$$
\pi_1(X,x_0)\longrightarrow\pi_1(X,x_1).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A topological space $X$ is path-connected if for every pair of points
$$
x,y\in X,
$$
there exists a continuous map
$$
\eta:[0,1]\to X
$$
such that
$$
\eta(0)=x,
\qquad
\eta(1)=y.
$$


::: pf-proof

This is the definition of path-connectedness.

:::

:::

::: {.pf-step #s1-2}

Since $X$ is path-connected, choose a path
$$
\eta:[0,1]\to X
$$
from $x_1$ to $x_0$:
$$
\eta(0)=x_1,
\qquad
\eta(1)=x_0.
$$
Let
$$
\bar\eta(t)
=
\eta(1-t)
$$
be the reverse path.


::: pf-proof

Existence of $\eta$ follows from path-connectedness.
The reverse path runs from
$$
x_0
$$
back to
$$
x_1.
$$

:::

:::

::: {.pf-step #s1-3}

For a loop
$$
\gamma
$$
based at $x_0$, define
$$
\Phi([\gamma])
\coloneqq
[\eta*\gamma*\bar\eta]
\in
\pi_1(X,x_1).
$$


::: pf-proof

The concatenation starts at
$$
x_1,
$$
follows $\eta$ to $x_0$, traverses the loop $\gamma$, and then follows
$\bar\eta$ back to $x_1$.
Hence it is a loop based at $x_1$.

:::

:::

::: {.pf-step #s1-4}

The map
$$
\Phi
$$
is well defined on homotopy classes.


::: pf-proof

Suppose
$$
\gamma_0
\simeq
\gamma_1
$$
rel endpoints.
Let
$$
H:[0,1]\times[0,1]\to X
$$
be such a path homotopy.

Concatenate the fixed path $\eta$ to the beginning of every path
$$
H(-,t)
$$
and the fixed path $\bar\eta$ to the end.
This produces a path homotopy rel endpoints between
$$
\eta*\gamma_0*\bar\eta
$$
and
$$
\eta*\gamma_1*\bar\eta.
$$
Thus the output class depends only on
$$
[\gamma].
$$

:::

:::

::: {.pf-step #s1-5}

The map $\Phi$ is a group homomorphism.


::: pf-proof

Let
$$
[\gamma_1],[\gamma_2]
\in
\pi_1(X,x_0).
$$
Then
$$
\begin{aligned}
\Phi([\gamma_1][\gamma_2])
&=
[\eta*\gamma_1*\gamma_2*\bar\eta].
\end{aligned}
$$

On the other hand,
$$
\begin{aligned}
\Phi([\gamma_1])
\Phi([\gamma_2])
&=
[\eta*\gamma_1*\bar\eta
*
\eta*\gamma_2*\bar\eta].
\end{aligned}
$$
The middle concatenation
$$
\bar\eta*\eta
$$
is path-homotopic rel endpoints to the constant loop at $x_0$.
Therefore
$$
[\eta*\gamma_1*\bar\eta
*
\eta*\gamma_2*\bar\eta]
=
[\eta*\gamma_1*\gamma_2*\bar\eta].
$$
Hence
$$
\Phi([\gamma_1][\gamma_2])
=
\Phi([\gamma_1])\Phi([\gamma_2]).
$$

:::

:::

::: {.pf-step #s1-6}

Define
$$
\Psi:
\pi_1(X,x_1)
\to
\pi_1(X,x_0)
$$
by
$$
\Psi([\lambda])
\coloneqq
[\bar\eta*\lambda*\eta].
$$


::: pf-proof

This is the same construction using the path
$$
\bar\eta:x_0\to x_1.
$$
By the same argument as steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref}, it is a well-defined group
homomorphism.

:::

:::

::: {.pf-step #s1-7}

The maps $\Phi$ and $\Psi$ are inverse to each other.


::: pf-proof

For
$$
[\gamma]\in\pi_1(X,x_0),
$$
$$
\begin{aligned}
\Psi(\Phi([\gamma]))
&=
[\bar\eta*\eta*\gamma*\bar\eta*\eta].
\end{aligned}
$$
Both
$$
\bar\eta*\eta
$$
and
$$
\bar\eta*\eta
$$
are homotopic rel endpoints to the constant loop at $x_0$, so
$$
\Psi(\Phi([\gamma]))
=
[\gamma].
$$

Similarly, for
$$
[\lambda]\in\pi_1(X,x_1),
$$
$$
\Phi(\Psi([\lambda]))
=
[\eta*\bar\eta*\lambda*\eta*\bar\eta]
=
[\lambda].
$$
Thus
$$
\Psi\circ\Phi
=
\operatorname{id},
\qquad
\Phi\circ\Psi
=
\operatorname{id}.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\Phi:
\pi_1(X,x_0)
\xrightarrow{\cong}
\pi_1(X,x_1)
}
$$
is an isomorphism.


::: pf-proof

Step [](#s1-5){.pf-ref} gives that $\Phi$ is a homomorphism, and step [](#s1-7){.pf-ref} gives its
two-sided inverse.

:::

:::

::: pf-step

The isomorphism depends on the chosen path $\eta$, but only up to an
inner automorphism of the target fundamental group.


::: pf-proof

If
$$
\eta'
$$
is another path from $x_1$ to $x_0$, then
$$
\eta'*\bar\eta
$$
is a loop at $x_1$.
The two basepoint-change maps differ by conjugation by its homotopy class.
Thus there is no canonical basepoint-independent isomorphism in general,
although the fundamental groups are always isomorphic for path-connected
$X$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and steps [](#s1-2){.pf-ref} through [](#s1-8){.pf-ref} construct
the isomorphism in full detail.

:::

:::

:::
