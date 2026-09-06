---
schema: qual/card@1
id: P-QSYKP
kind: problem
title: $\|v\|_{L^\infty([0,1]^2)}\le C\|v-\Delta v\|_{L^2([0,1]^2)}$ for trigonometric
  polynomials $v$
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - PDEs
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 2 of the UCLA Analysis Qualifying Exam, Fall 2009, from the collection provenance PDF.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Replaced the older proof's incorrect opening assertion that u has the same
    Fourier coefficients as v. The multiplier is
    1+4*pi^2(n^2+m^2); Parseval and Cauchy-Schwarz give the estimate, and the
    lattice sum is bounded by a product of two convergent one-dimensional sums.
---

::: {.problem}
Let $v$ be a trigonometric polynomial in two variables, i.e. $$v(x,y) = \sum_{n,m\in\mathbb{Z}} a_{n,m} e^{2\pi i(nx+my)}$$ with only finitely many nonzero $a_{n,m}$.
If $u=v-\Delta v$ where $\Delta = \partial_x^2 + \partial_y^2$ is the Laplacian, prove that $$||v||_{L^\infty([0,1]^2)} \le C||u||_{L^2([0,1]^2)}$$ for some constant $C$ independent of $v$.
:::

::: {.solution}
For $(n,m)\in\mathbb Z^2$, set
\[
\lambda_{n,m}=1+4\pi^2(n^2+m^2).
\]

<1>1. The Fourier expansion of $u=v-\Delta v$ is
\[
u(x,y)
=\sum_{n,m\in\mathbb Z}\lambda_{n,m}a_{n,m}e^{2\pi i(nx+my)}.
\]
::: {.proof}
For each Fourier mode,
\[
\begin{aligned}
\Delta e^{2\pi i(nx+my)}
&=\left((2\pi in)^2+(2\pi im)^2\right)e^{2\pi i(nx+my)}\\
&=-4\pi^2(n^2+m^2)e^{2\pi i(nx+my)}.
\end{aligned}
\]
Since $v$ is a trigonometric polynomial, the sum is finite and differentiation term by term is immediate.
Therefore the coefficient of the $(n,m)$ mode in $v-\Delta v$ is
\[
\bigl(1+4\pi^2(n^2+m^2)\bigr)a_{n,m}
=\lambda_{n,m}a_{n,m}.
\]
:::

<1>2. One has
\[
\|u\|_{L^2([0,1]^2)}^2
=\sum_{n,m\in\mathbb Z}\lambda_{n,m}^2|a_{n,m}|^2.
\]
::: {.proof}
The functions
\[
e^{2\pi i(nx+my)},
\qquad (n,m)\in\mathbb Z^2,
\]
are orthonormal in $L^2([0,1]^2)$.
Applying the Pythagorean identity to the finite expansion in <1>1 gives the displayed equality.
:::

<1>3. The numerical series
\[
S=\sum_{n,m\in\mathbb Z}\frac1{\lambda_{n,m}^2}
\]
converges.
::: {.proof}
Because $4\pi^2>1$,
\[
\lambda_{n,m}
\ge 1+n^2+m^2.
\]
Moreover,
\[
(1+n^2+m^2)^2
\ge(1+n^2)(1+m^2).
\]
Hence
\[
\frac1{\lambda_{n,m}^2}
\le
\frac1{(1+n^2)(1+m^2)}.
\]
Therefore
\[
S
\le
\left(\sum_{n\in\mathbb Z}\frac1{1+n^2}\right)^2
<\infty,
\]
since the one-dimensional series is dominated in its tails by a constant multiple of $\sum_{n\ge1}n^{-2}$.
:::

<1>4. For every $(x,y)\in[0,1]^2$,
\[
|v(x,y)|
\le \sqrt S\,\|u\|_{L^2([0,1]^2)}.
\]
::: {.proof}
Since the Fourier sum for $v$ is finite,
\[
|v(x,y)|
\le\sum_{n,m}|a_{n,m}|.
\]
Insert the weights $\lambda_{n,m}$ and apply Cauchy--Schwarz:
\[
\begin{aligned}
\sum_{n,m}|a_{n,m}|
&=\sum_{n,m}\lambda_{n,m}|a_{n,m}|\frac1{\lambda_{n,m}}\\
&\le
\left(\sum_{n,m}\lambda_{n,m}^2|a_{n,m}|^2\right)^{1/2}
\left(\sum_{n,m}\frac1{\lambda_{n,m}^2}\right)^{1/2}.
\end{aligned}
\]
By <1>2--<1>3, this is
\[
\sqrt S\,\|u\|_2.
\]
:::

<1>5. Consequently
\[
\boxed{
\|v\|_{L^\infty([0,1]^2)}
\le C\|u\|_{L^2([0,1]^2)}
}
\]
with the constant
\[
C=\sqrt S
\]
independent of $v$.
::: {.proof}
Take the supremum of the pointwise estimate in <1>4 over $(x,y)\in[0,1]^2$.
The number $S$ in <1>3 is a fixed numerical constant and does not depend on the coefficients of $v$.
:::
:::
