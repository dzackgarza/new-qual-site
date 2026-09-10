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
[It is a theorem that $L(n, k)$ and $L(n', k')$ are homeomorphic if and only if $n = n'$ and either $k \equiv k' \pmod{n}$ or $kk' \equiv 1 \pmod{n}$. The proof is decidedly nontrivial.]

(c) Show that $L(n, k)$ is a compact 3-manifold.
:::

::: {.solution}
(a) The map
\[
h(z_1,z_2)=(e^{2\pi i/n}z_1,e^{2\pi ik/n}z_2)
\]
is a homeomorphism of \(S^3\), with inverse obtained by replacing the exponents by their negatives. Also \(h^n=1\).

Suppose \(h^j\) fixes \((z_1,z_2)\in S^3\), with \(0<j<n\). At least one coordinate is nonzero. If \(z_1\ne0\), then
\[
e^{2\pi ij/n}=1,
\]
forcing \(n\mid j\), impossible. If \(z_1=0\), then \(z_2\ne0\) and
\[
e^{2\pi i k j/n}=1.
\]
Since \(\gcd(k,n)=1\), again \(n\mid j\), impossible. Thus no nonidentity power has a fixed point. In particular \(h\) has exact order \(n\), so
\[
G=\langle h\rangle\cong\mathbb Z/n.
\]

(b) The free finite action makes
\[
S^3\longrightarrow L(n,k)=S^3/G
\]
a regular \(n\)-sheeted covering. Since \(S^3\) is simply connected, it is the universal cover, and its group of covering transformations is \(G\). Therefore
\[
\pi_1(L(n,k))\cong G\cong\mathbb Z/n.
\]
A homeomorphism \(L(n,k)\cong L(n',k')\) induces an isomorphism of fundamental groups, so
\[
\mathbb Z/n\cong\mathbb Z/n'.
\]
Finite cyclic groups are isomorphic only when their orders agree. Hence \(n=n'\).

(c) The sphere \(S^3\) is compact. Its continuous image under the quotient map is therefore compact. Because the action is free and \(G\) is finite, for every \(x\in S^3\) one can choose a small open ball \(U\) such that
\[
gU\cap U=\varnothing\qquad(g\ne1).
\]
The quotient map restricts to a homeomorphism from \(U\) onto its image. Thus every point of \(L(n,k)\) has a neighborhood homeomorphic to an open subset of \(S^3\), hence to an open subset of \(\mathbb R^3\). The quotient is Hausdorff and second countable (finite group quotients preserve these properties). Therefore \(L(n,k)\) is a compact 3-manifold.
:::
