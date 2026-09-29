---
schema: qual/card@1
id: P-AZOFF-C09
kind: problem
title: Conformal map of the slit plane $\mathbb C\setminus(-\infty,0]$ onto the disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the principal square-root branch, with -pi<Arg z<pi, to map the plane
    slit along the nonpositive real axis biholomorphically onto the right
    half-plane. The Cayley map (w-1)/(w+1) then maps that half-plane onto the
    unit disk. The source compilation contains no worked solution.
---

::: {.problem}
Find a conformal map from $\mathbb { C } \backslash \{ x \in \mathbb { R } : x \leq 0 \}$ onto the open unit disk.
:::

::: {.solution}
Let
$$
D=\CC\sm(-\infty,0].
$$
On $D$ take the principal logarithm
$$
\Log z=\log\abs z+i\Arg z,
\qquad
-\pi<\Arg z<\pi,
$$
and define
$$
s(z)=\exp\!\left(\frac12\Log z\right).
$$

::: pf

::: {.pf-step #s1}

The map
$$
s:D\longrightarrow
R,
\qquad
R=\{w\in\CC:\operatorname{Re}w>0\},
$$
is a conformal bijection.

::: pf-proof

For $z\in D$,
$$
-\frac{\pi}{2}
<
\arg s(z)
=
\frac12\Arg z
<
\frac{\pi}{2}.
$$
Hence
$$
\operatorname{Re}s(z)>0,
$$
so $s(D)\subseteq R$.

Conversely, let $w\in R$. Then
$$
-\frac{\pi}{2}<\arg w<\frac{\pi}{2}.
$$
Set
$$
z=w^2.
$$
Then
$$
-\pi<\arg z<\pi,
$$
so $z\in D$, and the chosen branch satisfies
$$
s(z)=w.
$$
Thus $s$ is onto. Since
$$
z=s(z)^2,
$$
it is also injective.

Finally,
$$
s'(z)=\frac{s(z)}{2z}\neq0
$$
on $D$, so $s$ is conformal.

:::

:::

::: {.pf-step #s2}

The map
$$
C:R\longrightarrow\DD,
\qquad
C(w)=\frac{w-1}{w+1},
$$
is a conformal bijection.

::: pf-proof

For $w=u+iv$ with $u>0$,
$$
\abs{w+1}^2-\abs{w-1}^2=4u>0,
$$
so
$$
\abs{C(w)}<1.
$$

The inverse is
$$
C^{-1}(\eta)=\frac{1+\eta}{1-\eta}.
$$
For $\eta\in\DD$,
$$
\operatorname{Re}C^{-1}(\eta)
=
\frac{1-\abs\eta^2}{\abs{1-\eta}^2}
>
0.
$$
Thus $C^{-1}(\DD)\subseteq R$, proving bijectivity.

Also
$$
C'(w)=\frac{2}{(w+1)^2}\neq0
$$
on $R$, so $C$ is conformal.

:::

:::

::: {.pf-step #s3}

A conformal bijection from the slit plane $D$ onto the unit disk is
$$
\boxed{
F(z)
=
\frac{s(z)-1}{s(z)+1},
\qquad
s(z)=\exp\!\left(\frac12\Log z\right),
\quad
-\pi<\Arg z<\pi.
}
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref},
$$
F=C\circ s
$$
is a composition of conformal bijections
$$
D\xrightarrow{s}R\xrightarrow{C}\DD.
$$
Therefore $F$ is a conformal bijection from $D$ onto $\DD$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested map.

:::

:::

:::
