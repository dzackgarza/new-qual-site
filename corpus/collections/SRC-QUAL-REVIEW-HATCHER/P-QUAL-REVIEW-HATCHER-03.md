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

(b) Prove that $\mathbb{RP}^n$ cannot be covered by $n$ contractible subspaces.
:::

::: {.solution}
## Part (a)

Let
\[
\alpha_i\in H^{d_i}(X;R),
\qquad
d_i>0.
\]

<1>1. For every \(i\),
\[
\boxed{
\alpha_i|_{A_i}=0
\in H^{d_i}(A_i;R)}.
\]

::: {.proof}
Each \(A_i\) is contractible, so
\[
H^{d_i}(A_i;R)=0
\]
for every positive degree \(d_i>0\).
:::

<1>2. The long exact sequence of the pair \((X,A_i)\) contains
\[
H^{d_i}(X,A_i;R)
\longrightarrow
H^{d_i}(X;R)
\longrightarrow
H^{d_i}(A_i;R).
\]

::: {.proof}
This is the standard long exact cohomology sequence for a pair.
:::

<1>3. By step <1>1 and exactness, there exists
\[
\widetilde\alpha_i
\in
H^{d_i}(X,A_i;R)
\]
mapping to \(\alpha_i\).

::: {.proof}
The restriction of \(\alpha_i\) to \(A_i\) is zero, so \(\alpha_i\) lies in the kernel of the restriction map. Exactness says this kernel equals the image of
\[
H^{d_i}(X,A_i;R).
\]
:::

<1>4. Relative cup product gives
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

::: {.proof}
The relative cup product has the form
\[
H^p(X,A;R)\times H^q(X,B;R)
\longrightarrow
H^{p+q}(X,A\cup B;R),
\]
and iterating this construction gives the displayed class.
:::

<1>5. Since
\[
A_1\cup\cdots\cup A_n=X,
\]
the group in step <1>4 is
\[
\boxed{
H^{d_1+\cdots+d_n}(X,X;R)=0}.
\]

::: {.proof}
Relative cohomology of a pair \((X,X)\) is zero in every degree.
:::

<1>6. Therefore
\[
\boxed{
\widetilde\alpha_1\smile\cdots\smile\widetilde\alpha_n=0}.
\]

::: {.proof}
The class lies in the zero group by step <1>5.
:::

<1>7. Under the natural map from relative to absolute cohomology, the class in step <1>6 maps to
\[
\alpha_1\smile\cdots\smile\alpha_n.
\]

::: {.proof}
Relative cup product is natural with respect to the forgetful maps
\[
H^*(X,A_i;R)\to H^*(X;R),
\]
and each \(\widetilde\alpha_i\) maps to \(\alpha_i\) by step <1>3.
:::

<1>8. Hence
\[
\boxed{
\alpha_1\smile\cdots\smile\alpha_n=0}.
\]

::: {.proof}
The image of the zero class from step <1>6 is zero, and by step <1>7 that image is the desired product.
:::

## Part (b)

Suppose, toward a contradiction, that
\[
\mathbb{RP}^n
=
A_1\cup\cdots\cup A_n
\]
with every \(A_i\) contractible.

<1>9. Over \(\mathbb F_2\),
\[
\boxed{
H^*(\mathbb{RP}^n;\mathbb F_2)
\cong
\mathbb F_2[x]/(x^{n+1})}
\]
with
\[
|x|=1.
\]

::: {.proof}
This is the standard mod-\(2\) cohomology ring of real projective space.
:::

<1>10. In particular,
\[
\boxed{
x^n\ne0
\in H^n(\mathbb{RP}^n;\mathbb F_2)}.
\]

::: {.proof}
In the quotient ring
\[
\mathbb F_2[x]/(x^{n+1}),
\]
the class \(x^n\) survives while \(x^{n+1}=0\).
:::

<1>11. Apply part (a) with
\[
R=\mathbb F_2
\]
and
\[
\alpha_1=\cdots=\alpha_n=x.
\]

::: {.proof}
The class \(x\) has positive degree \(1\), so it satisfies the hypotheses of part (a).
:::

<1>12. Part (a) then gives
\[
\boxed{x^n=0}.
\]

::: {.proof}
Step <1>8 says the cup product of \(n\) positive-degree classes vanishes under an \(n\)-set contractible cover.
:::

<1>13. This contradicts step <1>10.

::: {.proof}
Step <1>10 says \(x^n\ne0\), while step <1>12 says \(x^n=0\).
:::

<1>14. Therefore
\[
\boxed{
\mathbb{RP}^n
\text{ cannot be covered by }n\text{ contractible subspaces}.}
\]

::: {.proof}
The assumed cover led to the contradiction in step <1>13.
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>8 proves part (a), and step <1>14 proves part (b).
:::
:::
