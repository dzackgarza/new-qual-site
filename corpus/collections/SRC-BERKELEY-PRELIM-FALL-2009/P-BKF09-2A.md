---
schema: qual/card@1
id: P-BKF09-2A
kind: problem
title: Berkeley Fall 2009 prelim problem 2A
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that no polynomial $p ( a , b , c , d )$in four variables over C has the property that when p is evaluated on the entries of a$2 \times 2$matrix$A = { \bigg [ } { a b } { \bigg ] }$ , the result is an eigenvalue of A, for all A.
:::

::: {.solution}
Assuming the opposite, we arrive at the absurd conclusion that $\sqrt { z }$is a polynomial in z; namely$p ( 0 , z , 1 , 0 ) ^ { 2 } = z$for all$z \in \mathbb { C }$Solution 2: Suppose p always evaluates to an eigenvalue of A. Then$q = \operatorname { t r } ( A ) - p = a + d - p$evaluates to the other eigenvalue, hence$$p q = \operatorname* { d e t } ( A ) = a d - b c .$$We claim that det(A) is an irreducible polynomial, and therefore either p or q must be constant, contradicting the eigenvalue property (note that q has the same property). One way to prove that$a d - b c$is irreducible is as follows. Since ad − bc is homogeneous quadratic, its only possible factorization is as a product of linear forms$\lambda \cdot \mu .$. Since no term of$a d - b c$is the square of a variable, none of the four variables occurs in both λ and$\mu .$Since none of the variables divides ad − bc, each of λ and$\mu$must have at least two terms, and hence exactly two terms. But this would force$\lambda \cdot \mu$ to have four terms.
:::
