---
schema: qual/card@1
id: P-NORI-GT-4-06
kind: problem
title: $S_d$ as a Galois group via symmetric rational functions
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.6 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let F be any field.
We have an action of the permutation group $S _ { d }$ on the polynomial ring $F [ X _ { 1 } , X _ { 2 } , . . . , X _ { d } ]$ by permuting the variables: for $\sigma \in S _ { d } .$ , we define $\sigma f ( X _ { 1 } , . . . , X _ { n } ) = f ( X _ { \sigma ( 1 ) } , . . . , X _ { \sigma ( n ) } )$ . This action of $S _ { d }$ on $F [ X _ { 1 } , . . . , X _ { d } ]$ extends uniquely to an action of $S _ { d }$ on its fraction field $F ( X _ { 1 } , . . . , X _ { n } )$

Employ Emil Artin’s theorem to deduce that there is a finite Galois extension of fields with $S _ { d }$ as Galois group.
:::

::: {.solution}

Let
$$
L=F(X_1,\ldots,X_d).
$$

::: pf

::: {.pf-step #s1-1}

The variable-permutation action defines an injective homomorphism
$$
S_d\hookrightarrow\operatorname{Aut}_F(L).
$$


::: pf-proof

A permutation $\sigma\in S_d$ acts on the polynomial ring by
$$
\sigma(f)(X_1,\ldots,X_d)
=f(X_{\sigma(1)},\ldots,X_{\sigma(d)}),
$$
and hence on the fraction field by
$$
\sigma\left(\frac fg\right)=\frac{\sigma(f)}{\sigma(g)}.
$$
This is an $F$-automorphism, and composition agrees with composition of permutations.

If $\sigma$ is not the identity, choose $i$ with $\sigma(i)\ne i$. Then
$$
\sigma(X_i)=X_{\sigma(i)}\ne X_i
$$
in the rational function field. Thus the action is faithful.

:::

:::

::: pf-step

Let
$$
K=L^{S_d}
=\{a\in L:\sigma(a)=a\text{ for every }\sigma\in S_d\}
$$
be the fixed field.


::: pf-proof

The set of elements fixed by every automorphism in a group is closed under addition, multiplication, additive inverses, and inversion of nonzero elements, so it is a subfield of $L$. Since every permutation fixes $F$, one has $F\subseteq K$.

:::

:::

::: {.pf-step #s1-3}

Artin's theorem on fixed fields gives
$$
[L:K]=\cardinality{S_d}=d!
$$
and
$$
\operatorname{Gal}(L/K)=S_d.
$$


::: pf-proof

Artin's theorem states: if a finite group $G$ acts faithfully by automorphisms on a field $L$ and $K=L^G$ is its fixed field, then
$$
[L:K]=\cardinality{G},
$$
the extension $L/K$ is finite Galois, and the full Galois group is exactly $G$.

Apply the theorem with
$$
G=S_d
$$
and the faithful action from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
F(X_1,\ldots,X_d)
/
F(X_1,\ldots,X_d)^{S_d}
}
$$
is a finite Galois extension with Galois group
$$
\boxed{S_d}.
$$


::: pf-proof

This is the conclusion of step [](#s1-3){.pf-ref} written for the present fields.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} supplies the requested finite Galois extension realizing $S_d$ as a Galois group.

:::

:::

:::
