---
schema: qual/card@1
id: P-WESTOP03-02
kind: problem
title: Pointed homotopy classes of maps from $S^0$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
The fundamental group $\pi_1(X,x)$ can be described as pointed homotopy classes of pointed maps
$$
(S^1,p)\to(X,x).
$$
Describe the set of pointed homotopy classes of pointed maps
$$
(S^0,p)\to(X,x),
$$
where
$$
S^0=\{-1,1\},
\qquad p=1.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A pointed map
$$
f:(S^0,1)\to(X,x)
$$
is completely determined by the point
$$
y=f(-1)\in X.
$$


::: pf-proof

Pointedness forces $f(1)=x$. Since $S^0$ has only the two points $1$ and $-1$, the only remaining choice is $f(-1)=y$. Every such choice defines a continuous map because $S^0$ is discrete.

:::

:::

::: pf-step

Let $f_y$ and $f_z$ be the pointed maps corresponding to $y,z\in X$. A pointed homotopy from $f_y$ to $f_z$ is a continuous map
$$
H:S^0\times I\to X
$$
such that
$$
H(1,t)=x
$$
for all $t$, with $H(-1,0)=y$ and $H(-1,1)=z$.


::: pf-proof

This is exactly the definition of a homotopy through pointed maps: the basepoint $1\in S^0$ must remain at $x$ throughout the homotopy.

:::

:::

::: {.pf-step #s1-3}

Such a pointed homotopy exists if and only if $y$ and $z$ lie in the same path component of $X$.


::: pf-proof

If $H$ exists, then
$$
\gamma(t)=H(-1,t)
$$
is a path from $y$ to $z$. Conversely, if $\gamma:I\to X$ is a path from $y$ to $z$, define
$$
H(-1,t)=\gamma(t),
\qquad
H(1,t)=x.
$$
Because $S^0\times I$ is the disjoint union of two copies of $I$, this $H$ is continuous and is a pointed homotopy.

:::

:::

::: {.pf-step #s1-4}

Therefore the set of pointed homotopy classes is naturally identified with the set of path components of $X$:
$$
\boxed{[(S^0,1),(X,x)]_*\cong\pi_0(X).}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} identifies pointed maps with points $y\in X$, and step [](#s1-3){.pf-ref} identifies precisely those points that represent the same pointed homotopy class. The quotient is the set of path components.

:::

:::

::: {.pf-step #s1-5}

Under this identification, the constant pointed map represents the path component containing $x$.


::: pf-proof

The constant pointed map has $f(-1)=x$, so step [](#s1-4){.pf-ref} sends its class to the path component of $x$.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give the requested description, including its distinguished base class.

:::

:::

:::
