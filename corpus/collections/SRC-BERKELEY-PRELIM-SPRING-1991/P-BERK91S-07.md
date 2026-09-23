---
schema: qual/card@1
id: P-BERK91S-07
kind: problem
title: Schwarz-type bound for a disk map with zeros at $0$ and $\pm r$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the bound on f, the three prescribed zeros, and the rational factor in the conclusion with Problem 7 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f$ be analytic in the unit disk with
$$
\abs{f(z)}\le1,
\qquad f(0)=0.
$$
Suppose there is $r\in(0,1)$ such that
$$
f(r)=f(-r)=0.
$$
Prove that
$$
\abs{f(z)}
\le
\abs{z}\abs{\frac{z^2-r^2}{1-r^2z^2}}.
$$
:::

::: {.hint}
For $a\in(-1,1)$, set $b_a(z)\coloneqq(z-a)/(1-az)$ on the unit disk.
Schwarz's lemma applied after precomposition with the inverse of $b_a$
gives $\abs{h(z)}\le\abs{b_a(z)}$ whenever $h$ is analytic on the unit
disk, $\abs{h}\le1$, and $h(a)=0$.
Divide $f$ successively by $b_0(z)=z$, $b_r(z)$, and $b_{-r}(z)$.
Each quotient extends analytically at the removed zero, and this estimate
keeps its modulus at most $1$. The product of the factors is
$$
b_0(z)b_r(z)b_{-r}(z)
=z\frac{z^2-r^2}{1-r^2z^2}.
$$
:::

::: {.solution}
Write $\DD\coloneqq\{z\in\CC:\abs{z}<1\}$. For $a\in(-1,1)$,
let $b_a:\DD\to\DD$ be the disk automorphism
$$
b_a(z)\coloneqq\frac{z-a}{1-az},
\qquad
b_a^{-1}(w)=\frac{w+a}{1+aw}.
$$
These are the [[PR-ULJAJ|Blaschke-factor automorphisms]], with the
opposite sign convention. In particular, $b_a(a)=0$, and $a$ is the
only zero of $b_a$ in $\DD$.

<1>1. If $h:\DD\to\CC$ is analytic, $\abs{h}\le1$, and $h(a)=0$
for $a\in(-1,1)$, then $h/b_a$ extends analytically to $\DD$ and its
extension has modulus at most $1$.

::: {.proof}
For $0<t<1$, define $H_t:\DD\to\DD$ by
$H_t(w)\coloneqq t h(b_a^{-1}(w))$. This function is analytic and
$H_t(0)=t h(a)=0$. The [[T-DAETF|Schwarz lemma]] gives
$\abs{H_t(w)}\le\abs{w}$. Substituting $w=b_a(z)$ and letting
$t\to1$ yields
$$
\abs{h(z)}\le\abs{b_a(z)}
\qquad(z\in\DD).
$$
Thus $\abs{h(z)/b_a(z)}\le1$ for $z\ne a$.

Since $h(a)=0$, its Taylor expansion at $a$ gives an analytic function
$u$ near $a$ such that $h(z)=(z-a)u(z)$. On that punctured neighborhood,
$$
\frac{h(z)}{b_a(z)}=(1-az)u(z).
$$
This formula supplies an analytic extension at $a$, with value
$(1-a^2)h'(a)$. The modulus bound at $a$ follows by continuity.
:::

<1>2. There is an analytic function $q_3:\DD\to\CC$ with
$\abs{q_3}\le1$ such that $f=b_0b_rb_{-r}q_3$ on $\DD$.

::: {.proof}
Apply step <1>1 to $h=f$ and $a=0$, and let $q_1$ be the analytic
extension of $f/b_0=f/z$. Then $\abs{q_1}\le1$ and
$$
q_1(r)=\frac{f(r)}r=0,
\qquad
q_1(-r)=\frac{f(-r)}{-r}=0,
$$
because $r\ne0$.

Apply step <1>1 to $h=q_1$ and $a=r$, and let $q_2$ be the analytic
extension of $q_1/b_r$. Then $\abs{q_2}\le1$. Since
$$
b_r(-r)=\frac{-2r}{1+r^2}\ne0,
$$
the quotient satisfies $q_2(-r)=q_1(-r)/b_r(-r)=0$.

Apply step <1>1 to $h=q_2$ and $a=-r$, and let $q_3$ be the analytic
extension of $q_2/b_{-r}$. Then $\abs{q_3}\le1$. The identities
$f=b_0q_1$, $q_1=b_rq_2$, and $q_2=b_{-r}q_3$ hold away from their
respective removed zeros and extend there by continuity. Multiplying
them gives $f=b_0b_rb_{-r}q_3$ throughout $\DD$.
:::

<1>3. For every $z\in\DD$,
$\abs{f(z)}\le\abs{z}\abs{(z^2-r^2)/(1-r^2z^2)}$.

::: {.proof}
By step <1>2,
$$
\begin{aligned}
\abs{f(z)}
&\le\abs{b_0(z)b_r(z)b_{-r}(z)}\\
&=\abs{z\frac{z-r}{1-rz}\frac{z+r}{1+rz}}\\
&=\abs{z}\abs{\frac{z^2-r^2}{1-r^2z^2}}.
\end{aligned}
$$
The denominators are nonzero on $\DD$, since $0<r<1$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the asserted bound on the entire unit disk.
:::
:::
