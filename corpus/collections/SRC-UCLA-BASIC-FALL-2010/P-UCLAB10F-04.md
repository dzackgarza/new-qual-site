---
schema: qual/card@1
id: P-UCLAB10F-04
kind: problem
title: Approximation by finite sums of separated functions
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
(a) Let $f$ be a real-valued continuous function on $[0,1]\times[0,1]$ and let $\varepsilon>0$.
Show that there exist real-valued continuous functions $g_1,\ldots,g_n$ and $h_1,\ldots,h_n$ on $[0,1]$, for some finite $n\ge1$, such that
\[
\left|f(x,y)-\sum_{i=1}^n g_i(x)h_i(y)\right|\le\varepsilon,
\qquad 0\le x,y\le1.
\]

(b) If $f(x,y)=f(y,x)$ for all $0\le x,y\le1$, can this be done with $h_i=g_i$ for every $i$?
Explain.
:::

::: {.solution}

Let
\[
K=[0,1]^2.
\]

::: pf

::: {.pf-step #s1-1}

The algebra of real polynomials in the coordinate functions $x$ and $y$ is uniformly dense in $C(K)$.


::: pf-proof

Apply the real Stone--Weierstrass theorem. The restrictions to $K$ of real polynomials in $x$ and $y$ form a subalgebra
\[
\mathcal A\subseteq C(K).
\]
It contains the constants. It separates points: if
\[
(x_1,y_1)\ne(x_2,y_2),
\]
then either $x_1\ne x_2$, in which case the coordinate function $(x,y)\mapsto x$ separates them, or $y_1\ne y_2$, in which case $(x,y)\mapsto y$ does. Since $K$ is compact Hausdorff, Stone--Weierstrass implies that $\mathcal A$ is uniformly dense in $C(K)$.

:::

:::

::: {.pf-step #s1-2}

Given $\varepsilon>0$, there is a polynomial
\[
P(x,y)=\sum_{(r,s)\in F}c_{rs}x^ry^s
\]
with $F\subseteq\NN^2$ finite such that
\[
\|f-P\|_\infty\le\varepsilon.
\]


::: pf-proof

This follows directly from the uniform density in step [](#s1-1){.pf-ref}. If the theorem gives strict inequality $<\varepsilon$, then the displayed weak inequality follows as well.

:::

:::

::: {.pf-step #s1-3}

The polynomial $P$ from step [](#s1-2){.pf-ref} can be written as a finite sum
\[
P(x,y)=\sum_{i=1}^n g_i(x)h_i(y)
\]
with continuous real-valued functions $g_i,h_i$ on $[0,1]$.


::: pf-proof

Enumerate the finitely many pairs in $F$ as
\[
(r_1,s_1),\ldots,(r_n,s_n).
\]
Define
\[
g_i(x)=c_{r_is_i}x^{r_i},
\qquad
h_i(y)=y^{s_i}.
\]
These are polynomials, hence continuous, and
\[
\sum_{i=1}^n g_i(x)h_i(y)
=
\sum_{(r,s)\in F}c_{rs}x^ry^s
=
P(x,y).
\]

:::

:::

::: {.pf-step #s1-4}

Therefore for every continuous $f$ and every $\varepsilon>0$ there are finitely many continuous $g_i,h_i$ such that
\[
\boxed{
\left|
f(x,y)-\sum_{i=1}^n g_i(x)h_i(y)
\right|
\le\varepsilon
}
\]
for every $(x,y)\in[0,1]^2$.


::: pf-proof

Combine steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Even when $f$ is symmetric, one cannot in general require
\[
h_i=g_i
\]
for every $i$.


::: pf-proof

Take the symmetric continuous function
\[
f(x,y)=-1.
\]
Suppose an approximation of the required special form existed with error less than $1$, say
\[
\left|
-1-\sum_{i=1}^n g_i(x)g_i(y)
\right|<1
\]
for all $x,y\in[0,1]$.
Setting $y=x$ gives
\[
\left|
-1-\sum_{i=1}^n g_i(x)^2
\right|<1.
\]
But
\[
\sum_{i=1}^n g_i(x)^2\ge0,
\]
so
\[
-1-\sum_{i=1}^n g_i(x)^2\le-1
\]
and therefore
\[
\left|
-1-\sum_{i=1}^n g_i(x)^2
\right|\ge1,
\]
a contradiction.
Thus for $\varepsilon<1$, the symmetric function $f\equiv-1$ cannot be approximated in the requested form.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} gives a symmetric counterexample for part (b).

:::

:::

:::
