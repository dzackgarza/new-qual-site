---
schema: qual/card@1
id: E-SS8.PR-7
kind: problem
title: Koebe's construction of a Riemann map
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 8, §3, problem 7, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a)--(e) and the hint. The defect the card's remark records in part (d) — that
    $\psi_\alpha(0)=\alpha\ne0$, so no square root of $\psi_\alpha$ can vanish at $0$, and that $S$
    must be defined on $\psi_\alpha(K)$ — was confirmed against the print and is used below in the
    corrected reading $S(w)^2=w$ on $\psi_\alpha(K)$ with $S(\alpha)=\beta$, under which the printed
    formula $\abs{f'(0)}=(1+r_K)/(2\sqrt{r_K})$ is exactly correct.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All five parts. (a) $\abs{f'(0)}>1$ by the maximum principle applied to $1/(f(z)/z)$, and
    $r_{f(K)}\ge r_K$ by Rouché on $\abs\zeta=\rho$ using $\abs{f(\zeta)}>\rho\ge\abs z$. (b) the
    derivative product by the chain rule and the bound $F_n'(0)\le1/\abs{\varphi'(0)}$ from the
    Schwarz lemma with the Riemann map $\varphi$ of $K_0$, which gives $\abs{f_n'(0)}\to1$. (c)
    Montel and Hurwitz for the limit, the inverse-limit argument with the identity
    $\operatorname{int}(\overline{K_0})=K_0$ for surjectivity, and uniqueness of the limit through
    automorphisms of $\DD$ fixing $0$ with derivative $1$. (d) the square root on $\psi_\alpha(K)$ and
    the Schwarz lemma applied to the extension $\Phi=\psi_\alpha\circ(\cdot)^2\circ\psi_\beta$ of
    $f^{-1}$ to $\DD$, with the derivative computed. (e) the iteration with $r_{K_n}\to1$. Nothing is
    left in outline.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read against the printed item, Chapter 8, Problem 7, which begins on printed p. 258 (PDF p. 277)
    and ends on p. 259 (PDF p. 278): parts (a)--(e), the paragraph defining $F_n=f_n\circ\cdots\circ f_0$,
    the paragraph introducing $\psi_\alpha=(\alpha-z)/(1-\overline\alpha z)$, and the printed data
    $\abs{f'(0)}=(1+r_K)/(2\sqrt{r_K})$. The asterisk the print sets before "7." is recorded in the
    remark. The defect the remark records was re-read in the print: part (d) does ask for a square
    root $S$ of $\psi_\alpha$ with $S(0)=0$, and $\psi_\alpha(0)=\alpha\ne0$. Not checked: the
    argument, which this pass did not re-derive.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step s5 on the reader's report. The step proved $F(K_0)\supseteq\DD$ through the
    identity $\operatorname{int}(\overline{K_0})=K_0$, which is false for a general Koebe domain:
    $K_0=\DD\setminus[1/2,1)$ is simply connected, proper, contains $0$, and has closure the closed
    disc, whose interior is $\DD$. The step now argues by Hurwitz's theorem instead: for every
    $\rho<1$ and all large $n$ the set $D(0,\rho)$ lies in $F_n(K_0)$, so $F_n-w$ has a zero in
    $K_0$ for each $w\in D(0,\rho)$; since $F_n\to F$ locally uniformly and $F-w$ is not identically
    zero, $F-w$ must have a zero as well, whence $\DD\subseteq F(K_0)$. The inverse family, Montel's
    theorem and the appeal to $\operatorname{int}(\overline{K_0})$ are removed, and no other step
    depends on them. Not checked in this pass: steps s1--s4 and s6--s7 beyond step s4's
    $F'(0)=L>0$, which the new argument uses.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    The Hurwitz repair of this step, recorded above, did not close the gap, and is replaced on a
    referee's report of this session. Hurwitz's theorem gives zero-freeness on compact subsets of
    $K_0$, not on $K_0$ itself, and the zeros $F_n^{-1}(w)$ are confined only to
    $K_0\cap\overline{D(0,\abs w)}$, whose closure meets $\partial K_0$; they can escape to the
    boundary, as the disc automorphisms $(z-p_n)/(1-\overline{p_n}z)$ with $p_n\to\partial\DD$ show.
    The step now works on the decreasing domains $U_n=F_n^{-1}(D(0,\rho'))$, whose closures lie in
    the fixed compact $\overline{U_N}\subseteq K_0$ by the expansion property, and transfers the zero
    of $F_{n_j}-w$ to $F-w$ by Rouché's theorem on $\partial U_{n_j}$, where
    $\abs{F_{n_j}-w}\ge\rho'-\rho>\abs{F-F_{n_j}}$. This is the printed hint's route, $r_{F(K_0)}\ge1$,
    and it uses neither simple connectivity of $K_0$ nor $\operatorname{int}(\overline{K_0})$.

---

::: {.exercise}
A *Koebe domain* is a simply connected proper subdomain $K$ of the unit disc $\DD$ containing $0$. Its inner radius is $r_K=\sup\{\rho\geq0:D(0,\rho)\subset K\}$. A holomorphic injection $f:K\to\DD$ is an *expansion* if $f(0)=0$ and $\abs{f(z)}>\abs z$ for $z\in K\setminus\{0\}$.

(a) Prove that an expansion satisfies $r_{f(K)}\geq r_K$ and $\abs{f'(0)}>1$.

Suppose $K_0$ is a Koebe domain and $f_n:K_n\to K_{n+1}$ are expansions, where $K_{n+1}=f_n(K_n)$. Set $F_n=f_n\circ\cdots\circ f_0:K_0\to\DD$.

(b) Prove that each $F_n$ is an expansion, that $F_n'(0)=\prod_{k=0}^{n}f_k'(0)$, and that $\lim_{n\to\infty}\abs{f_n'(0)}=1$.

(c) Show that if $r_{K_n}\to1$, then $F_n$ converges uniformly on compact subsets of $K_0$ to a conformal map $F:K_0\to\DD$.

For $\alpha\in\DD$, write $\psi_\alpha(z)=(\alpha-z)/(1-\overline\alpha z)$.

(d) Given a Koebe domain $K$, choose $\alpha\in\partial K\cap\DD$ with $\abs{\alpha}=r_K$ and $\beta\in\DD$ with $\beta^2=\alpha$. Let $S$ denote the square root of $\psi_\alpha$ on $K$ such that $S(0)=0$. Why is it well defined? Prove that $f=\psi_\beta\circ S\circ\psi_\alpha:K\to\DD$ is an expansion and that $\abs{f'(0)}=(1+r_K)/(2\sqrt{r_K})$.

(e) Use (d) to construct a sequence with $r_{K_n}\to1$.
:::

::: {.hint}
For (a), write $f(z)=zg(z)$ and use the maximum principle. For (b), use the Schwarz lemma. For (c), show that $r_{F(K_0)}\geq1$. For (d), apply the Schwarz lemma to the inverse map, expressed using $\psi_\alpha$, $\psi_\beta$, and $z\mapsto z^2$.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 8, Problem 7, printed pp. 258--259). Part (d) is inconsistent as printed: $\psi_\alpha(0)=\alpha\neq0$, so a square root of $\psi_\alpha$ cannot satisfy $S(0)=0$. The composition also requires $S$ to be defined on $\psi_\alpha(K)$. A coherent choice is a square root on $\psi_\alpha(K)$ with $S(\alpha)=\beta$.
:::

::: {.solution}
No published solution set covers the end-of-chapter Problems of Stein--Shakarchi: the set of R. C. Rhoades, *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), covers a selection of the chapter Exercises and not the Problems, and no other set was located. The argument is the card's own, following the book's hints.

Throughout $K$ is a Koebe domain, $r_K=\sup\{\rho:D(0,\rho)\subseteq K\}$, and $f:K\to\DD$ is an expansion: $f(0)=0$ and $\abs{f(z)}>\abs z$ for $z\in K\setminus\{0\}$.

::: pf

::: {.pf-step #s1}

Part (a), first claim: $\abs{f'(0)}>1$.

::: pf-proof

The function $g(z)=f(z)/z$ is holomorphic and non-vanishing on $K$ with $g(0)=f'(0)\ne0$ and $\abs{g(z)}>1$ for $z\ne0$. If $\abs{f'(0)}\le1$ then $1/g$ is holomorphic on $K$ with $\abs{1/g(z)}<1$ for $z\ne0$ and $\abs{1/g(0)}=1/\abs{f'(0)}\ge1$, so $\abs{1/g}$ has a maximum at the interior point $0$; by the maximum modulus principle $1/g$ is constant, contradicting the strict inequality off $0$. Hence $\abs{f'(0)}>1$.

:::

:::

::: {.pf-step #s2}

Part (a), second claim: $r_{f(K)}\ge r_K$.

::: pf-proof

Let $0<\rho<r_K$, so that $D(0,\rho)\subseteq K$. For $\abs\zeta=\rho$ we have $\zeta\in K$ and
$$
\abs{f(\zeta)}>\abs\zeta=\rho .
$$
Fix $z$ with $\abs z\le\rho$. On the circle $\abs\zeta=\rho$ the function $f$ therefore dominates the constant $-z$, since $\abs{f(\zeta)}>\rho\ge\abs z=\abs{-z}$. By Rouché's theorem applied on $D(0,\rho)$, the functions $f$ and $f-z$ have the same number of zeros in $D(0,\rho)$; $f$ has exactly one, at $0$, because $f$ is injective and $f(0)=0$. So $f-z$ has a zero in $D(0,\rho)$, that is, $z\in f(D(0,\rho))\subseteq f(K)$.

Hence $D(0,\rho)\subseteq f(K)$ for every $\rho<r_K$, so $r_{f(K)}\ge r_K$.

:::

:::

::: {.pf-step #s3}

Part (b): each $F_n=f_n\circ\cdots\circ f_0$ is an expansion, $F_n'(0)=\prod_{k=0}^{n}f_k'(0)$, and $\abs{f_n'(0)}\to1$.

::: pf-proof

A composition of expansions is an expansion: if $g:K\to K'$ and $h:K'\to\DD$ are expansions then $\abs{h(g(z))}>\abs{g(z)}>\abs z$ for $z\ne0$. By induction each $F_n:K_0\to K_{n+1}$ is an expansion, and $F_n(0)=0$.

The chain rule gives $F_n'(0)=\prod_{k=0}^{n}f_k'(0)$.

For the bound, let $\varphi:\DD\to K_0$ be a Riemann map with $\varphi(0)=0$, which exists because $K_0$ is simply connected and proper. Then $F_n\circ\varphi:\DD\to\DD$ is holomorphic with $F_n(\varphi(0))=0$, so by the Schwarz lemma
$$
P_n\abs{\varphi'(0)}=\abs{(F_n\circ\varphi)'(0)}\le1,
\qquad P_n:=\prod_{k=0}^{n}\abs{f_k'(0)} .
$$
So $(P_n)$ is a nondecreasing sequence, each factor exceeding $1$ by step [](#s1){.pf-ref}, bounded above by $1/\abs{\varphi'(0)}$; it converges to some $L\in(1,\infty)$. Hence
$$
\abs{f_n'(0)}=\frac{P_n}{P_{n-1}}\longrightarrow\frac LL=1 .
$$

:::

:::

::: {.pf-step #s4}

Part (c), first part: a subsequence of $(F_n)$ converges uniformly on compact subsets of $K_0$ to a holomorphic injection $F$ with $F(0)=0$ and $F'(0)=L>0$.

::: pf-proof

Each $F_n$ maps $K_0$ into $K_{n+1}\subseteq\DD$, so $\abs{F_n}<1$ on $K_0$ and $(F_n)$ is a normal family by Montel's theorem; some subsequence $F_{n_k}$ converges uniformly on compact subsets of $K_0$ to a holomorphic $F$. Then $F(0)=0$ and
$$
F'(0)=\lim_kF_{n_k}'(0)=\lim_kP_{n_k}=L>0
$$
by Weierstrass's theorem on derivatives, using step [](#s3){.pf-ref}. In particular $F$ is not constant; since each $F_{n_k}$ is injective, Hurwitz's theorem gives that $F$ is injective.

:::

:::

::: {.pf-step #s5}

Part (c), second part: every subsequential limit $F$ of step [](#s4){.pf-ref} satisfies $r_{F(K_0)}\ge1$, hence $F(K_0)=\DD$.

::: pf-proof

Let $F_{n_j}\to F$ be the subsequence of step [](#s4){.pf-ref}. Fix $\rho$ with $0<\rho<1$ and choose $\rho',\rho''$ with $\rho<\rho'<\rho''<1$. Since $r_{K_{n+1}}\to1$, there is $N$ such that $D(0,\rho'')\subseteq K_{n+1}$ for every $n\ge N$; for such $n$ put
$$
U_n:=F_n^{-1}\bigl(D(0,\rho')\bigr).
$$
Because $F_n:K_0\to K_{n+1}$ is a biholomorphism, $U_n$ is a domain and $F_n$ restricts to a biholomorphism of $U_n$ onto $D(0,\rho')$; hence $\partial U_n=F_n^{-1}(\{\abs\zeta=\rho'\})$ is an analytic Jordan curve on which $\abs{F_n}=\rho'$, and
$$
\overline{U_n}=F_n^{-1}\bigl(\overline{D(0,\rho')}\bigr)\subseteq F_n^{-1}\bigl(D(0,\rho'')\bigr)\subseteq K_0,
$$
so $\overline{U_n}$ is compact and lies in the open subset $F_n^{-1}(D(0,\rho''))$ of $K_0$.

The domains $U_n$ decrease in $n$. For $m<n$ the composite $f_n\circ\cdots\circ f_{m+1}:K_{m+1}\to K_{n+1}$ is an expansion, like any composite of expansions in step [](#s3){.pf-ref}, and $F_n=(f_n\circ\cdots\circ f_{m+1})\circ F_m$; since $F_m$ is injective with $F_m(0)=0$, so that $F_m(z)\ne0$ for $z\in K_0\setminus\{0\}$,
$$
\abs{F_n(z)}>\abs{F_m(z)},\qquad z\in K_0\setminus\{0\},
$$
which gives $U_n\subseteq U_m$. In particular $\overline{U_{n_j}}\subseteq\overline{U_N}$ for every $j$ with $n_j\ge N$, and $\overline{U_N}$ is a fixed compact subset of $K_0$.

Fix $w$ with $\abs w<\rho$. By step [](#s4){.pf-ref} the subsequence converges to $F$ uniformly on the compact set $\overline{U_N}\subseteq K_0$, so $j$ can be chosen with $n_j\ge N$ and
$$
\sup_{z\in\overline{U_N}}\abs{F(z)-F_{n_j}(z)}<\rho'-\rho .
$$
For $z\in\partial U_{n_j}$ this gives, with $\abs{F_{n_j}(z)}=\rho'$,
$$
\abs{F_{n_j}(z)-w}\ge\abs{F_{n_j}(z)}-\abs w\ge\rho'-\rho>\abs{F(z)-F_{n_j}(z)} .
$$
The functions $F-w$ and $F_{n_j}-w$ are holomorphic on the open set $K_0$, which contains $\overline{U_{n_j}}$, so Rouché's theorem on the bounded domain $U_{n_j}$ — in the form that holomorphic $g,h$ on a neighbourhood of $\overline U$ with $\abs{g-h}<\abs h$ on $\partial U$ have equally many zeros in $U$ — gives that $F-w$ and $F_{n_j}-w$ have equally many zeros in $U_{n_j}$. The function $F_{n_j}-w$ has exactly one, at $F_{n_j}^{-1}(w)$, which lies in $U_{n_j}$ because $w\in D(0,\rho)\subseteq D(0,\rho')=F_{n_j}(U_{n_j})$ and $F_{n_j}$ is injective. Hence $F-w$ has a zero in $U_{n_j}\subseteq K_0$, that is, $w\in F(K_0)$.

Since $\rho<1$ was arbitrary, $D(0,\rho)\subseteq F(K_0)$ for every $\rho<1$, which is $r_{F(K_0)}\ge1$. The reverse inclusion $F(K_0)\subseteq\DD$ holds because $F$ takes its values in $\DD$, so $F(K_0)=\DD$.

:::

:::

::: {.pf-step #s6}

Part (c), conclusion: the whole sequence $(F_n)$ converges uniformly on compact subsets of $K_0$ to a conformal map $F:K_0\to\DD$.

::: pf-proof

By steps [](#s4){.pf-ref} and [](#s5){.pf-ref} every subsequential limit of $(F_n)$ is a conformal map of $K_0$ onto $\DD$ with $F(0)=0$ and $F'(0)=L$.

If $F$ and $G$ are two such limits, then $G^{-1}\circ F$ is a conformal automorphism of $K_0$ fixing $0$ with derivative $F'(0)/G'(0)=1$. Composing with a Riemann map $\varphi:\DD\to K_0$ with $\varphi(0)=0$, the map $\varphi^{-1}\circ G^{-1}\circ F\circ\varphi$ is an automorphism of $\DD$ fixing $0$ with derivative $1$, hence the identity, since the automorphisms of $\DD$ fixing $0$ are the rotations $z\mapsto e^{i\theta}z$ and the derivative there is $e^{i\theta}$. So $F=G$: the limit is unique, and a normal family with a unique limit converges to it.

This $F$ is the conformal map promised in part (c), and it is onto $\DD$.

:::

:::

::: {.pf-step #s7}

Part (d): with $\alpha\in\partial K\cap\DD$, $\abs\alpha=r_K=r$, and $\beta\in\DD$ with $\beta^2=\alpha$, the branch $S$ of the square root on $\psi_\alpha(K)$ with $S(\alpha)=\beta$ is well defined; $f=\psi_\beta\circ S\circ\psi_\alpha$ is an expansion with $\abs{f'(0)}=\dfrac{1+r}{2\sqrt r}$.

::: pf-proof

*Well defined.* $\psi_\alpha$ is an automorphism of $\DD$, so $\psi_\alpha(K)$ is a simply connected domain. Also $0\notin\psi_\alpha(K)$, because $0=\psi_\alpha(\alpha)$ and $\alpha\notin K$ while $\psi_\alpha$ is injective. A non-vanishing holomorphic function on a simply connected domain has a holomorphic square root, unique up to sign; the two branches are interchanged by $w\mapsto-w$, so exactly one satisfies $S(\alpha)=\beta$.

Note the correction this requires: the printed part (d) asks for a square root of $\psi_\alpha$ with $S(0)=0$, which is impossible since $\psi_\alpha(0)=\alpha\ne0$. The identity $S(w)^2=w$ on $\psi_\alpha(K)$ is what the printed composition $f=\psi_\beta\circ S\circ\psi_\alpha$ uses, and with it the printed value of $\abs{f'(0)}$ below is exactly right.

*The derivative.* Since $S(w)^2=w$ one has $S'(\alpha)=1/(2\beta)$, and
$$
\psi_\alpha'(z)=\frac{\abs\alpha^2-1}{(1-\bar\alpha z)^2},\qquad
\psi_\beta'(\beta)=\frac{\abs\beta^2-1}{(1-\abs\beta^2)^2}=-\frac1{1-\abs\beta^2},
$$
with $\abs\beta^2=\abs\alpha=r$. By the chain rule, using $\psi_\alpha(0)=\alpha$ and $S(\alpha)=\beta$,
$$
f'(0)=\psi_\beta'(S(\psi_\alpha(0)))\,S'(\psi_\alpha(0))\,\psi_\alpha'(0)
=-\frac1{1-\abs\beta^2}\cdot\frac1{2\beta}\cdot(r^2-1)
=\frac{1+r}{2\beta},
$$
so $\abs{f'(0)}=\dfrac{1+r}{2\abs\beta}=\dfrac{1+r}{2\sqrt r}$.

*$f$ is an expansion.* Observe that
$$
\Phi:=\psi_\alpha\circ(\cdot)^2\circ\psi_\beta:\DD\longrightarrow\DD
$$
is holomorphic, and $\Phi(0)=\psi_\alpha(\psi_\beta(0)^2)=\psi_\alpha(\beta^2)=\psi_\alpha(\alpha)=0$. On $f(K)$ it agrees with $f^{-1}$: for $u\in f(K)$ write $u=\psi_\beta(S(\psi_\alpha(z)))$ with $z\in K$, so $\psi_\beta(u)=S(\psi_\alpha(z))$, hence $\psi_\beta(u)^2=\psi_\alpha(z)$ and $\Phi(u)=\psi_\alpha(\psi_\alpha(z))=z$. Also $f(0)=\psi_\beta(S(\alpha))=\psi_\beta(\beta)=0$.

By the Schwarz lemma, $\abs{\Phi(u)}\le\abs u$ on $\DD$, and $\Phi$ is not a rotation (it is a composition of two automorphisms with the squaring map), so $\abs{\Phi(u)}<\abs u$ for $u\ne0$. For $z\in K\setminus\{0\}$ put $u=f(z)\ne0$; then
$$
\abs z=\abs{\Phi(u)}<\abs u=\abs{f(z)} .
$$

:::

:::

::: {.pf-step #s8}

Part (e): iterating part (d) produces a sequence of expansions with $r_{K_n}\to1$.

::: pf-proof

Let $K_n$ be a Koebe domain with $r_n=r_{K_n}<1$. As shown in the preamble below, there is $\alpha_n\in\partial K_n\cap\DD$ with $\abs{\alpha_n}=r_n$. Part [](#s7){.pf-ref} applied to $K_n$ and $\alpha_n$ produces an expansion $f_n:K_n\to\DD$ with
$$
K_{n+1}:=f_n(K_n),\qquad \abs{f_n'(0)}=\frac{1+r_n}{2\sqrt{r_n}}=:G(r_n).
$$
The function $G(r)=(1+r)/(2\sqrt r)$ satisfies $G(1)=1$ and $G(r)>1$ for $r\ne1$; it is continuous and strictly decreasing on $(0,1)$. By part [](#s3){.pf-ref} applied to the resulting sequence of expansions, $\abs{f_n'(0)}=G(r_n)\to1$, hence $r_n\to1$.

*Existence of $\alpha_n$.* Since $D(0,\rho)\subseteq K_n$ for every $\rho<r_n$, the union gives $D(0,r_n)\subseteq K_n$. If the whole circle $\{\abs z=r_n\}$ lay in $K_n$, then by openness and compactness of that circle an annulus $\{r_n-\delta\le\abs z\le r_n+\delta\}$ would lie in $K_n$, giving $D(0,r_n+\delta)\subseteq K_n$ and contradicting the definition of $r_n$. So some point of the circle of radius $r_n$ lies outside $K_n$, and by radial continuity some point of that circle lies on $\partial K_n$; take it as $\alpha_n$. (If $r_n=1$ then $K_n=\DD$, which is excluded because $K_n$ is a proper subdomain, so always $r_n<1$.)

:::

:::

:::

:::
