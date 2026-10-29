---
schema: qual/card@1
id: P-WESCA09-III2
kind: problem
title: 'Harmonic conjugates on simply connected domains'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section III, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $u\in C^2(D)$ be harmonic on a simply connected domain $D\subset\CC$.
Prove that $u$ has a harmonic conjugate $v$, so that $u+iv$ is analytic on $D$.
Hint: consider $u_x-iu_y$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function
\[
g=u_x-i u_y
\]
is analytic on $D$.


::: pf-proof

Write
\[
g=p+iq,
\qquad
p=u_x,
\qquad
q=-u_y.
\]
Since $u\in C^2(D)$, the functions $p$ and $q$ have continuous first partial
derivatives. The Cauchy--Riemann equations for $g$ are
\[
p_x=q_y,
\qquad
p_y=-q_x.
\]
The first equation is
\[
u_{xx}=-u_{yy},
\]
which holds because $u$ is harmonic. The second is
\[
u_{xy}=u_{yx},
\]
which holds because $u\in C^2(D)$. Hence $g$ is analytic on $D$.

:::

:::

::: {.pf-step #s1-2}

The function $g$ has an analytic primitive $F$ on $D$.


::: pf-proof

By step [](#s1-1){.pf-ref}, $g$ is analytic. Since $D$ is simply connected, the standard
primitive theorem for holomorphic functions on simply connected domains gives
an analytic function $F$ on $D$ such that
\[
F'=g.
\]

:::

:::

::: {.pf-step #s1-3}

If $F=U+iV$, then $U-u$ is constant on $D$.


::: pf-proof

Since $F$ is analytic,
\[
F'=U_x+iV_x.
\]
Together with step [](#s1-2){.pf-ref} and the definition of $g$, this gives
\[
U_x=u_x,
\qquad
V_x=-u_y.
\]
The Cauchy--Riemann equations for $F$ give $U_y=-V_x$, so
\[
U_y=u_y.
\]
Thus
\[
(U-u)_x=0,
\qquad
(U-u)_y=0.
\]
Because $D$ is a domain and therefore connected, $U-u$ is constant on $D$.

:::

:::

::: {.pf-step #s1-4}

The function $u$ has a harmonic conjugate on $D$.


::: pf-proof

By step [](#s1-3){.pf-ref}, there is a real constant $c$ such that $U=u+c$. Define
\[
v=V.
\]
Then
\[
u+iv=F-c,
\]
which is analytic on $D$. Hence $v$ is a harmonic conjugate of $u$. In
particular, as the imaginary part of an analytic function, $v$ is harmonic.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required existence of a harmonic conjugate.

:::

:::

:::
