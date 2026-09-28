---
schema: qual/card@1
id: P-BERK79S-19
kind: problem
title: Compactness of an integral transform of an $L^2$-bounded sequence
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Cauchy--Schwarz gives
    |g_n(x)|<=sqrt(5)*sqrt(int_0^1(x+y)dy)<=sqrt(15/2).
    For equicontinuity, the elementary inequality
    |sqrt(a)-sqrt(b)|<=sqrt(|a-b|) gives
    |g_n(x)-g_n(x')|<=sqrt(5)|x-x'|^{1/2}, uniformly in n.
    Arzela--Ascoli on [0,1] then yields a uniformly convergent subsequence.
---

::: {.problem}
Let $f_n:[0,1]\to\mathbb R$ be continuous and suppose
\[
\int_0^1f_n(y)^2\,dy\le5
\]
for every $n$.
Define
\[
g_n(x)=\int_0^1\sqrt{x+y}\,f_n(y)\,dy,
\qquad 0\le x\le1.
\]

1. Find a constant $K\ge0$ such that $|g_n(x)|\le K$ for every $n$ and every $x\in[0,1]$.

2. Prove that some subsequence of $\{g_n\}$ converges uniformly on $[0,1]$.
:::

::: {.solution}
<1>1. For every $n$,
$$
\norm{f_n}_{L^2([0,1])}\leq\sqrt5.
$$

::: {.proof}
The hypothesis gives
$$
\int_0^1 f_n(y)^2\,dy\leq5.
$$
Taking square roots gives the stated $L^2$ bound.
:::

<1>2. For every $x\in[0,1]$,
$$
\int_0^1(x+y)\,dy=x+\frac12\leq\frac32.
$$

::: {.proof}
Direct integration gives
$$
\int_0^1(x+y)\,dy
=
x+\frac12.
$$
Since $x\leq1$, this is at most $3/2$.
:::

<1>3. For every $n$ and every $x\in[0,1]$,
$$
\abs{g_n(x)}
\leq
\sqrt{\frac{15}{2}}.
$$

::: {.proof}
By Cauchy--Schwarz,
$$
\begin{aligned}
\abs{g_n(x)}
&=
\abs{
\int_0^1
\sqrt{x+y}\,f_n(y)\,dy
}\\
&\leq
\left(
\int_0^1(x+y)\,dy
\right)^{1/2}
\left(
\int_0^1f_n(y)^2\,dy
\right)^{1/2}.
\end{aligned}
$$
Apply steps <1>1--<1>2:
$$
\abs{g_n(x)}
\leq
\sqrt{\frac32}\sqrt5
=
\sqrt{\frac{15}{2}}.
$$
:::

<1>4. One may take
$$
\boxed{
K=\sqrt{\frac{15}{2}}.
}
$$

::: {.proof}
Step <1>3 gives the required uniform bound for this constant.
:::

<1>5. For all nonnegative real numbers $a,b$,
$$
\abs{\sqrt a-\sqrt b}
\leq
\sqrt{\abs{a-b}}.
$$

::: {.proof}
Assume without loss of generality that $a\geq b$. Then
$$
\begin{aligned}
(\sqrt a-\sqrt b)^2
&=
a+b-2\sqrt{ab}\\
&\leq
a-b,
\end{aligned}
$$
because
$$
b\leq\sqrt{ab}
$$
when $a\geq b\geq0$. Taking square roots gives the claim.
:::

<1>6. For every $n$ and all $x,x'\in[0,1]$,
$$
\abs{g_n(x)-g_n(x')}
\leq
\sqrt5\,\abs{x-x'}^{1/2}.
$$

::: {.proof}
By the definition of $g_n$ and Cauchy--Schwarz,
$$
\begin{aligned}
\abs{g_n(x)-g_n(x')}
&\leq
\left(
\int_0^1
\abs{
\sqrt{x+y}-\sqrt{x'+y}
}^2
\,dy
\right)^{1/2}\\
&\qquad\cdot
\left(
\int_0^1f_n(y)^2\,dy
\right)^{1/2}.
\end{aligned}
$$
By step <1>5,
$$
\abs{
\sqrt{x+y}-\sqrt{x'+y}
}^2
\leq
\abs{x-x'}.
$$
Thus
$$
\int_0^1
\abs{
\sqrt{x+y}-\sqrt{x'+y}
}^2
\,dy
\leq
\abs{x-x'}.
$$
Combine this with step <1>1 to obtain the displayed estimate.
:::

<1>7. The family
$$
\{g_n:n\geq1\}
$$
is uniformly bounded and equicontinuous on $[0,1]$.

::: {.proof}
Uniform boundedness is step <1>3.

For equicontinuity, let $\varepsilon>0$ and choose
$$
\delta=\frac{\varepsilon^2}{5}.
$$
If
$$
\abs{x-x'}<\delta,
$$
then step <1>6 gives
$$
\abs{g_n(x)-g_n(x')}
<
\sqrt5\sqrt\delta
=
\varepsilon
$$
for every $n$. This is equicontinuity.
:::

<1>8. Some subsequence of $(g_n)$ converges uniformly on $[0,1]$.

::: {.proof}
Each $g_n$ is continuous by the estimate in step <1>6. The interval
$[0,1]$ is compact, and step <1>7 gives uniform boundedness and
equicontinuity. The Arzelà--Ascoli theorem therefore gives a subsequence
which converges uniformly on $[0,1]$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>4 answers part (1), and step <1>8 proves part (2).
:::
:::
