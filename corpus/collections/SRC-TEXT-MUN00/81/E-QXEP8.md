---
schema: qual/card@1
id: E-QXEP8
kind: problem
title: Lens spaces
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
audit:
- event: source-corrected
  by: Codex
  date: 2026-10-31
  note: The printed homeomorphism criterion omits orientation reversal. Complex conjugation in the second coordinate gives L(n,k) homeomorphic to L(n,-k), so both congruences require a possible minus sign.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 81 Exercise 5, printed p. 493. The lens space L(n,k) as the quotient of S^3 by the cyclic action, regular with group Z/n, and its fundamental group. Checked against Theorem 81.5 and the definition of a free action. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Citations added at every step: Theorem 59.3 (printed p. 369) for S^3 simply connected, Exercise 4 of §81 (printed p. 493) for a finite fixed-point-free action being properly discontinuous, Theorem 81.5 (printed p. 490) for the quotient map being a regular covering map with the acting group as its group of covering transformations, Corollary 81.4 (printed p. 489) for the group of covering transformations of a simply connected cover being the fundamental group of the base, Theorem 26.5 (printed p. 166) for compactness, Theorem 17.8 (printed p. 99) for a finite set in a Hausdorff space being closed, Theorem 32.3 (printed p. 202) for a compact Hausdorff space being normal, and the Definition of an m-manifold (printed p. 225). Corrected: part (b) called S^3 -> L(n,k) a regular covering and identified its group of covering transformations with G without deriving either from Theorem 81.5, which needs the action to be properly discontinuous; both are now derived, the second from Exercise 4 of §81. Corrected: part (c) asserted in one clause that "finite group quotients preserve Hausdorffness and second countability"; both are now proved, the first by averaging a pair of disjoint open sets over the finite group in a normal space, the second by taking the images of a countable basis under the open quotient map. What the certificate does not cover: the bracketed assertion printed with the exercise, that L(n,k) and L(n',k') are homeomorphic exactly under the stated congruences, is not proved here; part (b) proves only the necessary condition n = n'. The statement's correction of that bracket is the event above.
---

::: {.exercise}

Consider $S^3$ as the space of all pairs of complex numbers $(z_1, z_2)$ satisfying the equation $\abs{z_1}^2 + \abs{z_2}^2 = 1$.
Given relatively prime positive integers $n$ and $k$, define $h: S^3 \to S^3$ by the equation

$$
h(z_1, z_2) = (z_1 e^{2\pi i/n}, z_2 e^{2\pi i k/n}).
$$

(a) Show that $h$ generates a subgroup $G$ of the homeomorphism group of $S^3$ that is cyclic of order $n$, and that only the identity element of $G$ has a fixed point.
The orbit space $S^3/G$ is called the lens space $L(n, k)$.

(b) Show that if $L(n, k)$ and $L(n', k')$ are homeomorphic, then $n = n'$.
[It is a theorem that $L(n, k)$ and $L(n', k')$ are homeomorphic if and only if $n = n'$ and either $k \equiv \pm k' \pmod{n}$ or $kk' \equiv \pm 1 \pmod{n}$. The proof is decidedly nontrivial.]

(c) Show that $L(n, k)$ is a compact 3-manifold.

:::

::: {.solution}

(a) The map
$$
h(z_1,z_2)=(e^{2\pi i/n}z_1,e^{2\pi ik/n}z_2)
$$
is the restriction to $S^3$ of a bijective complex-linear map of $\CC^2$ that preserves the norm, so it is a homeomorphism of $S^3$ with inverse obtained by replacing the exponents by their negatives. Also $h^n=1$.

Suppose $h^j$ fixes $(z_1,z_2)\in S^3$, with $0<j<n$. At least one coordinate is nonzero. If $z_1\ne0$, then
$$
e^{2\pi ij/n}=1,
$$
forcing $n\mid j$, impossible. If $z_1=0$, then $z_2\ne0$ and
$$
e^{2\pi i k j/n}=1.
$$
Since $\gcd(k,n)=1$, again $n\mid j$, impossible. Thus no nonidentity power has a fixed point. In particular $h$ has exact order $n$, so
$$
G=\langle h\rangle\cong\ZZ/n.
$$

(b) The action of the finite group $G$ on the Hausdorff space $S^3$ is fixed-point free by part (a), so it is properly discontinuous by Exercise 4 of §81 (printed p. 493). By Theorem 81.5 (printed p. 490) the quotient map
$$
\pi:S^3\longrightarrow L(n,k)=S^3/G
$$
is then a regular covering map, and $G$ is its group of covering transformations; it is an $n$-sheeted covering because $G$ has $n$ elements, so every fibre has $n$ points. Since $S^3$ is simply connected (Theorem 59.3, printed p. 369), it is the universal covering space of $L(n,k)$, and Corollary 81.4 (printed p. 489) identifies its group of covering transformations with the fundamental group of the base:
$$
\pi_1(L(n,k))\cong G\cong\ZZ/n.
$$
A homeomorphism $L(n,k)\cong L(n',k')$ induces an isomorphism of fundamental groups, so
$$
\ZZ/n\cong\ZZ/n'.
$$
Finite cyclic groups are isomorphic only when their orders agree. Hence $n=n'$.

(c) The sphere $S^3$ is compact, so its continuous image $L(n,k)$ under the quotient map is compact (Theorem 26.5, printed p. 166).

Each point of $L(n,k)$ has a neighbourhood homeomorphic to an open subset of $\RR^3$. Indeed, let $u\in L(n,k)$ and choose $y\in\pi^{-1}(u)$. The open hemisphere $W=\{z\in S^3\mid z\cdot y>0\}$ is mapped homeomorphically onto the open unit ball of the hyperplane $y^\perp$ by orthogonal projection, so $S^3$ is a 3-manifold in the sense of the Definition (printed p. 225); and since $\pi$ is a covering map by part (b), $u$ has a neighbourhood evenly covered by $\pi$, over which $\pi$ restricts to a homeomorphism. Hence $u$ has a neighbourhood homeomorphic to an open subset of $\RR^3$.

$L(n,k)$ is Hausdorff. Let $u\ne v$ in $L(n,k)$ and choose $x,y\in S^3$ with $\pi(x)=u$, $\pi(y)=v$. The orbits $Gx$ and $Gy$ are finite, hence closed in the Hausdorff space $S^3$ (Theorem 17.8, printed p. 99), and they are disjoint. Each orbit is invariant under $G$. Since $S^3$, being compact and Hausdorff, is normal (Theorem 32.3, printed p. 202), there are disjoint open sets $U_0\supseteq Gx$ and $V_0\supseteq Gy$. Put
$$
U=\bigcap_{g\in G}g(U_0),\qquad V=\bigcap_{g\in G}g(V_0).
$$
These are open, $G$-invariant, contain $Gx$ and $Gy$ respectively (each $g(U_0)$ contains $g(Gx)=Gx$), and are disjoint: a point $z$ of $U\cap V$ would give $g^{-1}(z)\in U_0\cap V_0=\varnothing$ for every $g$. The quotient map $\pi$ is open, because $\pi^{-1}\pi(U_0)=\bigcup_{g\in G}g(U_0)$ is open for every open $U_0$; so $\pi(U)$ and $\pi(V)$ are disjoint open neighbourhoods of $u$ and $v$. Hence $L(n,k)$ is Hausdorff.

$L(n,k)$ has a countable basis. Let $\{B_m\}$ be a countable basis for $S^3$; then $\{\pi(B_m)\}$ is countable, consists of open sets because $\pi$ is open, and is a basis: given $u$ and an open $O\ni u$, choose $x\in\pi^{-1}(u)$ and $m$ with $x\in B_m\subseteq\pi^{-1}(O)$, so that $u\in\pi(B_m)\subseteq O$.

Therefore $L(n,k)$ is a compact Hausdorff space with a countable basis, each point of which has a neighbourhood homeomorphic to an open subset of $\RR^3$: it is a compact 3-manifold (Definition, printed p. 225).

:::
