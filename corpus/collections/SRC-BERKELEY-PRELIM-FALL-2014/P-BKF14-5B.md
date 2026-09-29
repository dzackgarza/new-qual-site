---
schema: qual/card@1
id: P-BKF14-5B
kind: problem
title: Zeros minus poles of an elliptic function sum to a Gaussian integer
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the poles w_b and put the unit-square condition inside math against Fall_2014_Exam.pdf page 16 problem 5B.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: pairing
    opposite edges gives an integer and an imaginary integer, and residues
    recover the weighted zero-minus-pole sum.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked orientations on all four edges, periodicity of f'/f, winding
    number integrality, and the residue signs at zeros and poles.
---

::: {.problem}
Let $f$ be a doubly-periodic meromorphic function: $f(z + 1) = f(z) = f(z + i)$ for all $z \in \mathbf{C}$. Let $z_a$ be the zeroes of $f$ inside the unit square $0 < \operatorname{Re} z, \operatorname{Im} z < 1$, $w_b$ be its poles inside the square, and $k_a$ and $l_b$ be respective multiplicities. Assuming that $f$ has no zeroes or poles on the boundary of the square, prove that

$$
\sum_a k_a z_a - \sum_b l_b w_b \in \mathbb{Z}[i],
$$

that is, is a Gaussian integer. Hint: Show that the following integral along the boundary of the square is a Gaussian integer:

$$
\frac{1}{2\pi i} \oint z \frac{f'(z)}{f(z)} \, dz.
$$
:::

::: {.solution}
Let $Q$ be the positively oriented boundary of the unit square and set
$$
h(z)\coloneqq\frac{f'(z)}{f(z)}.
$$
Since $f$ has no zero or pole on $Q$, the function $h$ is holomorphic
on a neighborhood of $Q$.

::: pf

::: {.pf-step #s1}

The logarithmic derivative $h$ has periods $1$ and $i$:
$$
h(z+1)=h(z)=h(z+i).
$$

::: pf-proof

Differentiating the identities
$$
f(z+1)=f(z)=f(z+i)
$$
gives
$$
f'(z+1)=f'(z)=f'(z+i).
$$
Dividing by the corresponding nonzero values of $f$ wherever $h$ is
defined gives the claimed periodicity.

:::

:::

::: {.pf-step #s2}

The sum of the contributions from the right and left edges to
$$
I\coloneqq\frac1{2\pi i}\oint_Q z h(z)\,dz
$$
is an integer.

::: pf-proof

The right edge is traversed from $1$ to $1+i$, while the left edge is
traversed from $i$ to $0$. Translating the right edge by $-1$ and using
step [](#s1){.pf-ref} gives
$$
\begin{aligned}
&\int_{1}^{1+i} z h(z)\,dz
+
\int_i^0 z h(z)\,dz\\
&\qquad=
\int_0^i(1+t)h(t)\,dt
-
\int_0^i t h(t)\,dt\\
&\qquad=
\int_0^i h(t)\,dt.
\end{aligned}
$$
Hence the paired contribution to $I$ is
$$
\frac1{2\pi i}\int_0^i\frac{f'(t)}{f(t)}\,dt.
$$
Because $f(i)=f(0)$ and $f$ is nonzero on this edge, the path
$t\mapsto f(t)$ is a closed curve in $\CC^\times$. Therefore
$$
\frac1{2\pi i}\int_0^i\frac{f'(t)}{f(t)}\,dt
$$
is its winding number about $0$, hence an integer.

:::

:::

::: {.pf-step #s3}

The sum of the contributions from the bottom and top edges to
$I$ is an imaginary integer.

::: pf-proof

The bottom edge is traversed from $0$ to $1$, and the top edge from
$1+i$ to $i$. Using the parameter $z=t+i$ on the top edge and step
[](#s1){.pf-ref},
$$
\begin{aligned}
&\int_0^1 z h(z)\,dz
+
\int_{1+i}^{i} z h(z)\,dz\\
&\qquad=
\int_0^1 t h(t)\,dt
-
\int_0^1(t+i)h(t)\,dt\\
&\qquad=
-i\int_0^1h(t)\,dt.
\end{aligned}
$$
Thus the paired contribution to $I$ is
$$
-i\left(
\frac1{2\pi i}\int_0^1\frac{f'(t)}{f(t)}\,dt
\right).
$$
Since $f(1)=f(0)$ and $f$ is nonzero on the bottom edge, the quantity
in parentheses is the winding number of the closed curve
$t\mapsto f(t)$ about $0$, and hence belongs to $\ZZ$. The whole
expression therefore belongs to $i\ZZ$.

:::

:::

::: {.pf-step #s4}

The contour integral satisfies
$$
I\in\ZZ[i].
$$

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, the vertical-edge pair contributes an integer
and the horizontal-edge pair contributes an imaginary integer. Their
sum is therefore a Gaussian integer.

:::

:::

::: {.pf-step #s5}

At a zero $z_a$ of multiplicity $k_a$, the function
$$
z\frac{f'(z)}{f(z)}
$$
has residue $k_a z_a$, and at a pole $w_b$ of order $l_b$ it has
residue $-l_b w_b$.

::: pf-proof

Near a zero $z_a$ of order $k_a$, write
$$
f(z)=(z-z_a)^{k_a}u(z),
\qquad
u(z_a)\ne0.
$$
Then
$$
\frac{f'(z)}{f(z)}
=
\frac{k_a}{z-z_a}+\frac{u'(z)}{u(z)},
$$
so multiplication by $z$ gives residue $k_a z_a$.

Near a pole $w_b$ of order $l_b$, write
$$
f(z)=(z-w_b)^{-l_b}v(z),
\qquad
v(w_b)\ne0.
$$
Then
$$
\frac{f'(z)}{f(z)}
=
-\frac{l_b}{z-w_b}+\frac{v'(z)}{v(z)},
$$
so the residue after multiplication by $z$ is $-l_b w_b$.

:::

:::

::: {.pf-step #s6}

One has
$$
\boxed{
\sum_a k_a z_a-\sum_b l_b w_b\in\ZZ[i].
}
$$

::: pf-proof

By the residue theorem and step [](#s5){.pf-ref},
$$
\frac1{2\pi i}\oint_Q
z\frac{f'(z)}{f(z)}\,dz
=
\sum_a k_a z_a-\sum_b l_b w_b.
$$
The left-hand side belongs to $\ZZ[i]$ by step [](#s4){.pf-ref}, proving the
claim.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the required Gaussian-integrality statement.

:::

:::

:::
