---
schema: qual/card@1
id: P-BKF82-1
kind: problem
title: Global existence for $y'=f(y)$
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used the strictly monotone antiderivative of 1/f to construct and uniquely characterize local solutions, then identified global existence with divergence of the reciprocal-speed integrals at both infinities."
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and nowhere zero, and consider $y'=f(y)$.

(a) For each $c\in\mathbb R$, show there is a unique $C^1$ solution near $0$ with $y(0)=c$.

(b) Determine the conditions on $f$ under which the solution exists for all $x\in\mathbb R$ for every initial value $c$.
:::

::: {.solution}
Because $f$ is continuous and nowhere zero on the connected set $\mathbb R$,
it has constant sign.

<1>1. Construct a local solution through an arbitrary initial value $c$.
::: {.proof}
Fix $c\in\mathbb R$ and define
$$
H_c(y)=\int_c^y\frac{ds}{f(s)}.
$$
Since $f$ is continuous and nowhere zero,
$$
H_c'(y)=\frac1{f(y)}
$$
is continuous and nowhere zero. Hence $H_c$ is strictly monotone and, by
the inverse function theorem, has a $C^1$ inverse on a neighborhood of
$H_c(c)=0$.

Define
$$
y(x)=H_c^{-1}(x)
$$
there. Then $y(0)=c$, and differentiating
$$
H_c(y(x))=x
$$
gives
$$
\frac{y'(x)}{f(y(x))}=1.
$$
Thus
$$
y'(x)=f(y(x)).
$$
So a local $C^1$ solution exists.
:::

<1>2. The local solution is unique even though no Lipschitz hypothesis was assumed.
::: {.proof}
Let $z(x)$ be any $C^1$ solution with $z(0)=c$. Then
$$
\frac d{dx}H_c(z(x))
=H_c'(z(x))z'(x)
=\frac{z'(x)}{f(z(x))}
=1.
$$
Since $H_c(z(0))=0$, integration gives
$$
H_c(z(x))=x.
$$
Where $H_c^{-1}$ is defined, this forces
$$
z(x)=H_c^{-1}(x)=y(x).
$$
Hence the local solution through $c$ is unique.
:::

<1>3. Describe the maximal interval of existence.
::: {.proof}
The same formula shows that the maximal solution is the inverse of $H_c$ on
the full interval
$$
H_c(\mathbb R).
$$
Because $H_c$ is continuous and strictly monotone, its image is the open
interval between the two improper endpoint limits
$$
\lim_{y\to-\infty}H_c(y)
\quad\text{and}\quad
\lim_{y\to+\infty}H_c(y).
$$
Thus the solution through $c$ exists for all $x\in\mathbb R$ exactly when
$$
H_c(\mathbb R)=\mathbb R.
$$
:::

<1>4. Express the global-existence condition directly in terms of $f$.
::: {.proof}
Since $f$ has constant sign, the condition in step <1>3 is equivalent to
requiring infinite reciprocal travel time in both directions:
$$
\boxed{
\int_0^{\infty}\frac{ds}{|f(s)|}=\infty
\quad\text{and}\quad
\int_{-\infty}^{0}\frac{ds}{|f(s)|}=\infty.}
$$
Indeed, changing the base point from $0$ to any finite $c$ alters either
improper integral only by a finite constant, so this criterion is independent
of the initial value.

If both integrals diverge, $H_c(\mathbb R)=\mathbb R$ for every $c$, and
every initial-value solution is global. If either integral is finite, the
corresponding endpoint of $H_c(\mathbb R)$ is finite, so the inverse solution
reaches infinity in finite $x$-time and cannot be defined on all of
$\mathbb R$.
:::
:::
