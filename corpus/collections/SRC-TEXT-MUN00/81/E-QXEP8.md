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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §81 Exercise 5, printed p. 493. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack Exchange advanced
    searches "lens space L(n,k) homeomorphic n=n'" and, in the title, "lens space fundamental group" (neither
    with hits) and the similar-question search from "Lens spaces L(n,k) homeomorphic implies n equal" (15
    items); the threads returned prove that the fundamental group separates the n, and none treats the
    classification within a fixed n. MathOverflow 156487 states the classification count of lens spaces
    without proof. The card keeps its own proof: pi_1(L(n,k)) = Z/n by Theorem 81.5 (printed p. 490) after the
    proper discontinuity of the action, so unequal n give non-homeomorphic spaces, and for n = n' the card's
    k-invariant distinguishes them.
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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, with every citation verified on the page and one ordering error repaired. The card previously derived "h has exact order n" from the absence of fixed points before proving the absence of fixed points; the two are now consecutive steps in the right order, with the fixed-point-free computation separated from the order statement. What was checked on the page: Theorem 81.5 (printed p. 490) is the quotient-by-a-properly-discontinuous-action covering theorem and does give regularity and the identification of G with the group of covering transformations; Corollary 81.4 (printed p. 489) is "if p: E -> B is a covering map with E simply connected then C(E,p,B) is isomorphic to pi_1(B,b_0)"; Exercise 4 of §81 (printed p. 493) is exactly the finite fixed-point-free Hausdorff statement used; Theorem 59.3 (printed p. 369) is "if n >= 2 the n-sphere is simply connected". Facts the prose used silently are now steps: path and local path connectedness of S^3 (needed before Theorem 81.5 applies), S^3 being a 3-manifold by the hemisphere projection, and the openness of the quotient map. Two gaps filled in the Hausdorff argument: the disjointness of the orbits (else u = v) and the disjointness of the images of the two G-invariant open sets (a shared point would put one of its preimages in both). The card states that only the necessity of n = n' is proved, and not the bracketed classification printed with the exercise. The verification is the card's own: no retained publication for this exercise was located, as the card's earlier audit records.
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
No retained solution set covers this exercise: the collection's provenance is the textbook, and the searches for this exercise are recorded on the card and in the `COMPLAINTS.md` entry for Sections 74--85 of `SRC-TEXT-MUN00`. The argument is the card's own, checked stepwise against Munkres, *Topology* (2000), Section 81 Exercise 5, and the numbered theorems cited in each step.

Write $S^3=\{(z_1,z_2)\in\CC^2:\abs{z_1}^2+\abs{z_2}^2=1\}$ and $\omega=e^{2\pi i/n}$, $\eta=e^{2\pi ik/n}$, so that $h(z_1,z_2)=(\omega z_1,\eta z_2)$ and $\gcd(k,n)=1$.

::: pf

::: {.pf-step #homeo}
$h$ is a homeomorphism of $S^3$, with $h^{-1}(z_1,z_2)=(\omega^{-1}z_1,\eta^{-1}z_2)$.

::: pf-proof
$h$ is the restriction to $S^3$ of the $\CC$-linear map $T(w_1,w_2)=(\omega w_1,\eta w_2)$ of $\CC^2$, which is invertible with inverse $T^{-1}(w_1,w_2)=(\omega^{-1}w_1,\eta^{-1}w_2)$. Since $\abs\omega=\abs\eta=1$,
$$
\abs{\omega w_1}^2+\abs{\eta w_2}^2=\abs{w_1}^2+\abs{w_2}^2,
$$
so $T$ and $T^{-1}$ carry $S^3$ into itself; hence $h$ is a bijection of $S^3$ with inverse $h^{-1}=T^{-1}\restrict_{S^3}$, continuous in both directions.
:::

:::

::: {.pf-step #nofix}
For $0<j<n$, $h^j$ has no fixed point on $S^3$.

::: pf-proof
Suppose $h^j(z_1,z_2)=(z_1,z_2)$, i.e. $\omega^jz_1=z_1$ and $\eta^jz_2=z_2$. At least one of $z_1,z_2$ is nonzero. If $z_1\ne0$ then $\omega^j=1$, so $n\mid j$. If $z_1=0$ then $\abs{z_2}=1$, so $z_2\ne0$ and $\eta^j=1$, i.e. $e^{2\pi ikj/n}=1$, i.e. $n\mid kj$; since $\gcd(k,n)=1$ this gives $n\mid j$. Both contradict $0<j<n$.
:::

:::

::: {.pf-step #ordern}
$h$ has order exactly $n$.

::: pf-proof
$h^n(z_1,z_2)=(\omega^nz_1,\eta^nz_2)=(z_1,z_2)$ because $\omega^n=1$ and $\eta^n=e^{2\pi ik}=1$, so $h^n=\operatorname{id}$. If $0<j<n$ and $h^j$ had a fixed point, step [](#nofix){.pf-ref} would give $n\mid j$, which is impossible; so $h^j\ne\operatorname{id}$ for $0<j<n$.
:::

:::

::: {.pf-step #parta}
$G=\langle h\rangle$ is a cyclic subgroup of the homeomorphism group of $S^3$ of order $n$, and only its identity element has a fixed point.

::: pf-proof
$G$ is cyclic by definition, and $\cardinality G=n$ by step [](#ordern){.pf-ref}, so $G\cong\ZZ/n$; each of its elements is a power of the homeomorphism $h$ (step [](#homeo){.pf-ref}). The nonidentity elements are exactly the $h^j$ with $0<j<n$, and none of them has a fixed point by step [](#nofix){.pf-ref}, while the identity fixes every point. This is part (a).
:::

:::

::: {.pf-step #manifold}
$S^3$ is a $3$-manifold: each of its points has a neighbourhood homeomorphic to an open subset of $\RR^3$.

::: pf-proof
Let $y\in S^3$ and let $W=\{z\in S^3:z\cdot y>0\}$, an open neighbourhood of $y$ in $S^3$. Orthogonal projection $z\mapsto z-(z\cdot y)y$ maps $W$ bijectively onto the open unit ball of the hyperplane $y^\perp\cong\RR^3$: writing $z=ty+u$ with $u\in y^\perp$ gives $\abs z^2=t^2+\abs u^2=1$ and $z\cdot y=t>0$, so $t=\sqrt{1-\abs u^2}>0$ and $\abs u<1$, with inverse $u\mapsto\sqrt{1-\abs u^2}\,y+u$. Both maps are continuous, so $W$ is homeomorphic to the open ball. This is the definition of a $3$-manifold (§36).
:::

:::

::: {.pf-step #smooth}
$S^3$ is path connected and locally path connected.

::: pf-proof
$S^3$ is a metric space. It is path connected: any point $p\in S^3$ has $\abs p=1$, so $p$ and $(1,0)$ are not antipodal and the great-circle arc $t\mapsto\frac{(1-t)p+t(1,0)}{\abs{(1-t)p+t(1,0)}}$ joins them inside $S^3$. It is locally Euclidean by step [](#manifold){.pf-ref}, and an open subset of $\RR^3$ is locally path connected, so $S^3$ is locally path connected.
:::

:::

::: {.pf-step #proper}
The action of the finite group $G$ on the Hausdorff space $S^3$ is properly discontinuous.

::: pf-proof
$S^3$ is Hausdorff, being a metric space, and $G$ is a finite group of homeomorphisms whose action is fixed-point free by step [](#parta){.pf-ref}. Exercise 4 of §81 says exactly this: a finite fixed-point-free action of homeomorphisms on a Hausdorff space is properly discontinuous.
:::

:::

::: {.pf-step #covering}
$\pi:S^3\to L(n,k)=S^3/G$ is a regular covering map whose group of covering transformations is $G$.

::: pf-proof
$S^3$ is path connected and locally path connected by step [](#smooth){.pf-ref}, and the action is properly discontinuous by step [](#proper){.pf-ref}; Theorem 81.5 then gives that the quotient map $\pi$ is a covering map, that it is regular, and that $G$ is its group of covering transformations.
:::

:::

::: {.pf-step #pi1}
$\pi_1\big(L(n,k),u_0\big)\cong G\cong\ZZ/n$ for a basepoint $u_0=\pi(x_0)$.

::: pf-proof
$S^3$ is simply connected by Theorem 59.3, since $3\ge2$. Corollary 81.4 then identifies the group of covering transformations of $\pi$ with the fundamental group of the base: $\mathcal C(S^3,\pi,L(n,k))\cong\pi_1(L(n,k),u_0)$. By step [](#covering){.pf-ref} that group of covering transformations is $G$, and $G\cong\ZZ/n$ by step [](#parta){.pf-ref}.
:::

:::

::: {.pf-step #partb}
If $L(n,k)$ and $L(n',k')$ are homeomorphic then $n=n'$.

::: pf-proof
A homeomorphism $\phi:L(n,k)\to L(n',k')$ carries a basepoint $u_0$ to $\phi(u_0)$ and induces an isomorphism $\phi_*:\pi_1(L(n,k),u_0)\to\pi_1(L(n',k'),\phi(u_0))$. By step [](#pi1){.pf-ref} the two groups are $\ZZ/n$ and $\ZZ/n'$, so $\ZZ/n\cong\ZZ/n'$; a group isomorphism carries the set of elements of finite order onto the set of elements of finite order, and $\ZZ/m$ has exactly $m$ elements, so $n=n'$. This is part (b), in the direction the exercise asks; the bracketed classification printed with the exercise is not proved here.
:::

:::

::: {.pf-step #compact}
$L(n,k)$ is compact.

::: pf-proof
$S^3$ is compact, being closed and bounded in $\CC^2\cong\RR^4$, and $\pi$ is continuous and onto, so $L(n,k)=\pi(S^3)$ is compact by Theorem 26.5.
:::

:::

::: {.pf-step #locallyeuclid}
Every point of $L(n,k)$ has a neighbourhood homeomorphic to an open subset of $\RR^3$.

::: pf-proof
Let $u\in L(n,k)$ and take $y\in S^3$ with $\pi(y)=u$. Since $\pi$ is a covering map (step [](#covering){.pf-ref}), $u$ has a neighbourhood $V$ evenly covered by $\pi$: $\pi^{-1}(V)$ is a disjoint union of open sets each mapped homeomorphically onto $V$ by $\pi$. The point $y$ lies in one such slice $S$, so $\pi\restrict_S:S\to V$ is a homeomorphism. Now $S$ is open in $S^3$, so by step [](#manifold){.pf-ref} it is homeomorphic to an open subset of $\RR^3$; composing, $V$ is homeomorphic to an open subset of $\RR^3$.
:::

:::

::: {.pf-step #open}
$\pi$ is an open map.

::: pf-proof
For open $U\subseteq S^3$, the preimage $\pi^{-1}\pi(U)=\bigcup_{g\in G}g(U)$ is a union of open sets, hence open; by the definition of the quotient topology $\pi(U)$ is then open in $S^3/G$.
:::

:::

::: {.pf-step #hausdorff}
$L(n,k)$ is Hausdorff.

::: pf-proof
Let $u\ne v$ in $L(n,k)$ and choose $x,y\in S^3$ with $\pi(x)=u$, $\pi(y)=v$. The orbits $Gx$ and $Gy$ are finite, hence closed in the Hausdorff space $S^3$ (Theorem 17.8), and they are disjoint: if $gx=g'y$ then $u=\pi(x)=\pi(gx)=\pi(g'y)=\pi(y)=v$.
$S^3$ is compact and Hausdorff, hence normal (Theorem 32.3), so there are disjoint open sets $U_0\supseteq Gx$ and $V_0\supseteq Gy$. Put $U=\bigcap_{g\in G}g(U_0)$ and $V=\bigcap_{g\in G}g(V_0)$; these are open, being finite intersections of open sets, and they contain $Gx$ and $Gy$ respectively, because $g(Gx)=Gx\subseteq g(U_0)$ for every $g$. They are $G$-invariant: $g(U)=\bigcap_{g'}gg'(U_0)=\bigcap_{g''}g''(U_0)=U$ since $g'$ runs over the group. And $U\cap V=\varnothing$: a point $z$ of the intersection would give $g^{-1}(z)\in U_0$ and $g^{-1}(z)\in V_0$ for every $g$, contradicting disjointness.
Finally $\pi(U)$ and $\pi(V)$ are disjoint: if $w=\pi(a)=\pi(b)$ with $a\in U$, $b\in V$, then $b=ga$ for some $g\in G$, so $a=g^{-1}b\in g^{-1}V=V$, a contradiction. By step [](#open){.pf-ref} both are open, and they contain $u$ and $v$.
:::

:::

::: {.pf-step #countable}
$L(n,k)$ has a countable basis.

::: pf-proof
$S^3\subseteq\RR^4$ is second countable, so let $\{B_m\}$ be a countable basis for $S^3$. Then $\{\pi(B_m)\}$ is countable and consists of open sets by step [](#open){.pf-ref}; it is a basis: given $u\in L(n,k)$ and an open $O\ni u$, the set $\pi^{-1}(O)$ is open and contains some $x\in\pi^{-1}(u)$, so there is $m$ with $x\in B_m\subseteq\pi^{-1}(O)$, whence $u\in\pi(B_m)\subseteq O$.
:::

:::

::: {.pf-step #partc}
$L(n,k)$ is a compact $3$-manifold.

::: pf-proof
$L(n,k)$ is a Hausdorff space with a countable basis (steps [](#hausdorff){.pf-ref}, [](#countable){.pf-ref}) in which every point has a neighbourhood homeomorphic to an open subset of $\RR^3$ (step [](#locallyeuclid){.pf-ref}), and it is compact (step [](#compact){.pf-ref}). That is the definition of a compact $3$-manifold (§36). This is part (c).
:::

:::

:::
:::
