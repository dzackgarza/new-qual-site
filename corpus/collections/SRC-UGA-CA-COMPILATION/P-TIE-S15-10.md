---
schema: qual/card@1
id: P-TIE-S15-10
kind: problem
title: Uniqueness and the Schwarz reflection principle for harmonic functions
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 10.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX and moved the Stein cross-reference to a remark against Spring 2015, question 10, page 12 of Questions_from_Tie.pdf (read from the page image).
---

::: {.problem}
(1) Assume $u$ is harmonic on open set $O$ and $z_n$ is a sequence in $O$ such that $u(z_n) = 0$ and $\lim z_n \in O$. Prove or disprove that $u$ is identically zero. What if $O$ is a region?

(2) Assume $u$ is harmonic on open set $O$ and $u(z) = 0$ on a disc in $O$. Prove or disprove that $u$ is identically zero. What if $O$ is a region?

(3) Formulate and prove a Schwarz reflection principle for harmonic functions.

Hint: Verify the mean value property for your new function obtained by Schwarz reflection principle.
:::

::: {.remark}
The source adds "cf. Theorem 5.6 on p.60 of Stein et al." to part (3), a pointer to the Schwarz reflection principle for holomorphic functions in Stein and Shakarchi, *Complex Analysis*; part (3) asks for the harmonic analogue and does not depend on the reference.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The assertion in part (1) is false, even when $O$ is a region.


::: pf-proof

Take
$$
O=\DD,
\qquad
u(z)\coloneqq\operatorname{Re}z.
$$
The function $u$ is harmonic and nonzero on the connected region $\DD$. Let
$$
z_n\coloneqq\frac{i}{n}.
$$
Then
$$
z_n\in\DD,
\qquad
u(z_n)=0
$$
for every $n$, and
$$
z_n\longrightarrow0\in\DD.
$$
Thus an accumulating sequence of zeros does not force a harmonic function to vanish identically.

:::

:::

::: {.pf-step #s1-2}

The assertion in part (2) is false for an arbitrary open set $O$.


::: pf-proof

Let
$$
O
\coloneqq
\{z:\abs{z}<1\}
\cup
\{z:\abs{z-3}<1\},
$$
the disjoint union of two disks. Define
$$
u(z)
\coloneqq
\begin{cases}
0,&\abs{z}<1,\\
1,&\abs{z-3}<1.
\end{cases}
$$
The function is harmonic on the open set $O$ and vanishes on the entire first disk, but it is not identically zero on $O$.

:::

:::

::: {.pf-step #s1-3}

If $O$ is a region and a harmonic function $u$ vanishes on a nonempty disk contained in $O$, then
$$
u\equiv0
$$
on $O$.


::: pf-proof

Let
$$
E
\coloneqq
\{z\in O:\text{$u$ vanishes on some neighborhood of $z$}\}.
$$
The set $E$ is nonempty by hypothesis and is open by definition.

We show that $E$ is closed in $O$. Let $z_0\in O$ lie in the closure of $E$. Choose a disk
$$
B(z_0,r)\subset O.
$$
Because $z_0$ lies in the closure of $E$, the disk contains some point $w\in E$, and therefore $u$ vanishes on a nonempty open subset of $B(z_0,r)$.

On the simply connected disk $B(z_0,r)$, the harmonic function $u$ has a harmonic conjugate $v$, so
$$
F\coloneqq u+iv
$$
is holomorphic there. Choose a connected nonempty open subset $V\subset B(z_0,r)$ on which $u=0$. Then
$$
F(V)\subset i\RR.
$$
If $F\restrict_V$ were nonconstant, the open mapping theorem would make $F(V)$ open in $\CC$, impossible because $i\RR$ has empty interior. Thus $F$ is constant on $V$. The identity theorem then implies that $F$ is constant on the whole disk. Its real part is $u$, and since $u=0$ on $V$, one has
$$
u\equiv0
$$
on $B(z_0,r)$. Thus $z_0\in E$.

Hence $E$ is nonempty, open, and closed in the connected set $O$. Therefore $E=O$, so $u\equiv0$ on $O$.

:::

:::

::: {.pf-step #s1-4}

Harmonic Schwarz reflection principle: let $G\subset\CC$ be a region symmetric under complex conjugation, let
$$
G^+\coloneqq G\cap\{z:\operatorname{Im}z>0\},
\qquad
I\coloneqq G\cap\RR,
$$
and suppose $u$ is harmonic on $G^+$, extends continuously to $G^+\cup I$, and satisfies
$$
u=0
$$
on $I$. Define
$$
U(z)
\coloneqq
\begin{cases}
u(z),&\operatorname{Im}z>0,\\
0,&z\in I,\\
-u(\overline z),&\operatorname{Im}z<0.
\end{cases}
$$
Then $U$ is harmonic on $G$.


::: pf-proof

The function $U$ is continuous across $I$ because $u$ extends continuously to $I$ with value $0$. Away from $I$, it is harmonic: in the upper half it equals $u$, while in the lower half it is the composition of $u$ with reflection followed by multiplication by $-1$, which preserves harmonicity.

It remains to verify harmonicity at a point $x_0\in I$. Choose $r>0$ such that the closed disk
$$
\overline{B(x_0,r)}
\subset G.
$$
For $0<\rho<r$, the average of $U$ over the circle $\abs{z-x_0}=\rho$ is
$$
\frac1{2\pi}
\int_0^{2\pi}
U(x_0+\rho e^{it})\,dt.
$$
Pair the point with parameter $t\in(0,\pi)$ with its reflected point having parameter $2\pi-t$. By the definition of $U$,
$$
U(x_0+\rho e^{i(2\pi-t)})
=
-U(x_0+\rho e^{it}).
$$
Hence the two semicircle contributions cancel, and the average is $0=U(x_0)$. Thus $U$ satisfies the mean value property at every point of $I$. Since $U$ is continuous and has the mean value property locally at every point of $G$, it is harmonic on $G$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (1), steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} answer part (2), and step [](#s1-4){.pf-ref} formulates and proves the harmonic Schwarz reflection principle requested in part (3).

:::

:::

:::
