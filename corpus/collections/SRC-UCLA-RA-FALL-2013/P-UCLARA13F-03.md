---
schema: qual/card@1
id: P-UCLARA13F-03
kind: problem
title: No holomorphic function blows up along every approach to the disk boundary
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Does there exist a holomorphic function $f:\DD\to\CC$ such that
$$
\abs{f(z_n)}\longrightarrow\infty
$$
for every sequence $(z_n)\subset\DD$ with $\abs{z_n}\to1$?
Justify your answer.
:::

::: {.solution}

No such holomorphic function exists.

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that $f:\DD\to\CC$ is holomorphic and satisfies the stated property.


::: pf-proof

This assumes the negation of the desired answer.

:::

:::

::: {.pf-step #s1-2}

The stated sequential property implies that for every $M>0$ there exists $0<r<1$ such that
$$
\abs{z}>r
\quad\Longrightarrow\quad
\abs{f(z)}>M.
$$


::: pf-proof

If this failed for some $M>0$, then for every integer $n$ one could choose $z_n\in\DD$ with
$$
\abs{z_n}>1-1/n
\qquad\text{and}\qquad
\abs{f(z_n)}\leq M.
$$
Then $\abs{z_n}\to1$ but $\abs{f(z_n)}$ would not tend to infinity, contradicting the hypothesis.

:::

:::

::: {.pf-step #s1-3}

Taking $M=1$, there exists $r<1$ such that $f$ has no zeros in the annulus
$$
r<\abs{z}<1.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $\abs{f(z)}>1$ throughout this annulus, so $f(z)\ne0$ there.

:::

:::

::: pf-step

The zeros of $f$ in the closed disk $\{\abs{z}\leq r\}$ are finite in number, counted without multiplicity.


::: pf-proof

The zero set of a nonzero holomorphic function is discrete. The function is not identically zero because step [](#s1-3){.pf-ref} gives $\abs{f}>1$ near the boundary. A discrete subset of the compact disk $\{\abs{z}\leq r\}$ is finite.

:::

:::

::: {.pf-step #s1-5}

Let $a_1,\ldots,a_s$ be these zeros, repeated according to multiplicity, and define
$$
p(z)=\prod_{j=1}^s(z-a_j),
\qquad
g(z)=\frac{p(z)}{f(z)}.
$$
Then $g$ extends to a holomorphic function on all of $\DD$.


::: pf-proof

By step [](#s1-3){.pf-ref} there are no zeros outside the compact disk, so $a_1,\ldots,a_s$ list every zero of $f$ in $\DD$. At each zero, $p$ has exactly the same multiplicity as $f$, so the apparent singularity of $p/f$ is removable. Removing all of them yields a holomorphic function on $\DD$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
g(z)\longrightarrow0
\qquad\text{whenever }\abs{z}\to1.
$$


::: pf-proof

The polynomial $p$ is bounded on the unit disk: there is $C<\infty$ with $\abs{p(z)}\leq C$ for $\abs{z}<1$. By the assumed property, $\abs{f(z)}\to\infty$ uniformly toward the boundary in the sense of step [](#s1-2){.pf-ref}. Hence
$$
\abs{g(z)}=\frac{\abs{p(z)}}{\abs{f(z)}}\leq\frac C{\abs{f(z)}}\to0.
$$

:::

:::

::: {.pf-step #s1-7}

For every $0<\rho<1$, the maximum modulus principle gives
$$
\max_{\abs{z}\leq\rho}\abs{g(z)}
=\max_{\abs{z}=\rho}\abs{g(z)}.
$$


::: pf-proof

The function $g$ is holomorphic on the unit disk by step [](#s1-5){.pf-ref}, hence on a neighborhood of the closed disk of radius $\rho$. The maximum modulus principle applies.

:::

:::

::: {.pf-step #s1-8}

Letting $\rho\uparrow1$ in step [](#s1-7){.pf-ref} and using step [](#s1-6){.pf-ref} gives
$$
g\equiv0.
$$


::: pf-proof

Fix $z\in\DD$. For every $\rho$ with $\abs{z}<\rho<1$,
$$
\abs{g(z)}\leq\max_{\abs{w}=\rho}\abs{g(w)}.
$$
Step [](#s1-6){.pf-ref}, in its uniform form from step [](#s1-2){.pf-ref}, says the right side tends to zero as $\rho\uparrow1$. Thus $g(z)=0$. Since $z$ was arbitrary, $g\equiv0$.

:::

:::

::: {.pf-step #s1-9}

This is impossible because $p$ is a nonzero polynomial and $g=p/f$ away from the zeros of $f$.


::: pf-proof

Choose a point $z$ that is not one of the finitely many zeros $a_j$. Then $p(z)\ne0$ and $f(z)\ne0$, so
$$
g(z)=p(z)/f(z)\ne0,
$$
contradicting step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{\text{no such holomorphic function exists}.}
$$


::: pf-proof

The existence assumption in step [](#s1-1){.pf-ref} led to the contradiction in step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} answers the question and proves the assertion.

:::

:::

:::
