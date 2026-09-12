---
schema: qual/card@1
id: P-APAS21D
kind: problem
title: Orthogonal projections onto $\operatorname{range}(C^H)$ and $\operatorname{null}(C)$; projectors onto a line
classification:
  areas:
  - applied-algebra
  topics:
  - Inner Product Spaces
  - Linear Algebra
relations: []
review: draft
---

::: problem
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex components, $\mathbb{C}^n$ is the set of column vectors with $n$ complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) Let $C \in M_{m,n}$ with $\operatorname{rank}(C) = m$.
Find orthogonal projections that project $x \in \mathbb{C}^n$ onto $\operatorname{range}(C^H)$ and $\operatorname{null}(C)$.
Verify that your projections satisfy the properties of an orthogonal projection.

(b) For a given nonzero $y \in \mathbb{C}^n$, let $Y = \operatorname{span}(y)$.

(i) Find an oblique projector $A$ that projects vectors onto $Y$.
Find the complementary projection.

(ii) Find the unique orthogonal projector $A$ that projects vectors onto $Y$.
Find the complementary projection associated with $A$.
:::

::: solution
(a) Since $\operatorname{rank}C=m$, the $m\times m$ matrix $CC^H$ is positive definite and hence invertible.
Set
\[
P=C^H(CC^H)^{-1}C.
\]
Then
\[
P^H=P
\]
and
\[
P^2=C^H(CC^H)^{-1}CC^H(CC^H)^{-1}C=P,
\]
so $P$ is an orthogonal projector.
Its range is contained in $\operatorname{range}(C^H)$, while for every $C^Hu$,
\[
P(C^Hu)=C^H(CC^H)^{-1}CC^Hu=C^Hu.
\]
Therefore
\[
\operatorname{range}P=\operatorname{range}(C^H).
\]
Thus the orthogonal projection onto $\operatorname{range}(C^H)$ is
\[
\boxed{P=C^H(CC^H)^{-1}C}.
\]

Because
\[
\ker C=(\operatorname{range}C^H)^\perp,
\]
the complementary orthogonal projector is
\[
\boxed{Q=I-C^H(CC^H)^{-1}C}.
\]
Indeed $Q^H=Q$, $Q^2=Q$, and $CQ=0$, so $\operatorname{range}Q\subseteq\ker C$; conversely, if $Cx=0$, then $Qx=x$.

(b)(i) Choose any $z\in\mathbb C^n$ satisfying
\[
z^Hy=1.
\]
Then
\[
A=yz^H
\]
satisfies
\[
A^2=yz^Hyz^H=y(z^Hy)z^H=yz^H=A,
\]
and $\operatorname{range}A=\mathbb Cy=Y$.
Thus $A$ is a projection onto $Y$, generally oblique.
Its complementary projection is
\[
\boxed{I-A=I-yz^H}.
\]

(ii) The orthogonal projector onto $Y$ is obtained by taking
\[
z=\frac{y}{y^Hy}.
\]
Hence
\[
\boxed{A=\frac{yy^H}{y^Hy}}.
\]
This matrix is Hermitian and idempotent, so it is the orthogonal projector onto $Y$.
The complementary orthogonal projector is
\[
\boxed{I-\frac{yy^H}{y^Hy}},
\]
which projects onto $Y^\perp$.
:::
