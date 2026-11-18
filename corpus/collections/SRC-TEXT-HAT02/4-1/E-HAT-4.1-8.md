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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located among the retained Hatcher sets, so the argument is the card's own. Checked against
    Hatcher, Section 4.1, printed pp. 342-345, for the definition of $\pi_1(X,A,x_0)$ as relative
    paths up to homotopy through relative paths and for the boundary map. Each step re-read: the
    composite $\partial\circ i$ is trivial because a loop starts at $x_0$; a class with
    $\partial[u]=[x_0]$ is homotopic, through relative paths, to the loop obtained by first
    traversing a path in $A$ from $x_0$ to $u(0)$; and the image of $\partial$ is exactly the set
    of components of $A$ that meet the component of $x_0$ in $X$. Exactness of a sequence of
    pointed sets is read as image = preimage of the basepoint. Not claimed: path-connectedness of
    $A$, which is not needed and is not assumed.
---

::: {.problem}
Show the sequence $\pi_1(X, x_0) \to \pi_1(X, A, x_0) \overset{\partial}{\longrightarrow} \pi_0(A, x_0) \to \pi_0(X, x_0)$ is exact.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves Section 4.1 Exercise 8. It is checked against Hatcher, Algebraic Topology, Section 4.1, printed pp. 342--345, where $\pi_1(X,A,x_0)$ is defined as the set of homotopy classes of paths $u:I\to X$ with $u(0)\in A$ and $u(1)=x_0$, homotopies being through paths of the same form, and the boundary map is $\partial[u]=[u(0)]$.

::: pf

::: {.pf-step #conventions}
The three maps of the sequence are: the inclusion of loops at $x_0$ into relative paths, since a loop is a path with both endpoints $x_0\in A$; the boundary map $\partial[u]=[u(0)]\in\pi_0(A,x_0)$; and the map $\pi_0(A,x_0)\to\pi_0(X,x_0)$ induced by the inclusion $A\subset X$. All are maps of pointed sets, the basepoints being the constant path and the component of $x_0$.

::: pf-proof
A loop at $x_0$ satisfies $u(0)=x_0\in A$ and $u(1)=x_0$, so it represents an element of $\pi_1(X,A,x_0)$, and the assignment is compatible with homotopies because a homotopy of loops rel endpoints is a homotopy through relative paths. The boundary map is well defined because a homotopy through paths from $A$ to $x_0$ moves $u(0)$ inside $A$, so it does not change the component of $A$ containing $u(0)$. The third map is the usual map on components.
:::

:::

::: {.pf-step #atpi1}
The sequence is exact at $\pi_1(X,A,x_0)$.

:::: pf-proof

::: {.pf-step #trivial}
$\partial$ composed with the inclusion is trivial.

::: pf-proof
If $\alpha$ is a loop at $x_0$ then $\partial[\alpha]=[\alpha(0)]=[x_0]$, the basepoint of $\pi_0(A,x_0)$.
:::

:::

::: {.pf-step #kernel}
Every class in the kernel of $\partial$ comes from a loop.

::: pf-proof
Let $[u]\in\pi_1(X,A,x_0)$ with $\partial[u]=[x_0]$, that is, $u(0)$ lies in the component of $x_0$ in $A$. Choose a path $v:I\to A$ from $x_0$ to $u(0)$, and let $vu$ be the path that traverses $v$ on $[0,\tfrac12]$ and $u$ reparametrised on $[\tfrac12,1]$; this is a loop at $x_0$. The family
$$
u_s(t)=\begin{cases} v\bigl((1-s)t\bigr), & t\le s,\\ u\Bigl(\dfrac{t-s}{1-s}\Bigr), & t\ge s,\end{cases}
$$
with the evident interpretation at $s=1$, is a homotopy from $u_1=u$ to $u_0=vu$ through paths whose initial point is $v\bigl((1-s)\cdot0\bigr)\in A$ and whose final point is $x_0$. Hence $[u]=[vu]$ in $\pi_1(X,A,x_0)$, and $[vu]$ is the image of the loop class of $vu$.
:::

:::

:::

:::

::: {.pf-step #atpi0}
The sequence is exact at $\pi_0(A,x_0)$.

::: {.pf-proof}
The image of $\partial$ consists of the components $[a]$ of $A$ for which there is a path $u$ in $X$ from $a$ to $x_0$, since such a $u$ is exactly a relative path with $u(0)=a$. A component $[a]$ of $A$ maps to the basepoint of $\pi_0(X,x_0)$ exactly when $a$ can be joined to $x_0$ by a path in $X$, that is, exactly when $[a]$ is the image of some $\partial[u]$. So the image of $\partial$ equals the kernel of $\pi_0(A,x_0)\to\pi_0(X,x_0)$.
:::

:::

::: {.pf-step}
The sequence $\pi_1(X,x_0)\to\pi_1(X,A,x_0)\xrightarrow{\partial}\pi_0(A,x_0)\to\pi_0(X,x_0)$ is exact.

::: pf-proof
Exactness at the two middle terms is steps [](#atpi1){.pf-ref} and [](#atpi0){.pf-ref}. No hypothesis that $A$ be path-connected is used: when $A$ is path-connected, $\pi_0(A,x_0)$ is a single point, but the argument above does not need that.
:::

:::

:::
:::
