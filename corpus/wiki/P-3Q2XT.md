---
schema: qual/card@1
id: P-3Q2XT
kind: problem
title: Euclidean domains are UFDs; a UFD need not be Euclidean
classification:
  areas:
  - algebra
  topics:
  - euclidean-domains
  - factorization
  - principal-ideal-domains
relations: []
review: draft
solved: true
---
a.
Define a *Euclidean domain*.

b.
Define a *unique factorization domain*.

c.
Is a Euclidean domain an UFD? 
Give either a proof or a counterexample with justification.

d.
Is a UFD a Euclidean domain?
Give either a proof or a counterexample with justification.


:::{.solution}
\envlist

- $R$ is Euclidean iff it admits a Euclidean algorithm: there is a degree function $f: R\to \ZZ_{\geq 0}$ such that for all $a,b\in R$, there exist $q, r\in R$ such that $a = bq + r$ where $f(r) <f(b)$ or $r=0$.

- $R$ is a UFD iff every nonzero $r\in R$ can be written as $r = u \prod_{i=1}^n p_i$ with $n\geq 0$, $u\in R\units$, and $p_i$ irreducible.
  This is unique up to associates of the $p_i$ and reordering.

- Euclidean implies UFD:
  - Euclidean implies PID:
    - If $I \in \Id(R)$ one can use the degree function to find any $b \in I$ where $f(b)$ is minimal.
    - Then $I = \gens{b}$, since if $a\in I$ one can write $a = bq + r$ and use that $a-bq \in I \implies r\in I$.
    - But by minimality, we can't have $f(r)<f(b)$, so $r=0$ and $b \divides a$, so $a\in \gens{b}$.
    
  - PID implies UFD:
    - Existence: a PID is Noetherian, and the ascending chain condition forces every nonzero nonunit to factor into finitely many irreducibles.
    Since irreducible implies prime in a PID, this is a factorization into primes.
    - Supposing $x = u_p \prod_{i=1}^m p_i = u_q \prod_{i=1}^n q_i$, use that $p_1$ divides the LHS and so $p_1$ divides the RHS.
    WLOG, $p_1\divides q_1$, so $q_1 = u_1 p_1$ for $u\in R\units$, so $x = u_q u_1 p_1 \prod_{i=2}^m q_i$ by rewriting a term on the RHS.
    - Note that this makes $p_1, q_1$ associates.
    - Continuing up to $m$, we get
  \[
  x 
  &= u_p \prod_{i=1}^m p_i \\
  &= 
  u_q \prod_{i=1}^m u_i p_i \prod_{k=m+1}^n q_i \\
  \implies 
  u_p 
  &= u_q \prod_{i=1}^m u_i \prod_{k=m+1}^n q_i \\
  \tilde u 
  &= \prod_{k=m+1}^n q_i
  ,\]
    where we've moved all units to the LHS.
    This makes $p_i, q_i$ associates for $i\leq m$.
    - But primes aren't units and the product of nontrivial primes can't be a unit, so the right-hand side product must be empty.
    - So $m=n$ and all $p_i, q_i$ are associate, QED.

- UFD does not imply Euclidean:
  - It suffices to find a UFD that is not a PID.
  - Take $R \da \CC[x, y]$, which is a UFD by the usual factorization of polynomials.
  It is not a PID, since $\gens{x, y}$ is not principal.


:::



