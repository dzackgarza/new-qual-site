---
schema: qual/card@1
id: P-MAXAT-2-01
kind: problem
title: Maxim algebraic topology 2.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 2, problem 1 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find spaces with the same homotopy (homology) groups, but having different homotopy type.
:::

::: {.solution}

Two standard pairs answer the two parenthetical versions separately.

::: pf

::: {.pf-step #s1-1}

The spaces
\[
X=\CP^2,
\qquad
Y=S^2\vee S^4
\]
have isomorphic integral homology groups in every degree.


::: pf-proof

The standard CW structure on $\CP^2$ has one cell in dimensions $0,2,4$ and no others; its cellular boundary maps vanish, so
\[
H_k(\CP^2;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,2,4,\\
0,&\text{otherwise}.
\end{cases}
\]
For a wedge of connected based CW complexes,
\[
\widetilde H_k(S^2\vee S^4)
\cong\widetilde H_k(S^2)\oplus\widetilde H_k(S^4),
\]
which gives exactly the same groups.

:::

:::

::: {.pf-step #s1-2}

Nevertheless,
\[
\CP^2\not\simeq S^2\vee S^4.
\]


::: pf-proof

Homotopy equivalence preserves the integral cohomology ring. For $\CP^2$,
\[
H^*(\CP^2;\ZZ)
\cong\ZZ[u]/(u^3),
\qquad |u|=2,
\]
and $u^2\ne0$ in $H^4$. In $S^2\vee S^4$, the generator $v\in H^2$ comes from the $S^2$ summand and satisfies $v^2=0$, since $H^4(S^2)=0$ and positive-degree cup products between distinct wedge summands vanish. Thus the cohomology rings are not isomorphic.

:::

:::

::: {.pf-step #s1-3}

For an example with the same homotopy groups, take two distinct lens spaces
\[
L(5,1)
\qquad\text{and}\qquad
L(5,2).
\]


::: pf-proof

Both are closed $3$-manifolds obtained as free quotients of $S^3$ by an action of the cyclic group $C_5$. Their universal covering space is therefore $S^3$ and their fundamental group is $C_5$.

:::

:::

::: {.pf-step #s1-4}

These lens spaces have isomorphic homotopy groups in every degree:
\[
\pi_1(L(5,1))\cong\pi_1(L(5,2))\cong C_5,
\]
and, for every $k\geq2$,
\[
\pi_k(L(5,1))\cong\pi_k(S^3)
\cong\pi_k(L(5,2)).
\]


::: pf-proof

The fundamental-group statement is step [](#s1-3){.pf-ref}. A covering map induces an isomorphism on $\pi_k$ for every $k\geq2$. Apply this to the universal coverings $S^3\to L(5,q)$.

:::

:::

::: {.pf-step #s1-5}

But
\[
L(5,1)\not\simeq L(5,2).
\]


::: pf-proof

The homotopy classification of three-dimensional lens spaces states that
\[
L(p,q)\simeq L(p,q')
\quad\Longleftrightarrow\quad
qq'\equiv\pm a^2\pmod p
\]
for some unit $a$ modulo $p$. For $p=5$, $q=1$, and $q'=2$, this would require
\[
2\equiv\pm a^2\pmod5.
\]
The nonzero squares modulo $5$ are $1$ and $4=-1$, so the values $\pm a^2$ are only $1$ and $4$, never $2$. Hence the two lens spaces are not homotopy equivalent.

:::

:::

::: {.pf-step #s1-6}

Therefore the requested examples are
\[
\boxed{
\CP^2\text{ and }S^2\vee S^4
\text{ for equal homology groups},}
\]
and
\[
\boxed{
L(5,1)\text{ and }L(5,2)
\text{ for equal homotopy groups}.}
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} establish the homology example, and steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} establish the homotopy-group example.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} supplies both requested kinds of examples and proves that their homotopy types differ.

:::

:::

:::
