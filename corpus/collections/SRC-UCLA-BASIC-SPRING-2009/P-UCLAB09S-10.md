---
schema: qual/card@1
id: P-UCLAB09S-10
kind: problem
title: Leibniz series from an integral
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Problem 10. (a) Rigorously justify
\[
\int_0^1\frac{dx}{1+x^2}
=
\lim_{N\to\infty}\sum_{n=0}^N\frac{(-1)^n}{2n+1}.
\]

(b) Deduce the value of
\[
1-\frac13+\frac15-\frac17+\cdots.
\]
:::

::: {.solution}
<1>1. For every integer $N\ge0$ and every $x\in[0,1]$,
\[
\boxed{
\frac1{1+x^2}
=
\sum_{n=0}^N(-1)^nx^{2n}
+
(-1)^{N+1}
\frac{x^{2N+2}}{1+x^2}.
}
\]

::: {.proof}
Apply the finite geometric-series identity
\[
\frac1{1-r}
=
\sum_{n=0}^Nr^n
+
\frac{r^{N+1}}{1-r}
\]
with
\[
r=-x^2.
\]
Then
\[
1-r=1+x^2,
\]
and
\[
r^{N+1}
=
(-1)^{N+1}x^{2N+2}.
\]
:::

<1>2. Integrating step <1>1 over $[0,1]$ gives
\[
\int_0^1\frac{dx}{1+x^2}
=
\sum_{n=0}^N
\frac{(-1)^n}{2n+1}
+
R_N,
\]
where
\[
R_N
=
(-1)^{N+1}
\int_0^1
\frac{x^{2N+2}}{1+x^2}
\,dx.
\]

::: {.proof}
The finite sum may be integrated term by term:
\[
\int_0^1x^{2n}\,dx
=
\frac1{2n+1}.
\]
The last term is exactly the stated remainder.
:::

<1>3. The remainder satisfies
\[
\boxed{
|R_N|
\le
\frac1{2N+3}.
}
\]

::: {.proof}
For
\[
0\le x\le1,
\]
one has
\[
1+x^2\ge1.
\]
Hence
\[
0
\le
\frac{x^{2N+2}}{1+x^2}
\le
x^{2N+2}.
\]
Therefore
\[
\begin{aligned}
|R_N|
&\le
\int_0^1x^{2N+2}\,dx\\
&=
\frac1{2N+3}.
\end{aligned}
\]
:::

<1>4. Consequently
\[
R_N\to0.
\]

::: {.proof}
The upper bound from step <1>3 satisfies
\[
\frac1{2N+3}\to0.
\]
Apply the squeeze theorem.
:::

<1>5. Therefore
\[
\boxed{
\int_0^1\frac{dx}{1+x^2}
=
\lim_{N\to\infty}
\sum_{n=0}^N
\frac{(-1)^n}{2n+1}.
}
\]

::: {.proof}
Take
\[
N\to\infty
\]
in the identity from step <1>2 and use step <1>4.
This rigorously justifies part (a) without interchanging an infinite sum and an integral.
:::

<1>6. One has
\[
\int_0^1\frac{dx}{1+x^2}
=
\frac{\pi}{4}.
\]

::: {.proof}
An antiderivative is
\[
\arctan x.
\]
Thus
\[
\int_0^1\frac{dx}{1+x^2}
=
\arctan(1)-\arctan(0)
=
\frac{\pi}{4}.
\]
:::

<1>7. Hence
\[
\boxed{
1-\frac13+\frac15-\frac17+\cdots
=
\frac{\pi}{4}.
}
\]

::: {.proof}
The partial sums of the displayed alternating series are exactly
\[
\sum_{n=0}^N\frac{(-1)^n}{2n+1}.
\]
By step <1>5 their limit is the integral from step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>7 proves part (b).
:::
:::
