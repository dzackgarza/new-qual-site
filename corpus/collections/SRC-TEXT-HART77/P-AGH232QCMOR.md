---
schema: qual/card@1
id: P-AGH232QCMOR
kind: problem
title: Quasi-compactness of a morphism can be checked on every open affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms Of Schemes
  - Quasi-Compactness
  - Affine Covers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.2 statement and the preceding localization results for distinguished opens.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
A morphism $f: X \to Y$ of schemes is **quasi-compact** if there is a cover of $Y$ by open affines $V_i$ such that $\inverseof{f}(V_i)$ is quasi-compact for each $i$.

Show that $f$ is quasi-compact if and only if for every open affine subset $V \subseteq Y$ the preimage $\inverseof{f}(V)$ is quasi-compact.
:::

::: {.solution}
<1>1. If $f^{-1}(V)$ is quasi-compact for every affine open $V\subseteq Y$, then $f$ is quasi-compact.
::: {.proof} Choose any affine open cover
\[
Y=\bigcup_iV_i.
\]
The hypothesis says that every $f^{-1}(V_i)$ is quasi-compact, which is exactly the definition given in the problem.
:::

<1>2. Conversely, suppose $f$ is quasi-compact in the stated sense.  Thus there is an affine open cover
\[
Y=\bigcup_iV_i
\]
such that every $f^{-1}(V_i)$ is quasi-compact.  Fix an arbitrary affine open
\[
V\subseteq Y.
\]
For every $y\in V$ there is an index $i$ and a distinguished open
\[
W_y=D(g_y)\subseteq V_i
\]
such that
\[
y\in W_y\subseteq V\cap V_i.
\]
::: {.proof}
Choose $i$ with $y\in V_i$.  Then $V\cap V_i$ is an open neighborhood of $y$ in the affine scheme $V_i$.  Distinguished opens form a basis of an affine scheme, so there is some $g_y\in\Gamma(V_i,\mathcal O_Y)$ with the asserted property.
:::

<1>3. For each $y\in V$, the inverse image
\[
f^{-1}(W_y)
\]
is quasi-compact.
::: {.proof} Fix $y$ and write $W_y=D(g_y)\subseteq V_i$.
Since $f^{-1}(V_i)$ is quasi-compact, choose a finite affine open cover
\[
f^{-1}(V_i)=U_1\cup\cdots\cup U_n.
\]
On each affine $U_j$, the pullback of $g_y$ is a global function, and
\[
U_j\cap f^{-1}(W_y)
\]
is its distinguished nonvanishing locus.
Hence it is affine, in particular quasi-compact.

Therefore
\[
f^{-1}(W_y)
=
\bigcup_{j=1}^n\bigl(U_j\cap f^{-1}(W_y)\bigr)
\]
is a finite union of quasi-compact open subsets and is quasi-compact.
:::

<1>4. Finitely many of the opens $W_y$ cover $V$.
::: {.proof}
The sets $W_y$ form an open cover of $V$.  Since $V$ is affine, its underlying topological space is quasi-compact.  Hence there are points
\[
y_1,\ldots,y_m\in V
\]
such that
\[
V=W_{y_1}\cup\cdots\cup W_{y_m}.
\]
:::

<1>5. The inverse image $f^{-1}(V)$ is quasi-compact.
::: {.proof}
By <1>4,
\[
f^{-1}(V)
=
f^{-1}(W_{y_1})\cup\cdots\cup f^{-1}(W_{y_m}).
\]
Each term is quasi-compact by <1>3, so their finite union is quasi-compact.
:::

<1>6. Hence the two formulations of quasi-compactness are equivalent.
::: {.proof}
Step <1>1 proves one implication and steps <1>2--<1>5 prove the converse.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>6 is the required equivalence.
:::
:::
