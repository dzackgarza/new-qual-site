---
schema: qual/card@1
id: P-5R3FT
kind: problem
title: Unique fixed point of $ce^z$ on $\{\operatorname{Re} z<1\}$ when $\abs{c}<1/3$
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Rouché
  - Zeros
relations: []
review: draft
---
::: {.problem}
Let $c \in \CC$ with $\abs{c} < \frac{1}{3}$. Show that on the open half-plane
$$
\Omega = \{z \in \CC \mid \operatorname{Re}(z) < 1\},
$$
the function $f(z) = c e^z$ has exactly one fixed point.
:::

::: {.solution}
Put
$$
g(z)=ce^z-z.
$$
A fixed point of $f(z)=ce^z$ is exactly a zero of $g$.

::: pf

::: {.pf-step #s1}

Every zero of $g$ in $\Omega$ lies in the open unit disk.

::: pf-proof

If $g(z)=0$ and $\Re z<1$, then
$$
\abs{z}=\abs{ce^z}=\abs{c}e^{\Re z}<\frac13e<1,
$$
because $e<3$. Hence every fixed point in $\Omega$ satisfies $\abs{z}<1$.

:::

:::

::: {.pf-step #s2}

For every $R>1$, define
$$
\Omega_R=\{z:\abs{z}<R,\ \Re z<1\}.
$$
On $\partial\Omega_R$ one has
$$
\abs{ce^z}<\abs{z}.
$$

::: pf-proof

The boundary consists of the vertical segment
$$
L_R=\{1+it:\abs{t}\le\sqrt{R^2-1}\}
$$
and the circular arc
$$
C_R=\{Re^{i\theta}:\Re(Re^{i\theta})\le1\}.
$$

If $z\in L_R$, then
$$
\abs{ce^z}=\abs{c}e<\frac e3<1\le\abs{z}.
$$
If $z\in C_R$, then $\Re z\le1$ and $\abs{z}=R>1$, so
$$
\abs{ce^z}=\abs{c}e^{\Re z}\le\abs{c}e<\frac e3<1<R=\abs{z}.
$$
Thus the strict inequality holds everywhere on the boundary.

:::

:::

::: {.pf-step #s3}

The function $g$ has exactly one zero in $\Omega_R$, counted with
multiplicity.

::: pf-proof

On $\partial\Omega_R$, step [](#s2){.pf-ref} gives
$$
\abs{ce^z}<\abs{-z}.
$$
Rouché's theorem therefore implies that
$$
g(z)=-z+ce^z
$$
and $-z$ have the same number of zeros in $\Omega_R$, counted with
multiplicity. The function $-z$ has exactly one simple zero, namely
$z=0$, and $0\in\Omega_R$. Hence $g$ has exactly one zero in
$\Omega_R$.

:::

:::

::: {.pf-step #s4}

The function $g$ has exactly one zero in the full half-plane
$\Omega$.

::: pf-proof

By step [](#s1){.pf-ref}, every zero of $g$ in $\Omega$ lies in $\abs{z}<1$. Therefore
every such zero lies in $\Omega_R$ for every $R>1$. Step [](#s3){.pf-ref} shows that
there is exactly one zero in each $\Omega_R$, counted with multiplicity.
Hence there is exactly one zero in $\Omega$.

:::

:::

::: {.pf-step #s5}

The map $f(z)=ce^z$ has exactly one fixed point in $\Omega$.

::: pf-proof

Fixed points of $f$ are precisely zeros of $g$, and step [](#s4){.pf-ref} gives
exactly one such zero in $\Omega$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
