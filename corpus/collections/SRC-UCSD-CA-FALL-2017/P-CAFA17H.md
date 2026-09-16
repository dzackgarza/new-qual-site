---
schema: qual/card@1
id: P-CAFA17H
kind: problem
title: "A harmonic function with polynomial growth on R is a polynomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Let $n \geq 1$ be an integer.
Let $u: \mathbb{C} \to \mathbb{R}$ be a harmonic function such that $|u(z)| \leq C(1 + |z|^n)$ for all $z \in \mathbb{C}$.
Show that $u$ is a polynomial.
:::

::: {.remark}
The official Fall 2017 exam states the growth bound for all points of $\mathbb C$. The previous card transcription incorrectly restricted it to the real axis; that weaker statement is false, for example for $u(z)=\operatorname{Im}(e^z)$.
:::

::: {.solution}
Because $\mathbb C$ is simply connected, $u$ has a global harmonic conjugate $v$. Thus
\[
F=u+iv
\]
is entire.

Fix $R>1$. By the Borel--Carathéodory inequality applied on $|z|<2R$,
\[
\max_{|z|\le R}|F(z)-F(0)|
\le C_1\max_{|z|\le2R}|\operatorname{Re}(F(z)-F(0))|
\le C_2(1+R^n).
\]
Hence, after enlarging the constant,
\[
\max_{|z|\le R}|F(z)|\le C_3(1+R^n).
\]

Cauchy's estimate gives, for every integer $m>n$,
\[
|F^{(m)}(0)|
\le \frac{m!}{R^m}\max_{|z|=R}|F(z)|
\le m!C_3\frac{1+R^n}{R^m}.
\]
Letting $R\to\infty$ yields $F^{(m)}(0)=0$ for all $m>n$. Therefore $F$ is a polynomial of degree at most $n$, and so its real part $u$ is a harmonic polynomial.
:::
