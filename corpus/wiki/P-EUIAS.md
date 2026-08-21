---
schema: qual/card@1
id: P-EUIAS
kind: problem
title: von Neumann's mean ergodic theorem for a unitary operator
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Functional Analysis
relations: []
review: draft
solved: true
---

::: problem
Let $U$ be a unitary operator on $H$ a Hilbert space, let $M \da \ts{x\in H \st Ux = x}$, let $P$ be the orthogonal projection onto $M$, and define
\[
S_N \da {1\over N} \sum_{n=0}^{N-1} U^n
.\]
Show that for all $x\in H$,
\[
\norm{ S_N x - Px}_H \converges{N\to \infty } \to 0
.\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $M = \{x : Ux = x\}$ is a closed linear subspace, and $M^\perp = \overline{\mathrm{ran}(U - I)}$.
    <2>1. $M$ is a linear subspace: if $Ux = x$ and $Uy = y$ then $U(x + y) = x + y$ and $U(\alpha x) = \alpha x$.
        Proof: $U$ is linear.
    <2>2. $M$ is closed: if $x_n \in M$ and $x_n \to x$, then $Ux = \lim Ux_n = \lim x_n = x$.
        Proof: $U$ is continuous (bounded).
    <2>3. $M^\perp = \overline{\mathrm{ran}(U - I)}$: $x \perp M$ iff $x \in \overline{\mathrm{ran}(U - I)}$.
        Proof: $x \perp M$ iff $\langle x, y\rangle = 0$ for all $y \in M$ iff $x \perp \ker(U^* - I)$. Since $U$ is unitary, $U^* = U^{-1}$, and $\ker(U^* - I) = \ker(U^{-1} - I) = \ker(U - I) = M$. The orthogonal complement of $\ker(U - I)$ is $\overline{\mathrm{ran}((U - I)^*)} = \overline{\mathrm{ran}(U^{-1} - I)} = \overline{\mathrm{ran}(U - I)}$ (as $U^{-1} - I = U^{-1}(I - U)$, and $U^{-1}$ is bijective). Standard fact: for a bounded operator $T$, $\ker T^* = (\mathrm{ran}\,T)^\perp$.

<1>2. For $x \in M$: $S_N x = x$ for all $N$, so $S_N x \to x = Px$.
    Proof: $U^n x = x$ for all $n$; $S_N x = \frac{1}{N}\sum_{n=0}^{N-1} x = x$.

<1>3. For $x = Uy - y \in \mathrm{ran}(U - I)$: $\|S_N x\| \to 0$.
    <2>1. $S_N (U - I) = \frac{1}{N}(U^N - I)$ (telescoping sum).
        Proof: $S_N U - S_N = \frac{1}{N}\sum_{n=0}^{N-1}(U^{n+1} - U^n) = \frac{1}{N}(U^N - I)$.
    <2>2. $\|S_N (Uy - y)\| = \frac{1}{N}\|U^N y - y\| \le \frac{2\|y\|}{N} \to 0$.
        Proof: <2>1 and the unitarity of $U$ ($\|U^N\| = 1$).

<1>4. For $x \in M^\perp = \overline{\mathrm{ran}(U - I)}$: $\|S_N x\| \to 0$.
    Proof: given $\eps > 0$, choose $z = Uy - y$ with $\|x - z\| < \eps/2$ (density, <1>1); then $\|S_N x\| \le \|S_N (x - z)\| + \|S_N z\| \le \|x - z\| + \|S_N z\|$ (since $\|S_N\| \le 1$: $\frac1N\sum_{n<N}\|U^n\| = 1$) $< \eps/2 + \eps/2$ for $N$ large by <1>3.

<1>5. For general $x = Px + (x - Px)$ with $Px \in M$, $x - Px \in M^\perp$: $\|S_N x - Px\| = \|S_N(x - Px)\| \to 0$.
    Proof: <1>2 gives $S_N Px = Px$; <1>4 applies to $x - Px \in M^\perp$.

<1>6. Q.E.D.
    Proof: <1>5 is exactly $\|S_N x - Px\|_H \to 0$ for all $x \in H$. (This is the mean ergodic theorem of von Neumann.)
:::
