---
schema: qual/card@1
id: P-TRIV-DE21
kind: problem
title: Perturbative ground-state energy of the quartic anharmonic oscillator
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed extraction residue in the statement of Differential Equations Problem 21 against pages 23-24 of the source PDF.
---

::: {.problem}
Consider Schrodinger equation for a quantum harmonic oscillator with small quartic perturbation
$$
\left(-\frac{1}{2}\frac{d^2}{dx^2} + \frac{x^2}{2} + \frac{g x^4}{4}\right)\psi(x) = E_0(g)\psi(x)
\tag{30}
$$
and make the ansatz
$$
\psi(x) = e^{-x^2/2} \sum_{n=0}^\infty \left(\frac{g}{4}\right)^n B_n(x) \qquad \text{with} \quad B_0(x) = 1
\tag{31}
$$
$$
E_0(g) = \sum_{k=0}^\infty a_k \left(\frac{g}{4}\right)^k.
\tag{32}
$$
We already know that $a_0 = \frac{1}{2}$ from the unperturbed oscillator.
We want to find the first two corrections $a_1$ and $a_2$.

(a) Find a recurrence relation for $B_k(x)$ and $a_k$

(b) Solve the relation by assuming $B_i(x) = \sum_{j=1}^{2i} x^{2j} (-1)^i B_{i,j}$.

(c) Considering different powers of $x$, find the following relations
$$
a_n = (-1)^{n+1} B_{n,1}
\tag{33}
$$
$$
2j B_{n,j} = (j+1)(2j+1) B_{n,j+1} + B_{n-1,j-2} - \sum_{k=1}^{n-1} B_{n-k,1} B_{k,j}
\tag{34}
$$

(d) Find $a_1$ and $a_2$.
You can check that your result agrees with the usual perturbation theory.
:::

::: {.solution}

Write $\lambda=g/4$ and
$$
S(x,\lambda)=\sum_{n=0}^{\infty}\lambda^nB_n(x),
\qquad
E_0(g)=\sum_{n=0}^{\infty}a_n\lambda^n,
\qquad B_0=1.
$$

::: pf

::: {.pf-step #s1-1}

After substituting $\psi=e^{-x^2/2}S$, the Schrodinger equation becomes
$$
-\frac12S''+xS'+\frac12S+\lambda x^4S=E_0S.
$$


::: pf-proof

Differentiation gives
$$
\psi'=e^{-x^2/2}(S'-xS)
$$
and
$$
\psi''=e^{-x^2/2}\bigl(S''-2xS'+(x^2-1)S\bigr).
$$
Substitution into the differential equation cancels the $x^2S/2$ terms. Since $gx^4/4=\lambda x^4$, the displayed equation follows.

:::

:::

::: {.pf-step #s1-2}

For every $n\geq1$,
$$
\boxed{
-\frac12B_n''+xB_n'
=\sum_{k=1}^{n}a_kB_{n-k}-x^4B_{n-1}.}
$$


::: pf-proof

The coefficient of $\lambda^n$ in step [](#s1-1){.pf-ref} is
$$
-\frac12B_n''+xB_n'+\frac12B_n+x^4B_{n-1}
=\sum_{k=0}^{n}a_kB_{n-k}.
$$
Since $a_0=1/2$, the terms $B_n/2$ cancel, giving the recurrence.

:::

:::

::: {.pf-step #s1-3}

Under
$$
B_n(x)=(-1)^n\sum_{j=1}^{2n}B_{n,j}x^{2j},
$$
the constant coefficient in step [](#s1-2){.pf-ref} gives
$$
\boxed{a_n=(-1)^{n+1}B_{n,1}}.
$$


::: pf-proof

The only constant term on the left side of step [](#s1-2){.pf-ref} is produced by $-B_n''/2$ from the $x^2$ term of $B_n$, and it equals $(-1)^{n+1}B_{n,1}$. On the right, the only constant term is $a_nB_0=a_n$, because every $B_k$ with $k\geq1$ has zero constant term.

:::

:::

::: {.pf-step #s1-4}

For $j\geq1$, comparison of the coefficient of $x^{2j}$ gives
$$
\boxed{
2jB_{n,j}=(j+1)(2j+1)B_{n,j+1}+B_{n-1,j-2}
-\sum_{k=1}^{n-1}B_{n-k,1}B_{k,j},}
$$
where coefficients outside their natural index ranges are zero.


::: pf-proof

In step [](#s1-2){.pf-ref}, the coefficient of $x^{2j}$ on the left is
$$
(-1)^n\left(2jB_{n,j}-(j+1)(2j+1)B_{n,j+1}\right).
$$
The term $-x^4B_{n-1}$ contributes $(-1)^nB_{n-1,j-2}$. For $1\leq k\leq n-1$, the product $a_kB_{n-k}$ contributes
$$
(-1)^{k+1}B_{k,1}\,(-1)^{n-k}B_{n-k,j}
=(-1)^{n+1}B_{k,1}B_{n-k,j}.
$$
Divide by $(-1)^n$ and relabel $k\leftrightarrow n-k$ in the finite sum to obtain the displayed recurrence.

:::

:::

::: {.pf-step #s1-5}

For $n=1$,
$$
B_{1,2}=\frac14,
\qquad
B_{1,1}=\frac34,
\qquad
\boxed{a_1=\frac34}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} with $(n,j)=(1,2)$ gives
$$
4B_{1,2}=B_{0,0}=1,
$$
where $B_{0,0}=1$ records $B_0=1$. Thus $B_{1,2}=1/4$. Step [](#s1-4){.pf-ref} with $(n,j)=(1,1)$ then gives
$$
2B_{1,1}=6B_{1,2}=\frac32,
$$
so $B_{1,1}=3/4$. Step [](#s1-3){.pf-ref} gives $a_1=3/4$.

:::

:::

::: {.pf-step #s1-6}

For $n=2$,
$$
B_{2,1}=\frac{21}{8},
\qquad
\boxed{a_2=-\frac{21}{8}}.
$$


::: pf-proof

At order $\lambda^2$, step [](#s1-2){.pf-ref} gives
$$
-\frac12B_2''+xB_2'=a_1B_1+a_2-x^4B_1.
$$
Using step [](#s1-4){.pf-ref} from the highest nonzero coefficient downward gives
$$
B_{2,4}=\frac1{32},\qquad
B_{2,3}=\frac{13}{48},\qquad
B_{2,2}=\frac{31}{32}.
$$
Indeed, these are respectively the $j=4,3,2$ instances of the recurrence, with $B_{1,2}=1/4$ and $B_{1,1}=3/4$. For $j=1$, step [](#s1-4){.pf-ref} gives
$$
2B_{2,1}=6B_{2,2}-B_{1,1}^2
=6\frac{31}{32}-\frac9{16}
=\frac{21}{4}.
$$
Thus $B_{2,1}=21/8$, and step [](#s1-3){.pf-ref} gives $a_2=-21/8$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} establish the requested recurrences, and steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} give the first two energy corrections.

:::

:::

:::
