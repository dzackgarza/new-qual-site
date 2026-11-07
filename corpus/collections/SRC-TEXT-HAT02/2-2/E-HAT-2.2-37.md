---
schema: qual/card@1
id: E-HAT-2.2-37
kind: problem
title: Elementary derivation of Mayer–Vietoris sequence in simplicial homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Simplicial Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 37.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the derivation: for subcomplexes of a $\Delta$-complex every simplex of $A\cup B$ lies in
    $A$ or in $B$ and one lying in both lies in $A\cap B$, so
    $0\to C_*(A\cap B)\to C_*(A)\oplus C_*(B)\to C_*(X)\to0$ is degreewise short exact and the maps
    commute with boundaries; its homology sequence is Mayer-Vietoris. This is exactly the point at
    which the $\Delta$-complex hypothesis is used, the identity $C_*(A+B)=C_*(X)$ failing for
    singular chains. The two closing steps are read at the level of their claims.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    The stored solution was placeholder text: the first step's proof read "setup.", the step
    carrying the short exact sequence had an informal paragraph in place of a proof block, the
    step drawing the long exact sequence had no proof block at all with its conclusion inside the
    step text, and the last step only pointed back. It is replaced by a derivation.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 37 as printed on p. 158. The rewritten proof: chain groups are free
    on the open simplices (p. 105) and a subcomplex is a union of simplices (p. 107); every open
    simplex of X lies wholly in A or in B because it is connected and A, B are unions of open
    simplices, whence Delta_n(A) + Delta_n(B) = Delta_n(X); the maps phi(x) = (x,-x) and
    psi(x,y) = x+y are the ones Hatcher uses on p. 150, with his exactness checks; Theorem 2.16
    p. 117 gives the sequence, and the connecting map is written out as the class of partial x for
    z = x + y a cycle. The final step says what makes this derivation elementary: no subdivision
    is needed, unlike the singular case which needs Proposition 2.21 p. 119. What is not covered:
    the independence of the connecting map from the choice of x and y is deferred to p. 150
    rather than redone.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Locator corrected after checking the printed exercise page: Hatcher §2.2 Exercise 37 is on
    p.158, not p.159 as the previous audit note and commit summary said. The solution is unchanged:
    the simplicial Mayer-Vietoris sequence comes from the exact sequence of chain complexes
    Delta_n(A cap B) -> Delta_n(A) + Delta_n(B) -> Delta_n(X) and Theorem 2.16 p.117.

---

::: {.problem}
Give an elementary derivation for the Mayer–Vietoris sequence in simplicial homology for a $\Delta$-complex $X$ decomposed as the union of subcomplexes $A$ and $B$.
:::

::: {.solution}
Let $X$ be a $\Delta$-complex and $A,B\subset X$ subcomplexes with $A\cup B=X$.

::: pf

::: {.pf-step #s1}

The chain groups $\Delta_n(A)$ and $\Delta_n(B)$ are subgroups of $\Delta_n(X)$, and
$$
\Delta_n(A)+\Delta_n(B)=\Delta_n(X).
$$

::: pf-proof

By the definition of the chain groups of a $\Delta$-complex (p. 105), $\Delta_n(X)$ is free abelian on the open $n$-simplices of $X$, and for a subcomplex the corresponding group is free on the open simplices it contains; a subcomplex of a $\Delta$-complex is a union of simplices (p. 107), so $\Delta_n(A)$ and $\Delta_n(B)$ are subgroups of $\Delta_n(X)$.

For the sum, let $\sigma$ be an open $n$-simplex of $X$. Its interior is connected and lies in $A\cup B$, and $A$ and $B$ are unions of open simplices, so the interior lies entirely in $A$ or entirely in $B$; since $A$ and $B$ are closed, the whole simplex does too. Every simplex of $X$ is thus a simplex of $A$ or of $B$, and a chain is a sum of simplices.

:::

:::

::: {.pf-step #s2}

The maps
$$
\varphi:\Delta_n(A\cap B)\to\Delta_n(A)\oplus\Delta_n(B),\qquad \varphi(x)=(x,-x),
$$
and
$$
\psi:\Delta_n(A)\oplus\Delta_n(B)\to\Delta_n(X),\qquad \psi(x,y)=x+y,
$$
are chain maps and form a short exact sequence of chain complexes.

::: pf-proof

Both are given by inclusions of chains, which commute with the simplicial boundary, so both are chain maps: $\partial(x,-x)=(\partial x,-\partial x)$ and $\partial(x+y)=\partial x+\partial y$.

That $\ker\varphi=0$ is immediate, since a chain of $A\cap B$ that is zero as a chain of $A$ is zero. $\operatorname{Im}\varphi\subset\ker\psi$ because $\psi\varphi(x)=x-x=0$. For $\ker\psi\subset\operatorname{Im}\varphi$, if $x+y=0$ in $\Delta_n(X)$ then $x=-y$, so $x$ is a chain carried by simplices lying in both $A$ and $B$, that is $x\in\Delta_n(A\cap B)$, and $(x,y)=(x,-x)$. Surjectivity of $\psi$ is step [](#s1){.pf-ref}. These are exactly the checks made for the singular case on p. 150.

:::

:::

::: {.pf-step #s3}

Theorem 2.16 (p. 117) applied to this short exact sequence gives the exact sequence
$$
\cdots\to H_n(A\cap B)\xrightarrow{\ \Phi\ }H_n(A)\oplus H_n(B)\xrightarrow{\ \Psi\ }H_n(X)\xrightarrow{\ \partial\ }H_{n-1}(A\cap B)\to\cdots
$$

::: pf-proof

Theorem 2.16 produces the long exact sequence of a short exact sequence of chain complexes, and pp. 116--117 construct its connecting map. Here $\Phi$ and $\Psi$ are the maps induced in homology by $\varphi$ and $\psi$, and the connecting map is computed as follows. Let $z$ be a cycle in $\Delta_n(X)$ and write $z=x+y$ with $x\in\Delta_n(A)$ and $y\in\Delta_n(B)$, which is possible by step [](#s1){.pf-ref}. Then $\partial x=-\partial y$ because $\partial z=0$, so $\partial x$ is a chain lying in both $A$ and $B$, and it is a cycle: $\partial\partial x=0$. The class of $\partial x$ in $H_{n-1}(A\cap B)$ is independent of the choice of $x$ and $y$, by the argument on p. 150, and is $\partial[z]$. Exactness at each term is that of Theorem 2.16.

:::

:::

::: {.pf-step #s4}

This is the Mayer--Vietoris sequence of $X=A\cup B$.

::: pf-proof

The sequence of step [](#s3){.pf-ref} has the form displayed in the subsection on Mayer--Vietoris sequences beginning on p. 149, with the same maps $\Phi$ and $\Psi$. The derivation here is elementary in that no subdivision is needed: for the singular theory one must invoke Proposition 2.21 (p. 119) to know that a class of $X$ is represented by a sum of chains in $A$ and in $B$, whereas for a $\Delta$-complex with $A$ and $B$ subcomplexes every simplex already lies in one of them, which is step [](#s1){.pf-ref}.

:::

:::

:::

:::
