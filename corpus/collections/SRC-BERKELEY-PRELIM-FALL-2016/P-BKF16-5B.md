---
schema: qual/card@1
id: P-BKF16-5B
kind: problem
title: Power sums of zeros in the disk depend analytically on a parameter
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: the
    logarithmic derivative has residue equal to the zero multiplicity, so
    the kth power sum is its weighted unit-circle residue integral.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked finiteness of the zero set in the disk, the logarithmic-derivative
    residue formula, local uniform nonvanishing on the contour, and the Morera
    argument proving holomorphic dependence on the parameter.
---

::: {.problem}
Let $f _ { t } ( z )$ be a family of entire functions depending analytically on $t \in \Delta$ , where $\Delta$ is the open unit disk in C. Suppose that for all $t , f _ { t } ( z )$ is non-vanishing on the unit circle $S ^ { 1 }$ in $\mathbb { C } .$ Prove that for each $k \geq 0$ ,

$$
N _ { k } ( t ) = \sum _ { | z | < 1 : f _ { t } ( z ) = 0 } z ^ { k }
$$

is an analytic function of t (the zeroes of $f _ { t } ( z )$ are taken with multiplicity in the sum).
:::

::: {.solution}
Write
$$
F(t,z)\coloneqq f_t(z).
$$

<1>1. For every fixed $t\in\Delta$, the zeros of $f_t$ in the unit
disk are finite in number, counted without multiplicity, and
$$
N_k(t)
=
\frac{1}{2\pi i}
\int_{|z|=1}
z^k\frac{\partial_zF(t,z)}{F(t,z)}\,dz.
$$

::: {.proof}
The function $f_t$ is not identically zero because it is nonvanishing on
$|z|=1$. Hence its zeros are isolated. Since it has no zero on the unit
circle, its zeros in the closed unit disk form a finite set.

If $a$ is a zero of multiplicity $m$, then locally
$$
f_t(z)=(z-a)^m u(z),
\qquad
u(a)\ne0,
$$
and therefore
$$
\frac{f_t'(z)}{f_t(z)}
=
\frac{m}{z-a}
+
\frac{u'(z)}{u(z)}.
$$
Thus
$$
\operatorname*{Res}_{z=a}
\left(
z^k\frac{f_t'(z)}{f_t(z)}
\right)
=
m a^k.
$$
The integrand has no pole on $|z|=1$, so the residue theorem gives
$$
\frac{1}{2\pi i}
\int_{|z|=1}
z^k\frac{f_t'(z)}{f_t(z)}\,dz
=
\sum_{|a|<1}m_a a^k
=
N_k(t).
$$
:::

<1>2. Fix $t_0\in\Delta$. There is an open disk $U$ about $t_0$ and
a number $c>0$ such that
$$
|F(t,z)|\ge c
$$
for every $t\in U$ and every $|z|=1$.

::: {.proof}
By hypothesis,
$$
F(t_0,z)\ne0
$$
on the compact unit circle. Hence
$$
m
\coloneqq
\min_{|z|=1}|F(t_0,z)|
>
0.
$$
The analytic dependence of the family on $t$ gives continuity of $F$ in
$(t,z)$. Compactness of the unit circle therefore gives a neighborhood
$U$ of $t_0$ such that
$$
|F(t,z)-F(t_0,z)|<\frac m2
$$
for $t\in U$ and $|z|=1$. Consequently
$$
|F(t,z)|
\ge
|F(t_0,z)|-|F(t,z)-F(t_0,z)|
>
\frac m2.
$$
Taking $c=m/2$ proves the claim.
:::

<1>3. On $U$, the function
$$
H(t)
\coloneqq
\frac{1}{2\pi i}
\int_{|z|=1}
z^k\frac{\partial_zF(t,z)}{F(t,z)}\,dz
$$
is holomorphic.

::: {.proof}
By step <1>2, the denominator does not vanish on
$$
U\times\{|z|=1\}.
$$
Hence
$$
G(t,z)
\coloneqq
z^k\frac{\partial_zF(t,z)}{F(t,z)}
$$
is continuous there and, for each fixed $z$ on the unit circle,
holomorphic in $t$.

Continuity of $G$ on compact parameter-circle products shows that $H$ is
continuous. Let $T$ be any triangle whose closure is contained in $U$.
Since $G$ is continuous on
$$
\partial T\times\{|z|=1\},
$$
the order of integration may be interchanged, giving
$$
\begin{aligned}
\int_{\partial T}H(t)\,dt
&=
\frac{1}{2\pi i}
\int_{|z|=1}
\left(
\int_{\partial T}G(t,z)\,dt
\right)dz\\
&=0.
\end{aligned}
$$
The inner integral is zero by Cauchy's theorem because
$t\mapsto G(t,z)$ is holomorphic on $U$. Morera's theorem therefore
implies that $H$ is holomorphic on $U$.
:::

<1>4. The function $N_k$ is analytic on $\Delta$.

::: {.proof}
By step <1>1,
$$
N_k(t)=H(t)
$$
for every $t$. Step <1>3 shows that this function is holomorphic on a
neighborhood of the arbitrary point $t_0\in\Delta$. Since $t_0$ was
arbitrary, $N_k$ is holomorphic on all of $\Delta$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required conclusion for every $k\ge0$.
:::
:::
