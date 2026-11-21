---
schema: qual/card@1
id: P-EMCA10
kind: problem
title: Rouché's theorem and local bijectivity where the derivative is nonzero
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (10) of Arango-Piñeros, Some quals problems; merged the duplicate P-ZLDP7, whose statement of Rouché's theorem compared the wrong pair of functions."
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and Rouché used for the bijection as the exercise directs. The prose proved injectivity only from the integral of f' (and recorded "the same number of zeros, namely one" without deriving surjectivity), whereas the exercise asks to use Rouché's theorem for the bijection; the card now applies Rouché to f and the constant -w on |z| = r, using the lower bound |f(z)| >= (|a|/2) r, to conclude that every w with |w| < (|a|/2) r has exactly one preimage in the disc: that is simultaneously injectivity and surjectivity onto a disc. The derivative-integral argument is kept as an independent check of injectivity. Statement (a) is the standard form of Rouché's theorem, stated as asked. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
(a) State Rouche's theorem.

(b) Let $f$ be analytic in a neighborhood of $0$, and satisfying $f'(0) \neq 0$.
Use Rouche's theorem to show that there exists a neighborhood $U$ of $0$ such that $f$ is a bijection in $U$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #rouche}
Rouché's theorem. Let $C$ be a positively oriented simple closed contour and let $F,G$ be holomorphic on an open set containing $C$ and its interior. If $\abs{G(z)}<\abs{F(z)}$ for every $z\in C$, then $F$ and $F+G$ have the same number of zeros inside $C$, counted with multiplicity.

::: pf-proof
This is the statement asked for in part (a). It is a theorem of the course, proved from the argument principle applied to $F+tG$ for $t\in[0,1]$, the count being a continuous integer-valued function of $t$.
:::

:::

::: {.pf-step #normalise}
Replacing $f$ by $f-f(0)$, one may assume $f(0)=0$, and still $f'(0)=a\ne0$.

::: pf-proof
$f-f(0)$ is holomorphic near $0$, its derivative is $f'$, and $f$ is injective near $0$ exactly when $f-f(0)$ is.
:::

:::

::: {.pf-step #expansion}
Near $0$, $f(z)=az+z\varepsilon(z)$ with $a=f'(0)\ne0$ and $\varepsilon(z)\to0$ as $z\to0$.

::: pf-proof
$f$ is holomorphic near $0$ with $f(0)=0$, so $f(z)/z$ extends holomorphically to $0$ with value $f'(0)=a$; putting $\varepsilon(z)=f(z)/z-a$ for $z\ne0$ gives the identity and $\varepsilon(z)\to0$.
:::

:::

::: {.pf-step #radius}
There is $r>0$ such that $f$ is holomorphic on a neighbourhood of $\overline{B(0,r)}$ and $\abs{\varepsilon(z)}<\frac{\abs a}{2}$ for $\abs z\le r$; then $\abs{f(z)}\ge\frac{\abs a}{2}r$ on $\abs z=r$.

::: pf-proof
Take $r$ with $\overline{B(0,r)}$ inside the domain of $f$ and small enough that $\abs{\varepsilon(z)}<\abs a/2$ there, possible by step [](#expansion){.pf-ref}. On $\abs z=r$,
$$
\abs{f(z)}=\abs{az+z\varepsilon(z)}=\abs z\abs{a+\varepsilon(z)}\ge r\left(\abs a-\abs{\varepsilon(z)}\right)>\frac{\abs a}{2}r.
$$
:::

:::

::: {.pf-step #bijection}
$f$ maps $B(0,r)$ bijectively onto the disc $B\bigl(0,\frac{\abs a}{2}r\bigr)$.

::: pf-proof
Let $\abs w<\frac{\abs a}{2}r$. On the circle $C=\{\abs z=r\}$ we have $\abs{-w}=\abs w<\abs{f(z)}$ by step [](#radius){.pf-ref}, so Rouché's theorem applied to $F=f$ and $G=-w$ (a constant) gives that $f$ and $f-w$ have the same number of zeros in $B(0,r)$. Now $f$ has exactly one zero there, counting multiplicity, because $\abs{f(z)-az}=\abs{z\varepsilon(z)}<\abs a r=\abs{az}$ on $\abs z=r$ and $az$ has the single simple zero $0$; so $f-w$ has exactly one zero in $B(0,r)$. Hence every $w$ with $\abs w<\frac{\abs a}{2}r$ has exactly one preimage in $B(0,r)$, which is bijectivity of $f:B(0,r)\to B(0,\frac{\abs a}{2}r)$.
:::

:::

::: {.pf-step #injective}
$f$ is injective on $U=B(0,r)$.

::: pf-proof
This is contained in step [](#bijection){.pf-ref}. As an independent check, shrinking $r$ if necessary so that $\abs{f'(z)-a}<\frac{\abs a}{2}$ on $B(0,r)$, for distinct $z,w$ the segment joining them lies in the disk and
$$
\frac{f(z)-f(w)}{z-w}=\int_0^1f'\bigl(w+t(z-w)\bigr)dt,
$$
whose distance from $a$ is at most $\frac{\abs a}{2}$, so the quotient is nonzero and $f(z)\ne f(w)$.
:::

:::

::: {.pf-step}
There is a neighbourhood $U$ of $0$ on which $f$ is a bijection.

::: pf-proof
Step [](#bijection){.pf-ref} gives the bijection of $B(0,r)$ onto an open disc, which answers (b) with $U=B(0,r)$.
:::

:::

:::
:::
