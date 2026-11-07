---
schema: qual/card@1
id: E-HAT-3.3-31
kind: problem
title: Boundary map sends fundamental class to fundamental class
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 31; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 31; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: at each boundary point the global class restricts to the local fundamental
    class of a half-ball, whose boundary is the local generator of the induced boundary
    orientation; a class with that property at every point is the fundamental class of
    $\partial M$. Read at the level of that characterisation.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The local half of this proof was a gesture — the image of the relative fundamental class in the
    local relative group was called the local fundamental class of the half-ball, and its local
    boundary the local generator, with no computation behind either claim. The solution now names the
    half-ball N and its flat part N', the two excisions that reduce the global statement to the pair
    (D^n, D^n-1), and the long exact sequence of the contractible pair that makes the boundary map an
    isomorphism there; and it says that M compact makes the boundary compact, so Lemma 3.27(a)
    applies with A equal to the boundary. Not checked: the global sign, which is the one fixed by
    Exercise 30's collar convention.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Replaced the false half-disk computation. Explicitly, for a half-disk N in D^2 or an annulus,
    N and N cap boundary M are contractible, so the previously used H_2(N,N cap boundary M) is 0,
    not R, and H_1(N cap boundary M) = H_1(D^1) = 0, not R; the asserted deformation retraction
    onto N also does not hold. The correct local pair is (D, boundary D), with D a closed half-ball
    and boundary D consisting of both its flat face and curved cap, so H_n(D,boundary D) = R and
    its boundary map is the suspension isomorphism. The new proof uses A = (M-U) union V and
    proves H_n(M,A) = H_n(D,boundary D) via good-pair quotients (Proposition 2.22 p.124), not a
    global excision. It then uses naturality of the triple (M,A,boundary M-V) and excision on the
    boundary sphere to compare with H_{n-1}(boundary M,boundary M-x). The n = 1 local group is
    treated separately using reduced H_0(S^0) and unreduced H_0 of a point.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The lower-right excision is now the actual comparison: deleting boundary M-V from the pair
    (boundary M,boundary M-x) leaves (V,V-x), so H_{n-1}(V,V-x) is excision-isomorphic to
    H_{n-1}(boundary M,boundary M-x), not to H_{n-1}(boundary M,boundary M-V), which would leave
    (V,empty). The comparison is stated as an equality in the common target H_{n-1}(V,V-x), with
    r_D and r_M induced by inclusion and the same excision on boundary D. Unit tracking is
    corrected: over an arbitrary coefficient ring R a generator is u[D] with u in R's unit group,
    not necessarily +-D, and the boundary normalization carries that unit.

---

::: {.problem}
Show that if $M$ is a compact $R$-orientable $n$-manifold, then the boundary map $H_n(M, \partial M; R) \to H_{n-1}(\partial M; R)$ sends a fundamental class for $(M, \partial M)$ to a fundamental class for $\partial M$.
:::

::: {.solution}
Let $[M]\in H_n(M,\partial M;R)$ be the relative fundamental class. On p. 250 Hatcher constructs it from the collar identification
$$
H_i(M,\partial M;R)\cong
H_i\bigl(M-\partial M,\partial M\times(0,\varepsilon);R\bigr):
$$
its restriction to $H_n(M-\partial M,(M-\partial M)-\{z\};R)$ is the chosen local orientation at every interior point $z$.

Fix $x\in\partial M$. Choose an open half-ball $U\subset M$ around $x$ in a single boundary chart, with $\overline U\cong D^n$ and $V=U\cap\partial M$ an open $(n-1)$-disk in the flat face. Put $D=\overline U$ and
$$
A=M-(U-V)=(M-U)\cup V .
$$
Then $\partial M\subset A$ and $V=\partial M\cap U$, so $(M,A,\partial M-V)$ is a triple. Also $A\cap D=\partial D$: the flat face $V$ is included in $\partial M$, and the curved cap is included in $M-U$.

The local relative group is computed by
$$
H_n(M,A;R)\cong H_n(D,\partial D;R)\cong R .
$$
This is not excision by deleting a flat boundary patch. Instead, both $(M,A)$ and $(D,\partial D)$ are good pairs: shrinking a boundary-chart half-ball and a collar gives neighborhoods that deformation retract to $A$ and $\partial D$, respectively. The inclusion of pairs induces a homeomorphism
$$
D/\partial D\xrightarrow{\ \cong\ }M/A
$$
because everything outside $D$ is contained in $A$. Proposition 2.22, p. 124, therefore gives the first isomorphism; the second is the pair sequence of $(D,\partial D)$, with $\partial D\cong S^{n-1}$. In particular $H_2(D,\partial D;R)=R$ for a disk or a half-disk in an annulus, in contrast to the zero group of a pair of two contractible disks.

I next check that the image of $[M]$ in $H_n(M,A;R)$ is a generator. Pick an interior point $z\in U-V$. Since $A\subset M-\{z\}$, the image of $[M]$ in $H_n(M,A;R)$ maps under the pair inclusion to its local orientation in $H_n(M,M-\{z\};R)$, which is a generator by the first paragraph. As $H_n(M,A;R)$ also has the single generator $[D]$ coming from $H_n(D,\partial D;R)$, the image of $[M]$ is $u[D]$ for a unit $u\in R^\times$ (and the local restriction map is an isomorphism onto $H_n(M,M-\{z\};R)$).

It remains to pass to the boundary at $x$. Ordinary excision, deleting $\partial M-V$ from the pair $(\partial M,\partial M-\{x\})$, gives
$$
H_{n-1}(V,V-\{x\};R)\cong H_{n-1}(\partial M,\partial M-\{x\};R):
$$
indeed $V=U\cap\partial M$ is open in $\partial M$ and $x\in V$, and $(\partial M-\{x\})-(\partial M-V)=V-\{x\}$. It is the same computation as Exercise 7's excision, but with the pair $(\partial M,\partial M-\{x\})$, not with $(\partial M,\partial M-V)$. Likewise, on $\partial D\cong S^{n-1}$,
$$
H_{n-1}(V,V-\{x\};R)\cong H_{n-1}(\partial D,\partial D-\{x\};R).
$$

Now define the local boundary $\partial_{D,x}$ as the composite
$$
H_n(D,\partial D;R)\xrightarrow{\ \partial\ }
H_{n-1}(\partial D;R)\longrightarrow H_{n-1}(\partial D,\partial D-\{x\};R).
$$
Write $e_D:H_{n-1}(V,V-\{x\};R)\to H_{n-1}(\partial D,\partial D-\{x\};R)$ and $e_M:H_{n-1}(V,V-\{x\};R)\to H_{n-1}(\partial M,\partial M-\{x\};R)$ for the two excision isomorphisms above, and let $r_D$ and $r_M$ be the two maps induced on local homology by inclusion. The required comparison is the equality
$$
e_M\bigl(r_M(\delta[M])\bigr)
 =u\,e_D\bigl(\partial_{D,x}[D]\bigr)
 \qquad\text{in }H_{n-1}(V,V-\{x\};R),
$$
where $u\in R^\times$ is the unit already found. To see it, localize the relative fundamental class to a representative of $[D]$ via the good-pair quotient comparison. Applying $\partial$ and restricting to the open face $V$ commute with that localization: in either order one obtains the same sum of the boundary simplices lying in the open face. This is naturality of the connecting map on the corresponding relative singular chain complexes, restricted to the displayed local pairs; no map through $H_{n-1}(\partial M,\partial M-V)$ is involved.

Now $H_n(D,\partial D;R)\cong R$ and $H_{n-1}(\partial D;R)\cong R$ for $n\ge2$, with $\delta$ an isomorphism by the pair sequence because $D$ is contractible. For $n=1$, the reduced pair sequence gives $H_1(D,\partial D;R)\cong\widetilde H_0(S^0;R)\cong R$, while the unreduced local groups are $H_0(S^0,S^0-\{x\};R)\cong H_0(V;R)\cong R$ because $V=\{x\}$. In every dimension the boundary map sends $[D]$ to a fundamental class $[\partial D]$, with its unit of normalization determined by Exercise 30's collar convention. Hence $\delta[M]$ maps to a generator of
$$
H_{n-1}(\partial M,\partial M-\{x\};R),
$$
with coefficient $u$ times the image of the local fundamental class.
Its normalization is exactly the unit fixed by Exercise 30's product orientation of the collar: the relative class comes from an oriented interior disk times the collar interval, and $\partial$ picks out that interval's endpoint.

Since $x$ was arbitrary, $\delta[M]$ restricts to a local orientation generator at every boundary point. As $M$ is compact, $\partial M$ is compact, so Lemma 3.27(a), p. 236, with $A=\partial M$ identifies this section with the fundamental class of $\partial M$. Hence
$$
\delta[M]=[\partial M].
$$
:::
