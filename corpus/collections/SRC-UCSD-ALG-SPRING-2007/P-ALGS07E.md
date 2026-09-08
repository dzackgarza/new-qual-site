---
schema: qual/card@1
id: P-ALGS07E
kind: problem
title: "An algebraic extension of a perfect field is perfect"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared the statement with Problem 5 of the official Spring 2007 UCSD algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Replaced the invalid claim that Frobenius on F(alpha) is F-linear. The corrected proof uses an F-basis and perfection of F to show the pth powers of the basis are again an F-basis.
---

::: problem
Recall that a "perfect" field of characteristic $p$ is one for which the Frobenius map $\operatorname{Fr}: x \mapsto x^p$ is onto.

Let $F$ be a perfect field, and $E/F$ an algebraic extension.
Show that $E$ is perfect.
:::

::: {.solution}
<1>1. It is enough to prove that every $\alpha\in E$ has a $p$th root in $E$.
::: {.proof}
By the definition recalled in the problem, a field of characteristic $p$ is perfect exactly when its Frobenius map
\[
\operatorname{Fr}_E:E\longrightarrow E,
\qquad
x\longmapsto x^p,
\]
is surjective.
:::

<1>2. Fix $\alpha\in E$ and put $K=F(\alpha)$. Then $K/F$ is finite.
::: {.proof}
The extension $E/F$ is algebraic, so $\alpha$ is algebraic over $F$. Hence
\[
[K:F]=[F(\alpha):F]<\infty.
\]
:::

<1>3. If $e_1,\ldots,e_n$ is an $F$-basis of $K$, then $e_1^p,\ldots,e_n^p$ is also an $F$-basis of $K$.
::: {.proof}
It suffices to prove linear independence, because there are exactly $n=[K:F]$ elements.
Suppose
\[
\sum_{i=1}^n c_i e_i^p=0,
\qquad c_i\in F.
\]
Since $F$ is perfect, Frobenius on $F$ is surjective. Choose $d_i\in F$ with
\[
d_i^p=c_i.
\]
In characteristic $p$,
\[
0
=\sum_{i=1}^n d_i^p e_i^p
=\left(\sum_{i=1}^n d_i e_i\right)^p.
\]
A field has no nonzero nilpotents, so
\[
\sum_{i=1}^n d_i e_i=0.
\]
Because the $e_i$ are $F$-linearly independent, every $d_i=0$, hence every $c_i=0$.
Thus $e_1^p,\ldots,e_n^p$ is an $F$-basis of $K$.
:::

<1>4. Frobenius on $K$ is surjective.
::: {.proof}
Let $y\in K$. By <1>3, write
\[
y=\sum_{i=1}^n c_i e_i^p,
\qquad c_i\in F.
\]
Again using perfection of $F$, choose $d_i\in F$ with $d_i^p=c_i$. Then
\[
y
=\sum_{i=1}^n d_i^p e_i^p
=\left(\sum_{i=1}^n d_i e_i\right)^p.
\]
Thus $y$ is a $p$th power of an element of $K$.
:::

<1>5. Therefore Frobenius on $E$ is surjective, so $E$ is perfect.
::: {.proof}
Apply <1>4 to $y=\alpha$. There is $\beta\in K\subseteq E$ such that
\[
\beta^p=\alpha.
\]
Since $\alpha\in E$ was arbitrary, every element of $E$ has a $p$th root in $E$. Hence Frobenius on $E$ is surjective, and $E$ is perfect.
:::
:::
