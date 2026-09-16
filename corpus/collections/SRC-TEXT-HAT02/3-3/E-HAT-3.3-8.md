---
schema: qual/card@1
id: E-HAT-3.3-8
kind: problem
title: "Degree as sum of local signs"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds, suppose there is a ball $B \subset N$ such that $f^{-1}(B)$ is the disjoint union of balls $B_i$ each mapped homeomorphically by $f$ onto $B$.
Show the degree of $f$ is $\sum_i \varepsilon_i$ where $\varepsilon_i$ is $+1$ or $-1$ according to whether $f: B_i \to B$ preserves or reverses local orientations induced from given fundamental classes $[M]$ and $[N]$.
:::

::: {.solution}
Choose $y\in\operatorname{int}B$. Then
\[
f^{-1}(y)=\{x_1,\ldots,x_r\},\qquad x_i\in\operatorname{int}B_i.
\]
Excision identifies
\[
H_n(M,M-f^{-1}(y))
\cong
\bigoplus_i H_n(B_i,B_i-\{x_i\})
\cong \bigoplus_i\mathbb Z,
\]
while
\[
H_n(N,N-\{y\})\cong\mathbb Z.
\]
The image of the fundamental class $[M]$ in the direct sum of local homology groups is the tuple of local orientation generators. On the $i$th summand, the map induced by $f|_{B_i}:B_i\to B$ is multiplication by
\[
\varepsilon_i=
\begin{cases}
+1,&f|_{B_i}\text{ preserves the chosen local orientations},\\
-1,&f|_{B_i}\text{ reverses them}.
\end{cases}
\]
Hence the image of $[M]$ in $H_n(N,N-\{y\})$ is
\[
\left(\sum_i\varepsilon_i\right)\mu_y.
\]
But the image of $[M]$ under $f_*$ is also $\deg(f)[N]$, whose local image at $y$ is $\deg(f)\mu_y$. Therefore
\[
\boxed{\deg(f)=\sum_i\varepsilon_i.}
\]
:::
