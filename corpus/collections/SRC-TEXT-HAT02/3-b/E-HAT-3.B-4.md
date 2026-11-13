---
schema: qual/card@1
id: E-HAT-3.B-4
kind: problem
title: "Cross product of fundamental classes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.B, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.B, Exercise 4; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.B Exercise 4, printed p. 280; the statement
    matches the print. The gap was the last step: the card asserted that "the cross product of the
    two standard local generators is the standard generator in dimension $m+n$; this follows directly
    from the relative Künneth theorem, or from the product orientation on Euclidean space", which is
    exactly the content. It is now computed over $\ZZ$ from the relative Künneth formula printed on
    p. 276 applied to the CW pairs $(D^m,S^{m-1})$ and $(D^n,S^{n-1})$, where only one group on the
    left survives and no Tor term occurs, so the cross product is an isomorphism $\ZZ\otimes\ZZ\to\ZZ$
    on the top group; the passage to an arbitrary coefficient ring $R$ is by naturality in the
    coefficients, not by a second Künneth argument. Also supplied: the definition of fundamental class
    and the existence of $[M]$ for closed $R$-orientable $M$ from Theorem 3.26(a) (p. 236), the
    equality $(M-x)\times N\cup M\times(N-y)=M\times N-\{(x,y)\}$, the excision hypotheses for the
    inclusion of $(B_x\times B_y,B_x\times B_y-\{(x,y)\})$ into $(M\times N,M\times N-\{(x,y)\})$ with
    the excised closed set named, and the role of the charts $u,v$ in making $\iota_m\otimes\iota_n$
    correspond to $[M]_x\otimes[N]_y$. No published solution of this exercise is in the retained
    sets — Sam has no §3.B, Stanford 215C solution2 covers §3.B exercises 1 and 3 only, Li stops at
    §3.3, the Math 538 sheets are §3.3 only — recorded in COMPLAINTS.md.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 4 of §3.B on printed p. 280,
    identical in the current online text, and the card states it word for word. The obligation that
    #123 records is unchanged and stays open: no published solution of this exercise was located.
    Searched without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C
    Solution Sets 1--5, the UCR Math 205B help file, May, Bredon, Maxim's Math 752 notes) and in
    Hatcher's text and errata; the Math 538 set held here is a scan with no text layer and opens at
    §3.2 (Borsuk--Ulam), not at §3.B.
---

::: {.problem}
Show that the cross product of fundamental classes for closed $\RR$-orientable manifolds $M$ and $N$ is a fundamental class for $M \times N$.
:::

::: {.solution}
Let $M^m$ and $N^n$ be closed $R$-orientable manifolds. A fundamental class for a closed $R$-orientable $n$-manifold is an element of $H_n(M;R)$ whose image in $H_n(M,M-x;R)$ is a generator of that free rank-one $R$-module for every $x\in M$; such a class exists for closed $R$-orientable $M$ by Theorem 3.26(a) (p. 236), where the definition is also given. Choose fundamental classes
$$
[M]\in H_m(M;R),
\qquad
[N]\in H_n(N;R),
$$
and write $[M]_x$ and $[N]_y$ for their images in $H_m(M,M-x;R)$ and $H_n(N,N-y;R)$.

Throughout, the cross product for a pair of pairs is
$$
H_k(X,A;R)\otimes H_\ell(Y,B;R)\longrightarrow H_{k+\ell}\bigl(X\times Y,\ A\times Y\cup X\times B;R\bigr),
$$
and it is natural in maps of pairs in each variable.

*The local class of $[M]\times[N]$.* Fix $(x,y)\in M\times N$. Since $(a,b)$ lies in $(M-x)\times N$ exactly when $a\neq x$, and in $M\times(N-y)$ exactly when $b\neq y$,
$$
(M-x)\times N\ \cup\ M\times(N-y)=M\times N-\{(x,y)\}.
$$
Naturality, applied to the identity map viewed as a map of pairs $(M,\emptyset)\times(N,\emptyset)\to(M,M-x)\times(N,N-y)$, says that the image of $[M]\times[N]$ in $H_{m+n}(M\times N,M\times N-\{(x,y)\};R)$ is the cross product
$$
[M]_x\times[N]_y\in H_{m+n}\bigl(M\times N,\ (M-x)\times N\cup M\times(N-y);R\bigr).
$$

*Reduction to Euclidean space.* Choose charts, that is, homeomorphisms of pairs $u:(D^m,S^{m-1})\to(B_x,B_x-x)$ and $v:(D^n,S^{n-1})\to(B_y,B_y-y)$ onto open balls about $x$ and $y$, and let $\iota_m$ and $\iota_n$ be the generators of $H_m(D^m,S^{m-1};R)$ and $H_n(D^n,S^{n-1};R)$ that $u_*$ and $v_*$ carry to $[M]_x$ and $[N]_y$. Naturality of the cross product on $u\times v$ says that $u_*\otimes v_*$ carries $\iota_m\otimes\iota_n$ to the cross product of the two ball classes. The inclusion of pairs
$$
\bigl(B_x\times B_y,\ B_x\times B_y-\{(x,y)\}\bigr)\longrightarrow\bigl(M\times N,\ M\times N-\{(x,y)\}\bigr)
$$
is an excision, so it is an isomorphism on $H_{m+n}(-;R)$: the excised set $Z=M\times N-(B_x\times B_y)$ is closed and lies in the open set $M\times N-\{(x,y)\}$, whose complement in $M\times N$ is the single point $(x,y)\in B_x\times B_y$. Hence $[M]_x\times[N]_y$ is an isomorphism's image of $u_*\iota_m\times v_*\iota_n$, and is a generator exactly when $\iota_m\times\iota_n$ is one.

*The Euclidean computation.* Take first $R=\ZZ$. The relative Künneth formula for the CW pairs $(D^m,S^{m-1})$ and $(D^n,S^{n-1})$, printed on p. 276, is the split exact sequence
$$
0\to\bigoplus_i H_i(D^m,S^{m-1})\otimes H_{m+n-i}(D^n,S^{n-1})
\to H_{m+n}\bigl(D^m\times D^n,\ (S^{m-1}\times D^n)\cup(D^m\times S^{n-1})\bigr)
\to\bigoplus_i\operatorname{Tor}\bigl(H_i(D^m,S^{m-1}),H_{m+n-i-1}(D^n,S^{n-1})\bigr)\to0,
$$
and the left-hand map is induced by the cross product. Here $H_i(D^m,S^{m-1})$ is $\ZZ$ for $i=m$ and $0$ otherwise, and likewise for $n$; so the left-hand group is $\ZZ\otimes\ZZ$ in degree $m+n$, every Tor group vanishes, and the cross product $\ZZ\otimes\ZZ\to H_{m+n}(\text{product pair})\cong\ZZ$ is an isomorphism. Therefore $\iota_m\times\iota_n$ is a generator over $\ZZ$.

For an arbitrary coefficient ring $R$, use the coefficient homomorphism $\ZZ\to R$: the cross product is natural in the coefficients, so $\iota_m\otimes\iota_n$ over $R$ is the image of the integral class, and $H_m(D^m,S^{m-1};R)\cong R$, $H_n(D^n,S^{n-1};R)\cong R$ are generated by the images of $\iota_m,\iota_n$, since the universal coefficient sequence of Corollary 3A.4 (p. 264) degenerates in these degrees. The image of a generator of a free rank-one $\ZZ$-module generates the free rank-one $R$-module, so $\iota_m\times\iota_n$ is a generator over $R$ too.

*Conclusion.* For every $(x,y)\in M\times N$ the image of $[M]\times[N]$ in the local group $H_{m+n}(M\times N,M\times N-\{(x,y)\};R)$ is a generator. By the definition recalled above, $[M]\times[N]$ is a fundamental class for the closed $R$-orientable $(m+n)$-manifold $M\times N$.
:::
