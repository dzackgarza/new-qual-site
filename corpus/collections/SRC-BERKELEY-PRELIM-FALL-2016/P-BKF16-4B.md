---
schema: qual/card@1
id: P-BKF16-4B
kind: problem
title: Holomorphic square root of $z(e^z-1)$ near $0$
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
    Independently checked the retained Fall 2016 solution packet: after
    factoring the double zero at the origin, a local logarithm gives a
    square root; coefficient comparison gives 1, 1/4, 5/96; and the simple
    zero at 2*pi*i obstructs an entire square root.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked removability and nonvanishing of (e^z-1)/z near zero, the first
    three series coefficients, and the odd-multiplicity-zero obstruction to
    global extension.
---

::: {.problem}
Put $f ( z ) = z ( e ^ { z } - 1 )$ . Prove there exists an analytic function h(z) defined near $z = 0$ such that $f ( z ) = h ( z ) ^ { 2 }$ . Find the first 3 terms in the power series expansion $h ( z ) = \sum a _ { n } z ^ { n }$ Does h(z) extend to an entire function on C?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function
$$
g(z)
\coloneqq
\begin{cases}
\dfrac{e^z-1}{z},&z\ne0,\\
1,&z=0
\end{cases}
$$
is entire, satisfies
$$
g(0)=1,
$$
and gives
$$
f(z)=z^2g(z).
$$

::: pf-proof

The exponential series gives
$$
\frac{e^z-1}{z}
=
1+\frac z{2!}+\frac{z^2}{3!}+\cdots
$$
for $z\ne0$, and the right-hand side is an entire power series whose
value at $0$ is $1$. Thus the apparent singularity is removable and
the stated extension is entire. The factorization
$$
z(e^z-1)=z^2\frac{e^z-1}{z}
$$
holds away from $0$ and hence everywhere.

:::

:::

::: {.pf-step #s2}

There is a disk $U$ about $0$ on which $g$ has no zeros and a
holomorphic function
$$
L:U\to\CC
$$
such that
$$
e^{L(z)}=g(z).
$$

::: pf-proof

Since $g(0)=1\ne0$ and $g$ is continuous, it is nonzero on some disk
about $0$. Shrink that disk if necessary so that it is simply
connected. A nonvanishing holomorphic function on a simply connected
domain admits a holomorphic logarithm, giving $L$.

:::

:::

::: {.pf-step #s3}

On $U$, the function
$$
h(z)
\coloneqq
z\,e^{L(z)/2}
$$
is holomorphic and satisfies
$$
\boxed{h(z)^2=f(z)}.
$$

::: pf-proof

The function is a product of holomorphic functions. By steps
[](#s1){.pf-ref} and [](#s2){.pf-ref},
$$
\begin{aligned}
h(z)^2
&=
z^2e^{L(z)}\\
&=
z^2g(z)\\
&=
f(z).
\end{aligned}
$$
Thus a local analytic square root exists.

:::

:::

::: {.pf-step #s4}

Choose the sign of $h$ so that
$$
h'(0)=1.
$$
Then write
$$
h(z)
=
z+az^2+bz^3+O(z^4).
$$

::: pf-proof

Since
$$
h(z)^2=f(z)=z^2+O(z^3),
$$
the zero of $h$ at $0$ is simple and its linear coefficient squares
to $1$. Replacing $h$ by $-h$ if necessary makes that coefficient
$1$, giving the displayed form.

:::

:::

::: {.pf-step #s5}

The coefficients in step [](#s4){.pf-ref} are
$$
a=\frac14,
\qquad
b=\frac5{96}.
$$

::: pf-proof

The exponential series gives
$$
f(z)
=
z(e^z-1)
=
z^2+\frac12z^3+\frac16z^4+O(z^5).
$$
On the other hand,
$$
\begin{aligned}
h(z)^2
&=
\left(
z+az^2+bz^3+O(z^4)
\right)^2\\
&=
z^2+2az^3+(a^2+2b)z^4+O(z^5).
\end{aligned}
$$
Equating coefficients gives
$$
2a=\frac12,
$$
so
$$
a=\frac14.
$$
Then
$$
\frac1{16}+2b=\frac16,
$$
and hence
$$
b=\frac5{96}.
$$

:::

:::

::: {.pf-step #s6}

Thus the first three nonzero terms of the branch with
$h'(0)=1$ are
$$
\boxed{
h(z)
=
z+\frac14z^2+\frac5{96}z^3+O(z^4).
}
$$

::: pf-proof

This is step [](#s4){.pf-ref} with the coefficients from step [](#s5){.pf-ref}. The other
local square root is its negative.

:::

:::

::: {.pf-step #s7}

The function $f$ has a simple zero at
$$
z_0=2\pi i.
$$

::: pf-proof

At $z_0$,
$$
e^{z_0}-1=0
$$
and $z_0\ne0$. Moreover,
$$
\frac{d}{dz}(e^z-1)\bigg|_{z=z_0}
=
e^{z_0}
=
1\ne0.
$$
Hence $e^z-1$ has a simple zero at $z_0$, and multiplication by the
nonzero factor $z$ does not change its multiplicity there.

:::

:::

::: {.pf-step #s8}

The local function $h$ cannot extend to an entire function on
$\CC$.

::: pf-proof

Suppose an entire function $H$ agrees with $h$ near $0$. Then
$$
H^2
$$
and $f$ are entire and agree on a neighborhood of $0$ by step [](#s3){.pf-ref}.
The identity theorem therefore gives
$$
H^2=f
$$
on all of $\CC$.

Every zero of a square of a holomorphic function has even
multiplicity. This contradicts step [](#s7){.pf-ref}, where $f$ has a simple zero
at $2\pi i$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves local existence, step [](#s6){.pf-ref} gives the requested series
terms, and step [](#s8){.pf-ref} proves that no entire extension exists.

:::

:::

:::
