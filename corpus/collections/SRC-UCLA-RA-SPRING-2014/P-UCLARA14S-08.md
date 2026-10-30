---
schema: qual/card@1
id: P-UCLARA14S-08
kind: problem
title: Entire function with simple zeros at the positive integers
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Zeros
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
$$
E_1(w)
\coloneqq
(1-w)e^w
$$
and consider
$$
f(z)
\coloneqq
\prod_{n=1}^{\infty}
E_1\!\left(\frac zn\right)
=
\prod_{n=1}^{\infty}
\left(1-\frac zn\right)e^{z/n}.
$$

::: pf

::: {.pf-step #s1-1}

There are constants $\delta>0$ and $C>0$ such that
$$
\abs{\Log(1-w)+w}
\le
C\abs{w}^2
\qquad
(\abs{w}<\delta),
$$
where $\Log$ is the principal logarithm near $1$.


::: pf-proof

For $\abs{w}<1$,
$$
\Log(1-w)
=
-\sum_{k=1}^{\infty}\frac{w^k}{k}.
$$
Hence
$$
\Log(1-w)+w
=
-\sum_{k=2}^{\infty}\frac{w^k}{k}.
$$
For $\abs{w}\le1/2$,
$$
\abs{\Log(1-w)+w}
\le
\sum_{k=2}^{\infty}\abs{w}^k
\le
2\abs{w}^2.
$$
Thus one may take $\delta=1/2$ and $C=2$.

:::

:::

::: {.pf-step #s1-2}

For every $R>0$, the series
$$
\sum_{n=1}^{\infty}
\left[
\Log\left(1-\frac zn\right)+\frac zn
\right]
$$
converges uniformly on $\abs{z}\le R$ after deleting finitely many initial terms.


::: pf-proof

Choose $N>2R$. Then for $n\ge N$ and $\abs{z}\le R$,
$$
\abs{\frac zn}
\le
\frac12.
$$
By step [](#s1-1){.pf-ref},
$$
\abs{
\Log\left(1-\frac zn\right)+\frac zn
}
\le
2\frac{\abs{z}^2}{n^2}
\le
2\frac{R^2}{n^2}.
$$
Since
$$
\sum_{n=N}^{\infty}\frac1{n^2}<\infty,
$$
the Weierstrass M-test gives uniform convergence of the tail on the closed disk.

:::

:::

::: {.pf-step #s1-3}

The product defining $f$ converges uniformly on compact subsets of $\CC$ to an entire function.


::: pf-proof

Fix $R>0$ and choose $N>2R$ as in step [](#s1-2){.pf-ref}. For $n\ge N$ and $\abs{z}\le R$,
$$
E_1\!\left(\frac zn\right)
=
\exp\left(
\Log\left(1-\frac zn\right)+\frac zn
\right).
$$
By step [](#s1-2){.pf-ref}, the sum of the exponents converges uniformly on $\abs{z}\le R$. Therefore the tail product
$$
\prod_{n=N}^{\infty}
E_1\!\left(\frac zn\right)
$$
converges uniformly there to the exponential of a holomorphic limit, hence to a holomorphic nonvanishing function.

Multiplying by the finite product
$$
\prod_{n=1}^{N-1}
E_1\!\left(\frac zn\right)
$$
shows that the full product converges uniformly on $\abs{z}\le R$ to a holomorphic function. Since $R$ was arbitrary, $f$ is entire.

:::

:::

::: {.pf-step #s1-4}

If $z\notin\NN_{>0}$, then
$$
f(z)\ne0.
$$


::: pf-proof

Fix such a $z$. Choose $N>\abs{z}+1$. The tail product from step [](#s1-3){.pf-ref} is nonzero because it is the exponential of a convergent series. Every factor in the finite product
$$
\prod_{n=1}^{N-1}
\left(1-\frac zn\right)e^{z/n}
$$
is also nonzero because $z\ne n$ for every positive integer $n$. Hence their product $f(z)$ is nonzero.

:::

:::

::: {.pf-step #s1-5}

Every positive integer $m$ is a simple zero of $f$.


::: pf-proof

Factor out the $m$-th term:
$$
f(z)
=
\left(1-\frac zm\right)e^{z/m}
\prod_{n\ne m}
\left(1-\frac zn\right)e^{z/n}.
$$
By the same compact-uniform convergence argument as in step [](#s1-3){.pf-ref}, the product over $n\ne m$ defines a holomorphic function near $z=m$. Step [](#s1-4){.pf-ref} applied to the product with the $m$-th factor removed shows that its value at $m$ is nonzero.

The factor
$$
1-\frac zm
$$
has a simple zero at $z=m$, while $e^{z/m}$ is nonzero there. Therefore $f$ has a simple zero at $m$.

:::

:::

::: {.pf-step #s1-6}

Thus
$$
\boxed{
f(z)
=
\prod_{n=1}^{\infty}
\left(1-\frac zn\right)e^{z/n}
}
$$
is a nonconstant entire function whose zeros are exactly the positive natural numbers, all simple.


::: pf-proof

Entirety is step [](#s1-3){.pf-ref}, absence of all other zeros is step [](#s1-4){.pf-ref}, and simplicity at every positive integer is step [](#s1-5){.pf-ref}. Since the function has zeros, it is not constant.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} provides the required construction and verifies all of its properties.

:::

:::

:::
