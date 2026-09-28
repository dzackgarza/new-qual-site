---
schema: qual/card@1
id: P-BKS10-1B
kind: problem
title: Uniform convergence and the mean value of an oscillatory series
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the Weierstrass M-test, termwise integration, and the R-uniform tail estimate needed to pass from finite partial sums to the limiting mean.
---

::: {.problem}
Show that
\[
f(x)=\sum_{n=0}^\infty \frac{e^{i\sqrt n\,x}}{n^2+1}
\]
converges uniformly for real \(x\). Prove that
\[
\lim_{R\to+\infty}\frac1{2R}\int_{-R}^{R}f(x)\,dx
\]
exists and calculate it.
:::

::: {.solution}
For $N\geq0$, set
$$
S_N(x)
\coloneqq
\sum_{n=0}^N
\frac{e^{i\sqrt n\,x}}{n^2+1}.
$$

<1>1. The series defining $f$ converges uniformly on $\RR$.

::: {.proof}
For every real $x$ and every $n\geq0$,
$$
\abs{
\frac{e^{i\sqrt n\,x}}{n^2+1}
}
=
\frac{1}{n^2+1}.
$$
The numerical series
$$
\sum_{n=0}^{\infty}\frac1{n^2+1}
$$
converges. The Weierstrass M-test therefore gives uniform convergence of
$S_N$ to $f$ on all of $\RR$.
:::

<1>2. For $n=0$, the mean of the $n$th summand over $[-R,R]$ is $1$.
For every $n\geq1$, it is
$$
\frac{1}{n^2+1}
\frac{\sin(\sqrt n\,R)}{\sqrt n\,R}.
$$

::: {.proof}
The $n=0$ summand is identically $1$. If $n\geq1$, then
$$
\begin{aligned}
\frac1{2R}
\int_{-R}^{R}
\frac{e^{i\sqrt n\,x}}{n^2+1}\,dx
&=
\frac{1}{n^2+1}
\frac{1}{2R}
\left[
\frac{e^{i\sqrt n\,x}}{i\sqrt n}
\right]_{-R}^{R}\\
&=
\frac{1}{n^2+1}
\frac{\sin(\sqrt n\,R)}{\sqrt n\,R}.
\end{aligned}
$$
:::

<1>3. For each fixed $N$,
$$
\lim_{R\to\infty}
\frac1{2R}\int_{-R}^{R}S_N(x)\,dx
=
1.
$$

::: {.proof}
By step <1>2, the mean of $S_N$ is
$$
1
+
\sum_{n=1}^N
\frac{1}{n^2+1}
\frac{\sin(\sqrt n\,R)}{\sqrt n\,R}.
$$
For each fixed $n\geq1$,
$$
\left|
\frac{\sin(\sqrt n\,R)}{\sqrt n\,R}
\right|
\leq
\frac{1}{\sqrt n\,R}
\longrightarrow0.
$$
The sum is finite, so its nonconstant terms all tend to $0$.
:::

<1>4. For every $N$ and every $R>0$,
$$
\abs{
\frac1{2R}
\int_{-R}^{R}
\bigl(f(x)-S_N(x)\bigr)\,dx
}
\leq
\sum_{n=N+1}^{\infty}\frac1{n^2+1}.
$$

::: {.proof}
Uniform convergence permits termwise subtraction, and for every $x$,
$$
\abs{f(x)-S_N(x)}
\leq
\sum_{n=N+1}^{\infty}\frac1{n^2+1}.
$$
Hence
$$
\begin{aligned}
\abs{
\frac1{2R}
\int_{-R}^{R}
(f-S_N)(x)\,dx
}
&\leq
\frac1{2R}
\int_{-R}^{R}
\abs{f(x)-S_N(x)}\,dx\\
&\leq
\sum_{n=N+1}^{\infty}\frac1{n^2+1}.
\end{aligned}
$$
The bound is independent of $R$.
:::

<1>5. The requested limit exists and equals
$$
\boxed{1}.
$$

::: {.proof}
Let $\varepsilon>0$. Choose $N$ so large that
$$
\sum_{n=N+1}^{\infty}\frac1{n^2+1}
<
\frac{\varepsilon}{2}.
$$
By step <1>3, for all sufficiently large $R$,
$$
\abs{
\frac1{2R}\int_{-R}^{R}S_N(x)\,dx-1
}
<
\frac{\varepsilon}{2}.
$$
Step <1>4 then gives
$$
\abs{
\frac1{2R}\int_{-R}^{R}f(x)\,dx-1
}
<
\varepsilon.
$$
This proves both existence of the limit and its value.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves uniform convergence, and step <1>5 computes the requested
mean.
:::
:::
