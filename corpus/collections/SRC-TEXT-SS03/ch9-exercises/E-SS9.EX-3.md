---
schema: qual/card@1
id: E-SS9.EX-3
kind: problem
title: "In contrast with the result in Lemma 1"
classification:
  areas:
  - complex-analysis
  topics: ['Elliptic Functions', 'Weierstrass P', 'Lattices']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
3. In contrast with the result in Lemma 1.5, prove that the series

$$
\sum_ {n + m \tau \in \Lambda^ {*}} \frac {1}{| n + m \tau | ^ {2}} \quad \mathrm{where} \tau \in \mathbb {H}
$$

does not converge.
In fact, show that

$$
\sum_ {1 \leq n ^ {2} + m ^ {2} \leq R ^ {2}} 1 / (n ^ {2} + m ^ {2}) = 2 \pi \log R + O (1) \quad \text { as } R \to \infty .
$$
:::

::: {.solution}
First consider the square lattice. For $p=(m,n)\in\mathbb Z^2\setminus\{0\}$, let $Q_p=p+[-1/2,1/2]^2$. For $|p|\ge2$ and $x\in Q_p$, the mean-value theorem applied to $r\mapsto r^{-2}$ gives
\[
\left|\frac1{|x|^2}-\frac1{|p|^2}\right|
\le \frac{C}{|p|^3},
\]
with an absolute constant $C$. Hence
\[
\int_{Q_p}\frac{dx}{|x|^2}
=\frac1{|p|^2}+O(|p|^{-3}).
\tag{1}
\]
The total error from summing (1) over $1\le|p|\le R$ is bounded, because
\[
\sum_{p\ne0}|p|^{-3}<\infty.
\]
The union of the corresponding unit squares differs from the annulus $1\le|x|\le R$ only by a fixed inner region and an outer annulus of width $O(1)$. The integral of $|x|^{-2}$ over that outer annulus is $O(1/R)$, hence in particular $O(1)$. Consequently
\[
\sum_{1\le m^2+n^2\le R^2}\frac1{m^2+n^2}
=\int_{1\le|x|\le R}\frac{dx}{|x|^2}+O(1).
\]
In polar coordinates,
\[
\int_{1\le|x|\le R}\frac{dx}{|x|^2}
=\int_0^{2\pi}\int_1^R\frac1{r^2}r\,dr\,d\theta
=2\pi\log R.
\]
Thus
\[
\sum_{1\le m^2+n^2\le R^2}\frac1{m^2+n^2}
=2\pi\log R+O(1).
\]

Now let $\tau\in\mathbb H$. Since the real-linear map
\[
(m,n)\longmapsto n+m\tau
\]
is an isomorphism $\mathbb R^2\to\mathbb C$, there is $C>0$ such that
\[
|n+m\tau|\le C\sqrt{m^2+n^2}
\]
for all integers $m,n$. Hence
\[
\frac1{|n+m\tau|^2}\ge \frac1{C^2(m^2+n^2)}.
\]
The square-lattice sum diverges logarithmically, so
\[
\sum_{n+m\tau\in\Lambda^*}\frac1{|n+m\tau|^2}
\]
diverges as well.
:::
