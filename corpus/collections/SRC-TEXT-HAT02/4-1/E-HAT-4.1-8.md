---
schema: qual/card@1
id: E-HAT-4.1-8
kind: problem
title: "Exactness of $\\pi_1$ sequence for pairs"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 8; the stored statement matches.
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
    Read line by line. Correct, in Hatcher's convention where a relative path has `u(0) = x_0` and
    `u(1) in A` and `partial[u] = [u(1)]`. At `pi_1(X,A,x_0)`: `[u]` is in the kernel exactly when `u(1)`
    lies in the component of `x_0` in `A`, and then a path `v` in `A` from `u(1)` back to `x_0` turns `u`
    into the loop `uv`, whose relative class is that of `u`; so the kernel is the image of
    `pi_1(X,x_0)`. At `pi_0(A,x_0)`: a component lies in the image of `partial` exactly when it is joined
    to `x_0` by a path in `X`, i.e. exactly when it maps to the distinguished component of `X`. Exactness
    as pointed sets follows. No correction was needed.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The earlier note on this card recorded Hatcher's convention wrongly. Hatcher p. 344 defines
    $\pi_1(X,A,x_0)$ as the set of homotopy classes of paths in $X$ "from a varying point in $A$ to
    the fixed basepoint $x_0\in A$", so $u(0)\in A$, $u(1)=x_0$ and $\partial[u]=[u(0)]$; the card had
    used the reversed convention $u(0)=x_0$, $u(1)\in A$, $\partial[u]=[u(1)]$, which is not
    Hatcher's and disagreed with the sibling cards 4.1-5 and 4.1-6. The solution is rewritten in the
    book's convention, with $\partial[u]=[u(0)]$, the loop $vu$ formed from a path $v$ in $A$ from
    $x_0$ to $u(0)$, and the homotopy that traverses $v$ only on $[0,1-s]$ written out.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 8, printed p. 358. This exercise
    does have a complete published solution in the retained sets: Kenneth DeMason, M382C Full Credit
    HW Problems, §4.1 exercise 8, printed p. 89, proves both exactness statements — $\ker\beta$ is
    contained in the image of $\partial$ because a component of $A$ inside the component of $x_0$ in
    $X$ is joined to $x_0$ by a path in $X$, and $\ker\partial\subseteq\ker$ of the inclusion because
    the endpoint can be slid along a path in $A$; that is the argument the card carries, with the
    endpoint-sliding homotopy written out and in Hatcher's convention. DeMason works in the reverse
    convention, with representatives $f(0)=x_0$, $f(1)\in A$ and $\partial[f]$ the component of
    $f(1)$; the two conventions give the same sequence and the same two verifications. No statement
    defect was found: the sequence as printed is exact with no hypothesis on $A$ beyond $x_0\in A$.
---

::: {.problem}
Show the sequence $\pi_1(X, x_0) \to \pi_1(X, A, x_0) \overset{\partial}{\longrightarrow} \pi_0(A, x_0) \to \pi_0(X, x_0)$ is exact.
:::

::: {.solution}
Use Hatcher's conventions (§4.1, p. 344): an element of $\pi_1(X,A,x_0)$ is represented by a path $u:I\to X$ with $u(0)\in A$ and $u(1)=x_0$, and two such paths are identified when they are homotopic through paths of the same form. The three maps of the displayed sequence are the inclusion of loops at $x_0$ (a loop is a path of the required form, since $x_0\in A$), the boundary map
$$
\partial[u]=[u(0)]\in\pi_0(A,x_0),
$$
and the map $\pi_0(A,x_0)\to\pi_0(X,x_0)$ induced by the inclusion $A\subset X$, all as pointed sets.

*Exactness at $\pi_1(X,A,x_0)$.* The composite is trivial: for a loop $\alpha$ at $x_0$, viewed as a relative path, $\partial[\alpha]=[x_0]$ is the distinguished element. Conversely let $[u]\in\ker\partial$, so $u(0)$ lies in the component of $x_0$ in $A$. Choose a path $v$ in $A$ from $x_0$ to $u(0)$; then $vu$, first $v$ and then $u$, is a loop at $x_0$. The relative classes of $vu$ and $u$ agree: the family $u_s$ that traverses $v$ only on $[0,1-s]$ and then $u$ rescaled to $[1-s,1]$ is a homotopy through paths from $A$ to $x_0$, because $v$ lies in $A$ so every initial point $v(\cdot)$ is in $A$, and $u_0=vu$, $u_1=u$. Hence $[u]$ is the image of the loop class $[vu]$.

*Exactness at $\pi_0(A,x_0)$.* The image of $\partial$ consists of the components of $A$ containing a point that is joined to $x_0$ by a path in $X$, and these are exactly the components whose image in $\pi_0(X,x_0)$ is the component of $x_0$. So $\operatorname{im}\partial=\ker\bigl(\pi_0(A,x_0)\to\pi_0(X,x_0)\bigr)$.

Thus the sequence is exact as a sequence of pointed sets. No hypothesis that $A$ be path-connected is needed; when $A$ is path-connected, as in the preceding exercise, $\pi_0(A,x_0)$ is a single point.
:::
