---
schema: qual/card@1
id: P-UCLAB06W-03
kind: problem
title: Composite trapezoid-rule error estimate
classification:
  areas: [prelim]
  topics: []
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
---

::: {.problem}
Let $f:[a,b]\to\mathbb R$ be twice continuously differentiable, including at the endpoints.
Let
\[
a=x_0<x_1<\cdots<x_n=b
\]
be the uniform partition of $[a,b]$, so that $x_{i+1}-x_i=(b-a)/n$ for $0\leq i<n$.

Show that there exists $M$ such that for all $n\geq1$,
\[
\left|
\frac1n\left(\frac12f(x_0)+f(x_1)+\cdots+f(x_{n-1})+\frac12f(x_n)\right)
-\int_a^b f(x)\,dx
\right|
\leq \frac{M}{n^2}.
\]

The source notes that the sum is an approximation of the integral in the trapezoid rule and suggests first treating $n=1$.
:::

::: {.solution}
<1>1. As printed, the asserted estimate is false on a general interval $[a,b]$ with $b-a\ne1$.

::: {.proof}
Take the twice continuously differentiable function $f\equiv1$. For every $n$,
$$
\frac12f(x_0)+f(x_1)+\cdots+f(x_{n-1})+\frac12f(x_n)=n.
$$
Hence the first term in the printed expression equals $1$, whereas
$$
\int_a^b f(x)\,dx=b-a.
$$
Thus the left-hand side equals the positive constant
$$
\abs{1-(b-a)}
$$
when $b-a\ne1$. No fixed $M$ can satisfy
$$
\abs{1-(b-a)}\le\frac{M}{n^2}
$$
for every $n$, because the right-hand side tends to $0$.
:::

<1>2. The standard trapezoid formula replaces the printed factor $1/n$ by
$$
h=\frac{b-a}{n}.
$$
Let
$$
T_n
=h\left(
\frac12f(x_0)+f(x_1)+\cdots+f(x_{n-1})+\frac12f(x_n)
\right).
$$
Put
$$
K=\max_{x\in[a,b]}\abs{f''(x)}.
$$

::: {.proof}
The maximum $K$ exists because $f''$ is continuous on the compact interval $[a,b]$. The quantity $T_n$ is the usual composite trapezoid sum for the uniform mesh size $h$.
:::

<1>3. On each subinterval $[x_i,x_{i+1}]$, if $L_i$ is the affine function agreeing with $f$ at the two endpoints, then for every $x\in[x_i,x_{i+1}]$,
$$
\abs{f(x)-L_i(x)}
\le
\frac K2(x-x_i)(x_{i+1}-x).
$$

::: {.proof}
Set
$$
q(x)=(x-x_i)(x_{i+1}-x).
$$
Then $q\ge0$ on the subinterval, $q$ vanishes at both endpoints, and
$$
q''(x)=-2.
$$
Since $L_i''=0$, the function
$$
\phi_+(x)=f(x)-L_i(x)-\frac K2q(x)
$$
satisfies
$$
\phi_+''(x)=f''(x)+K\ge0.
$$
Thus $\phi_+$ is convex. Its values at both endpoints are $0$, so convexity gives $\phi_+(x)\le0$ throughout the interval. Hence
$$
f(x)-L_i(x)\le\frac K2q(x).
$$

Similarly,
$$
\phi_-(x)=f(x)-L_i(x)+\frac K2q(x)
$$
satisfies
$$
\phi_-''(x)=f''(x)-K\le0.
$$
Thus $\phi_-$ is concave with zero endpoint values, so $\phi_-(x)\ge0$. Therefore
$$
f(x)-L_i(x)\ge-\frac K2q(x).
$$
Combining the two inequalities proves the claim.
:::

<1>4. The trapezoid error on one subinterval satisfies
$$
\abs{
\int_{x_i}^{x_{i+1}}f(x)\,dx
-
\frac h2\bigl(f(x_i)+f(x_{i+1})\bigr)
}
\le
\frac{Kh^3}{12}.
$$

::: {.proof}
Because $L_i$ is affine and takes the endpoint values of $f$,
$$
\int_{x_i}^{x_{i+1}}L_i(x)\,dx
=
\frac h2\bigl(f(x_i)+f(x_{i+1})\bigr).
$$
By step <1>3,
$$
\begin{aligned}
\abs{\int_{x_i}^{x_{i+1}}(f-L_i)(x)\,dx}
&\le
\frac K2\int_{x_i}^{x_{i+1}}(x-x_i)(x_{i+1}-x)\,dx\\
&=
\frac K2\int_0^h t(h-t)\,dt\\
&=
\frac{Kh^3}{12}.
\end{aligned}
$$
:::

<1>5. The corrected composite trapezoid estimate is
$$
\boxed{
\abs{T_n-\int_a^b f(x)\,dx}
\le
\frac{K(b-a)^3}{12n^2}
}.
$$

::: {.proof}
Sum the $n$ local errors from step <1>4 and use the triangle inequality:
$$
\abs{T_n-\int_a^b f(x)\,dx}
\le
n\frac{Kh^3}{12}.
$$
Since $h=(b-a)/n$,
$$
n\frac{Kh^3}{12}
=
\frac{K(b-a)^3}{12n^2}.
$$
:::

<1>6. If $b-a=1$, then the source's printed factor $1/n$ equals $h$, and the requested estimate is true with
$$
M=\frac K{12}.
$$
If $b-a\ne1$, the printed assertion is false.

::: {.proof}
When $b-a=1$, step <1>5 becomes exactly the printed estimate. When $b-a\ne1$, step <1>1 supplies a counterexample.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1 and <1>6 completely resolve the statement as printed, while steps <1>2--<1>5 prove the intended composite trapezoid estimate.
:::
:::
