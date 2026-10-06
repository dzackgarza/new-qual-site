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
\[
g(z)=f(\sqrt z).
\]
Show that $g$ is well-defined and analytic on $B(0,r^2)$, and express $g^{(n)}(0)$ in terms of derivatives of $f$ at $0$.
:::

::: {.solution}
<1>1. Since $f$ is analytic on
\[
B(0,r),
\]
it has a Taylor expansion
\[
f(w)
=
\sum_{m=0}^{\infty}
a_m w^m
\]
for
\[
|w|<r.
\]

::: {.proof}
This is the Taylor-series theorem for holomorphic functions on a disk.
Moreover,
\[
a_m
=
\frac{f^{(m)}(0)}{m!}.
\]
:::

<1>2. Because $f$ is even,
\[
a_m=0
\]
for every odd integer $m$.

::: {.proof}
Evenness gives
\[
f(-w)=f(w).
\]
Using the Taylor expansion,
\[
\sum_{m=0}^{\infty}
a_m(-1)^m w^m
=
\sum_{m=0}^{\infty}
a_m w^m.
\]
Uniqueness of power-series coefficients gives
\[
a_m(-1)^m=a_m.
\]
If $m$ is odd, then
\[
-a_m=a_m,
\]
so
\[
a_m=0.
\]
:::

<1>3. Hence
\[
f(w)
=
\sum_{n=0}^{\infty}
a_{2n}w^{2n}.
\]

::: {.proof}
Delete the odd terms using step <1>2.
:::

<1>4. If
\[
z\in B(0,r^2),
\]
then every square root $w$ of $z$ satisfies
\[
|w|<r.
\]

::: {.proof}
If
\[
w^2=z,
\]
then
\[
|w|^2
=
|z|
<
r^2.
\]
Therefore
\[
|w|<r.
\]
:::

<1>5. The value
\[
f(\sqrt z)
\]
is independent of the choice of square root.

::: {.proof}
For
\[
z\ne0,
\]
the two square roots are
\[
w
\quad\text{and}\quad
-w.
\]
Since $f$ is even,
\[
f(-w)=f(w).
\]
At
\[
z=0,
\]
the only square root is $0$.
Thus the value is well defined for every
\[
z\in B(0,r^2).
\]
:::

<1>6. For
\[
z\in B(0,r^2),
\]
one has
\[
\boxed{
g(z)
=
\sum_{n=0}^{\infty}
a_{2n}z^n.
}
\]

::: {.proof}
Choose any
\[
w
\]
with
\[
w^2=z.
\]
By steps <1>3--<1>4,
\[
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
\]
:::

<1>7. The series in step <1>6 converges for every
\[
|z|<r^2.
\]

::: {.proof}
If
\[
|z|<r^2,
\]
choose
\[
w
\]
with
\[
w^2=z.
\]
Then
\[
|w|<r
\]
by step <1>4.
The series
\[
\sum_{n=0}^{\infty}
a_{2n}w^{2n}
\]
is a subseries of the absolutely convergent Taylor series for $f(w)$.
Hence
\[
\sum_{n=0}^{\infty}
a_{2n}z^n
\]
converges.
:::

<1>8. Therefore $g$ is analytic on
\[
B(0,r^2).
\]

::: {.proof}
Step <1>6 represents $g$ by a convergent power series throughout
\[
B(0,r^2).
\]
Thus $g$ is holomorphic there.
:::

<1>9. The Taylor coefficient of $z^n$ in $g$ is
\[
a_{2n}
=
\frac{f^{(2n)}(0)}{(2n)!}.
\]

::: {.proof}
The first equality follows from step <1>6.
The second follows from the Taylor coefficient formula in step <1>1.
:::

<1>10. Consequently
\[
\boxed{
g^{(n)}(0)
=
\frac{n!}{(2n)!}
f^{(2n)}(0).
}
\]

::: {.proof}
For a power series
\[
g(z)
=
\sum_{n=0}^{\infty}
b_nz^n,
\]
one has
\[
g^{(n)}(0)
=
n!b_n.
\]
Here
\[
b_n
=
a_{2n}
=
\frac{f^{(2n)}(0)}{(2n)!}
\]
by step <1>9.
Substitute.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>5 proves well-definedness, step <1>8 proves analyticity, and step
<1>10 gives the requested derivative formula.
:::
:::
