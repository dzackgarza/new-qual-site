---
schema: qual/card@1
id: E-SS3.EX-19
kind: problem
title: The maximum principle for harmonic functions
classification:
  areas:
    - complex-analysis
  topics: [Maximum Principle, Harmonic Functions]
relations: []
review: draft
audit:
  - event: solution-written
    by: claude
    date: 2026-11-20
    note: >-
      Converted from prose to numbered steps under #2, four of them, each with its proof, and the
      citation moved from a printed-page reference to the book's chapter, section and exercise
      number: Stein--Shakarchi, *Complex Analysis*, Chapter 3 §8 Exercise 19, read in the retained
      text version. The mathematics is the book's argument, with the open-and-closed argument for the
      connected domain spelled out and the boundary part's dichotomy stated. The card's part labels
      are folded into the steps that prove them. Not checked: no certificate, and the maximum modulus
      principle used in step #local is cited as standard rather than proved here.
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
---

::: {.exercise}
Prove the maximum principle for harmonic functions, that is:

(a) If $u$ is a non-constant real-valued harmonic function in a region $\Omega$, then $u$ cannot attain a maximum (or a minimum) in $\Omega$.

(b) Suppose that $\Omega$ is a region with compact closure $\overline{\Omega}$. If $u$ is harmonic in $\Omega$ and continuous in $\overline{\Omega}$, then
$$
\sup_{z \in \Omega} \abs{u(z)} \leq \sup_{z \in \overline{\Omega} - \Omega} \abs{u(z)}.
$$
[Hint: To prove the first part, assume that $u$ attains a local maximum at $z_0$. Let $f$ be holomorphic near $z_0$ with $u = \Re(f)$, and show that $f$ is not open. The second part follows directly from the first.]
:::

::: {.solution}
This is Stein--Shakarchi, *Complex Analysis*, Chapter 3 §8 Exercise 19, read in `tmp/sources/ss03-stein-shakarchi-complex-analysis.md`: the maximum principle for harmonic functions in part (a) and its boundary form in part (b). The argument below is that book's, with the connectedness step made explicit.

::: pf

::: {.pf-step #local}
A harmonic function on a domain cannot have a local maximum at an interior point unless it is constant near that point.

::: pf-proof
Let $u$ be harmonic with a local maximum at $z_0$ and let $D$ be a disc about $z_0$ inside the domain. On a simply connected disc $u$ has a harmonic conjugate $v$, so $F=u+iv$ is holomorphic on $D$ and $\abs{e^{F(z)}}=e^{u(z)}$. Near $z_0$ one has $u(z)\le u(z_0)$, hence $\abs{e^{F(z)}}\le\abs{e^{F(z_0)}}$, so the holomorphic function $e^F$ attains a local maximum of its modulus and is constant by the maximum modulus principle. Then $F$ is constant, and $u=\Re F$ is constant on $D$.
:::

:::

::: {.pf-step #global}
If a harmonic $u$ on a connected domain attains a maximum value $M$ at some point, then $u\equiv M$.

::: pf-proof
Let $A$ be the set of points having a neighbourhood on which $u\equiv M$. It is open by definition and nonempty because step [](#local){.pf-ref} makes the point where $u=M$ interior to such a neighbourhood. It is closed in the domain: if $z_n\in A$ and $z_n\to z$, then $u(z)=M$ by continuity, and step [](#local){.pf-ref} applies at $z$. A nonempty subset of a connected space that is both open and closed is the whole space, so $A$ is the domain and $u\equiv M$. Applying the same to $-u$ gives the statement for minima.
:::

:::

::: {.pf-step #boundary}
If $\overline\Omega$ is compact and $u$ is continuous on it and harmonic on $\Omega$, then $\sup_{z\in\Omega}\abs{u(z)}\le\sup_{z\in\overline\Omega\setminus\Omega}\abs{u(z)}$.

::: pf-proof
$\abs{u}$ attains a maximum on the compact set $\overline\Omega$, at some $z_0$. If $z_0\in\Omega$ and $\abs{u(z_0)}$ exceeds every boundary value, then either $u(z_0)$ or $-u(z_0)$ equals $\abs{u(z_0)}$ and is the maximum of $u$ or of $-u$ over $\overline\Omega$, hence an interior maximum of that harmonic function, so $u$ is constant by step [](#global){.pf-ref}; in the constant case the same value is taken on the boundary. In both cases the supremum over $\Omega$ is at most the boundary supremum.
:::

:::

::: {.pf-step}
Both assertions of Exercise 19 hold: the interior maximum principle and its boundary form.

::: pf-proof
Step [](#global){.pf-ref} is part (a) and step [](#boundary){.pf-ref} is part (b).
:::

:::

:::


:::
