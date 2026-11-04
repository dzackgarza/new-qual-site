---
schema: qual/card@1
id: E-HAT-4.2-4
kind: problem
title: "Homotopy of infinite wedge of spheres"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 4 (AT.txt 19340-19343) and correct as it stands, with one
    external citation that was checked against the source. The map r_k collapsing the other spheres to the
    common point is continuous because the diameters shrink, and the collapse construction for
    surjectivity of Phi is the standard one; both are right. The (n-1)-connectedness claim for n>=2 rests
    on Eda and Kawamura, Fundamenta Mathematicae 165 (2000) 17-28, Corollary 1.2, which I read: it states
    that for the n-dimensional Hawaiian earring H_n with n>=2, pi_n(H_n) is Z^omega and pi_i(H_n) is
    trivial for 1 <= i <= n-1. That is exactly the cited assertion, and it is stronger than what the
    exercise asks (the paper's pi_n is the full product, so Phi is in fact an isomorphism). Not checked:
    the proof of that corollary, which is the paper's. The n=1 case is only pi_0, correctly.

---

::: {.problem}
Let $X \subset \RR^{n+1}$ be the union of the infinite sequence of spheres $S_k^n$ of radius $1/k$ and center $(1/k, 0, \ldots, 0)$.
Show that $\pi_i(X) = 0$ for $i < n$ and construct a homomorphism from $\pi_n(X)$ onto $\prod_k \pi_n(S_k^n)$.
:::

::: {.solution}
For each $k$, let
$$
r_k:X\to S_k^n
$$
collapse every sphere $S_j^n$ with $j\ne k$ to the common tangent point. This is continuous because the diameters of the spheres tend to zero. Hence there is a homomorphism
$$
\Phi:\pi_n(X)\longrightarrow\prod_{k\ge1}\pi_n(S_k^n),
\qquad
\Phi([f])=([r_kf])_k.
$$

The shrinking union has the metric topology of the $n$-dimensional Hawaiian earring; cellular approximation for a CW complex does not apply to it. For $n\ge2$, [Eda and Kawamura, Corollary 1.2](https://people.math.rochester.edu/faculty/doug/otherpapers/eda-kawamura1.pdf) proves that this space is $(n-1)$-connected. For $n=1$, the required assertion concerns only $\pi_0$, and $X$ is path-connected. Therefore
$$
\boxed{\pi_i(X)=0\qquad(i<n).}
$$

To prove surjectivity of $\Phi$, choose arbitrary classes
$$
a_k\in\pi_n(S_k^n)\cong\ZZ.
$$
Choose pairwise disjoint closed $n$-balls $B_k\subset S^n$ whose diameters tend to zero and which accumulate only at one point $q$. Collapse the complement of the interiors of all $B_k$'s to the common basepoint of $X$. On each quotient
$$
B_k/\partial B_k\cong S^n
$$
map to $S_k^n$ by a representative of degree $a_k$. Since $\operatorname{diam}(S_k^n)\to0$, these maps fit continuously at the accumulation point $q$. The resulting map
$$
f:S^n\to X
$$
satisfies
$$
[r_kf]=a_k
$$
for every $k$. Thus
$$
\boxed{\Phi:\pi_n(X)\twoheadrightarrow\prod_k\pi_n(S_k^n).}
$$
:::
