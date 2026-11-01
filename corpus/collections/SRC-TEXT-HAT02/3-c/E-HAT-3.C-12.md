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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 12; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read; the answer is right and so are the three relations. Repaired two places where the
    argument was named rather than given. First, primitivity of $\alpha$ is now derived from the
    absence of bidegrees $(i,j)$ with $i,j>0$ summing to $1$, and $\Delta(\beta)$ now records
    what about the Bockstein is used — naturality and additivity — and that $\beta$ is $\pm\beta_1(\alpha)$
    with the sign harmless; the previous line appealed to "naturality" alone, which does not
    produce the two terms by itself. Second, the dualization is now justified: $H_*$ is the dual of
    $H^*$ (finite type over the field $\ZZ_p$), the Pontryagin product is the transpose of the
    coproduct, and the note shows the paired computations for $x^2=0$ and $y_iy_j=\binom{i+j}{i}y_{i+j}$,
    with $xy_i=y_ix$ from graded commutativity in even degree $|y_i|=2i$. Also corrected a typo in
    the text ($H_{2n+1}(H;\ZZ_p)$) and added the remark that the displayed relations determine the
    multiplication. The boxed answer $\Lambda_{\ZZ_p}(x)\otimes\Gamma_{\ZZ_p}(y)$ is correct.
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
\qquad \gradeddegree{\alpha}=1,\ \gradeddegree{\beta}=2,
$$
with $\beta$ the Bockstein of $\alpha$.

The H-space structure comes from the abelian group structure on $K(\ZZ_p,1)$, so $\Delta$ is the map induced by the group multiplication.

The degree-one class $\alpha$ is primitive for a reason that needs no computation: $\Delta(\alpha)-\alpha\otimes1-1\otimes\alpha$ is a sum of terms of bidegree $(i,j)$ with $i,j>0$ and $i+j=1$, and there are no such bidegrees. Hence
$$
\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha.
$$
For $\beta$ one uses that the Bockstein $\beta_1$ of $0\to\ZZ_p\to\ZZ_{p^2}\to\ZZ_p\to0$ is natural and additive, and that $\beta$ is $\pm\beta_1(\alpha)$; the sign is irrelevant because it is the same on both sides. Then
$$
\Delta(\beta)=\pm\beta_1\bigl(\Delta(\alpha)\bigr)
=\pm\bigl(\beta_1(\alpha)\otimes1+1\otimes\beta_1(\alpha)\bigr)
=\beta\otimes1+1\otimes\beta,
$$
so both algebra generators are primitive. Note what is *not* being used: the derivation property of the Bockstein would also do here, but additivity and naturality suffice. Therefore
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
The dualization needs one sentence of justification. $H_*(L;\ZZ_p)$ is the dual of $H^*(L;\ZZ_p)$ — finite type, and $\ZZ_p$ a field — and by definition of the Pontryagin product $\langle uv,w\rangle=\langle u\otimes v,\Delta w\rangle$. Since $\{\alpha^i\beta^j\}$ is a $\ZZ_p$-basis of $H^*(L;\ZZ_p)$, it suffices to pair each identity with it. For instance
$$
\langle x^2,\beta\rangle=\langle x\otimes x,\beta\otimes1+1\otimes\beta\rangle=0,
$$
so $x^2$, which lies in the one-dimensional $H_2(L;\ZZ_p)=\ZZ_p\cdot y_1$, is zero; and
$$
\langle y_iy_j,\beta^{i+j}\rangle=\langle y_i\otimes y_j,\Delta(\beta^{i+j})\rangle=\binom{i+j}{i},
\qquad
\langle y_iy_j,\alpha\beta^{i+j}\rangle=0,
$$
which is the second identity; the third is graded commutativity, $xy_i=(-1)^{|x||y_i|}y_ix=y_ix$, because $|y_i|=2i$ is even. The same three computations with $\alpha\beta^m$ in place of $\beta^m$ give $x\cdot xy_i=0$ and $xy_i\cdot y_j=\binom{i+j}{i}xy_{i+j}$, so the displayed relations determine the whole multiplication and no relation is missing.
Thus the Pontryagin algebra is
$$
\boxed{H_*(L;\ZZ_p)
\cong\Lambda_{\ZZ_p}(x)\otimes\Gamma_{\ZZ_p}(y),}
$$
with $\gradeddegree{x}=1$, $\gradeddegree{y_n}=2n$, and the divided-power multiplication displayed above.
:::
