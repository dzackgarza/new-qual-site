---
schema: qual/card@1
id: E-HAT-3.C-12
kind: problem
title: Pontryagin product in lens space homology
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Compute the Pontryagin product structure in $H_*(L; \ZZ_p)$ where $L$ is an infinite-dimensional lens space $S^\infty / \ZZ_p$, for $p$ an odd prime, using the coproduct in $H^*(L; \ZZ_p)$.
:::

::: {.solution}
For the infinite lens space
$$
L=S^\infty/\ZZ_p=K(\ZZ_p,1),
\qquad p\text{ odd},
$$
one has
$$
H^*(L;\ZZ_p)\cong
\Lambda(\alpha)\otimes\ZZ_p[\beta],
\qquad |\alpha|=1,\ |\beta|=2,
$$
with $\beta$ the Bockstein of $\alpha$.

The H-space structure comes from the abelian group structure on $K(\ZZ_p,1)$. The degree-one class $\alpha$ is primitive:
$$
\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha.
$$
Naturality of the Bockstein gives
$$
\Delta(\beta)=\beta\otimes1+1\otimes\beta,
$$
so both algebra generators are primitive. Therefore
$$
\Delta(\beta^n)=\sum_{i=0}^n\binom ni\beta^i\otimes\beta^{n-i},
$$
and
$$
\Delta(\alpha\beta^n)
=\sum_{i=0}^n\binom ni
\bigl(\alpha\beta^i\otimes\beta^{n-i}
+\beta^i\otimes\alpha\beta^{n-i}\bigr).
$$

Let $x\in H_1(L;\ZZ_p)$ be dual to $\alpha$, and let $y_n\in H_{2n}(L;\ZZ_p)$ be dual to $\beta^n$, with $y_0=1$. Let $xy_n\in H_{2n+1}$ denote the class dual to $\alpha\beta^n$. Dualizing the coproduct gives
$$
x^2=0,
\qquad
y_i y_j=\binom{i+j}{i}y_{i+j},
\qquad
x y_i=y_i x.
$$
Thus the Pontryagin algebra is
$$
\boxed{H_*(L;\ZZ_p)
\cong\Lambda_{\ZZ_p}(x)\otimes\Gamma_{\ZZ_p}(y),}
$$
with $|x|=1$, $|y_n|=2n$, and the divided-power multiplication displayed above.
:::
