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

(a) Let $f:\RR\to\RR$ be defined by
$$
f(x)=
\begin{cases}
0,&x\leq 0,\\
e^{-1/x},&x>0.
\end{cases}
$$
Prove that $f$ is infinitely differentiable.

(b) In Euclidean space $\RR^n$, for $n\geq 1$, find a function $\varphi\in C^\infty(\RR^n)$ such that $\varphi(x)\geq 0$ for all $x$, $\varphi(x)=0$ if $\norm{x}>1$, and
$$
\int_{\RR^n}\varphi(x)\,dx=1.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every integer $m\geq0$,
$$
\lim_{x\downarrow0}x^{-m}e^{-1/x}=0.
$$


::: pf-proof

Set $t=1/x$. Then $x\downarrow0$ means $t\to\infty$, and
$$
x^{-m}e^{-1/x}=t^me^{-t}.
$$
Repeated l'Hopital, or the power-series estimate $e^t\geq t^{m+1}/(m+1)!$, shows $t^me^{-t}\to0$.

:::

:::

::: {.pf-step #s1-2}

For every $k\geq0$ there is a polynomial $P_k$ such that, for $x>0$,
$$
f^{(k)}(x)=P_k(1/x)e^{-1/x}.
$$


::: pf-proof

For $k=0$, take $P_0=1$. If the formula holds for $k$, differentiation gives
$$
f^{(k+1)}(x)
=\left[-x^{-2}P_k'(1/x)+x^{-2}P_k(1/x)\right]e^{-1/x},
$$
which again has the required form with a polynomial in $1/x$.

:::

:::

::: {.pf-step #s1-3}

For every $k\geq0$,
$$
\lim_{x\downarrow0}f^{(k)}(x)=0.
$$


::: pf-proof

Expand the polynomial in step [](#s1-2){.pf-ref} into finitely many monomials $c_mx^{-m}$. Each monomial times $e^{-1/x}$ tends to zero by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is $C^\infty$ on $\RR$, and
$$
f^{(k)}(0)=0
\qquad(k\geq0).
$$


::: pf-proof

On $(-\infty,0)$ the function is identically zero and on $(0,\infty)$ it is smooth. Induct on $k$. Suppose $f^{(k)}$ extends continuously to $0$ with value $0$. Its derivative at zero is
$$
\lim_{h\to0}\frac{f^{(k)}(h)-f^{(k)}(0)}h.
$$
For $h<0$ the quotient is zero. For $h>0$, step [](#s1-2){.pf-ref} expresses it as a finite sum of terms $h^{-m}e^{-1/h}$, which tend to zero by step [](#s1-1){.pf-ref}. Thus the derivative exists and equals zero; step [](#s1-3){.pf-ref} gives continuity of the next derivative. This proves the assertion for all $k$.

:::

:::

::: {.pf-step #s1-5}

Define
$$
\psi(x)=f(1-\norm{x}^2),
\qquad x\in\RR^n.
$$
Then $\psi\in C^\infty(\RR^n)$, $\psi\geq0$, and
$$
\psi(x)=0\quad\text{for }\norm{x}\geq1,
$$
while $\psi(x)>0$ for $\norm{x}<1$.


::: pf-proof

The map $x\mapsto1-\norm{x}^2$ is smooth, and step [](#s1-4){.pf-ref} says $f$ is smooth, so their composition is smooth. The defining formula for $f$ gives nonnegativity and the support statement immediately.

:::

:::

::: pf-step

The number
$$
C=\int_{\RR^n}\psi(x)\,dx
$$
is finite and strictly positive.


::: pf-proof

The function $\psi$ is continuous and supported in the compact unit ball, hence integrable with finite integral. It is nonnegative everywhere and strictly positive on the open unit ball, so its integral is positive.

:::

:::

::: {.pf-step #s1-7}

Set
$$
\varphi(x)=C^{-1}\psi(x).
$$
Then
$$
\varphi\in C^\infty(\RR^n),\qquad
\varphi\geq0,\qquad
\varphi(x)=0\text{ if }\norm{x}>1,
$$
and
$$
\int_{\RR^n}\varphi(x)\,dx=1.
$$


::: pf-proof

All regularity, positivity, and support properties follow from step [](#s1-5){.pf-ref} because $C>0$. By the definition of $C$,
$$
\int\varphi=C^{-1}\int\psi=1.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-7){.pf-ref} constructs the function required in part (b).

:::

:::

:::
