---
schema: qual/card@1
id: P-UGASAMP-01
kind: problem
title: Inverse functions and the inverse of $(x+2)/(3x-1)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Define what is meant by an inverse function, and give necessary and sufficient conditions for an inverse function to exist. Find the inverse of
\[
f(x)=\frac{x+2}{3x-1},
\qquad x\in\RR,\quad x\ne\frac13.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A function \(f:X\to Y\) has an inverse if there is a function \(g:Y\to X\) such that
\[
g\circ f=\operatorname{id}_X
\qquad\text{and}\qquad
f\circ g=\operatorname{id}_Y.
\]
Such a function \(g\) is unique and is denoted \(f^{-1}\).


::: pf-proof

If \(g\) and \(h\) are both inverses of \(f\), then
\[
g=g\circ\operatorname{id}_Y
=g\circ(f\circ h)
=(g\circ f)\circ h
=\operatorname{id}_X\circ h
=h.
\]
Thus an inverse, if it exists, is unique.

:::

:::

::: {.pf-step #s1-2}

A function \(f:X\to Y\) has an inverse if and only if it is bijective.


::: pf-proof

If \(g\) is an inverse of \(f\), then \(f\) is injective: if \(f(x_1)=f(x_2)\), applying \(g\) gives
\[
x_1=g(f(x_1))=g(f(x_2))=x_2.
\]
It is surjective because for each \(y\in Y\),
\[
y=f(g(y)).
\]

Conversely, suppose \(f\) is bijective. For each \(y\in Y\), surjectivity gives an \(x\in X\) with \(f(x)=y\), and injectivity makes this \(x\) unique. Define \(g(y)\) to be that unique \(x\). Then \(g(f(x))=x\) for every \(x\in X\) and \(f(g(y))=y\) for every \(y\in Y\), so \(g=f^{-1}\).

:::

:::

::: {.pf-step #s1-3}

For
\[
f(x)=\frac{x+2}{3x-1},
\qquad
x\ne\frac13,
\]
the image is contained in \(\RR\setminus\{\frac13\}\).


::: pf-proof

If \(f(x)=\frac13\), then
\[
3(x+2)=3x-1,
\]
which simplifies to \(6=-1\), a contradiction. Hence \(f(x)\ne\frac13\) for every \(x\) in the domain.

:::

:::

::: {.pf-step #s1-4}

Solving \(y=f(x)\) for \(x\) gives
\[
x=\frac{y+2}{3y-1}.
\]


::: pf-proof

Starting from
\[
y=\frac{x+2}{3x-1},
\]
cross-multiplication gives
\[
3xy-y=x+2.
\]
Thus
\[
x(3y-1)=y+2.
\]
By step [](#s1-3){.pf-ref}, \(y\ne\frac13\), so \(3y-1\ne0\), and division yields
\[
x=\frac{y+2}{3y-1}.
\]

:::

:::

::: {.pf-step #s1-5}

The function
\[
f:\RR\setminus\left\{\frac13\right\}
\longrightarrow
\RR\setminus\left\{\frac13\right\}
\]
is bijective and
\[
\boxed{f^{-1}(x)=\frac{x+2}{3x-1}.}
\]


::: pf-proof

Define
\[
g(y)=\frac{y+2}{3y-1}
\]
on \(\RR\setminus\{\frac13\}\). Step [](#s1-4){.pf-ref} shows that \(g(y)\) is exactly the unique solution of \(f(x)=y\). Therefore
\[
f(g(y))=y
\qquad\text{and}\qquad
g(f(x))=x,
\]
so \(g=f^{-1}\). In particular, \(f\) is bijective by step [](#s1-2){.pf-ref}. The formula for \(g\) is the same as the formula for \(f\), so \(f\) is an involution.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the definition and necessary-and-sufficient condition for an inverse function to exist, and step [](#s1-5){.pf-ref} computes the inverse of the given function.

:::

:::

:::
