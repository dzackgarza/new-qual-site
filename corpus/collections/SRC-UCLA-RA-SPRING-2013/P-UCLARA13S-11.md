---
schema: qual/card@1
id: P-UCLARA13S-11
kind: problem
title: Poles and Taylor coefficients of minus pi z cot pi z
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let
$$
f(z)=-\pi z\cot(\pi z).
$$

(a) Locate all poles of $f$ and determine their residues.

(b) Show that for every $n\ge1$, the coefficient of $z^{2n}$ in the Taylor expansion of $f$ about $0$ is
$$
\sum_{k=1}^{\infty}\frac{2}{k^{2n}}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The point $z=0$ is a removable singularity of $f$, with
$$
f(0)=-1
$$
after removal.


::: pf-proof

Since
$$
\sin(\pi z)
=
\pi z+O(z^3),
\qquad
\cos(\pi z)
=
1+O(z^2),
$$
one has
$$
-\pi z\cot(\pi z)
=
-\pi z\frac{\cos(\pi z)}{\sin(\pi z)}
\longrightarrow
-1
$$
as $z\to0$.

:::

:::

::: {.pf-step #s1-2}

The poles of $f$ are exactly the nonzero integers, and each is simple.


::: pf-proof

Write
$$
f(z)
=
-\pi z\frac{\cos(\pi z)}{\sin(\pi z)}.
$$
The zeros of $\sin(\pi z)$ are exactly the integers, and they are simple because
$$
\frac{d}{dz}\sin(\pi z)
=
\pi\cos(\pi z),
$$
which is nonzero at every integer. At a nonzero integer $m$, the numerator
$$
-\pi m\cos(\pi m)
$$
is nonzero, so there is a simple pole. Step [](#s1-1){.pf-ref} shows that the singularity at $0$ cancels.

:::

:::

::: {.pf-step #s1-3}

For every nonzero integer $m$,
$$
\boxed{
\operatorname{Res}(f;m)=-m
}.
$$


::: pf-proof

Using the simple-zero quotient formula,
$$
\begin{aligned}
\operatorname{Res}(f;m)
&=
\frac{-\pi m\cos(\pi m)}
{\pi\cos(\pi m)}\\
&=
-m.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

For $z\notin\ZZ$, the standard cotangent partial fraction expansion is
$$
\pi\cot(\pi z)
=
\frac1z
+
\sum_{k=1}^{\infty}
\frac{2z}{z^2-k^2},
$$
with locally uniform convergence away from the integers.


::: pf-proof

This is the classical Mittag--Leffler expansion of $\pi\cot(\pi z)$, obtained by pairing the terms at $k$ and $-k$ in
$$
\sum_{k\in\ZZ}\frac1{z-k}.
$$
The paired series converges locally uniformly off $\ZZ$ because its terms are $O(k^{-2})$ on compact sets.

:::

:::

::: {.pf-step #s1-5}

For $|z|<1$,
$$
f(z)
=
-1
+
\sum_{k=1}^{\infty}
\frac{2z^2}{k^2-z^2}.
$$


::: pf-proof

Multiply the identity in step [](#s1-4){.pf-ref} by $-z$:
$$
\begin{aligned}
-\pi z\cot(\pi z)
&=
-1
-
\sum_{k=1}^{\infty}
\frac{2z^2}{z^2-k^2}\\
&=
-1
+
\sum_{k=1}^{\infty}
\frac{2z^2}{k^2-z^2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

Fix $0<r<1$. On $|z|\le r$, the double series
$$
\sum_{k=1}^{\infty}
\sum_{n=1}^{\infty}
\frac{2z^{2n}}{k^{2n}}
$$
converges absolutely and uniformly.


::: pf-proof

For $|z|\le r$,
$$
\begin{aligned}
\sum_{k=1}^{\infty}
\sum_{n=1}^{\infty}
\frac{2|z|^{2n}}{k^{2n}}
&\le
\sum_{k=1}^{\infty}
\frac{2r^2}{k^2-r^2}.
\end{aligned}
$$
Since
$$
k^2-r^2
\ge
(1-r^2)k^2
\qquad
(k\ge1),
$$
the last sum is bounded by
$$
\frac{2r^2}{1-r^2}
\sum_{k=1}^{\infty}\frac1{k^2}
<
\infty.
$$
The Weierstrass M-test gives absolute uniform convergence.

:::

:::

::: {.pf-step #s1-7}

For $|z|<1$,
$$
f(z)
=
-1
+
\sum_{n=1}^{\infty}
\left(
\sum_{k=1}^{\infty}
\frac{2}{k^{2n}}
\right)z^{2n}.
$$


::: pf-proof

For each fixed $k$ and $|z|<1$,
$$
\frac{2z^2}{k^2-z^2}
=
\frac{2z^2}{k^2}
\frac1{1-z^2/k^2}
=
\sum_{n=1}^{\infty}
\frac{2z^{2n}}{k^{2n}}.
$$
Substitute this into step [](#s1-5){.pf-ref}. Step [](#s1-6){.pf-ref} justifies interchanging the sums.

:::

:::

::: {.pf-step #s1-8}

For every $n\ge1$, the coefficient of $z^{2n}$ in the Taylor expansion of $f$ at $0$ is
$$
\boxed{
\sum_{k=1}^{\infty}\frac{2}{k^{2n}}
}.
$$


::: pf-proof

The power series in step [](#s1-7){.pf-ref} converges on $|z|<1$ and is the Taylor expansion of $f$ there. Reading off the coefficient of $z^{2n}$ gives the stated value.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} prove part (a), and step [](#s1-8){.pf-ref} proves part (b).

:::

:::

:::
