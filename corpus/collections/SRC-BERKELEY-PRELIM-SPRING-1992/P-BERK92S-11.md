---
schema: qual/card@1
id: P-BERK92S-11
kind: problem
title: Laurent series for a logarithm branch on $1<|z|<2$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Find a Laurent series converging in the annulus
\[
1<|z|<2
\]
to a branch of
\[
\log\left(\frac{z(2-z)}{1-z}\right).
\]
:::

::: {.solution}
On the annulus $1<\abs{z}<2$,
$$
\frac{z(2-z)}{1-z}
=-2\,\frac{1-z/2}{1-1/z}.
$$

<1>1. The Laurent series
$$
L(z)\coloneqq
\log2+i\pi
-\sum_{n=1}^{\infty}\frac{z^n}{n2^n}
+\sum_{n=1}^{\infty}\frac{z^{-n}}n
$$
converges normally on compact subsets of $1<\abs{z}<2$.

::: {.proof}
On this annulus,
$$
\abs{\frac z2}<1,
\qquad
\abs{\frac1z}<1.
$$
Thus both geometric logarithm series
$$
-\sum_{n=1}^{\infty}\frac{(z/2)^n}{n},
\qquad
-\sum_{n=1}^{\infty}\frac{(1/z)^n}{n}
$$
converge normally on compact subannuli. The displayed series for
$L$ is their difference plus the constant $\log2+i\pi$.
:::

<1>2. On $1<\abs{z}<2$,
$$
\exp L(z)=\frac{z(2-z)}{1-z}.
$$

::: {.proof}
For $\abs{w}<1$,
$$
-\sum_{n=1}^{\infty}\frac{w^n}{n}=\Log(1-w),
$$
where this is the holomorphic logarithm normalized to vanish at
$w=0$. Hence
$$
\begin{aligned}
L(z)
&=\log2+i\pi+\Log(1-z/2)-\Log(1-1/z),
\end{aligned}
$$
and therefore
$$
\begin{aligned}
\exp L(z)
&=-2\,\frac{1-z/2}{1-1/z}\\
&=\frac{z(2-z)}{1-z}.
\end{aligned}
$$
:::

<1>3. The requested Laurent series is
$$
\boxed{
\log2+i\pi
-\sum_{n=1}^{\infty}\frac{z^n}{n2^n}
+\sum_{n=1}^{\infty}\frac{z^{-n}}n
}.
$$

::: {.proof}
By step <1>1 it is holomorphic on the specified annulus, and by step
<1>2 its exponential is the given nonvanishing holomorphic function.
Thus it is a branch of its logarithm there.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required Laurent series and its domain of
convergence.
:::
:::
