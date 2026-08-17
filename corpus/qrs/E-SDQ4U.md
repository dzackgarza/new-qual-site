---
schema: qual/card@1
id: E-SDQ4U
kind: exercise
title: $L^p$ inclusions on finite measure spaces and $\ell^p$ inclusions on $\mathbb{Z}$
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - l-infty
  - l1
relations: []
review: draft
solved: true
---

::: exercise
- Prove the following inclusions of $L^p$ spaces for $m(X) < \infty$:
\[
L^\infty(X) &\subset L^2(X) \subset L^1(X) \\
\ell^2(\ZZ) &\subset \ell^1(\ZZ) \subset \ell^\infty(\ZZ)
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Honesty note:** the second line of the display has the inclusions backwards as written: $\ell^2(\ZZ) \not\subset \ell^1(\ZZ)$ (e.g. $a_n = 1/n$ is in $\ell^2$ but not $\ell^1$). The true inclusions for counting measure on $\ZZ$ are $\ell^1 \subset \ell^2 \subset \ell^\infty$. The solution proves the correct statements.

<1>1. For $m(X) < \infty$: $L^\infty(X) \subseteq L^2(X) \subseteq L^1(X)$.
    <2>1. $L^2 \subseteq L^1$: $\|f\|_1 \le m(X)^{1/2}\|f\|_2$ for $f \in L^2$.
        Proof: Cauchy–Schwarz, $\int|f| = \int |f|\cdot 1 \le \|f\|_2\|1\|_2 = \|f\|_2 m(X)^{1/2}$.
    <2>2. $L^\infty \subseteq L^2$: $\|f\|_2 \le m(X)^{1/2}\|f\|_\infty$ for $f \in L^\infty$.
        Proof: $\int|f|^2 \le \|f\|_\infty^2 m(X)$.
    <2>3. The inclusions are strict in general.
        Proof: on $[0,1]$ with Lebesgue measure, $x^{-1/3} \in L^1 \setminus L^2$ and $\log x \in L^2 \setminus L^\infty$ (up to modification; $\log x$ is square-integrable on $[0,1]$ and unbounded).
    <2>4. Q.E.D.
        Proof: <2>1 and <2>2.

<1>2. For counting measure on $\ZZ$: $\ell^1(\ZZ) \subseteq \ell^2(\ZZ) \subseteq \ell^\infty(\ZZ)$.
    <2>1. $\ell^1 \subseteq \ell^2$: if $\sum_n |a_n| < \infty$ then $\sum_n |a_n|^2 < \infty$.
        Proof: the terms of a convergent series tend to $0$, so $|a_n| \le 1$ eventually, where $|a_n|^2 \le |a_n|$; hence $\sum |a_n|^2 \le \sum |a_n| < \infty$.
    <2>2. $\ell^2 \subseteq \ell^\infty$: if $\sum_n |a_n|^2 < \infty$ then $\sup_n |a_n| < \infty$.
        Proof: $|a_n|^2 \le \sum_k |a_k|^2$ for every $n$, so $|a_n| \le \|a\|_2$.
    <2>3. The inclusions are strict: $a_n = 1/n \in \ell^2 \setminus \ell^1$ and $a_n = 1/\sqrt n \in \ell^\infty \setminus \ell^2$.
        Proof: $\sum 1/n$ diverges while $\sum 1/n^2$ converges; $\sup_n n^{-1/2} = 1 < \infty$ while $\sum 1/n$ diverges.
    <2>4. Q.E.D.
        Proof: <2>1–<2>3.

<1>3. Q.E.D.
    Proof: <1>1 proves the first line of the display; <1>2 proves the corrected second line.
:::
