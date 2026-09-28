---
schema: qual/card@1
id: P-BKF04-3A
kind: problem
title: A nonconstant entire $f$ composed with an essential singularity of $g$ gives an essential singularity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f$ and $g$ be functions that are holomorphic on all of $\mathbb{C}$, except that $g$ has an essential singularity at the complex number $c$. Prove that either $f$ is constant, or the composition $f\circ g$ has an essential singularity at $c$. (Hint: you may assume the Casorati-Weierstrass Theorem, which states that if a function $f$ has an essential singularity at $c$, then for any punctured neighborhood $N$ of $c$ on which $f$ is holomorphic, the image $f(N)$ is dense in $\mathbb{C}$.)
:::

::: {.solution}
Suppose that $f$ is not constant. Choose $a,b\in\CC$ such that $f(a)\neq f(b)$. If $N$ is any punctured neighborhood of $c$, then $g(N)$ is dense in $\CC$ by the Casorati--Weierstrass theorem. In particular, the closure of $g(N)$ contains $a$ and $b$, so, by continuity of $f$, the closure of $f(g(N))$ contains $f(a)$ and $f(b)$. Since this holds for every $N$, the limit $\lim_{z\to c}f(g(z))$ is not $\infty$, and it does not exist as a complex number either. Thus $f\circ g$ has neither a pole nor a removable singularity at $c$, so it has an essential singularity at $c$.
:::
