---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-03
kind: problem
title: Cup-length obstruction from a contractible cover
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 3 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Let $X$ be a topological space with subspaces $A_1,\dots,A_n$.
Assume that every $A_i$ is contractible and that
\[
\bigcup_i A_i=X.
\]

(a) Prove that if $R$ is a ring and $\alpha_1,\dots,\alpha_n\in H^*(X;R)$ all have positive degree, then
\[
\alpha_1\smile\cdots\smile\alpha_n=0.
\]

(b) Prove that $\RP^n$ cannot be covered by $n$ contractible subspaces.
:::

::: {.solution}

## Part (a)

Let
\[
\alpha_i\in H^{d_i}(X;R),
\qquad
d_i>0.
\]

::: pf

::: {.pf-step #s1-1}

For every \(i\),
\[
\boxed{
\alpha_i|_{A_i}=0
\in H^{d_i}(A_i;R)}.
\]


::: pf-proof

Each \(A_i\) is contractible, so
\[
H^{d_i}(A_i;R)=0
\]
for every positive degree \(d_i>0\).

:::

:::

::: pf-step

The long exact sequence of the pair \((X,A_i)\) contains
\[
H^{d_i}(X,A_i;R)
\longrightarrow
H^{d_i}(X;R)
\longrightarrow
H^{d_i}(A_i;R).
\]


::: pf-proof

This is the standard long exact cohomology sequence for a pair.

:::

:::

::: {.pf-step #s1-3}

By step [](#s1-1){.pf-ref} and exactness, there exists
\[
\widetilde\alpha_i
\in
H^{d_i}(X,A_i;R)
\]
mapping to \(\alpha_i\).


::: pf-proof

The restriction of \(\alpha_i\) to \(A_i\) is zero, so \(\alpha_i\) lies in the kernel of the restriction map. Exactness says this kernel equals the image of
\[
H^{d_i}(X,A_i;R).
\]

:::

:::

::: {.pf-step #s1-4}

Relative cup product gives
\[
\boxed{
\widetilde\alpha_1\smile\cdots\smile\widetilde\alpha_n
\in
H^{d_1+\cdots+d_n}
\left(
X,\,
A_1\cup\cdots\cup A_n;
R
\right)}.
\]


::: pf-proof

The relative cup product has the form
\[
H^p(X,A;R)\times H^q(X,B;R)
\longrightarrow
H^{p+q}(X,A\cup B;R),
\]
and iterating this construction gives the displayed class.

:::

:::

::: {.pf-step #s1-5}

Since
\[
A_1\cup\cdots\cup A_n=X,
\]
the group in step [](#s1-4){.pf-ref} is
\[
\boxed{
H^{d_1+\cdots+d_n}(X,X;R)=0}.
\]


::: pf-proof

Relative cohomology of a pair \((X,X)\) is zero in every degree.

:::

:::

::: {.pf-step #s1-6}

Therefore
\[
\boxed{
\widetilde\alpha_1\smile\cdots\smile\widetilde\alpha_n=0}.
\]


::: pf-proof

The class lies in the zero group by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Under the natural map from relative to absolute cohomology, the class in step [](#s1-6){.pf-ref} maps to
\[
\alpha_1\smile\cdots\smile\alpha_n.
\]


::: pf-proof

Relative cup product is natural with respect to the forgetful maps
\[
H^*(X,A_i;R)\to H^*(X;R),
\]
and each \(\widetilde\alpha_i\) maps to \(\alpha_i\) by step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Hence
\[
\boxed{
\alpha_1\smile\cdots\smile\alpha_n=0}.
\]


::: pf-proof

The image of the zero class from step [](#s1-6){.pf-ref} is zero, and by step [](#s1-7){.pf-ref} that image is the desired product.

:::

:::

::: pf-step

Over \(\FF_2\),
\[
\boxed{
H^*(\RP^n;\FF_2)
\cong
\FF_2[x]/(x^{n+1})}
\]
with
\[
|x|=1.
\]


::: pf-proof

This is the standard mod-\(2\) cohomology ring of real projective space.

:::

:::

::: {.pf-step #s1-10}

In particular,
\[
\boxed{
x^n\ne0
\in H^n(\RP^n;\FF_2)}.
\]


::: pf-proof

In the quotient ring
\[
\FF_2[x]/(x^{n+1}),
\]
the class \(x^n\) survives while \(x^{n+1}=0\).

:::

:::

::: pf-step

Apply part (a) with
\[
R=\FF_2
\]
and
\[
\alpha_1=\cdots=\alpha_n=x.
\]


::: pf-proof

The class \(x\) has positive degree \(1\), so it satisfies the hypotheses of part (a).

:::

:::

::: {.pf-step #s1-12}

Part (a) then gives
\[
\boxed{x^n=0}.
\]


::: pf-proof

Step [](#s1-8){.pf-ref} says the cup product of \(n\) positive-degree classes vanishes under an \(n\)-set contractible cover.

:::

:::

::: {.pf-step #s1-13}

This contradicts step [](#s1-10){.pf-ref}.


::: pf-proof

Step [](#s1-10){.pf-ref} says \(x^n\ne0\), while step [](#s1-12){.pf-ref} says \(x^n=0\).

:::

:::

::: {.pf-step #s1-14}

Therefore
\[
\boxed{
\RP^n
\text{ cannot be covered by }n\text{ contractible subspaces}.}
\]


::: pf-proof

The assumed cover led to the contradiction in step [](#s1-13){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves part (a), and step [](#s1-14){.pf-ref} proves part (b).

:::

:::

:::
