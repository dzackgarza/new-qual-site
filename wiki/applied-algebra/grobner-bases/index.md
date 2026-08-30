---
title: Gröbner bases and varieties
order: 4
problems:
  topics:
  - Gröbner Bases
  - Ideals
  - Commutative Algebra
---

# Gröbner bases and varieties

## The algorithm

1. Fix a monomial order -- lex for elimination, graded reverse lex for speed.

2. Run Buchberger: for each pair, form the $S\dash$polynomial, reduce it against the current basis, and adjoin any nonzero remainder.

3. Stop when every $S\dash$polynomial reduces to zero.

Buchberger's criterion is that this terminating condition is equivalent to being a Gröbner basis, and termination follows from the ascending chain condition on monomial ideals, which is Dickson's lemma.

## What a Gröbner basis is for

- **Ideal membership.** $f\in I$ exactly when $f$ reduces to zero against a Gröbner basis, which is the only algorithmic test.

- **Elimination.** With lex order, $G\intersect k[x_{i+1},\dots,x_n]$ is a Gröbner basis of the elimination ideal, which is how a system is solved by back-substitution and how implicitization is done.

- **Dimension and degree** of a variety, read from the leading term ideal.

- **Deciding whether two ideals are equal,** by comparing reduced Gröbner bases, which are unique once the order is fixed.

## The dictionary

The Nullstellensatz makes the correspondence between ideals and varieties precise: $I(V(J)) = \sqrt J$ over an algebraically closed field.
So a geometric question becomes a radical membership question, and a radical membership question becomes a Gröbner basis computation by the Rabinowitsch trick.

Weak form: $V(J) = \emptyset$ exactly when $1\in J$, which is a single reduction to check.
