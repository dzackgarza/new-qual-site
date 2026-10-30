---
schema: qual/card@1
id: P-UCLAB11S-06
kind: problem
title: Normal equations characterize least-squares minimizers
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Let $V,W$ be finite-dimensional real inner-product spaces, let $A:V\to W$ be linear, and let $w\in W$.
Show that the vectors $v\in V$ minimizing
$$
\norm{Av-w}
$$
are exactly the solutions of the normal equation
$$
A^*Av=A^*w.
$$
:::

::: {.solution}

For
$$
v\in V,
$$
define the residual
$$
r_v=Av-w.
$$

::: pf

::: {.pf-step #s1-1}

The normal equation
$$
A^*Av=A^*w
$$
is equivalent to
$$
\boxed{A^*r_v=0}.
$$


::: pf-proof

By linearity,
$$
A^*r_v
=
A^*(Av-w)
=
A^*Av-A^*w.
$$
Thus the displayed vector vanishes exactly when the normal equation holds.

:::

:::

::: {.pf-step #s1-2}

The condition
$$
A^*r_v=0
$$
is equivalent to
$$
r_v\perp\operatorname{im}A.
$$


::: pf-proof

For every
$$
h\in V,
$$
the defining property of the adjoint gives
$$
\langle r_v,Ah\rangle_W
=
\langle A^*r_v,h\rangle_V.
$$
Thus
$$
A^*r_v=0
$$
if and only if
$$
\langle r_v,Ah\rangle_W=0
$$
for every $h$, which is exactly orthogonality to $\operatorname{im}A$.

:::

:::

::: {.pf-step #s1-3}

Suppose $v$ satisfies the normal equation.
Then for every $u\in V$,
$$
Au-w
=
r_v+A(u-v),
$$
and the two terms on the right are orthogonal.


::: pf-proof

The algebraic identity is
$$
Au-w
=
(Av-w)+A(u-v)
=
r_v+A(u-v).
$$
By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, the normal equation implies
$$
r_v\perp\operatorname{im}A.
$$
Since
$$
A(u-v)\in\operatorname{im}A,
$$
the two summands are orthogonal.

:::

:::

::: {.pf-step #s1-4}

If $v$ satisfies the normal equation, then
$$
\norm{Au-w}^2
=
\norm{Av-w}^2
+
\norm{A(u-v)}^2
$$
for every $u\in V$.


::: pf-proof

Apply the Pythagorean theorem to the orthogonal decomposition in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Every solution of the normal equation minimizes
$$
\norm{Av-w}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives
$$
\norm{Au-w}^2
\ge
\norm{Av-w}^2
$$
for every $u\in V$.
Taking square roots gives
$$
\norm{Au-w}
\ge
\norm{Av-w}.
$$
Thus $v$ is a minimizer.

:::

:::

::: {.pf-step #s1-6}

Conversely, suppose $v$ minimizes
$$
\norm{Av-w}.
$$
Fix
$$
h\in V
$$
and define
$$
\phi(t)
=
\norm{A(v+th)-w}^2.
$$
Then $\phi$ has a minimum at
$$
t=0.
$$


::: pf-proof

For every real $t$,
$$
v+th\in V.
$$
Since $v$ is a global minimizer,
$$
\norm{Av-w}
\le
\norm{A(v+th)-w}.
$$
Squaring preserves the inequality because both sides are nonnegative.
Thus
$$
\phi(0)\le\phi(t)
$$
for every $t$.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\phi'(0)
=
2\langle r_v,Ah\rangle_W.
$$


::: pf-proof

Since
$$
A(v+th)-w
=
r_v+tAh,
$$
one has
$$
\begin{aligned}
\phi(t)
&=
\norm{r_v+tAh}^2\\
&=
\norm{r_v}^2
+
2t\langle r_v,Ah\rangle
+
t^2\norm{Ah}^2.
\end{aligned}
$$
Differentiate at $t=0$.

:::

:::

::: {.pf-step #s1-8}

For every
$$
h\in V,
$$
one has
$$
\langle r_v,Ah\rangle_W=0.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, $\phi$ has a minimum at $0$.
Therefore
$$
\phi'(0)=0.
$$
Using step [](#s1-7){.pf-ref},
$$
2\langle r_v,Ah\rangle_W=0.
$$

:::

:::

::: {.pf-step #s1-9}

Every minimizer satisfies the normal equation.


::: pf-proof

Step [](#s1-8){.pf-ref} says
$$
r_v\perp\operatorname{im}A.
$$
By step [](#s1-2){.pf-ref},
$$
A^*r_v=0.
$$
By step [](#s1-1){.pf-ref}, this is equivalent to
$$
A^*Av=A^*w.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
v\text{ minimizes }\norm{Av-w}
\iff
A^*Av=A^*w.
}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} proves the reverse implication from the normal equation to minimality.
Step [](#s1-9){.pf-ref} proves the converse.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required characterization.

:::

:::

:::
