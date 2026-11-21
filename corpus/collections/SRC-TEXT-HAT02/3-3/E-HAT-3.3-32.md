---
schema: qual/card@1
id: E-HAT-3.3-32
kind: problem
title: Compact manifolds do not retract onto boundary
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 32; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 32; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument over $\ZZ_2$, where every manifold is orientable: a retraction makes $i_*$
    injective on $H_{n-1}$, while exactness together with $\delta[M,\partial M]=[\partial M]\ne0$
    makes $i_*[\partial M]=0$.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Added the published corroboration: Steven V. Sam, Solutions to Algebraic Topology (2008),
    SS3.3 Exercise 32, printed p.16, is the same argument, and this card matches it step for step
    except that Sam's own text slips in writing the retraction identity on M instead of on the
    boundary. Read against Hatcher: the ZZ_2 coefficient ring makes orientability automatic and
    Exercise 31 supplies the nonzero boundary class.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 32 of §3.3, printed p. 260 — the
    exercises of §3.3 are 1--6 on p. 257, 7--14 on p. 258, 15--26 on p. 259 and 27--35 on p. 260,
    checked at PDF pages 266--269 of the held book — and against the source transcribed, Steven V.
    Sam, *Solutions to Algebraic Topology* (2008), §3.3 Exercise 32, whose printed folio is 16 while
    the PDF page is 17 of `tmp/sources/hatcher-solutions-sam-2008.pdf` (the page's running head
    "3.C. H-SPACES AND HOPF ALGEBRAS" and its number 16), so the card's "printed p. 16" is right and
    the offset is what a page check must allow for. Checked: with $R=\ZZ_2$ every manifold is
    $R$-orientable, so Exercise 31 applies and $\partial[M,\partial M]=[\partial M]$; exactness of
    $H_n(M,\partial M)\to H_{n-1}(\partial M)\xrightarrow{i_*}H_{n-1}(M)$ gives
    $\mathrm{im}\,\partial=\ker i_*$, so a retraction, which makes $i_*$ injective by
    $r_*i_*=\mathrm{id}$, forces $\partial=0$, contradicting $\partial[M,\partial M]=[\partial M]\ne0$
    — the form in which Sam states it; the card states the equivalent form $i_*[\partial M]=0$ with
    $[\partial M]\ne0$. Confirmed at the page: Sam writes "$r\circ i$ is the identity on $M$" where
    the composite is the identity on $\partial M$, the slip the card records and does not reproduce.
    No defect. The printed page is added, the card having had none.
---

::: {.problem}
Show that a compact manifold does not retract onto its boundary.
:::

::: {.solution}
The exercise is §3.3 Exercise 32.

The argument is the one in Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.3 Exercise 32: coefficients $\ZZ_{2}$ so that orientability is free, Exercise 31 to make the boundary map nonzero on the fundamental class, and exactness to make $i_{*}$ kill that class. Sam's text prints "$r\circ i$ is the identity on $M$" where the composite is the identity on $\partial M$; the slip is not reproduced here.

Let $M$ be a compact $n$-manifold with boundary, $i:\partial M\to M$ the inclusion, and $R=\ZZ_{2}$.

::: pf

::: {.pf-step #coefficients}
With $R=\ZZ_{2}$ the manifold is $R$-orientable, so Exercise 31 applies to $M$.

::: pf-proof
Every manifold is $\ZZ_{2}$-orientable: the local orientation of a chart is unique in $\ZZ_{2}$ coefficients, so the local orientations admit no obstruction to being pieced together, and a compact manifold has a fundamental class in $\ZZ_{2}$ coefficients. Hence the hypothesis of Exercise 31 — $M$ compact and $R$-orientable — is satisfied with $R=\ZZ_{2}$, and by that exercise the boundary map sends a fundamental class for $(M,\partial M)$ to a fundamental class for $\partial M$.
:::

:::

::: {.pf-step #injective}
A retraction $r:M\to\partial M$ would make $i_{*}:H_{n-1}(\partial M;R)\to H_{n-1}(M;R)$ injective.

::: pf-proof
A retraction satisfies $r\circ i=\operatorname{id}_{\partial M}$, so on homology $r_{*}i_{*}=\operatorname{id}$; if $i_{*}\alpha=0$ then $\alpha=r_{*}i_{*}\alpha=0$, which is injectivity.
:::

:::

::: {.pf-step #killed}
$i_{*}[\partial M]=0$ in $H_{n-1}(M;R)$, while $[\partial M]\ne0$.

::: pf-proof
Let $[M,\partial M]\in H_{n}(M,\partial M;R)$ be a fundamental class. By step [](#coefficients){.pf-ref} the boundary map satisfies $\delta[M,\partial M]=[\partial M]$, a fundamental class of $\partial M$, which is nonzero because $H_{n-1}(\partial M;R)\cong R$ is generated by it. The long exact sequence of the pair contains
$$
H_{n}(M,\partial M;R)\xrightarrow{\ \delta\ }H_{n-1}(\partial M;R)\xrightarrow{\ i_{*}\ }H_{n-1}(M;R),
$$
and exactness says $\operatorname{im}\delta=\ker i_{*}$, so
$$
i_{*}[\partial M]=i_{*}\delta[M,\partial M]=0 .
$$
:::

:::

::: {.pf-step #contradiction}
No retraction $M\to\partial M$ exists.

::: pf-proof
By step [](#killed){.pf-ref} the class $[\partial M]\ne0$ lies in the kernel of $i_{*}$, so $i_{*}$ is not injective; by step [](#injective){.pf-ref} a retraction would force it to be injective. Hence no such retraction exists, that is a compact manifold does not retract onto its boundary.
:::

:::

:::
:::
