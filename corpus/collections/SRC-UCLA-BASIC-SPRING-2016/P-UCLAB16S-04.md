---
schema: qual/card@1
id: P-UCLAB16S-04
kind: problem
title: Limit of Picard iterates for a linear Volterra integral equation
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Given continuous functions $\alpha:[0,1]\to\mathbb R$ and $\beta:[0,1]\to[0,1)$, define $f_n:[0,1]\to\mathbb R$ recursively by
\[
f_{n+1}(x)=\alpha(x)+\int_0^x \beta(t)f_n(t)\,dt,
\qquad f_0(x)=0.
\]
Prove that for each $x\in[0,1]$ the limit
\[
f(x):=\lim_{n\to\infty}f_n(x)
\]
exists and compute its value.
:::

Define the operator
\[
(K\varphi)(x)
=
\int_0^x\beta(t)\varphi(t)\,dt
\]
on
\[
C([0,1]).
\]
Then
\[
f_{n+1}
=
\alpha+Kf_n,
\qquad
f_0=0.
\]

::: pf

::: pf-step

There exists
\[
q<1
\]
such that
\[
0\le\beta(t)\le q
\]
for every
\[
t\in[0,1].
\]


::: pf-proof

The function $\beta$ is continuous on the compact interval $[0,1]$, so it attains a maximum.
Because its values lie in
\[
[0,1),
\]
that maximum is a number
\[
q<1.
\]

:::

:::

::: pf-step

For every
\[
\varphi,\psi\in C([0,1]),
\]
one has
\[
\|K\varphi-K\psi\|_\infty
\le
q\|\varphi-\psi\|_\infty.
\]


::: pf-proof

For
\[
x\in[0,1],
\]
\[
\begin{aligned}
|(K\varphi)(x)-(K\psi)(x)|
&=
\left|
\int_0^x
\beta(t)(\varphi(t)-\psi(t))
\,dt
\right|\\
&\le
\int_0^x
q\|\varphi-\psi\|_\infty
\,dt\\
&\le
q\|\varphi-\psi\|_\infty.
\end{aligned}
\]
Take the supremum over $x$.

:::

:::

::: pf-step

The map
\[
\mathcal T(\varphi)
=
\alpha+K\varphi
\]
is a contraction on the Banach space
\[
C([0,1])
\]
with the supremum norm.


::: pf-proof

The space
\[
C([0,1])
\]
is complete in the uniform norm.
Step <1>2 gives
\[
\|\mathcal T(\varphi)-\mathcal T(\psi)\|_\infty
\le
q\|\varphi-\psi\|_\infty
\]
with
\[
q<1.
\]
Thus $\mathcal T$ is a contraction.

:::

:::

::: pf-step

The sequence $(f_n)$ converges uniformly to the unique fixed point
\[
f
\]
of $\mathcal T$.


::: pf-proof

By definition,
\[
f_{n+1}
=
\mathcal T(f_n).
\]
The contraction mapping theorem applied to step <1>3 therefore implies
\[
f_n\to f
\]
uniformly for a unique continuous function $f$ satisfying
\[
\mathcal T(f)=f.
\]
In particular, the pointwise limit exists for every $x\in[0,1]$.

:::

:::

::: pf-step

The limit satisfies the integral equation
\[
\boxed{
f(x)
=
\alpha(x)
+
\int_0^x\beta(t)f(t)\,dt.
}
\]


::: pf-proof

This is precisely the fixed-point equation
\[
\mathcal T(f)=f.
\]

:::

:::

::: pf-step

Define
\[
B(x)
=
\int_0^x\beta(s)\,ds
\]
and
\[
H(x)
=
e^{B(x)}
\int_0^x
\beta(t)\alpha(t)e^{-B(t)}
\,dt.
\]
Then
\[
H(0)=0.
\]


::: pf-proof

At
\[
x=0,
\]
the integral is zero.
Thus
\[
H(0)
=
e^{B(0)}\cdot0
=0.
\]

:::

:::

::: pf-step

One has
\[
\boxed{
H'(x)
=
\beta(x)\bigl(\alpha(x)+H(x)\bigr).
}
\]


::: pf-proof

Because $\alpha$ and $\beta$ are continuous,
\[
B'(x)=\beta(x).
\]
Differentiate using the product rule and the fundamental theorem of calculus:
\[
\begin{aligned}
H'(x)
&=
\beta(x)e^{B(x)}
\int_0^x
\beta(t)\alpha(t)e^{-B(t)}
\,dt\\
&\quad+
e^{B(x)}
\beta(x)\alpha(x)e^{-B(x)}\\
&=
\beta(x)H(x)
+
\beta(x)\alpha(x).
\end{aligned}
\]

:::

:::

::: pf-step

Consequently,
\[
H(x)
=
\int_0^x
\beta(t)\bigl(\alpha(t)+H(t)\bigr)
\,dt.
\]


::: pf-proof

Integrate the differential equation from step <1>7 from $0$ to $x$ and use
\[
H(0)=0
\]
from step <1>6.

:::

:::

::: pf-step

Define
\[
g(x)
=
\alpha(x)+H(x).
\]
Then
\[
g
\]
satisfies the fixed-point equation in step <1>5.


::: pf-proof

By step <1>8,
\[
\begin{aligned}
g(x)
&=
\alpha(x)+H(x)\\
&=
\alpha(x)
+
\int_0^x
\beta(t)\bigl(\alpha(t)+H(t)\bigr)
\,dt\\
&=
\alpha(x)
+
\int_0^x
\beta(t)g(t)
\,dt.
\end{aligned}
\]

:::

:::

::: pf-step

Therefore the limit is
\[
\boxed{
f(x)
=
\alpha(x)
+
e^{\int_0^x\beta(s)\,ds}
\int_0^x
\beta(t)\alpha(t)
e^{-\int_0^t\beta(s)\,ds}
\,dt.
}
\]


::: pf-proof

By step <1>9, the function $g$ is a fixed point of $\mathcal T$.
By uniqueness of the fixed point from step <1>4,
\[
f=g.
\]
Substitute the definition of $H$ from step <1>6.

:::

:::

::: pf-step

Hence for every $x\in[0,1]$,
\[
\boxed{
\lim_{n\to\infty}f_n(x)
=
\alpha(x)
+
e^{\int_0^x\beta(s)\,ds}
\int_0^x
\beta(t)\alpha(t)
e^{-\int_0^t\beta(s)\,ds}
\,dt.
}
\]


::: pf-proof

Step <1>4 gives convergence of $f_n$ to $f$, and step <1>10 computes $f$ explicitly.

:::

:::

::: pf-qed

Step <1>11 is the required pointwise limit and its value.

:::

:::
