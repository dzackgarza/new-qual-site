---
schema: qual/card@1
id: P-UCLAB06W-03
kind: problem
title: Composite trapezoid-rule error estimate
classification:
  areas: [prelim]
  topics:
  - Integrals
  - Taylor Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Qual Winter 2006 PDF; the source itself prints the factor $1/n$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The printed estimate is false for a general interval; the solution gives a constant-function counterexample and proves the corrected trapezoid estimate.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The exam printed the factor 1/n in front of the trapezoid sum, which fails for f=1 whenever b-a is not 1; the factor is now (b-a)/n.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added the identification of the printed
    sum with the h/2-weighted sum over consecutive pairs, which is what makes the per-interval bound
    add up; the reason the affine interpolant integrates to the trapezoid term, which is the step
    where the estimate is actually used; the evaluation of the integral of t(h - t) as h^3/6; and the
    simplification n h^3 = (b - a)^3 / n^2. The printed statement was then confirmed: the retained
    exam has no text layer, so the page was rendered as an image instead, and Problem 3 of
    assets/attachments/basic-06W.pdf, page 1, prints "(1/n)( 1/2 f(x_0) + f(x_1) + ... + f(x_{n-1}) +
    1/2 f(x_n) )" against the integral, with the bound "M/n^2" -- the prefactor 1/n that the erratum
    remark corrects, not (b-a)/n. The remark's counterexample is arithmetic on the same reading: for
    f identically 1 the bracket is 1 while the integral is b-a.
---

::: {.problem}
Let $f:[a,b]\to\RR$ be twice continuously differentiable, including at the endpoints.
Let
$$
a=x_0<x_1<\cdots<x_n=b
$$
be the uniform partition of $[a,b]$, so that $x_{i+1}-x_i=(b-a)/n$ for $0\leq i<n$.

Show that there exists $M$ such that for all $n\geq1$,
$$
\abs{
\frac{b-a}n\left(\frac12f(x_0)+f(x_1)+\cdots+f(x_{n-1})+\frac12f(x_n)\right)
-\int_a^b f(x)\,dx
}
\leq \frac{M}{n^2}.
$$

[Recall that the sum is an approximation of the integral in the Trapezoid Rule. It may be instructive to first solve the problem for $n=1$ and then address the general case.]
:::

::: {.remark title="Erratum"}
The exam prints the prefactor $1/n$ in place of $(b-a)/n$.
Under that reading the claim is false whenever $b-a\neq1$: for $f\equiv1$ the printed sum is $1$ and the integral is $b-a$, so their difference does not tend to $0$.
The statement above uses the trapezoid weight $(b-a)/n$.
:::

::: {.solution}
This is Problem 3 of the UCLA basic qualifying examination of Winter 2006, in the corrected form recorded in the remark above: the paper prints the prefactor $1/n$ where the trapezoid weight $(b-a)/n$ belongs, and the printed claim is false for $b-a\neq1$. No published solution set is transcribed: the argument is the card's own.

::: pf

::: {.pf-step #weights}
With $h=(b-a)/n$, the sum in the statement equals $\sum_{i=0}^{n-1}\frac h2\bigl(f(x_{i})+f(x_{i+1})\bigr)$.

::: pf-proof
In $\frac h1\left(\frac12f(x_{0})+f(x_{1})+\cdots+f(x_{n-1})+\frac12f(x_{n})\right)$ each interior value $f(x_{i})$ with $0<i<n$ appears once and each of $f(x_{0})$, $f(x_{n})$ appears with weight $\frac12$; the same is true of the sum of the $\frac h2$-weighted pairs, since $f(x_{i})$ for $0<i<n$ occurs in the pairs $i-1$ and $i$, contributing $\frac h2+\frac h2=h$ times it, while $f(x_{0})$ and $f(x_{n})$ occur once with weight $\frac h2$.
:::
:::

::: {.pf-step #remainder}
On $[x_{i},x_{i+1}]$, with $x=x_{i}+t$, $0\leq t\leq h$, and $L_{i}$ the affine interpolant of $f$ at the endpoints, there is for each $t$ a point $\xi_{t}\in(x_{i},x_{i+1})$ with $f(x_{i}+t)-L_{i}(x_{i}+t)=\frac{f''(\xi_{t})}{2}t(t-h)$.

::: pf-proof
The affine interpolant has the Newton form $L_{i}(x_{i}+t)=f(x_{i})+\frac{f(x_{i+1})-f(x_{i})}{h}t$, and $f$ is twice continuously differentiable on $[x_{i},x_{i+1}]$. The interpolation error formula for two nodes gives the displayed identity with some point $\xi_{t}$ depending on $t$, which is the standard remainder $f[x_{i},x_{i+1},x_{i}+t]\,t(t-h)$ rewritten.
:::
:::

::: {.pf-step #interval}
$\abs{\int_{x_{i}}^{x_{i+1}}f(x)\,dx-\frac h2\bigl(f(x_{i})+f(x_{i+1})\bigr)}\leq\frac{Kh^{3}}{12}$ with $K=\max_{[a,b]}\abs{f''}$.

::: pf-proof
Since $L_{i}$ is affine, $\int_{x_{i}}^{x_{i+1}}L_{i}=\frac h2(f(x_{i})+f(x_{i+1}))$. Hence the difference is $\int_{0}^{h}\left(f(x_{i}+t)-L_{i}(x_{i}+t)\right)dt$, whose modulus is at most $\frac K2\int_{0}^{h}\abs{t(t-h)}\,dt=\frac K2\cdot\frac{h^{3}}{6}=\frac{Kh^{3}}{12}$, using $\abs{t(t-h)}=t(h-t)$ for $0\leq t\leq h$ and $\int_{0}^{h}t(h-t)\,dt=\frac{h^{3}}{6}$.
:::
:::

::: {.pf-step #sum}
$\abs{T_{n}-\int_{a}^{b}f}\leq\frac{K(b-a)^{3}}{12n^{2}}$, so the estimate holds with $M=\frac{K(b-a)^{3}}{12}$.

::: pf-proof
Summing the estimate of step [](#interval){.pf-ref} over the $n$ subintervals gives $\abs{T_{n}-\int_{a}^{b}f}\leq n\cdot\frac{Kh^{3}}{12}$, and $h=(b-a)/n$ makes $nh^{3}=\frac{(b-a)^{3}}{n^{2}}$, so the bound is $\frac{K(b-a)^{3}}{12n^{2}}$. Taking $M=\frac{K(b-a)^{3}}{12}$, which is finite because $f''$ is continuous on the compact interval, gives the statement for every $n\geq1$.
:::
:::
:::

:::
