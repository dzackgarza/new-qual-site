---
schema: qual/card@1
id: P-CASP26D
kind: problem
title: "Holomorphic function on the upper half-plane with real boundary values and polynomial growth is a Laurent polynomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Boundary Values
  - Reflection Principle
  - Growth Estimates
relations: []
review: draft
---

::: {.problem}
Let $f$ be holomorphic on the upper half-plane $H = \{z \in \CC : \operatorname{Im} z > 0\}$.
Assume that

(i) $f$ extends continuously to $H \setminus \{0\}$,

(ii) $f(x) \in \RR$ for all $x \in \RR \setminus \{0\}$,

(iii) there exists an integer $N > 0$ such that $|f(z)| \leq |z|^N + |z|^{-N}$ for all $z \in H$.

Prove that there are constants $a_k \in \RR$ such that $f(z) = \sum_{k=-N}^{N} a_k z^k$.
:::

::: {.solution}
By Schwarz reflection across the real axis, the boundary reality hypothesis
extends $f$ to a holomorphic function $F$ on $\CC\setminus\{0\}$ by
$$
F(z)=
\begin{cases}
f(z),&\operatorname{Im}z\ge0,\ z\ne0,\\
\overline{f(\bar z)},&\operatorname{Im}z<0.
\end{cases}
$$
The reflected function satisfies
$$
F(\bar z)=\overline{F(z)}
$$
and the same growth estimate
$$
|F(z)|\le |z|^N+|z|^{-N}.
$$

Write the Laurent expansion on $\CC^*$ as
$$
F(z)=\sum_{k\in\ZZ}a_k z^k.
$$
For every $r>0$, Cauchy's coefficient formula gives
$$
|a_k|
\le (r^N+r^{-N})r^{-k}.
$$
If $k>N$, let $r\to\infty$ to obtain $a_k=0$. If $k<-N$, let $r\to0$
to obtain $a_k=0$. Therefore
$$
F(z)=\sum_{k=-N}^N a_k z^k.
$$

Finally, the symmetry
$F(\bar z)=\overline{F(z)}$ forces every Laurent coefficient to be real.
Restricting back to the upper half-plane gives
$$
\boxed{f(z)=\sum_{k=-N}^N a_k z^k,\qquad a_k\in\RR.}
$$
:::
