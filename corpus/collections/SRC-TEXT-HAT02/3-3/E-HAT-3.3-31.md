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

I next check that the image of $[M]$ in $H_n(M,A;R)$ is a generator. Pick an interior point $z\in U-V$. Since $A\subset M-\{z\}$, the image of $[M]$ in $H_n(M,A;R)$ maps under the pair inclusion to its local orientation in $H_n(M,M-\{z\};R)$, which is a generator by the first paragraph. As $H_n(M,A;R)$ also has the single generator $[D]$ coming from $H_n(D,\partial D;R)$, the image of $[M]$ is $\pm[D]$ (and the local restriction map is an isomorphism onto $H_n(M,M-\{z\};R)$).

It remains to pass to the boundary at $x$. Write $\partial_{D,V}$ for the composite
$$
H_n(D,\partial D;R)\xrightarrow{\ \partial\ }
H_{n-1}(\partial D;R)\longrightarrow
H_{n-1}(\partial D,\partial D-\{x\};R)
\xleftarrow[\ \cong\ ]{\ \operatorname{exc}\ }
H_{n-1}(V,V-\{x\};R).
$$
The last arrow is an isomorphism by excision in the $(n-1)$-sphere $\partial D$, since $V$ is an open disk in $\partial D$ around $x$ and $x\in V$. By naturality of the boundary map in the triple $(M,A,\partial M-V)$, and of the quotient-pair isomorphisms above, the following diagram commutes:
$$
\begin{array}{ccc}
H_n(M,\partial M;R) & \xrightarrow{\ \delta\ } & H_{n-1}(\partial M;R)\\
\Big\downarrow && \Big\downarrow\\
H_n(M,A;R) && H_{n-1}(\partial M,\partial M-V;R)\\
\Big\uparrow{\cong} && \Big\uparrow{\cong}\\
H_n(D,\partial D;R) & \xrightarrow{\ \partial_{D,V}\ } & H_{n-1}(V,V-\{x\};R) .
\end{array}
$$
The upper-left vertical map is the relative localization just computed; the upper-right one is induced by inclusion. The right-hand lower vertical map is again excision, with $V$ open in $\partial M$. The bottom equality of the two composites is the chain-level statement that a relative local cycle and its boundary are localized by the same restriction.

Now $H_n(D,\partial D;R)\cong R$ and $H_{n-1}(\partial D;R)\cong R$ for $n\ge2$, with $\delta$ an isomorphism by the pair sequence because $D$ is contractible. For $n=1$, the reduced pair sequence gives $H_1(D,\partial D;R)\cong\widetilde H_0(S^0;R)\cong R$, while the unreduced local groups are $H_0(S^0,S^0-\{x\};R)\cong H_0(V;R)\cong R$ because $V=\{x\}$. In every dimension the boundary map sends $[D]$ to a fundamental class $[\partial D]$. Its restriction to $H_{n-1}(V,V-\{x\};R)$ is therefore a generator. By the diagram, $\delta[M]$ maps to a generator of
$$
H_{n-1}(\partial M,\partial M-\{x\};R).
$$
Its sign is exactly the one fixed by Exercise 30's product orientation of the collar: the relative class comes from an oriented interior disk times the collar interval, and $\partial$ picks out that interval's endpoint.

Since $x$ was arbitrary, $\delta[M]$ restricts to a local orientation generator at every boundary point. As $M$ is compact, $\partial M$ is compact, so Lemma 3.27(a), p. 236, with $A=\partial M$ identifies this section with the fundamental class of $\partial M$. Hence
$$
\delta[M]=[\partial M].
$$
:::
