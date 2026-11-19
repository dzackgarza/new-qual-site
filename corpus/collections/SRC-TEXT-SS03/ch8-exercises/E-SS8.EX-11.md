---
schema: qual/card@1
id: E-SS8.EX-11
kind: problem
title: $\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}\le\frac{\abs z}{MR}$ for $\abs f\le M$ on $D(0,R)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired the non-strict bound so the displayed Möbius quotient is defined in the extremal constant
    case.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Restored the book's bound |f|<=M; the solution treats the constant case |f|=M, where the quotient
    is undefined.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Recorded as its own step what the
    prose stated in passing: the statement as printed is not an assertion about a constant f with
    |f(0)| = M, since then numerator and denominator vanish identically and the quotient is 0/0;
    for constants of modulus below M the left side is zero and the inequality holds. Checked: the
    maximum modulus principle gives |f| < M on the connected disc once f is nonconstant, so
    a = f(0)/M has |a| < 1; phi_a maps the disc into itself with |phi_a(w)| < 1 equivalent to
    (1-|w|^2)(1-|a|^2) > 0, and phi_{-a} is a two-sided inverse; h = phi_a o g has h(0) = 0, so
    Schwarz gives |h(zeta)| <= |zeta|. The rewriting M (f(z)-f(0))/(M^2 - conj(f(0)) f(z)) is
    recomputed and appears as its own step, which is where the M in the denominator of the right
    side comes from. Statement and hint unchanged; no retained solution set covers the exercises
    of Stein-Shakarchi, so the card says the argument is its own.
---

::: {.exercise}
Show that if $f : D(0,R) \to \CC$ is holomorphic, with $\abs{f(z)} \leq M$ for some $M > 0$, then
$$
\abs{\frac{f(z)-f(0)}{M^{2}-\overline{f(0)}\,f(z)}} \leq \frac{\abs{z}}{MR}.
$$

[Hint: Use the Schwarz lemma.]
:::

::: {.solution}
Part (i) is the Schwarz--Pick argument: the constant case $\abs f\equiv M$ must be excluded, since there the quotient is $0/0$; otherwise $g=f/M$ and the disc automorphism $\phi_a$ with $a=g(0)$ give a self-map of the disc fixing $0$, to which Schwarz's lemma applies. The argument is this card's own: no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #constant}
If $f$ is constant then the stated inequality holds whenever its left side is defined, that is unless $\abs{f(0)}=M$; in the remaining case both numerator and denominator vanish identically and the quotient is not defined.

::: pf-proof
Let $f\equiv c$. The left side is $\dfrac{\abs{c-c}}{\abs{M^2-\overline c\,c}}=\dfrac{0}{M^2-\abs c^2}$, which is $0\le\abs z/(MR)$ when $\abs c<M$. If $\abs c=M$ then the denominator is $0$ as well, so the expression is $0/0$ and the printed inequality cannot be read as an assertion about it; the statement therefore tacitly assumes $f$ is not a constant of modulus $M$. From here $f$ is a holomorphic map of $D(0,R)$ with $\abs f<M$.
:::

:::


::: {.pf-step #maxmod}
If $f$ is nonconstant with $\abs{f(z)}\le M$ on $D(0,R)$, then $\abs{f(z)}<M$ for every $z\in D(0,R)$.

::: pf-proof
Suppose $\abs{f(z_0)}=M$ at some $z_0$. The maximum modulus principle applied to the nonconstant holomorphic $f$ on the connected domain $D(0,R)$ says $\abs f$ has no maximum there, so $\abs{f(z_0)}=M\ge\sup\abs f$ contradicts nonconstancy. Hence $\abs f<M$ pointwise. In particular $\abs{f(0)}<M$, so $a=f(0)/M$ satisfies $\abs a<1$.
:::

:::


::: {.pf-step #selfmap}
With $g(\zeta)=f(R\zeta)/M$ and $a=g(0)$, the map $\phi_a(w)=\dfrac{w-a}{1-\overline a\,w}$ is a holomorphic automorphism of $\DD$, and $h=\phi_a\circ g$ is holomorphic $\DD\to\DD$ with $h(0)=0$.

::: pf-proof
The map $\zeta\mapsto R\zeta$ carries $\DD$ onto $D(0,R)$, so $g$ is holomorphic on $\DD$ and $\abs{g(\zeta)}=\abs{f(R\zeta)}/M<1$ by step [](#maxmod){.pf-ref}; thus $g(\DD)\subseteq\DD$ and $a=g(0)$ has $\abs a<1$. For $\abs a<1$ the map $\phi_a$ is holomorphic on $\DD$; if $\abs w<1$ then $\abs{1-\overline aw}>1-\abs a>0$, so the denominator does not vanish, and
$$
\abs{\phi_a(w)}<1\iff\abs{w-a}^2<\abs{1-\overline aw}^2\iff(1-\abs w^2)(1-\abs a^2)>0,
$$
which holds for $\abs w<1$. So $\phi_a$ maps $\DD$ into itself, and $\phi_{-a}$ is a two-sided inverse since $\phi_{-a}(\phi_a(w))=w$ by direct computation; hence $\phi_a$ is an automorphism of $\DD$ carrying $a$ to $0$. Therefore $h=\phi_a\circ g$ is holomorphic with values in $\DD$, and $h(0)=\phi_a(a)=0$.
:::

:::


::: {.pf-step #schwarz}
$\abs{h(\zeta)}\le\abs\zeta$ for $\abs\zeta<1$.

::: pf-proof
$h$ is holomorphic $\DD\to\DD$ with $h(0)=0$, which is the hypothesis of Schwarz's lemma; so $\abs{h(\zeta)}\le\abs\zeta$ on $\DD$.
:::

:::


::: {.pf-step #rewrite}
For $z=R\zeta$ with $0<\abs z<R$, $\displaystyle h(\zeta)=M\,\frac{f(z)-f(0)}{M^2-\overline{f(0)}\,f(z)}$.

::: pf-proof
By definition $h(\zeta)=\dfrac{g(\zeta)-a}{1-\overline a\,g(\zeta)}$ with $g(\zeta)=f(z)/M$ and $a=f(0)/M$. Substituting,
$$
h(\zeta)=\frac{\frac{f(z)}{M}-\frac{f(0)}{M}}{1-\frac{\overline{f(0)}}{M}\cdot\frac{f(z)}{M}}
=\frac{\frac{f(z)-f(0)}{M}}{\frac{M^2-\overline{f(0)}f(z)}{M^2}}
=M\,\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)},
$$
so the displayed identity holds, and the denominator is nonzero because $1-\overline a g(\zeta)\ne0$ for $\abs{g(\zeta)}<1$.
:::

:::


::: {.pf-step #conclusion}
$\displaystyle\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}\,f(z)}}\le\frac{\abs z}{MR}$ for every $z\in D(0,R)$.

::: pf-proof
Let $z\in D(0,R)$ and $\zeta=z/R$, so $\abs\zeta<1$ and $\abs\zeta=\abs z/R$. By steps [](#schwarz){.pf-ref} and [](#rewrite){.pf-ref},
$$
M\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}=\abs{h(\zeta)}\le\abs\zeta=\frac{\abs z}{R},
$$
and dividing both sides by $M>0$ gives the inequality. At $z=0$ it reads $0\le0$ by step [](#rewrite){.pf-ref}.
:::

:::

:::
:::
