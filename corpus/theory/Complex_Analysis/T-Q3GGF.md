---
schema: qual/card@1
id: T-Q3GGF
kind: theorem
title: Schwarz reflection principle
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
relations: []
review: draft
---

::: {.theorem ref="SchwarzReflection"}
Let $\Omega\subseteq\CC$ be an open set with $\overline{z}\in\Omega$ for every $z\in\Omega$, and put $\Omega^+\coloneqq\{z\in\Omega : \operatorname{Im}z>0\}$, $\Omega^-\coloneqq\{z\in\Omega : \operatorname{Im}z<0\}$, and $I\coloneqq\Omega\cap\RR$.
Let $f$ be [[D-E7A5W|holomorphic]] on $\Omega^+$, continuous on $\Omega^+\cup I$, and real-valued on $I$.
Then the function
$$
F(z)\coloneqq\begin{cases}f(z), & z\in\Omega^+\cup I,\\ \overline{f(\overline{z})}, & z\in\Omega^-,\end{cases}
$$
is holomorphic on $\Omega$.
In particular, for $\Omega=\CC$: if $f$ is holomorphic on the upper half-plane, continuous on its closure, and real-valued on $\RR$, then $F$ is [[D-E7A5W|entire]].
:::
