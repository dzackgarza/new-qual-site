---
schema: qual/card@1
id: E-HAT-3.C-1
kind: problem
title: "H-space structure and strict identity"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Suppose that $X$ is a CW complex with basepoint $e \in X$ a 0-cell.
Show that $X$ is an H-space if there is a map $\mu: X \times X \to X$ such that the maps $X \to X$, $x \mapsto \mu(x, e)$ and $x \mapsto \mu(e, x)$, are homotopic to the identity.
[Sometimes this is taken as the definition of an H-space, rather than the more restrictive condition in the definition we have given.] With the same hypotheses, show also that $\mu$ can be homotoped so that $e$ is a strict two-sided identity.

::: {.solution}
Because $e$ is a $0$-cell of the CW complex $X$, the inclusion $\{e\}\hookrightarrow X$ is a closed cofibration; equivalently, $(X,e)$ is well-pointed. For well-pointed H-spaces there is a standard unit-strictification theorem: a multiplication having a two-sided homotopy unit in the unbased sense can be homotoped first so that the unit homotopies preserve the basepoint, and if $X\vee X\hookrightarrow X\times X$ is a cofibration, the multiplication can then be homotoped to have a strict two-sided unit. See tom Dieck--Kamps--Puppe, *Homotopy Theory*, Theorem 3.37 and Proposition 3.38.

The hypotheses of that theorem hold here. Indeed $\{e\}\hookrightarrow X$ is a closed cofibration, hence so is
\[
X\vee X=(X\times\{e\})\cup(\{e\}\times X)
\hookrightarrow X\times X.
\]
By assumption, the two restrictions
\[
r(x)=\mu(x,e),
\qquad
\ell(x)=\mu(e,x)
\]
are homotopic to $\operatorname{id}_X$. The first part of the strictification theorem therefore replaces $\mu$, through a homotopy of multiplications, by a multiplication for which these homotopies can be taken through maps $(X,e)\to(X,e)$. This is exactly Hatcher's H-space condition.

For the stronger assertion, apply the second part of the theorem to the cofibration $X\vee X\hookrightarrow X\times X$. The restriction of the adjusted multiplication to $X\vee X$ is homotopic, through based maps, to the fold map
\[
\nabla:X\vee X\to X,
\qquad
\nabla|_{X\times\{e\}}=\operatorname{id}
=\nabla|_{\{e\}\times X}.
\]
The homotopy extension property extends this homotopy from the wedge to all of $X\times X$. At the end we obtain a multiplication $\mu'$ homotopic to $\mu$ such that
\[
\mu'(x,e)=x=\mu'(e,x)
\]
for every $x\in X$. Thus $e$ is a strict two-sided identity.
:::
