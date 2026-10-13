---
schema: qual/card@1
id: P-UCLARA11S-06
kind: problem
title: Existence and uniqueness of the Lebesgue decomposition of finite positive Borel measures
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Suppose $\mu$ and $\nu$ are finite positive regular Borel measures on $\mathbb R^n$.
Prove that there is a unique pair of positive Borel measures $\mu_a,\mu_s$ such that
\[
\mu=\mu_a+\mu_s,
\qquad
\mu_a\ll\nu,
\qquad
\mu_s\perp\nu.
\]
:::

::: {.solution}
<1>1. Set
\[
\lambda
\coloneqq
\mu+\nu.
\]
Then
\[
\nu\ll\lambda.
\]

::: {.proof}
If $\lambda(E)=0$, then
\[
0
=
\lambda(E)
=
\mu(E)+\nu(E).
\]
Both terms are nonnegative, so $\nu(E)=0$.
:::

<1>2. Let
\[
f
\coloneqq
\frac{d\nu}{d\lambda}.
\]
Then $f\ge0$ $\lambda$-almost everywhere and
\[
\nu(E)
=
\int_E f\,d\lambda
\]
for every Borel set $E$.

::: {.proof}
This is the Radon--Nikodym theorem applied to step <1>1. Positivity of $\nu$ allows the Radon--Nikodym derivative to be chosen nonnegative.
:::

<1>3. Define
\[
X
\coloneqq
\{f>0\},
\qquad
Y
\coloneqq
\{f=0\},
\]
and
\[
\mu_a(E)
\coloneqq
\mu(E\cap X),
\qquad
\mu_s(E)
\coloneqq
\mu(E\cap Y).
\]
Then
\[
\mu
=
\mu_a+\mu_s.
\]

::: {.proof}
The sets $X$ and $Y$ are measurable, disjoint, and cover $\mathbb R^n$ up to a $\lambda$-null set. Modifying $f$ on that null set if necessary, assume they partition all of $\mathbb R^n$. Then
\[
E
=
(E\cap X)\sqcup(E\cap Y)
\]
for every Borel set $E$, so
\[
\mu(E)
=
\mu(E\cap X)+\mu(E\cap Y)
=
\mu_a(E)+\mu_s(E).
\]
:::

<1>4. The measure $\mu_s$ is singular with respect to $\nu$.

::: {.proof}
By construction,
\[
\mu_s(X)=0.
\]
Also,
\[
\nu(Y)
=
\int_Y f\,d\lambda
=0.
\]
Thus $X$ and $Y$ are complementary measurable sets with
\[
\mu_s(X)=0,
\qquad
\nu(Y)=0,
\]
which is exactly
\[
\mu_s\perp\nu.
\]
:::

<1>5. The measure $\mu_a$ is absolutely continuous with respect to $\nu$.

::: {.proof}
Let $E$ be Borel and suppose
\[
\nu(E)=0.
\]
Then
\[
0
=
\nu(E\cap X)
=
\int_{E\cap X}f\,d\lambda.
\]
For $m\ge1$, set
\[
X_m
\coloneqq
\{f\ge1/m\}.
\]
Since
\[
X
=
\bigcup_{m=1}^{\infty}X_m,
\]
and
\[
0
\ge
\int_{E\cap X_m}f\,d\lambda
\ge
\frac1m\lambda(E\cap X_m),
\]
one has
\[
\lambda(E\cap X_m)=0
\]
for every $m$. Hence
\[
\lambda(E\cap X)=0.
\]
Because $\mu\le\lambda$,
\[
\mu_a(E)
=
\mu(E\cap X)
=0.
\]
Thus $\mu_a\ll\nu$.
:::

<1>6. Steps <1>3--<1>5 give a Lebesgue decomposition
\[
\mu=\mu_a+\mu_s,
\qquad
\mu_a\ll\nu,
\qquad
\mu_s\perp\nu.
\]

::: {.proof}
This is just the collection of the conclusions already proved.
:::

<1>7. Suppose
\[
\mu
=
\mu_a+\mu_s
=
\mu_a'+\mu_s'
\]
are two such decompositions. Then the signed measure
\[
\eta
\coloneqq
\mu_a-\mu_a'
\]
is absolutely continuous with respect to $\nu$.

::: {.proof}
If $\nu(E)=0$, then
\[
\mu_a(E)=\mu_a'(E)=0
\]
by absolute continuity, so
\[
\eta(E)=0.
\]
Thus $\eta\ll\nu$.
:::

<1>8. The same signed measure $\eta$ is singular with respect to $\nu$.

::: {.proof}
From equality of the two decompositions,
\[
\eta
=
\mu_s'-\mu_s.
\]
Because
\[
\mu_s\perp\nu
\qquad\text{and}\qquad
\mu_s'\perp\nu,
\]
there are Borel sets $N,N'$ with
\[
\nu(N)=\nu(N')=0
\]
such that $\mu_s$ is concentrated on $N$ and $\mu_s'$ is concentrated on $N'$. Therefore the signed measure
\[
\mu_s'-\mu_s
\]
is concentrated on
\[
N\cup N',
\]
which is $\nu$-null. Hence $\eta\perp\nu$.
:::

<1>9. A signed measure that is both absolutely continuous and singular with respect to $\nu$ is zero.

::: {.proof}
Let $\eta\ll\nu$ and $\eta\perp\nu$. Singularity gives a Borel set $N$ such that
\[
\nu(N)=0
\]
and $\eta$ is concentrated on $N$. Absolute continuity gives
\[
\eta(N)=0.
\]
Since $\eta$ vanishes outside $N$ as well, $\eta=0$.
:::

<1>10. The decomposition is unique.

::: {.proof}
By steps <1>7--<1>9,
\[
\eta
=
\mu_a-\mu_a'
=0,
\]
so
\[
\mu_a=\mu_a'.
\]
Subtracting from $\mu$ gives
\[
\mu_s=\mu_s'.
\]
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>6 proves existence, and step <1>10 proves uniqueness.
:::
:::
