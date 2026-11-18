---
schema: qual/card@1
id: E-SS10.EX-8
kind: problem
title: Parametrization of primitive Pythagorean triples
classification:
  areas:
  - complex-analysis
  topics:
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so; the printed hint is followed in (b). Each step re-read: two odd
    legs give a sum 2 mod 4, which is not a square, and two even ones contradict coprimality; with a
    odd and b even, c is odd and coprime to a, because a common divisor divides c^2 - a^2 = b^2 and
    hence b; u = (c-a)/2 and v = (c+a)/2 are positive coprime integers with uv = (b/2)^2; a product
    of coprime integers that is a square has square factors, by comparing prime exponents; and the
    parametrisation follows. (c) is the direct verification. Not claimed: that distinct pairs (m,n)
    give distinct triples, or that the parametrisation is injective.
---

::: {.exercise}
Consider Pythagorean triples $(a, b, c)$ with $a^2 + b^2 = c^2$, and with $a, b, c \in \ZZ$. Suppose moreover that $a$ and $b$ have no common factors.

(a) Show that either $a$ or $b$ must be odd, and the other even.

(b) Show in this case (assuming $a$ is odd and $b$ even) that there are integers $m, n$ so that $a = m^2 - n^2$, $b = 2mn$, and $c = m^2 + n^2$. [Hint: Note that $b^2 = (c - a)(c + a)$, and prove that $(c - a)/2$ and $(c + a)/2$ are relatively prime integers.]

(c) Conversely, show that whenever $c$ is a sum of two squares, then there exist integers $a$ and $b$ such that $a^2 + b^2 = c^2$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 10 Exercise 8, and follows the printed hint for part (b).

::: pf

::: {.pf-step #parta}
If $\gcd(a,b)=1$ and $a^{2}+b^{2}=c^{2}$ then exactly one of $a,b$ is even.

:::: pf-proof

::: {.pf-step #notbothodd}
$a$ and $b$ are not both odd.

::: pf-proof
Then $a^{2}+b^{2}\equiv1+1\equiv2\pmod 4$, but a square is $0$ or $1\pmod4$, so $a^{2}+b^{2}$ is not a square.
:::

:::

::: {.pf-step #notbotheven}
$a$ and $b$ are not both even.

::: pf-proof
That would give the common divisor $2$, contradicting $\gcd(a,b)=1$.
:::

:::

::: {.pf-step}
Exactly one of $a,b$ is even.

::: pf-proof
Steps [](#notbothodd){.pf-ref} and [](#notbotheven){.pf-ref} exclude both odd and both even, and every integer is odd or even.
:::

:::

:::

:::

::: {.pf-step #partb}
If $a$ is odd and $b$ even, then there are integers $m,n$ with $a=m^{2}-n^{2}$, $b=2mn$ and $c=m^{2}+n^{2}$.

:::: pf-proof

::: {.pf-step #coprimeac}
$c$ is odd and $\gcd(a,c)=1$.

::: pf-proof
$c^{2}=a^{2}+b^{2}\equiv1+0\equiv1\pmod4$ with $b$ even, so $c$ is odd. A common divisor $d$ of $a$ and $c$ divides $c^{2}-a^{2}=b^{2}$, hence divides $b$; since $\gcd(a,b)=1$, $d=1$.
:::

:::

::: {.pf-step #uv}
With $u=(c-a)/2$ and $v=(c+a)/2$: $u,v$ are positive coprime integers and $uv=(b/2)^{2}$.

::: pf-proof
$c$ and $a$ are both odd, so $c\pm a$ is even and $u,v$ are integers; $c>a\ge0$ because $b\ne0$, so both are positive. $uv=(c^{2}-a^{2})/4=b^{2}/4=(b/2)^{2}$, and $b/2$ is an integer. A common divisor $d$ of $u$ and $v$ divides $u+v=c$ and $v-u=a$, so $d=1$ by step [](#coprimeac){.pf-ref}.
:::

:::

::: {.pf-step #squares}
Coprime $u,v$ with $uv$ a square are themselves squares.

::: pf-proof
In the prime factorisation of the square $uv$, every prime occurs to an even exponent; a prime dividing $u$ does not divide $v$, so its exponent in $u$ equals its exponent in $uv$ and is even, and likewise for $v$. Hence $u=n^{2}$ and $v=m^{2}$ for positive integers $n,m$.
:::

:::

::: {.pf-step #conclusion}
$a=m^{2}-n^{2}$, $b=2mn$, $c=m^{2}+n^{2}$.

::: pf-proof
With $u=n^{2}$ and $v=m^{2}$ from step [](#squares){.pf-ref}: $a=v-u=m^{2}-n^{2}$ and $c=u+v=m^{2}+n^{2}$ by the definitions of $u$ and $v$; and $b^{2}=4uv=4m^{2}n^{2}$ with $b>0$ gives $b=2mn$.
:::

:::

:::

:::

::: {.pf-step #partc}
If $c=m^{2}+n^{2}$ is a sum of two squares then $c$ is the hypotenuse of an integral right triangle.

::: pf-proof
Put $a=m^{2}-n^{2}$ and $b=2mn$. Then
$$
a^{2}+b^{2}=(m^{2}-n^{2})^{2}+4m^{2}n^{2}=m^{4}+2m^{2}n^{2}+n^{4}=(m^{2}+n^{2})^{2}=c^{2},
$$
so $(a,b,c)$ is a Pythagorean triple with hypotenuse $c$.
:::

:::

::: {.pf-step}
Parts (a), (b) and (c) hold.

::: pf-proof
Steps [](#parta){.pf-ref}, [](#partb){.pf-ref} and [](#partc){.pf-ref} are the three parts:
$$
\boxed{\text{a primitive triple has one even leg};\quad a=m^{2}-n^{2},\,b=2mn,\,c=m^{2}+n^{2};\quad \text{every sum of two squares is a hypotenuse}.}
$$
Part (b) is stated for $a$ odd; the case $a$ even is the same argument with $a$ and $b$ interchanged.
:::

:::

:::
:::
