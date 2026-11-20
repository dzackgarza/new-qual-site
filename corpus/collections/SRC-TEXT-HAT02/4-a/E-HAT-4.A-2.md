---
schema: qual/card@1
id: E-HAT-4.A-2
kind: problem
title: '$\pi_1$-action on $\langle X, Y \rangle$ and Eilenberg--MacLane spaces'
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.A, printed p. 426, with the action of Proposition 4A.1
    (p. 422), the change-of-basepoint isomorphism of §4.1 (p. 342), Proposition 4A.2 (p. 422) and
    Proposition 1B.9 (p. 90). Correct. A homotopy $H$ representing the action of $\gamma$ gives,
    for each based $a\colon S^n\to X$, a homotopy $H\circ(a\times\mathrm{id})$ from $fa$ to
    $(\gamma f)a$ whose basepoint traces $\gamma$, which is exactly the definition of $\beta_\gamma$
    on $\pi_n(Y)$, so $(\gamma f)_*=\beta_\gamma f_*$ for every $a$ and hence as homomorphisms.
    For $n=1$, $\beta_\gamma$ is conjugation by $\gamma$, so free homotopy classes of maps into
    $K(\pi,1)$ are the orbits of $\operatorname{Hom}(\pi_1(X),\pi)$ under $\operatorname{Inn}(\pi)$,
    and when $\pi$ is abelian the orbits are singletons, giving
    $[X,K(\pi,1)]=\langle X,K(\pi,1)\rangle=\operatorname{Hom}(\pi_1(X),\pi)$. Nothing changed.
    Not claimed: a published solution, and no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.A Exercise 2, with the action of Proposition 4A.1, the
    change-of-basepoint isomorphism of §4.1, Lemma 1.19, Proposition 4A.2 and Proposition 1B.9.
    One mathematical defect repaired. The card let $H$ run from $f$ to $\gamma f$ with basepoint
    path $\gamma$ and read off $[(\gamma f)a]=\beta_\gamma[fa]$. That homotopy is the *right*
    action of Proposition 4A.1: by Lemma 1.19, $\phi_{0*}=\beta_h\phi_{1*}$ on a homotopy with
    basepoint path $h$, so its endpoint is $\beta_\gamma^{-1}$ applied to its start, and the
    derivation as written would prove $(\gamma f)_*=\beta_\gamma^{-1}f_*$. The left action the
    exercise uses, $[\gamma][f_0]=[f_0][\gamma]^{-1}$, is represented by the reverse homotopy, so
    $H$ now runs from $\gamma f$ to $f$ with basepoint path $\gamma$, and then
    $[(\gamma f)a]=\beta_\gamma[fa]$ is correct. The card also carried no structured proof, its
    solution being one prose argument; it is now five steps with their proofs. The prose named
    printed pages for Proposition 4A.1, the change-of-basepoint map, Proposition 1B.9 and
    Proposition 4A.2; by the owner's correction of this date it cites the numbered statements
    only. The lead now says that no retained solution set covers the exercise, checked against
    Sam's set, which has no §4.A. Not checked: no certificate, and no re-derivation of
    Proposition 1B.9.

---

::: {.problem}
Show that under the map $\langle X, Y \rangle \to \operatorname{Hom}(\pi_n(X, x_0), \pi_n(Y, y_0))$, $[f] \mapsto f_*$, the action of $\pi_1(Y, y_0)$ on $\langle X, Y \rangle$ corresponds to composing with the action on $\pi_n(Y, y_0)$, that is, $(\gamma f)_* = \beta_\gamma f_*$.
Deduce a bijection of $[X, K(\pi, 1)]$ with the set of orbits of $\operatorname{Hom}(\pi_1(X), \pi)$ under composition with inner automorphisms of $\pi$.
In particular, if $\pi$ is abelian then $[X, K(\pi, 1)] = \langle X, K(\pi, 1) \rangle = \operatorname{Hom}(\pi_1(X), \pi)$.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own. It is Hatcher's Exercise 2 of §4.A, and it uses the action of Proposition 4A.1, the change-of-basepoint isomorphism $\beta_\gamma$ of §4.1, Proposition 4A.2 and Proposition 1B.9.

Let $H:X\times I\to Y$ be a homotopy from a representative of $\gamma f$ to $f$ whose basepoint path $t\mapsto H(x_0,t)$ is the loop $\gamma$. This is the left action of $\pi_1(Y,y_0)$ on $\langle X,Y\rangle$: Hatcher defines a right action by $[f_0][\gamma]=[f_1]$ when a homotopy from $f_0$ to $f_1$ has basepoint path $\gamma$, and converts it to the left action by $[\gamma][f_0]=[f_0][\gamma]^{-1}$, which runs that homotopy backwards; so a homotopy representing $[\gamma][f_0]$ runs from $f_1$ to $f_0$ with basepoint path $\gamma$.

::: pf

::: {.pf-step #track}
For every based $a\colon(S^n,s_0)\to(X,x_0)$ the composite $H\circ(a\times\id)$ is a homotopy from $(\gamma f)a$ to $fa$ whose basepoint path is $\gamma$.

::: pf-proof
$(H\circ(a\times\id))(s,0)=H(a(s),0)=(\gamma f)(a(s))$ and $(H\circ(a\times\id))(s,1)=H(a(s),1)=f(a(s))$, while at the basepoint $s_0$ of $S^n$ the path $t\mapsto H(a(s_0),t)=H(x_0,t)$ is $\gamma$.
:::

:::

::: {.pf-step #beta}
$[(\gamma f)a]=\beta_\gamma[fa]$ for every based $a$.

::: pf-proof
By the definition in §4.1, $\beta_\gamma$ carries the class of a based map $g$ to the class obtained by dragging the basepoint of $g$ backwards along $\gamma$, which is the value at the start of a homotopy ending at $g$ whose basepoint path is $\gamma$. Step [](#track){.pf-ref} exhibits exactly such a homotopy, ending at $fa$ and starting at $(\gamma f)a$.
:::

:::

::: {.pf-step #homomorphism}
$(\gamma f)_*=\beta_\gamma f_*$ as homomorphisms $\pi_n(X,x_0)\to\pi_n(Y,y_0)$.

::: pf-proof
By step [](#beta){.pf-ref} the two homomorphisms agree on every class $[a]$, and the classes $[a]$ generate $\pi_n(X,x_0)$.
:::

:::

::: {.pf-step #degree-one}
For $n=1$ the orbit set of the action is $\operatorname{Hom}(\pi_1(X),\pi)/\operatorname{Inn}(\pi)$, hence $[X,K(\pi,1)]\cong\operatorname{Hom}(\pi_1(X),\pi)/\operatorname{Inn}(\pi)$.

::: pf-proof
A based map $X\to K(\pi,1)$ is determined up to based homotopy by its homomorphism $\pi_1(X)\to\pi$, and every homomorphism is realised, by Proposition 1B.9. In degree one $\beta_\gamma$ is conjugation by $\gamma\in\pi$, so step [](#homomorphism){.pf-ref} says that acting by $\gamma$ composes the homomorphism with conjugation by $\gamma$. Free homotopy classes are the orbits of the based classes under this action, by Proposition 4A.2 applied with $Z=X$ and with $K(\pi,1)$ in place of the target. Hence the displayed bijection.
:::

:::

::: {.pf-step #abelian}
If $\pi$ is abelian then $[X,K(\pi,1)]=\langle X,K(\pi,1)\rangle=\operatorname{Hom}(\pi_1(X),\pi)$.

::: pf-proof
For abelian $\pi$ the group $\operatorname{Inn}(\pi)$ is trivial, so by step [](#degree-one){.pf-ref} the forgetful map $\langle X,K(\pi,1)\rangle\to[X,K(\pi,1)]$ is a bijection: every free homotopy class contains exactly one based class. Composing with the bijection of Proposition 1B.9 gives the displayed identity.
:::

:::

:::
:::
