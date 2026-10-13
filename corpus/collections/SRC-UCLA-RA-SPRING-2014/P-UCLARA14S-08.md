---
schema: qual/card@1
id: P-UCLARA14S-08
kind: problem
title: Entire function with simple zeros at the positive integers
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Construct a nonconstant entire function whose zeros are all simple and are exactly the positive natural numbers.
:::

::: {.solution}
Define
\[
E_1(w)
\coloneqq
(1-w)e^w
\]
and consider
\[
f(z)
\coloneqq
\prod_{n=1}^{\infty}
E_1\!\left(\frac zn\right)
=
\prod_{n=1}^{\infty}
\left(1-\frac zn\right)e^{z/n}.
\]

<1>1. There are constants $\delta>0$ and $C>0$ such that
\[
|\Log(1-w)+w|
\le
C|w|^2
\qquad
(|w|<\delta),
\]
where $\Log$ is the principal logarithm near $1$.

::: {.proof}
For $|w|<1$,
\[
\Log(1-w)
=
-\sum_{k=1}^{\infty}\frac{w^k}{k}.
\]
Hence
\[
\Log(1-w)+w
=
-\sum_{k=2}^{\infty}\frac{w^k}{k}.
\]
For $|w|\le1/2$,
\[
|\Log(1-w)+w|
\le
\sum_{k=2}^{\infty}|w|^k
\le
2|w|^2.
\]
Thus one may take $\delta=1/2$ and $C=2$.
:::

<1>2. For every $R>0$, the series
\[
\sum_{n=1}^{\infty}
\left[
\Log\left(1-\frac zn\right)+\frac zn
\right]
\]
converges uniformly on $|z|\le R$ after deleting finitely many initial terms.

::: {.proof}
Choose $N>2R$. Then for $n\ge N$ and $|z|\le R$,
\[
\left|\frac zn\right|
\le
\frac12.
\]
By step <1>1,
\[
\left|
\Log\left(1-\frac zn\right)+\frac zn
\right|
\le
2\frac{|z|^2}{n^2}
\le
2\frac{R^2}{n^2}.
\]
Since
\[
\sum_{n=N}^{\infty}\frac1{n^2}<\infty,
\]
the Weierstrass M-test gives uniform convergence of the tail on the closed disk.
:::

<1>3. The product defining $f$ converges uniformly on compact subsets of $\mathbb C$ to an entire function.

::: {.proof}
Fix $R>0$ and choose $N>2R$ as in step <1>2. For $n\ge N$ and $|z|\le R$,
\[
E_1\!\left(\frac zn\right)
=
\exp\left(
\Log\left(1-\frac zn\right)+\frac zn
\right).
\]
By step <1>2, the sum of the exponents converges uniformly on $|z|\le R$. Therefore the tail product
\[
\prod_{n=N}^{\infty}
E_1\!\left(\frac zn\right)
\]
converges uniformly there to the exponential of a holomorphic limit, hence to a holomorphic nonvanishing function.

Multiplying by the finite product
\[
\prod_{n=1}^{N-1}
E_1\!\left(\frac zn\right)
\]
shows that the full product converges uniformly on $|z|\le R$ to a holomorphic function. Since $R$ was arbitrary, $f$ is entire.
:::

<1>4. If $z\notin\mathbb N_{>0}$, then
\[
f(z)\ne0.
\]

::: {.proof}
Fix such a $z$. Choose $N>|z|+1$. The tail product from step <1>3 is nonzero because it is the exponential of a convergent series. Every factor in the finite product
\[
\prod_{n=1}^{N-1}
\left(1-\frac zn\right)e^{z/n}
\]
is also nonzero because $z\ne n$ for every positive integer $n$. Hence their product $f(z)$ is nonzero.
:::

<1>5. Every positive integer $m$ is a simple zero of $f$.

::: {.proof}
Factor out the $m$-th term:
\[
f(z)
=
\left(1-\frac zm\right)e^{z/m}
\prod_{n\ne m}
\left(1-\frac zn\right)e^{z/n}.
\]
By the same compact-uniform convergence argument as in step <1>3, the product over $n\ne m$ defines a holomorphic function near $z=m$. Step <1>4 applied to the product with the $m$-th factor removed shows that its value at $m$ is nonzero.

The factor
\[
1-\frac zm
\]
has a simple zero at $z=m$, while $e^{z/m}$ is nonzero there. Therefore $f$ has a simple zero at $m$.
:::

<1>6. Thus
\[
\boxed{
f(z)
=
\prod_{n=1}^{\infty}
\left(1-\frac zn\right)e^{z/n}
}
\]
is a nonconstant entire function whose zeros are exactly the positive natural numbers, all simple.

::: {.proof}
Entirety is step <1>3, absence of all other zeros is step <1>4, and simplicity at every positive integer is step <1>5. Since the function has zeros, it is not constant.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 provides the required construction and verifies all of its properties.
:::
:::
