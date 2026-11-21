---
schema: qual/card@1
id: P-CAFA15F
kind: problem
title: "Periods of meromorphic functions form a discrete subgroup"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/Complex-Qual-F15.pdf, problem 6 (10
    pts): "Let f(z) be a meromorphic function. A complex number omega is called a period of f if
    f(z + omega) = f(z) for all z. (i) Show that if omega_1 and omega_2 are periods of f then
    n_1 omega_1 + n_2 omega_2 is a period of f for all integers n_1 and n_2. (ii) Show that there are
    at most finitely many periods of f in any bounded subset of the complex plane." The card's two
    parts are those two; the card adds "nonconstant", which the paper omits, and its remark records
    the counterexample to the printed wording.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The one gap closed is in the passage
    "by continuity f(z + omega) = lim f(z + omega_n) = f(z)": for a fixed z the points z + omega_n
    could be poles, so the step now restricts z to the open set where f is holomorphic at z + omega,
    observes that only finitely many omega_n give a pole there -- otherwise z + omega is a limit of
    poles -- and concludes the equality on a nonempty open set, whence the identity theorem for
    meromorphic functions. Checked additionally that the derivative computation needs the disc
    B(z_0, 2r) free of poles, and that nonconstancy is exactly the hypothesis used at the end.
---

::: {.problem}
Let $f(z)$ be a nonconstant meromorphic function.
A complex number $\omega$ is called a period of $f$ if $f(z + \omega) = f(z)$ for all $z$.

(i) Show that if $\omega_1$ and $\omega_2$ are periods of $f$, then $n_1\omega_1 + n_2\omega_2$ is a period of $f$ for all integers $n_1$ and $n_2$.

(ii) Show that there are at most finitely many periods of $f$ in any bounded subset of the complex plane.
:::

::: {.remark}
The official Fall 2015 exam omits the word "nonconstant." Without it, part (ii) is false: every complex number is a period of a constant meromorphic function.
:::

::: {.solution}
This is Problem 6 (10 points) of the UCSD complex-analysis qualifying exam of Fall 2015 (`assets/attachments/Complex-Qual-F15.pdf`). No published solution set is transcribed: the argument is the card's own.

The paper prints the problem for a meromorphic function and does not say "nonconstant"; part (ii) is false without that hypothesis, since every complex number is a period of a constant function. The statement on this card carries the hypothesis and the remark below records the defect of the printed wording.

::: pf

::: {.pf-step #subgroup}
(i) The set $\Lambda=\theset{\omega\in\CC\mid f(z+\omega)=f(z)\text{ for all }z}$ of periods of $f$ is an additive subgroup of $\CC$; in particular $n_{1}\omega_{1}+n_{2}\omega_{2}\in\Lambda$ for all $n_{1},n_{2}\in\ZZ$ whenever $\omega_{1},\omega_{2}\in\Lambda$.

::: pf-proof
$0\in\Lambda$ because $f(z+0)=f(z)$. If $\omega,\eta\in\Lambda$ then for every $z$,
$$f(z+\omega+\eta)=f((z+\omega)+\eta)=f(z+\omega)=f(z),$$
so $\omega+\eta\in\Lambda$. If $\omega\in\Lambda$ then $f(z-\omega)=f((z-\omega)+\omega)=f(z)$, so $-\omega\in\Lambda$. A subset of an abelian group closed under addition and negation and containing $0$ is a subgroup, and the integer combination $n_{1}\omega_{1}+n_{2}\omega_{2}$ is a sum of $\pm\omega_{1}$ and $\pm\omega_{2}$.
:::
:::

::: {.pf-step #limitpoint}
If a sequence of distinct periods $\omega_{n}$ converges to $\omega\in\CC$, then $\omega$ is a period of $f$.

::: pf-proof
Let $U$ be the set of $z$ such that $f$ is holomorphic at $z+\omega$; its complement is the translate of the pole set of $f$, which is discrete, so $U$ is a nonempty open set. Fix $z\in U$. Only finitely many $\omega_{n}$ can be poles of $f$ at $z+\omega_{n}$: otherwise some subsequence of the points $z+\omega_{n}$ would consist of poles tending to $z+\omega$, making $z+\omega$ a limit of poles and hence a pole, contrary to $z\in U$. So for all large $n$ the point $z+\omega_{n}$ is not a pole, and continuity of $f$ at $z+\omega$ gives
$$f(z+\omega)=\lim_{n\to\infty}f(z+\omega_{n})=\lim_{n\to\infty}f(z)=f(z).$$
Thus $f(z+\omega)=f(z)$ for all $z$ in the nonempty open set $U$, and the identity theorem for meromorphic functions gives the equality for all $z$; so $\omega\in\Lambda$.
:::
:::

::: {.pf-step #small}
If some bounded set contains infinitely many periods, then there are nonzero periods $\tau_{n}$ with $\tau_{n}\to0$.

::: pf-proof
An infinite bounded set has an accumulation point, so a bounded set containing infinitely many periods contains a sequence of distinct periods $\omega_{n}\to\omega$; by step [](#limitpoint){.pf-ref}, $\omega$ is a period, and $\tau_{n}=\omega_{n}-\omega$ is a nonzero period for every $n$ by step [](#subgroup){.pf-ref}, with $\tau_{n}\to0$.
:::
:::

::: {.pf-step #constant}
Under the hypothesis of step [](#small){.pf-ref}, $f$ is constant.

::: pf-proof
Choose $z_{0}$ with $f$ holomorphic at $z_{0}$ and $r>0$ with $f$ holomorphic and hence bounded on $B(z_{0},2r)$; this is possible because the poles of $f$ are isolated. For $\abs{z-z_{0}}<r$ and for all $n$ large enough that $\abs{\tau_{n}}<r$ one has $z+\tau_{n}\in B(z_{0},2r)$ and $f(z+\tau_{n})=f(z)$ since $\tau_{n}$ is a period. Hence
$$f'(z)=\lim_{n\to\infty}\frac{f(z+\tau_{n})-f(z)}{\tau_{n}}=0$$
for every $z\in B(z_{0},r)$, the limit being along the sequence $\tau_{n}\to0$ with $\tau_{n}\neq0$. So $f$ is constant on the nonempty open disc $B(z_{0},r)$, and by the identity theorem for meromorphic functions $f$ is constant on $\CC$.
:::
:::

::: {.pf-step #finitely}
(ii) Every bounded subset of $\CC$ contains at most finitely many periods of a nonconstant meromorphic $f$.

::: pf-proof
If a bounded set contained infinitely many periods, steps [](#small){.pf-ref} and [](#constant){.pf-ref} would make $f$ constant, contradicting the hypothesis that $f$ is nonconstant. Note that this is where nonconstancy is used: without it the statement fails, every point of $\CC$ being a period of a constant meromorphic function, which is the defect the exam's own wording leaves open and the remark above records.
:::
:::
:::

:::
