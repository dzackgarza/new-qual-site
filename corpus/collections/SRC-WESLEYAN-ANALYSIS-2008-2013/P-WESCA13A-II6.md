---
schema: qual/card@1
id: P-WESCA13A-II6
kind: problem
title: 'Even analytic functions descend through squaring'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash corrupts the radius/center symbols in this line; the evenness and $f(\sqrt z)$ formulation unambiguously identifies the intended descent-through-$z\mapsto z^2$ problem.
---

::: {.problem}
Let $f$ be even and analytic on a disk $B(0,r)$.
Define
$$
g(z)=f(\sqrt z).
$$
Show that $g:B(0,r)\to\CC$ is well-defined and analytic, and express $g^{(n)}(0)$ in terms of derivatives of $f$ at $0$.
:::

::: {.remark}
As printed, $g$ is defined on $B(0,r)$; for $r<1$ this disk is larger than the natural domain, because $\sqrt z$ lies in $B(0,r)$ only when $\abs{z}<r^2$.
The intended domain is $B(0,r^2)$, and the solution works there.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since $f$ is analytic on
$$
B(0,r),
$$
it has a Taylor expansion
$$
f(w)
=
\sum_{m=0}^{\infty}
a_m w^m
$$
for
$$
\abs{w}<r.
$$


::: pf-proof

This is the Taylor-series theorem for holomorphic functions on a disk.
Moreover,
$$
a_m
=
\frac{f^{(m)}(0)}{m!}.
$$

:::

:::

::: {.pf-step #s1-2}

Because $f$ is even,
$$
a_m=0
$$
for every odd integer $m$.


::: pf-proof

Evenness gives
$$
f(-w)=f(w).
$$
Using the Taylor expansion,
$$
\sum_{m=0}^{\infty}
a_m(-1)^m w^m
=
\sum_{m=0}^{\infty}
a_m w^m.
$$
Uniqueness of power-series coefficients gives
$$
a_m(-1)^m=a_m.
$$
If $m$ is odd, then
$$
-a_m=a_m,
$$
so
$$
a_m=0.
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
f(w)
=
\sum_{n=0}^{\infty}
a_{2n}w^{2n}.
$$


::: pf-proof

Delete the odd terms using step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

If
$$
z\in B(0,r^2),
$$
then every square root $w$ of $z$ satisfies
$$
\abs{w}<r.
$$


::: pf-proof

If
$$
w^2=z,
$$
then
$$
\abs{w}^2
=
\abs{z}
<
r^2.
$$
Therefore
$$
\abs{w}<r.
$$

:::

:::

::: {.pf-step #s1-5}

The value
$$
f(\sqrt z)
$$
is independent of the choice of square root.


::: pf-proof

For
$$
z\ne0,
$$
the two square roots are
$$
w
\quad\text{and}\quad
-w.
$$
Since $f$ is even,
$$
f(-w)=f(w).
$$
At
$$
z=0,
$$
the only square root is $0$.
Thus the value is well defined for every
$$
z\in B(0,r^2).
$$

:::

:::

::: {.pf-step #s1-6}

For
$$
z\in B(0,r^2),
$$
one has
$$
\boxed{
g(z)
=
\sum_{n=0}^{\infty}
a_{2n}z^n.
}
$$


::: pf-proof

Choose any
$$
w
$$
with
$$
w^2=z.
$$
By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
\begin{aligned}
g(z)
&=
f(w)\\
&=
\sum_{n=0}^{\infty}
a_{2n}w^{2n}\\
&=
\sum_{n=0}^{\infty}
a_{2n}(w^2)^n\\
&=
\sum_{n=0}^{\infty}
a_{2n}z^n.
\end{aligned}
$$

:::

:::

::: pf-step

The series in step [](#s1-6){.pf-ref} converges for every
$$
\abs{z}<r^2.
$$


::: pf-proof

If
$$
\abs{z}<r^2,
$$
choose
$$
w
$$
with
$$
w^2=z.
$$
Then
$$
\abs{w}<r
$$
by step [](#s1-4){.pf-ref}.
The series
$$
\sum_{n=0}^{\infty}
a_{2n}w^{2n}
$$
is a subseries of the absolutely convergent Taylor series for $f(w)$.
Hence
$$
\sum_{n=0}^{\infty}
a_{2n}z^n
$$
converges.

:::

:::

::: {.pf-step #s1-8}

Therefore $g$ is analytic on
$$
B(0,r^2).
$$


::: pf-proof

Step [](#s1-6){.pf-ref} represents $g$ by a convergent power series throughout
$$
B(0,r^2).
$$
Thus $g$ is holomorphic there.

:::

:::

::: {.pf-step #s1-9}

The Taylor coefficient of $z^n$ in $g$ is
$$
a_{2n}
=
\frac{f^{(2n)}(0)}{(2n)!}.
$$


::: pf-proof

The first equality follows from step [](#s1-6){.pf-ref}.
The second follows from the Taylor coefficient formula in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Consequently
$$
\boxed{
g^{(n)}(0)
=
\frac{n!}{(2n)!}
f^{(2n)}(0).
}
$$


::: pf-proof

For a power series
$$
g(z)
=
\sum_{n=0}^{\infty}
b_nz^n,
$$
one has
$$
g^{(n)}(0)
=
n!b_n.
$$
Here
$$
b_n
=
a_{2n}
=
\frac{f^{(2n)}(0)}{(2n)!}
$$
by step [](#s1-9){.pf-ref}.
Substitute.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves well-definedness, step [](#s1-8){.pf-ref} proves analyticity, and step
[](#s1-10){.pf-ref} gives the requested derivative formula.

:::

:::

:::
