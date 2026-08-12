---
schema: qual/card@1
id: P-VJBIB
kind: problem
title: "Parts If $A$ has two distinct eigenvalues, we will have $A = PDP\\inv$ where $P$\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
1. Parts
   1. If $A$ has two distinct eigenvalues, we will have $A = PDP\inv$ where $P$ is the matrix of eigenvectors and $D$ has eigenvalues on the diagonal. We can compute the characteristic polynomial
  $$
  p_\chi(x) = x^2 - (\Tr A)x + \det A = x^2 - 7x + 6 = (x-6)(x-1),
  $$

      and so $\spec(A) = \theset{6,1}$. Computing the kernel of $A-\lambda I$ for each of these yields
  $$
  \vector v_1 = \left[ \begin{array} { c } { 1 } \\ { - 2 } \end{array} \right],
  \vector v_2 = \left[ \begin{array} { c } { 2 } \\ { 1 } \end{array} \right],
  $$

      And so we can write and check
  $$
  P = \left[ \begin{array} { c c } { 1 } & { 2 } \\ { - 2 } & { 1 } \end{array} \right] \\
  D = \left(\begin{array}{rr}
    6 & 0 \\
    0 & 1
    \end{array}\right) \\
  $$

      We can compute $PP^T = \mathrm{diag}(5,5)$, so $P$ can be made orthogonal by replacing $P$ with $(1/\sqrt 5) P$. With this replacement, a quick computation shows that $PDP^T = A$.

   1. We will use the fact that $A = PDP\inv$ where since $A$ is symmetric and $P$ is orthogonal. We can write
   $$
   \inner{A\vector x}{\vector x} = \vector x^T A^T \vector x = \vector x^T (PDP^T)^T \vector x 
   = (P^T \vector x)^T D (P^T\vector x) = \vector y^T D \vector y = \inner{\vector y}{ D\vector y},
   $$
   where $\vector x\in S^2 \implies P^T\vector x \definedas \vector y \in S^2$ since $P^T$ is both orthogonal and full-rank (and thus a bijection $S^2 \selfmap$).

      We can now expand 
    $$
    \inner{\vector y}{D \vector y} = \sum_{i=1}^2 y_i \lambda_i y_i = \sum_{i=1}^2 \lambda_i y_i^2
    $$

      We now note that we can take $\vector y = \thevector{0, 1}$, in which case $D\vector y = \thevector{0, \lambda_2} = \thevector{0, 1}$ and thus $\inner{\vector y}{D \vector y} = 1$ is a candidate minimum.

      We can write this as the constrained optimization problem
      $$
      \text{Minimize } f(y_1, y_2) = 6y_1^2 + 1 y_2^2\\
      \text{subject to } g(y_1, y_2) = y_1^2 + y_2^2 = 1
      $$

      where we note that this constraint is equivalent to the original $\norm{\vector y} = \sqrt{y_1^2 + y_2^2} = 1$.

      This can be approached with Lagrange multipliers, i.e. looking at where $\nabla f = \lambda \nabla g$. This yields
      $$
      \thevector{12y_1, 2y_2} = \lambda \thevector{2y_1, 2y_2} \implies \\
      6y_1 = \lambda y_1, ~ y_2 = \lambda y_2.
      $$

      The second condition forces $y_2 \in \theset{0,1}$, and solving for $\lambda$ in this expression yields $\lambda = 1$ and so the first condition forces $y_1 = 0$. This leaves only one possibility, $\vector y = \thevector{0, 1}$, which is indeed the candidate from above. Thus the minimum value is 1. $\qed$
 

