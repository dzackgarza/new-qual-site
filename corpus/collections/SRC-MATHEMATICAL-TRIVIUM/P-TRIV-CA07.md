---
schema: qual/card@1
id: P-TRIV-CA07
kind: problem
title: Laurent series of $\sin\frac{z}{1-z}$ about $z=1$
classification:
  areas: [complex-analysis]
  topics:
  - Laurent Series
  - Essential Singularities
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the Laurent series of $f(z) = \sin\frac{z}{1 - z}$ around $z_0 = 1$; give the region of convergence.
:::

::: {.solution}

Set
$$
w=z-1.
$$
Then
$$
\frac{z}{1-z}
=
-1-\frac1w.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
f(z)
=
-\sin\left(1+\frac1w\right).
$$


::: pf-proof

Since
$$
z=1+w
$$
and
$$
1-z=-w,
$$
one gets
$$
\frac{z}{1-z}
=
\frac{1+w}{-w}
=
-1-\frac1w.
$$
Using oddness of sine gives the displayed formula.

:::

:::

::: {.pf-step #s1-2}

The sine addition formula gives
$$
f(z)
=
-\sin 1\,
\cos\left(\frac1w\right)
-
\cos 1\,
\sin\left(\frac1w\right).
$$


::: pf-proof

Apply
$$
\sin(a+b)
=
\sin a\cos b+\cos a\sin b
$$
with
$$
a=1,
\qquad
b=1/w,
$$
and then multiply by $-1$ as in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

For $w\neq0$,
$$
\cos\left(\frac1w\right)
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{(2n)!}w^{-2n},
$$
and
$$
\sin\left(\frac1w\right)
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{(2n+1)!}w^{-(2n+1)}.
$$


::: pf-proof

Substitute $1/w$ into the globally convergent Taylor series for cosine and
sine.

:::

:::

::: {.pf-step #s1-4}

Therefore the Laurent series about $z=1$ is
$$
\boxed{
\begin{aligned}
\sin\frac{z}{1-z}
&=
-\sin1
\sum_{n=0}^{\infty}
\frac{(-1)^n}{(2n)!}(z-1)^{-2n}\\
&\qquad
-\cos1
\sum_{n=0}^{\infty}
\frac{(-1)^n}{(2n+1)!}(z-1)^{-(2n+1)}.
\end{aligned}
}
$$


::: pf-proof

Substitute the two expansions from step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref} and replace
$w$ by $z-1$.

:::

:::

::: {.pf-step #s1-5}

The region of convergence is
$$
\boxed{
0<\abs{z-1}<\infty.
}
$$


::: pf-proof

The Taylor series for sine and cosine converge for every finite complex
argument. Thus after substituting $1/(z-1)$ they converge for every
$z\neq1$. The center $z=1$ is excluded because the original function has an
essential singularity there.

:::

:::

::: pf-step

The singularity at $z=1$ is essential.


::: pf-proof

Step [](#s1-4){.pf-ref} contains infinitely many nonzero negative-power terms. Hence the
principal part is infinite, which characterizes an essential singularity.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give the Laurent series and its exact region of convergence.

:::

:::

:::
