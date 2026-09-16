---
schema: qual/card@1
id: P-IXED6
kind: problem
title: Gcd ideals and compatible congruences in a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked July 2013 Rings 4 and the definition of ideal join in Rings 1 on PDF page 7; no coprimality hypothesis is imposed."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the least-ideal property, both divisibility conditions defining the gcd, and the signs in the explicit simultaneous-congruence solution."
---

::: {.problem}
Suppose that $R$ is a principal-ideal domain and $a, b, c, d \in R$ with $a, b \neq 0$.
For ideals $J,L$ of $R$, let $J\vee L$ denote the least ideal
containing both $J$ and $L$.

a. Find a generator for the ideal $(a) \vee (b)$.

b. For $u, v \in R$ and $I$ any ideal of $R$, write $$u \equiv v \bmod I$$ for $$u - v \in I.$$ Show that

There is $x \in R$ with $x \equiv c \bmod (a)$ and $x \equiv d \bmod (b)$

just in case $$c \equiv d \bmod (a) \vee (b).$$
:::

::: {.solution}
<1>1. The join is
$$
(a)\vee(b)=(a)+(b)=\{ua+vb:u,v\in R\}.
$$

::: {.proof}
The displayed set contains zero, is closed under subtraction,
and is closed under multiplication by any $r\in R$:
$r(ua+vb)=(ru)a+(rv)b$. It is therefore an ideal.
It contains both $(a)$ and $(b)$. Any ideal containing these
two ideals contains every sum $ua+vb$, so it contains the
displayed ideal. This proves the least-ideal property and
hence the asserted identification with the join.
:::

<1>2. A greatest common divisor $g$ of $a$ and $b$ generates
this ideal; in particular, $g=ra+sb$ for suitable $r,s\in R$.

::: {.proof}
Because $R$ is a PID, step <1>1 gives $(a)+(b)=(g)$ for
some $g\in R$. This generator is nonzero because the ideal
contains $a\ne0$. Membership of $a,b$ in $(g)$ says that
$g$ divides both $a$ and $b$. Membership of $g$ in the sum
gives $g=ra+sb$.

If $h$ divides both $a$ and $b$, then it divides every
linear combination of them, and in particular divides $g$.
Thus $g$ is a greatest common divisor in the divisibility
sense. Conversely, any other greatest common divisor $g'$
divides $g$ and is divisible by $g$, so $(g')=(g)$.
Hence any choice of gcd is a generator of the join.
:::

<1>3. The simultaneous congruences are solvable exactly when
$c-d\in(a)\vee(b)$.

::: {.proof}
If $x$ satisfies the congruences, then
$c-x\in(a)$ and $x-d\in(b)$. Adding gives
$c-d\in(a)+(b)$, which is the required compatibility.

Conversely, if $c-d\in(a)+(b)$, choose $u,v\in R$ with
$c-d=ua+vb$. Set
$$
x=c-ua=d+vb.
$$
Then $x-c=-ua\in(a)$ and $x-d=vb\in(b)$, proving both
congruences. In terms of step <1>2, write $c-d=kg$ and
$g=ra+sb$; the explicit solution becomes
$x=c-kra=d+ksb$. No assumption that $a$ and $b$ are
coprime was used.
:::
:::
