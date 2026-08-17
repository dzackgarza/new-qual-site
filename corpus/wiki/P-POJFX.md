---
schema: qual/card@1
id: P-POJFX
kind: problem
title: Jordan form of the all-ones matrix over a field
classification:
  areas:
  - algebra
  topics:
  - jordan-canonical-form
  - eigenvalues-and-eigenvectors
  - characteristic
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Let $F$ be a field and $n$ a positive integer, and consider
\[
A=\left[\begin{array}{ccc}
1 & \dots & 1 \\
& \ddots & \\
1 & \dots & 1
\end{array}\right] \in M_{n}(F)
.\]

Show that $A$ has a Jordan normal form over $F$ and find it.

> Hint: treat the cases $n\cdot  1 \neq 0$ in $F$ and $n\cdot 1 = 0$ in $F$ separately.

:::

:::{.solution}
Note that if $\vector x = \tv{x_1,\cdots, x_n}$ then $A\vector x = \tv{\sum x_i, \sum x_i, \cdots, \sum x_i}$, so $A$ acts by summing the entries in $\vector x$ and setting every coordinate to that sum.
By inspection (or clever guessing), we can find eigenvalues and eigenvectors:

- $\lambda = 0$ and:
  - $\vector v_1 = \tv{1,0,0,\cdots,0, -1}$ 
  - $\vector v_2 = \tv{0,1,0,\cdots,0, -1}$
  - $\vector v_3 = \tv{0,0,1,\cdots,0, -1}$
  - $\cdots$
  - $\vector v_{n-1} = \tv{0,0,0,\cdots,1, -1}$
- $\lambda = n$ and $\vector v_n = \tv{1,1,\cdots, 1}$

Note that for $\lambda = n$, we have $A \tv{1,1,\cdots, 1} = \tv{n\cdot 1,\cdots, n\cdot 1}$.
So for $n\cdot 1\neq 0$, there are two eigenspaces corresponding to $\lambda = 0, n$, and if $n\cdot 1 = 0$ these collapse to just a single eigenspace for $\lambda = 0$.

Assuming $n\cdot 1\neq 0$, we get a characteristic polynomial of $(x-n)x^{n-1}$.
The $x-n$ factor corresponds to a single $1\times 1$ Jordan block with diagonal $n$.
For the $x^{n-1}$ factor, we've produced $n-1$ distinct eigenvectors, so we get $n-1$ Jordan blocks of size $1\times 1$ with diagonal zero.
Thus
\[
\JCF(A) =
\left[
\begin{array}{c|c|c|c|c}
n & \cdot & \cdot & \cdot & \cdot \\ \hline
\cdot & 0 & \cdot & \cdot & \cdot \\ \hline
\cdot & \cdot & 0 & \ddots & \cdot \\ \hline
\cdot & \cdot & \cdot & \ddots & \cdot \\ \hline
\cdot & \cdot & \cdot & \cdot & 0 
\end{array}
\right]
.\]
One can verify this by checking directly that the minimal polynomial of $A$ is $p(x) = (x-n)x$, so the size of the largest Jordan block for $\lambda = n$ is 1 and for $\lambda = 0$ is $n-1$, while the characteristic polynomial is $(x-n)x^{n-1}$, so the sum of the sizes of Jordan blocks for $\lambda = n$ is 1 and for $\lambda = 0$ is $n-1$, forcing the $1\times 1$ blocks everywhere.

Now consider the case when $n\cdot 1 = 0$; then $\vector v_n$ becomes an eigenvector for $\lambda = 0$ instead of $\lambda = n$.
The minimal polynomial becomes $(x-0)x = x^2$ and the characteristic polynomial becomes $x^n$, so $\lambda = 0$ has:

- The size of the largest Jordan block is 2,
- The sum of sizes of Jordan blocks is $n-1$,

and so this forces one block of size $2\times 2$ and $n-2$ blocks of size $1\times 1$.
So we now have:
\[
\JCF(A) = 
\left[
\begin{array}{cc|c|c|c}
0 & 1 & \cdot & \cdot & \cdot \\
\cdot & 0 & 0 & \cdot & \cdot \\ \hline
\cdot & \cdot & 0 & \ddots & \cdot \\ \hline
\cdot & \cdot & \cdot & \ddots & 0 \\ \hline
\cdot & \cdot & \cdot & \cdot & 0 
\end{array}
\right]
.\]



:::

