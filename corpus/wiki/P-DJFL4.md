---
schema: qual/card@1
id: P-DJFL4
kind: problem
title: "Since 0 is an eigenvalue, there exists an eigenvector $\\vector v$ such\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Since 0 is an eigenvalue, there exists an eigenvector $\vector v$ such that $L\vector v = 0 \vector v = 0$.
But then $\vector v \in \ker(L)$, so $\dim\ker(L) \geq 1$.
Since $\ker(L) \neq 0$, $L$ can not be injective.

By the rank-nullity theorem, we must also have $5 = \dim\ker(L) + \dim \im (L)$.
But then $\dim \im (L) \leq 5 = \dim \RR^5$, so $L$ can not be surjective either.

## Part 2
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

## Part 3

If $L\vector x = \vector x$, then $\vector x$ is an eigenvector with eigenvalue $\lambda = 1$.
Since $1 \not\in \spec(L)$, such an $\vector x$ can not exist, so $L$ has only one fixed point: namely $\vector x = \vector 0$.


