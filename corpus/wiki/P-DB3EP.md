---
schema: qual/card@1
id: P-DB3EP
kind: problem
title: "$\\impliedby$: Suppose that $A\\vector x = \\vector b$ has a solution $\\v\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
$\impliedby$: Suppose that $A\vector x = \vector b$ has a solution $\vector x$.

Write $A = [\vector a_1, \vector a_2, \cdots \vector a_m]^t$ in block form with each $\vector a_i$ a row of $A$.
By definition, a solution to this equation is a $\vector x = (x_i)$ such that for each $i$, we have $\inner{\vector a_i}{\vector x} = b_i$ (by carrying out the matrix multiplication).

But 

\begin{align*}
\inner{\vector a_i}{\vector x} &= b_i \\
\implies \sum_{j=1}^m a_{ij} x_j &= b_i
,\end{align*}

which says that the collection $x_1, \cdots, x_n$ solves the equation
$$
a_{i1} x_1 + a_{i2} x_2 + \cdots a_{im} = b_i
$$

for every $i$, which is exactly the statement that the $x_i$ simultaneously solve the given system.

$\implies$:
Suppose that the given system has a simultaneous solutions $x_1, x_2, \cdots, x_n$, and consider the matrix equation $A\vector x = \vector b$.

Letting $\vector x = [x_1, x_2, \cdots, x_n]$, we can rewrite
$$
b_i = a_{i1}x_1 + a_{i2} x_2 + \cdots + a_{im} x_m = \inner{\vector a_i}{\vector x},
$$

where $\vector a_i = [a_{i1}, a_{i2}, \cdots, a_{im}]$.

But then $\vector a_i$ is the $i$th row of $A$, and $A\vector x = \vector b$ has a solution iff there is a $\vector x$ such that $\inner{\vector a_i}{\vector x} = b_i$ for all $i$, which is exactly what we've constructed.

## Part 2

Noting that applying a row operation to $A$ is the same as taking the product $E A$ for some elementary matrix $E$, we can write 
$A_1 = \left( \prod_{i=1}^\ell E_i \right) A$ 
and 
$B_1 = \left( \prod_{i=1}^\ell E_i \right) B$,

thus

\begin{align*}
A \vector x &= \vector b \\
\implies E_\ell A \vector x &= E_\ell \vector b \\
\implies E_{\ell-1} E_\ell A \vector x &= E_{\ell-1} E_\ell \vector b \\
&\vdots \\
\implies E_1 E_2 \cdots E_\ell A \vector x &= E_1 E_2 \cdots E_\ell A \vector b \\
\implies A_1 \vector x &= B_1
\end{align*}

## Part 3

1. $AX=B$ has a solution $\iff \rank(A) = \rank(C)$:

Note that we can only have $\rank C \geq \rank A$.

$\implies$:

Suppose that $AX = B$ has a solution; then $\vector b$ is in the column space of $A$.
But this says that 
$$
\mathrm{span}(\theset{\vector a_i}) = \mathrm{span}(\theset{\vector a_i} \union \theset{\vector b}),
$$

where $\vector a_i$ are the columns of $A$. 
But then taking dimensions on both sides yields $\rank A = \rank C$, since the rank of the dimension of the column space.

$\impliedby$:

Suppose $\rank A = \rank C$; then the 
$$
\dim \mathrm{span}(\theset{\vector a_i}) = \dim \mathrm{span}( \theset{\vector a_i} \union \theset{\vector b} ),
$$

which says that $\vector b_i$ is in the column space of $A$, and thus $AX=B$ has a solution. 
$\qed$

2. The solution is unique $\iff \rank(A) = m$.

$\implies$:
To the contrapositive, Suppose $\rank(A) < m$.
Then by rank-nullity, $\dim \ker A > 0$, so there is a vector $\vector v \neq 0$ such that $A\vector v = 0$.
But noting that $\vector x = \vector 0$ is always *a* solution to $A\vector x = \vector 0$, this yields two distinct solutions.

$\impliedby$:

Suppose that $\rank(A) = m$. 
Then by rank-nullity, $\dim \ker A = 0$, so $\ker A = \theset{\vector 0}$.
Now suppose $\vector v_1, \vector v_2$ are potentially distinct solutions to $A\vector x = \vector b$.

Then,
\begin{align*}
A \vector v_1 &= A \vector v_2 = \vector b \\
&\implies A \vector v_1 - A \vector v_2 =  \vector b - \vector b = \vector 0 \\
&\implies A (\vector v_1 - \vector v_2) = \vector 0 \\
&\implies \vector v_1 - \vector v_2 \in \ker A \\
&\implies \vector v_1 - \vector v_2 = \vector 0 \\
&\implies \vector v_1 = \vector v_2
,\end{align*}

which shows that any solution is unique.

## Part 4

We want to show that $A\vector x = \vector 0$ has a nontrivial solution $\iff \rank(A) < m$.

$\implies$:
Suppose $A\vector v = \vector 0$ for some $\vector v \neq 0$. Then $\dim \ker A \geq 1$, and by rank nullity we must have $m = \dim \ker A + \rank(A)$. 
But this immediately forces $\rank(A) \leq m-1$.

$\impliedby$:
Suppose $\rank(A) < m$. Then again by rank nullity, this forces $\dim \ker A \geq 1$, so $A$ has a nontrivial kernel and thus there is a nontrivial solution to $A\vector x = 0$.


