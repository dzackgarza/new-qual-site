---
schema: qual/card@1
id: E-AMD-FN5JCFZP
kind: problem
title: Cayley--Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    theorem, proved here rather than cited, over an arbitrary commutative ring with
    1 and not only over a field), and the existing prose solution against a fresh
    re-derivation: the adjugate identity over R[t] gives (tI - A) adj(tI - A) =
    p(t) I; the adjugate has entries of degree at most n-1, so it is
    sum B_k t^k for k < n; comparing coefficients of t^0, t^k and t^n gives
    -A B_0 = c_0 I, B_{k-1} - A B_k = c_k I, and B_{n-1} = c_n I; multiplying by
    I, A, ..., A^n and adding telescopes because A^k B_{k-1} appears with both
    signs, leaving p(A) = 0. Correct. Two things the prose assumed are now argued:
    that the entries of the adjugate have degree at most n-1, and that c_n = 1.
    No source solution is retained for this card, so no source comparison was
    made. What was not checked: any printed source.
---

::: {.exercise}
Prove the Cayley--Hamilton theorem.
:::

::: {.solution}
Let $R$ be a commutative ring with $1$, let $A\in\Mat_n(R)$ with $n\geq1$, and let $p(t)=\det(t\Id-A)=c_0+c_1t+\cdots+c_nt^n$ be the characteristic polynomial, so that $c_n=1$; $\operatorname{adj}(M)$ denotes the adjugate of a square matrix $M$, characterised by $M\operatorname{adj}(M)=\det(M)\Id$.

::: pf

::: {.pf-step #degree}
$p$ has degree $n$ and leading coefficient $c_n=1$, and $\operatorname{adj}(t\Id-A)$ is a matrix over $R$ whose entries are polynomials in $t$ of degree at most $n-1$; hence $\operatorname{adj}(t\Id-A)=B_0+B_1t+\cdots+B_{n-1}t^{n-1}$ with $B_k\in\Mat_n(R)$.

::: pf-proof
$t\Id-A$ has degree-one entries on the diagonal and constant entries elsewhere, so its determinant is a sum of products of $n$ entries, exactly one of which contributes the $t$ from each row; the term of highest degree is the product of the $n$ diagonal entries, namely $t^n$, so $p$ is monic of degree $n$ and $c_n=1$. The $(i,j)$ entry of the adjugate is $(-1)^{i+j}$ times the determinant of an $(n-1)\times(n-1)$ submatrix of $t\Id-A$, hence a polynomial of degree at most $n-1$; collecting the coefficients of $t^k$ across all entries gives the matrices $B_k$.
:::

:::

::: {.pf-step #adjugate}
Over the ring $R[t]$, $(t\Id-A)\,(B_0+B_1t+\cdots+B_{n-1}t^{n-1})=p(t)\,\Id$.

::: pf-proof
$R[t]$ is a commutative ring, so the adjugate identity $M\operatorname{adj}(M)=\det(M)\Id$ applies to $M=t\Id-A\in\Mat_n(R[t])$; its determinant is by definition $p(t)$, and its adjugate is $B_0+\cdots+B_{n-1}t^{n-1}$ by step [](#degree){.pf-ref}.
:::

:::

::: {.pf-step #coefficients}
Comparing coefficients of $t$ in step [](#adjugate){.pf-ref} gives $-AB_0=c_0\Id$, then $B_{k-1}-AB_k=c_k\Id$ for $1\leq k\leq n-1$, and finally $B_{n-1}=c_n\Id$.

::: pf-proof
Expanding the left-hand side,
$$(t\Id-A)\sum_{k=0}^{n-1}B_kt^k=\sum_{k=0}^{n-1}B_kt^{k+1}-\sum_{k=0}^{n-1}AB_kt^k=\sum_{j=1}^{n}B_{j-1}t^j-\sum_{k=0}^{n-1}AB_kt^k.$$
The coefficient of $t^0$ is $-AB_0$, and on the right it is $c_0\Id$. For $1\leq k\leq n-1$ the coefficient of $t^k$ is $B_{k-1}-AB_k$ (the first sum contributing $B_{k-1}$ with $j=k$, the second $-AB_k$), and on the right it is $c_k\Id$. The coefficient of $t^n$ is $B_{n-1}$ from the first sum, the second sum having no $t^n$ term, and on the right it is $c_n\Id$. Two matrices with entries in $R[t]$ are equal exactly when the coefficient matrices of each power of $t$ agree.
:::

:::

::: {.pf-step #telescope}
$c_0\Id+c_1A+\cdots+c_nA^n=0$.

::: pf-proof
Multiply the equations of step [](#coefficients){.pf-ref} on the left by $\Id,A,A^2,\ldots,A^n$ respectively and add:
$$-AB_0+\bigl(AB_0-A^2B_1\bigr)+\bigl(A^2B_1-A^3B_2\bigr)+\cdots+\bigl(A^{n-1}B_{n-2}-A^nB_{n-1}\bigr)+A^nB_{n-1}=0,$$
where the right-hand sides sum to $c_0\Id+c_1A+\cdots+c_nA^n$. In the left-hand side each $A^{k}B_{k-1}$ occurs once with a plus sign and once with a minus sign, except the first term $-AB_0$ and the last term $A^nB_{n-1}$, which have no partner; so the sum telescopes to $0$. The two sides being equal, $c_0\Id+c_1A+\cdots+c_nA^n=0$.
:::

:::

::: {.pf-step}
$p(A)=0$, that is, the Cayley--Hamilton theorem holds for $A$.

::: pf-proof
Evaluating $p$ at the matrix $A$ gives $p(A)=c_0\Id+c_1A+\cdots+c_nA^n$ by the definition of polynomial evaluation on matrices, and step [](#telescope){.pf-ref} shows this is the zero matrix. The argument used only that $R$ is commutative, so it holds for matrices over any commutative ring with $1$, in particular over a field.
:::

:::

:::
:::
