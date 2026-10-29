---
schema: qual/card@1
id: P-UCLAB09S-12
kind: problem
title: Local divergence identity from flux over all balls
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Let $F:\RR^3\to\RR^3$ and $\rho:\RR^3\to\RR$ be smooth.
Prove that
$$
\operatorname{div}F=\rho
$$
at every point if and only if
$$
\iint_{\partial\Omega}F\cdot dS
=
\iiint_\Omega \rho\,dx\,dy\,dz
$$
for every ball $\Omega$ of every positive radius and center.
You may use the standard theorems of vector calculus without proof.
:::

::: {.solution}

Define
$$
G=\operatorname{div}F-\rho.
$$
Since $F$ and $\rho$ are smooth, $G$ is continuous.

::: pf

::: {.pf-step #s1-1}

Suppose first that
$$
\operatorname{div}F=\rho
$$
everywhere.
Then for every ball $\Omega$,
$$
\iint_{\partial\Omega}F\cdot dS
=
\iiint_\Omega\rho\,dx\,dy\,dz.
$$


::: pf-proof

The divergence theorem gives
$$
\iint_{\partial\Omega}F\cdot dS
=
\iiint_\Omega
\operatorname{div}F
\,dx\,dy\,dz.
$$
Under the hypothesis
$$
\operatorname{div}F=\rho,
$$
the right side equals
$$
\iiint_\Omega\rho\,dx\,dy\,dz.
$$

:::

:::

::: {.pf-step #s1-2}

Conversely, suppose that for every ball $\Omega$,
$$
\iint_{\partial\Omega}F\cdot dS
=
\iiint_\Omega\rho\,dx\,dy\,dz.
$$
Then
$$
\iiint_\Omega G\,dx\,dy\,dz=0
$$
for every ball $\Omega$.


::: pf-proof

By the divergence theorem,
$$
\iint_{\partial\Omega}F\cdot dS
=
\iiint_\Omega\operatorname{div}F\,dx\,dy\,dz.
$$
Subtract the assumed identity:
$$
\iiint_\Omega
\bigl(
\operatorname{div}F-\rho
\bigr)
\,dx\,dy\,dz
=0.
$$
This is
$$
\iiint_\Omega G=0.
$$

:::

:::

::: {.pf-step #s1-3}

Suppose, for contradiction, that
$$
G(p)>0
$$
at some point
$$
p\in\RR^3.
$$
Then there exists a ball $\Omega$ centered at $p$ such that
$$
G>0
$$
throughout $\Omega$.


::: pf-proof

Since $G$ is continuous and
$$
G(p)>0,
$$
there exists $r>0$ such that
$$
|G(q)-G(p)|
<
\frac12G(p)
$$
whenever
$$
\|q-p\|<r.
$$
Hence on the ball
$$
\Omega=B(p,r),
$$
one has
$$
G(q)
>
\frac12G(p)
>
0.
$$

:::

:::

::: {.pf-step #s1-4}

The situation in step [](#s1-3){.pf-ref} contradicts step [](#s1-2){.pf-ref}.


::: pf-proof

On the ball $\Omega$ from step [](#s1-3){.pf-ref},
$$
G(q)
>
\frac12G(p)
$$
for every $q\in\Omega$.
Therefore
$$
\iiint_\Omega G
>
\frac12G(p)\operatorname{vol}(\Omega)
>
0.
$$
But step [](#s1-2){.pf-ref} says that the integral of $G$ over every ball is zero.
This is a contradiction.

:::

:::

::: {.pf-step #s1-5}

No point can satisfy
$$
G(p)<0.
$$


::: pf-proof

Apply steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} to the continuous function
$$
-G.
$$
If
$$
G(p)<0,
$$
then
$$
(-G)(p)>0,
$$
which would produce a ball on which
$$
\iiint_\Omega G<0,
$$
again contradicting step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{G\equiv0}.
$$


::: pf-proof

At every point, steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} rule out both positive and negative values.
Thus
$$
G(p)=0
$$
for every
$$
p\in\RR^3.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{\operatorname{div}F=\rho}
$$
everywhere.


::: pf-proof

By definition,
$$
G
=
\operatorname{div}F-\rho.
$$
Step [](#s1-6){.pf-ref} gives
$$
G=0,
$$
so
$$
\operatorname{div}F=\rho.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the forward implication, and steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} prove the converse.

:::

:::

:::
