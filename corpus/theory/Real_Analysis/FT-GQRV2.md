---
schema: qual/card@1
id: FT-GQRV2
kind: theorem
title: Inclusions among $L^p$ spaces
prompts:
- How do the $L^p$ spaces include into one another when $m(X) < \infty$, and when $m(X) = \infty$?
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $1\le p< q\le\infty$.

1. If $(X,\mcm,\mu)$ is a [[D-QYLPH|measure]] space with $\mu(X)<\infty$, then $L^q(X)\subseteq L^p(X)$, and $\norm{f}_p\le\mu(X)^{\frac1p-\frac1q}\norm{f}_q$ for $f\in L^q(X)$, with $\frac1\infty\coloneqq0$.
In particular $L^\infty(X) \subseteq L^2(X) \subseteq L^1(X)$.

2. For counting measure on $\ZZ$, $\ell^p(\ZZ)\subseteq\ell^q(\ZZ)$, and $\norm{a}_q\le\norm{a}_p$ for $a\in\ell^p(\ZZ)$.
In particular $\ell^1(\ZZ) \subseteq \ell^2(\ZZ) \subseteq \ell^\infty(\ZZ)$.

3. For Lebesgue measure on $\RR^n$, neither $L^p(\RR^n)\subseteq L^q(\RR^n)$ nor $L^q(\RR^n)\subseteq L^p(\RR^n)$ holds.
:::

::: {.proof}
(1) For $q=\infty$, $\int_X\abs{f}^p\le\mu(X)\norm{f}_\infty^p$.
For $q<\infty$, apply Hölder's inequality with exponents $r=q/p$ and $r'=q/(q-p)$ to $\abs{f}^p\cdot1$:
$$
\int_X\abs{f}^p\dmu\le\qty{\int_X\abs{f}^q\dmu}^{p/q}\mu(X)^{1-p/q},
$$
and take $p$-th roots.

(2) If $\norm{a}_p=1$, then $\abs{a_k}\le1$ for all $k$, so $\norm{a}_\infty\le1$ and, for $q<\infty$, $\sum_k\abs{a_k}^q\le\sum_k\abs{a_k}^p=1$.
The general case follows by scaling $a$ by $1/\norm{a}_p$.

(3) Let $f_a(x)\coloneqq\abs{x}^{-a}\one_{\abs{x}\le1}$ and $g_a(x)\coloneqq\abs{x}^{-a}\one_{\abs{x}>1}$.
In polar coordinates, $f_a\in L^r(\RR^n)$ if and only if $ar<n$ (for $r<\infty$), and $g_a\in L^r(\RR^n)$ if and only if $ar>n$.
If $q<\infty$, choose $a$ with $n/q\le a<n/p$: then $f_a\in L^p\setminus L^q$, and choosing $a$ with $n/q<a\le n/p$ gives $g_a\in L^q\setminus L^p$.
If $q=\infty$, then $f_a\in L^p\setminus L^\infty$ for $0<a<n/p$, and the constant function $1$ lies in $L^\infty\setminus L^p$.
:::
