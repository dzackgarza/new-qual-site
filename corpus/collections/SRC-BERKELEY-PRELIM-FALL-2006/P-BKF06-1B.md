---
schema: qual/card@1
id: P-BKF06-1B
kind: problem
title: Entire functions with $\lvert f(z^2)\rvert\le2\lvert f(z)\rvert$ are constant
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the iterated growth bound and Cauchy estimate. The
    retained solution omits the factor m! in the derivative form of Cauchy's
    estimate; restoring it does not affect the limiting argument.
---

::: {.problem}
Let $f:\mathbb C\to\mathbb C$ be entire.
Assume
\[
|f(z^2)|\le2|f(z)|
\]
for all $z\in\mathbb C$.
Show that $f$ is constant.
:::

::: {.solution}
<1>1. For every integer $n\ge0$ and every $z\in\CC$,
$$
\abs{f\left(z^{2^n}\right)}
\le
2^n\abs{f(z)}.
$$

::: {.proof}
For $n=0$ this is equality. Suppose it holds for $n$. Applying the
hypothesis to $z^{2^n}$ gives
$$
\begin{aligned}
\abs{f\left(z^{2^{n+1}}\right)}
&=
\abs{f\left((z^{2^n})^2\right)}
\\
&\le
2\abs{f\left(z^{2^n}\right)}
\\
&\le
2^{n+1}\abs{f(z)}.
\end{aligned}
$$
The claim follows by induction.
:::

<1>2. Let
$$
M=\max_{\abs z=2}\abs{f(z)}
$$
and
$$
R_n=2^{2^n}.
$$
Then
$$
\max_{\abs w=R_n}\abs{f(w)}
\le
2^nM.
$$

::: {.proof}
The maximum $M$ exists because $f$ is continuous on the compact
circle $\abs z=2$. If $\abs w=R_n$, choose a $2^n$-th root $z$ of
$w$. Then
$$
\abs z=R_n^{1/2^n}=2.
$$
By step <1>1,
$$
\abs{f(w)}
=
\abs{f\left(z^{2^n}\right)}
\le
2^n\abs{f(z)}
\le
2^nM.
$$
Taking the maximum over the circle proves the claim.
:::

<1>3. For every integer $m\ge1$ and every $n\ge0$,
$$
\abs{f^{(m)}(0)}
\le
m!M\,2^{n-m2^n}.
$$

::: {.proof}
Cauchy's derivative estimate on the circle of radius $R_n$ gives
$$
\abs{f^{(m)}(0)}
\le
\frac{m!}{R_n^m}
\max_{\abs w=R_n}\abs{f(w)}.
$$
Using step <1>2 and $R_n=2^{2^n}$ yields
$$
\abs{f^{(m)}(0)}
\le
\frac{m!2^nM}{2^{m2^n}}
=
m!M\,2^{n-m2^n}.
$$
:::

<1>4. For every $m\ge1$,
$$
f^{(m)}(0)=0.
$$

::: {.proof}
Fix $m\ge1$. Since
$$
n-m2^n\longrightarrow-\infty,
$$
the right-hand side in step <1>3 tends to zero as $n\to\infty$.
The nonnegative number $\abs{f^{(m)}(0)}$ is bounded by all of these
quantities, so it must be zero.
:::

<1>5. The entire function $f$ is constant.

::: {.proof}
The Taylor series of $f$ at $0$ converges on all of $\CC$. By step
<1>4, every coefficient of positive degree vanishes. Hence
$$
f(z)=f(0)
$$
for every $z\in\CC$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the required conclusion.
:::
:::
