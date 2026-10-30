---
schema: qual/card@1
id: P-TRIV-CA27
kind: problem
title: Large-$x$ asymptotics of the modified Bessel function $K_\nu$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 27, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
The modified Bessel function of the second kind has the following integral representation: $K_\nu(x) = \frac{1}{2} \int_0^{\infty} \exp\left( -\frac{x}{2}\left( s + \frac{1}{s} \right) \right) \frac{\mathrm{d}s}{s^{1-\nu}}$. Find the asymptotic expansion for $x \gg 1$.
:::

::: {.solution}

Assume $x>0$ and $\nu$ is fixed.

::: pf

::: {.pf-step #s1-1}

With the substitution
$$
s=e^t,
$$
the integral becomes
$$
K_\nu(x)
=
\frac12
\int_{-\infty}^{\infty}
e^{-x\cosh t+\nu t}
\,dt.
$$


::: pf-proof

Since
$$
ds=e^t,dt=s,dt,
$$
one has
$$
s^{\nu-1}ds=e^{\nu t},dt.
$$
Also
$$
\frac12
\left(
s+\frac1s
\right)
=
\frac12(e^t+e^{-t})
=
\cosh t.
$$
Substituting gives the displayed integral.

:::

:::

::: {.pf-step #s1-2}

Equivalently,
$$
K_\nu(x)
=
\int_0^\infty
e^{-x\cosh t}
\cosh(\nu t)
\,dt.
$$


::: pf-proof

Split the integral from step [](#s1-1){.pf-ref} at $0$ and substitute $t\mapsto -t$ in
the negative half. Since $\cosh t$ is even,
$$
e^{-x\cosh(-t)}=e^{-x\cosh t},
$$
and
$$
\frac12(e^{\nu t}+e^{-\nu t})
=
\cosh(\nu t).
$$

:::

:::

::: pf-step

The phase $\cosh t$ has a unique minimum at $t=0$, with
$$
\cosh0=1,
\qquad
(\cosh t)''\evalfrom_{t=0}=1.
$$


::: pf-proof

One has
$$
(\cosh t)'=\sinh t,
$$
which vanishes only at $t=0$, and
$$
(\cosh t)''=\cosh t>0.
$$
Thus $t=0$ is the unique nondegenerate minimum.

:::

:::

::: {.pf-step #s1-4}

The leading saddle-point approximation is
$$
K_\nu(x)
\sim
e^{-x}
\sqrt{\frac{\pi}{2x}}.
$$


::: pf-proof

Near $t=0$,
$$
\cosh t
=
1+\frac{t^2}{2}+O(t^4),
$$
and
$$
\cosh(\nu t)=1+O(t^2).
$$
Hence the saddle-point region has width $t=O(x^{-1/2})$. Put
$$
t=\frac{u}{\sqrt x}.
$$
Then
$$
K_\nu(x)
=
\frac{e^{-x}}{\sqrt x}
\int_0^\infty
e^{-u^2/2+O(u^4/x)}
\left(1+O(u^2/x)\right)
\,du.
$$
The leading term is therefore
$$
\frac{e^{-x}}{\sqrt x}
\int_0^\infty e^{-u^2/2}\,du
=
e^{-x}
\sqrt{\frac{\pi}{2x}}.
$$

:::

:::

::: {.pf-step #s1-5}

The function $K_\nu$ satisfies
$$
x^2K_\nu''(x)
+
xK_\nu'(x)
-
(x^2+\nu^2)K_\nu(x)
=
0.
$$


::: pf-proof

Starting from step [](#s1-2){.pf-ref}, differentiation under the integral gives
$$
K_\nu'(x)
=
-\int_0^\infty
\cosh t,
e^{-x\cosh t}
\cosh(\nu t)
\,dt
$$
and
$$
K_\nu''(x)
=
\int_0^\infty
\cosh^2 t,
e^{-x\cosh t}
\cosh(\nu t)
\,dt.
$$

Also
$$
\frac{d^2}{dt^2}\cosh(\nu t)
=
\nu^2\cosh(\nu t).
$$
Integrating twice by parts transfers these two $t$-derivatives to
$e^{-x\cosh t}$. The boundary terms vanish, and
$$
\frac{d^2}{dt^2}e^{-x\cosh t}
=
\left(
x^2\sinh^2 t-x\cosh t
\right)
e^{-x\cosh t}.
$$
Therefore
$$
\nu^2K_\nu
=
x^2
\int_0^\infty
\sinh^2 t,
e^{-x\cosh t}
\cosh(\nu t)
\,dt
+
xK_\nu'(x).
$$
Since
$$
\sinh^2 t
=
\cosh^2 t-1,
$$
the integral equals
$$
K_\nu''(x)-K_\nu(x).
$$
Rearranging gives the differential equation.

:::

:::

::: {.pf-step #s1-6}

Write the saddle expansion in the form
$$
K_\nu(x)
\sim
e^{-x}x^{-1/2}
\sum_{k=0}^{\infty}a_kx^{-k}.
$$
Then the coefficients satisfy
$$
a_{k+1}
=
\frac{
4\nu^2-(2k+1)^2
}{
8(k+1)
}
a_k.
$$


::: pf-proof

Let
$$
A(x)
=
\sum_{k=0}^{\infty}a_kx^{-k}
$$
and
$$
K_\nu(x)
=
e^{-x}x^{-1/2}A(x).
$$
Substitution into the differential equation from step [](#s1-5){.pf-ref} gives
$$
A''-2A'
+
\frac{1/4-\nu^2}{x^2}A
=
0.
$$
Now
$$
A'
=
-\sum_{k\geq0}
k a_kx^{-k-1},
$$
and
$$
A''
=
\sum_{k\geq0}
k(k+1)a_kx^{-k-2}.
$$
Equating the coefficient of $x^{-k-2}$ gives
$$
k(k+1)a_k
+
2(k+1)a_{k+1}
+
\left(
\frac14-\nu^2
\right)a_k
=
0.
$$
Solving for $a_{k+1}$ yields
$$
a_{k+1}
=
\frac{
\nu^2-(k+1/2)^2
}{
2(k+1)
}
a_k,
$$
which is the displayed recurrence.

:::

:::

::: {.pf-step #s1-7}

The leading coefficient is
$$
a_0=\sqrt{\frac\pi2}.
$$


::: pf-proof

Compare the general ansatz in step [](#s1-6){.pf-ref} with the leading saddle estimate from
step [](#s1-4){.pf-ref}:
$$
K_\nu(x)
\sim
e^{-x}x^{-1/2}
\sqrt{\frac\pi2}.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
K_\nu(x)
\sim
\sqrt{\frac{\pi}{2x}}
e^{-x}
\sum_{k=0}^{\infty}
\frac{
\displaystyle
\prod_{j=1}^{k}
\left(
4\nu^2-(2j-1)^2
\right)
}{
k!\,(8x)^k
}
}
$$
as $x\to\infty$, with the empty product equal to $1$.


::: pf-proof

Starting from $a_0$ in step [](#s1-7){.pf-ref} and iterating the recurrence in step [](#s1-6){.pf-ref}
gives
$$
a_k
=
\sqrt{\frac\pi2}
\frac{
\prod_{j=1}^{k}
\left(
4\nu^2-(2j-1)^2
\right)
}{
k!\,8^k
}.
$$
Substitute these coefficients into the expansion of step [](#s1-6){.pf-ref}.

:::

:::

::: pf-step

In particular,
$$
K_\nu(x)
\sim
\sqrt{\frac{\pi}{2x}}
e^{-x}
\left[
1
+
\frac{4\nu^2-1}{8x}
+
\frac{
(4\nu^2-1)(4\nu^2-9)
}{
2!(8x)^2
}
+
\cdots
\right].
$$


::: pf-proof

Expand the first two nontrivial terms of step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref} give the leading saddle approximation and the full
asymptotic expansion, respectively.

:::

:::

:::
