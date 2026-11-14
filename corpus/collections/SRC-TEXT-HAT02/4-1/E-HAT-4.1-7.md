---
schema: qual/card@1
id: E-HAT-4.1-7
kind: problem
title: "Change-of-basepoint for relative homotopy groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct, and it separates the two things that have to be checked: that the collar
    construction depends only on the relative class (reparametrization and width, standard), and that the
    resulting maps are compatible with the rest of the long exact sequence. The inverse is `beta` along the
    reversed path and the cocycle is `beta_{gamma eta} = beta_gamma beta_eta` with the stated path order;
    concatenation and homotopy rel endpoints behave as claimed. The naturality `partial beta_gamma =
    beta_gamma partial` with the boundary map into `pi_{n-1}(A)` is the point that makes the relative
    theory work, and it is stated. The closing remark about `A` path-connected and the `pi_1(A)`-ambiguity
    matches the absolute case. No correction was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 7, printed p. 358, with Hatcher's
    own description of the relative change-of-basepoint maps on p. 345 (place a copy of $f$ in a
    smaller cube with its face $I^{n-1}$ centered in the corresponding face of the larger cube; the
    properties are left as this exercise). The earlier note on this card called the construction
    standard and needed no correction; that was too generous — the card then said only that "the
    usual reparametrization argument" gives independence of choices and listed the properties without
    proof. The solution now carries the construction explicitly, with the inner cube
    $Q=[\varepsilon,1-\varepsilon]^{n-1}\times[0,1-\varepsilon]$, the rescaling $\varphi$, and the
    shell parameter $\delta$ with $\delta^{-1}(0)=\partial I^n$, $\delta^{-1}(1)=\partial Q$; it
    proves well-definedness, naturality, the constant-path case by the family $Q_u$, the
    concatenation law $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$ by sliding the shell, additivity by
    the explicit family of moving boxes $[c_u,d_u]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon]$
    with $c_u=\varepsilon(1-u/2)$, $d_u=(1-u\varepsilon)/2$, whose ends are $\gamma(f+g)$ and
    $\gamma f+\gamma g$, and $\partial\beta_\gamma=\beta_\gamma\partial$. No published solution of
    this exercise is in the retained sets; Sam's §4.1 covers 2, 3, 5, 10-15 and 19.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 358 and asks for the change-of-basepoint properties of Hatcher p. 345 to be extended to relative homotopy groups. The published complete treatment is May, *A Concise Course in Algebraic Topology*, §5 "Change of basepoint", printed pp. 68--69: $\pi_n(X,A,a)$ is identified with $\pi_0$ of a fibre, a path class $[\alpha]$ in $A$ from $a$ to $a'$ induces an isomorphism $\tau[\alpha]$, and the printed Theorem on p. 69 gives both naturality squares $f_*\tau[\alpha]=\tau[f\circ\alpha]f_*$ and $\tau[h(a)]f_*=f'_*$ for a homotopy $h$. The card's proof is that construction written in Hatcher's cubical model, with the rescaling of the smaller cube and the compatibility with the boundary map. Checked against the book: Hatcher's own description of the relative $\beta_\gamma$ on p. 345, the formulas (1)--(3) on p. 341, and the long exact sequence of Theorem 4.3 on p. 344. Not claimed: that Hatcher prints the exercise; May prints the theorem for the relative groups.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The construction on this card was wrong and is repaired. Its auxiliary function was asked to
    satisfy $\delta^{-1}(0)=\partial I^n$ and $\delta^{-1}(1)=\partial Q$, which cannot hold: with
    $Q=[\varepsilon,1-\varepsilon]^{n-1}\times[0,1-\varepsilon]$ the bottom face $B$ of $Q$ lies in
    both $\partial I^n$ and $\partial Q$, and $\operatorname{int}B$ is not reached by the shell at
    all. The card also asserted that $\varphi$ carries $B$ into the boundary of the free face; it
    carries $B$ onto the free face and $\partial B$ onto $\partial I^{n-1}$. Repaired as follows, and
    stated on the card: $\delta$ is defined on $S=I^n-\operatorname{int}Q$ by the boundary values
    $0$ on the non-free faces (hence on $\partial I^{n-1}$) and $1$ on the non-bottom faces of $Q$
    and on $\partial B$, interpolating across the annulus $\Sigma=I^{n-1}-\operatorname{int}B$, with
    an explicit formula; continuity at $Q\cap S=\partial Q$ then uses $f(\varphi(\partial B)) =
    f(\partial I^{n-1}) = x_1$, which is where the value $x_1$ comes from, and not the value of $f$
    on the interior of the free face, which is an arbitrary map into $A$. The conclusion offered
    against the card, that $\gamma f$ is not continuous unless $\gamma$ is constant, does not hold:
    with $\delta$ as above $\gamma f$ is a map of triples for every path $\gamma$ in $A$ from $x_0$
    to $x_1$, whose endpoints are the only constraint on $\gamma$. The card's remark that Hatcher's
    picture puts $\gamma$ on the bottom-face shell is right and is now stated: centering the small
    cube's free face in the large one is exactly what makes $\Sigma$ part of the shell. The
    concatenation law was used with the wrong basepoints and is corrected: with
    $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$ the identities are
    $\beta_{\bar\gamma}\beta_\gamma=\beta_{\bar\gamma\gamma}=\mathrm{id}$ on
    $\pi_n(X,A,x_1)$ and $\beta_\gamma\beta_{\bar\gamma}=\beta_{\gamma\bar\gamma}=\mathrm{id}$ on
    $\pi_n(X,A,x_0)$, not $\beta_{\bar\gamma}\beta_\gamma=\beta_{\gamma\bar\gamma}$. The published
    source is cited correctly for the first time: J. Peter May (not Michael May), *A Concise Course
    in Algebraic Topology*, Chapter 9 §5, printed pp. 68--69, and the remark now states what that
    construction covers — the isomorphism $\tau[\alpha]$ for the relative groups and the two
    naturality squares of its Theorem on p. 69 — and what it does not: Hatcher's cubical $\gamma f$,
    the explicit laws in that model and $\partial\beta_\gamma=\beta_\gamma\partial$. No published
    solution of the exercise as a whole has been located. Not verified: the pagination of the 1999
    Chicago bound volume, the quoted pages being those of the revised PDF.
---

::: {.problem}
Extend the results proved near the beginning of this section for the change-of-basepoint maps $\beta_\gamma$ to the case of relative homotopy groups.
:::

::: {.solution}
Hatcher's cubical model (printed p. 344): $I^{n-1}$ is the face $s_n=0$ of $I^n$, the free face; $J^{n-1}$ is the closure of $\partial I^n-I^{n-1}$; and $\pi_n(X,A,x_1)$ is the set of homotopy classes of maps
$$
f:(I^n,\partial I^n,J^{n-1})\longrightarrow(X,A,x_1),
$$
so $f(\partial I^n)\subseteq A$ and $f(J^{n-1})=x_1$. Two consequences are used throughout. Because $I^{n-1}\subset\partial I^n$, the whole free face maps into $A$. Because $\partial I^{n-1}\subset J^{n-1}$, the boundary of the free face maps to the single point $x_1$. Hatcher defines $\gamma f$ on printed p. 345, for a path $\gamma$ in $A$ from $x_0$ to $x_1$, "by placing a copy of $f$ in a smaller cube with its face $I^{n-1}$ centered in the corresponding face of the larger cube", and leaves the properties to this exercise.

*The construction.* Fix $\varepsilon\in(0,\tfrac13)$ and put
$$
Q=[\varepsilon,1-\varepsilon]^{n-1}\times[0,1-\varepsilon],\qquad
\varphi(s)=\Bigl(\frac{s_1-\varepsilon}{1-2\varepsilon},\dots,\frac{s_{n-1}-\varepsilon}{1-2\varepsilon},\frac{s_n}{1-\varepsilon}\Bigr),
$$
so that $\varphi:Q\to I^n$ is a homeomorphism carrying the face $B=[\varepsilon,1-\varepsilon]^{n-1}\times\{0\}$ of $Q$ onto the free face $I^{n-1}$ and every other face of $Q$ into $J^{n-1}$. The copy of $f$ sits in $Q$ and its free face $B$ sits in the interior of the free face of $I^n$, which is what "centered in the corresponding face" says. Write $S=I^n-\operatorname{int}Q$ for the shell and $\Sigma=I^{n-1}-\operatorname{int}B$ for the annulus of the free face outside $B$; then $\partial S=\partial I^n\cup\partial Q$ and $Q\cap S=\partial Q$.

Choose a continuous $\delta:S\to[0,1]$ which is $0$ on the non-free faces of $I^n$, and hence on their closure, which contains $\partial I^{n-1}$; which is $1$ on the non-bottom faces of $Q$ and on $\partial B$; and which on the annulus $\Sigma$ runs from $0$ at $\partial I^{n-1}$ to $1$ at $\partial B$. Such a function exists, for example
$$
\delta(s)=1-\max\bigl(\nu(s_1,\dots,s_{n-1}),\tau(s_n)\bigr),\qquad
\nu=\max_i\max\Bigl\{\frac{\varepsilon-s_i}{\varepsilon},\frac{s_i-(1-\varepsilon)}{\varepsilon},0\Bigr\},\qquad
\tau=\max\Bigl\{\frac{s_n-(1-\varepsilon)}{\varepsilon},0\Bigr\},
$$
both maxima truncated at $1$: then $\nu=1$ exactly on the non-free faces (some $s_i\in\{0,1\}$ with $i<n$), $\tau=1$ exactly on the face $s_n=1$, and on $\Sigma$, where $s_n=0$, $\delta=1-\nu$ is $1$ at $\partial B$ and $0$ at $\partial I^{n-1}$. Define
$$
\gamma f:I^n\longrightarrow X,\qquad
\gamma f(s)=\begin{cases}f(\varphi(s)),&s\in Q,\\[2pt] \gamma(\delta(s)),&s\in S,\end{cases}
$$
and set $\beta_\gamma([f])=[\gamma f]$. This is the map of Hatcher's picture: the shell carries $\gamma$, radially, from $x_0$ on the outer boundary to $x_1$ where it meets the small cube.

*Continuity, and what the boundary values of $\delta$ have to be.* The two formulas must agree on $Q\cap S=\partial Q$, and they do: on a non-bottom face of $Q$ the first gives $f(\varphi(s))=x_1$ because $\varphi$ carries that face into $J^{n-1}$, and the second gives $\gamma(1)=x_1$; on $\partial B$ the first gives $f(\varphi(s))=x_1$ because $\varphi$ carries $\partial B$ onto $\partial I^{n-1}\subset J^{n-1}$, and the second gives $\gamma(1)=x_1$. So $\gamma f$ is continuous for every path $\gamma$ in $A$ from $x_0$ to $x_1$.

It is neither necessary nor possible to require $\delta^{-1}(0)=\partial I^n$ and $\delta^{-1}(1)=\partial Q$: $B$ lies in $\partial I^n\cap\partial Q$, so the two preimages would have to be disjoint, and in fact the shell never reaches $\operatorname{int}B$, since every point of $I^n$ directly above $\operatorname{int}B$ is an interior point of $Q$. What continuity at that junction needs is the value of $f$ on $\partial B$, not on $B$: $f$ is an arbitrary map into $A$ on the interior of the free face and takes the single value $x_1$ on its boundary. The annulus $\Sigma$ is the part of the shell that carries the interpolation, and it is exactly the region Hatcher's picture adds by centering the small cube's free face in the large one.

$\gamma f$ is a map of triples: on the non-free faces and on the annulus $\Sigma$, both of which lie in $\partial I^n$ and in $S$, the second formula gives $\gamma(\delta(s))\in A$; on $B\subset\partial I^n$ the first gives a point of $A$, since the free face maps into $A$; and $J^{n-1}$ is contained in the closure of the non-free faces, where $\delta=0$, so $\gamma f(J^{n-1})=\gamma(0)=x_0$.

*Well defined.* If $f_t$ is a homotopy of maps of triples from $f$ to $f'$, then $\gamma f_t$ is one from $\gamma f$ to $\gamma f'$: the formula is applied to $f_t$ inside $Q$, with the shell map unchanged. So $\beta_\gamma$ is a well-defined map of sets. It is natural: for a map of triples $\psi:(X,A,x_1)\to(Y,B,y_1)$ one has $\psi(\gamma f)=(\psi\gamma)(\psi f)$, so $\psi_*\beta_\gamma=\beta_{\psi\gamma}\psi_*$.

*Constant path.* If $\gamma$ is constant at $x_0=x_1$, then $\gamma f$ equals $f\circ\varphi$ on $Q$ and $x_0$ on the shell. Replacing $Q,\varphi,\delta$ by $Q_u=[u\varepsilon,1-u\varepsilon]^{n-1}\times[0,1-u\varepsilon]$ and the corresponding $\varphi_u,\delta_u$ for $u\in(0,1]$ gives a homotopy of maps of triples from $\gamma f$ to $f$ as $u\to0$: the shell shrinks onto $\partial I^n$ and its image is the single point $x_0$ throughout. Hence $\beta_\gamma=\mathrm{id}$ for the constant path $\gamma$ at $x_0=x_1$.

*Concatenation.* For paths $\gamma$ from $x_0$ to $x_1$ and $\eta$ from $x_1$ to $x_2$ in $A$ one has $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$: both sides put $f$ in a small cube and fill the shell by $\eta$ near the cube and by $\gamma$ near the outer boundary, and the family that moves the radius at which the shell switches from $\eta$ to $\gamma$ is a homotopy of maps of triples, the shell always lying in $A$. The same sliding of the shell shows that $\beta_\gamma$ depends only on the homotopy class of $\gamma$ rel endpoints.

*Isomorphism.* Apply the two laws to the reversed path $\bar\gamma(s)=\gamma(1-s)$. Since $\bar\gamma\gamma$ is a loop at $x_1$ and $\gamma\bar\gamma$ a loop at $x_0$, and each is homotopic rel endpoints to the constant path at its basepoint,
$$
\beta_{\bar\gamma}\beta_\gamma=\beta_{\bar\gamma\gamma}=\mathrm{id}_{\pi_n(X,A,x_1)},\qquad
\beta_\gamma\beta_{\bar\gamma}=\beta_{\gamma\bar\gamma}=\mathrm{id}_{\pi_n(X,A,x_0)} .
$$
The two composites are endomorphisms of groups at different basepoints, which is why the concatenations are written in that order: by the rule $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$ the path $\gamma$ is traversed first, so the pair complementary to $\gamma$ on the left is $\bar\gamma\gamma$ and on the right $\gamma\bar\gamma$. Hence $\beta_\gamma$ is a bijection, with inverse $\beta_{\bar\gamma}$.

*Additivity.* For $n\ge2$ the group structure on $\pi_n(X,A,x_1)$ comes from the first coordinate, which is not the special coordinate $s_n$, so $f+g$ is defined by the usual formula in $s_1$, and $\beta_\gamma([f]+[g])=\beta_\gamma[f]+\beta_\gamma[g]$ is the relative form of Hatcher's formula (1) on p. 341. On the inner cube $Q$ the map $\gamma(f+g)$ is $f$ on the half with the rescaled first coordinate in $[0,\tfrac12]$ and $g$ on the other half, with last and transverse coordinates rescaled as in $\gamma f$ and $\gamma g$. On the other hand $\gamma f+\gamma g$ is $f$ and $g$ on the two boxes
$$
Q_1=\bigl[\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2}\bigr]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon],\qquad
Q_2=\bigl[\tfrac{1+\varepsilon}{2},1-\tfrac{\varepsilon}{2}\bigr]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon],
$$
mapped through $\varphi$ composed with the doubling of the first coordinate, and $\gamma(\delta)$ elsewhere. Both maps are assembled from the same three ingredients — $f$ on a box, $g$ on a box, and $\gamma$ on the complement — and differ only in the position of the two boxes. For $u\in[0,1]$ put $c_u=\varepsilon(1-\tfrac u2)$ and $d_u=\tfrac12(1-u\varepsilon)$, so that $(c_0,d_0)=(\varepsilon,\tfrac12)$ and $(c_1,d_1)=(\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2})$, and move the two boxes to $[c_u,d_u]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon]$ and its mirror image $[1-d_u,1-c_u]\times\cdots$, carrying $f$ and $g$ with the first argument the affine map of the box onto $[0,1]$ and the shell carrying $\gamma$ composed with the corresponding distance function. Every stage is a map of triples: the boundary of each moving box carries $x_1$ on the $f$- and $g$-side, where the first argument is $0$ or $1$, and $\gamma(1)=x_1$ on the shell side; the boxes stay inside $[\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2}]$ and its mirror image, so they never meet. At $u=0$ this is $\gamma(f+g)$ and at $u=1$ it is $\gamma f+\gamma g$, so $\beta_\gamma(f+g)\simeq\beta_\gamma f+\beta_\gamma g$ and $\beta_\gamma$ is a homomorphism for $n\ge2$.

*Compatibility with the exact sequence.* The boundary map $\partial:\pi_n(X,A,x_1)\to\pi_{n-1}(A,x_1)$ restricts a representative to the face $s_n=0$. The restriction of $\gamma f$ to that face consists of the copy $f\circ\varphi$ on $B$, which is the restriction of $f$ to the free face, together with $\gamma(\delta)$ on the annulus $\Sigma$; that is exactly the absolute $\gamma(f|_{I^{n-1}})$ of p. 341, whose shell is $\Sigma$ and whose inner cube is $B$. So $\partial\beta_\gamma=\beta_\gamma\partial$ for the absolute change-of-basepoint maps on $\pi_{n-1}(A,x_1)$. Together with naturality this says that the action of $\pi_1(A,x_0)$ on the relative groups by $[\gamma]\mapsto\beta_\gamma$ commutes with every map of the long exact sequence of the pair, as Hatcher states on p. 345, and that $\pi_n(X,A,x_0)$ is independent of the basepoint in $A$ when $A$ is path-connected.

Checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 7, printed p. 358 ("Extend the results proved near the beginning of this section for the change-of-basepoint maps $\beta_\gamma$ to the case of relative homotopy groups"), with the three results of p. 341 and Hatcher's description of the relative $\beta_\gamma$ on p. 345.
:::

::: {.remark title="Published solution"}
J. Peter May, *A Concise Course in Algebraic Topology*, Chapter 9 §5 "Change of basepoint", printed pp. 68--69, gives the part of this exercise that is stated in terms of fibres rather than cubes. May identifies $\pi_n(X,A,a)$ with $\pi_0$ of the fibre over $a$ of the fibration $(X,A)^{(CS^{n-1},S^{n-1})}\to A$, so that a path class $[\alpha]$ in $A$ from $a$ to $a'$ induces a homotopy equivalence $\tau[\alpha]$ of fibres and hence an isomorphism $\tau[\alpha]:\pi_n(X,A,a)\to\pi_n(X,A,a')$, and the Theorem on p. 69 gives the two naturality squares: $f_*\tau[\alpha]=\tau[f\circ\alpha]f_*$ for a map of pairs, and $\tau[h(a)]f_*=f'_*$ for a homotopy $h$ from $f$ to $f'$. That is the isomorphism, its naturality and the functoriality of translation on which $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$ rests. The source does not contain Hatcher's cubical construction $\gamma f$, the explicit laws $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$, $\beta_{\bar\gamma}\beta_\gamma=\mathrm{id}$ and additivity of $\beta_\gamma$ in that model, or the compatibility $\partial\beta_\gamma=\beta_\gamma\partial$ with the boundary map, which are what this exercise asks for and what the solution above supplies. The pagination is that of the revised edition in `tmp/sources/may-concise-course-revised.pdf`; the pagination of the 1999 Chicago bound volume is not verified.
:::
