---
schema: qual/card@1
id: P-AGHREALIRRED
kind: problem
title: An irreducible real polynomial with reducible zero set
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Real Fields
  - Plane Curves
relations:
- kind: uses
  target: T-JRTS2
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the requested example with the retained Hartshorne I.1.12 transcription. The proof treats the real point set with its Zariski topology, proves irreducibility by the monic quadratic factorization, and distinguishes that point set from the integral affine scheme defined by the same equation.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Give an example of an irreducible polynomial $f \in \RR[x,y]$ whose zero set $Z(f)$ in $\AA^2_\RR$ is not irreducible.
:::

::: {.solution}
Here $Z(f)$ is the set of real solutions in $\RR^2$, with the Zariski topology whose closed sets are common zero sets of real polynomials.

::: pf

::: {.pf-step #f-irreducible}
An irreducible polynomial with the required property is
$$
\boxed{f(x,y)=x^2+(y^2-1)^2.}
$$

::: pf-proof
Regard $f$ as a monic polynomial of degree two in $x$ over the domain $\RR[y]$.
Suppose $f=gh$ with neither factor a unit in $\RR[y][x]$.
The $x$-degrees add, and the leading coefficients in $x$ multiply to $1$.
A factor of $x$-degree zero would therefore be a unit of $\RR[y]$, which is excluded.
Both factors consequently have $x$-degree one, and their leading coefficients are nonzero real constants.
Rescaling the two factors by reciprocal constants gives
$$
f=(x+a(y))(x+b(y))\qquad(a,b\in\RR[y]).
$$
Comparison of the coefficient of $x$ gives $b=-a$.
Comparison of the constant coefficient then gives $-a(y)^2=(y^2-1)^2$.
Evaluating this polynomial identity at $y=0$ gives $-a(0)^2=1$, impossible over $\RR$.
Thus no nontrivial factorization exists, proving irreducibility.
:::

:::

::: {.pf-step #zero-set-reducible}
The real zero set is $Z(f)=\{(0,1),(0,-1)\}$ and is reducible.

::: pf-proof
At a real point, both summands $x^2$ and $(y^2-1)^2$ are nonnegative.
Their sum is zero exactly when $x=0$ and $y^2-1=0$.
This gives the two stated points.
The singleton subsets are Zariski closed, since they are $Z(x,y-1)$ and $Z(x,y+1)$ respectively.
Each is a proper nonempty closed subset of $Z(f)$, and their union is all of $Z(f)$.
This is a decomposition showing that $Z(f)$ is not irreducible.
:::

:::

::: pf-qed
Step [](#f-irreducible){.pf-ref} proves that the displayed polynomial is irreducible in $\RR[x,y]$, and step [](#zero-set-reducible){.pf-ref} proves that its real zero set is reducible.
:::

:::
:::

::: {.remark title="Real points and the affine scheme"}
The ideal of this real point set is $(x,y^2-1)$.
Indeed, reducing a polynomial modulo $x$ leaves a polynomial in $y$, which vanishes at both $1$ and $-1$ exactly when it is divisible by $y^2-1$.
It strictly contains $(f)$: the element $x$ belongs to the former and not the latter, as its $x$-degree is smaller than that of $f$.
By contrast, $(f)$ is a prime ideal because $\RR[x,y]$ is a UFD and $f$ is irreducible, so $\Spec(\RR[x,y]/(f))$ is integral and irreducible.
The example concerns the real point set, not a failure of irreducibility for that scheme; the [[T-JRTS2|algebraically closed-field hypothesis in the Nullstellensatz]] is what distinguishes the two ideal computations [@Har10a, Chapter I, §1].
:::
