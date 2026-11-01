---
schema: qual/card@1
id: E-HAT-4.2-28
kind: problem
title: "$\\ZZ_p \\times \\ZZ_p$ cannot act freely on spheres"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 28; the stored statement matches.
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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 28 (AT.txt 19430-19435) and repaired. The statement
    quantifies over any sphere S^n and the proof opened "Suppose first n>1", then handled n=1, and
    never covered S^0; the case is now disposed of in one sentence (a free action of a group of order
    p^2 >= 4 on two points is impossible). Verified as correct and left unchanged: the K(Z_p x Z_p,1)
    construction with one (n+1)-cell, the bound dim H^{n+1}(K;Z_p) <= 1, the identification
    K(Z_p x Z_p,1) = K(Z_p,1) x K(Z_p,1), and the one-dimensional degree-d part of each factor's
    cohomology (Z_p[u] for p=2; Lambda(u) tensor Z_p[v] for odd p), which gives d+1 = n+2 > 1. The n=1
    case rests on "a finite free action on S^1 is cyclic"; that classical statement is not in AT.txt,
    though it follows from covering space theory, and the card records it as such rather than proving
    it.

---

::: {.problem}
Show that the group $\ZZ_p \times \ZZ_p$ with $p$ prime cannot act freely on any sphere $S^n$, by filling in details of the following argument. Such an action would define a covering space $S^n \to M$ with $M$ a closed manifold. When $n > 1$, build a $K(\ZZ_p \times \ZZ_p, 1)$ from $M$ by attaching a single $(n + 1)$-cell and then cells of higher dimension. Deduce that $H^{n+1}(K(\ZZ_p \times \ZZ_p, 1); \ZZ_p)$ is $\ZZ_p$ or 0, a contradiction. (The case $n = 1$ is more elementary.)
:::

::: {.solution}
Let
$$
G=\ZZ_p\times\ZZ_p.
$$
For $n=0$ there is no free action at all: $G$ has order $p^2\ge4$ while $S^0$ has only two points. So assume $n\ge1$ and suppose first that $n>1$ and that $G$ acts freely on $S^n$. Then
$$
S^n\longrightarrow M=S^n/G
$$
is the universal covering of a closed $n$-manifold, with
$$
\pi_1(M)=G,
\qquad
\pi_i(M)=0\quad(1<i<n),
\qquad
\pi_n(M)\cong\ZZ.
$$
Attach one $(n+1)$-cell along a generator of $\pi_n(M)$, then cells of dimensions at least $n+2$ to kill all remaining higher homotopy groups. This produces a $K(G,1)$.

Up through dimension $n+1$ this CW complex has exactly one new $(n+1)$-cell beyond the $n$-dimensional manifold $M$. With $\FF_p$-coefficients the cochain group in degree $n+1$ is therefore one-dimensional. Consequently
$$
\dim_{\FF_p}H^{n+1}(K(G,1);\FF_p)\le1.
$$

But
$$
K(G,1)\simeq K(\ZZ_p,1)\times K(\ZZ_p,1).
$$
For $p=2$,
$$
H^*(K(\ZZ_2,1);\FF_2)\cong\FF_2[u],\quad \gradeddegree{u}=1,
$$
and for odd $p$,
$$
H^*(K(\ZZ_p,1);\FF_p)
\cong\Lambda(u)\otimes\FF_p[v],
\quad \gradeddegree{u}=1,\ \gradeddegree{v}=2.
$$
In either case the Künneth formula shows that the degree-$d$ cohomology of the product has dimension $d+1$. In particular
$$
\dim H^{n+1}(K(G,1);\FF_p)=n+2>1,
$$
a contradiction.

If $n=1$, any finite group acting freely on $S^1$ is cyclic: an orientation-reversing homeomorphism of $S^1$ has a fixed point, so a finite free action is orientation-preserving and conjugate to a rotation action. Since $\ZZ_p\times\ZZ_p$ is not cyclic, it cannot act freely on $S^1$ either.

Thus
$$
\boxed{\ZZ_p\times\ZZ_p\text{ acts freely on no sphere}.}
$$
:::
