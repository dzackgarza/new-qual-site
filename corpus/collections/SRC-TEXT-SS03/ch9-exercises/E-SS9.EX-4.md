---
schema: qual/card@1
id: E-SS9.EX-4
kind: problem
title: "SS 9.4: Periodicity of the Weierstrass function by rearrangement"
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
4. By rearranging the series

$$
\frac {1}{z ^ {2}} + \sum_ {\omega \in \Lambda^ {*}} \left[ \frac {1}{(z + \omega) ^ {2}} - \frac {1}{\omega^ {2}} \right],
$$

show directly, without diferentiation, that $\wp ( z + \omega ) = \wp ( z )$ whenever $\omega \in \Lambda .$ [Hint: For R suficiently large, note that $\wp ( z ) = \wp ^ { R } ( z ) + O ( 1 / R )$ where $\begin{array} { r } { \dot { \wp } ^ { R } ( z ) = z ^ { - 2 } + \sum _ { 0 < \lvert \omega \rvert < R } ( ( z + \omega ) ^ { - 2 } - \omega ^ { - 2 } ) } \end{array}$ Next, observe that both $\boldsymbol { \wp } ^ { R } ( z + 1 ) - \boldsymbol { \wp } ^ { R } ( z )$ and $\wp ^ { R } ( z + \tau ) - \wp ^ { R } ( z )$ are $\begin{array} { r } { O ( \sum _ { R - c < | \omega | < R + c } | \omega | ^ { - 2 } ) = O ( 1 / R ) . ] } \end{array}$
:::

::: {.solution}
It suffices to prove periodicity under an arbitrary fixed $\lambda\in\Lambda$. For $R>0$, define
\[
\wp^R(z)=\frac1{z^2}+
\sum_{0<|\omega|<R}
\left(\frac1{(z+\omega)^2}-\frac1{\omega^2}\right).
\]
For $z$ in a fixed compact set disjoint from $-\Lambda$, the tail satisfies
\[
\wp(z)-\wp^R(z)
=O\left(\sum_{|\omega|\ge R}|\omega|^{-3}\right)
=O(R^{-1}),
\tag{1}
\]
because
\[
\frac1{(z+\omega)^2}-\frac1{\omega^2}=O(|\omega|^{-3})
\]
uniformly on such compact sets.

Also
\[
\wp^R(z)=
\sum_{|\omega|<R}\frac1{(z+\omega)^2}
-\sum_{0<|\omega|<R}\frac1{\omega^2}.
\]
Thus, after reindexing $\eta=\omega+\lambda$,
\[
\wp^R(z+\lambda)-\wp^R(z)
=
\sum_{|\eta-\lambda|<R}\frac1{(z+\eta)^2}
-\sum_{|\eta|<R}\frac1{(z+\eta)^2}.
\tag{2}
\]
Only lattice points in the symmetric difference of the two radius-$R$ discs contribute. They lie in the annulus
\[
R-|\lambda|<|\eta|<R+|\lambda|.
\]
This annulus contains $O(R)$ lattice points, while each summand in (2) is $O(R^{-2})$. Hence
\[
\wp^R(z+\lambda)-\wp^R(z)=O(R^{-1}).
\tag{3}
\]
Combining (1) and (3),
\[
\wp(z+\lambda)-\wp(z)=O(R^{-1}).
\]
Letting $R\to\infty$ gives
\[
\wp(z+\lambda)=\wp(z)
\]
for all $z$ away from the poles. By meromorphic continuation the identity holds everywhere. Thus every $\lambda\in\Lambda$ is a period of $\wp$.
:::
