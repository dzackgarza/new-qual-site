---
schema: qual/card@1
id: E-SS10.PR-3
kind: problem
title: $S$ and $T_2$ generate the theta group
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
3. In this problem, consider the group $G$ of matrices $\left( \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right)$ with integer entries, determinant 1, and such that a and d have the same parity, b and c have the same parity, and c and d have opposite parity.
   This group also acts on the upper half-plane by fractional linear transformations.
   To the group $G$ corresponds the fundamental domain $\mathcal { F }$ defined by $| \tau | \geq 1 , | \mathrm { R e } ( \tau ) | \leq 1$ , and Im $. ( \tau ) \geq 0$ (see Figure 1). Also, let

$$
S (\tau) = - 1 / \tau \leftrightarrow \left( \begin{array}{c c} 0 & - 1 \\ 1 & 0 \end{array} \right) \quad \text { and } \quad T _ {2} (\tau) = \tau + 2 \leftrightarrow \left( \begin{array}{c c} 1 & 2 \\ 0 & 1 \end{array} \right).
$$

Prove that every fractional linear transformation corresponding to $g \in G$ is a composition of finitely many S, $T _ { 2 }$ and their inverses, in analogy with the previous problem.
:::

::: {.solution}
Let $G_0 = \langle S, T_2 \rangle$, and recall that for $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\in\operatorname{SL}_2(\ZZ)$ and $\tau\in\mathbb H$,
$$\Im(M\tau) = \frac{\Im\tau}{\abs{c\tau + d}^2}.$$
Put $\mathcal{F} = \{\tau \in \mathbb{H} : |\tau| \ge 1,\ |\Re\tau| \le 1\}$.

<1>1. $G_0 \subseteq G$.

::: {.proof}
For $S$: $a=d=0$ have the same parity, $b=-1$ and $c=1$ have the same parity, and $c=1$, $d=0$ have opposite parity. For $T_2$: $a=d=1$, $b=2$ and $c=0$ are even, and $c=0$, $d=1$ have opposite parity. Since $G$ is a group, it contains $\langle S,T_2\rangle$.
:::

<1>2. Every $G_0$-orbit in $\mathbb H$ meets $\mathcal F$.

::: {.proof}
Fix $\tau\in\mathbb H$. The numbers $c\tau+d$, for bottom rows $(c,d)$ of matrices in $G_0$, lie in the lattice $\ZZ\tau+\ZZ$ and are nonzero, so $\abs{c\tau+d}$ attains a positive minimum; hence some $\tau'$ in the orbit maximizes $\Im$ over the orbit. Choose $k\in\ZZ$ with $\tau'' = \tau' + 2k$ satisfying $|\Re\tau''| \le 1$; then $\Im\tau''=\Im\tau'$ is still maximal. If $|\tau''| < 1$, then $\Im(S\tau'') = \Im\tau''/|\tau''|^2 > \Im\tau''$, contradicting maximality. So $\tau''\in\mathcal F$.
:::

<1>3. If $h\in G$ and $h(2i)\in\mathcal F$, then $h(2i)=2i$.

::: {.proof}
For $M=\begin{pmatrix} a & b \\ c & d \end{pmatrix}\in G$, the entries $c$ and $d$ have opposite parity, so $\abs c\ne\abs d$; the same holds for the bottom row $(-c,a)$ of $M^{-1}$, since $a\equiv d$. For $\sigma=x+iy\in\mathcal F$ and such a bottom row with $c\ne0$,
$$\abs{c\sigma+d}^2=c^2\abs\sigma^2+2cdx+d^2\ge c^2-2\abs{cd}+d^2=(\abs c-\abs d)^2\ge1,\tag{$*$}$$
and the first inequality is strict when $\abs\sigma>1$ and $\abs x<1$.

Let $h=\begin{pmatrix} a & b \\ c & d \end{pmatrix}\in G$, $\tau=2i$, and $\tau'=h\tau\in\mathcal F$. If $\Im\tau'<\Im\tau$, then $\abs{-c\tau'+a}<1$ for the bottom row of $h^{-1}$; by $(*)$ this forces $c=0$, and then $a=\pm1$, a contradiction. So $\Im\tau'\ge\Im\tau$ and $\abs{c\tau+d}\le1$. Since $\abs\tau=2>1$ and $\Re\tau=0$, the strict form of $(*)$ excludes $c\ne0$. Hence $c=0$, $a=d=\pm1$, $b$ is even, and $\tau'=\tau\pm b$. As $\abs{\Re\tau'}\le1$ and $\Re\tau=0$, $\abs b\le1$, so $b=0$ and $\tau'=\tau$.
:::

<1>4. The only elements of $\operatorname{SL}_2(\ZZ)$ fixing $2i$ are $\pm I$.

::: {.proof}
If $\frac{2ia+b}{2ic+d}=2i$, then $2ia+b=-4c+2id$, so $d = a$ and $b = -4c$. Then $ad - bc = a^2 + 4c^2 = 1$ forces $c=0$, $b=0$, $a=d=\pm1$.
:::

<1>5. Q.E.D.

::: {.proof}
Let $g\in G$. By step <1>2 there is $\gamma\in G_0$ with $\gamma g(2i)\in\mathcal F$. By step <1>1, $\gamma g\in G$, so step <1>3 gives $\gamma g(2i)=2i$ and step <1>4 gives $\gamma g=\pm I$. Hence the transformation $g$ equals $\gamma^{-1}$, a finite composition of $S$, $T_2$, and their inverses.
:::
:::
