---
schema: qual/card@1
id: P-WESCA04-P7
kind: problem
title: "Order of the singularity of a sum of two functions with poles"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 7 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md. Flash misplaces $z_0$ inside the phrase describing the order of the pole of $g$; the surrounding sentence uniquely determines “a pole of order n at the same point.”
---

::: {.problem}
Let $f$ have a pole of order $m$ at $z_0$, and let $g$ have a pole of order $n$ at the same point.
Show that $f+g$ has either a removable singularity at $z_0$ or a pole of order at most
$$
\max\{m,n\}.
$$
:::

::: {.solution}

Set
$$
M
\coloneqq
\max\{m,n\}.
$$

::: pf

::: {.pf-step #s1-1}

There are holomorphic functions
$$
F,G
$$
near $z_0$ such that
$$
f(z)
=
\frac{F(z)}
{(z-z_0)^m},
\qquad
g(z)
=
\frac{G(z)}
{(z-z_0)^n},
$$
with
$$
F(z_0)\ne0,
\qquad
G(z_0)\ne0.
$$


::: pf-proof

This is the local factorization characterizing a pole and its order.

:::

:::

::: {.pf-step #s1-2}

The function
$$
H(z)
\coloneqq
(z-z_0)^M
\bigl(
f(z)+g(z)
\bigr)
$$
extends holomorphically across $z_0$.


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
\begin{aligned}
H(z)
&=
(z-z_0)^{M-m}F(z)
+
(z-z_0)^{M-n}G(z).
\end{aligned}
$$
Both exponents
$$
M-m
\quad\text{and}\quad
M-n
$$
are nonnegative integers.
Hence each term is holomorphic near $z_0$, and so is their sum.

:::

:::

::: {.pf-step #s1-3}

If
$$
H(z_0)\ne0,
$$
then $f+g$ has a pole of order exactly $M$ at $z_0$.


::: pf-proof

In that case,
$$
f(z)+g(z)
=
\frac{H(z)}
{(z-z_0)^M}
$$
with $H$ holomorphic and nonzero at $z_0$.
That is precisely a pole of order $M$.

:::

:::

::: {.pf-step #s1-4}

If
$$
H(z_0)=0,
$$
let $r$ be the order of the zero of $H$ at $z_0$, unless
$$
H\equiv0
$$
near $z_0$.
Then
$$
H(z)
=
(z-z_0)^rK(z)
$$
with $K$ holomorphic and
$$
K(z_0)\ne0.
$$


::: pf-proof

This is the standard factorization of a nonzero holomorphic function at a
zero.
If $H$ vanishes identically on a neighborhood, then
$$
f+g=0
$$
there, so the singularity is removable; that case is already settled.

:::

:::

::: {.pf-step #s1-5}

If
$$
0<r<M,
$$
then $f+g$ has a pole of order
$$
M-r.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
f(z)+g(z)
=
\frac{(z-z_0)^rK(z)}
{(z-z_0)^M}
=
\frac{K(z)}
{(z-z_0)^{M-r}}.
$$
Since
$$
K(z_0)\ne0,
$$
this is a pole of order
$$
M-r.
$$
In particular,
$$
M-r<M.
$$

:::

:::

::: {.pf-step #s1-6}

If
$$
r\ge M,
$$
then the singularity of $f+g$ at $z_0$ is removable.


::: pf-proof

Again using step [](#s1-4){.pf-ref},
$$
f(z)+g(z)
=
(z-z_0)^{r-M}K(z).
$$
The exponent
$$
r-M
$$
is nonnegative, so the right-hand side extends holomorphically across
$z_0$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
f+g
\text{ has either a removable singularity or a pole of order at most }
\max\{m,n\}.
}
$$


::: pf-proof

If $H(z_0)\ne0$, step [](#s1-3){.pf-ref} gives pole order
$$
M.
$$
If $H(z_0)=0$, steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give either a smaller pole order or a
removable singularity.

:::

:::

::: {.pf-step #s1-8}

More sharply, if
$$
m\ne n,
$$
then the pole order of $f+g$ is exactly
$$
\max\{m,n\}.
$$


::: pf-proof

Suppose, for example,
$$
m>n.
$$
Then
$$
M=m,
$$
and step [](#s1-2){.pf-ref} gives
$$
H(z)
=
F(z)
+
(z-z_0)^{m-n}G(z).
$$
At $z_0$,
$$
H(z_0)
=
F(z_0)
\ne
0.
$$
Thus step [](#s1-3){.pf-ref} gives a pole of order $m$.
The case
$$
n>m
$$
is symmetric.
Only when
$$
m=n
$$
can leading terms cancel.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves the required statement; step [](#s1-8){.pf-ref} records the sharper
non-equal-order case.

:::

:::

:::
