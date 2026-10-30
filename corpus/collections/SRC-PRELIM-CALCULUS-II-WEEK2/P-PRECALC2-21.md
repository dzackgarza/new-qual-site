---
schema: qual/card@1
id: P-PRECALC2-21
kind: problem
title: Riemann sum limits of $\sum_k\frac{1}{\sqrt{n^2+k^2}}$ and $\sum_k\frac{1}{\sqrt{n^2+k}}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate the following limits or prove that they diverge:
$$
\lim_{n \to \infty} \left( \frac{1}{\sqrt{n^{2} + 1^{2}}} + \frac{1}{\sqrt{n^{2} + 2^{2}}} + \cdots + \frac{1}{\sqrt{n^{2} + n^{2}}} \right); \tag{1}
$$
$$
\lim_{n \to \infty} \left( \frac{1}{\sqrt{n^{2} + 1}} + \frac{1}{\sqrt{n^{2} + 2}} + \cdots + \frac{1}{\sqrt{n^{2} + n}} \right); \tag{2}
$$
$$
\lim_{n \to \infty} \left( \frac{1}{\sqrt{n^{2} + 1}} + \frac{1}{\sqrt{n^{2} + 2}} + \cdots + \frac{1}{\sqrt{n^{2} + n^{2}}} \right). \tag{3}
$$
:::

::: {.solution}

## Limit (1)

Let
$$
S_n
=
\sum_{k=1}^{n}
\frac1{\sqrt{n^2+k^2}}.
$$

::: pf

::: {.pf-step #s1-1}

One can rewrite $S_n$ as
$$
\boxed{
S_n
=
\frac1n
\sum_{k=1}^{n}
\frac1{\sqrt{1+(k/n)^2}}}.
$$


::: pf-proof

Factor $n^2$ from each square root:
$$
\sqrt{n^2+k^2}
=
n\sqrt{1+(k/n)^2}.
$$

:::

:::

::: pf-step

The expression in step [](#s1-1){.pf-ref} is the right-endpoint Riemann sum for
$$
f(x)=\frac1{\sqrt{1+x^2}}
$$
on $[0,1]$.


::: pf-proof

The interval width is
$$
\Delta x=\frac1n,
$$
and the right endpoints are
$$
x_k=\frac{k}{n}.
$$
Thus
$$
\frac1n\sum_{k=1}^nf(k/n)
$$
is exactly the right-endpoint Riemann sum.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\lim_{n\to\infty}S_n
=
\int_0^1
\frac{dx}{\sqrt{1+x^2}}.
$$


::: pf-proof

The function $f$ is continuous on $[0,1]$, so its Riemann sums converge
to its integral.

:::

:::

::: {.pf-step #s1-4}

An antiderivative is
$$
\boxed{
\operatorname{arsinh}x
=
\log\left(x+\sqrt{1+x^2}\right)}.
$$


::: pf-proof

Differentiate:
$$
\frac{d}{dx}\log\left(x+\sqrt{1+x^2}\right)
=
\frac1{\sqrt{1+x^2}}.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\lim_{n\to\infty}S_n
=
\log(1+\sqrt2)}.
$$


::: pf-proof

Evaluate step [](#s1-3){.pf-ref} using step [](#s1-4){.pf-ref}:
$$
\int_0^1\frac{dx}{\sqrt{1+x^2}}
=
\log(1+\sqrt2)-\log1.
$$

:::

:::

::: {.pf-step #s1-6}

Rewrite
$$
\boxed{
T_n
=
\frac1n
\sum_{k=1}^{n}
\frac1{\sqrt{1+k/n^2}}}.
$$


::: pf-proof

Factor $n^2$ from the denominator:
$$
\sqrt{n^2+k}
=
n\sqrt{1+k/n^2}.
$$

:::

:::

::: {.pf-step #s1-7}

For $1\le k\le n$,
$$
0<\frac{k}{n^2}\le\frac1n.
$$


::: pf-proof

Since $k\le n$,
$$
\frac{k}{n^2}
\le
\frac{n}{n^2}
=
\frac1n.
$$

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\frac1{\sqrt{1+1/n}}
\le
\frac1{\sqrt{1+k/n^2}}
\le
1.
$$


::: pf-proof

The function
$$
x\mapsto\frac1{\sqrt{1+x}}
$$
is decreasing for $x\ge0$. Apply step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Averaging the inequalities in step [](#s1-8){.pf-ref},
$$
\boxed{
\frac1{\sqrt{1+1/n}}
\le
T_n
\le
1}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
T_n
=
\frac1n\sum_{k=1}^{n}
\frac1{\sqrt{1+k/n^2}}.
$$
Average the lower and upper bounds from step [](#s1-8){.pf-ref} over the $n$ terms.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\lim_{n\to\infty}T_n=1}.
$$


::: pf-proof

The lower bound in step [](#s1-9){.pf-ref} tends to $1$, and the upper bound is exactly
$1$. Apply the squeeze theorem.

:::

:::

::: {.pf-step #s1-11}

For $1\le k\le n^2$,
$$
n^2+k\le2n^2.
$$


::: pf-proof

Since $k\le n^2$,
$$
n^2+k
\le
n^2+n^2
=
2n^2.
$$

:::

:::

::: {.pf-step #s1-12}

Hence every term satisfies
$$
\boxed{
\frac1{\sqrt{n^2+k}}
\ge
\frac1{\sqrt2\,n}}.
$$


::: pf-proof

Take square roots in step [](#s1-11){.pf-ref}:
$$
\sqrt{n^2+k}
\le
\sqrt2\,n.
$$
All quantities are positive, so taking reciprocals reverses the inequality.

:::

:::

::: pf-step

Therefore
$$
U_n
\ge
n^2\cdot\frac1{\sqrt2\,n}
=
\frac{n}{\sqrt2}.
$$


::: pf-proof

There are $n^2$ terms in the sum, each bounded below as in step [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Hence
$$
\boxed{
U_n\to+\infty}.
$$


::: pf-proof

The lower bound
$$
\frac{n}{\sqrt2}
$$
tends to $+\infty$.

:::

:::

::: {.pf-step #s1-15}

Thus the three answers are
$$
\boxed{
\log(1+\sqrt2),\qquad
1,\qquad
+\infty}.
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} and [](#s1-10){.pf-ref}, and [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} gives all three requested limits.

:::

:::

:::
