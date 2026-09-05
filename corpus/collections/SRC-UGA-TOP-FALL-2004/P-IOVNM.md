---
schema: qual/card@1
id: P-IOVNM
kind: problem
title: The quotient of a compact Hausdorff space by a closed equivalence relation
  is Hausdorff
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Hausdorff Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 2 of the official UGA Fall 2004 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Verified that the quotient projection is closed by compactness of saturated
    closed sets, then descended disjoint neighborhoods of two equivalence
    classes to the quotient.
---

::: {.problem}
Let $X$ be a compact Hausdorff space and suppose $R \subset X \times X$ is a closed equivalence relation.
Show that the quotient space $X/R$ is Hausdorff.
:::

::: {.solution}
Let
\[
q:X\longrightarrow X/R
\]
be the quotient projection.

<1>1. The saturation of every closed subset of $X$ is closed.
::: {.proof}
Let $F\subseteq X$ be closed.
Since $X$ is compact, $F$ is compact, and therefore
\[
F\times X
\]
is compact.
The relation $R$ is closed in $X\times X$, so
\[
R\cap(F\times X)
\]
is closed in the compact space $F\times X$ and hence is compact.

Let
\[
p_2:X\times X\longrightarrow X
\]
be projection onto the second factor.
Then
\[
p_2\bigl(R\cap(F\times X)\bigr)
=q^{-1}(q(F)).
\]
Indeed, a point $y\in X$ lies in the left-hand side exactly when there is some $x\in F$ with
\[
(x,y)\in R,
\]
which is exactly the condition that $y$ be equivalent to some point of $F$.

The continuous image of a compact space is compact, so
\[
q^{-1}(q(F))
\]
is compact.
Since $X$ is Hausdorff, it is therefore closed in $X$.
:::

<1>2. The quotient map $q$ is a closed map.
::: {.proof}
Let $F\subseteq X$ be closed.
By <1>1,
\[
q^{-1}(q(F))
\]
is closed in $X$.
Because $q$ is a quotient map, a subset $C\subseteq X/R$ is closed exactly when
\[
q^{-1}(C)
\]
is closed in $X$: this is the defining quotient condition applied to complements.
Taking $C=q(F)$ therefore shows that
\[
q(F)
\]
is closed in $X/R$.
Thus $q$ is closed.
:::

<1>3. Every equivalence class is compact.
::: {.proof}
Fix $x\in X$ and consider
\[
i_x:X\longrightarrow X\times X,
\qquad
i_x(y)=(x,y).
\]
This map is continuous, and the equivalence class of $x$ is
\[
[x]=i_x^{-1}(R).
\]
Since $R$ is closed, $[x]$ is closed in $X$.
Because $X$ is compact, $[x]$ is compact.
:::

<1>4. Any two distinct equivalence classes have disjoint open neighborhoods in $X$.
::: {.proof}
Let $A$ and $B$ be distinct equivalence classes.
They are disjoint compact subsets of the Hausdorff space $X$ by <1>3.

For each $a\in A$ and $b\in B$, choose disjoint open neighborhoods
\[
U_{a,b}\ni a,
\qquad
V_{a,b}\ni b.
\]
Fix $a\in A$.
The sets $V_{a,b}$ cover the compact set $B$, so choose
\[
b_1,\ldots,b_r\in B
\]
such that
\[
B\subseteq V_{a,b_1}\cup\cdots\cup V_{a,b_r}.
\]
Set
\[
U_a=U_{a,b_1}\cap\cdots\cap U_{a,b_r},
\qquad
V_a=V_{a,b_1}\cup\cdots\cup V_{a,b_r}.
\]
Then $U_a$ and $V_a$ are disjoint open sets with
\[
a\in U_a,
\qquad
B\subseteq V_a.
\]

The sets $U_a$ cover the compact set $A$, so choose
\[
a_1,\ldots,a_s\in A
\]
with
\[
A\subseteq U_{a_1}\cup\cdots\cup U_{a_s}.
\]
Define
\[
U=U_{a_1}\cup\cdots\cup U_{a_s},
\qquad
V=V_{a_1}\cap\cdots\cap V_{a_s}.
\]
Then $U$ and $V$ are open,
\[
A\subseteq U,
\qquad
B\subseteq V,
\]
and $U\cap V=\emptyset$.
Indeed, if $z\in U$, then $z\in U_{a_j}$ for some $j$, while every point of $V$ lies in $V_{a_j}$, and those two sets are disjoint.
:::

<1>5. Distinct points of $X/R$ have disjoint open neighborhoods.
::: {.proof}
Let
\[
\alpha,\beta\in X/R,
\qquad
\alpha\ne\beta,
\]
and let
\[
A=q^{-1}(\alpha),
\qquad
B=q^{-1}(\beta).
\]
By <1>4, choose disjoint open sets $U,V\subseteq X$ such that
\[
A\subseteq U,
\qquad
B\subseteq V.
\]

Define
\[
O_\alpha=(X/R)\setminus q(X\setminus U),
\qquad
O_\beta=(X/R)\setminus q(X\setminus V).
\]
The sets $X\setminus U$ and $X\setminus V$ are closed in $X$.
By <1>2 their images under $q$ are closed, so $O_\alpha$ and $O_\beta$ are open in $X/R$.

Since the whole fiber $A$ lies in $U$, no representative of $\alpha$ lies in $X\setminus U$.
Hence
\[
\alpha\in O_\alpha.
\]
Similarly,
\[
\beta\in O_\beta.
\]

Finally, if $\gamma\in O_\alpha$, then
\[
q^{-1}(\gamma)\subseteq U,
\]
because otherwise $\gamma\in q(X\setminus U)$.
Likewise, if $\gamma\in O_\beta$, then
\[
q^{-1}(\gamma)\subseteq V.
\]
Since every fiber of $q$ is nonempty and $U\cap V=\emptyset$, no $\gamma$ can lie in both $O_\alpha$ and $O_\beta$.
Thus
\[
O_\alpha\cap O_\beta=\emptyset.
\]
:::

<1>6. Therefore $X/R$ is Hausdorff.
::: {.proof}
By <1>5, every pair of distinct points of $X/R$ has disjoint open neighborhoods, which is exactly the Hausdorff condition.
:::
:::
