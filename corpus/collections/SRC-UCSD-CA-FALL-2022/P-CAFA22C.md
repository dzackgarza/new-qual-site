---
schema: qual/card@1
id: P-CAFA22C
kind: problem
title: "Punctured disk and annulus are not conformally equivalent"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Show that the punctured unit disk $\mathbb{D}^* = \mathbb{D} \setminus \{0\}$ and the annulus $A = \{z : 1 < |z| < 2\}$ are not conformally equivalent.
:::

::: solution
Suppose $F:\mathbb D^*\to A$ were a biholomorphism. Since $F$ is bounded,
the isolated singularity at $0$ is removable, so $F$ extends holomorphically
to $\widetilde F:\mathbb D\to\mathbb C$.

Take any sequence $z_n\to0$, $z_n\ne0$. Compactness of the closed annulus
$1\le|w|\le2$ gives a subsequence for which $F(z_n)$ converges; continuity of
$\widetilde F$ shows every such limit equals $\widetilde F(0)$. Thus
$|\widetilde F(0)|\in[1,2]$.

If $1<|\widetilde F(0)|<2$, then this value lies in $A$, so surjectivity of
$F$ gives $w\in\mathbb D^*$ with $F(w)=\widetilde F(0)$, contradicting
injectivity of the nonconstant holomorphic map $\widetilde F$ in a
neighborhood of $0$ (equivalently, zeros of
$\widetilde F-\widetilde F(0)$ near $0$ have positive multiplicity and $0$ is
not isolated from the image in that fashion). More directly, the open mapping
theorem at $0$ would put values with modulus $<1$ or $>2$ in the image if
$|\widetilde F(0)|$ is on either boundary circle, while an interior value
would violate injectivity as above. In every case we obtain a contradiction.

Hence no conformal equivalence exists.
:::
