---
schema: qual/card@1
id: T-NRT7K
kind: theorem
title: $n$th roots of a complex number
slogan: 'A nonzero complex number has exactly $n$ distinct $n$th roots, equally spaced on a circle.'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Numbers
  - Roots of Unity
relations: []
review: draft
---

::: {.theorem}
Let $n\geq1$ and let $z=re^{i\theta}\neq0$ with $r>0$.
The solutions of $w^n=z$ are
$$
w_k=r^{1/n}e^{i(\theta+2k\pi)/n},\qquad 0\leq k\leq n-1,
$$
and there are exactly $n$ of them: each has modulus $r^{1/n}$, and consecutive ones differ in argument by $2\pi/n$.

This is [@Ahl73, ch. 1, §2.2, The Binomial Equation], which solves $z^n=a$ by writing $a=r(\cos\varphi+i\sin\varphi)$ and obtains the $n$ roots in this form; de Moivre's formula of that section,
$(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$, is the computation that produces them.
:::
