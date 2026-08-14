---
schema: qual/card@1
id: E-PHSV5
kind: exercise
title: "Show that if $f \\in \\FF_p[x]^{\\irr}$ is degree $d$,"
classification:
  areas:
  - algebra
  topics:
  - finite-fields
  - irreducibility-criteria
  - field-extensions
relations: []
review: draft
---
:::{.exercise title="?"}
Show that if $f \in \FF_p[x]^{\irr}$ is degree $d$,
\[
f \divides x^{p^n}-x \iff d\divides n
.\]
:::

:::{.solution}
$\impliedby$:

- If $d\divides n$, $x^d-1 \divides x^n-1$ by a previous exercise, and so $p^d-1 \divides p^n-1$.
- So $x^{p^d-1} \divides x^{p^n-1}$, now multiply through by $x$.
- Claim: $f \divides x^{p^d-1}$, from which the result immediately follows.
- For $\alpha$ any root of $f$, $\FF_p(\alpha)$ is a finite field of size $p^d$ since $[\FF_p(\alpha):\FF_p] = d$.
- So $\FF_p(\alpha)\cong \GF(p^d)$, which is the splitting field of $x^{p^d}-x$.
- Thus $\alpha$ is a root of $x^{p^d}-x$.
  Iterating over all roots yields the divisibility statement.

$\implies$:

- If $f\divides g_n(x) \da x^{p^n}-x$, then every root $\alpha$ of $f$ is a root of $g_n$.
- So $\FF_p(\alpha) \subseteq \GF(p^n)$.
- The result follows from the computation
\[
n &= [\GF(p^n) : \FF_p] \\
&= [\GF(p^n) : \FF_p(\alpha)] \cdot [\FF_p(\alpha) : \FF_p] \\
&= kd
.\]

:::

