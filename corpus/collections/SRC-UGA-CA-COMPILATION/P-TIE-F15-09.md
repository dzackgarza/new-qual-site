---
schema: qual/card@1
id: P-TIE-F15-09
kind: problem
title: Accumulating zeros force an essential singularity
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 9.
---

::: {.problem}
Let $f(z)$ be a non-constant analytic function in $\abs{z} > 0$ such that $f(z_{n}) = 0$ for infinitely many points $z_{n}$ with $\lim_{n \to \infty} z_{n} = 0$. Show that $z = 0$ is an essential singularity for $f(z)$. (An example of such a function is $f(z) = \sin(1/z)$.)
:::

::: {.solution}

The point $0$ is an isolated singularity of $f$, so it is removable, a pole, or essential.

::: pf

::: {.pf-step #s1-1}

The singularity at $0$ is not removable.


::: pf-proof

Suppose that $0$ were removable. Then $f$ would extend to a holomorphic function
$$
\widetilde f:\CC\to\CC.
$$
For every $n$,
$$
\widetilde f(z_n)=f(z_n)=0,
$$
and $z_n\to0$. Thus the zeros of $\widetilde f$ have an accumulation point in its domain. By the identity theorem,
$$
\widetilde f\equiv0.
$$
Hence $f\equiv0$ on $\CC\setminus\{0\}$, contradicting the hypothesis that $f$ is nonconstant.

:::

:::

::: {.pf-step #s1-2}

The singularity at $0$ is not a pole.


::: pf-proof

Suppose that $0$ were a pole of order $m\ge1$. Then
$$
g(z)\coloneqq z^m f(z)
$$
extends holomorphically to a neighborhood of $0$ and satisfies
$$
g(0)\ne0.
$$
For every sufficiently large $n$, one has $z_n\ne0$, and therefore
$$
g(z_n)
=
z_n^m f(z_n)
=0.
$$
Since $z_n\to0$ and $g$ is continuous at $0$,
$$
g(0)
=
\lim_{n\to\infty}g(z_n)
=0,
$$
contradicting $g(0)\ne0$.

:::

:::

::: {.pf-step #s1-3}

Therefore $0$ is an essential singularity of $f$.


::: pf-proof

An isolated singularity is exactly one of removable, pole, or essential. Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} exclude the first two possibilities. Hence
$$
\boxed{0\text{ is an essential singularity of }f.}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
