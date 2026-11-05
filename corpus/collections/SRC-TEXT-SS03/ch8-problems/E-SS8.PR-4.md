---
schema: qual/card@1
id: E-SS8.PR-4
kind: problem
title: SU(1,1) and automorphisms of the unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Mappings
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 8, §3, problem 4, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a) and (b) and the hint; nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) the isometry condition is exactly $M^*JM=J$, so $M^*=JM^{-1}J$, and comparing with
    $M^*=\overline{M}^{\,t}$ gives $d=\bar a$, $c=\bar b$; the norm identity follows. (b) the
    associated Möbius map preserves the disc because $\abs{\bar bz+\bar a}^2-\abs{az+b}^2=(\abs a^2-\abs b^2)(1-\abs z^2)$;
    the kernel is $\pm I$; and surjectivity uses the book's normal form of a disc automorphism with
    the hint's matrix, which is checked to lie in $\mathrm{SU}(1,1)$ and to induce it. Nothing is left
    in outline.
---

::: {.exercise}
Let $\mathrm{SU}(1,1)$ be the group of matrices $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with complex entries, determinant $1$, and
$$
\inner{MZ}{MW}=\inner{Z}{W},\qquad
\inner{Z}{W}=z_1\overline{w_1}-z_2\overline{w_2}
$$
for all $Z,W\in\CC^2$.

(a) Prove that every matrix in $\mathrm{SU}(1,1)$ has the form
$$
\begin{pmatrix}a&b\\\overline b&\overline a\end{pmatrix},
\qquad \abs{a}^2-\abs{b}^2=1.
$$
Use $J=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ and $\inner{Z}{W}={}^t\overline{W}JZ$, where ${}^t\overline{W}$ denotes the conjugate transpose of $W$.

(b) Associate to $M$ the fractional linear map $z\mapsto(az+b)/(cz+d)$. Prove that $\mathrm{SU}(1,1)/\{\pm I\}$ is isomorphic to the group of automorphisms of the unit disc.
:::

::: {.hint}
In (b), associate $e^{2i\theta}(z-\alpha)/(1-\overline\alpha z)$ with
$$
\frac{1}{\sqrt{1-\abs{\alpha}^2}}
\begin{pmatrix}
e^{i\theta}&-\alpha e^{i\theta}\\
-\overline\alpha e^{-i\theta}&e^{-i\theta}
\end{pmatrix}.
$$
:::

::: {.solution}

Write $\langle Z,W\rangle=z_1\overline{w_1}-z_2\overline{w_2}=\overline W^{\,t}JZ$ with $J=\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$, and let $D$ be the unit disc.

::: pf

::: {.pf-step #s1}

The condition $\langle MZ,MW\rangle=\langle Z,W\rangle$ for all $Z,W$ is equivalent to $M^*JM=J$, where $M^*=\overline M^{\,t}$.

::: pf-proof

$\langle MZ,MW\rangle=\overline{MW}^{\,t}JMZ=\overline W^{\,t}M^*JMZ$. This equals $\overline W^{\,t}JZ$ for all $Z,W$ exactly when $M^*JM=J$: choosing $W,Z$ running over the standard basis, the two hermitian matrices $M^*JM$ and $J$ have equal entries, and conversely if $M^*JM=J$ the equality holds for all $Z,W$.

:::

:::

::: {.pf-step #s2}

Part (a): if $M\in\mathrm{SU}(1,1)$ then $M=\bigl(\begin{smallmatrix}a&b\\ \bar b&\bar a\end{smallmatrix}\bigr)$ with $\abs a^2-\abs b^2=1$.

::: pf-proof

Let $M=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ have determinant $1$. From $M^*JM=J$ one gets $M^*=JM^{-1}J$, since $J^{-1}=J$.

As $\det M=1$, $M^{-1}=\bigl(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\bigr)$, so
$$
JM^{-1}J=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}
=\begin{pmatrix}d&b\\c&a\end{pmatrix}.
$$
Comparing with $M^*=\overline M^{\,t}=\bigl(\begin{smallmatrix}\bar a&\bar c\\ \bar b&\bar d\end{smallmatrix}\bigr)$ gives
$$
\bar a=d,\qquad \bar c=b,\qquad \bar b=c,\qquad \bar d=a .
$$
The middle two are the same relation, so $c=\bar b$ and $d=\bar a$; the last two are also compatible with these. Hence $M=\bigl(\begin{smallmatrix}a&b\\ \bar b&\bar a\end{smallmatrix}\bigr)$ with $\det M=\abs a^2-\abs b^2=1$.

Conversely, a matrix of this form with $\abs a^2-\abs b^2=1$ satisfies $M^*JM=J$: the diagonal entries are $\abs a^2-\abs b^2=1$ and $\abs b^2-\abs a^2=-1$, and the off-diagonal entry is $\bar ab-\bar ba=0$.

:::

:::

::: {.pf-step #s3}

Part (b), the map is well defined and faithful: $M\mapsto f_M$, $f_M(z)=\dfrac{az+b}{\bar bz+\bar a}$, carries $\mathrm{SU}(1,1)$ homomorphically into the automorphisms of $D$, with kernel $\{\pm I\}$.

::: pf-proof

The denominator $\bar bz+\bar a$ does not vanish on $D$: if $\bar bz=-\bar a$ with $\abs z<1$ then $\abs a=\abs b\abs z<\abs b\le\abs a$, since $\abs a^2-\abs b^2=1$ forces $\abs a>\abs b$. So $f_M$ is holomorphic on a neighbourhood of $\overline D$. Moreover, for $\abs z<1$,
$$
\abs{\bar bz+\bar a}^2-\abs{az+b}^2
=\bigl(\abs b^2\abs z^2+2\operatorname{Re}(a\bar bz)+\abs a^2\bigr)-\bigl(\abs a^2\abs z^2+2\operatorname{Re}(a\bar bz)+\abs b^2\bigr)
=\bigl(\abs a^2-\abs b^2\bigr)\bigl(1-\abs z^2\bigr)>0,
$$
so $\abs{f_M(z)}<1$: the disc is mapped into itself. Composing such maps corresponds to multiplying the matrices, so $M\mapsto f_M$ is a homomorphism, and $f_{M^{-1}}$ is inverse to $f_M$ because $M^{-1}$ has the same form; hence each $f_M$ is an automorphism of $D$.

If $f_M=\mathrm{id}$ then $az+b=z(\bar bz+\bar a)$ for all $z$, so $\bar b=0$, $a=\bar a$ and $b=0$; then $\abs a^2=1$, so $a=\pm1$ and $M=\pm I$. Thus the kernel is exactly $\{\pm I\}$ and $\mathrm{SU}(1,1)/\{\pm I\}$ injects into $\operatorname{Aut}(D)$.

:::

:::

::: {.pf-step #s4}

Every automorphism of $D$ is some $f_M$, so $\mathrm{SU}(1,1)/\{\pm I\}\cong\operatorname{Aut}(D)$.

::: pf-proof

By the normal form of disc automorphisms (Chapter 8), every $f\in\operatorname{Aut}(D)$ is
$$
f(z)=e^{2i\theta}\,\frac{z-\alpha}{1-\bar\alpha z}
\qquad\text{with } \abs\alpha<1,\ \theta\in\RR .
$$
For such $\alpha,\theta$ put
$$
M=\frac{1}{\sqrt{1-\abs\alpha^2}}
\begin{pmatrix} e^{i\theta} & -\alpha e^{i\theta}\\ -\bar\alpha e^{-i\theta} & e^{-i\theta}\end{pmatrix},
\qquad a=\frac{e^{i\theta}}{\sqrt{1-\abs\alpha^2}},\quad b=\frac{-\alpha e^{i\theta}}{\sqrt{1-\abs\alpha^2}} .
$$
Then $d=e^{-i\theta}/\sqrt{1-\abs\alpha^2}=\bar a$ and $c=-\bar\alpha e^{-i\theta}/\sqrt{1-\abs\alpha^2}=\bar b$, so $M$ has the form of part (a); and
$$
\det M=\frac{1}{1-\abs\alpha^2}\bigl(e^{i\theta}e^{-i\theta}-\abs\alpha^2e^{i\theta}e^{-i\theta}\bigr)=1,\qquad
\abs a^2-\abs b^2=\frac{1-\abs\alpha^2}{1-\abs\alpha^2}=1 .
$$
So $M\in\mathrm{SU}(1,1)$. Its fractional linear map is
$$
\frac{az+b}{cz+d}=\frac{e^{i\theta}(z-\alpha)}{e^{-i\theta}(1-\bar\alpha z)}=e^{2i\theta}\frac{z-\alpha}{1-\bar\alpha z}=f(z),
$$
so $f_M=f$. Hence the map is surjective, and with step [](#s3){.pf-ref} it induces an isomorphism $\mathrm{SU}(1,1)/\{\pm I\}\to\operatorname{Aut}(D)$.

:::

:::

:::

:::
