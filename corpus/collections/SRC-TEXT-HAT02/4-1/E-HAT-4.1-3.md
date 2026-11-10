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
---

::: {.problem}
For an H-space $(X, x_0)$ with multiplication $\mu: X \times X \to X$, show that the group operation in $\pi_n(X, x_0)$ can also be defined by the rule $(f + g)(x) = \mu\bigl(f(x), g(x)\bigr)$.
:::

::: {.solution}
Write points of $I^n$ as $s=(s_1,\bar s)$ with $\bar s=(s_2,\dots,s_n)$, and let $+$ be the usual sum in the first coordinate and $x_0$ the constant map. The claim is that
$$
f+g\ \simeq\ \mu\circ(f,g),\qquad \bigl(\mu\circ(f,g)\bigr)(s)=\mu\bigl(f(s),g(s)\bigr),
$$
as maps of pairs $(I^n,\partial I^n)\to(X,x_0)$; the right-hand map sends $\partial I^n$ to $\mu(x_0,x_0)=x_0$, so it represents a class in $\pi_n(X,x_0)$, and the class is then exactly the one defined by the rule in the exercise. This is the route of Sam, *Solutions to Algebraic Topology* (2008), §4.1 Exercise 3, printed p. 17, with the interpolations of the arguments that the printed argument leaves to the reader written out below.

*First homotopy.* By Hatcher's definition (p. 281) the unit maps $x\mapsto\mu(x,x_0)$ and $x\mapsto\mu(x_0,x)$ are homotopic to the identity through maps $(X,x_0)\to(X,x_0)$; let $G_u$ be such a homotopy from $\mu(-,x_0)$ to the identity, so $G_u(x_0)=x_0$ for all $u$. Define
$$
A(s)=\begin{cases}\mu\bigl(f(2s_1,\bar s),x_0\bigr),&s_1\le\tfrac12,\\[2pt]
\mu\bigl(x_0,g(2s_1-1,\bar s)\bigr),&s_1\ge\tfrac12.\end{cases}
$$
On $s_1\le\tfrac12$ the map $(s,u)\mapsto G_u\bigl(f(2s_1,\bar s)\bigr)$ runs from $A$ to $f+g$, and on $s_1\ge\tfrac12$ the map $(s,u)\mapsto H_u\bigl(g(2s_1-1,\bar s)\bigr)$ does, where $H_u$ is a homotopy from $\mu(x_0,-)$ to the identity through maps $(X,x_0)\to(X,x_0)$, so $H_u(x_0)=x_0$. For $s\in\partial I^n$ the point $(2s_1,\bar s)$, respectively $(2s_1-1,\bar s)$, also lies on $\partial I^n$, so $f$ and $g$ take the value $x_0$ there and both ends of the homotopy equal $x_0$ at every stage, because $G_u(x_0)=x_0$. Hence $A\simeq f+g$ through maps of pairs.

*Second homotopy.* Define, on the first half $s_1\le\tfrac12$,
$$
H_u(s)=\mu\Bigl(f\bigl((2-u)s_1,\bar s\bigr),\ g\bigl(us_1,\bar s\bigr)\Bigr),\qquad u\in[0,1],
$$
and on the second half
$$
H_u(s)=\mu\Bigl(f\bigl((1-u)+us_1,\bar s\bigr),\ g\bigl((1-u)(2s_1-1)+us_1,\bar s\bigr)\Bigr).
$$
Each argument is a point of $I^n$: on the first half $(2-u)s_1\in[0,1]$ and $us_1\in[0,1]$; on the second half $2s_1-1\in[0,1]$ because $s_1\ge\tfrac12$, and both interpolated coordinates lie between $s_1$ and a point of $\{1\}$ or $[0,1]$. At $u=0$ the first half gives $\mu(f(2s_1,\bar s),g(0,\bar s))=\mu(f(2s_1,\bar s),x_0)$ because $(0,\bar s)\in\partial I^n$, and the second half gives $\mu(f(1,\bar s),g(2s_1-1,\bar s))=\mu(x_0,g(2s_1-1,\bar s))$ because $(1,\bar s)\in\partial I^n$; so $H_0=A$. At $u=1$ both halves give $\mu(f(s),g(s))$; so $H_1=\mu\circ(f,g)$.

$H_u$ is a homotopy of maps of pairs: if $s\in\partial I^n$ then either $s_1\in\{0,1\}$, in which case every interpolated first coordinate lies in $\{0\}$ or $\{1\}$ and every interpolated second coordinate lies in $\{0\}$ or $\{1\}$, or some $\bar s_i\in\{0,1\}$, which is untouched by the interpolation. In either case both arguments of $\mu$ lie on $\partial I^n$, where $f$ and $g$ take the value $x_0$, so $H_u(s)=\mu(x_0,x_0)=x_0$.

Combining the two homotopies, $f+g\simeq\mu\circ(f,g)$ through maps of pairs, so the two rules give the same operation on $\pi_n(X,x_0)$.
:::
