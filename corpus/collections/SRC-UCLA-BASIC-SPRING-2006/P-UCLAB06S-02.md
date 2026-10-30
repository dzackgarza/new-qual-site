---
schema: qual/card@1
id: P-UCLAB06S-02
kind: problem
title: Radius of convergence of a power series
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 2 of the retained UCLA Basic Examination Spring 2006 PDF.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The exam asked for a unique number rho at least 0, which fails for series such as e^x that converge everywhere; the statement now asks for a unique rho in [0, infinity].
---

::: {.problem}
Let $F(x) = \sum_{n=0}^\infty a_n x^n$ be a power series with $a_n \in \RR$. Show that there exists a unique $\rho \in [0,\infty]$ such that $F(x)$ converges if $\abs{x} < \rho$ and $F(x)$ diverges if $\abs{x} > \rho$.
:::

::: {.solution}

Define
$$
C=
\left\{
r\ge0:
\sum_{n=0}^{\infty}a_nx^n
\text{ converges for every }x\text{ with }\abs{x}<r
\right\}.
$$
The set $C$ is nonempty because
$$
0\in C.
$$

::: pf

::: {.pf-step #s1-1}

If the series converges at some nonzero point
$$
x_0,
$$
then it converges absolutely at every $x$ with
$$
\abs{x}<\abs{x_0}.
$$


::: pf-proof

Convergence of
$$
\sum_{n=0}^{\infty}a_nx_0^n
$$
implies
$$
a_nx_0^n\to0.
$$
Hence the sequence
$$
(a_nx_0^n)
$$
is bounded: there exists
$$
M>0
$$
such that
$$
\abs{a_nx_0^n}\le M
$$
for all $n$.

If
$$
\abs{x}<\abs{x_0},
$$
set
$$
q=\frac{\abs{x}}{\abs{x_0}}<1.
$$
Then
$$
\abs{a_nx^n}
=
\abs{a_nx_0^n}q^n
\le
Mq^n.
$$
The geometric series
$$
\sum_{n=0}^{\infty}Mq^n
$$
converges, so comparison gives absolute convergence of
$$
\sum_{n=0}^{\infty}a_nx^n.
$$

:::

:::

::: pf-step

If the series diverges at some point
$$
x_0,
$$
then it diverges at every $x$ with
$$
\abs{x}>\abs{x_0}.
$$


::: pf-proof

Suppose instead that the series converged at some $x$ satisfying
$$
\abs{x}>\abs{x_0}.
$$
Then step [](#s1-1){.pf-ref}, applied to the convergence point $x$, would imply convergence at every point whose absolute value is smaller than $\abs{x}$, in particular at $x_0$.
This contradicts the assumed divergence at $x_0$.

:::

:::

::: {.pf-step #s1-3}

Define
$$
\rho=\sup C
$$
in the extended interval $[0,\infty]$.
Then the series converges for every
$$
x
$$
with
$$
\abs{x}<\rho.
$$


::: pf-proof

Fix $x$ with
$$
\abs{x}<\rho.
$$
Choose a number $r$ satisfying
$$
\abs{x}<r<\rho.
$$
By the definition of the supremum, there exists
$$
s\in C
$$
with
$$
r<s\le\rho.
$$
Since
$$
\abs{x}<s
$$
and
$$
s\in C,
$$
the series converges at $x$.

:::

:::

::: {.pf-step #s1-4}

If
$$
\rho<\infty,
$$
then the series diverges for every $x$ with
$$
\abs{x}>\rho.
$$


::: pf-proof

Suppose, for contradiction, that the series converges at some $x$ with
$$
\abs{x}>\rho.
$$
By step [](#s1-1){.pf-ref}, it then converges for every $y$ satisfying
$$
\abs{y}<\abs{x}.
$$
Hence
$$
\abs{x}\in C.
$$
But
$$
\abs{x}>\rho=\sup C,
$$
a contradiction.
Therefore the series diverges for every
$$
\abs{x}>\rho.
$$

:::

:::

::: {.pf-step #s1-5}

If the series converges for every real $x$, then
$$
\rho=\infty.
$$


::: pf-proof

In this case every
$$
r\ge0
$$
belongs to $C$.
Thus $C$ is unbounded above, and its supremum in the extended interval is
$$
\infty.
$$

:::

:::

::: {.pf-step #s1-6}

The radius is unique.


::: pf-proof

Suppose
$$
\rho_1<\rho_2
$$
both had the stated property.
Choose
$$
x
$$
with
$$
\rho_1<\abs{x}<\rho_2.
$$
The property for $\rho_1$ would force divergence at $x$, while the property for $\rho_2$ would force convergence at $x$.
This contradiction shows that two distinct radii cannot satisfy the condition.

:::

:::

::: {.pf-step #s1-7}

Therefore there is a unique radius of convergence
$$
\boxed{
\rho\in[0,\infty]
}
$$
such that the power series converges for
$$
\abs{x}<\rho
$$
and diverges for
$$
\abs{x}>\rho.
$$


::: pf-proof

Existence follows from steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref}, and uniqueness from step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the assertion.

:::

:::

:::
