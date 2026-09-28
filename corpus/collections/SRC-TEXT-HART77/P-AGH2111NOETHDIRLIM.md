---
schema: qual/card@1
id: P-AGH2111NOETHDIRLIM
kind: problem
title: On a noetherian space the sectionwise direct limit of sheaves is already a sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Direct Limits
  - Noetherian Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.11 statement and source-order placement after II.1.10.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $\ts{\mcf_i}$ be a direct system of sheaves on a noetherian topological space $X$.
Show that the presheaf $U \mapsto \varinjlim \mcf_i(U)$ is already a sheaf.
In particular,
\[
\Gamma\qty{X, \varinjlim \mcf_i} = \varinjlim \Gamma(X, \mcf_i).
\]
:::

::: {.solution}
Let
\[
\mcp(U)=\varinjlim_i\mcf_i(U)
\]
be the sectionwise direct-limit presheaf.  We assume, as usual for a direct system, that the index set is directed.

<1>1. Every open subset of a noetherian topological space is quasicompact.
::: {.proof}
Let $U\subseteq X$ be open and suppose
\[
U=\bigcup_{\alpha\in A}U_\alpha
\]
is an open cover with no finite subcover.

Choose $\alpha_1$.  Since $U_{\alpha_1}$ does not cover $U$, choose $\alpha_2$ such that
\[
U_{\alpha_2}\not\subseteq U_{\alpha_1}.
\]
Inductively, because no finite union covers $U$, choose $\alpha_{n+1}$ so that
\[
U_{\alpha_{n+1}}
\not\subseteq
U_{\alpha_1}\cup\cdots\cup U_{\alpha_n}.
\]
Then the open subsets
\[
U_{\alpha_1}
\subsetneq
U_{\alpha_1}\cup U_{\alpha_2}
\subsetneq\cdots
\]
form a strictly ascending chain.  A noetherian topological space satisfies the ascending-chain condition on open subsets, contradiction.  Thus a finite subcover exists.
:::

<1>2. The presheaf $\mcp$ satisfies uniqueness for a finite open cover.
::: {.proof}
Let
\[
U=U_1\cup\cdots\cup U_r
\]
and suppose
\[
s,t\in\mcp(U)
\]
have equal restrictions to every $U_a$.

Because the index system is directed, after passing to a common stage we may represent both $s$ and $t$ by sections
\[
s_i,t_i\in\mcf_i(U)
\]
for one index $i$.

For each $a$, equality
\[
s|_{U_a}=t|_{U_a}
\]
in the direct limit means that there is some index $j_a\ge i$ at which the images of
\[
s_i|_{U_a},\quad t_i|_{U_a}
\]
become equal.  Since there are only finitely many $a$, directedness supplies one index $j$ dominating all $j_a$.

Thus the images
\[
s_j,t_j\in\mcf_j(U)
\]
have equal restrictions on every member of the finite cover.  Since $\mcf_j$ is a sheaf,
\[
s_j=t_j.
\]
Hence $s=t$ in $\mcp(U)$.
:::

<1>3. The presheaf $\mcp$ satisfies gluing for a finite open cover.
::: {.proof}
Let
\[
U=U_1\cup\cdots\cup U_r
\]
and let
\[
s_a\in\mcp(U_a)
\]
be sections whose restrictions agree on every overlap $U_a\cap U_b$.

Because there are finitely many sections, directedness lets us choose one index $i$ and representatives
\[
s_{a,i}\in\mcf_i(U_a)
\]
for every $a$.

For every pair $(a,b)$, compatibility in the direct limit means that at some later index $j_{ab}\ge i$ the two restrictions
\[
s_{a,i}|_{U_a\cap U_b},
\qquad
s_{b,i}|_{U_a\cap U_b}
\]
become equal.  There are only finitely many pairs, so choose one index $j$ dominating all $j_{ab}$.

The resulting sections
\[
s_{a,j}\in\mcf_j(U_a)
\]
are genuinely compatible on every overlap.  Since $\mcf_j$ is a sheaf, there is a unique
\[
s_j\in\mcf_j(U)
\]
restricting to all $s_{a,j}$.  Its image
\[
s\in\mcp(U)
\]
restricts to the original sections $s_a$.
:::

<1>4. The presheaf $\mcp$ is a sheaf for arbitrary open covers.
::: {.proof}
Let
\[
U=\bigcup_{\alpha\in A}U_\alpha
\]
be any open cover.  By <1>1, choose a finite subcover
\[
U=U_{\alpha_1}\cup\cdots\cup U_{\alpha_r}.
\]

Uniqueness for the original cover follows immediately from uniqueness for this finite subcover, proved in <1>2.

Now suppose a compatible family
\[
s_\alpha\in\mcp(U_\alpha)
\]
is given.  By <1>3, the finite subfamily indexed by $\alpha_1,\ldots,\alpha_r$ glues to a section
\[
s\in\mcp(U).
\]
For any other $\alpha$, both
\[
s|_{U_\alpha}
\quad\text{and}\quad
s_\alpha
\]
restrict to the same section on each open
\[
U_\alpha\cap U_{\alpha_a},
\qquad 1\le a\le r,
\]
because the original family was compatible.  These finitely many intersections cover $U_\alpha$, so <1>2 gives
\[
s|_{U_\alpha}=s_\alpha.
\]
Thus $s$ glues the entire family.

Hence $\mcp$ satisfies both sheaf axioms for every cover.
:::

<1>5. Therefore no sheafification is needed:
\[
\boxed{
\varinjlim_i\mcf_i
=\left(U\longmapsto\varinjlim_i\mcf_i(U)\right).
}
\]
::: {.proof}
Hartshorne II.1.10 defines the direct limit sheaf as the sheafification of $\mcp$.  By <1>4, $\mcp$ is already a sheaf, so its sheafification map is an isomorphism.
:::

<1>6. In particular,
\[
\boxed{
\Gamma\!\left(X,\varinjlim_i\mcf_i\right)
=\varinjlim_i\Gamma(X,\mcf_i).
}
\]
::: {.proof}
Evaluate the equality of sheaves in <1>5 on the open set $X$:
\[
\left(\varinjlim_i\mcf_i\right)(X)
=\mcp(X)
=\varinjlim_i\mcf_i(X).
\]
By definition, these are the two sides of the displayed identity.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>5 proves that the sectionwise direct limit is already a sheaf, and <1>6 gives the stated consequence for global sections.
:::
:::
