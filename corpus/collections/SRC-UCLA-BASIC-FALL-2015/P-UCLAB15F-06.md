---
schema: qual/card@1
id: P-UCLAB15F-06
kind: problem
title: A complete metric compatible with the punctured-line topology
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
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $X=\RR\setminus\{0\}$.
Find a metric $\rho$ on $X$ such that:

1. $(X,\rho)$ is complete;

2. for every sequence $\{x_n\}\subset X$ and every $x\in X$,
$$
\lim_{n\to\infty}\abs{x_n-x}=0
\quad\Longleftrightarrow\quad
x_n\to x\text{ in }(X,\rho).
$$

Prove both properties, together with all other assertions used in your construction.
:::

::: {.solution}

Define
$$
\boxed{
\rho(x,y)
=
\abs{x-y}
+
\abs{\frac1x-\frac1y}
},
\qquad
x,y\in X.
$$

::: pf

::: {.pf-step #s1-1}

The function $\rho$ is a metric on $X$.


::: pf-proof

Nonnegativity and symmetry are immediate.

If
$$
\rho(x,y)=0,
$$
then in particular
$$
\abs{x-y}=0,
$$
so $x=y$.
Conversely,
$$
\rho(x,x)=0.
$$

For the triangle inequality, if $x,y,z\in X$, then
$$
\abs{x-z}
\le
\abs{x-y}+\abs{y-z}
$$
and
$$
\abs{\frac1x-\frac1z}
\le
\abs{\frac1x-\frac1y}
+
\abs{\frac1y-\frac1z}.
$$
Adding the two inequalities gives
$$
\rho(x,z)
\le
\rho(x,y)+\rho(y,z).
$$
Thus $\rho$ is a metric.

:::

:::

::: {.pf-step #s1-2}

If
$$
x_n\to x
$$
in the metric $\rho$, then
$$
\abs{x_n-x}\to0.
$$


::: pf-proof

By definition,
$$
\abs{x_n-x}
\le
\rho(x_n,x).
$$
Hence convergence in $\rho$ implies ordinary convergence.

:::

:::

::: {.pf-step #s1-3}

If
$$
\abs{x_n-x}\to0
$$
for some $x\in X$, then
$$
\abs{\frac1{x_n}-\frac1x}\to0.
$$


::: pf-proof

Since $x\ne0$, choose $N$ such that for $n\ge N$,
$$
\abs{x_n-x}<\frac{\abs{x}}{2}.
$$
Then
$$
\abs{x_n}
\ge
\abs{x}-\abs{x_n-x}
>
\frac{\abs{x}}{2}.
$$
Therefore, for $n\ge N$,
$$
\abs{
\frac1{x_n}-\frac1x
}
=
\frac{\abs{x_n-x}}{\abs{x_nx}}
\le
\frac{2}{\abs{x}^2}\abs{x_n-x}.
$$
The right side tends to $0$.

:::

:::

::: {.pf-step #s1-4}

Ordinary convergence to a point of $X$ is equivalent to convergence in $\rho$:
$$
\boxed{
\abs{x_n-x}\to0
\iff
\rho(x_n,x)\to0
}.
$$


::: pf-proof

The forward implication follows from step [](#s1-3){.pf-ref}:
$$
\rho(x_n,x)
=
\abs{x_n-x}
+
\abs{
\frac1{x_n}-\frac1x
}
\longrightarrow0.
$$
The reverse implication is step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Let $(x_n)$ be a $\rho$-Cauchy sequence.
Then both real sequences
$$
(x_n)
\qquad\text{and}\qquad
\left(\frac1{x_n}\right)
$$
are Cauchy in $\RR$.


::: pf-proof

For all $m,n$,
$$
\abs{x_n-x_m}
\le
\rho(x_n,x_m)
$$
and
$$
\abs{
\frac1{x_n}-\frac1{x_m}
}
\le
\rho(x_n,x_m).
$$
Thus the Cauchy property for $\rho$ implies the ordinary Cauchy property for each coordinate sequence.

:::

:::

::: {.pf-step #s1-6}

There exist real numbers $a,b$ such that
$$
x_n\to a
\qquad\text{and}\qquad
\frac1{x_n}\to b.
$$


::: pf-proof

The real line is complete, and both sequences are Cauchy by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

One has
$$
ab=1.
$$


::: pf-proof

For every $n$,
$$
x_n\cdot\frac1{x_n}=1.
$$
Multiplication is continuous, so using the limits from step [](#s1-6){.pf-ref} gives
$$
ab
=
\lim_{n\to\infty}
x_n\frac1{x_n}
=1.
$$

:::

:::

::: {.pf-step #s1-8}

In particular,
$$
a\ne0,
$$
so $a\in X$, and
$$
b=\frac1a.
$$


::: pf-proof

The identity
$$
ab=1
$$
from step [](#s1-7){.pf-ref} rules out $a=0$.
Solving for $b$ gives
$$
b=1/a.
$$

:::

:::

::: {.pf-step #s1-9}

The sequence $(x_n)$ converges to $a$ in the metric $\rho$.


::: pf-proof

By steps [](#s1-6){.pf-ref} and [](#s1-8){.pf-ref},
$$
\abs{x_n-a}\to0
$$
and
$$
\abs{
\frac1{x_n}-\frac1a
}
\to0.
$$
Therefore
$$
\rho(x_n,a)
=
\abs{x_n-a}
+
\abs{
\frac1{x_n}-\frac1a
}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{(X,\rho)\text{ is complete}}.
$$


::: pf-proof

Every $\rho$-Cauchy sequence converges in $\rho$ to a point $a\in X$ by steps [](#s1-5){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves that $\rho$ is a metric, step [](#s1-4){.pf-ref} proves that it induces the same sequential convergence as the usual metric on $X$, and step [](#s1-10){.pf-ref} proves completeness.

:::

:::

:::
