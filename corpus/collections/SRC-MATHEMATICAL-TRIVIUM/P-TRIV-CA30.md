---
schema: qual/card@1
id: P-TRIV-CA30
kind: problem
title: Stirling asymptotics of $\binom{2N}{N}$ and $\log\binom{N}{m}$
classification:
  areas: [complex-analysis]
  topics:
  - Stirling's Formula
  - Binomial Coefficients
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 30, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Using Stirling's approximation, find the leading behavior of:

(a) $\binom{2N}{N}$ for large $N$.

(b) $S = \log Z(N, m)$ with $Z = \frac{N!}{(N - m)!\, m!}$ for large $N$.
:::

::: {.solution}

Use Stirling's formula
$$
n!
\sim
\sqrt{2\pi n}
\left(\frac ne\right)^n.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\binom{2N}{N}
=
\frac{(2N)!}{(N!)^2}.
$$


::: pf-proof

This is the definition of the central binomial coefficient.

:::

:::

::: {.pf-step #s1-2}

Applying Stirling's formula to step [](#s1-1){.pf-ref} gives
$$
\binom{2N}{N}
\sim
\frac{
\sqrt{4\pi N}
\left(\frac{2N}{e}\right)^{2N}
}{
2\pi N
\left(\frac Ne\right)^{2N}
}.
$$


::: pf-proof

Apply Stirling's formula to $(2N)!$ and to each factor $N!$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\binom{2N}{N}
\sim
\frac{4^N}{\sqrt{\pi N}}
}.
$$


::: pf-proof

In step [](#s1-2){.pf-ref},
$$
\left(
\frac{2N}{N}
\right)^{2N}
=
2^{2N}
=
4^N,
$$
and
$$
\frac{\sqrt{4\pi N}}{2\pi N}
=
\frac1{\sqrt{\pi N}}.
$$

:::

:::

::: {.pf-step #s1-4}

Part (a) follows.


::: pf-proof

This is step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Assume
$$
m\to\infty
\qquad\text{and}\qquad
N-m\to\infty.
$$
Then
$$
Z(N,m)
=
\binom Nm
\sim
\sqrt{
\frac{N}
{2\pi m(N-m)}
}
\frac{
N^N
}{
m^m(N-m)^{N-m}
}.
$$


::: pf-proof

Apply Stirling's formula to
$$
Z(N,m)
=
\frac{N!}{m!(N-m)!}.
$$
The exponential factors $e^{-N}$, $e^{-m}$, and $e^{-(N-m)}$ cancel because
$$
m+(N-m)=N.
$$
The square-root prefactors simplify to
$$
\frac{\sqrt{2\pi N}}
{\sqrt{2\pi m}\sqrt{2\pi(N-m)}}
=
\sqrt{
\frac{N}
{2\pi m(N-m)}
}.
$$

:::

:::

::: {.pf-step #s1-6}

Taking logarithms in step [](#s1-5){.pf-ref} gives
$$
\boxed{
\begin{aligned}
S
&=
N\log N
-
m\log m
-
(N-m)\log(N-m)\\
&\qquad
-
\frac12
\log\left(
\frac{2\pi m(N-m)}{N}
\right)
+
o(1).
\end{aligned}
}
$$


::: pf-proof

Take the logarithm of the asymptotic formula in step [](#s1-5){.pf-ref}. Since the quotient
of the two sides tends to $1$, the logarithm of that quotient is $o(1)$.

:::

:::

::: {.pf-step #s1-7}

If
$$
m=pN
$$
with fixed
$$
0<p<1,
$$
then
$$
\boxed{
S
=
N
\left[
-p\log p
-
(1-p)\log(1-p)
\right]
-
\frac12
\log\left(
2\pi Np(1-p)
\right)
+
o(1).
}
$$


::: pf-proof

Substitute
$$
m=pN,
\qquad
N-m=(1-p)N
$$
into step [](#s1-6){.pf-ref}. The coefficients of $\log N$ in the leading terms cancel:
$$
N-pN-(1-p)N=0.
$$
after collecting the three logarithmic contributions, leaving
$$
-Np\log p
-
N(1-p)\log(1-p).
$$
The square-root correction becomes
$$
-\frac12
\log\left(
2\pi Np(1-p)
\right).
$$

:::

:::

::: {.pf-step #s1-8}

The leading extensive behavior in the fixed-density regime is
$$
\boxed{
S
\sim
N
\left[
-p\log p
-
(1-p)\log(1-p)
\right].
}
$$


::: pf-proof

The logarithmic correction in step [](#s1-7){.pf-ref} is lower order than $N$.

:::

:::

::: {.pf-step #s1-9}

Part (b) follows.


::: pf-proof

Step [](#s1-6){.pf-ref} gives the general Stirling form when both $m$ and $N-m$ grow, and
steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} give the standard fixed-density large-$N$ form.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-9){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
