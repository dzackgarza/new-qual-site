---
schema: qual/card@1
id: P-BERK87S-12
kind: problem
title: Approximation of $\int_0^{1/2}\sin x/x\,dx$ within $0.005$
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
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the cubic Taylor polynomial sin x=x-x^3/6 with Lagrange remainder
    bounded by x^4/24 on [0,1/2]. After division by x and integration, the
    total error is at most 1/1536, which certifies I*=0.49.
---

::: {.problem}
Evaluate
\[
I=\int_0^{1/2}\frac{\sin x}{x}\,dx
\]
to an accuracy of two decimal places: find $I^*$ such that
\[
|I-I^*|<0.005.
\]
:::

::: {.solution}
<1>1. For every $x\in[0,1/2]$,
$$
\sin x
=
x-\frac{x^3}{6}+R(x),
\qquad
\abs{R(x)}
\leq
\frac{x^4}{24}.
$$

::: {.proof}
Taylor's theorem about $0$, through degree $3$, gives
$$
\sin x
=
x-\frac{x^3}{6}
+
\frac{\sin \xi_x}{24}x^4
$$
for some $\xi_x$ between $0$ and $x$. Since
$$
\abs{\sin \xi_x}\leq1,
$$
the stated remainder bound follows.
:::

<1>2. If
$$
I_0
\coloneqq
\int_0^{1/2}
\left(1-\frac{x^2}{6}\right)\,dx,
$$
then
$$
I_0
=
\frac12-\frac1{144}
=
\frac{71}{144}.
$$

::: {.proof}
Direct integration gives
$$
\begin{aligned}
I_0
&=
\left[
x-\frac{x^3}{18}
\right]_{0}^{1/2}\\
&=
\frac12-\frac{1}{8\cdot18}\\
&=
\frac12-\frac1{144}.
\end{aligned}
$$
:::

<1>3. The approximation error satisfies
$$
\abs{I-I_0}
\leq
\frac1{1536}.
$$

::: {.proof}
For $x>0$, step <1>1 gives
$$
\frac{\sin x}{x}
=
1-\frac{x^2}{6}
+
\frac{R(x)}x,
$$
with
$$
\abs{\frac{R(x)}x}
\leq
\frac{x^3}{24}.
$$
The same bound extends continuously to $x=0$. Therefore
$$
\begin{aligned}
\abs{I-I_0}
&\leq
\int_0^{1/2}\frac{x^3}{24}\,dx\\
&=
\left[
\frac{x^4}{96}
\right]_{0}^{1/2}\\
&=
\frac{1}{16\cdot96}\\
&=
\frac1{1536}.
\end{aligned}
$$
:::

<1>4. The number
$$
\boxed{I^*=0.49}
$$
satisfies
$$
\abs{I-I^*}<0.005.
$$

::: {.proof}
By steps <1>2 and <1>3,
$$
\begin{aligned}
\abs{I-0.49}
&\leq
\abs{I-I_0}
+
\abs{I_0-0.49}\\
&\leq
\frac1{1536}
+
\left(
\frac{71}{144}-\frac{49}{100}
\right)\\
&=
\frac1{1536}
+
\frac{11}{3600}.
\end{aligned}
$$
Moreover,
$$
\frac1{1536}<\frac1{1500}
\qquad\text{and}\qquad
\frac{11}{3600}<\frac{11}{3300}=\frac1{300},
$$
so
$$
\abs{I-0.49}
<
\frac1{1500}+\frac1{300}
=
\frac1{250}
=
0.004
<
0.005.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required two-decimal approximation with the stated
strict error tolerance.
:::
:::
