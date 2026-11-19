---
schema: qual/card@1
id: E-HAT-4.1-5
kind: problem
title: "Relative $\\pi_1$ as cosets"
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
  note: Checked against Hatcher Section 4.1 Exercise 5 and the 2021-06-02 correction; corrected the stored coset from alpha H to H alpha.
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
    Read line by line. Correct, both directions. A relative path `u` with `u(0) in A`, `u(1) = x_0` and
    a path `v` in `A` from `x_0` to `u(0)` give the loop `vu`, and the left coset `H[vu]` is well
    defined because another choice `v'` differs by the loop `v'v^{-1}` in `A`, i.e. by an element of
    `H = i_* pi_1(A,x_0)`. Conversely a loop at `x_0` is a relative path with initial point in `A`, and
    two loops give the same relative class exactly when `[alpha'][alpha]^{-1} in H`, i.e. exactly when
    the left cosets agree. The bijection is with the *left* cosets `H \ pi_1(X,x_0)`, the side the card
    displays, and it is natural in the pair.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The problem block had replaced the print's "the set of cosets $\alpha H$" by "$H\alpha$". The
    printed wording is restored, and the solution now says which family of cosets the relative classes
    actually give and why: replacing the path $v$ replaces $[vu]$ by the left multiple
    $[v'v^{-1}][vu]$, so the invariant is $\{h\alpha\}$ with $H$ on the left. Since
    $H=i_*\pi_1(A,x_0)$ need not be normal, $\{h\alpha\}$ and $\{\alpha h\}$ are different families,
    and the print's $\alpha H$ has to be read as $\{h\alpha\}$ here; the card states this instead of
    silently changing the book's notation. Read against Hatcher, Algebraic Topology (2002), §4.1
    Exercise 5, printed p. 358, with the definition of $\pi_1(X,A,x_0)$ on p. 344. Sam's solution of
    this exercise (printed pp. 17-18) reaches the same identification and also writes $\alpha H$; his
    proof is the second construction on the card.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The two constructions are now given
    as mutually inverse maps rather than as two halves of a bijection: Phi sends a relative class
    to the left coset H[v nu], and is well defined because another choice v' of the path in A
    multiplies on the left by [v'v^{-1}] in H, and a relative homotopy moves the initial point
    along a path w in A so that vw^{-1} replaces v; Psi sends a left coset H[omega] to the
    relative class of the loop omega read as a path from A to x_0, and is well defined because
    [omega'] = h[omega] means omega' is relatively homotopic to omega with the initial point
    moving along a loop in A. The composite checks are written out. The card's own remark about
    the printed notation is kept as a step, with the reason: only left multiplication arises, and
    H need not be normal, so the printed alpha H is to be read as {h alpha}. Statement unchanged;
    the card says the argument is its own.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Notation repair after the corpus check reported raw TeX the page cannot show. One sentence
    names Hatcher's section as `\S4.1`, a section sign written as a TeX command outside a math
    span, which the HTML writer drops; it now reads the character `§4.1`, as the corpus does
    elsewhere. Mathematics and wording unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card said no retained solution set covers this exercise, and that is false: Sam's set,
    retained as `tmp/sources/hatcher-solutions-sam-2008.pdf`, solves it at §4.1 Exercise 5 on
    printed p. 17, and the card's own 2026-11-07 event already recorded that. The rendered
    sentence now cites it and says which construction is Sam's. Found by screening the residue's
    absence claims against the solution sets inventoried in
    `wiki/topology/resources/solutions.md`; no step of the proof changed.
---

::: {.problem}
For a pair $(X, A)$ of path-connected spaces, show that $\pi_1(X, A, x_0)$ can be identified in a natural way with the set of cosets $\alpha H$ of the subgroup $H \subset \pi_1(X, x_0)$ represented by loops in $A$ at $x_0$.
:::

::: {.solution}
An element of $\pi_1(X,A,x_0)$ is a path $\nu$ from $A$ to $x_0$, up to homotopies that keep the endpoint at $x_0$ and let the initial point move inside $A$; since $A$ is path-connected, prepending a path in $A$ from $x_0$ to $\nu(0)$ makes it a loop, and changing that path or $\nu$ multiplies the loop on the left by an element of $H=i_*\pi_1(A,x_0)$. The two constructions, relative class $\mapsto$ left coset and left coset $\mapsto$ relative class of a representing loop, are mutually inverse because a path in $A$ may be absorbed into the allowed motion of the initial point. The card records that the printed $\alpha H$ must be read as $\{h\alpha\}$, with $H$ on the left. The second construction is the retained solution set's: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.1 Exercise 5**, printed p. 17 of `tmp/sources/hatcher-solutions-sam-2008.pdf`, identifies the relative classes with the cosets $\alpha H$ through the surjection from loops at $x_0$ and the criterion that $\gamma_0^{-1}\gamma_1$ be a loop in $A$. The two mutually inverse maps are the card's arrangement of that identification.

::: pf

::: {.pf-step #model}
An element of $\pi_1(X,A,x_0)$ is represented by a path $\nu\colon I\to X$ with $\nu(0)\in A$ and $\nu(1)=x_0$, two such being identified when homotopic through paths whose endpoint is $x_0$ throughout and whose initial point stays in $A$.

::: pf-proof
This is Hatcher's definition in §4.1. The set is a pointed set with basepoint the constant path at $x_0$, whose initial point is $x_0\in A$; no group structure is used below.
:::

:::


::: {.pf-step #map}
Choosing for each relative class $[\nu]$ a path $v$ in $A$ from $x_0$ to $\nu(0)$ and setting $\Phi([\nu])=H[v\nu]$ gives a well-defined map $\Phi$ from $\pi_1(X,A,x_0)$ to the set of left cosets of $H$ in $\pi_1(X,x_0)$.

::: pf-proof
$v\nu$ is a loop at $x_0$, so $[v\nu]\in\pi_1(X,x_0)$ and $H[v\nu]$ is a left coset, a subset of the group. If $v'$ is another path in $A$ from $x_0$ to $\nu(0)$, then $v'v^{-1}$ is a loop in $A$, so $[v'v^{-1}]\in H$ and $[v'\nu]=[v'v^{-1}][v\nu]$ gives $H[v'\nu]=H[v\nu]$. If $\nu'$ is relatively homotopic to $\nu$, the homotopy moves the initial point along a path $w$ in $A$ from $\nu(0)$ to $\nu'(0)$, so $vw^{-1}$ is a path in $A$ from $x_0$ to $\nu'(0)$ and $[vw^{-1}\nu']=[v\nu]$; by the first part, $H[v\nu]$ is then the value computed with the path $vw^{-1}$, which is the value attached to $[\nu']$. So $\Phi$ is independent of the choices.
:::

:::


::: {.pf-step #inverse}
Defining $\Psi$ on a left coset by $\Psi(H[\omega])=\text{the relative class of }\omega$, for $\omega$ a loop at $x_0$ read as a path from $A$ to $x_0$, gives a well-defined map inverse to $\Phi$.

::: pf-proof
A left coset has the form $H[\omega]$ with $\omega$ a loop at $x_0$, and $\omega(0)=x_0\in A$, so $\omega$ does define an element of $\pi_1(X,A,x_0)$. If $H[\omega']=H[\omega]$, then $[\omega']=h[\omega]$ with $h=[\lambda]$, $\lambda$ a loop in $A$ at $x_0$; so $\omega'\simeq\lambda\omega$ in $X$ relative to endpoints, and $\lambda\omega$ is relatively homotopic to $\omega$ because the initial point may move along $\lambda$, which lies in $A$. Hence $\omega'$ and $\omega$ define the same relative class and $\Psi$ is well defined.
:::

:::


::: {.pf-step #composites}
$\Psi\circ\Phi$ and $\Phi\circ\Psi$ are the identities.

::: pf-proof
For a relative class $[\nu]$, $\Phi([\nu])=H[v\nu]$ and $v\nu$ is a loop at $x_0$, so $\Psi(\Phi([\nu]))$ is the relative class of the loop $v\nu$. The path $v$ lies in $A$, so moving the initial point along $v$ is an allowed homotopy, and $v\nu$ is relatively homotopic to $\nu$; hence $\Psi\Phi[\nu]=[\nu]$. For a coset $H[\omega]$, $\Psi$ gives the relative class of $\omega$, and $\Phi$ of it is $H[v\omega]$ computed with the path $v$ in $A$ from $x_0=\omega(0)$ to $\omega(0)$, which may be taken constant; then $[v\omega]=[\omega]$ and $\Phi\Psi(H[\omega])=H[\omega]$. So the two maps are mutually inverse.
:::

:::


::: {.pf-step #natural}
The bijection is natural in the triple, and the printed $\alpha H$ denotes the family $\{h\alpha:h\in H\}$.

::: pf-proof
A map of triples $g\colon(X,A,x_0)\to(Y,B,y_0)$ carries paths from $A$ to $x_0$ to paths from $B$ to $y_0$ and preserves relative homotopies, and $g_*\colon\pi_1(X,x_0)\to\pi_1(Y,y_0)$ is a homomorphism with $g_*(H)\subseteq i_*\pi_1(B,y_0)$. Hence the coset attached to $g[\nu]$ is $g_*(H)\,[g\circ v\cdot g\circ\nu]$, which is the image of $H[v\nu]$ under $g_*$; that is naturality. For the side: step [](#map){.pf-ref} produces the family with $H$ multiplying on the left, and the only freedom, replacing $v$ by $v'$, multiplies on the left; nothing multiplies on the right. Since $H$ need not be normal in $\pi_1(X,x_0)$, the families $\{h\alpha\}$ and $\{\alpha h\}$ differ in general, so the printed $\alpha H$ is read as the set of left cosets.
:::

:::


::: {.pf-step #conclusion}
$\pi_1(X,A,x_0)$ is naturally identified with the set of left cosets of $H=i_*\pi_1(A,x_0)$ in $\pi_1(X,x_0)$, for $A$ path-connected.

::: pf-proof
Steps [](#map){.pf-ref}, [](#inverse){.pf-ref} and [](#composites){.pf-ref} give the bijection of pointed sets, and step [](#natural){.pf-ref} gives naturality together with the reading of the printed notation.
:::

:::

:::
:::
