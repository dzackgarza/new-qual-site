---
schema: qual/card@1
id: P-PBVSZ
kind: problem
title: The element $\sum x_i y_i$ of an algebra with invariant form is well-defined
  and central
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Algebras
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.problem}
Let $A$ be a finite-dimensional algebra over a field $F$ equipped with a non-degenerate symmetric bilinear form $(\cdot,\cdot): A \times A \to F$.
Let $x_1,\dots,x_n$ be a basis for $A$ and $y_1,\dots,y_n$ be the dual basis with respect to the given form, i.e., $(x_i,y_j) = \delta_{i,j}$ for all $i,j = 1,\dots,n$.

a. Show that the element $$z := \sum_{i=1}^n x_i y_i$$ is well defined independent of the initial choice of the basis $x_1,\dots,x_n$.
b. Assume for the remainder of the question that the form $(\cdot,\cdot)$ is *invariant*, which means that $(ab,c) = (a,bc)$ for all $a,b,c \in A$.
Show that $([a,b],c) = (a,[b,c])$ where $[\cdot,\cdot]$ is the commutator.
c. Let $a \in A$ be any element and suppose that $[a,x_i] = \sum_{j=1}^n \lambda_{ij} x_j$ and $[a,y_i] = \sum_{j=1}^n \mu_{ij} y_j$ for scalars $\lambda_{ij}, \mu_{ij} \in F$.
Show that $\lambda_{ij} + \mu_{ji} = 0$.
Deduce that $z$ lies in the *center* of the algebra $A$.
(You may find the identity $[a,xy] = [a,x]y + x[a,y]$ helpful here.)
:::

::: {.solution}
**(a)** Let $x_1',\dots,x_n'$ be another basis with dual basis $y_1',\dots,y_n'$.
Say $x_j' = \sum_i a_{ij}x_i$, $y_i = \sum_j b_{ij}y_j'$.
Then $(x_j',y_i) = a_{ij} = b_{ij}$.

Then $$z = \sum_i x_i y_i = \sum_{i,j} b_{ij} x_i y_j' \quad\text{(the same!)}$$ $$z' = \sum_j x_j' y_j' = \sum_{i,j} a_{ij} x_i y_j'$$ Since $a_{ij}=b_{ij}$, $z=z'$.

**(b)** $$([a,b],c) = (ab-ba,c) = (ab,c)-(c,ba) = (a,bc)-(cb,a) = (a,bc-cb) = (a,[b,c])$$

**(c)** We have $$\lambda_{ij} = ([a,x_i],y_j) = -([x_i,a],y_j) = -(x_i,[a,y_j])$$ $$\mu_{ji} = (x_i,[a,y_j])$$ so $\lambda_{ij}+\mu_{ji}=0$.

To show $z$ is central, show $[a,z]=0$ for all $a$: $$[a,z] = \sum_i [a,x_iy_i] = \sum_i \big([a,x_i]y_i + x_i[a,y_i]\big) = \sum_{i,j}\lambda_{ij}x_jy_i + \sum_{i,j}x_i\mu_{ij}y_j = \sum_{i,j}(\lambda_{ij}+\mu_{ji})x_jy_i = 0$$
:::
