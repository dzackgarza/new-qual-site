---
schema: qual/card@1
id: P-AZOFF-C10
kind: problem
title: Conformal map of $\mathbb C\setminus\{x\in\mathbb R:|x|\ge1\}$ onto the disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used M(z)=(1+z)/(1-z) to send the two deleted real rays to the
    nonpositive real slit. The principal square root maps that slit plane
    biholomorphically to the right half-plane, and (w-1)/(w+1) maps the right
    half-plane to the unit disk. The source compilation contains no worked
    solution.
---

::: {.problem}
Find a conformal map from $\mathbb { C } \backslash \{ x \in \mathbb { R } : | x | \geq 1 \}$ onto the open unit disk.
:::

::: {.solution}
Let
$$
D=\CC\sm\{x\in\RR:\abs x\geq1\}
$$
and define
$$
M(z)=\frac{1+z}{1-z}.
$$

::: pf

::: {.pf-step #s1}

The map
$$
M:D\longrightarrow
\CC\sm(-\infty,0]
$$
is a conformal bijection.

::: pf-proof

The only pole of $M$ is $z=1$, which is not in $D$. Its inverse is
$$
M^{-1}(w)=\frac{w-1}{w+1}.
$$

On the two deleted rays away from the pole,
$$
(-\infty,-1]
\longmapsto
(-1,0],
\qquad
(1,\infty)
\longmapsto
(-\infty,-1).
$$
The remaining deleted point $z=1$ is the pole of $M$.
Conversely, if $w\leq0$ is real and $w\neq-1$, then
$$
M^{-1}(w)\in\RR
$$
and
$$
\abs{M^{-1}(w)}\geq1.
$$
Thus a finite point $z$ lies in $D$ exactly when $M(z)$ does not lie on the
nonpositive real axis. Since $-1$ itself belongs to the deleted target slit,
the inverse is defined at every point of
$$
\CC\sm(-\infty,0].
$$
Hence $M$ is bijective between the displayed domains.

Finally,
$$
M'(z)=\frac{2}{(1-z)^2}\neq0
$$
on $D$, so $M$ is conformal.

:::

:::

::: {.pf-step #s2}

On
$$
\CC\sm(-\infty,0]
$$
take the principal logarithm
$$
\Log w=\log\abs w+i\Arg w,
\qquad
-\pi<\Arg w<\pi,
$$
and put
$$
s(w)=\exp\!\left(\frac12\Log w\right).
$$
Then
$$
s:\CC\sm(-\infty,0]\longrightarrow
R,
\qquad
R=\{\zeta\in\CC:\operatorname{Re}\zeta>0\},
$$
is a conformal bijection.

::: pf-proof

The argument of $s(w)$ is
$$
\frac12\Arg w\in
\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
$$
so $s(w)\in R$.

Conversely, if $\zeta\in R$, then
$$
-\frac{\pi}{2}<\arg\zeta<\frac{\pi}{2}.
$$
Thus
$$
w=\zeta^2
$$
has argument in $(-\pi,\pi)$ and lies in the slit plane, with
$$
s(w)=\zeta.
$$
This proves surjectivity, and $w=s(w)^2$ proves injectivity.

Also
$$
s'(w)=\frac{s(w)}{2w}\neq0,
$$
so $s$ is conformal.

:::

:::

::: {.pf-step #s3}

The map
$$
C:R\longrightarrow\DD,
\qquad
C(\zeta)=\frac{\zeta-1}{\zeta+1},
$$
is a conformal bijection.

::: pf-proof

For $\zeta=u+iv$ with $u>0$,
$$
\abs{\zeta+1}^2-\abs{\zeta-1}^2=4u>0,
$$
so $\abs{C(\zeta)}<1$.

Its inverse is
$$
C^{-1}(\eta)=\frac{1+\eta}{1-\eta},
$$
and for $\eta\in\DD$,
$$
\operatorname{Re}C^{-1}(\eta)
=
\frac{1-\abs\eta^2}{\abs{1-\eta}^2}
>
0.
$$
Hence $C$ is bijective. Since
$$
C'(\zeta)=\frac{2}{(\zeta+1)^2}\neq0
$$
on $R$, it is conformal.

:::

:::

::: {.pf-step #s4}

Put
$$
q(z)=
s(M(z))
=
\exp\!\left[
\frac12
\Log\!\left(\frac{1+z}{1-z}\right)
\right],
$$
where the logarithm is the principal branch. A conformal bijection from $D$
onto the unit disk is
$$
\boxed{
F(z)=\frac{q(z)-1}{q(z)+1}.
}
$$

::: pf-proof

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
F=C\circ s\circ M
$$
is a composition of conformal bijections
$$
D\xrightarrow{M}\CC\sm(-\infty,0]
\xrightarrow{s}R\xrightarrow{C}\DD.
$$
Therefore $F$ is a conformal bijection from $D$ onto $\DD$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested map.

:::

:::

:::
