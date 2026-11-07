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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read (a) in both directions: restricting a retraction to the cone gives the contraction of $A$
    in $X$, and a contraction extends over the cone and is well defined at the cone vertex. Read
    (b): $(Y,X)$ is a good pair with $Y/X=SA$, so $H_n(Y,X)\cong\tilde H_{n-1}(A)$; the retraction
    makes $i_*$ injective and splits the long exact sequence, giving
    $\tilde H_n(Y)\cong\tilde H_n(X)\oplus\tilde H_{n-1}(A)$; and excision over the contractible
    cone identifies $H_n(X,A)$ with $\tilde H_n(Y)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 26 (a) and (b) as printed on p. 157, including the hint that
    (X union CA)/X is SA. Part (a) is correct in both directions; the converse now says why the
    formula for r is continuous, from the attaching-space description on pp. 12-13. Part (b) had
    two unnamed steps, now cited: the good-pair identification is Proposition 2.22 p. 124, the
    homeomorphism (X union CA)/X = CA/A is the printed hint, and the suspension isomorphism is
    no longer quoted but derived from the pair sequence of Theorem 2.16 p. 117 for the
    contractible pair (CA,A) together with Proposition 2.22; excision is Theorem 2.20 p. 119.
    What is not covered: the good-pair hypothesis for (Y,X) is asserted from the deformation
    retraction of a neighborhood, not constructed.
---

::: {.problem}
For a pair $(X, A)$, let $X \cup CA$ be $X$ with a cone on $A$ attached.

(a) Show that $X$ is a retract of $X \cup CA$ iff $A$ is contractible in $X$: There is a homotopy $f_t: A \to X$ with $f_0$ the inclusion $A \hookrightarrow X$ and $f_1$ a constant map.

(b) Show that if $A$ is contractible in $X$ then $H_n(X, A) \approx \tilde{H}_n(X) \oplus \tilde{H}_{n-1}(A)$, using the fact that $(X \cup CA)/X$ is the suspension $SA$ of $A$.
:::

::: {.solution}
Set
$$
Y=X\cup CA.
$$

::: pf

::: pf-step
If there is a retraction $r:Y\to X$, then $A$ is contractible in $X$.

::: pf-proof
Parametrize the cone as
$$
CA=A\times[0,1]/(A\times\{1\}),
$$
with $A=A\times\{0\}$. Restrict $r$ to the cone and define
$$
f_t(a)=r([a,t]).
$$
Since $r\restrict_X=\operatorname{id}_X$, one has
$$
f_0(a)=a.
$$
At $t=1$ all points $[a,1]$ are the cone vertex, so $f_1$ is constant. Thus $f_t$ contracts the inclusion $A\hookrightarrow X$ to a constant map inside $X$.
:::

:::

::: pf-step
Conversely, if the inclusion $A\hookrightarrow X$ is homotopic in $X$ to a constant map, then $X$ is a retract of $Y$.

::: pf-proof
Let
$$
f_t:A\to X,
\qquad f_0(a)=a,\quad f_1(a)=x_0,
$$
be such a homotopy. Define $r:Y\to X$ by
$$
r\restrict_X=\operatorname{id}_X,
\qquad
r([a,t])=f_t(a)
$$
on $CA$. This is well defined at the cone vertex because $f_1$ is constant, and the two definitions agree along $A=A\times\{0\}$. Continuity follows from the defining property of the attaching space: $Y=X\cup_f CA$ is the quotient of the disjoint union $X\coprod CA$ by the identification of $A\subset CA$ with its image under the attaching map (pp. 12–13), and a map on a quotient is continuous exactly when its composition with the quotient map is, which holds here because $f_t$ is a homotopy. Hence $r$ is a continuous retraction.
:::

:::

::: pf-qed
This proves part (a).
:::

:::

Assume now that $A$ is contractible in $X$, so the retraction exists.

::: pf

::: {.pf-step #s3}
The pair $(Y,X)$ has
$$
H_n(Y,X)\cong\widetilde H_n(Y/X)\cong\widetilde H_n(SA)\cong\widetilde H_{n-1}(A).
$$

::: pf-proof
Collapsing $X$ in $Y=X\cup CA$ leaves
$$
CA/A=SA.
$$
The first identification is Proposition 2.22 (p. 124), the pair $(Y,X)$ being good because $X$ is a deformation retract of a neighborhood in $Y$; the second is the homeomorphism $(X\cup CA)/X\cong CA/A$ quoted in the hint. For the third, $CA$ is contractible, so the pair sequence of Theorem 2.16 (p. 117) for $(CA,A)$ reads
$$
0=H_n(CA)\to H_n(CA,A)\xrightarrow{\ \cong\ }\widetilde H_{n-1}(A)\to\widetilde H_{n-1}(CA)=0,
$$
and Proposition 2.22 (p. 124) identifies $H_n(CA,A)$ with $\widetilde H_n(CA/A)=\widetilde H_n(SA)$. This derives the suspension isomorphism from the pair rather than quoting it.
:::

:::

::: {.pf-step #s4}
The retraction splits the long exact sequence of $(Y,X)$, giving
$$
\widetilde H_n(Y)\cong
\widetilde H_n(X)\oplus\widetilde H_{n-1}(A).
$$

::: pf-proof
The inclusion $i:X\hookrightarrow Y$ has a left inverse $r$, so $i_*$ is injective in every degree. Hence the connecting map
$$
H_n(Y,X)\to H_{n-1}(X)
$$
has zero image, and the long exact sequence breaks into short exact sequences
$$
0\to\widetilde H_n(X)\xrightarrow{i_*}\widetilde H_n(Y)
\to H_n(Y,X)\to0.
$$
The map $r_*$ splits these sequences. Apply step [](#s3){.pf-ref}.
:::

:::

::: {.pf-step #s5}
There is a natural isomorphism
$$
H_n(X,A)\cong\widetilde H_n(Y).
$$

::: pf-proof
The cone $CA$ is contractible. Excision, Theorem 2.20 (p. 119), applied to the cover $Y=X\cup CA$ with the interior of $CA$ as one of the two sets, identifies
$$
H_n(X,A)\cong H_n(Y,CA).
$$
Since $CA$ is contractible and nonempty, the pair sequence of Theorem 2.16 (p. 117) for $(Y,CA)$ gives
$$
H_n(Y,CA)\cong\widetilde H_n(Y)
$$
with the standard reduced interpretation in degree $0$: the terms $\widetilde H_n(CA)$ vanish, so the map $\widetilde H_n(Y)\to H_n(Y,CA)$ is an isomorphism for $n\ge1$, and for $n=0$ the same argument applies with $\widetilde H_{-1}=0$.
:::

:::

::: pf-step
Combining steps [](#s4){.pf-ref} and [](#s5){.pf-ref} yields
$$
\boxed{H_n(X,A)\cong\widetilde H_n(X)\oplus\widetilde H_{n-1}(A).}
$$
:::

:::

:::
