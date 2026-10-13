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
\[
f(z)=-\pi z\cot(\pi z).
\]

(a) Locate all poles of $f$ and determine their residues.

(b) Show that for every $n\ge1$, the coefficient of $z^{2n}$ in the Taylor expansion of $f$ about $0$ is
\[
\sum_{k=1}^{\infty}\frac{2}{k^{2n}}.
\]
:::

::: {.solution}
<1>1. The point $z=0$ is a removable singularity of $f$, with
\[
f(0)=-1
\]
after removal.

::: {.proof}
Since
\[
\sin(\pi z)
=
\pi z+O(z^3),
\qquad
\cos(\pi z)
=
1+O(z^2),
\]
one has
\[
-\pi z\cot(\pi z)
=
-\pi z\frac{\cos(\pi z)}{\sin(\pi z)}
\longrightarrow
-1
\]
as $z\to0$.
:::

<1>2. The poles of $f$ are exactly the nonzero integers, and each is simple.

::: {.proof}
Write
\[
f(z)
=
-\pi z\frac{\cos(\pi z)}{\sin(\pi z)}.
\]
The zeros of $\sin(\pi z)$ are exactly the integers, and they are simple because
\[
\frac{d}{dz}\sin(\pi z)
=
\pi\cos(\pi z),
\]
which is nonzero at every integer. At a nonzero integer $m$, the numerator
\[
-\pi m\cos(\pi m)
\]
is nonzero, so there is a simple pole. Step <1>1 shows that the singularity at $0$ cancels.
:::

<1>3. For every nonzero integer $m$,
\[
\boxed{
\operatorname{Res}(f;m)=-m
}.
\]

::: {.proof}
Using the simple-zero quotient formula,
\[
\begin{aligned}
\operatorname{Res}(f;m)
&=
\frac{-\pi m\cos(\pi m)}
{\pi\cos(\pi m)}\\
&=
-m.
\end{aligned}
\]
:::

<1>4. For $z\notin\mathbb Z$, the standard cotangent partial fraction expansion is
\[
\pi\cot(\pi z)
=
\frac1z
+
\sum_{k=1}^{\infty}
\frac{2z}{z^2-k^2},
\]
with locally uniform convergence away from the integers.

::: {.proof}
This is the classical Mittag--Leffler expansion of $\pi\cot(\pi z)$, obtained by pairing the terms at $k$ and $-k$ in
\[
\sum_{k\in\mathbb Z}\frac1{z-k}.
\]
The paired series converges locally uniformly off $\mathbb Z$ because its terms are $O(k^{-2})$ on compact sets.
:::

<1>5. For $|z|<1$,
\[
f(z)
=
-1
+
\sum_{k=1}^{\infty}
\frac{2z^2}{k^2-z^2}.
\]

::: {.proof}
Multiply the identity in step <1>4 by $-z$:
\[
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
\]
:::

<1>6. Fix $0<r<1$. On $|z|\le r$, the double series
\[
\sum_{k=1}^{\infty}
\sum_{n=1}^{\infty}
\frac{2z^{2n}}{k^{2n}}
\]
converges absolutely and uniformly.

::: {.proof}
For $|z|\le r$,
\[
\begin{aligned}
\sum_{k=1}^{\infty}
\sum_{n=1}^{\infty}
\frac{2|z|^{2n}}{k^{2n}}
&\le
\sum_{k=1}^{\infty}
\frac{2r^2}{k^2-r^2}.
\end{aligned}
\]
Since
\[
k^2-r^2
\ge
(1-r^2)k^2
\qquad
(k\ge1),
\]
the last sum is bounded by
\[
\frac{2r^2}{1-r^2}
\sum_{k=1}^{\infty}\frac1{k^2}
<
\infty.
\]
The Weierstrass M-test gives absolute uniform convergence.
:::

<1>7. For $|z|<1$,
\[
f(z)
=
-1
+
\sum_{n=1}^{\infty}
\left(
\sum_{k=1}^{\infty}
\frac{2}{k^{2n}}
\right)z^{2n}.
\]

::: {.proof}
For each fixed $k$ and $|z|<1$,
\[
\frac{2z^2}{k^2-z^2}
=
\frac{2z^2}{k^2}
\frac1{1-z^2/k^2}
=
\sum_{n=1}^{\infty}
\frac{2z^{2n}}{k^{2n}}.
\]
Substitute this into step <1>5. Step <1>6 justifies interchanging the sums.
:::

<1>8. For every $n\ge1$, the coefficient of $z^{2n}$ in the Taylor expansion of $f$ at $0$ is
\[
\boxed{
\sum_{k=1}^{\infty}\frac{2}{k^{2n}}
}.
\]

::: {.proof}
The power series in step <1>7 converges on $|z|<1$ and is the Taylor expansion of $f$ there. Reading off the coefficient of $z^{2n}$ gives the stated value.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>2--<1>3 prove part (a), and step <1>8 proves part (b).
:::
:::
