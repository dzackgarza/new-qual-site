---
schema: qual/card@1
id: P-UCLAB14S-08
kind: problem
title: A smooth cutoff function on Euclidean space
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 8.

(a) Let $f:\mathbb R\to\mathbb R$ be defined by
\[
f(x)=
\begin{cases}
0,&x\leq 0,\\
e^{-1/x},&x>0.
\end{cases}
\]
Prove that $f$ is infinitely differentiable.

(b) In Euclidean space $\mathbb R^n$, for $n\geq 1$, find a function $\varphi\in C^\infty(\mathbb R^n)$ such that $\varphi(x)\geq 0$ for all $x$, $\varphi(x)=0$ if $|x|>1$, and
\[
\int_{\mathbb R^n}\varphi(x)\,dx=1.
\]
:::

::: {.solution}
<1>1. For every integer $m\geq0$,
\[
\lim_{x\downarrow0}x^{-m}e^{-1/x}=0.
\]

::: {.proof}
Set $t=1/x$. Then $x\downarrow0$ means $t\to\infty$, and
\[
x^{-m}e^{-1/x}=t^me^{-t}.
\]
Repeated l'Hopital, or the power-series estimate $e^t\geq t^{m+1}/(m+1)!$, shows $t^me^{-t}\to0$.
:::

<1>2. For every $k\geq0$ there is a polynomial $P_k$ such that, for $x>0$,
\[
f^{(k)}(x)=P_k(1/x)e^{-1/x}.
\]

::: {.proof}
For $k=0$, take $P_0=1$. If the formula holds for $k$, differentiation gives
\[
f^{(k+1)}(x)
=\left[-x^{-2}P_k'(1/x)+x^{-2}P_k(1/x)\right]e^{-1/x},
\]
which again has the required form with a polynomial in $1/x$.
:::

<1>3. For every $k\geq0$,
\[
\lim_{x\downarrow0}f^{(k)}(x)=0.
\]

::: {.proof}
Expand the polynomial in step <1>2 into finitely many monomials $c_mx^{-m}$. Each monomial times $e^{-1/x}$ tends to zero by step <1>1.
:::

<1>4. The function $f$ is $C^\infty$ on $\mathbb R$, and
\[
f^{(k)}(0)=0
\qquad(k\geq0).
\]

::: {.proof}
On $(-\infty,0)$ the function is identically zero and on $(0,\infty)$ it is smooth. Induct on $k$. Suppose $f^{(k)}$ extends continuously to $0$ with value $0$. Its derivative at zero is
\[
\lim_{h\to0}\frac{f^{(k)}(h)-f^{(k)}(0)}h.
\]
For $h<0$ the quotient is zero. For $h>0$, step <1>2 expresses it as a finite sum of terms $h^{-m}e^{-1/h}$, which tend to zero by step <1>1. Thus the derivative exists and equals zero; step <1>3 gives continuity of the next derivative. This proves the assertion for all $k$.
:::

<1>5. Define
\[
\psi(x)=f(1-|x|^2),
\qquad x\in\mathbb R^n.
\]
Then $\psi\in C^\infty(\mathbb R^n)$, $\psi\geq0$, and
\[
\psi(x)=0\quad\text{for }|x|\geq1,
\]
while $\psi(x)>0$ for $|x|<1$.

::: {.proof}
The map $x\mapsto1-|x|^2$ is smooth, and step <1>4 says $f$ is smooth, so their composition is smooth. The defining formula for $f$ gives nonnegativity and the support statement immediately.
:::

<1>6. The number
\[
C=\int_{\mathbb R^n}\psi(x)\,dx
\]
is finite and strictly positive.

::: {.proof}
The function $\psi$ is continuous and supported in the compact unit ball, hence integrable with finite integral. It is nonnegative everywhere and strictly positive on the open unit ball, so its integral is positive.
:::

<1>7. Set
\[
\varphi(x)=C^{-1}\psi(x).
\]
Then
\[
\varphi\in C^\infty(\mathbb R^n),\qquad
\varphi\geq0,\qquad
\varphi(x)=0\text{ if }|x|>1,
\]
and
\[
\int_{\mathbb R^n}\varphi(x)\,dx=1.
\]

::: {.proof}
All regularity, positivity, and support properties follow from step <1>5 because $C>0$. By the definition of $C$,
\[
\int\varphi=C^{-1}\int\psi=1.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), and step <1>7 constructs the function required in part (b).
:::
:::
