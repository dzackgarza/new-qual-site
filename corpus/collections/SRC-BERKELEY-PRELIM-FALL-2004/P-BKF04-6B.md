---
schema: qual/card@1
id: P-BKF04-6B
kind: problem
title: Averages of $f$ over the circle $|z|=1/n$ for $f$ with a pole at $0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that $f(z)$ is holomorphic on all of $\mathbb{C}$ except for a pole at $z=0$. Prove that

$$
\lim_{n\to\infty}\frac1n\sum_{k=1}^n f\left(\frac1ne^{2\pi ik/n}\right)
$$

exists.
:::

::: {.solution}
If $f$ were holomorphic at $0$, then each term in the sum would be $f(0)+O(1/n)$, where the implied constant is independent of $k$ and $n$, so the average of these values of $f$ would also be $f(0)+O(1/n)$, which tends to $f(0)$ as $n\to\infty$.

In general, the principal part of the Laurent series of $f$ at $0$ is finite, so $f$ is a finite linear combination of functions $z^{-m}$ with $m>0$ plus one entire function. By linearity, it remains to prove the statement for $f(z)=z^{-m}$. In this case the average equals $n^{m-1}\sum_{k=1}^n e^{-2\pi ikm/n}$, a finite geometric series whose value is $0$ when $n>m$.
:::
