---
schema: qual/card@1
id: P-UCLARA17S-08
kind: problem
title: Critical points of finite Blaschke products
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $a_1,\dots,a_n$ be $n\ge1$ points in the disk $D=\{\abs{z}<1\}$, possibly with repetitions, so that the function
$$
B(z)=\prod_{j=1}^n\frac{z-a_j}{1-\overline{a_j}z}
$$
has $n$ zeros in $D$. Prove that the derivative $B'(z)$ has $n-1$ zeros in $D$.
:::

::: {.solution}

For $a\in D$, write
$$
b_a(z)\coloneqq\frac{z-a}{1-\overline a z},
$$
so that $B=\prod_{j=1}^n b_{a_j}$.

::: pf

::: {.pf-step #s1-1}

Wherever $B(z)\ne0$,
$$
\frac{B'(z)}{B(z)}
=\sum_{j=1}^n
\frac{1-\abs{a_j}^2}{(z-a_j)(1-\overline{a_j}z)}.
$$


::: pf-proof

For one factor,
$$
b_a'(z)
=\frac{1-\abs{a}^2}{(1-\overline a z)^2},
$$
and hence
$$
\frac{b_a'(z)}{b_a(z)}
=\frac{1-\abs{a}^2}{(z-a)(1-\overline a z)}.
$$
Taking the logarithmic derivative of the product defining $B$ gives the displayed sum.

:::

:::

::: {.pf-step #s1-2}

For every $z$ with $\abs{z}=1$,
$$
\boxed{
\frac{zB'(z)}{B(z)}
=\sum_{j=1}^n\frac{1-\abs{a_j}^2}{\abs{z-a_j}^2}>0.}
$$


::: pf-proof

If $\abs{z}=1$, then
$$
(z-a)(1-\overline a z)
=z\abs{z-a}^2.
$$
Substituting this into step [](#s1-1){.pf-ref} gives the equality. Since every $\abs{a_j}<1$, each numerator $1-\abs{a_j}^2$ is positive, so the sum is strictly positive.

:::

:::

::: {.pf-step #s1-3}

The function $B'$ has no zeros on the unit circle, and along $\abs{z}=1$ its change of argument equals the change of argument of $B(z)/z$.


::: pf-proof

Each factor $b_{a_j}$ has modulus $1$ on the unit circle, so $B(z)\ne0$ there. Step [](#s1-2){.pf-ref} writes
$$
B'(z)=\frac{B(z)}{z}\,c(z),
$$
where $c(z)>0$ is real. Hence $B'(z)\ne0$ on the circle, and multiplication by the positive real function $c$ contributes no change of argument. Therefore
$$
\Delta_{\abs{z}=1}\arg B'
=\Delta_{\abs{z}=1}\arg(B/z).
$$

:::

:::

::: {.pf-step #s1-4}

As $z$ traverses the positively oriented unit circle once,
$$
\Delta\arg B(z)=2\pi n.
$$


::: pf-proof

The function $B$ is holomorphic on a neighborhood of the closed unit disk: if $a_j\ne0$, the corresponding factor has its only pole at $1/\overline{a_j}$, outside the closed unit disk, while the factor for $a_j=0$ is simply $z$. It has exactly the $n$ zeros $a_1,\ldots,a_n$ in the disk, counted with multiplicity, and no zeros on the boundary. By the argument principle,
$$
\frac1{2\pi}\Delta_{\abs{z}=1}\arg B=n.
$$

:::

:::

::: {.pf-step #s1-5}

As $z$ traverses the unit circle once,
$$
\Delta\arg B'(z)=2\pi(n-1).
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\Delta\arg B'
=\Delta\arg B-\Delta\arg z.
$$
Step [](#s1-4){.pf-ref} gives the first term as $2\pi n$, while $z$ itself winds once around $0$, so $\Delta\arg z=2\pi$. Thus the difference is $2\pi(n-1)$.

:::

:::

::: {.pf-step #s1-6}

The derivative $B'$ has exactly
$$
\boxed{n-1}
$$
zeros in $D$, counted with multiplicity.


::: pf-proof

The function $B'$ is holomorphic on a neighborhood of the closed unit disk and has no boundary zeros by step [](#s1-3){.pf-ref}. Applying the argument principle to $B'$ and using step [](#s1-5){.pf-ref} gives
$$
\#\{\text{zeros of }B'\text{ in }D\}
=\frac1{2\pi}\Delta_{\abs{z}=1}\arg B'
=n-1,
$$
counting multiplicities.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
