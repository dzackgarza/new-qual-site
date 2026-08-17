---
schema: qual/card@1
id: P-3KOGW
kind: problem
title: Mean-square identity for power series, and Liouville's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - power-series
  - entire-functions
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
\envlist

- Assume $f(z)=\sum_{n=0}^{\infty} c_{n} z^{n}$ converges in $|z|<R$. Show that for $r<R$,

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi}\left|f\left(r e^{i \theta}\right)\right|^{2} d \theta=\sum_{n=0}^{\infty}\left|c_{n}\right|^{2} r^{2 n}
$$

- Deduce Liouville's theorem from (a).

:::

:::{.solution}
Computing the LHS:
\[
\int_{[0, 2\pi]} \abs{f(re^{i\theta})}^2 \dtheta
&= \int_{[0, 2\pi]} f(re^{i\theta}) \bar{f(re^{i\theta}) } \dtheta \\
&= \int_{[0, 2\pi]} \sum_{k\geq 0} c_k r^k e^{ik\theta} \sum_{j\geq 0} \bar{c_j} r^j e^{-ij\theta} \dtheta \\
&= \int_{[0, 2\pi]} \sum_{k,j\geq 0} c_k\bar{c_j} r^{k+j} e^{i(k-j)\theta} \dtheta \\
&= \sum_{k,j\geq 0} c_k\bar{c_j} r^{k+j} \int_{[0, 2\pi]} e^{i(k-j)\theta} \dtheta \\
&= \sum_{k,j\geq 0} c_k\bar{c_j} r^{k+j} \chi_{i=j}\cdot 2\pi \\
&= \sum_{k\geq 0} c_k\bar{c_k} r^{2k} \cdot 2\pi \\
&= 2\pi \sum_{k\geq 0}\abs{c_k}^2 r^{2k}
,\]
where we've used that the series converges uniformly in its radius of convergence to commute sums and integrals.

Now supposing $\abs{f(z)}\leq M$ for all $z\in \CC$, if $f$ is entire then $\sum_{k\geq 0} c_k z^k$ converges for all $r$, so
\[
\sum_{k\geq 0} \abs{c_k}^2 r^{2k} = {1\over 2\pi }\int_{[0, 2\pi]} \abs{f(re^{i\theta})}^2 \dtheta \leq {1\over 2\pi}\int_{[0, 2\pi]} M^2 \dtheta = M^2
.\]
Thus for all $r$,
\[
\abs{c_0}^2 + \abs{c_1}^2 r^2 + \abs{c_2}^2 r^{4} + \cdots \leq M^2
,\]
and taking $r\to\infty$ forces $\abs{c_1}^2 = \abs{c_2}^2 = \cdots = 0$.
So $f(z) = c_0$ is constant.



:::
