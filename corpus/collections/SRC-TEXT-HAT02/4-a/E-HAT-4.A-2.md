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
---

::: {.problem}
Show that under the map $\langle X, Y \rangle \to \operatorname{Hom}(\pi_n(X, x_0), \pi_n(Y, y_0))$, $[f] \mapsto f_*$, the action of $\pi_1(Y, y_0)$ on $\langle X, Y \rangle$ corresponds to composing with the action on $\pi_n(Y, y_0)$, that is, $(\gamma f)_* = \beta_\gamma f_*$.
Deduce a bijection of $[X, K(\pi, 1)]$ with the set of orbits of $\operatorname{Hom}(\pi_1(X), \pi)$ under composition with inner automorphisms of $\pi$.
In particular, if $\pi$ is abelian then $[X, K(\pi, 1)] = \langle X, K(\pi, 1) \rangle = \operatorname{Hom}(\pi_1(X), \pi)$.
:::

::: {.solution}
Let $H:X\times I\to Y$ represent the action of a loop $\gamma$ on a based map $f:X\to Y$. Thus $H(-,0)=f$, $H(-,1)$ represents $\gamma f$, and the path $H(x_0,t)$ represents $\gamma$; this is the action of Proposition 4A.1 (p. 422), in the left-action convention obtained from Hatcher's right action by $[\gamma][f_0]=[f_0][\gamma]^{-1}$. For any based $a:S^n\to X$, the composite
$$
S^n\times I\xrightarrow{a\times\id}X\times I\xrightarrow{H}Y
$$
is a homotopy from $fa$ to $(\gamma f)a$ whose basepoint traces $\gamma$. The definition of the basepoint-change isomorphism $\beta_\gamma$ on $\pi_n(Y,y_0)$ (§4.1, p. 342) therefore gives
$$
[(\gamma f)a]=\beta_\gamma[fa].
$$
Since this holds for every $[a]\in\pi_n(X)$, it proves $(\gamma f)_*=\beta_\gamma f_*$.

A based map $X\to K(\pi,1)$ is classified up to based homotopy by its homomorphism $\pi_1(X)\to\pi$, and every homomorphism is realized (Proposition 1B.9, p. 90). In degree one, $\beta_\gamma$ is conjugation by $\gamma\in\pi$. Passing from based to free homotopy classes takes orbits under this action, by Proposition 4A.2 (p. 422) applied to $Z=X$ and $X=K(\pi,1)$. Hence
$$
[X,K(\pi,1)]\cong\operatorname{Hom}(\pi_1(X),\pi)/\operatorname{Inn}(\pi).
$$

If $\pi$ is abelian then $\operatorname{Inn}(\pi)=1$, so the orbit set is the whole of $\operatorname{Hom}(\pi_1(X),\pi)$, and the bijection says that the forgetful map $\langle X,K(\pi,1)\rangle\to[X,K(\pi,1)]$ is itself a bijection: every free homotopy class contains a unique based one. Hence
$$
[X,K(\pi,1)]=\langle X,K(\pi,1)\rangle=\operatorname{Hom}(\pi_1(X),\pi).
$$
:::
