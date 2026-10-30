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
Given continuous functions $\alpha:[0,1]\to\RR$ and $\beta:[0,1]\to[0,1)$, define $f_n:[0,1]\to\RR$ recursively by
$$
f_{n+1}(x)=\alpha(x)+\int_0^x \beta(t)f_n(t)\,dt,
\qquad f_0(x)=0.
$$
Prove that for each $x\in[0,1]$ the limit
$$
f(x):=\lim_{n\to\infty}f_n(x)
$$
exists and compute its value.
:::

::: {.solution}

Define the operator
$$
(K\varphi)(x)
=
\int_0^x\beta(t)\varphi(t)\,dt
$$
on
$$
C([0,1]).
$$
Then
$$
f_{n+1}
=
\alpha+Kf_n,
\qquad
f_0=0.
$$

::: pf

::: pf-step

There exists
$$
q<1
$$
such that
$$
0\le\beta(t)\le q
$$
for every
$$
t\in[0,1].
$$


::: pf-proof

The function $\beta$ is continuous on the compact interval $[0,1]$, so it attains a maximum.
Because its values lie in
$$
[0,1),
$$
that maximum is a number
$$
q<1.
$$

:::

:::

::: {.pf-step #s1-2}

For every
$$
\varphi,\psi\in C([0,1]),
$$
one has
$$
\norm{K\varphi-K\psi}_\infty
\le
q\norm{\varphi-\psi}_\infty.
$$


::: pf-proof

For
$$
x\in[0,1],
$$
$$
\begin{aligned}
\abs{(K\varphi)(x)-(K\psi)(x)}
&=
\abs{
\int_0^x
\beta(t)(\varphi(t)-\psi(t))
\,dt
}\\
&\le
\int_0^x
q\norm{\varphi-\psi}_\infty
\,dt\\
&\le
q\norm{\varphi-\psi}_\infty.
\end{aligned}
$$
Take the supremum over $x$.

:::

:::

::: {.pf-step #s1-3}

The map
$$
\mathcal T(\varphi)
=
\alpha+K\varphi
$$
is a contraction on the Banach space
$$
C([0,1])
$$
with the supremum norm.


::: pf-proof

The space
$$
C([0,1])
$$
is complete in the uniform norm.
Step [](#s1-2){.pf-ref} gives
$$
\norm{\mathcal T(\varphi)-\mathcal T(\psi)}_\infty
\le
q\norm{\varphi-\psi}_\infty
$$
with
$$
q<1.
$$
Thus $\mathcal T$ is a contraction.

:::

:::

::: {.pf-step #s1-4}

The sequence $(f_n)$ converges uniformly to the unique fixed point
$$
f
$$
of $\mathcal T$.


::: pf-proof

By definition,
$$
f_{n+1}
=
\mathcal T(f_n).
$$
The contraction mapping theorem applied to step [](#s1-3){.pf-ref} therefore implies
$$
f_n\to f
$$
uniformly for a unique continuous function $f$ satisfying
$$
\mathcal T(f)=f.
$$
In particular, the pointwise limit exists for every $x\in[0,1]$.

:::

:::

::: {.pf-step #s1-5}

The limit satisfies the integral equation
$$
\boxed{
f(x)
=
\alpha(x)
+
\int_0^x\beta(t)f(t)\,dt.
}
$$


::: pf-proof

This is precisely the fixed-point equation
$$
\mathcal T(f)=f.
$$

:::

:::

::: {.pf-step #s1-6}

Define
$$
B(x)
=
\int_0^x\beta(s)\,ds
$$
and
$$
H(x)
=
e^{B(x)}
\int_0^x
\beta(t)\alpha(t)e^{-B(t)}
\,dt.
$$
Then
$$
H(0)=0.
$$


::: pf-proof

At
$$
x=0,
$$
the integral is zero.
Thus
$$
H(0)
=
e^{B(0)}\cdot0
=0.
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
\boxed{
H'(x)
=
\beta(x)\bigl(\alpha(x)+H(x)\bigr).
}
$$


::: pf-proof

Because $\alpha$ and $\beta$ are continuous,
$$
B'(x)=\beta(x).
$$
Differentiate using the product rule and the fundamental theorem of calculus:
$$
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
$$

:::

:::

::: {.pf-step #s1-8}

Consequently,
$$
H(x)
=
\int_0^x
\beta(t)\bigl(\alpha(t)+H(t)\bigr)
\,dt.
$$


::: pf-proof

Integrate the differential equation from step [](#s1-7){.pf-ref} from $0$ to $x$ and use
$$
H(0)=0
$$
from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Define
$$
g(x)
=
\alpha(x)+H(x).
$$
Then
$$
g
$$
satisfies the fixed-point equation in step [](#s1-5){.pf-ref}.


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
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
$$

:::

:::

::: {.pf-step #s1-10}

Therefore the limit is
$$
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
$$


::: pf-proof

By step [](#s1-9){.pf-ref}, the function $g$ is a fixed point of $\mathcal T$.
By uniqueness of the fixed point from step [](#s1-4){.pf-ref},
$$
f=g.
$$
Substitute the definition of $H$ from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Hence for every $x\in[0,1]$,
$$
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
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives convergence of $f_n$ to $f$, and step [](#s1-10){.pf-ref} computes $f$ explicitly.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required pointwise limit and its value.

:::

:::

:::
