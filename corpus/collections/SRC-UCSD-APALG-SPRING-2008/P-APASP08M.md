---
schema: qual/card@1
id: P-APASP08M
kind: problem
title: "Construction of a matrix group via Young representation, invariant ring, and Hilbert series"
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Representation Theory
  - Gröbner Bases
relations: []
review: draft
---

::: problem
Construct the group $G$ of $3 \times 3$ matrices by applying the Young natural representation indexed by $[2,1,1]$ to the permutations of $S_4$.

(1) Compute the Hilbert series $F_{\mathbb{R}[x]}(q)$ of the ring of $G$-invariants.

(2) Rewrite it in the form $$F_{\mathbb{R}[x]}(q) = \frac{1 + q^d}{(1 - q^{d_1})(1 - q^{d_2})(1 - q^{d_3})}.$$

(3) Calculate the first 10 terms of this series.

(4) Construct three homogeneous $G$-invariants of degrees $d_1, d_2, d_3$.

(5) Compute the Gröbner basis of the ideal $(I_1, I_2, I_3)$.

(6) Verify that $I_1, I_2, I_3$ are a system of parameters by checking that the quotient $\mathbb{Q}[x_1, x_2, x_3]/(I_1, I_2, I_3)$ has finite dimension.
If not, go back to step (4).

(7) Construct a $G$-invariant $\eta$ of degree $d$.

(8) Verify that it is not a polynomial in $I_1, I_2, I_3$ by computing the polynomial $Q$ such that $Q(\eta, I_1, I_2, I_3) = 0$.

(9) Based on your previous results, show that step (8) is not needed.

(10) Compute the Jacobian of $I_1, I_2, I_3$ and construct its linear factors.

(11) Assuming that there is a reflection group $G'$ that also leaves $I_1, I_2, I_3$ invariant, you could have predicted the number of these linear factors.
Why?
:::
