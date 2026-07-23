---
schema: qual/card@1
id: P-RB3X3
kind: problem
title: "Let $L$ be a 3-manifold with homology $[\\ZZ, \\ZZ_3, 0, \\ZZ, \\ldots]$ a\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
Let $L$ be a 3-manifold with homology $[\ZZ, \ZZ_3, 0, \ZZ, \ldots]$ and let $X = L \cross \Sigma L$. Compute $H_*(X), H^*(X)$.

:::{.solution}
Useful facts:

- $H_{k}(X\times Y) \cong \bigoplus _{{i+j=k}}H_{i}(X)\otimes H_{j}(Y) \bigoplus_{i+j=k-1}\tor(H_i(X), H_j(Y))$
- $\tilde H_i(\Sigma X) = \tilde H_{i-1}(X)$

We will use the fact that $H_*(\Sigma L) = [\ZZ, \ZZ, \ZZ_3, 0, \ZZ]$.

Represent $H_*(L)$ by $p(x, y) = 1 + yx + x^3$ and $H_*(\Sigma L)$ by $q(x,y) = 1 + x + yx^2 + x^4$, we can extract the free part of $H_*(X)$ by multiplying

$$p(x,y)q(x,y) = 1 + (1+y)x + 2yx^2 + (y^2+1)x^3 + 2x^4 + 2yx^5 + x^7$$

where multiplication corresponds to the tensor product, addition to the direct sum/product.

So the free portion is
$$H_*(X) = [\ZZ, \ZZ\oplus \ZZ_3, \ZZ_3\tensor \ZZ_3, \ZZ \oplus \ZZ_3\tensor \ZZ_3, \ZZ^2, \ZZ_3^2, 0, \ZZ] \\
=[\ZZ, \ZZ\oplus \ZZ_3, \ZZ_3, \ZZ \oplus \ZZ_3, \ZZ^2, \ZZ_3^2, 0, \ZZ]
$$

We can add in the correction from torsion by noting that only terms of the form $\tor(\ZZ_3, \ZZ_3) = \ZZ_3$ survive. These come from the terms $i=1, j=2$, so $i+j=k-1 \implies k = 1+2+1 = 4$ and there is thus an additional torsion term appearing in dimension 4. So we have

$$H_*(X) = [\ZZ, \ZZ\times \ZZ_3, \ZZ_3, \ZZ \times \ZZ_3, \ZZ^2 \times \ZZ_3, \ZZ_3^2, 0, \ZZ] \\ = [\ZZ, \ZZ, 0,\ZZ,\ZZ^2,0,0,\ZZ] \times [0,\ZZ_3,\ZZ_3,\ZZ_3,\ZZ_3,\ZZ_3^2,0,0]$$

and $$H^*(X)= [\ZZ, \ZZ, 0,\ZZ,\ZZ^2,0,0,\ZZ] \times [0, 0,\ZZ_3,\ZZ_3,\ZZ_3,\ZZ_3,\ZZ_3^2,0] \\ = [\ZZ, \ZZ, \ZZ_3,\ZZ\times \ZZ_3,\ZZ^2\times \ZZ_3,\ZZ_3,\ZZ_3^2,\ZZ].$$

:::

