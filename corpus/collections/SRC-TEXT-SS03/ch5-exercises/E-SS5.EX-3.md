---
schema: qual/card@1
id: E-SS5.EX-3
kind: problem
title: "SS 5.3: The Jacobi theta function has order 2"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 5 growth-order convention.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
3. Show that if $\tau$ is fixed with Im $( \tau ) > 0$ , then the Jacobi theta function

$$
\Theta (z | \tau) = \sum_ {n = - \infty} ^ {\infty} e ^ {\pi i n ^ {2} \tau} e ^ {2 \pi i n z}
$$

is of order 2 as a function of $z .$ . Further properties of $\Theta$ will be studied in Chapter 10.

[Hint: $- n ^ { 2 } t + 2 n | z | \leq - n ^ { 2 } t / 2$ when $t > 0$ and $n \geq 4 | z | / t . ]$
:::

::: {.solution}
Write
\[
\tau=u+it,
\qquad t=\Im\tau>0.
\]
For $z=x+iy$, the $n$th summand satisfies
\[
\left|e^{\pi i n^2\tau}e^{2\pi inz}\right|
=e^{-\pi t n^2-2\pi ny}
\le e^{-\pi t n^2+2\pi|n||y|}.
\]
Using
\[
2|n||y|\le \frac t2 n^2+\frac{2}{t}y^2,
\]
we obtain
\[
-\pi t n^2+2\pi|n||y|
\le -\frac{\pi t}{2}n^2+\frac{2\pi}{t}y^2.
\]
Hence
\[
|\Theta(z\mid\tau)|
\le e^{2\pi y^2/t}
\sum_{n\in\mathbb Z}e^{-\pi t n^2/2}
\le C_t e^{(2\pi/t)|z|^2}.
\]
Thus the order is at most $2$.

To prove that it is not smaller, first note the quasi-periodicity. Reindexing the absolutely convergent series gives
\[
\Theta(z+\tau\mid\tau)
=e^{-\pi i\tau-2\pi iz}\Theta(z\mid\tau),
\]
and therefore, for every integer $m\ge1$,
\[
\Theta(z+m\tau\mid\tau)
=e^{-\pi i m^2\tau-2\pi i m z}\Theta(z\mid\tau).
\tag{1}
\]
The theta function is not identically zero: on the real interval $[0,1]$ termwise integration gives
\[
\int_0^1\Theta(x\mid\tau)\,dx=1,
\]
since all Fourier modes except $n=0$ integrate to zero. Choose $z_0$ with $\Theta(z_0\mid\tau)\ne0$.

Taking absolute values in (1),
\[
|\Theta(z_0+m\tau\mid\tau)|
=|\Theta(z_0\mid\tau)|
\exp\!\left(\pi t m^2+2\pi m\Im z_0\right).
\]
Meanwhile
\[
|z_0+m\tau|=O(m).
\]
Thus along this sequence
\[
\log|\Theta(z_0+m\tau\mid\tau)|
=\pi t m^2+O(m),
\]
which cannot be bounded by $O(m^\rho)$ for any $\rho<2$. Therefore the order is at least $2$.

Consequently
\[
\boxed{\rho_\Theta=2}.
\]
:::
