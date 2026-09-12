---
schema: qual/card@1
id: E-HAT-2.2-26
kind: problem
title: Retraction of $X \cup CA$ onto $X$ iff $A$ contractible in $X$; homology decomposition
classification:
  areas:
  - topology
  topics:
  - Homology
  - Retractions
  - Cone Constructions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 26; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked.
---

For a pair $(X, A)$, let $X \cup CA$ be $X$ with a cone on $A$ attached.

(a) Show that $X$ is a retract of $X \cup CA$ iff $A$ is contractible in $X$: There is a homotopy $f_t: A \to X$ with $f_0$ the inclusion $A \hookrightarrow X$ and $f_1$ a constant map.

(b) Show that if $A$ is contractible in $X$ then $H_n(X, A) \approx \tilde{H}_n(X) \oplus \tilde{H}_{n-1}(A)$, using the fact that $(X \cup CA)/X$ is the suspension $SA$ of $A$.

::: {.solution}
Set
\[
Y=X\cup CA.
\]

<1>1. If there is a retraction $r:Y\to X$, then $A$ is contractible in $X$.
::: {.proof}
Parametrize the cone as
\[
CA=A\times[0,1]/(A\times\{1\}),
\]
with $A=A\times\{0\}$. Restrict $r$ to the cone and define
\[
f_t(a)=r([a,t]).
\]
Since $r|_X=\operatorname{id}_X$, one has
\[
f_0(a)=a.
\]
At $t=1$ all points $[a,1]$ are the cone vertex, so $f_1$ is constant. Thus $f_t$ contracts the inclusion $A\hookrightarrow X$ to a constant map inside $X$.
:::

<1>2. Conversely, if the inclusion $A\hookrightarrow X$ is homotopic in $X$ to a constant map, then $X$ is a retract of $Y$.
::: {.proof}
Let
\[
f_t:A\to X,
\qquad f_0(a)=a,\quad f_1(a)=x_0,
\]
be such a homotopy. Define $r:Y\to X$ by
\[
r|_X=\operatorname{id}_X,
\qquad
r([a,t])=f_t(a)
\]
on $CA$. This is well defined at the cone vertex because $f_1$ is constant, and the two definitions agree along $A=A\times\{0\}$. Hence $r$ is a continuous retraction.
:::

This proves part (a).

Assume now that $A$ is contractible in $X$, so the retraction exists.

<1>3. The pair $(Y,X)$ has
\[
H_n(Y,X)\cong\widetilde H_n(Y/X)\cong\widetilde H_n(SA)\cong\widetilde H_{n-1}(A).
\]
::: {.proof}
Collapsing $X$ in $Y=X\cup CA$ leaves
\[
CA/A=SA.
\]
The quotient theorem for relative homology and the suspension isomorphism give the displayed identifications.
:::

<1>4. The retraction splits the long exact sequence of $(Y,X)$, giving
\[
\widetilde H_n(Y)\cong
\widetilde H_n(X)\oplus\widetilde H_{n-1}(A).
\]
::: {.proof}
The inclusion $i:X\hookrightarrow Y$ has a left inverse $r$, so $i_*$ is injective in every degree. Hence the connecting map
\[
H_n(Y,X)\to H_{n-1}(X)
\]
has zero image, and the long exact sequence breaks into short exact sequences
\[
0\to\widetilde H_n(X)\xrightarrow{i_*}\widetilde H_n(Y)
\to H_n(Y,X)\to0.
\]
The map $r_*$ splits these sequences. Apply <1>3.
:::

<1>5. There is a natural isomorphism
\[
H_n(X,A)\cong\widetilde H_n(Y).
\]
::: {.proof}
The cone $CA$ is contractible. Excision identifies
\[
H_n(X,A)\cong H_n(Y,CA).
\]
Since $CA$ is contractible and nonempty, the long exact sequence of $(Y,CA)$ gives
\[
H_n(Y,CA)\cong\widetilde H_n(Y)
\]
(with the standard reduced interpretation in degree $0$).
:::

Combining <1>4 and <1>5 yields
\[
\boxed{H_n(X,A)\cong\widetilde H_n(X)\oplus\widetilde H_{n-1}(A).}
\]
:::
