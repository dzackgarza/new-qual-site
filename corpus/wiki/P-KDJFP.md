---
schema: qual/card@1
id: P-KDJFP
kind: problem
title: '1. $AX=B$ has a solution $\iff \rank(A) = \rank(C)$:'
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
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
