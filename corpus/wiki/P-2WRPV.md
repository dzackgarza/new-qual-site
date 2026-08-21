---
schema: qual/card@1
id: P-2WRPV
kind: problem
title: Cokernel of a map $\ZZ^4\to\ZZ^3$ is $\ZZ/12\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Smith Normal Form
  - Structure Theorem
  - Modules
relations: []
review: draft
solved: false
---

::: problem
Let $\phi: \ZZ^4 \to \ZZ^3$ be a linear map which in the standard basis $\mathcal B$ is represented by

\begin{align*}
T &\definedas [\phi]_{\mathcal B} = 
[f_1^t, f_2^t, f_3^t, f_4^t] = 
\left[\begin{array}{cccc}
1  & 2  & 0 & 3 \\
0  & -3 & 3 & 1 \\
-1 & 1  & 1 & 5
\end{array}\right]
.\end{align*}

Then $\im T = \spanof_\ZZ\theset{f_1 ,f_2, f_3, f_4} \definedas N$ by construction.

We can then compute the echelon form

\begin{align*}
\left(\begin{array}{cccc}
1 & 1 & 1 & 5 \\
0 & 3 & 1 & 8 \\
0 & 0 & 4 & 9
\end{array}\right)
,\end{align*}

which has pivots in columns $1,2,$ and $3$, and thus

$$
N = \spanof_\ZZ\theset{f_1, f_2, f_3}
$$

Without loss of generality, we can consider the image of the reduced matrix

\begin{align*}
A' =
\left(\begin{array}{ccc}
-1 & 2 & 0 \\
0 & -3 & 3 \\
1 & 1 & 1
\end{array}\right)
,\end{align*}

since $N = \im A = \im A'$.

When computing the characteristic polynomial, we find that $\chi_{A'}(x) = (x+3)(x+2)(x-2)$, which means that $A'$ has distinct eigenvalues.
We can thus immediately write

\begin{align*}
JCF(A) = 
\left[\begin{array}{c|c|c}
2 & 0 & 0 \\
\hline
0 & -2 & 0 \\
\hline
0 & 0 & -3
\end{array}\right]
.\end{align*}

From this, we can obtain the Smith normal form,

\begin{align*}
SNF(A') = 
\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 12 \\
\end{array}\right]
,\end{align*}

which allows us to read off

\begin{align*}
\im A' \cong \ZZ \oplus \ZZ \oplus 12\ZZ 
,\end{align*}

and thus

\begin{align*}
\ZZ^3/N \cong \frac{\ZZ \oplus \ZZ \oplus \ZZ}{\ZZ \oplus \ZZ \oplus 12\ZZ} \cong \ZZ/12\ZZ.
.\end{align*}
:::
