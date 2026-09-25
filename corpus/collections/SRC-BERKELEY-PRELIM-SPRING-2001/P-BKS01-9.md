---
schema: qual/card@1
id: P-BKS01-9
kind: problem
title: Entire scalar and matrix functions with positive Hermitian part are constant
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    For the scalar case, e^{-f} is bounded entire and hence constant.
    For the matrix case, every scalar compression v^*F(z)v has positive
    real part and is constant; evaluating the resulting zero quadratic
    form on basis vectors and their real and imaginary pairwise sums
    forces every matrix entry to be constant.
---

::: {.problem}
1. Prove that an entire function with positive real part is constant.
2. Prove the analogous result for $2\times2$ matrix functions: if
   \[
   F(z)=(f_{jk}(z))
   \]
   has entire entries and $F(z)+F(z)^*$ is positive definite for every $z\in\mathbb C$, prove that $F$ is constant.
:::

::: {.solution}
<1>1. If $f$ is entire and
$$
\operatorname{Re}f(z)>0
$$
for every $z\in\CC$, then $f$ is constant.

::: {.proof}
Define
$$
g(z)=e^{-f(z)}.
$$
The function $g$ is entire and
$$
\abs{g(z)}
=
e^{-\operatorname{Re}f(z)}
<
1
$$
for every $z$. By Liouville's theorem, $g$ is constant. Since
$g(z)\ne0$,
$$
0
=
g'(z)
=
-f'(z)e^{-f(z)}
$$
implies $f'(z)=0$ for every $z$. Hence $f$ is constant.
:::

<1>2. For each fixed nonzero vector $v\in\CC^2$, the scalar function
$$
\phi_v(z)=v^*F(z)v
$$
is entire and has positive real part.

::: {.proof}
Because the entries of $F$ are entire and the coordinates of $v$ are
constant, $\phi_v$ is entire. Moreover,
$$
\begin{aligned}
2\operatorname{Re}\phi_v(z)
&=
\phi_v(z)+\overline{\phi_v(z)}\\
&=
v^*F(z)v+v^*F(z)^*v\\
&=
v^*\bigl(F(z)+F(z)^*\bigr)v.
\end{aligned}
$$
The last quantity is strictly positive because
$F(z)+F(z)^*$ is positive definite and $v\ne0$.
:::

<1>3. For every $v\in\CC^2$, the function $\phi_v$ is constant.

::: {.proof}
For $v\ne0$, apply step <1>1 to $\phi_v$ using step <1>2. For
$v=0$, the function is identically zero.
:::

<1>4. Let
$$
D(z)=F(z)-F(0).
$$
Then for every $z\in\CC$ and every $v\in\CC^2$,
$$
v^*D(z)v=0.
$$

::: {.proof}
By step <1>3,
$$
v^*F(z)v
=
v^*F(0)v
$$
for every $v$ and $z$. Subtracting gives the claim.
:::

<1>5. If
$$
D(z)
=
\begin{pmatrix}
d_{11}&d_{12}\\
d_{21}&d_{22}
\end{pmatrix},
$$
then all four entries vanish.

::: {.proof}
Fix $z$ and suppress it from the notation. Taking
$v=e_1$ and $v=e_2$ in step <1>4 gives
$$
d_{11}=d_{22}=0.
$$
Taking
$$
v=e_1+e_2
$$
gives
$$
d_{12}+d_{21}=0.
$$
Taking
$$
v=e_1+ie_2
$$
gives
$$
i d_{12}-i d_{21}=0.
$$
Thus
$$
d_{12}=d_{21}=0.
$$
Hence $D(z)=0$.
:::

<1>6. The matrix function $F$ is constant.

::: {.proof}
Step <1>5 holds for every $z\in\CC$, so
$$
F(z)=F(0)
$$
for all $z$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 proves part 1, and step <1>6 proves part 2.
:::
:::
