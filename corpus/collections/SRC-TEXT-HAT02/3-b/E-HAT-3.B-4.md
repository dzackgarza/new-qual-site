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
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    The published solution of the exercise has now been located and read: C. Kottke, *Math 2420
    Problem Set 3 solutions* (Brown University, Spring 2012),
    `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf`, 3 pp., sha256
    e84fd60496037db45bb18457b7c922233f5912a41b5d067112ba75a8211c22a7, Problem 1, printed p. 1. Its
    Problem 1 states both that $M$ and $N$ are orientable if and only if $M\times N$ is and that
    $\alpha\times\beta$ is a fundamental class when $\alpha,\beta$ are, and proves them: the local
    cross product $H_m(M|x)\otimes H_n(N|y)\to H_{m+n}(M\times N|x\times y)$ is an isomorphism by the
    relative Künneth theorem, for $R=\ZZ$ at a point and after replacing points by closed balls; the
    product of orientations is an orientation of $M\times N$; and for closed manifolds the Künneth
    formula for $M\times N$ leaves $H_m(M)\otimes H_n(N)$. So this is a complete published solution
    of Exercise 4 of §3.B, printed p. 280, which is the second of its two statements. Checked against
    Hatcher: the printed statement on p. 280, the definition of fundamental class and Theorem 3.26(a)
    on p. 236, the relative Künneth statement on p. 276, the relative singular chains' freeness on
    p. 261, the universal coefficient theorem for homology on p. 264, the topological Künneth theorem
    on p. 275 and Corollary A.12 on p. 529. This supersedes the preceding note's closing sentence,
    which said no published solution was in the retained sets; it was not, and the owner supplied it.
- event: solution-written
  by: claude
  date: 2026-11-13
  note: >-
    The solution is now the transcription of that published solution, with the page cited in the
    opening sentence of the solution as well as here. Written out from the source: the local cross
    product and the identity of complements, the integral case at a point by the relative Künneth
    formula on the ball pairs, the multiplication of orientations with the compatibility condition
    carried by products of closed balls, the integral computation $H_{m+n}(M\times N)\cong
    H_m(M)\otimes H_n(N)$ for closed manifolds, and the two routes the source gives to the
    fundamental class, of which the second --- $(\alpha\times\beta)_{(x,y)}=\alpha_x\times\beta_y$
    together with Hatcher's local definition on p. 236 --- is the one used to conclude. Filled, since
    the source leaves it to one sentence: the passage from $R=\ZZ$ to an arbitrary commutative ring,
    done on the card from Theorem 3A.3 (printed p. 264) applied to the free complex $C_*(M,M-x)$,
    which gives $H_m(M|x;R)\cong\ZZ\otimes_\ZZ R$ with the generator $\zeta_x\otimes1$, together with
    Proposition 3B.1 and the tensor identification used on p. 276 for the coefficient change. The
    earlier proof is replaced, not kept alongside: it reached the same conclusion through charts and
    excision of the pair $(M\times N,M\times N-\{(x,y)\})$, and its ring step, on the ball pair, was
    the same argument as the fill made here. Not rewritten into `pf` steps; the source's paragraph
    order is kept so the transcription can be checked against p. 1.
---

::: {.problem}
Show that the cross product of fundamental classes for closed $\RR$-orientable manifolds $M$ and $N$ is a fundamental class for $M \times N$.
:::

::: {.solution}
The proof below is **C. Kottke, *Math 2420 Problem Set 3 solutions*, Brown University, Spring 2012, Problem 1, printed p. 1** (`tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf`), transcribed. That problem proves two things: that $M$ and $N$ are orientable if and only if $M\times N$ is, and that $\alpha\times\beta$ is a fundamental class for $M\times N$. The exercise here is the second, which is Exercise 4 of §3.B, printed p. 280. The one step the source leaves is its passage from $R=\ZZ$ to an arbitrary commutative ring, made in a single sentence --- "it still holds that the product of generators is a generator (i.e. $\pm1\times1=\pm1$ still holds in (1))" --- and it is filled in *The coefficient ring* below from Hatcher's universal coefficient theorem, printed p. 264.

Let $R$ be a commutative ring with identity, let $M^m$ and $N^n$ be closed $R$-orientable manifolds with fundamental classes $\alpha\in H_m(M;R)$ and $\beta\in H_n(N;R)$, and write $\alpha_x$, $\beta_y$ for their images in the local groups at $x\in M$ and $y\in N$. Write $H_m(M\,||\,x;R)=H_m(M,M-x;R)$, Hatcher's notation for the local group (printed p. 234).

*The local cross product.* Since
$$
(M-x)\times N\ \cup\ M\times(N-y)=M\times N-\{(x,y)\},
$$
the relative cross product of §3.B (printed p. 276) is a map
$$
\times:\ H_m(M\,||\,x;R)\otimes_R H_n(N\,||\,y;R)\longrightarrow H_{m+n}\bigl(M\times N\,||\,(x,y);R\bigr).
$$

*The integral case at a point.* Take $R=\ZZ$ and excise the charts, so that the local groups are those of the CW pairs $(D^m,S^{m-1})$, $(D^n,S^{n-1})$ and $(D^m\times D^n,\ S^{m-1}\times D^n\cup D^m\times S^{n-1})$, the product pair being reached by radial deformation of $D^m\times D^n-\{0\}$ onto that subcomplex. The relative Künneth theorem (printed p. 276) then gives
$$
H_{m+n}\bigl(D^m\times D^n,\ S^{m-1}\times D^n\cup D^m\times S^{n-1}\bigr)
\cong\bigoplus_{p+q=m+n}H_p(D^m,S^{m-1})\otimes H_q(D^n,S^{n-1})
\ \oplus\!\!\bigoplus_{p+q=m+n-1}\!\!\operatorname{Tor}\bigl(H_p(D^m,S^{m-1}),H_q(D^n,S^{n-1})\bigr),
$$
whose only surviving summands are the top ones; so the local cross product is an isomorphism over $\ZZ$. Replacing $x$ and $y$ by closed balls of finite radius gives the same statement for the groups $H_*(M\,||\,B_1)$ and $H_*(N\,||\,B_2)$ of a pair of balls, which is the form the compatibility condition of an orientation uses.

*The coefficient ring.* This is the step the source asserts. The relative chain complex $C_*(M,M-x)$ is free in each degree (printed p. 261), so the universal coefficient theorem for homology, Theorem 3A.3 (printed p. 264), gives the natural short exact sequence
$$
0\to H_m(M\,||\,x;\ZZ)\otimes_\ZZ R\to H_m(M\,||\,x;R)\to\operatorname{Tor}\bigl(H_{m-1}(M\,||\,x;\ZZ),R\bigr)\to 0 .
$$
By excision $H_m(M\,||\,x;\ZZ)\cong H_m(D^m,S^{m-1})\cong\ZZ$ and $H_{m-1}(M\,||\,x;\ZZ)=0$, so $H_m(M\,||\,x;R)\cong\ZZ\otimes_\ZZ R=R$, and the generator over $R$ is the image $\zeta_x\otimes 1$ of an integral generator $\zeta_x$; the same holds at $y$. By Proposition 3B.1 and the identification $C_*(X;R)\otimes_R C_*(Y;R)=C_*(X\times Y;R)$ used on printed p. 276, the cross product with coefficients in $R$ is the integral chain-level cross product followed by $-\otimes_\ZZ R$. Hence the local cross product carries $\zeta_x\otimes1$ and $\zeta_y\otimes1$ to $(\zeta_x\times\zeta_y)\otimes1=\pm1$: over $R$ it too is an isomorphism $R\otimes_R R\to R$, and the product of generators is a generator.

*Orientations multiply.* If $x\mapsto\mu_x$ and $y\mapsto\nu_y$ are $R$-orientations of $M$ and $N$, then $(x,y)\mapsto\mu_x\times\nu_y$ is an $R$-orientation of $M\times N$: it is a section of the local system by the two paragraphs above, and it satisfies the compatibility condition by passing to the product of closed balls $B_1\ni x$ and $B_2\ni y$. So $M\times N$ is $R$-orientable, and by Theorem 3.26(a) (printed p. 236) the map $H_{m+n}(M\times N;R)\to H_{m+n}(M\times N\,||\,(x,y);R)\cong R$ is an isomorphism.

*The closed manifolds, integral coefficients.* Take $R=\ZZ$ again. Kottke's next computation is the Künneth formula for the product, Theorem 3B.6 (printed p. 275), which applies since a closed manifold is homotopy equivalent to a CW complex (Corollary A.12, printed p. 529):
$$
H_{m+n}(M\times N)\ \cong\ H_m(M)\otimes H_n(N)\ \oplus\ \operatorname{Tor}\bigl(H_m(M),H_{n-1}(N)\bigr)\ \oplus\ \operatorname{Tor}\bigl(H_{m-1}(M),H_n(N)\bigr)\ =\ H_m(M)\otimes H_n(N),
$$
all other terms vanishing and the two Tor groups vanishing because the top degree groups are free. So $[M]\times[N]$ is a generator of $H_{m+n}(M\times N)\cong\ZZ$.

*The fundamental class.* Finally, for each $(x,y)$ the naturality of the cross product in the pair variables gives
$$
(\alpha\times\beta)_{(x,y)}=\alpha_x\times\beta_y\ \in\ H_{m+n}\bigl(M\times N\,||\,(x,y);R\bigr),
$$
and by *The coefficient ring* this is a generator whenever $\alpha_x$ and $\beta_y$ are. So $\alpha\times\beta$ has a generator as its image in every local group, which by Hatcher's definition of a fundamental class (printed p. 236) is exactly that $\alpha\times\beta$ is a fundamental class for $M\times N$ with coefficients in $R$.
:::
