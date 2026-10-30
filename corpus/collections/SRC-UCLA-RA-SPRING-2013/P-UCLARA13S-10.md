---
schema: qual/card@1
id: P-UCLARA13S-10
kind: problem
title: A nonconstant entire function takes arbitrarily far positive real values
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $f:\CC\to\CC$ be a nonconstant entire function.
Without using either Picard theorem, show that there exist complex numbers $z$ of arbitrarily large modulus for which $f(z)$ is a positive real number.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, toward a contradiction, that there is $R_0>0$ such that
$$
\abs{z}>R_0
\quad\Longrightarrow\quad
f(z)\notin(0,\infty).
$$


::: pf-proof

This is exactly the negation of the assertion that points of arbitrarily large modulus are mapped to positive real numbers.

:::

:::

::: {.pf-step #s1-2}

Choose a positive real number $M$ such that
$$
M>
\max_{\abs{z}\le R_0}\abs{f(z)}
$$
and define
$$
g(z)=f(z)-M.
$$
Then
$$
g(\CC)
\subset
\CC\setminus[0,\infty).
$$


::: pf-proof

First suppose $\abs{z}\le R_0$. If
$$
g(z)\in[0,\infty),
$$
then
$$
f(z)=M+g(z)
$$
is a positive real number of modulus at least $M$, contradicting the choice of $M$.

Now suppose $\abs{z}>R_0$. If $g(z)\in[0,\infty)$, then
$$
f(z)=M+g(z)>0
$$
is a positive real number, contradicting step [](#s1-1){.pf-ref}. Thus $g$ avoids the entire nonnegative real axis.

:::

:::

::: {.pf-step #s1-3}

There is an injective holomorphic map
$$
\Phi:
\CC\setminus[0,\infty)
\longrightarrow
\DD.
$$


::: pf-proof

On the slit plane
$$
\CC\setminus[0,\infty),
$$
choose the branch of the argument in $(0,2\pi)$ and define
$$
S(w)=\sqrt w
=
\exp\left(\frac12(\log\abs{w}+i\operatorname{Arg}w)\right).
$$
Then
$$
0<\operatorname{Arg}S(w)<\pi,
$$
so $S$ maps the slit plane biholomorphically onto the upper half-plane.

The Cayley transform
$$
C(\zeta)
=
\frac{\zeta-i}{\zeta+i}
$$
maps the upper half-plane biholomorphically onto the unit disk. Thus
$$
\Phi=C\circ S
$$
is an injective holomorphic map into $\DD$.

:::

:::

::: pf-step

The entire function
$$
\Phi\circ g:\CC\to\DD
$$
is constant.


::: pf-proof

By step [](#s1-2){.pf-ref}, $g$ takes values in the domain of $\Phi$. Hence the composition is entire. Its image lies in the unit disk, so it is bounded. Liouville's theorem therefore makes it constant.

:::

:::

::: {.pf-step #s1-5}

The function $f$ is constant.


::: pf-proof

The map $\Phi$ is injective by step [](#s1-3){.pf-ref}. Thus constancy of
$$
\Phi\circ g
$$
implies constancy of $g$. Since
$$
f=g+M,
$$
the function $f$ is constant as well.

:::

:::

::: {.pf-step #s1-6}

The assumption in step [](#s1-1){.pf-ref} is impossible.


::: pf-proof

Step [](#s1-5){.pf-ref} contradicts the hypothesis that $f$ is nonconstant.

:::

:::

::: {.pf-step #s1-7}

Therefore, for every $R>0$, there exists $z\in\CC$ with
$$
\abs{z}>R
$$
such that
$$
\boxed{f(z)\in(0,\infty)}.
$$


::: pf-proof

If this failed for some $R$, step [](#s1-1){.pf-ref} would hold with $R_0=R$, contradicting step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required statement.

:::

:::

:::
