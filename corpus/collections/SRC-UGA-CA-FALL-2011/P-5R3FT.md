---
schema: qual/card@1
id: P-5R3FT
kind: problem
title: Unique fixed point of $ce^z$ on $\{\operatorname{Re} z<1\}$ when $|c|<1/3$
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
Let $c \in \mathbb{C}$ with $|c| < \frac{1}{3}$. Show that on the open half-plane
$$
\Omega = \{z \in \mathbb{C} \mid \operatorname{Re}(z) < 1\},
$$
the function $f(z) = c e^z$ has exactly one fixed point.
:::

::: {.solution}
Put
$$
g(z)=ce^z-z.
$$
A fixed point of $f(z)=ce^z$ is exactly a zero of $g$.

<1>1. Every zero of $g$ in $\Omega$ lies in the open unit disk.

::: {.proof}
If $g(z)=0$ and $\Re z<1$, then
$$
|z|=|ce^z|=|c|e^{\Re z}<\frac13e<1,
$$
because $e<3$. Hence every fixed point in $\Omega$ satisfies $|z|<1$.
:::

<1>2. For every $R>1$, define
$$
\Omega_R=\{z:|z|<R,\ \Re z<1\}.
$$
On $\partial\Omega_R$ one has
$$
|ce^z|<|z|.
$$

::: {.proof}
The boundary consists of the vertical segment
$$
L_R=\{1+it:|t|\le\sqrt{R^2-1}\}
$$
and the circular arc
$$
C_R=\{Re^{i\theta}:\Re(Re^{i\theta})\le1\}.
$$

If $z\in L_R$, then
$$
|ce^z|=|c|e<\frac e3<1\le|z|.
$$
If $z\in C_R$, then $\Re z\le1$ and $|z|=R>1$, so
$$
|ce^z|=|c|e^{\Re z}\le|c|e<\frac e3<1<R=|z|.
$$
Thus the strict inequality holds everywhere on the boundary.
:::

<1>3. The function $g$ has exactly one zero in $\Omega_R$, counted with
multiplicity.

::: {.proof}
On $\partial\Omega_R$, step <1>2 gives
$$
|ce^z|<|-z|.
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

<1>4. The function $g$ has exactly one zero in the full half-plane
$\Omega$.

::: {.proof}
By step <1>1, every zero of $g$ in $\Omega$ lies in $|z|<1$. Therefore
every such zero lies in $\Omega_R$ for every $R>1$. Step <1>3 shows that
there is exactly one zero in each $\Omega_R$, counted with multiplicity.
Hence there is exactly one zero in $\Omega$.
:::

<1>5. The map $f(z)=ce^z$ has exactly one fixed point in $\Omega$.

::: {.proof}
Fixed points of $f$ are precisely zeros of $g$, and step <1>4 gives
exactly one such zero in $\Omega$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
