---
schema: qual/card@1
id: P-GSFRX
kind: problem
title: "Since all eigenvalues are roots of the minimal polynomial and complex\u2026"
classification:
  areas:
  - algebra
  topics:
  - minimal-and-characteristic-polynomials
  - eigenvalues-and-eigenvectors
relations: []
review: draft
---

Since all eigenvalues are roots of the minimal polynomial and complex roots occur in conjugate pairs, we must have
$$
\spec(L) = \theset{0, 1 \pm i, 1\pm 2i}.
$$

Moreover, since this is a $5\times 5$ matrix and we have 5 eigenvalues, this is all of them, and we have the characteristic polynomial
$$
\chi_L(x) = x(x^2-2x+2)(x^2 - 2x + 5) \in \RR[x]
$$

Since the minimal polynomial $p_L(x)$ must divide the characteristic polynomial and have every eigenvalue as a root, this forces
$$
p_L(x) = \chi_L(x).
$$
