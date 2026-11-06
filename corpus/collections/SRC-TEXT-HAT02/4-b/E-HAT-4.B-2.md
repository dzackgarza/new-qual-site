---
schema: qual/card@1
id: E-HAT-4.B-2
kind: problem
title: "Fiber bundles $S^k \\to S^m \\to S^n$ and the Hopf invariant"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.B, Exercise 2 and its hint; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
Show that if $S^k \to S^m \xrightarrow{p} S^n$ is a fiber bundle, then $m = 2n-1$, $k = n-1$, and, when $n > 1$, $H(p) = \pm 1$.
[Show that $C_p$ is a manifold and apply Poincaré duality.]
:::

::: {.solution}
Suppose
$$
S^k\longrightarrow S^m\xrightarrow{p}S^n
$$
is a fiber bundle.

First compare dimensions. Since a fiber bundle is locally a product, the total space is locally modeled on
$$
\RR^n\times\RR^k,
$$
so
$$
m=n+k.
\tag{1}
$$

Assume first that $n>1$. Then the base is simply connected. The fiber cannot be $S^0$, since a bundle with discrete two-point fiber over a simply connected base is the trivial double cover, whose total space is disconnected. Hence $k>0$, and by (1), $m>n$ and $m>k$.

The long exact homotopy sequence of the bundle (Theorem 4.41, p. 376) contains
$$
\pi_n(S^m)\longrightarrow\pi_n(S^n)
\longrightarrow\pi_{n-1}(S^k).
$$
Since $m>n$, the first group is zero (Corollary 4.9, p. 349), while
$$
\pi_n(S^n)\cong\ZZ
$$
(Corollary 4.25, p. 361). Exactness makes the map $\ZZ\to\pi_{n-1}(S^k)$ injective, so $\pi_{n-1}(S^k)\ne0$; but $\pi_i(S^k)=0$ whenever $i<k$ (Corollary 4.9, p. 349), forcing
$$
k\le n-1.
\tag{2}
$$
On the other hand, if $k<n-1$, then by Corollary 4.9 (p. 349) the segment
$$
\pi_{k+1}(S^n)\longrightarrow\pi_k(S^k)
\longrightarrow\pi_k(S^m)
$$
of the same sequence would be
$$
0\longrightarrow\ZZ\longrightarrow0
$$
(with $\pi_k(S^k)\cong\ZZ$ by Corollary 4.25, p. 361, and $\pi_k(S^m)=0$ because $k<m$); exactness would make the middle group a quotient of $0$, a contradiction. Hence
$$
k\ge n-1.
\tag{3}
$$
From (2) and (3),
$$
\boxed{k=n-1},
$$
and then (1) gives
$$
\boxed{m=2n-1}.
$$
For $n=1$, the same dimension relation $m=1+k$ and the segment $\pi_1(S^m)\to\pi_1(S^1)\to\pi_0(S^k)$ force $k=0$: if $k>0$ then $\pi_0(S^k)=0$, so $\pi_1(S^m)\to\pi_1(S^1)=\ZZ$ would be onto, whereas $m=1+k\ge2$ gives $\pi_1(S^m)=0$. Hence $m=1$, which is the exceptional double-cover case $S^0\to S^1\to S^1$.

Now suppose $n>1$, so the bundle has the form
$$
S^{n-1}\longrightarrow S^{2n-1}\xrightarrow{p}S^n.
$$
Consider the mapping cone
$$
C_p=S^n\cup_p CS^{2n-1}.
$$
This is a closed $2n$-manifold. Indeed, away from the copy of $S^n$ and the cone point this is clear. Near a point of the copy of $S^n$, choose a bundle trivialization over a small ball $U\subset S^n$. Coning each fiber $S^{n-1}$ produces a disk $D^n$, so a neighborhood is
$$
U\times D^n\cong\RR^{2n}.
$$
A neighborhood of the cone point is the cone on $S^{2n-1}$, hence a $2n$-disk. It is orientable: $C_p$ is the one-point compactification of the interior of the associated disk bundle $D^n\to D(E)\to S^n$, and the tangent bundle of $D(E)$ is $\pi^*TS^n\oplus\pi^*\xi$ for the rank $n$ vector bundle $\xi$ of the bundle; since $H^1(S^n;\ZZ_2)=0$ for $n>1$, every vector bundle over $S^n$ has $w_1(\xi)=0$, so $D(E)$ and hence $C_p$ are orientable.

The cellular cohomology of the mapping cone has
$$
H^n(C_p;\ZZ)\cong\ZZ,
\qquad
H^{2n}(C_p;\ZZ)\cong\ZZ.
$$
Let $\alpha$ and $\beta$ be generators in these degrees. By definition of the Hopf invariant,
$$
\alpha^2=H(p)\,\beta.
$$
Since $C_p$ is a closed connected orientable $2n$-manifold, Poincaré duality (Theorem 3.30, p. 241) makes the cup product pairing
$$
H^n(C_p;\ZZ)\times H^n(C_p;\ZZ)
\longrightarrow H^{2n}(C_p;\ZZ)\cong\ZZ
$$
nonsingular, in the form of Corollary 3.39 (p. 250): an element of $H^n$ generates an infinite cyclic summand if and only if it pairs to a generator with some element of the complementary degree. Write $\alpha^2=H(p)\,\gamma$ with $\gamma$ a generator of $H^{2n}(C_p;\ZZ)\cong\ZZ$. Since $H^n(C_p;\ZZ)\cong\ZZ=\ZZ\langle\alpha\rangle$, every element of $H^n$ is $\beta=m\alpha$, so $\alpha\smile\beta=mH(p)\,\gamma$; Corollary 3.39 supplies such a $\beta$ for which this is a generator of $H^{2n}$, forcing $mH(p)=\pm1$ and hence
$$
\boxed{H(p)=\pm1}.
$$

Thus every such sphere bundle satisfies
$$
\boxed{m=2n-1,\qquad k=n-1,}
$$
and for $n>1$ its projection has Hopf invariant $\pm1$.
:::
