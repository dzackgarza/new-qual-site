---
schema: qual/card@1
id: E-SS7.PR-3
kind: problem
title: $\pi(x)-\operatorname{Li}(x)=O(x^{\alpha+\epsilon})$ and the zero-free half-plane $\Re s>\alpha$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Prime Number Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read against the printed item, Chapter 7, Problem 3 on printed p. 204 (PDF p. 223): the
    statement is the print's, both directions and the closing sentence that $\alpha=1/2$ is the
    Riemann hypothesis, and the asterisk the print sets before "3." is recorded in the remark. The
    argument was read and checked: the partial-summation identities between $\pi$, $\theta$ and
    $\psi$; the Tauberian step from $\psi_1(x)=x^2/2-\sum_\rho x^{\rho+1}/(\rho(\rho+1))+O(x)$,
    whose error terms are $O(x^\alpha\log^2T)$, $O(x^\alpha\log T)$, $O(x^\alpha)$ and
    $O(x^{1-\alpha-\epsilon})$ with $h=x^{\alpha+\epsilon}$ and $T=x/h$, all $O(x^{\alpha+\epsilon})$
    for $\alpha\ge1/2$; the variation bound $\sum_{x-h<n\le x+h}\Lambda(n)=O(h\log x)$; the Mellin
    identity $\int_1^\infty(\psi(x)-x)x^{-s-1}dx=-\frac1s\frac{\zeta'}{\zeta}(s)-\frac1{s-1}$ and its
    holomorphic extension; and the pole argument at a zero $\rho$ with $\Re\rho>\alpha$. Not checked:
    the zero-counting estimate $N(T)=O(T\log T)$, which is cited as standard and not proved here.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step `tauberian` on the reader's report. The averaging estimate is
    $\psi(x)-x=O(x^{\alpha+2\epsilon})$ with $h=x^{\alpha+\epsilon}$, not $O(x^{\alpha+\epsilon})$:
    the passage from the average to $\psi(x)$ costs $O(h\log x)=O(x^{\alpha+2\epsilon})$, so the
    displayed conclusion and the closing "renaming" sentence asserted the claim from a weaker bound.
    The display now reads $O(x^{\alpha+2\epsilon})$, and the closing sentence states the substitution
    that yields the claim: the argument is applied with $\epsilon/2$ in place of $\epsilon$, so that
    $h=x^{\alpha+\epsilon/2}$ and the average is $x+O(x^{\alpha+\epsilon/2})$, whence
    $\psi(x)-x=O(x^{\alpha+\epsilon})$. All other steps are unchanged; the constants were not
    recomputed. Provenance: no published solution set covers this Problem (Rhoades, *Solutions/Hints
    to the Exercises*, 2006, covers a selection of the Exercises), so the argument is the card's own.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Second component of the same step repaired, on a referee's report of this session: the step also
    needed $\alpha+\epsilon<1$. As written, "for $x$ large, $h=x^{\alpha+\epsilon}<x/2$" is false for
    $\epsilon\ge(1-\alpha)/2$ — with $\alpha=9/10$ and $\epsilon=1/2$ one gets $h=x^{7/5}>x$, so
    $x-h<0$, $\psi_1$ is evaluated below $1$ and $T=x/h<1$. The step now opens by restricting to
    $0<\epsilon<(1-\alpha)/2$, which loses nothing because a bound with a smaller exponent implies
    one with a larger, and then $h\le x^{(1+\alpha)/2}<x/2$ and $x-h\ge1$. The closing substitution is
    correspondingly legitimate. The body's estimates are unchanged.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Record of the search behind the solution's provenance sentence, which the reader asked for where
    no published solution set covers the Problem. Read: the head of R. C. Rhoades,
    *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), whose
    abstract describes it as solutions or hints to "many of the exercises", with one part per
    chapter. Searched the open web for a set answering the end-of-chapter Problems of this book: no
    document answering Chapter 7, Problem 3 was found. This search located no published set answering
    this Problem, and none is retained in this repository. Not checked: whether such a set exists
    outside what a web search reaches. The mathematics of the card is unchanged.
---

::: {.exercise}
Using the previous problem one can show that
$$
\pi(x) - \operatorname{Li}(x) = O(x^{\alpha + \epsilon}) \quad \text{as } x \to \infty
$$
for every $\epsilon > 0$, where $\alpha$ is fixed and $1/2 \leq \alpha < 1$ if and only if $\zeta(s)$ has no zeros in the strip $\alpha < \Re(s) < 1$. The case $\alpha = 1/2$ corresponds to the Riemann hypothesis.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 7, Problem 3).
:::

::: {.solution}
No published solution set covers the end-of-chapter Problems of Stein--Shakarchi: the set of R. C. Rhoades, *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), covers a selection of the chapter Exercises and not the Problems, and no other set was located. The argument is the card's own, following the printed hint.
Let
$$
\psi(x)=\sum_{n\le x}\Lambda(n),\qquad
\psi_1(x)=\int_1^x\psi(t)\,dt=\sum_{n\le x}\Lambda(n)(x-n),
$$
and let $\pi(x)=\sum_{p\le x}1$ and $\operatorname{Li}(x)=\int_2^x dt/\log t$ for $x\ge2$. We prove that the two error terms $\pi(x)-\operatorname{Li}(x)$ and $\psi(x)-x$ have the same order of magnitude, that the zero-free region implies the bound for $\psi(x)-x$, and that the bound for $\psi(x)-x$ implies the zero-free region.

::: pf

::: {.pf-step #pi-psi}
For every $\epsilon>0$,
$$
\pi(x)-\operatorname{Li}(x)=O(x^{\alpha+\epsilon})
\quad\Longleftrightarrow\quad
\psi(x)-x=O(x^{\alpha+\epsilon}).
$$

::: pf-proof
Let $\theta(x)=\sum_{p\le x}\log p$. Partial summation gives
$$
\theta(x)=\pi(x)\log x-\int_2^x\frac{\pi(t)}{t}\,dt
$$
and
$$
\pi(x)=\frac{\theta(x)}{\log x}+\int_2^x\frac{\theta(t)}{t\log^2t}\,dt.
$$
Since
$$
\psi(x)=\theta(x)+O(x^{1/2}\log x),
$$
substitution in the first identity gives
$$
\psi(x)-x=(\pi(x)-\operatorname{Li}(x))\log x-\int_2^x\frac{\pi(t)-\operatorname{Li}(t)}{t}\,dt+O(x^{1/2}\log x),
$$
where we used
$$
x=\operatorname{Li}(x)\log x-\int_2^x\frac{\operatorname{Li}(t)}{t}\,dt+O(1).
$$
If $\pi-\operatorname{Li}=O(t^{\alpha+\epsilon})$, the integral is $O(x^{\alpha+\epsilon})$ and the right side is $O(x^{\alpha+\epsilon}\log x)=O(x^{\alpha+2\epsilon})$; renaming $\epsilon$ gives the forward implication.

Conversely, substitution of $\theta=\psi+O(t^{1/2}\log t)$ in the second identity gives
$$
\pi(x)=\frac{\psi(x)}{\log x}+\int_2^x\frac{\psi(t)}{t\log^2t}\,dt+O(x^{1/2}),
$$
and
$$
\operatorname{Li}(x)=\frac{x}{\log x}+\int_2^x\frac{dt}{\log^2t}+O(1).
$$
Subtracting,
$$
\pi(x)-\operatorname{Li}(x)=\frac{\psi(x)-x}{\log x}+\int_2^x\frac{\psi(t)-t}{t\log^2t}\,dt+O(x^{1/2}).
$$
If $\psi(t)-t=O(t^{\alpha+\epsilon})$, the integral is $O(x^{\alpha+\epsilon})$, the first term is $O(x^{\alpha+\epsilon}/\log x)$, and $O(x^{1/2})=O(x^{\alpha+\epsilon})$ because $\alpha+\epsilon\ge1/2$. Hence $\pi-\operatorname{Li}=O(x^{\alpha+\epsilon})$.
:::

:::

:::

::: pf

::: {.pf-step #tauberian}
If all nontrivial zeros of $\zeta$ satisfy $\Re\rho\le\alpha$, then for every $\epsilon>0$,
$$
\psi(x)-x=O(x^{\alpha+\epsilon}).
$$

::: pf-proof
Fix $\epsilon>0$. Since a bound $O(x^{\alpha+\epsilon'})$ with $0<\epsilon'\le\epsilon$ implies $O(x^{\alpha+\epsilon})$, we may assume $\epsilon<(1-\alpha)/2$; put $h=x^{\alpha+\epsilon}$. Then $h\le x^{(1+\alpha)/2}<x/2$ for $x$ large, and $x-h\ge x/2\ge1$. By [[E-SS7.PR-2|the previous problem]],
$$
\psi_1(x)=\frac{x^2}{2}-\sum_\rho\frac{x^{\rho+1}}{\rho(\rho+1)}+O(x).
$$
Since $\psi_1'=\psi$ almost everywhere,
$$
\frac{\psi_1(x+h)-\psi_1(x-h)}{2h}
=\frac{1}{2h}\int_{x-h}^{x+h}\psi(t)\,dt.
$$
On the other hand, the difference quotient of the right side is
$$
x-\sum_\rho\frac{(x+h)^{\rho+1}-(x-h)^{\rho+1}}{2h\rho(\rho+1)}+O(x/h).
$$
For each nontrivial zero $\rho$, Taylor's formula gives, uniformly for $\abs{\rho}\le T$,
$$
\frac{(x+h)^{\rho+1}-(x-h)^{\rho+1}}{2h\rho(\rho+1)}
=\frac{x^\rho}{\rho}+O\left(h^2\abs{\rho}x^{\Re\rho-2}\right).
$$
Let $T=x/h$. The zeros with $\abs{\Im\rho}\le T$ contribute
$$
O\left(x^\alpha\sum_{\abs{\Im\rho}\le T}\frac{1}{\abs{\rho}}\right)
=O(x^\alpha\log^2T)
$$
by the standard zero-counting estimate $N(T)=O(T\log T)$ and partial summation. The Taylor errors contribute
$$
O\left(h^2x^{\alpha-2}\sum_{\abs{\Im\rho}\le T}\abs{\rho}\right)
=O(h^2x^{\alpha-2}T^2\log T)
=O(x^\alpha\log T).
$$
The zeros with $\abs{\Im\rho}>T$ contribute
$$
O\left(\frac{x^{\alpha+1}}{h}\sum_{\abs{\Im\rho}>T}\frac{1}{\abs{\rho}^2}\right)
=O\left(\frac{x^{\alpha+1}}{hT}\right)
=O(x^\alpha).
$$
The $O(x/h)$ term is $O(x^{1-\alpha-\epsilon})$. Since $1/2\le\alpha<1$, every error is $O(x^{\alpha+\epsilon})$, so
$$
\frac{1}{2h}\int_{x-h}^{x+h}\psi(t)\,dt=x+O(x^{\alpha+\epsilon}).
$$
Finally, $\psi$ is nondecreasing and its total increase over $[x-h,x+h]$ is at most
$$
\sum_{x-h<n\le x+h}\Lambda(n)\le(2h+1)\log(x+h)=O(h\log x).
$$
Hence the average differs from $\psi(x)$ by $O(h\log x)=O(x^{\alpha+2\epsilon})$, and
$$
\psi(x)-x=O(x^{\alpha+2\epsilon}).
$$
Since $\epsilon>0$ was arbitrary and $\epsilon/2<(1-\alpha)/2$ as well, applying the argument with $\epsilon/2$ in place of $\epsilon$ — so that $h=x^{\alpha+\epsilon/2}$ and the average is $x+O(x^{\alpha+\epsilon/2})$ — gives $\psi(x)-x=O(x^{\alpha+\epsilon})$, which is the claim.
:::

:::

:::

::: pf

::: {.pf-step #mellin}
For $\Re s>1$,
$$
\int_1^\infty(\psi(x)-x)x^{-s-1}\,dx
=-\frac{1}{s}\frac{\zeta'}{\zeta}(s)-\frac{1}{s-1}.
$$
If $\psi(x)-x=O(x^{\alpha+\epsilon})$ for every $\epsilon>0$, then the right side extends holomorphically to $\Re s>\alpha$.

::: pf-proof
The Dirichlet series gives
$$
-\frac{\zeta'}{\zeta}(s)=s\int_1^\infty\psi(x)x^{-s-1}\,dx,\qquad \Re s>1.
$$
Since
$$
\int_1^\infty x\cdot x^{-s-1}\,dx=\frac{1}{s-1},
$$
subtraction gives the identity. If $\psi(x)-x=O(x^{\alpha+\epsilon})$, the integral converges absolutely and locally uniformly on $\Re s>\alpha+\epsilon$, so it is holomorphic there. Since $\epsilon>0$ is arbitrary, it is holomorphic on $\Re s>\alpha$. The identity then continues the right side holomorphically to $\Re s>\alpha$. Near $s=1$,
$$
-\frac{\zeta'}{\zeta}(s)=\frac{1}{s-1}+O(1),
$$
so
$$
-\frac{1}{s}\frac{\zeta'}{\zeta}(s)-\frac{1}{s-1}
=\frac{1}{s(s-1)}-\frac{1}{s-1}+O(1)
=-\frac{1}{s}+O(1),
$$
which is holomorphic at $s=1$.
:::

:::

::: {.pf-step #no-zeros}
If $\psi(x)-x=O(x^{\alpha+\epsilon})$ for every $\epsilon>0$, then $\zeta(s)\ne0$ for $\Re s>\alpha$.

::: pf-proof
Suppose $\zeta$ has a zero of order $m\ge1$ at $\rho$ with $\Re\rho>\alpha$. Choose $\epsilon>0$ with $\alpha+\epsilon<\Re\rho$. By step [](#mellin){.pf-ref}, the right side of the Mellin identity is holomorphic on $\Re s>\alpha+\epsilon$. But $-\zeta'/\zeta$ has a simple pole at $\rho$, the term $-1/(s-1)$ is holomorphic at $\rho$ because $\rho\ne1$, and $1/s$ is holomorphic and nonzero at $\rho$. Hence the right side has a pole at $\rho$, a contradiction. Therefore no zero lies in $\Re s>\alpha$.
:::

:::

:::

Combining the three parts, if $\zeta$ has no zeros in $\alpha<\Re s<1$, then every nontrivial zero satisfies $\Re\rho\le\alpha$ because $\zeta$ has no zeros with $\Re s\ge1$ (the Euler product for $\Re s>1$, and the nonvanishing of $\zeta$ on $\Re s=1$). Step [](#tauberian){.pf-ref} gives $\psi(x)-x=O(x^{\alpha+\epsilon})$, and step [](#pi-psi){.pf-ref} gives $\pi(x)-\operatorname{Li}(x)=O(x^{\alpha+\epsilon})$ for every $\epsilon>0$. Conversely, if $\pi(x)-\operatorname{Li}(x)=O(x^{\alpha+\epsilon})$ for every $\epsilon>0$, then step [](#pi-psi){.pf-ref} gives $\psi(x)-x=O(x^{\alpha+\epsilon})$, and step [](#no-zeros){.pf-ref} gives $\zeta(s)\ne0$ for $\Re s>\alpha$, in particular in the strip $\alpha<\Re s<1$. Thus the two conditions are equivalent. For $\alpha=1/2$, the condition says that there are no zeros with $\Re s>1/2$; the functional equation then places every nontrivial zero on $\Re s=1/2$, which is the Riemann hypothesis.
:::
