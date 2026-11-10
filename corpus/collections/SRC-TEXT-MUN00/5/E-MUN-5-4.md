---
schema: qual/card@1
id: E-MUN-5-4
kind: problem
title: Bijections between finite and countable product spaces
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 4; restored part (f) to the printed map X^A -> X^B for A subset B.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (f) did not say what the retained printing says. Munkres, Topology (2000), §5
    Exercise 4(f), printed p. 39, reads "If A is a subset of B, find an injective map
    m : (A^omega)^n -> B^omega", read on the page image as well as in the text layer.
    The card stated instead "m : X^A -> X^B", and its earlier note called that the
    printed map. Dan Whitman's manual (printed p. 71) records why both readings exist:
    the older printings say X^A -> X^B, which the text never defines, and the printing
    retained here was changed. The statement now follows the retained printing; the
    older reading is recorded here rather than silently dropped.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.4,
    printed pp. 71-73 (tmp/sources/munkres-solutions-whitman.pdf). Parts (a)-(e) are his.
    Part (f) now proves the map the retained printing asks for: interleave the n
    sequences x_1, ..., x_n by the bijection k = (j-1)n + i between Z_+ and
    Z_+ x {1, ..., n}; injectivity is that bijection's uniqueness. The previous proof of
    the X^A -> X^B reading, which padded with a chosen point, is superseded.
---

::: {.exercise}

Let $m, n \in \ZZ_{+}$ . Let $X \neq \varnothing$ .

(a) If $m \leq n$, find an injective map $f: X^m \to X^n$ .

(b) Find a bijective map $g: X^m \times X^n \to X^{m+n}$ .

(c) Find an injective map $h: X^n \to X^\omega$ .

(d) Find a bijective map $k: X^n \times X^\omega \to X^\omega$ .

(e) Find a bijective map $l: X^{\omega} \times X^{\omega} \to X^{\omega}$ .

(f) If $A \subset B$, find an injective map $m: (A^{\omega})^{n} \to B^{\omega}$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.4, printed pp. 71--73** (`tmp/sources/munkres-solutions-whitman.pdf`); the six constructions below are his, part (f) being the interleaving he writes with the division algorithm.

Choose once and for all a point $x_0\in X$.

(a) If $m\le n$, define
$$
f(x_1,\dots,x_m)
=(x_1,\dots,x_m,\underbrace{x_0,\dots,x_0}_{n-m}).
$$
The first $m$ coordinates recover the input, so $f$ is injective.

(b) Concatenation gives a bijection
$$
g:X^m\times X^n\longrightarrow X^{m+n},
$$
$$
g((x_1,\dots,x_m),(y_1,\dots,y_n))
=(x_1,\dots,x_m,y_1,\dots,y_n).
$$
Its inverse splits an $(m+n)$-tuple after the $m$-th coordinate.

(c) Define
$$
h(x_1,\dots,x_n)
=(x_1,\dots,x_n,x_0,x_0,\dots).
$$
Again the first $n$ coordinates recover the input, so $h$ is injective.

(d) Define
$$
k((x_1,\dots,x_n),(y_1,y_2,\dots))
=(x_1,\dots,x_n,y_1,y_2,\dots).
$$
The inverse separates the first $n$ coordinates from the infinite tail, so $k$ is bijective.

(e) Interleave coordinates:
$$
l((x_1,x_2,\dots),(y_1,y_2,\dots))
=(x_1,y_1,x_2,y_2,\dots).
$$
Taking odd and even coordinates gives the inverse, hence $l$ is bijective.

(f) Let $A\subset B$. Given
$$
x=(x_1,\dots,x_n)\in (A^{\omega})^{n},
$$
with each $x_i=(x_i(1),x_i(2),\dots)$ a sequence in $A$, define $m(x)=y\in B^{\omega}$ by
$$
y_k=x_i(j),
\qquad\text{where } k=(j-1)n+i,\quad i\in\{1,\dots,n\},\ j\in\ZZ_+ .
$$
Every $k\in\ZZ_+$ has exactly one such expression, because division of $k-1$ by $n$ gives a unique quotient $j-1$ and remainder $i-1$ with $0\le i-1<n$; and $y_k\in A\subset B$, so $y\in B^{\omega}$. If $x\ne x'$, then $x_i\ne x'_i$ for some $i$, hence $x_i(j)\ne x'_i(j)$ for some $j$, and at $k=(j-1)n+i$ the two images differ. Thus
$$
m:(A^{\omega})^{n}\hookrightarrow B^{\omega}
$$
is injective.
:::
