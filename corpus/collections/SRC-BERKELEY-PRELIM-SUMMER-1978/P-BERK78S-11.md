---
schema: qual/card@1
id: P-BERK78S-11
kind: problem
title: Multiplying power-series coefficients by a polynomial factor preserves the radius of convergence
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
  note: The source indexes both series from n=0 and then prints |b_n|<n^2|a_n| "for all n". At n=0 that strict inequality is impossible, so the mathematically coherent intended condition is stated for n>=1, with b_0 unrestricted.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For a fixed |z|<R, chose r with |z|<r<R. Convergence of sum a_n r^n
    makes the terms a_n r^n bounded. Hence
    |b_n z^n| is bounded by M n^2(|z|/r)^n, and the latter numerical series
    converges.
---

::: {.problem}
Suppose
\[
\sum_{n=0}^\infty a_nz^n
\]
converges for $|z|<R$, where $z,a_n\in\mathbb C$. Let $b_n\in\mathbb C$ satisfy
\[
|b_n|<n^2|a_n|
\qquad(n\ge1).
\]
Prove that
\[
\sum_{n=0}^\infty b_nz^n
\]
also converges for $|z|<R$.
:::

::: {.solution}
Fix
$$
z\in\CC
\qquad\text{with}\qquad
\abs{z}<R.
$$

::: pf

::: {.pf-step #s1}

Choose a real number $r$ such that
$$
\abs{z}<r<R.
$$

::: pf-proof

The interval
$$
(\abs{z},R)
$$
is nonempty because $\abs{z}<R$.

:::

:::

::: {.pf-step #s2}

The sequence
$$
(a_nr^n)_{n\geq0}
$$
is bounded.

::: pf-proof

Since
$$
r<R,
$$
the hypothesis gives convergence of
$$
\sum_{n=0}^{\infty}a_nr^n.
$$
The terms of a convergent series tend to zero, and therefore form a
bounded sequence. Hence there is $M\geq0$ such that
$$
\abs{a_n}r^n\leq M
$$
for every $n\geq0$.

:::

:::

::: {.pf-step #s3}

For every $n\geq1$,
$$
\abs{b_nz^n}
<
Mn^2
\left(
\frac{\abs{z}}r
\right)^n.
$$

::: pf-proof

Using the coefficient hypothesis and step [](#s2){.pf-ref},
$$
\begin{aligned}
\abs{b_nz^n}
&<
n^2\abs{a_n}\abs{z}^n\\
&=
n^2\abs{a_n}r^n
\left(
\frac{\abs{z}}r
\right)^n\\
&\leq
Mn^2
\left(
\frac{\abs{z}}r
\right)^n.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

The numerical series
$$
\sum_{n=1}^{\infty}
n^2
\left(
\frac{\abs{z}}r
\right)^n
$$
converges.

::: pf-proof

Set
$$
q=\frac{\abs{z}}r.
$$
By step [](#s1){.pf-ref},
$$
0\leq q<1.
$$
For the terms
$$
u_n=n^2q^n,
$$
one has
$$
\frac{u_{n+1}}{u_n}
=
\left(\frac{n+1}{n}\right)^2q
\longrightarrow
q
<
1.
$$
The ratio test gives convergence.

:::

:::

::: {.pf-step #s5}

The series
$$
\sum_{n=0}^{\infty}b_nz^n
$$
converges absolutely.

::: pf-proof

The term $b_0$ is a single finite complex number. For $n\geq1$, step [](#s3){.pf-ref}
and convergence in step [](#s4){.pf-ref} give
$$
\sum_{n=1}^{\infty}\abs{b_nz^n}
<
M
\sum_{n=1}^{\infty}
n^2
\left(
\frac{\abs{z}}r
\right)^n
<
\infty.
$$
Thus the full series converges absolutely.

:::

:::

::: {.pf-step #s6}

The series
$$
\boxed{
\sum_{n=0}^{\infty}b_nz^n
}
$$
converges for every $\abs{z}<R$.

::: pf-proof

The point $z$ was arbitrary subject only to $\abs{z}<R$, and step [](#s5){.pf-ref}
proves convergence at every such point.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the required conclusion.

:::

:::

:::
