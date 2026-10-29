---
schema: qual/card@1
id: P-NORI-GT-3-03
kind: problem
title: Towers of quadratic extensions of $\FF_p$ by iterated square roots
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.3 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let p be a prime which is  1 mod $2 ^ { k }$ , but not congruent to 1 modulo a higher power of 2. Assume $k \geq 2$ . Assume that $u _ { 0 } \in \FF _ { p }$ is not a square.
Construct a sequence of pairs $\left( E _ { n } , u _ { n } \right)$ where $E _ { n }$ is a field and $u _ { n } \in E _ { n }$ as follows.
Define $( E _ { 0 } , u _ { 0 } ) = ( \FF _ { p } , u _ { 0 } )$

Assume that $( E _ { n } , u _ { n } )$ has been defined.
Let $E _ { n + 1 }$ be a field extension of $E _ { n }$ obtaing by adjoining a square-root $u _ { n + 1 }$ of $u _ { n } \in E _ { n }$

Show that $\mathrm { d e g } ( E _ { n } / E _ { n - 1 } ) = 2$ for all $n > 0$
:::

::: {.solution}

Write
$$
p-1=2^k m
$$
with $m$ odd; this is exactly the hypothesis that $p\equiv1\pmod{2^k}$ but not modulo a higher power of $2$.

::: pf

::: {.pf-step #p1-s1-1}

For every $n\geq0$, one has
$$
u_n^{2^n}=u_0.
$$


::: pf-proof

The defining relations are $u_{j+1}^2=u_j$. Iterating them gives
$$
u_n^{2^n}=u_{n-1}^{2^{n-1}}=\cdots=u_0.
$$

:::

:::

::: {.pf-step #p1-s1-2}

If all extensions through $E_n$ have degree $2$, then
$$
E_n\cong\FF_{p^{2^n}}.
$$


::: pf-proof

Starting with $E_0=\FF_p$, the tower law gives
$$
[E_n:\FF_p]=2^n.
$$
Every finite extension of $\FF_p$ of degree $2^n$ is isomorphic to the unique finite field $\FF_{p^{2^n}}$.

:::

:::

::: {.pf-step #p1-s1-3}

In a finite field $K$ of odd order $Q$, an element $a\in K^\times$ is a square if and only if
$$
a^{(Q-1)/2}=1.
$$


::: pf-proof

The cyclic group $K^\times$ has order $Q-1$. Its subgroup of squares has index $2$ and therefore order $(Q-1)/2$. The displayed equation cuts out exactly this subgroup.

:::

:::

::: {.pf-step #p1-s1-4}

The initial element $u_0$ satisfies
$$
u_0^{(p-1)/2}=-1.
$$


::: pf-proof

By hypothesis $u_0$ is not a square in $\FF_p$. Euler's criterion, equivalently step [](#p1-s1-3){.pf-ref} with $Q=p$, gives the value $-1$ rather than $1$.

:::

:::

::: {.pf-step #p1-s1-5}

The first extension has degree
$$
[E_1:E_0]=2.
$$


::: pf-proof

The polynomial $X^2-u_0$ has no root in $E_0$ because $u_0$ is not a square there. Hence it is irreducible of degree $2$, and adjoining $u_1$ gives a quadratic extension.

:::

:::

::: {.pf-step #p1-s1-6}

Assume inductively that
$$
[E_j:E_{j-1}]=2
$$
for $1\leq j\leq n$. Then $E_n=\FF_{p^{2^n}}$ and
$$
u_n^{(p^{2^n}-1)/2}=-1.
$$


::: pf-proof

The field identification is step [](#p1-s1-2){.pf-ref}. Factor
$$
p^{2^n}-1=(p-1)(1+p+\cdots+p^{2^n-1}).
$$
By step [](#p1-s1-1){.pf-ref},
$$
u_n^{(p^{2^n}-1)/2}
=\left(u_n^{2^n}\right)^A
=u_0^A,
$$
provided
$$
A=\frac{p^{2^n}-1}{2^{n+1}}
$$
is an integer. Since $v_2(p-1)=k\ge2$, the lifting-the-exponent formula for odd $p$ gives
$$
v_2(p^{2^n}-1)=v_2(p-1)+v_2(p+1)+n-1=k+n,
$$
because $p\equiv1\pmod4$ implies $v_2(p+1)=1$. Thus $A$ is an integer. Moreover
$$
A=\frac{p-1}{2}\cdot
\frac{1+p+\cdots+p^{2^n-1}}{2^n}.
$$
The second factor is odd: each $p^j\equiv1\pmod{2^k}$, and the standard valuation just computed shows the sum has exactly $2$-adic valuation $n$. Hence $A$ is an odd multiple of $(p-1)/2$. Step [](#p1-s1-4){.pf-ref} therefore gives
$$
u_0^A
=\left(u_0^{(p-1)/2}\right)^{\text{odd}}
=-1.
$$

:::

:::

::: {.pf-step #p1-s1-7}

Hence $u_n$ is not a square in $E_n$.


::: pf-proof

By step [](#p1-s1-6){.pf-ref},
$$
u_n^{(|E_n|-1)/2}=-1.
$$
The square criterion in step [](#p1-s1-3){.pf-ref} therefore says that $u_n$ is a nonsquare.

:::

:::

::: {.pf-step #p1-s1-8}

Consequently
$$
[E_{n+1}:E_n]=2.
$$


::: pf-proof

Since $u_n$ is not a square in $E_n$, the polynomial $X^2-u_n$ is irreducible over $E_n$. By construction $E_{n+1}=E_n(u_{n+1})$ with $u_{n+1}^2=u_n$, so the extension degree is $2$.

:::

:::

::: {.pf-step #p1-s1-9}

By induction,
$$
\boxed{[E_n:E_{n-1}]=2\quad\text{for every }n>0.}
$$


::: pf-proof

Step [](#p1-s1-5){.pf-ref} is the base case. Steps [](#p1-s1-6){.pf-ref} through [](#p1-s1-8){.pf-ref} show that if all stages through $n$ are quadratic, then the next stage is quadratic. Induction proves the assertion for every $n$.

:::

:::

::: pf-qed

Step [](#p1-s1-9){.pf-ref} is the required conclusion.

:::

:::

Write
$$
p-1=2^k m,
\qquad m\text{ odd},
$$
which is possible by the hypothesis that $2^k$ is the exact power of $2$ dividing $p-1$.

::: pf

::: {.pf-step #p2-s1-1}

For every $n\geq0$ one has
$$
u_n^{2^n}=u_0.
$$


::: pf-proof

By construction $u_{j+1}^2=u_j$. Iterating gives
$$
u_n^{2^n}=u_{n-1}^{2^{n-1}}=\cdots=u_0.
$$

:::

:::

::: {.pf-step #p2-s1-2}

It suffices to prove inductively that
$$
E_n=\FF_{p^{2^n}}
$$
and that $u_n$ is not a square in $E_n$.


::: pf-proof

If $u_n$ is not a square in $E_n$, then $X^2-u_n$ is irreducible over $E_n$, so adjoining its root $u_{n+1}$ gives
$$
[E_{n+1}:E_n]=2.
$$
Since a degree-two extension of the finite field $\FF_{p^{2^n}}$ is the unique field $\FF_{p^{2^{n+1}}}$, the asserted field identification propagates as well.

:::

:::

::: {.pf-step #p2-s1-3}

The assertion holds at $n=0$: $E_0=\FF_p$ and $u_0$ is not a square in $E_0$.


::: pf-proof

This is exactly the initial condition in the problem.

:::

:::

::: {.pf-step #p2-s1-4}

Assume
$$
E_n=\FF_{p^{2^n}}
$$
and $u_n$ is not a square in $E_n$. Then
$$
[E_{n+1}:E_n]=2
$$
and
$$
E_{n+1}=\FF_{p^{2^{n+1}}}.
$$


::: pf-proof

The polynomial $X^2-u_n$ has no root in $E_n$ by the nonsquare hypothesis, hence is irreducible. Thus adjoining $u_{n+1}$ gives degree two. The resulting field has
$$
|E_n|^2=p^{2^{n+1}}
$$
elements, so it is the finite field $\FF_{p^{2^{n+1}}}$.

:::

:::

::: {.pf-step #p2-s1-5}

In a finite field $K=\FF_Q$ of odd order, an element $a\in K^\times$ is a square if and only if
$$
a^{(Q-1)/2}=1.
$$


::: pf-proof

The cyclic group $K^\times$ has order $Q-1$. If $g$ is a generator and $a=g^r$, then $a$ is a square exactly when $r$ is even. Also
$$
a^{(Q-1)/2}=(-1)^r,
$$
so this equals $1$ exactly when $r$ is even.

:::

:::

::: {.pf-step #p2-s1-6}

Since $u_0$ is a nonsquare in $\FF_p$, one has
$$
u_0^{(p-1)/2}=-1.
$$


::: pf-proof

Apply step [](#p2-s1-5){.pf-ref} with $Q=p$. The value has square $1$ by Fermat's theorem, and it is not $1$ because $u_0$ is a nonsquare; in odd characteristic it must therefore be $-1$.

:::

:::

::: {.pf-step #p2-s1-7}

Let
$$
Q_{n+1}=p^{2^{n+1}}=|E_{n+1}|.
$$
Then
$$
u_{n+1}^{(Q_{n+1}-1)/2}
=u_0^{(Q_{n+1}-1)/2^{n+2}}.
$$


::: pf-proof

By step [](#p2-s1-1){.pf-ref},
$$
u_{n+1}^{2^{n+1}}=u_0.
$$
The exponent $(Q_{n+1}-1)/2$ is divisible by $2^{n+1}$ because $p\equiv1\pmod{2^k}$ with $k\ge2$, and the factorization in step [](#p2-s1-8){.pf-ref} below makes the divisibility explicit. Hence
$$
u_{n+1}^{(Q_{n+1}-1)/2}
=\left(u_{n+1}^{2^{n+1}}\right)^{(Q_{n+1}-1)/2^{n+2}}
=u_0^{(Q_{n+1}-1)/2^{n+2}}.
$$

:::

:::

::: {.pf-step #p2-s1-8}

The integer
$$
\frac{Q_{n+1}-1}{2^{n+2}}
$$
is an odd multiple of $(p-1)/2$.


::: pf-proof

Factor
$$
p^{2^{n+1}}-1
=(p-1)(p+1)(p^2+1)\cdots(p^{2^n}+1).
$$
Because $p\equiv1\pmod4$ (as $k\ge2$), each factor
$$
p^{2^j}+1
$$
is congruent to $2$ modulo $4$ and therefore has exact $2$-adic valuation $1$. Thus
$$
v_2(Q_{n+1}-1)=v_2(p-1)+(n+1)=k+n+1.
$$
After dividing by $2^{n+2}$, the quotient has $2$-adic valuation $k-1$, exactly the same as $(p-1)/2$. Hence their quotient is odd. Equivalently,
$$
\frac{Q_{n+1}-1}{2^{n+2}}
=\frac{p-1}{2}\cdot M
$$
for an odd integer $M$.

:::

:::

::: {.pf-step #p2-s1-9}

Therefore
$$
u_{n+1}^{(Q_{n+1}-1)/2}=-1.
$$


::: pf-proof

By steps [](#p2-s1-7){.pf-ref} through [](#p2-s1-8){.pf-ref},
$$
u_{n+1}^{(Q_{n+1}-1)/2}
=\left(u_0^{(p-1)/2}\right)^M
$$
with $M$ odd. Step [](#p2-s1-6){.pf-ref} gives $u_0^{(p-1)/2}=-1$, so the result is $(-1)^M=-1$.

:::

:::

::: {.pf-step #p2-s1-10}

Hence $u_{n+1}$ is not a square in $E_{n+1}$.


::: pf-proof

Apply the square criterion in step [](#p2-s1-5){.pf-ref} to $K=E_{n+1}$, whose order is $Q_{n+1}$ by step [](#p2-s1-4){.pf-ref}. Step [](#p2-s1-9){.pf-ref} gives the value $-1$, not $1$.

:::

:::

::: {.pf-step #p2-s1-11}

By induction, $u_n$ is a nonsquare in $E_n$ for every $n\ge0$, and therefore
$$
\boxed{[E_n:E_{n-1}]=2\quad(n>0).}
$$


::: pf-proof

Step [](#p2-s1-3){.pf-ref} is the base case. Steps [](#p2-s1-4){.pf-ref} and [](#p2-s1-10){.pf-ref} propagate both the finite-field identification and the nonsquare property. Then step [](#p2-s1-2){.pf-ref} gives the desired degree at every stage.

:::

:::

::: pf-qed

Step [](#p2-s1-11){.pf-ref} is exactly the assertion of the problem.

:::

:::

:::
