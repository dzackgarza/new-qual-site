---
schema: qual/card@1
id: E-HAT-4.2-29
kind: problem
title: "Homotopy classification of lens spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 29; the stored statement matches.
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
    Proof read against Hatcher Sec. 4.2 Exercise 29 (AT.txt 19436-19460) and repaired in two places.
    (i) Part (b)'s conclusion deg g = d_0 + dm was asserted with no argument, although the printed
    hint (AT.txt 19456-19457) asks the reader to compute it on the lift. The card now computes it on
    H_{2n-1}: the pinch sends the fundamental class to [L] + [S^{2n-1}], the second map multiplies the
    sphere summand by d, and the third multiplies by d_0 on L and by m through the m-sheeted covering,
    giving d_0 + dm. (ii) The final paragraph lifts g to universal covers, which requires S^{2n-1}
    simply connected and so fails at n=1; that case is now separated and is trivial, the only lens
    space in dimension 1 being S^1. Verified as correct and left unchanged: part (a)'s reduction to
    k=1, the congruence d_0 P = P' giving d_0 = +-1 mod m, and the Whitehead step. Not checked: the
    construction of f in Sec. 3.E Exercise 2(b), cited rather than re-derived.

---

::: {.problem}
Finish the homotopy classification of lens spaces begun in Exercise 2 of §3.E by showing that two lens spaces $L_m(\ell_1, \ldots, \ell_n)$ and $L_m(\ell_1', \ldots, \ell_n')$ are homotopy equivalent if $\ell_1 \cdots \ell_n \equiv \pm k^n \ell_1' \cdots \ell_n' \pmod{m}$ for some integer $k$, via the following steps:

(a) Reduce to the case $k = 1$ by showing that $L_m(\ell_1', \ldots, \ell_n') = L_m(k\ell_1', \ldots, k\ell_n')$ if $k$ is relatively prime to $m$. [Rechoose the generator of the $\ZZ_m$ action on $S^{2n-1}$.]

(b) Let $f: L \to L'$ be a map constructed as in part (b) of the exercise in §3.E. Construct a map $g: L \to L'$ as a composition $L \to L \vee S^{2n-1} \to L \vee S^{2n-1} \to L'$ where the first map collapses the boundary of a small ball to a point, the second map is the wedge of the identity on $L$ and a map of some degree $d$ on $S^{2n-1}$, and the third map is $f$ on $L$ and the projection $S^{2n-1} \to L'$ on $S^{2n-1}$. Show that $g$ has degree $k_1 \cdots k_n + dm$, that is, $g$ induces multiplication by $k_1 \cdots k_n + dm$ on $H_{2n-1}(-; \ZZ)$. [Show first that a lift of $g$ to the universal cover $S^{2n-1}$ has this degree.]

(c) If $\ell_1 \cdots \ell_n \equiv \pm \ell_1' \cdots \ell_n' \pmod{m}$, choose $d$ so that $k_1 \cdots k_n + dm = \pm 1$ and show this implies that $g$ induces an isomorphism on all homotopy groups, hence is a homotopy equivalence. [For $\pi_i$ with $i > 1$, consider a lift of $g$ to the universal cover.]
:::

::: {.solution}
Put
$$
P=\ell_1\cdots\ell_n,
\qquad
P'=\ell_1'\cdots\ell_n'.
$$
Assume
$$
P\equiv \pm k^nP'\pmod m.
$$
Since $P$ and $P'$ are units modulo $m$, so is $k$. Replacing the chosen generator of the $\ZZ_m$-action on the target by its $k$-th power replaces every $\ell_j'$ by $k\ell_j'$ without changing the lens space. Thus we may reduce to the case
$$
P\equiv\pm P'\pmod m.
$$

Choose nonzero integers $k_j$ satisfying
$$
k_j\ell_j\equiv\ell_j'\pmod m.
$$
Exercise 2 of §3.E constructs an equivariant map of universal covers and hence a map
$$
f:L_m(\ell_1,\dots,\ell_n)\to L_m(\ell_1',\dots,\ell_n')
$$
that induces an isomorphism on $\pi_1$ and has degree
$$
d_0=k_1\cdots k_n.
$$
Modulo $m$,
$$
d_0P\equiv P',
$$
so the reduced congruence gives
$$
d_0\equiv\pm1\pmod m.
$$
Choose $d\in\ZZ$ with
$$
d_0+dm=\pm1.
$$

Modify $f$ inside a small ball in the source as follows. Pinch that ball to add an $S^{2n-1}$-summand, map this new sphere to $S^{2n-1}$ with degree $d$, then compose with the $m$-sheeted covering
$$
S^{2n-1}\to L_m(\ell_1',\dots,\ell_n').
$$
The resulting map $g$ agrees with $f$ on the $1$-skeleton, so it induces the same isomorphism on $\pi_1$, while its degree is
$$
\deg g=d_0+dm=\pm1.
$$
For the degree, compute on $H_{2n-1}(-;\ZZ)\cong\ZZ$, as the hint directs. Collapsing the boundary of a small ball in $L$ to a point is a pinch map sending the fundamental class to $[L]+[S^{2n-1}]$; the second map fixes the $L$ summand and multiplies the class of the attached sphere by $d$; the third is $f$ on $L$ and the $m$-sheeted covering $S^{2n-1}\to L'$ on the sphere, so it multiplies by $d_0$ and by $m$ respectively. Hence $[L]\mapsto[L]+d\,[S^{2n-1}]\mapsto d_0[L']+dm[L']$, that is, $\deg g=d_0+dm$. Equivalently, on the lift to universal covers the summand of the added sphere contributes $dm$, and $d_0+dm=\pm1$ is exactly the choice of $d$.

For $n=1$ the assertion is trivial: $S^{1}$ is the only lens space in dimension $1$, so both sides are $S^1$ and are homotopy equivalent regardless of the congruences. So assume $n\ge2$, where $S^{2n-1}$ is simply connected and the lift is available.

Lift $g$ to universal covers. Since the covering maps on both sides have degree $m$, the lift
$$
\widetilde g:S^{2n-1}\to S^{2n-1}
$$
has degree $\pm1$, hence is a homotopy equivalence. Therefore $g$ induces isomorphisms on all higher homotopy groups as well as on $\pi_1$. Lens spaces are CW complexes, so Whitehead's theorem gives
$$
\boxed{L_m(\ell_1,\dots,\ell_n)\simeq L_m(\ell_1',\dots,\ell_n').}
$$
This proves the converse and completes the classification.
:::
