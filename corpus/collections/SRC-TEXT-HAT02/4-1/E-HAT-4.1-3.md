---
schema: qual/card@1
id: E-HAT-4.1-3
kind: problem
title: "H-space multiplication gives group structure on $\\pi_n$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 3; the stored statement matches.
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
    Read line by line. Correct. `mu_*` is a homomorphism because it is a map of groups between
    `pi_n(X) x pi_n(X)`, whose group structure is componentwise, and `pi_n(X x X) = pi_n(X) x pi_n(X)`;
    the unit conditions give `mu_*(a,0) = a` and `mu_*(0,b) = b`; hence
    `mu_*(a,b) = mu_*((a,0)+(0,b)) = a + b`, and the composite class is represented by
    `x |-> mu(f(x),g(x))`. One hypothesis the card does not name: calling this *the* group operation
    presupposes `pi_n` is a group for this `mu`, i.e. that `mu` is homotopy associative; without it the
    computation still shows the pointwise rule and the usual rule agree, both being `mu_*`.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 3, printed p. 358, and rewritten
    from the published solution of Sam, Solutions to Algebraic Topology (2008), §4.1 Exercise 3,
    printed p. 17: both homotopies from the usual sum $f+g$ to $\mu\circ(f,g)$ are now explicit, the
    first through the unit homotopies and the second through interpolation of the arguments of $f$
    and $g$ inside $I^n$, which is what the printed argument leaves to the reader. Every stage is
    checked to be a map of pairs: on $\partial I^n$ both arguments lie on $\partial I^n$, so $f$ and
    $g$ take the value $x_0$, and $\mu(x_0,x_0)=x_0$. The first homotopy is stationary on
    $\partial I^n$ because Hatcher's H-space definition (p. 281) requires the unit homotopies to be
    through maps $(X,e)\to(X,e)$, so $G_u(x_0)=x_0$ for every $u$; the earlier version of this card
    argued through $\mu_*$ and left that point unstated. The earlier note is right that no
    associativity of $\mu$ is used: the computation shows the pointwise rule and the usual rule
    agree, both being $\mu_*$, and neither is claimed to be a group law by itself.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the existing argument into numbered steps without changing it, and re-read the one
    hypothesis it rests on: Hatcher, Algebraic Topology (2002), Section 3.C, printed p. 281, defines
    an H-space by requiring x |-> mu(x,e) and x |-> mu(e,x) to be homotopic to the identity through
    maps (X,e) -> (X,e), and states there "In particular, this implies that mu(e,e) = e". That is
    what makes mu o (f,g) carry the boundary to x_0, and the solution now proves it as a step
    instead of asserting it. Checked: each half of each homotopy is continuous, the halves agree on
    s_1 = 1/2, each homotopy is stationary on the boundary because the unit homotopies are through
    based maps, and the endpoints are the stated maps. Not re-read this session: the printed page
    of Sam, whose argument was compared in the retained text
    tmp/sources/hatcher-solutions-sam-2008.md, Section 4.1 Exercise 3.
---

::: {.problem}
For an H-space $(X, x_0)$ with multiplication $\mu: X \times X \to X$, show that the group operation in $\pi_n(X, x_0)$ can also be defined by the rule $(f + g)(x) = \mu\bigl(f(x), g(x)\bigr)$.
:::

::: {.solution}

The route is that of Sam, *Solutions to Algebraic Topology* (2008), §4.1 Exercise 3 (`tmp/sources/hatcher-solutions-sam-2008.md`, printed p. 17): the pointwise rule is homotopic to the usual sum, first through the unit homotopies and then by interpolating the arguments of $f$ and $g$ inside $I^{n}$; the interpolations the printed argument leaves to the reader are written out below. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 3, printed p. 358, with the definition of an H-space in §3.C, printed p. 281.

Write points of $I^{n}$ as $s=(s_{1},\bar s)$ with $\bar s=(s_{2},\dots,s_{n})$, let $+$ be the usual sum in the first coordinate, and let $\mu\colon X\times X\to X$ be the multiplication with identity element $x_{0}$, so that $f$ and $g$ are maps of pairs $(I^{n},\partial I^{n})\to(X,x_{0})$.

::: pf

::: {.pf-step #unit}
$\mu(x_{0},x_{0})=x_{0}$.

::: pf-proof
By the definition of an H-space (Hatcher, §3.C, printed p. 281) the maps $x\mapsto\mu(x,x_{0})$ and $x\mapsto\mu(x_{0},x)$ are homotopic to the identity through maps $(X,x_{0})\to(X,x_{0})$, and Hatcher records there that this implies $\mu(x_{0},x_{0})=x_{0}$: a homotopy through based maps fixes the basepoint at every stage, so the value at $x_{0}$ never changes.
:::

:::

::: {.pf-step #pair}
The map $\mu\circ(f,g)\colon s\mapsto\mu\bigl(f(s),g(s)\bigr)$ is a map of pairs $(I^{n},\partial I^{n})\to(X,x_{0})$, so it represents a class in $\pi_{n}(X,x_{0})$.

::: pf-proof
It is continuous, being the composite of the continuous map $(f,g)\colon I^{n}\to X\times X$ with $\mu$. If $s\in\partial I^{n}$ then $f(s)=g(s)=x_{0}$ because $f$ and $g$ are maps of pairs, so $\mu(f(s),g(s))=\mu(x_{0},x_{0})=x_{0}$ by step [](#unit){.pf-ref}.
:::

:::

::: {.pf-step #criterion}
The rule $(f+g)(s)=\mu\bigl(f(s),g(s)\bigr)$ defines the same operation on $\pi_{n}(X,x_{0})$ as the usual sum once $f+g\simeq\mu\circ(f,g)$ through maps of pairs.

::: pf-proof
The class of $f+g$ is by definition the sum of the classes of $f$ and of $g$, and by step [](#pair){.pf-ref} the class of $\mu\circ(f,g)$ is what the rule assigns to the pair. Homotopic maps of pairs represent the same class, so the two classes coincide for every pair $f,g$, which is exactly the assertion that the two rules give the same operation.
:::

:::

::: {.pf-step #first}
Define $A\colon I^{n}\to X$ by
$$
A(s)=\begin{cases}\mu\bigl(f(2s_{1},\bar s),x_{0}\bigr),&s_{1}\le\tfrac12,\\[2pt]
\mu\bigl(x_{0},g(2s_{1}-1,\bar s)\bigr),&s_{1}\ge\tfrac12.\end{cases}
$$
Then $A$ is a map of pairs and $A\simeq f+g$ through maps of pairs.

:::: pf-proof

::: {.pf-step #first-well}
$A$ is well defined and continuous, and $A(s)=x_{0}$ for $s\in\partial I^{n}$.

::: pf-proof
At $s_{1}=\tfrac12$ the two formulas give $\mu(f(1,\bar s),x_{0})=\mu(x_{0},x_{0})$ and $\mu(x_{0},g(0,\bar s))=\mu(x_{0},x_{0})$, equal by step [](#unit){.pf-ref}; on each closed half $A$ is a composite of continuous maps, so by the pasting lemma $A$ is continuous. For $s\in\partial I^{n}$ the points $(2s_{1},\bar s)$ and $(2s_{1}-1,\bar s)$, wherever they are defined, lie on $\partial I^{n}$, so $f$ and $g$ take the value $x_{0}$ there and both formulas give $x_{0}$ by step [](#unit){.pf-ref}.
:::

:::

::: {.pf-step #first-homotopy}
$A\simeq f+g$ through maps of pairs, by a homotopy stationary on $\partial I^{n}$.

::: pf-proof
Let $G_{u}$ be a homotopy from $x\mapsto\mu(x,x_{0})$ to the identity and $H_{u}$ one from $x\mapsto\mu(x_{0},x)$ to the identity, both through maps $(X,x_{0})\to(X,x_{0})$. Define $\Phi(s,u)$ to be $G_{u}\bigl(f(2s_{1},\bar s)\bigr)$ for $s_{1}\le\tfrac12$ and $H_{u}\bigl(g(2s_{1}-1,\bar s)\bigr)$ for $s_{1}\ge\tfrac12$. The halves agree at $s_{1}=\tfrac12$, where both arguments are $x_{0}$ and both values are $G_{u}(x_{0})=H_{u}(x_{0})=x_{0}$, so $\Phi$ is continuous. At $u=0$ the halves are $\mu(f(2s_{1},\bar s),x_{0})$ and $\mu(x_{0},g(2s_{1}-1,\bar s))$, that is $\Phi(\cdot,0)=A$; at $u=1$ they are $f(2s_{1},\bar s)$ and $g(2s_{1}-1,\bar s)$, that is $\Phi(\cdot,1)=f+g$. For $s\in\partial I^{n}$ the argument of $f$, respectively of $g$, lies in $\partial I^{n}$ and is sent to $x_{0}$, and $G_{u}(x_{0})=H_{u}(x_{0})=x_{0}$ because the homotopies are through based maps, so $\Phi(s,u)=x_{0}$ for every $u$.
:::

:::

::::

:::

::: {.pf-step #second}
$A\simeq\mu\circ(f,g)$ through maps of pairs.

:::: pf-proof

::: {.pf-step #second-def}
The formula
$$
\Psi(s,u)=\begin{cases}\mu\Bigl(f\bigl((2-u)s_{1},\bar s\bigr),\ g\bigl(us_{1},\bar s\bigr)\Bigr),&s_{1}\le\tfrac12,\\[4pt]
\mu\Bigl(f\bigl((1-u)+us_{1},\bar s\bigr),\ g\bigl((1-u)(2s_{1}-1)+us_{1},\bar s\bigr)\Bigr),&s_{1}\ge\tfrac12,\end{cases}
$$
is well defined and continuous on $I^{n}\times I$.

::: pf-proof
Every argument is a point of $I^{n}$: on the first half $(2-u)s_{1}$ and $us_{1}$ lie in $[0,1]$ because $s_{1}\le\tfrac12$; on the second half $2s_{1}-1\in[0,1]$, and $(1-u)+us_{1}$ and $(1-u)(2s_{1}-1)+us_{1}$ are convex combinations of points of $[0,1]$. On each closed half $\Psi$ is a composite of continuous maps, and at $s_{1}=\tfrac12$ the two formulas agree, both being $\mu\bigl(f(1-\tfrac{u}{2},\bar s),g(\tfrac{u}{2},\bar s)\bigr)$; so $\Psi$ is continuous by the pasting lemma.
:::

:::

::: {.pf-step #second-ends}
$\Psi(\cdot,0)=A$ and $\Psi(\cdot,1)=\mu\circ(f,g)$.

::: pf-proof
At $u=0$ the first half gives $\mu(f(2s_{1},\bar s),g(0,\bar s))=\mu(f(2s_{1},\bar s),x_{0})$ because $(0,\bar s)\in\partial I^{n}$, and the second half gives $\mu(f(1,\bar s),g(2s_{1}-1,\bar s))=\mu(x_{0},g(2s_{1}-1,\bar s))$ because $(1,\bar s)\in\partial I^{n}$; these are the two halves of $A$. At $u=1$ both halves give $\mu(f(s_{1},\bar s),g(s_{1},\bar s))$, that is $\mu\circ(f,g)$.
:::

:::

::: {.pf-step #second-boundary}
$\Psi(s,u)=x_{0}$ for every $s\in\partial I^{n}$ and every $u$.

::: pf-proof
If $s\in\partial I^{n}$ then either $s_{1}\in\{0,1\}$, in which case every interpolated first coordinate lies in $\{0\}$ or in $\{1\}$ and every interpolated second coordinate lies in $\{0\}$ or in $\{1\}$, or some $\bar s_{i}\in\{0,1\}$, a coordinate the interpolation does not touch; in either case both arguments of $\mu$ lie on $\partial I^{n}$, where $f$ and $g$ take the value $x_{0}$, so the value is $\mu(x_{0},x_{0})=x_{0}$ by step [](#unit){.pf-ref}.
:::

:::

::::

:::

::: {.pf-step}
$f+g\simeq\mu\circ(f,g)$ through maps of pairs, so the rule of the exercise defines the same operation on $\pi_{n}(X,x_{0})$ as the usual sum.

::: pf-proof
Steps [](#first){.pf-ref} and [](#second){.pf-ref} give the two homotopies, and concatenating them gives $f+g\simeq\mu\circ(f,g)$; the conclusion is step [](#criterion){.pf-ref}.
:::

:::

::: {.pf-step}
Neither associativity nor commutativity of $\mu$ is used.

::: pf-proof
Every step above uses only continuity of $\mu$, the unit homotopies through based maps, and the fact that $f$ and $g$ are maps of pairs. The conclusion compares two descriptions of one class; it does not assert that $\mu$ is a group law, so associativity is irrelevant to it.
:::

:::

:::

:::
