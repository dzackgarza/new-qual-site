---
schema: qual/card@1
id: P-BKF04-7A
kind: problem
title: A disk self-map with $f(-\frac12)=0$ and $f(0)=\frac12$ has $f(\frac12)=\frac45$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $D$ be the open unit disk in $\mathbb{C}$, and $f\colon D\to D$ a holomorphic function. Suppose that $f(-\frac12)=0$ and $f(0)=\frac12$. Prove that there is only one possible value for $f(\frac12)$, and find it.
:::

::: {.solution}
The linear fractional transformation

$$
g(z)=\frac{z+\frac12}{1+\frac z2}=\frac{2z+1}{2+z}
$$

is an automorphism of $D$ satisfying

$$
g(-\tfrac12)=0,\qquad g(0)=\tfrac12.
$$

Then the composition $h=f\circ g^{-1}$ satisfies

$$
h\colon D\to D,\qquad h(0)=0,\qquad h(\tfrac12)=\tfrac12.
$$

By Schwarz's lemma, $\abs{h(z)}\leq\abs z$ in $D$. Equality holds at $z=\frac12$, so $h(z)=\lambda z$ with $\abs\lambda=1$, and $h(\frac12)=\frac12$ gives $\lambda=1$. Hence $f=g$, and

$$
f(\tfrac12)=\boxed{\tfrac45}.
$$
:::
