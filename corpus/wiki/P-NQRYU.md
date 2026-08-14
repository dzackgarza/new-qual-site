---
schema: qual/card@1
id: P-NQRYU
kind: problem
title: "Let $A = (a_{ij})$ and consider $\\vector \\epsilon_{ij}$, the matrix w\u2026"
classification:
  areas:
  - algebra
  topics:
  - centralizers-and-normalizers
  - matrices
  - rings
relations: []
review: draft
---

Let $A = (a_{ij})$ and consider $\vector \epsilon_{ij}$, the matrix with a $1$ in the $i$th row and $j$th column and zeros elsewhere.

Then, for a fixed $(i, j)$, if we write $A = [\vector a_1^t, \vector a_2^t, \cdots, \vector a_n^t]$ as a block matrix of column vectors, we have
$$
A \vector e_{ij} = [0, 0, \cdots, \vector a_i^t, 0, \cdots, 0]
$$
as a block matrix where $\vector a_i^t$ occurs as the $j$th column.

In other words, right-multiplication by $\vector e_{ij}$ selects column $i$ from $A$, placing it in column $j$ of a matrix of zeros.

For example, for $(i, j) = (3, 2)$ we have

$$
A \vector e_{32} = 
\left(\begin{matrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{21}&a_{22}&a_{33}\end{matrix}\right) 
\left(\begin{matrix}0&0&0\\0&0&0\\0&1&0\end{matrix}\right) =
\left(\begin{matrix}0&a_{13}&0\\0&a_{23}&0\\0&a_{33}&0\end{matrix}\right),
$$

which is a matrix that contains column $3$ of $A$ (the $i$ value) as its $2$nd column (the $j$ value).

On the other hand, *left* multiplication by $\vector e_{ij}$ selects the $j$th **row** of $A$ and places it the $i$th **row** of a zero matrix, so for example we have

$$
\vector e_{32} A = 
\left(\begin{matrix}0&0&0\\0&0&0\\0&1&0\end{matrix}\right) \left(\begin{matrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{21}&a_{22}&a_{33}\end{matrix}\right) 
=
\left(\begin{matrix}0&0&0\\0&0&0\\a_{21}&a_{22}&a_{23}\end{matrix}\right)
$$

In general, these two products will not be equal, since the first has a nontrivial column and the latter has a nontrivial row.
If $A \in Z(M_n(R))$, these two must be equal, so we can equate corresponding entries to find that

- $a_{21} = 0$, from comparing entries in row 3, column 1,

- $a_{23} = 0$, from comparing entries in row 3, column 3

- $a_{22} = a_{33}$ by comparing entries in row 3, column 2.

Letting the multiplication run over all possibilities for $\vector e_{ij}$ yields $a_{ii} = a_{jj}$ for every pair $i, j$ and $a_{ij} = 0$ whenever $i\neq j$.
Setting $r = a_{ii} = a_{jj}$ for all $1\leq i,j \leq n$ forces $A$ to be a matrix of the form

$$
A = \left(\begin{matrix}r&0&0&\cdots&0\\0&r&0&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\0&0&0&\cdots&r\end{matrix}\right) \definedas r I_n.
$$

To see that we must have $r\in Z(R)$, let $sI_n \in Z(M_n(R))$ be arbitrary, where $s$ is not assumed to be in $Z(R)$.
Then $(rI_n)(sI_n) = (sI_n)(rI_n)$ by assumption, since these are matrices in the center of $M_n(R)$.
But $M_n(R)$ is an $R\dash$module, and so the scalars $r,s$ commute with the module elements $I_n$.
This means that we in fact have

\begin{align*}
(r I_n) (s I_n) &= (rs) I_n^2 = (rs)I_n, \\
(s I_n) (r I_n) &= (sr) I_n^2 = (sr)I_n \\
&\implies (rs) I_n = (sr) I_n \\
&\implies (rs -sr) I_n = 0_n,
\end{align*}

the $n\times n$ zero matrix.

But then by equating (for example) the $1,1$ entry of the matrix $(rs -sr) I_n$ with the corresponding entry in $0_n$, we find $rs - sr = 0_R$, which means $rs = sr \in R$.

Now since $s\in R$ was arbitrary, we find that $r\in Z(R)$ as desired.
