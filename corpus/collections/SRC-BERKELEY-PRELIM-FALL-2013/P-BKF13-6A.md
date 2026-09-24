---
schema: qual/card@1
id: P-BKF13-6A
kind: problem
title: Conjugation-invariant quadratic forms on $2\times2$ complex matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 6A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the restriction to diagonal matrices, the conjugation symmetry,
    and an explicit density proof for matrices with distinct eigenvalues.
---

::: {.problem}
Let V be the complex vector space of complex $2 \times 2$ matrices X. Find all quadratic forms $Q$ on V such that $Q ( X ) = Q ( A X A ^ { - 1 } )$ for any complex invertible $2 \times 2$ matrix A.
:::

::: {.solution}
For $\alpha,\beta\in\CC$, define
$$
Q_{\alpha,\beta}(X)
\coloneqq
\alpha\,\operatorname{tr}(X^2)
+\beta\,\operatorname{tr}(X)^2.
$$

<1>1. Every $Q_{\alpha,\beta}$ is a conjugation-invariant quadratic
form.

::: {.proof}
Both $\operatorname{tr}(X^2)$ and $\operatorname{tr}(X)^2$ are
homogeneous quadratic polynomials in the entries of $X$. If $A$ is
invertible, then
$$
(AXA^{-1})^2=AX^2A^{-1},
$$
so invariance of trace under conjugation gives
$$
\operatorname{tr}((AXA^{-1})^2)
=\operatorname{tr}(X^2),
\qquad
\operatorname{tr}(AXA^{-1})
=\operatorname{tr}(X).
$$
Thus $Q_{\alpha,\beta}(AXA^{-1})=Q_{\alpha,\beta}(X)$.
:::

<1>2. The restriction of any conjugation-invariant quadratic form
$Q$ to diagonal matrices is of the form
$$
Q\!\left(
\begin{pmatrix}
a&0\\
0&b
\end{pmatrix}
\right)
=
\alpha(a^2+b^2)
+\beta(a+b)^2
$$
for unique $\alpha,\beta\in\CC$.

::: {.proof}
Because $Q$ is quadratic, its restriction to diagonal matrices has the
form
$$
c\,a^2+d\,ab+e\,b^2.
$$
Conjugation by
$$
P=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
$$
exchanges the two diagonal entries. Invariance therefore gives
$$
c\,a^2+d\,ab+e\,b^2
=
c\,b^2+d\,ab+e\,a^2
$$
for all $a,b$, so $c=e$. Hence
$$
Q(\operatorname{diag}(a,b))
=c(a^2+b^2)+d\,ab.
$$
Taking
$$
\beta=\frac d2,
\qquad
\alpha=c-\frac d2
$$
gives the displayed expression. Uniqueness follows by comparing the
coefficients of $a^2$ and $ab$.
:::

<1>3. Matrices with two distinct eigenvalues are dense in
$M_2(\CC)$.

::: {.proof}
Let
$$
X=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\qquad
D=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
$$
The discriminant of the characteristic polynomial of $X+tD$ is
$$
\begin{aligned}
\Delta(t)
&=\operatorname{tr}(X+tD)^2-4\det(X+tD)\\
&=(a+d)^2
-4\bigl(ad-bc+t(d-a)-t^2\bigr).
\end{aligned}
$$
This is a polynomial in $t$ with leading coefficient $4$, so it has
only finitely many zeros. Hence there are arbitrarily small nonzero
$t$ for which $\Delta(t)\ne0$. For such $t$, the matrix $X+tD$ has
two distinct eigenvalues and is therefore diagonalizable. Since
$X+tD\to X$ as $t\to0$, the claim follows.
:::

<1>4. Every conjugation-invariant quadratic form $Q$ equals one of the
forms in step <1>1.

::: {.proof}
Choose $\alpha,\beta$ from step <1>2 and set
$$
R\coloneqq Q-Q_{\alpha,\beta}.
$$
Then $R$ vanishes on every diagonal matrix. If $X$ is diagonalizable,
there is an invertible $A$ such that $AXA^{-1}$ is diagonal. Since both
$Q$ and $Q_{\alpha,\beta}$ are conjugation invariant,
$$
R(X)=R(AXA^{-1})=0.
$$
Thus $R$ vanishes on all matrices with distinct eigenvalues. By step
<1>3 this set is dense, and $R$ is a polynomial, hence continuous.
Therefore $R$ vanishes on all of $M_2(\CC)$.
:::

<1>5. Consequently the complete family is
$$
\boxed{
Q(X)
=
\alpha\,\operatorname{tr}(X^2)
+\beta\,\operatorname{tr}(X)^2,
\qquad
\alpha,\beta\in\CC.
}
$$

::: {.proof}
Step <1>1 shows that every displayed form is admissible, and step
<1>4 shows that there are no others.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested classification.
:::
:::
