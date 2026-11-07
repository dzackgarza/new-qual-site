---
schema: qual/card@1
id: E-HAT-3.3-8
kind: problem
title: Degree as sum of local signs
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 8; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the local-degree computation: at a regular value the fundamental class goes to the tuple
    of local generators, each carrying the sign $\varepsilon_i$, so the degree is
    $\sum_i\varepsilon_i$.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Added the published corroboration: Steven V. Sam, Solutions to Algebraic Topology (2008),
    SS3.3 Exercise 8, printed pp.14-15, is the same diagram-of-local-homology argument. Sam's set is
    thin here (its SS3.3 covers only Exercises 8, 17 and 32) and the file carries a cover sheet, so
    printed pages, not PDF pages, are cited. Sam's proof is corroborative only: it is not used to
    replace any step, and the local-degree step is checked against Hatcher p.135.
---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds, suppose there is a ball $B \subset N$ such that $f^{-1}(B)$ is the disjoint union of balls $B_i$ each mapped homeomorphically by $f$ onto $B$.
Show the degree of $f$ is $\sum_i \varepsilon_i$ where $\varepsilon_i$ is $+1$ or $-1$ according to whether $f: B_i \to B$ preserves or reverses local orientations induced from given fundamental classes $[M]$ and $[N]$.
:::

::: {.solution}
Choose $y\in\operatorname{int}B$. Then
$$
f^{-1}(y)=\{x_1,\ldots,x_r\},\qquad x_i\in\operatorname{int}B_i.
$$
Excision identifies
$$
H_n(M,M-f^{-1}(y))
\cong
\bigoplus_i H_n(B_i,B_i-\{x_i\})
\cong \bigoplus_i\ZZ,
$$
while
$$
H_n(N,N-\{y\})\cong\ZZ.
$$
The image of the fundamental class $[M]$ in the direct sum of local homology groups is the tuple of local orientation generators. On the $i$th summand, the map induced by $f\restrict_{B_i}:B_i\to B$ is multiplication by
$$
\varepsilon_i=
\begin{cases}
+1,&f\restrict_{B_i}\text{ preserves the chosen local orientations},\\
-1,&f\restrict_{B_i}\text{ reverses them}.
\end{cases}
$$
Hence the image of $[M]$ in $H_n(N,N-\{y\})$ is
$$
\left(\sum_i\varepsilon_i\right)\mu_y.
$$
But the image of $[M]$ under $f_*$ is also $\deg(f)[N]$, whose local image at $y$ is $\deg(f)\mu_y$. Therefore
$$
\boxed{\deg(f)=\sum_i\varepsilon_i.}
$$

The argument agrees with the published solution of Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.3 Exercise 8, printed pp.14--15, which sets up the same diagram of local homology groups; that solution is cited as a check on the structure, and the cover-shifting page index of the file is not used as a citation.
:::
