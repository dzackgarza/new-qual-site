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
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The exercise's properties are now the source's: tom Dieck, *Algebraic Topology* (EMS Textbooks in
    Mathematics, 2008), §6.2, printed pp. 126--127 — the transport along paths by homotopy extension,
    Proposition (6.2.2) for the relative groups (well-definedness, dependence on the path class only,
    the homomorphism property for $n\ge2$, and functoriality of $v\mapsto v_\#$), Proposition (6.2.1)
    with its proof in the absolute case, transcribed here, and Proposition (6.2.3) for the
    compatibility with the exact sequence of the pair. Three things the source leaves to the reader
    are written out and labelled as such on the card: the relative case of the (6.2.1) argument, for
    which the source says only "as above" and which needs the pair condition $V_t(\partial I^n)
    \subseteq A$ to be met by carrying the boundary of the free face along $v$ inside $A$; the
    homomorphism property for $n\ge2$ in the relative case, which the source asserts and the card
    proves by the moving-boxes argument; and the identification of Hatcher's cubical $\gamma f$ with
    the source's transport, settled by exhibiting the family $V_t$, $t\in[0,1]$, with $V_0=f$,
    $V_1=\gamma f$ and $V_t(J^{n-1})=\gamma(1-t)$, which gives $\beta_\gamma=(\bar\gamma)_\#$. That
    identification also settles the construction this card uses, which the previous event had to
    repair: the explicit $\delta$ is the $t=1$ member of that family. Checked against Hatcher (2002),
    §4.1 Exercise 7 on printed p. 358, the three formulas of p. 341 and the relative $\beta_\gamma$ of
    p. 345. Not claimed: that the source states Hatcher's exercise, or that it prints the relative
    proof it asserts.
---

::: {.problem}
Extend the results proved near the beginning of this section for the change-of-basepoint maps $\beta_\gamma$ to the case of relative homotopy groups.
:::

::: {.solution}
Hatcher's cubical model (printed p. 344): $I^{n-1}$ is the face $s_n=0$ of $I^n$, the free face; $J^{n-1}$ is the closure of $\partial I^n-I^{n-1}$; and $\pi_n(X,A,x_1)$ is the set of homotopy classes of maps $f:(I^n,\partial I^n,J^{n-1})\to(X,A,x_1)$, so $f(\partial I^n)\subseteq A$ and $f(J^{n-1})=x_1$. Because $I^{n-1}\subset\partial I^n$ the whole free face maps into $A$, and because $\partial I^{n-1}\subset J^{n-1}$ the boundary of the free face maps to the single point $x_1$. Hatcher defines $\gamma f$ on printed p. 345, for a path $\gamma$ in $A$ from $x_0$ to $x_1$, "by placing a copy of $f$ in a smaller cube with its face $I^{n-1}$ centered in the corresponding face of the larger cube", and leaves the properties to this exercise. The source for the properties is tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), §6.2, printed pp. 126--127; the solution below transcribes it and shows that Hatcher's $\gamma f$ is the value at $1$ of the homotopy the source constructs.

*The construction in Hatcher's cube.* Fix $\varepsilon\in(0,\tfrac13)$ and put
$$
Q=[\varepsilon,1-\varepsilon]^{n-1}\times[0,1-\varepsilon],\qquad
\varphi(s)=\Bigl(\frac{s_1-\varepsilon}{1-2\varepsilon},\dots,\frac{s_{n-1}-\varepsilon}{1-2\varepsilon},\frac{s_n}{1-\varepsilon}\Bigr),
$$
so that $\varphi:Q\to I^n$ is a homeomorphism carrying the face $B=[\varepsilon,1-\varepsilon]^{n-1}\times\{0\}$ of $Q$ onto the free face $I^{n-1}$ and every other face of $Q$ into $J^{n-1}$. The copy of $f$ sits in $Q$ and its free face $B$ sits in the interior of the free face of $I^n$, which is what "centered in the corresponding face" says. Write $S=I^n-\operatorname{int}Q$ for the shell and $\Sigma=I^{n-1}-\operatorname{int}B$ for the annulus of the free face outside $B$; then $\partial S=\partial I^n\cup\partial Q$ and $Q\cap S=\partial Q$. Choose a continuous $\delta:S\to[0,1]$ which is $0$ on the non-free faces of $I^n$, and hence on their closure, which contains $\partial I^{n-1}$; which is $1$ on the non-bottom faces of $Q$ and on $\partial B$; and which on $\Sigma$ runs from $0$ at $\partial I^{n-1}$ to $1$ at $\partial B$. Such a function exists, for example
$$
\delta(s)=1-\max\bigl(\nu(s_1,\dots,s_{n-1}),\tau(s_n)\bigr),\qquad
\nu=\max_i\max\Bigl\{\frac{\varepsilon-s_i}{\varepsilon},\frac{s_i-(1-\varepsilon)}{\varepsilon},0\Bigr\},\qquad
\tau=\max\Bigl\{\frac{s_n-(1-\varepsilon)}{\varepsilon},0\Bigr\},
$$
with both maxima truncated at $1$. Then
$$
\gamma f:I^n\longrightarrow X,\qquad
\gamma f(s)=\begin{cases}f(\varphi(s)),&s\in Q,\\[2pt] \gamma(\delta(s)),&s\in S\end{cases}
$$
is well defined and continuous: on a non-bottom face of $Q$ the first formula gives $f(\varphi(s))=x_1$ and the second $\gamma(1)=x_1$; on $\partial B$ the first gives $f(\varphi(s))=f(\partial I^{n-1})=x_1$ and the second $\gamma(1)=x_1$. It is a map of triples, since on the non-free faces and on $\Sigma$ the second formula gives $\gamma(\delta(s))\in A$, on $B\subset\partial I^n$ the first gives a point of $A$, and $J^{n-1}$ lies where $\delta=0$, so $\gamma f(J^{n-1})=\gamma(0)=x_0$. Note that the boundary values of $\delta$ cannot be $\delta^{-1}(0)=\partial I^n$, $\delta^{-1}(1)=\partial Q$: $B$ lies in both, and no point of $\operatorname{int}B$ is reached by the shell. What continuity at $\partial B$ needs is the value of $f$ on $\partial B$, not on $B$; the annulus $\Sigma$ is the piece of the shell that carries the interpolation, and it is exactly what centering the small free face in the large one adds.

*The source's transport.* (tom Dieck §6.2, printed pp. 126--127.) Let $v:I\to A$ be a path from $a_0$ to $a_1$ and $f:(I^n,\partial I^n,J^{n-1})\to(X,A,a_0)$ a map. The source reads $v$ as a homotopy of the constant map $J^{n-1}\to\{a_0\}$ and extends it to a homotopy $V_t:(I^n,\partial I^n)\to(X,A)$ with $V_0=f$; it says that an extension exists because $J^{n-1}\subset\partial I^n$ and $\partial I^n\subset I^n$ are cofibrations. Proposition (6.2.2), printed p. 127: the assignment $[V_0]\mapsto[V_1]$ is a well-defined map
$$
v_\#:\pi_n(X,A,a_0)\longrightarrow\pi_n(X,A,a_1)
$$
which depends only on the morphism $[v]$ in the fundamental groupoid $\Pi(A)$; for $n\ge2$ the map $v_\#$ is a homomorphism; and $v\mapsto v_\#$ is a transport functor from $\Pi(A)$, so $(v\cdot w)_\#=w_\#\circ v_\#$. The source states this in the relative case and writes the proof only in the absolute case, as (6.2.1) on printed pp. 126--127; the proof is:

> Let $\varphi:f\simeq g$ be a homotopy of maps $(I^n,\partial I^n)\to(X,x_0)$ and $\psi:v\simeq w$ a homotopy of paths from $x_0$ to $x_1$. Let $V_t$ extend $(f,\hat v)$ and $W_t$ extend $(g,\hat w)$. These data combine to a map on $T=I^n\times0\times I\;\cup\;\partial I^n\times I\times I\;\cup\;I^n\times I\times\partial I\subset I^{n+2}$ as follows: on $I^n\times0\times I$ use $\varphi$, on $\partial I^n\times I\times I$ use $\hat\psi$, on $I^n\times I\times0$ use $V$, and on $I^n\times I\times1$ use $W$. If we interchange the last two coordinates then $T$ is transformed into $J^{n+1}$. Therefore our map has an extension to $I^{n+2}$, and its restriction to $I^n\times1\times I$ is a homotopy from $V_1$ to $W_1$. This shows the independence of the representatives $f$ and $v$. The other properties are clear from the construction.

The same $T$ serves the relative case, with $J^{n-1}$ carrying the path $v$ and $\partial I^n$ carrying $A$. The source writes the proof for the absolute case only, and in (6.2.2) refers the functor property back to it with the words "As above"; the one point it leaves implicit is that the pair condition $V_t(\partial I^n)\subseteq A$ forces the boundary of the free face to be carried along $v$ inside $A$, which the absolute case in degree $n-1$ supplies. Adjoining (6.2.2) the source records that $v_\#$ is always bijective, and Proposition (6.2.3), printed p. 127, states that the morphisms in the exact homotopy sequence of the pair $(X,A)$ are natural transformations of transport functors on $\Pi(A)$, hence $\pi_1(A,\cdot)$-equivariant.

*Hatcher's $\gamma f$ realizes this transport.* Put $v=\bar\gamma$, the path from $x_1$ to $x_0$ given by $\bar\gamma(t)=\gamma(1-t)$, and for $t\in[0,1]$ let
$$
Q_t=[t\varepsilon,1-t\varepsilon]^{n-1}\times[0,1-t\varepsilon],\qquad
V_t(s)=\begin{cases}f(\varphi_t(s)),&s\in Q_t,\\ \gamma\bigl(1-t+t\rho_t(s)\bigr),&s\notin\operatorname{int}Q_t,\end{cases}
$$
where $\varphi_t:Q_t\to I^n$ is the rescaling of the construction above and $\rho_t$ is the corresponding $\delta$. Then $Q_0=I^n$ and $V_0=f$; $Q_1=Q$ and $V_1=\gamma f$; $V_t$ is a map of pairs for every $t$, since for $t>0$ the boundary $\partial I^n$ lies in the shell and its image is $\gamma(1-t+t\rho_t)\in A$; and $V_t(J^{n-1})=\gamma(1-t)=v(t)$, since $\rho_t$ vanishes on $\partial I^n$. The family is continuous at $t=0$ as well: as $t\to0$ the annulus $\Sigma_t$ shrinks onto the edge $\partial I^{n-1}$, where $f$ and $\gamma$ agree at the value $x_1$. So $V_t$ is the homotopy the source constructs for the path $\bar\gamma$, and therefore
$$
[\gamma f]=(\bar\gamma)_\#([f]),\qquad\text{that is}\qquad \beta_\gamma=(\bar\gamma)_\# ,
$$
the directions agreeing because $\bar\gamma$ runs from $x_1$ to $x_0$.

*The properties follow from the source.* Well-definedness, dependence of $\beta_\gamma$ only on the class of $\gamma$ rel endpoints, and the composition law are (6.2.2) and the functoriality of $v\mapsto v_\#$, applied to $v=\bar\gamma$ and to $\overline{\gamma\eta}=\bar\eta\,\bar\gamma$:
$$
\beta_{\gamma\eta}=(\overline{\gamma\eta})_\#=(\bar\eta\bar\gamma)_\#=(\bar\gamma)_\#(\bar\eta)_\#=\beta_\gamma\beta_\eta .
$$
Bijectivity: $\beta_{\bar\gamma}\beta_\gamma=\beta_{\bar\gamma\gamma}=\mathrm{id}$ on $\pi_n(X,A,x_1)$ and $\beta_\gamma\beta_{\bar\gamma}=\beta_{\gamma\bar\gamma}=\mathrm{id}$ on $\pi_n(X,A,x_0)$, since each of $\bar\gamma\gamma$ and $\gamma\bar\gamma$ is homotopic rel endpoints to the constant path at its basepoint, where the transport is the identity. The two composites are endomorphisms of groups at different basepoints, which is why the concatenations are written in that order: by the rule $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$ the path $\gamma$ is traversed first.

*Additivity.* (6.2.2) asserts that $v_\#$ is a homomorphism for $n\ge2$ without printing the argument, which in the relative case is not the absolute one. For $n\ge2$ the group structure on $\pi_n(X,A,x_1)$ comes from the first coordinate, which is not the special coordinate $s_n$, and $\beta_\gamma([f]+[g])=\beta_\gamma[f]+\beta_\gamma[g]$ is the relative form of Hatcher's formula (1) on p. 341. On the inner cube $Q$ the map $\gamma(f+g)$ is $f$ on the half with the rescaled first coordinate in $[0,\tfrac12]$ and $g$ on the other half. On the other hand $\gamma f+\gamma g$ is $f$ and $g$ on the two boxes
$$
Q_1=\bigl[\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2}\bigr]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon],\qquad
Q_2=\bigl[\tfrac{1+\varepsilon}{2},1-\tfrac{\varepsilon}{2}\bigr]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon],
$$
mapped through $\varphi$ composed with the doubling of the first coordinate, and $\gamma(\delta)$ elsewhere. Both maps are assembled from the same three ingredients — $f$ on a box, $g$ on a box, and $\gamma$ on the complement — and differ only in the position of the two boxes. For $u\in[0,1]$ put $c_u=\varepsilon(1-\tfrac u2)$ and $d_u=\tfrac12(1-u\varepsilon)$, so that $(c_0,d_0)=(\varepsilon,\tfrac12)$ and $(c_1,d_1)=(\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2})$, and move the two boxes to $[c_u,d_u]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon]$ and its mirror image $[1-d_u,1-c_u]\times\cdots$, carrying $f$ and $g$ with the first argument the affine map of the box onto $[0,1]$ and the shell carrying $\gamma$ composed with the corresponding distance function. Every stage is a map of triples: the boundary of each moving box carries $x_1$ on the $f$- and $g$-side, where the first argument is $0$ or $1$, and $\gamma(1)=x_1$ on the shell side; the boxes stay inside $[\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2}]$ and its mirror image, so they never meet. At $u=0$ this is $\gamma(f+g)$ and at $u=1$ it is $\gamma f+\gamma g$, so $\beta_\gamma(f+g)\simeq\beta_\gamma f+\beta_\gamma g$ and $\beta_\gamma$ is a homomorphism for $n\ge2$.

*Compatibility with the exact sequence.* This is Proposition (6.2.3) of the source. In the cubical model the boundary map $\partial:\pi_n(X,A,x_1)\to\pi_{n-1}(A,x_1)$ restricts a representative to the face $s_n=0$, and the restriction of $\gamma f$ to that face is the copy $f\circ\varphi$ on $B$, which is the restriction of $f$ to the free face, together with $\gamma(\delta)$ on the annulus $\Sigma$; that is exactly the absolute $\gamma\restrictionof{f}{I^{n-1}}$ of p. 341, whose shell is $\Sigma$ and whose inner cube is $B$. So $\partial\beta_\gamma=\beta_\gamma\partial$ for the absolute change-of-basepoint maps on $\pi_{n-1}(A,x_1)$, and with naturality this says that the action of $\pi_1(A,x_0)$ on the relative groups by $[\gamma]\mapsto\beta_\gamma$ commutes with every map of the long exact sequence of the pair, as Hatcher states on p. 345, and that $\pi_n(X,A,x_0)$ is independent of the basepoint in $A$ when $A$ is path-connected.

Checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 7, printed p. 358 ("Extend the results proved near the beginning of this section for the change-of-basepoint maps $\beta_\gamma$ to the case of relative homotopy groups"), with the three results of p. 341 and Hatcher's description of the relative $\beta_\gamma$ on p. 345.
:::

::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), §6.2, printed pp. 126--127: the transport functor along paths, Proposition (6.2.1) with its full proof in the absolute case, Proposition (6.2.2) for the relative case — well-definedness, dependence on the path class only, the homomorphism property for $n\ge2$ and functoriality — and Proposition (6.2.3) for the compatibility with the exact sequence of the pair. The source writes the proof only for the absolute case and asserts the relative one; the argument for the relative case, and the identification of Hatcher's $\gamma f$ with the transport along the reversed path, are written out above. The exercise is Exercise 7 of §4.1, printed p. 358, and Hatcher describes the relative $\beta_\gamma$ on p. 345.
:::
