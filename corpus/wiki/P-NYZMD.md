---
schema: qual/card@1
id: P-NYZMD
kind: problem
title: "Consider $L^2([0, 1])$ and define"
classification:
  areas:
  - real-analysis
  topics:
  - hilbert-spaces
  - l2
  - polynomials
relations: []
review: draft
---

::: problem
Consider $L^2([0, 1])$ and define
\[
e_0(x) &= 1 \\
e_1(x) &= \sqrt{3}(2x-1)
.\]

a. Show that $\ts{e_0, e_1}$ is an orthonormal system.

b. Show that the polynomial $p(x)$ where $\deg(p) = 1$ which is closest to $f(x) = x^2$ in $L^2([0, 1])$ is given by
\[
h(x) = x - {1\over 6}
.\]

Compute $\norm{f - g}_2$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (a) $\{e_0, e_1\}$ with $e_0 \equiv 1$, $e_1(x) = \sqrt 3(2x - 1)$ is orthonormal in $L^2([0,1])$.
    <2>1. $\|e_0\|_2^2 = \int_0^1 1\,dx = 1$.
        Proof: direct.
    <2>2. $\|e_1\|_2^2 = 3\int_0^1 (2x - 1)^2\,dx = 3\int_0^1(4x^2 - 4x + 1)\,dx = 3\left(\frac43 - 2 + 1\right) = 3\cdot\frac13 = 1$.
        Proof: polynomial integration.
    <2>3. $\inner{e_0}{e_1} = \int_0^1 \sqrt 3(2x-1)\,dx = \sqrt 3(1 - 1) = 0$.
        Proof: $\int_0^1 2x\,dx - \int_0^1 1\,dx = 1 - 1 = 0$.

<1>2. (b) The closest degree-$\le 1$ polynomial to $f(x) = x^2$ is the orthogonal projection onto $\span\{e_0, e_1\}$: $h = \inner{f}{e_0}e_0 + \inner{f}{e_1}e_1$.
    <2>1. $\inner{f}{e_0} = \int_0^1 x^2\,dx = \frac13$.
        Proof: direct.
    <2>2. $\inner{f}{e_1} = \sqrt 3\int_0^1 x^2(2x - 1)\,dx = \sqrt 3\left(\frac12 - \frac13\right) = \frac{\sqrt 3}{6}$.
        Proof: $\int_0^1 2x^3\,dx - \int_0^1 x^2\,dx = \frac12 - \frac13 = \frac16$.
    <2>3. $h(x) = \frac13 + \frac{\sqrt 3}{6}\cdot\sqrt 3(2x - 1) = \frac13 + \frac12(2x - 1) = x - \frac16$.
        Proof: substitute the coefficients into $h = \frac13 e_0 + \frac{\sqrt3}{6}e_1$.

<1>3. (c) $\|f - h\|_2 = \frac{1}{6\sqrt 5}$.
    <2>1. $\|f - h\|_2^2 = \|f\|_2^2 - \|h\|_2^2$ (Pythagoras, since $f - h \perp \span\{e_0, e_1\} \ni h$).
        Proof: orthogonal decomposition; $h$ is the projection of $f$.
    <2>2. $\|f\|_2^2 = \int_0^1 x^4\,dx = \frac15$.
        Proof: direct.
    <2>3. $\|h\|_2^2 = \inner{f}{e_0}^2 + \inner{f}{e_1}^2 = \frac19 + \frac{3}{36} = \frac19 + \frac1{12} = \frac{7}{36}$.
        Proof: Parseval for the orthonormal pair; $\frac19 = \frac4{36}$, so $\frac4{36} + \frac3{36} = \frac7{36}$.
    <2>4. $\|f - h\|_2^2 = \frac15 - \frac7{36} = \frac{36 - 35}{180} = \frac1{180}$, so $\|f - h\|_2 = \frac1{6\sqrt5}$.
        Proof: $\sqrt{180} = 6\sqrt 5$.

<1>4. Q.E.D.
    Proof: <1>1, <1>2, <1>3 settle (a), (b), and the norm computation.
:::
