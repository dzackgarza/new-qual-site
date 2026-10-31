---
schema: qual/card@1
id: E-SS8.PR-8
kind: problem
title: Bieberbach bound for real Taylor coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Univalent Functions
relations: []
review: draft
---

::: {.exercise}
Let $f$ be injective and holomorphic on the unit disc, with $f(0)=0$ and $f'(0)=1$. Write $f(z)=z+a_2z^2+a_3z^3+\cdots$. This problem proves $\abs{a_n}\leq n$ under the additional assumption that every $a_n$ is real.

(a) For $z=re^{i\theta}$ with $0<r<1$, let $v(r,\theta)=\Im f(re^{i\theta})$. Show that
$$
a_nr^n=\frac2\pi\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta.
$$

(b) Show that $\abs{\sin(n\theta)}\leq n\sin\theta$ for $0\leq\theta\leq\pi$ and $n\geq1$.

(c) Use $a_n\in\RR$ to show that $f(\DD)$ is symmetric about the real axis and that $f$ maps the upper half-disc into either the upper or lower part of $f(\DD)$.

(d) Show that $v(r,\theta)=r\sin\theta[1+O(r)]$ for small $r$. Deduce that $v(r,\theta)\sin\theta\geq0$ for all $0<r<1$ and $0\leq\theta\leq\pi$.

(e) Prove that $\abs{a_nr^n}\leq nr$, then let $r\to1$.

(f) Check that $f(z)=z/(1-z)^2$ meets the hypotheses and has $a_n=n$ for every $n$.
:::
