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
<1>1. The element
$$
z=\sum_{i=1}^n x_i y_i
$$
is independent of the chosen basis $x_1,\ldots,x_n$ and its dual basis.
::: {.proof}
Let $x_1',\ldots,x_n'$ be another basis, with dual basis $y_1',\ldots,y_n'$. Write
$$
x_j'=\sum_i a_{ij}x_i,
\qquad
y_i=\sum_j b_{ij}y_j'.
$$
Since the two displayed bases are dual,
$$
a_{ij}=(x_j',y_i)=b_{ij}.
$$
Therefore
$$
\sum_i x_i y_i
=\sum_{i,j} b_{ij}x_i y_j'
=\sum_{i,j} a_{ij}x_i y_j'
=\sum_j x_j'y_j'.
$$
Thus $z$ is basis-independent.
:::

<1>2. If the form is invariant, then
$$
\boxed{([a,b],c)=(a,[b,c])}
$$
for all $a,b,c\in A$.
::: {.proof}
Using bilinearity, symmetry, and invariance,
$$
\begin{aligned}
([a,b],c)
&=(ab-ba,c)\\
&=(ab,c)-(ba,c)\\
&=(a,bc)-(c,ba)\\
&=(a,bc)-(cb,a)\\
&=(a,bc)-(a,cb)\\
&=(a,[b,c]).
\end{aligned}
$$
:::

<1>3. If
$$
[a,x_i]=\sum_j\lambda_{ij}x_j,
\qquad
[a,y_i]=\sum_j\mu_{ij}y_j,
$$
then
$$
\boxed{\lambda_{ij}+\mu_{ji}=0}
$$
for all $i,j$.
::: {.proof}
By duality,
$$
\lambda_{ij}=([a,x_i],y_j).
$$
Using step <1>2,
$$
([x_i,a],y_j)=(x_i,[a,y_j]),
$$
so
$$
\lambda_{ij}
=-([x_i,a],y_j)
=-(x_i,[a,y_j])
=-\mu_{ji}.
$$
:::

<1>4. The element $z$ lies in the center of $A$.
::: {.proof}
For arbitrary $a\in A$, the commutator identity gives
$$
\begin{aligned}
[a,z]
&=\sum_i[a,x_i y_i]\\
&=\sum_i\bigl([a,x_i]y_i+x_i[a,y_i]\bigr)\\
&=\sum_{i,j}\lambda_{ij}x_jy_i
  +\sum_{i,j}\mu_{ij}x_i y_j\\
&=\sum_{i,j}(\lambda_{ij}+\mu_{ji})x_jy_i\\
&=0
\end{aligned}
$$
by step <1>3. Since $a$ was arbitrary,
$$
\boxed{z\in Z(A)}.
$$
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>1 proves part (a), step <1>2 proves part (b), and step <1>3 together with step <1>4 proves part (c).
:::
:::
