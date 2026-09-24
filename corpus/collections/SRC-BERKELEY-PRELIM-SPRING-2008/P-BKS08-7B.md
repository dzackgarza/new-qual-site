---
schema: qual/card@1
id: P-BKS08-7B
kind: problem
title: Evaluate a rational integral with denominator power five
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
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the parameter-differentiation recurrence and all four
    constants through the fifth denominator power against the vendored
    solution.
---

::: {.problem}
Evaluate
\[
\int_{-\infty}^{\infty}\frac{dx}{(1+x^2)^5}.
\]
:::

::: {.solution}
For $a>0$ and $m\ge1$, set
$$
J_m(a)\coloneqq
\int_{-\infty}^{\infty}\frac{dx}{(a+x^2)^m}.
$$

<1>1. One has
$$
J_1(a)=\pi a^{-1/2}.
$$

::: {.proof}
With the substitution $x=\sqrt a\,t$,
$$
\begin{aligned}
J_1(a)
&=\int_{-\infty}^{\infty}\frac{\sqrt a\,dt}
{a(1+t^2)}\\
&=a^{-1/2}\int_{-\infty}^{\infty}\frac{dt}{1+t^2}\\
&=\pi a^{-1/2}.
\end{aligned}
$$
:::

<1>2. For every $m\ge1$,
$$
J_{m+1}(a)=-\frac1mJ_m'(a).
$$

::: {.proof}
Differentiating under the integral sign gives
$$
J_m'(a)
=-m\int_{-\infty}^{\infty}\frac{dx}{(a+x^2)^{m+1}}
=-mJ_{m+1}(a).
$$
The differentiation is justified locally for $a>0$ by domination:
if $a$ ranges in a compact subinterval of $(0,\infty)$, the absolute
value of the differentiated integrand is bounded by a constant
multiple of $(1+x^2)^{-m-1}$, which is integrable.
:::

<1>3. Successive applications of step <1>2 give
$$
\begin{aligned}
J_2(a)&=\frac{\pi}{2}a^{-3/2},\\
J_3(a)&=\frac{3\pi}{8}a^{-5/2},\\
J_4(a)&=\frac{5\pi}{16}a^{-7/2},\\
J_5(a)&=\frac{35\pi}{128}a^{-9/2}.
\end{aligned}
$$

::: {.proof}
Starting from step <1>1,
$$
J_2(a)
=-J_1'(a)
=\frac{\pi}{2}a^{-3/2}.
$$
Then
$$
J_3(a)
=-\frac12J_2'(a)
=\frac{3\pi}{8}a^{-5/2},
$$
$$
J_4(a)
=-\frac13J_3'(a)
=\frac{5\pi}{16}a^{-7/2},
$$
and finally
$$
J_5(a)
=-\frac14J_4'(a)
=\frac{35\pi}{128}a^{-9/2}.
$$
:::

<1>4. Setting $a=1$ yields
$$
\boxed{
\int_{-\infty}^{\infty}\frac{dx}{(1+x^2)^5}
=\frac{35\pi}{128}.
}
$$

::: {.proof}
The integral is $J_5(1)$ by definition, and step <1>3 gives its value.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested evaluation.
:::
:::
