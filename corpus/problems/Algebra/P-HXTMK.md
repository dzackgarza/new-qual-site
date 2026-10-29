---
schema: qual/card@1
id: P-HXTMK
kind: problem
title: Rational canonical forms from specified minimal polynomials in dimensions $6$ and $10$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
  - Structure Theorem
relations: []
review: draft
---

::: {.problem}
(a) Let $A\in M_6(\QQ)$ have minimal polynomial
$$
m_A=(x-1)(x^2+1)^2.
$$
Determine all possible rational canonical forms of $A$.

(b) Let $B\in M_{10}(\QQ)$ have minimal polynomial
$$
m_B=(x^2+1)^2(x^3+1).
$$
Determine all possible rational canonical forms of $B$.
:::

::: {.solution}
Write $C(g)$ for the companion matrix of a monic polynomial $g$.
Recall that the invariant factors $e_1\mid e_2\mid\cdots\mid e_t$ of a matrix $M$ satisfy $\chi_M=\prod_i e_i$ and $m_M=e_t$, and that $M$ has rational canonical form $C(e_1)\oplus\cdots\oplus C(e_t)$.
The elementary divisors are the prime-power factors of the $e_i$; their irreducible factors are those of $m_M$, the largest power of each irreducible factor is its power in $m_M$, and the invariant factors are recovered by aligning the powers of each irreducible factor from the right.
Over $\QQ$ the polynomials $x-1$, $x+1$, $x^2+1$ and $x^2-x+1$ are irreducible, and $x^3+1=(x+1)(x^2-x+1)$.

::: pf

::: pf-step
(a) The only rational canonical form is $\boxed{C(x-1)\oplus C\bigl((x-1)(x^2+1)^2\bigr)}$.

::: pf-proof
Write $a=x-1$ and $b=x^2+1$.
The elementary divisors include $a$ and $b^2$, of total degree $1+4=5$, and every further elementary divisor is one of $a$, $b$, $b^2$.
The remaining degree is $1$, so the only further elementary divisor is $a$.
Thus the elementary divisors are $a,a,b^2$, and the invariant factors are $e_1=a$ and $e_2=ab^2$.
:::

:::

::: pf-step
(b) The rational canonical forms are exactly
$$
\boxed{
\begin{gathered}
C(x^3+1)\oplus C(m_B),\qquad
C\bigl((x^2+1)(x+1)\bigr)\oplus C(m_B),\\
C(x+1)\oplus C(x+1)\oplus C(x+1)\oplus C(m_B).
\end{gathered}}
$$

::: pf-proof
Write $b=x^2+1$, $c=x+1$ and $r=x^2-x+1$, so $m_B=b^2cr$ has degree $7$.
The elementary divisors include $b^2$, $c$ and $r$, and every further elementary divisor is one of $b$, $b^2$, $c$, $r$, of degrees $2$, $4$, $1$, $2$.
The further ones have total degree $10-7=3$, so they are $\{c,r\}$, $\{c,b\}$ or $\{c,c,c\}$.

- Further divisors $c,r$: the elementary divisors are $b^2,c,c,r,r$, so $e_1=cr=x^3+1$ and $e_2=b^2cr=m_B$.

- Further divisors $c,b$: the elementary divisors are $b,b^2,c,c,r$, so $e_1=bc=(x^2+1)(x+1)$ and $e_2=m_B$.

- Further divisors $c,c,c$: the elementary divisors are $b^2,c,c,c,c,r$, so $e_1=e_2=e_3=c$ and $e_4=m_B$.
:::

:::

:::

:::
