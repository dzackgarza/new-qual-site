---
schema: qual/card@1
id: P-CAFA25C
kind: problem
title: "Biholomorphic map between simply connected regions: existence, derivative bound, and equality"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Riemann Mapping Theorem
  - Schwarz Lemma
  - Biholomorphic Maps
relations: []
review: draft
---

::: problem
Suppose $R_1, R_2$ are bounded simply connected regions in $\mathbb{C}$.
Let $z_1 \in R_1$ and $z_2 \in R_2$.

(i) Prove that there exists a holomorphic bijective function $f : R_1 \to R_2$ such that $f(z_1) = z_2$.

(ii) Suppose that $g : R_1 \to R_2$ is a holomorphic function such that $g(z_1) = z_2$.
Prove that $|g'(z_1)| \leq |f'(z_1)|$.

(iii) When does equality occur in (ii)?
:::

::: solution
Choose Riemann maps
\[
\phi_j:R_j\to\mathbb D
\]
with
\[
\phi_j(z_j)=0,
\qquad j=1,2.
\]

(i) Then
\[
f=\phi_2^{-1}\circ\phi_1
\]
is a biholomorphism $R_1\to R_2$ and satisfies $f(z_1)=z_2$.

(ii) Given $g:R_1\to R_2$ with $g(z_1)=z_2$, define
\[
G=\phi_2\circ g\circ\phi_1^{-1}:\mathbb D\to\mathbb D.
\]
Then $G(0)=0$, so Schwarz's lemma gives $|G'(0)|\le1$. By the chain rule,
\[
|G'(0)|
=\frac{|\phi_2'(z_2)|\,|g'(z_1)|}{|\phi_1'(z_1)|}.
\]
For the map $f$ above,
\[
|f'(z_1)|
=\frac{|\phi_1'(z_1)|}{|\phi_2'(z_2)|}.
\]
Therefore
\[
\boxed{|g'(z_1)|\le|f'(z_1)|.}
\]

(iii) Equality occurs exactly in the equality case of Schwarz's lemma, namely
when
\[
G(z)=e^{i\theta}z
\]
for some real $\theta$. Equivalently,
\[
\boxed{
g=\phi_2^{-1}\circ(e^{i\theta}\operatorname{id})\circ\phi_1.
}
\]
Thus equality holds exactly for biholomorphisms $R_1\to R_2$ carrying $z_1$
to $z_2$.
:::
