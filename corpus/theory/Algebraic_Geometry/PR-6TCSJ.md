---
schema: qual/card@1
id: PR-6TCSJ
kind: proposition
title: Properties of $\Spec A$ read off $A$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Integral Schemes
  - Noetherian Schemes
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- When is $\Spec A$ reduced, irreducible, integral?
- What is the generic point of an irreducible scheme?
---

::: {.proposition}
For a ring $A$:

| $\Spec A$ | $A$ |
| --- | --- |
| reduced | no nonzero nilpotents |
| irreducible | the nilradical is prime |
| integral | a domain |
| connected | no nontrivial idempotents |
| Noetherian | Noetherian |
| a single point | local artinian |

An irreducible scheme has a unique **generic point**, dense in it; for $\Spec A$ integral it is the prime $(0)$, with residue field $\Frac(A)$.
:::

::: {.remark}
"Integral is reduced plus irreducible" is the one relation among these worth being able to prove on the spot, and it is immediate from the table: no nilpotents plus a prime nilradical means $(0)$ is prime.

Generic points are the visible difference from the classical picture, and the useful slogan is that a statement holds generically exactly when it holds at the generic point.
The function field of an integral scheme is the residue field there, which is how $k(X)$ becomes an object rather than a construction.
:::
