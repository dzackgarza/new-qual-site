---
schema: qual/card@1
id: S-6CZ3B
kind: solution
title: Solution to P-PBVSZ
classification:
  areas:
  - algebra
  topics:
  - bilinear-forms
  - algebras
  - centralizers-and-normalizers
relations:
- kind: solves
  target: P-PBVSZ
review: draft
---

::: {.solution}
**(a)** Let $x_1',\dots,x_n'$ be another basis with dual basis $y_1',\dots,y_n'$.
Say $x_j' = \sum_i a_{ij}x_i$, $y_i = \sum_j b_{ij}y_j'$.
Then $(x_j',y_i) = a_{ij} = b_{ij}$.

Then $$z = \sum_i x_i y_i = \sum_{i,j} b_{ij} x_i y_j' \quad\text{(the same!)}$$ $$z' = \sum_j x_j' y_j' = \sum_{i,j} a_{ij} x_i y_j'$$ Since $a_{ij}=b_{ij}$, $z=z'$.

**(b)** $$([a,b],c) = (ab-ba,c) = (ab,c)-(c,ba) = (a,bc)-(cb,a) = (a,bc-cb) = (a,[b,c])$$

**(c)** We have $$\lambda_{ij} = ([a,x_i],y_j) = -([x_i,a],y_j) = -(x_i,[a,y_j])$$ $$\mu_{ji} = (x_i,[a,y_j])$$ so $\lambda_{ij}+\mu_{ji}=0$.

To show $z$ is central, show $[a,z]=0$ for all $a$: $$[a,z] = \sum_i [a,x_iy_i] = \sum_i \big([a,x_i]y_i + x_i[a,y_i]\big) = \sum_{i,j}\lambda_{ij}x_jy_i + \sum_{i,j}x_i\mu_{ij}y_j = \sum_{i,j}(\lambda_{ij}+\mu_{ji})x_jy_i = 0$$
:::
