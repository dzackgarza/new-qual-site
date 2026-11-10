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
---

::: {.problem}
Extend the results proved near the beginning of this section for the change-of-basepoint maps $\beta_\gamma$ to the case of relative homotopy groups.
:::

::: {.solution}
Use Hatcher's cubical model (p. 344): $I^{n-1}$ is the face $s_n=0$ of $I^n$, $J^{n-1}$ is the closure of $\partial I^n-I^{n-1}$, and $\pi_n(X,A,x_1)$ is the set of homotopy classes of maps
$$
f:(I^n,\partial I^n,J^{n-1})\longrightarrow(X,A,x_1),
$$
that is, $\partial I^n$ maps into $A$ and $J^{n-1}$ maps to $x_1$. Hatcher introduces $\beta_\gamma$ for a path $\gamma$ in $A$ from $x_0$ to $x_1$ by "placing a copy of $f$ in a smaller cube with its face $I^{n-1}$ centered in the corresponding face of the larger cube" (p. 345) and leaves the properties to this exercise. Here is the construction with the rescaling written out.

*The construction.* Fix $\varepsilon\in(0,\tfrac12)$ and put
$$
Q=\bigl[\varepsilon,1-\varepsilon\bigr]^{n-1}\times\bigl[0,1-\varepsilon\bigr],\qquad
\varphi(s)=\Bigl(\frac{s_1-\varepsilon}{1-2\varepsilon},\dots,\frac{s_{n-1}-\varepsilon}{1-2\varepsilon},\frac{s_n}{1-\varepsilon}\Bigr),
$$
so that $\varphi:Q\to I^n$ is a homeomorphism carrying the face $s_n=0$ of $Q$ into the face $s_n=0$ of $I^n$ and the remaining faces of $Q$ into $J^{n-1}$. Choose a continuous $\delta:I^n\to[0,1]$ with $\delta^{-1}(0)=\partial I^n$ and $\delta^{-1}(1)=\partial Q$, for instance $\delta(s)=d(s,\partial I^n)/\bigl(d(s,\partial I^n)+d(s,\partial Q)\bigr)$ on $I^n-\operatorname{int}Q$. Define
$$
\gamma f:I^n\longrightarrow X,\qquad
\gamma f(s)=\begin{cases} f(\varphi(s)),&s\in Q,\\[2pt] \gamma(\delta(s)),&s\notin\operatorname{int}Q,\end{cases}
$$
and set $\beta_\gamma([f])=[\gamma f]$. This is continuous because on $\partial Q$ the two formulas agree: $\varphi(\partial Q)\subset\partial I^n$ with the faces $s_n=0$ of $Q$ mapping to the boundary of the free face and the other faces mapping into $J^{n-1}$, so $f(\varphi(s))=x_1=\gamma(1)$ there. It is a map of triples: for $s\in\partial I^n$ one has $s\notin\operatorname{int}Q$, so $\gamma f(s)=\gamma(\delta(s))=\gamma(0)=x_0$, and $x_0\in A$; in particular $J^{n-1}$ maps to $x_0$.

*Well defined.* If $f_t$ is a homotopy of maps of triples from $f$ to $f'$, then $\gamma f_t$ is one from $\gamma f$ to $\gamma f'$: the formula is applied to $f_t$ inside $Q$ with the shell map unchanged. So $\beta_\gamma$ is a well-defined map of sets, and it is natural: for a map of triples $\psi:(X,A,x_1)\to(Y,B,y_1)$ one has $\psi(\gamma f)=(\psi\gamma)(\psi f)$, so $\psi_*\beta_\gamma=\beta_{\psi\gamma}\psi_*$.

*Constant path.* If $\gamma$ is the constant path at $x_0=x_1$, then $\beta_\gamma[f]=[f]$: the map $\gamma f$ equals $f\circ\varphi$ on $Q$ and $x_0$ on the shell, and the family obtained by replacing $Q,\varphi,\delta$ by $Q_u,\varphi_u,\delta_u$ with $u\in(0,1]$ and $Q_u=[u\varepsilon,1-u\varepsilon]^{n-1}\times[0,1-u\varepsilon]$ is a homotopy of maps of triples from $\gamma f$ to $f$ as $u\to0$, since the shell shrinks onto $\partial I^n$ and its image is the single point $x_0$ throughout. Hence $\beta_{\bar\gamma}\beta_\gamma=\beta_{\gamma\bar\gamma}=\mathrm{id}$ and $\beta_\gamma$ is a bijection, where $\bar\gamma(s)=\gamma(1-s)$.

*Concatenation.* For paths $\gamma$ from $x_0$ to $x_1$ and $\eta$ from $x_1$ to $x_2$ in $A$ one has $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$: both sides are the map that puts $f$ in a small cube and fills the shell by $\eta$ near the cube and by $\gamma$ near the boundary, and the family that moves the radius at which the shell switches from $\eta$ to $\gamma$ is a homotopy of maps of triples, the shell always lying in $A$. In particular $\beta_\gamma$ depends only on the homotopy class of $\gamma$ rel endpoints, by the same sliding of the shell.

*Additivity.* For $n\ge2$ the group structure on $\pi_n(X,A,x_1)$ comes from the first coordinate, which is not the special coordinate, so $f+g$ is defined by the usual formula in $s_1$. We show $\beta_\gamma([f]+[g])=\beta_\gamma[f]+\beta_\gamma[g]$, the relative form of Hatcher's formula (1) on p. 341.

On the inner cube $Q$ the map $\gamma(f+g)$ equals $(f+g)\circ\varphi$; since $\varphi$ does not change the first coordinate except by the affine reparametrization $s_1\mapsto(s_1-\varepsilon)/(1-2\varepsilon)$, this is $f$ on the part of $Q$ with $(s_1-\varepsilon)/(1-2\varepsilon)\le\tfrac12$ and $g$ on the rest, with the last and transverse coordinates rescaled exactly as in $\gamma f$ and $\gamma g$. On the other hand $\gamma f+\gamma g$ is $f$ and $g$ on the two boxes
$$
Q_1=\bigl[\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2}\bigr]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon],\qquad
Q_2=\bigl[\tfrac{1+\varepsilon}{2},1-\tfrac{\varepsilon}{2}\bigr]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon],
$$
mapped through $\varphi$ composed with the doubling of the first coordinate, and $\gamma(\delta)$ elsewhere. Both maps are therefore assembled from the same three ingredients — $f$ on a box, $g$ on a box, and $\gamma$ on the complement — and they differ only in the position of the two boxes. Precisely, on $Q$ the map $\gamma(f+g)$ is $f$ on the box $\{s\in Q:\ s_1\le\tfrac12\}=[\varepsilon,\tfrac12]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon]$ with first argument $2\,(s_1-\varepsilon)/(1-2\varepsilon)$, and $g$ on the mirror box $[\tfrac12,1-\varepsilon]\times\cdots$ with first argument $2(s_1-\varepsilon)/(1-2\varepsilon)-1$; on $Q_1,Q_2$ the map $\gamma f+\gamma g$ is $f$, respectively $g$, with first argument the affine map of $[\varepsilon/2,(1-\varepsilon)/2]$, respectively of $[(1+\varepsilon)/2,1-\varepsilon/2]$, onto $[0,1]$. For $u\in[0,1]$ let
$$
c_u=\varepsilon\bigl(1-\tfrac u2\bigr),\qquad d_u=\tfrac12\bigl(1-u\varepsilon\bigr),
$$
so that $(c_0,d_0)=(\varepsilon,\tfrac12)$ and $(c_1,d_1)=(\tfrac{\varepsilon}{2},\tfrac{1-\varepsilon}{2})$, and let the moving boxes be $[c_u,d_u]\times[\varepsilon,1-\varepsilon]^{n-2}\times[0,1-\varepsilon]$ and its mirror image $[1-d_u,1-c_u]\times\cdots$, carrying $f$ and $g$ with first argument the affine map of the box onto $[0,1]$ and the shell carrying $\gamma$ composed with the corresponding distance function. Every stage is a map of triples, because the boundary of each moving box carries $x_1$ on the $f$- and $g$-side (the first argument is then $0$ or $1$) and $\gamma(1)=x_1$ on the shell side; and $u=0$ gives $\gamma(f+g)$ while $u=1$ gives $\gamma f+\gamma g$. Hence $\beta_\gamma(f+g)\simeq\beta_\gamma f+\beta_\gamma g$ and $\beta_\gamma$ is a homomorphism for $n\ge2$.

*Compatibility with the exact sequence.* The boundary map $\partial:\pi_n(X,A,x_1)\to\pi_{n-1}(A,x_1)$ restricts a representative to the face $s_n=0$. Under the construction, the restriction of $\gamma f$ to that face is the same construction applied to the restriction of $f$, with the same shell; so $\partial\beta_\gamma=\beta_\gamma\partial$ for the absolute change-of-basepoint maps on $\pi_{n-1}(A,x_1)$. Together with naturality, this says the action of $\pi_1(A,x_0)$ on the relative groups by $[\gamma]\mapsto\beta_\gamma$ commutes with every map of the long exact sequence of the pair, as Hatcher states on p. 345, and that $\pi_n(X,A,x_0)$ is independent of the basepoint in $A$ when $A$ is path-connected.
:::
