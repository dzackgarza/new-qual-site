---
schema: qual/card@1
id: P-UCLARA11S-06
kind: problem
title: Existence and uniqueness of the Lebesgue decomposition of finite positive Borel measures
classification: {areas: [real-analysis], topics: [Radon-Nikodym, Absolute Continuity, Borel Measures]}
relations: []
review: draft
---

::: {.problem}
Suppose $\mu$ and $\nu$ are finite positive regular Borel measures on $\RR^n$.
Prove that there is a unique pair of positive Borel measures $\mu_a,\mu_s$ such that
$$
\mu=\mu_a+\mu_s,
\qquad
\mu_a\ll\nu,
\qquad
\mu_s\perp\nu.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Set
$$
\lambda
\coloneqq
\mu+\nu.
$$
Then
$$
\nu\ll\lambda.
$$


::: pf-proof

If $\lambda(E)=0$, then
$$
0
=
\lambda(E)
=
\mu(E)+\nu(E).
$$
Both terms are nonnegative, so $\nu(E)=0$.

:::

:::

::: pf-step

Let
$$
f
\coloneqq
\frac{d\nu}{d\lambda}.
$$
Then $f\ge0$ $\lambda$-almost everywhere and
$$
\nu(E)
=
\int_E f\,d\lambda
$$
for every Borel set $E$.


::: pf-proof

This is the Radon--Nikodym theorem applied to step [](#s1-1){.pf-ref}. Positivity of $\nu$ allows the Radon--Nikodym derivative to be chosen nonnegative.

:::

:::

::: {.pf-step #s1-3}

Define
$$
X
\coloneqq
\{f>0\},
\qquad
Y
\coloneqq
\{f=0\},
$$
and
$$
\mu_a(E)
\coloneqq
\mu(E\cap X),
\qquad
\mu_s(E)
\coloneqq
\mu(E\cap Y).
$$
Then
$$
\mu
=
\mu_a+\mu_s.
$$


::: pf-proof

The sets $X$ and $Y$ are measurable, disjoint, and cover $\RR^n$ up to a $\lambda$-null set. Modifying $f$ on that null set if necessary, assume they partition all of $\RR^n$. Then
$$
E
=
(E\cap X)\sqcup(E\cap Y)
$$
for every Borel set $E$, so
$$
\mu(E)
=
\mu(E\cap X)+\mu(E\cap Y)
=
\mu_a(E)+\mu_s(E).
$$

:::

:::

::: {.pf-step #s1-4}

The measure $\mu_s$ is singular with respect to $\nu$.


::: pf-proof

By construction,
$$
\mu_s(X)=0.
$$
Also,
$$
\nu(Y)
=
\int_Y f\,d\lambda
=0.
$$
Thus $X$ and $Y$ are complementary measurable sets with
$$
\mu_s(X)=0,
\qquad
\nu(Y)=0,
$$
which is exactly
$$
\mu_s\perp\nu.
$$

:::

:::

::: {.pf-step #s1-5}

The measure $\mu_a$ is absolutely continuous with respect to $\nu$.


::: pf-proof

Let $E$ be Borel and suppose
$$
\nu(E)=0.
$$
Then
$$
0
=
\nu(E\cap X)
=
\int_{E\cap X}f\,d\lambda.
$$
For $m\ge1$, set
$$
X_m
\coloneqq
\{f\ge1/m\}.
$$
Since
$$
X
=
\bigcup_{m=1}^{\infty}X_m,
$$
and
$$
0
\ge
\int_{E\cap X_m}f\,d\lambda
\ge
\frac1m\lambda(E\cap X_m),
$$
one has
$$
\lambda(E\cap X_m)=0
$$
for every $m$. Hence
$$
\lambda(E\cap X)=0.
$$
Because $\mu\le\lambda$,
$$
\mu_a(E)
=
\mu(E\cap X)
=0.
$$
Thus $\mu_a\ll\nu$.

:::

:::

::: {.pf-step #s1-6}

Steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} give a Lebesgue decomposition
$$
\mu=\mu_a+\mu_s,
\qquad
\mu_a\ll\nu,
\qquad
\mu_s\perp\nu.
$$


::: pf-proof

This is just the collection of the conclusions already proved.

:::

:::

::: {.pf-step #s1-7}

Suppose
$$
\mu
=
\mu_a+\mu_s
=
\mu_a'+\mu_s'
$$
are two such decompositions. Then the signed measure
$$
\eta
\coloneqq
\mu_a-\mu_a'
$$
is absolutely continuous with respect to $\nu$.


::: pf-proof

If $\nu(E)=0$, then
$$
\mu_a(E)=\mu_a'(E)=0
$$
by absolute continuity, so
$$
\eta(E)=0.
$$
Thus $\eta\ll\nu$.

:::

:::

::: {.pf-step #s1-8}

The same signed measure $\eta$ is singular with respect to $\nu$.


::: pf-proof

From equality of the two decompositions,
$$
\eta
=
\mu_s'-\mu_s.
$$
Because
$$
\mu_s\perp\nu
\qquad\text{and}\qquad
\mu_s'\perp\nu,
$$
there are Borel sets $N,N'$ with
$$
\nu(N)=\nu(N')=0
$$
such that $\mu_s$ is concentrated on $N$ and $\mu_s'$ is concentrated on $N'$. Therefore the signed measure
$$
\mu_s'-\mu_s
$$
is concentrated on
$$
N\cup N',
$$
which is $\nu$-null. Hence $\eta\perp\nu$.

:::

:::

::: {.pf-step #s1-9}

A signed measure that is both absolutely continuous and singular with respect to $\nu$ is zero.


::: pf-proof

Let $\eta\ll\nu$ and $\eta\perp\nu$. Singularity gives a Borel set $N$ such that
$$
\nu(N)=0
$$
and $\eta$ is concentrated on $N$. Absolute continuity gives
$$
\eta(N)=0.
$$
Since $\eta$ vanishes outside $N$ as well, $\eta=0$.

:::

:::

::: {.pf-step #s1-10}

The decomposition is unique.


::: pf-proof

By steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref},
$$
\eta
=
\mu_a-\mu_a'
=0,
$$
so
$$
\mu_a=\mu_a'.
$$
Subtracting from $\mu$ gives
$$
\mu_s=\mu_s'.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves existence, and step [](#s1-10){.pf-ref} proves uniqueness.

:::

:::

:::
