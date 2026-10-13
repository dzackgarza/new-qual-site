---
schema: qual/card@1
id: P-NORI-GT-4-07
kind: problem
title: Every finite group is a Galois group
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.7 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Show that every finite group can be realised as the Galois group of some finite Galois extension of fields.
:::

::: {.solution}
Let $G$ be a finite group and let $F$ be any field. Introduce algebraically independent indeterminates
$$
\{X_h:h\in G\}
$$
and set
$$
L=F(X_h:h\in G).
$$

<1>1. The group $G$ acts on $L$ by $F$-automorphisms via
$$
g(X_h)=X_{gh}
$$
for $g,h\in G$.

::: {.proof}
For fixed $g\in G$, the assignment
$$
X_h\longmapsto X_{gh}
$$
is a permutation of the set of indeterminates, so it extends uniquely to an automorphism of the polynomial ring and then of its fraction field $L$, fixing $F$ pointwise.

For $g_1,g_2\in G$,
$$
g_1(g_2(X_h))
=g_1(X_{g_2h})
=X_{g_1g_2h}
=(g_1g_2)(X_h),
$$
so this is a group action.
:::

<1>2. The action in step <1>1 is faithful.

::: {.proof}
If $g\ne e$, then
$$
g(X_e)=X_g\ne X_e.
$$
Thus no nonidentity element acts trivially.
:::

<1>3. Let
$$
K=L^G
$$
be the fixed field. Then
$$
L/K
$$
is a finite Galois extension and
$$
\operatorname{Gal}(L/K)\cong G.
$$

::: {.proof}
Artin's fixed-field theorem states that if a finite group $G$ acts faithfully by automorphisms on a field $L$, then for the fixed field $K=L^G$ one has
$$
[L:K]=|G|
$$
and
$$
\operatorname{Gal}(L/K)=G.
$$
The hypotheses are verified by steps <1>1--<1>2.
:::

<1>4. Therefore every finite group is realizable as the Galois group of a finite Galois extension.

::: {.proof}
For the arbitrary finite group $G$, step <1>3 explicitly constructs such an extension $L/L^G$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required assertion.
:::
:::
